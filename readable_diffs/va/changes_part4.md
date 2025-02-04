# Change History for va.json (Part 4)

### Changes from 31606f9 to dd2190f (Part 4/7)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset contains the data about staffing for Nurses, Physicians, and other Healthcare Professionals.</p>",
-            "title": "Veterans Health Administration 2008 Hospital Report Card - Medical Center Staffing",
-            "isPartOf": "VA-VHA-OIA-583",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset contains the data about staffing for Nurses, Physicians, and other Healthcare Professionals.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41726,49 +41702,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fd22-twij/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fd22-twij/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fd22-twij/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/fd22-twij/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fd22-twij/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fd22-twij/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fd22-twij/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fd22-twij/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fd22-twij/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-027",
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
+            "landingPage": "https://www.data.va.gov/d/fd22-twij",
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
+            "title": "Veterans Health Administration 2008 Hospital Report Card - Medical Center Staffing"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/fdjf-462q",
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
+            "description": "<p>The Veterans Health Administration (VHA) Leadership and Workforce Development System (VHALWD) has 36 separate databases that contain information on people, positions, and organizations, work groups, workforce, workforce and leadership classes, workforce development programs and participation, personal development plans, supervisory levels, mentor and coach attributes, High Performance Development Model (HPDM) core competency, intern data, Equal Employment Opportunity (EEO) reporting, succession planning, workforce planning, senior executive information, applicant tracking and recruitment, Executive Career Field (ECF) position and performance information, and education funding and programs. The VHA Executive Management Program consists of the functions that fall under the purview of the VHA Executive Resources Board (ERB) and the VHA Performance Review Board (PRB). Their functions include executive development, recruitment and placement, organizational analysis, succession planning, workforce planning, EEO and Alternative Dispute Resolution (ADR) assessment, workload tracking and reporting of human capital and HR, and individual and organizational performance assessment and recognition. The method used to collect this information is a proprietary system using relational database technology. Information from these databases are joined and expanded to inform programs and processes. This combination of information is used in the administration of talent management, VHA human capital objectives, and in the support of the ERB and PRB functions.</p>",
+            "identifier": "VA-VHA-LWD-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1999-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "capital",
                 "eeo",
@@ -41785,94 +41788,72 @@
                 "veteran",
                 "workforce"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/fdjf-462q",
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
-            "identifier": "VA-VHA-LWD-001",
-            "description": "<p>The Veterans Health Administration (VHA) Leadership and Workforce Development System (VHALWD) has 36 separate databases that contain information on people, positions, and organizations, work groups, workforce, workforce and leadership classes, workforce development programs and participation, personal development plans, supervisory levels, mentor and coach attributes, High Performance Development Model (HPDM) core competency, intern data, Equal Employment Opportunity (EEO) reporting, succession planning, workforce planning, senior executive information, applicant tracking and recruitment, Executive Career Field (ECF) position and performance information, and education funding and programs. The VHA Executive Management Program consists of the functions that fall under the purview of the VHA Executive Resources Board (ERB) and the VHA Performance Review Board (PRB). Their functions include executive development, recruitment and placement, organizational analysis, succession planning, workforce planning, EEO and Alternative Dispute Resolution (ADR) assessment, workload tracking and reporting of human capital and HR, and individual and organizational performance assessment and recognition. The method used to collect this information is a proprietary system using relational database technology. Information from these databases are joined and expanded to inform programs and processes. This combination of information is used in the administration of talent management, VHA human capital objectives, and in the support of the ERB and PRB functions.</p>",
-            "title": "VHA Leadership and Workforce Development System (VHALWD (Prior Executive Information System (EIS)))",
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
+            "title": "VHA Leadership and Workforce Development System (VHALWD (Prior Executive Information System (EIS)))"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/fdvk-ae4b",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "rhode island",
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
-            "identifier": "https://www.data.va.gov/api/views/fdvk-ae4b",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Rhode Island",
+            "identifier": "https://www.data.va.gov/api/views/fdvk-ae4b",
+            "issued": "2021-08-26",
+            "keyword": [
+                "rhode island",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fdvk-ae4b",
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
+            "title": "State Summaries_Rhode Island"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fe7d-awnt",
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
-                "appendix f-1",
-                "appendix g-1"
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
-            "identifier": "https://www.data.va.gov/api/views/fe7d-awnt",
             "description": "The PTSD-Repository is a comprehensive database of PTSD trials. The PTSD-Repository allows clinical, research, education, and policy stakeholders to understand current research on treatment effectiveness and harms, and enable informed decisions about future research, mental health policy, and clinical care priorities. This report updates the studies and variables included in the PTSD-Repository to include recently published trials, interventions targeting comorbid PTSD/SUD (substance use disorder), variables related to comorbidities such as suicide and SUDs, and risk of bias (ROB) assessment.\n\nThe Comparative Effectiveness Review (Update Report) and Evidence Tables (Appendix E, F-1, & G-1) are included in the downloadable .zip file. For more information, visit AHRQ's page, and open the \"Previous Versions\" tab: https://effectivehealthcare.ahrq.gov/products/ptsd-pharm-non-pharm-treatment/research",
-            "title": "AHRQ Report and Data Files (2020): Pharmacologic and Nonpharmacologic Treatments for Posttraumatic Stress Disorder (Update)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41880,21 +41861,45 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/fe7d-awnt",
+            "issued": "2020-11-24",
+            "keyword": [
+                "ahrq report",
+                "appendix e",
+                "appendix f-1",
+                "appendix g-1"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fe7d-awnt",
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
+            "title": "AHRQ Report and Data Files (2020): Pharmacologic and Nonpharmacologic Treatments for Posttraumatic Stress Disorder (Update)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/fei6-37eb",
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
+            "description": "<p>Combined cancer registry data from all VHA facilities.  Includes North American Association of Central Cancer Registries, Inc. (NAACCR).</p>",
+            "identifier": "VA-VHA-10P-SCS",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cancer",
                 "health",
@@ -41904,42 +41909,43 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/fei6-37eb",
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
-            "identifier": "VA-VHA-10P-SCS",
-            "description": "<p>Combined cancer registry data from all VHA facilities.  Includes North American Association of Central Cancer Registries, Inc. (NAACCR).</p>",
-            "title": "Oncology Tumor Registry (ONC)",
-            "programCode": [
-                "029:086"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1D",
             "theme": [
                 "cancer registry"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Oncology Tumor Registry (ONC)"
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
+            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- March 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING032014-054",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-03-01T05:00:00Z/2013-03-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 030",
                 "face amount",
@@ -41948,61 +41954,38 @@
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
-            "identifier": "VA-VBA-USASPENDING032014-054",
-            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- March 2013.</p>",
-            "title": "USA Spending file- 03/2014-New Life Insurance Policies-Insurance -  CFDA 64.030",
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
+            "title": "USA Spending file- 03/2014-New Life Insurance Policies-Insurance -  CFDA 64.030"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/ffxm-y9uj",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "preference",
-                "user"
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
-            "identifier": "VA-ORCH-15",
+            "dataQuality": true,
             "description": "<p>The Preferences service provides a means to store, retrieve, and manage user preferences. The service supports definition of enterprise wide preferences, as well as preferences that are specific to an application or business domain. The service supports dynamic creation and modification of preference definitions, supports the dynamic setting and modification of preference values,and supports governance of changes to preference domain definitions, preference definitions, and changes to preference values.</p>",
-            "title": "VIERS- User Preference Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42011,23 +41994,43 @@
                     "title": "VIERS- User Preference Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-15",
+            "issued": "2017-11-17",
+            "keyword": [
+                "preference",
+                "user"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ffxm-y9uj",
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
+            "title": "VIERS- User Preference Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/fgas-fuw8",
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
+            "description": "<p>The Post-Deployment Health Strategic Healthcare Group (PDHSHG) Registry System of Records is the information system encompassing the Ionizing Radiation Registry (IRR), the Agent Orange Registry (AOR), and the Gulf War Registry (GWR) which also includes related Depleted Uranium (DU) exams.</p>",
+            "identifier": "VA-VHA-OPH-007",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2002-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "gulf",
                 "health",
@@ -42037,43 +42040,43 @@
                 "veteran",
                 "war"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/fgas-fuw8",
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
-            "identifier": "VA-VHA-OPH-007",
-            "description": "<p>The Post-Deployment Health Strategic Healthcare Group (PDHSHG) Registry System of Records is the information system encompassing the Ionizing Radiation Registry (IRR), the Agent Orange Registry (AOR), and the Gulf War Registry (GWR) which also includes related Depleted Uranium (DU) exams.</p>",
-            "title": "Gulf War Registry (GWR) - The Post-Deployment Health Strategic Healthcare Group (PDHSHG) Registry System of Records",
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
+            "title": "Gulf War Registry (GWR) - The Post-Deployment Health Strategic Healthcare Group (PDHSHG) Registry System of Records"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/fgpr-x6yu",
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
+            "description": "<p>The Non-VA Care Medical and Pharmacy System (FEE) automates the Veterans Health Administration (VHA) Fee for Service program. It authorizes and pays private physicians, hospitals, and pharmacists for products and services provided to Veterans approved for the program. Veterans are reimbursed through VistA Fee for medically-related expenses including travel. Information is entered into the VistA Fee system through Veterans Health Information Systems and Technology Architecture (VistA) online menus. VistA Fee is run at the Austin Information Technology Center and interfaces with the Financial Management System (FMS), the Beneficiary Identification and Records Locator System (BIRLS), and the VHA Work Measurement database (VWM), to produce payments, accounting updates, and reports. VistA Fee facilitates money management, master record updating, and input error resolution. Daily reports indicating all payments processed and erroneous input transactions are transmitted to approximately 170 Veterans Affairs Medical Centers (VAMCs). Letters are sent to Veterans on a monthly basis detailing payments made on their behalf to Non-VA Care Service providers. Monthly, quarterly, semi-annual and annual reports are sent to the Veterans Affairs Central Office (VACO) and VAMCs. The Non-VA Care Fee Basis Medical System is commonly referred to as Central FEE.</p>",
+            "identifier": "VA-VHA-CBO-007",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1975-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "basis",
                 "central",
@@ -42087,109 +42090,84 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/fgpr-x6yu",
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
-            "identifier": "VA-VHA-CBO-007",
-            "description": "<p>The Non-VA Care Medical and Pharmacy System (FEE) automates the Veterans Health Administration (VHA) Fee for Service program. It authorizes and pays private physicians, hospitals, and pharmacists for products and services provided to Veterans approved for the program. Veterans are reimbursed through VistA Fee for medically-related expenses including travel. Information is entered into the VistA Fee system through Veterans Health Information Systems and Technology Architecture (VistA) online menus. VistA Fee is run at the Austin Information Technology Center and interfaces with the Financial Management System (FMS), the Beneficiary Identification and Records Locator System (BIRLS), and the VHA Work Measurement database (VWM), to produce payments, accounting updates, and reports. VistA Fee facilitates money management, master record updating, and input error resolution. Daily reports indicating all payments processed and erroneous input transactions are transmitted to approximately 170 Veterans Affairs Medical Centers (VAMCs). Letters are sent to Veterans on a monthly basis detailing payments made on their behalf to Non-VA Care Service providers. Monthly, quarterly, semi-annual and annual reports are sent to the Veterans Affairs Central Office (VACO) and VAMCs. The Non-VA Care Fee Basis Medical System is commonly referred to as Central FEE.</p>",
-            "title": "Non-VA Care Medical System (Fee)",
-            "programCode": [
-                "029:041"
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
+            "title": "Non-VA Care Medical System (Fee)"
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
+            "description": "<p>USA Spending- Veterans Dependency and indemnity Compensation for Service-Connected Death-- February 2014</p>",
+            "identifier": "VA-VBA-USASPENDING022014-035",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING022014-035",
-            "description": "<p>USA Spending- Veterans Dependency and indemnity Compensation for Service-Connected Death-- February 2014</p>",
-            "title": "USA Spending file- 02/2014 Veterans Dependency and indemnity Compensation for Service-Connected Death-  CFDA 64.110",
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
+            "title": "USA Spending file- 02/2014 Veterans Dependency and indemnity Compensation for Service-Connected Death-  CFDA 64.110"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_Program_by_State_Dec_2011.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-12-31T05:00:00Z/2011-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Face_Amount_by_Program_Dec_2011.doc"
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
-            "identifier": "VA-VBA-INS2011-004",
+            "dataQuality": true,
             "description": "<p>Face value of insurance for each administered life insurance program listed by state. Data is current as of 12-31-11.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Face Amount of Life Insurance Coverage by Program by State",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42197,66 +42175,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fh64-x25b/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fh64-x25b/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fh64-x25b/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/fh64-x25b/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fh64-x25b/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fh64-x25b/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fh64-x25b/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fh64-x25b/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fh64-x25b/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-004",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_Program_by_State_Dec_2011.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Face_Amount_by_Program_Dec_2011.doc"
+            ],
+            "temporal": "2010-12-31T05:00:00Z/2011-12-31T05:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Face Amount of Life Insurance Coverage by Program by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fhvc-6xzy",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "north carolina",
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
-            "identifier": "VA-OEI-OEI-119",
             "description": "<p>This is a summary of the programs and services provided by VA in North Carolina in fiscal year 2014.</p>",
-            "title": "State Summary:  North Carolina",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42265,44 +42248,45 @@
                     "title": "State Summary:  North Carolina"
                 }
             ],
+            "identifier": "VA-OEI-OEI-119",
+            "issued": "2017-07-26",
+            "keyword": [
+                "north carolina",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fhvc-6xzy",
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
+            "title": "State Summary:  North Carolina"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fiu4-8fx3",
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
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "5c515084-fa64-40bc-957a-bbc36966a7b3",
+            "dataQuality": true,
             "description": "<p>The product displays data for FY2000 to FY2017. It includes data related to Healthcare Priority Group</p>",
-            "title": "Veteran Patients by Healthcare Priority Group FY2000 to FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42310,37 +42294,36 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "5c515084-fa64-40bc-957a-bbc36966a7b3",
+            "issued": "2018-08-24",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fiu4-8fx3",
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
+            "title": "Veteran Patients by Healthcare Priority Group FY2000 to FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fkjq-z6m8",
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
-            "identifier": "https://www.data.va.gov/api/views/fkjq-z6m8",
             "description": "The Department of Veterans Affairs provides official estimates and projections of the Veteran population using the Veteran Population Projection Model (VetPop). Based on the available information through September 30, 2020, the latest model VetPop2020 estimated the Veteran population for the period from 2000 to 2020. The \u201cNumber of Estimated Veterans by State, Gender, and Age Group, 9/30/2000 to 9/30/2020\u201d data table shows the number of living Veterans at the end of each fiscal year from 2000 to 2020.",
-            "title": "VetPop2020 State Estimates 2000 to 2020",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42348,57 +42331,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fkjq-z6m8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fkjq-z6m8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fkjq-z6m8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/fkjq-z6m8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fkjq-z6m8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fkjq-z6m8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fkjq-z6m8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fkjq-z6m8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fkjq-z6m8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/fkjq-z6m8",
+            "issued": "2022-10-04",
+            "keyword": [
+                "historical period estimate",
+                "veteran population"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fkjq-z6m8",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-06",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020 State Estimates 2000 to 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fkqh-v9ds",
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
-            "identifier": "https://www.data.va.gov/api/views/fkqh-v9ds",
+            "dataQuality": true,
             "description": "<p>VBA SPECIALLY ADAPTED HOUSING BENEFIT PROGRAMS. The Specially Adapted Housing (SAH) grant program helps Veterans with certain service-connected disabilities live independently in a barrier-free environment. SAH grants can be used in one of the following ways: (1) construct a suitable home on suitable land either already owned or to be acquired by the veteran, or (2) remodel an existing home if it can be suitably adapted, or (3) acquire a suitably adapted home or reduce the outstanding mortgage on a suitably adapted home already owned by the veteran. b. The Special Housing Adaptation (SHA) grant program helps veterans with certain service-connected disabilities adapt or purchase a home to accommodate the disability. SHA grants can be used in one of the following ways: (1) adapt an existing home the veteran or a family member already owns in which the veteran lives; (2) adapt a home the veteran or family member intends to purchase in which the veteran will live; (3) help a veteran purchase a home already adapted in which the veteran will live. c. . The Temporary Residence Adaptations (TRA) program provides adaptation assistance to veterans who are residing, but do not intend to permanently reside, in the a residence owned by a family member. If a veteran is otherwise eligible for SAH or SHA, the assistance is limited. d. SAH and SHA grants may be used up to three times, as long as the aggregate grant amount does not exceed the statutory dollar limitation. TRA grants may only be used once (and count as a grant usage for purposes of the limit of three), and the amount of assistance provided will be subtracted from the veteran's available statutory maximum.</p>",
-            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS APR2019",
-            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42406,76 +42390,103 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fkqh-v9ds/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fkqh-v9ds/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fkqh-v9ds/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/fkqh-v9ds/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fkqh-v9ds/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fkqh-v9ds/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fkqh-v9ds/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fkqh-v9ds/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fkqh-v9ds/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/fkqh-v9ds",
+            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 106"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fkqh-v9ds",
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
+            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/fkvh-2i7t",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary South Dakota FY2023",
+            "identifier": "https://www.data.va.gov/api/views/fkvh-2i7t",
             "issued": "2024-06-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "south dakota"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/fkvh-2i7t",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/fkvh-2i7t",
-            "description": "NCVAS State Summary South Dakota FY2023",
-            "title": "NCVAS State Summary South Dakota FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary South Dakota FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.gibill.va.gov/",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.vba.va.gov/REPORTS/abr/index.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Salminio Garner",
+                "hasEmail": "mailto:salminio.garner1@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Education Recipients by training type and VA Education Benefit Program (By fiscal year). The data represents the number of individuals by VA education program who have used their VA education benefit during fiscal year.   Training type statistics may include individuals who used their education benefits in more than one training type, therefore the total within this table may be different than the total number of beneficiaries during the fiscal year.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.benefits.va.gov/reports/abr/2012_abr.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
             ],
+            "identifier": "VA-VBA-EDU2012-002",
+            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
+            "issued": "2017-07-26",
             "keyword": [
                 "dependents educational assistance",
                 "graduate",
@@ -42488,53 +42499,55 @@
                 "undergraduate",
                 "voc tech"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Salminio Garner",
-                "hasEmail": "mailto:salminio.garner1@va.gov"
-            },
+            "landingPage": "https://www.gibill.va.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-EDU2012-002",
-            "description": "<p>Education Recipients by training type and VA Education Benefit Program (By fiscal year). The data represents the number of individuals by VA education program who have used their VA education benefit during fiscal year.   Training type statistics may include individuals who used their education benefits in more than one training type, therefore the total within this table may be different than the total number of beneficiaries during the fiscal year.</p>",
-            "title": "FY12 Use of VA Education Benefits by Training Type & VA Education Benefit Program",
-            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
-            "programCode": [
-                "029:003"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.benefits.va.gov/reports/abr/2012_abr.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
+            "references": [
+                "https://www.vba.va.gov/REPORTS/abr/index.asp"
             ],
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2009-06-19/pdf/E9-14302.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "Statistical counts of students",
                 "Training Type",
                 "VA Education Program"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY12 Use of VA Education Benefits by Training Type & VA Education Benefit Program"
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
+            "description": "<p>This is a monthly report that the VA Office of Information Technology provides to congress about data incidents that took place during the month (April 2014).  The report contains details about and total numbers of mis-handling incidents;  mis-mailed incidents; mis-mailed CMOP incidents; IT equipment inventory incidents; missing stolen PC incidents; missing/stolen laptop incident; lost blackberry incidents;  and lost non-blackberry mobile devices (tablets, iPhones, androids, etc.) incidents.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/ABOUT_VA/docs/monthly_rfc_apr2014.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-18",
             "issued": "2017-07-26",
-            "temporal": "2014-03-31T04:00:00Z/2014-05-04T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "blackberry",
                 "congress",
@@ -42558,69 +42571,39 @@
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
-            "identifier": "VA-OIT-ITIS-18",
-            "description": "<p>This is a monthly report that the VA Office of Information Technology provides to congress about data incidents that took place during the month (April 2014).  The report contains details about and total numbers of mis-handling incidents;  mis-mailed incidents; mis-mailed CMOP incidents; IT equipment inventory incidents; missing stolen PC incidents; missing/stolen laptop incident; lost blackberry incidents;  and lost non-blackberry mobile devices (tablets, iPhones, androids, etc.) incidents.</p>",
-            "title": "Department of Veterans Affairs - Monthly Report to Congress of Data Incidents (April 2014)",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/ABOUT_VA/docs/monthly_rfc_apr2014.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-03-31T04:00:00Z/2014-05-04T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs - Monthly Report to Congress of Data Incidents (April 2014)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fp2p-5e3c",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "south dakota",
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
-            "identifier": "VA-OEI-OEI-128",
             "description": "<p>This is a summary of the programs and services provided by VA in South Dakota in fiscal year 2014.</p>",
-            "title": "State Summary:  South Dakota",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42629,48 +42612,46 @@
                     "title": "State Summary:  South Dakota"
                 }
             ],
+            "identifier": "VA-OEI-OEI-128",
+            "issued": "2017-07-26",
+            "keyword": [
+                "south dakota",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fp2p-5e3c",
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
+            "title": "State Summary:  South Dakota"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fpev-z8ks",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-04-01T04:00:00Z/2014-04-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 105",
-                "compensation and pension",
-                "usa spending",
-                "veterans surviving spouses and children"
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
-            "identifier": "VA-VBA-USASPENDING042014-059",
+            "dataQuality": true,
             "description": "<p>USA Spending- Veterans Surviving Spouses and Children- April 2014</p>",
-            "title": "USA Spending file- 04/2014 Compensation and Pension-  CFDA 64.105",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42679,57 +42660,79 @@
                     "title": "USA Spending file- 04/2014 Compensation and Pension- CFDA 64.105"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-USASPENDING042014-059",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cfda 64 105",
+                "compensation and pension",
+                "usa spending",
+                "veterans surviving spouses and children"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fpev-z8ks",
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
+            "title": "USA Spending file- 04/2014 Compensation and Pension-  CFDA 64.105"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/fpvw-bmp7",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Colorado FY2023",
+            "identifier": "https://www.data.va.gov/api/views/fpvw-bmp7",
             "issued": "2024-05-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "colorado",
                 "fy2024 data",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/fpvw-bmp7",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/fpvw-bmp7",
-            "description": "NCVAS State Summary Colorado FY2023",
-            "title": "NCVAS State Summary Colorado FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Colorado FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/fqc6-3qw6",
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
+            "description": "<p>The Community Nursing Home (CNH) database contains a list of all Community Nursing Home facilities under local contract to Veterans Health Administration (VHA). CNH facilities are not managed by VA. Instead, CNH facilities are private or public facilities licensed by the state where they provide the patient services. Each day all Veterans Affairs Medical Center (VAMC) that have a contract with a CNH enter information about the CNH into the Fee Basis module of Veterans Health Information Systems and Technology Architecture. This information is sent via MailMan to the VA Austin Information Technology Center where it is collected in a queue. A quarterly batch process is run on the queue. VAMCs that have sent invalid data or VAMCs that have contracts and did not send data are notified. Valid data is processed and used to update the database. Quarterly reports are sent to the CNHs, VAMCs, Veterans Integrated Service Networks (VISNs), Geriatrics &amp; Extended Care Strategic Health Care Group, and VA Central Office (VACO).</p>",
+            "identifier": "VA-VHA-GER-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1978-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "community living center",
                 "contract",
@@ -42742,61 +42745,41 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/fqc6-3qw6",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:055"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-GER-001",
-            "description": "<p>The Community Nursing Home (CNH) database contains a list of all Community Nursing Home facilities under local contract to Veterans Health Administration (VHA). CNH facilities are not managed by VA. Instead, CNH facilities are private or public facilities licensed by the state where they provide the patient services. Each day all Veterans Affairs Medical Center (VAMC) that have a contract with a CNH enter information about the CNH into the Fee Basis module of Veterans Health Information Systems and Technology Architecture. This information is sent via MailMan to the VA Austin Information Technology Center where it is collected in a queue. A quarterly batch process is run on the queue. VAMCs that have sent invalid data or VAMCs that have contracts and did not send data are notified. Valid data is processed and used to update the database. Quarterly reports are sent to the CNHs, VAMCs, Veterans Integrated Service Networks (VISNs), Geriatrics &amp; Extended Care Strategic Health Care Group, and VA Central Office (VACO).</p>",
-            "title": "Community Nursing Home (CNH)",
-            "programCode": [
-                "029:055"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1978-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Community Nursing Home (CNH)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/webservices/press/documentation/releases.cfm",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "press release",
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
-            "identifier": "VA-OIT-WSG-02",
             "description": "<p>The press release web service provides VA press release information. The VA press release feature is available across the enterprise, on any webpage, for the Department of Veterans Affairs.</p>",
-            "title": "Press Release",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42805,41 +42788,41 @@
                     "title": "API"
                 }
             ],
+            "identifier": "VA-OIT-WSG-02",
+            "issued": "2017-07-26",
+            "keyword": [
+                "press release",
+                "va"
+            ],
+            "landingPage": "https://www.va.gov/webservices/press/documentation/releases.cfm",
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
+            "title": "Press Release"
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
-            "identifier": "VA-OGC-009",
             "description": "<p>Duty to Assist in Seeking Records pertaining to an Individual other than the Claimant</p>",
-            "title": "OGC Precedent Opinion 5-2014",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42848,46 +42831,46 @@
                     "title": "VAOGCPREC 5-2014"
                 }
             ],
+            "identifier": "VA-OGC-009",
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
+            "title": "OGC Precedent Opinion 5-2014"
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
-            "temporal": "2014-03-31T04:00:00Z/2014-06-30T04:00:00Z",
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
-            "identifier": "VA-OEI-OEI-044",
+            "dataQuality": true,
             "description": "<p>NCVAS Pocket Cards are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs (VA) benefits and health care utilization.</p>",
-            "title": "VA Benefits & Health Care Utilization",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42896,29 +42879,49 @@
                     "title": "VA Benefits and Health Care Utilization"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-044",
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
+            "temporal": "2014-03-31T04:00:00Z/2014-06-30T04:00:00Z",
             "theme": [
                 "Veteran Benefits",
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
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/ftpi-epf7",
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
+            "description": "<p>The Veterans Health Administration (VHA) is increasingly dependent upon data.  Most of its employees generate and use vast amounts of data on a daily basis.  To improve our capacity for data analysis while providing the most efficient and the highest quality health care to our Veteran patients, VHA, working with the VA Office of Information and Technology, implemented a health data warehouse.  Central to this plan is consolidating data from disparate sources into a coherent single logical data model.  The Corporate Data Warehouse (CDW) is the physical implementation of this logical data model at the enterprise level for VHA.   Although the CDW initially began to store data as early as 2006, a renewed effort began in 2010 to accelerate CDW's content by including more subject areas from Veterans Health Information Systems and Technology Architecture (VistA) and content from other existing national data systems.  CDW supports fully developed subject areas in its production environment as well as supporting rapid prototyping by extracting data directly from source systems with very minor data transformations.  The Regional Data Warehouses and the Veterans Integrated Service Network (VISN) Data Warehouses share content from CDW and allow for greater reporting flexibility at the local level throughout the VHA organization.</p>",
+            "identifier": "VA-VHA-OIA-006",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2011-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "domain",
                 "health",
@@ -42929,61 +42932,40 @@
                 "vista",
                 "warehouse"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/ftpi-epf7",
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
-            "identifier": "VA-VHA-OIA-006",
-            "description": "<p>The Veterans Health Administration (VHA) is increasingly dependent upon data.  Most of its employees generate and use vast amounts of data on a daily basis.  To improve our capacity for data analysis while providing the most efficient and the highest quality health care to our Veteran patients, VHA, working with the VA Office of Information and Technology, implemented a health data warehouse.  Central to this plan is consolidating data from disparate sources into a coherent single logical data model.  The Corporate Data Warehouse (CDW) is the physical implementation of this logical data model at the enterprise level for VHA.   Although the CDW initially began to store data as early as 2006, a renewed effort began in 2010 to accelerate CDW's content by including more subject areas from Veterans Health Information Systems and Technology Architecture (VistA) and content from other existing national data systems.  CDW supports fully developed subject areas in its production environment as well as supporting rapid prototyping by extracting data directly from source systems with very minor data transformations.  The Regional Data Warehouses and the Veterans Integrated Service Network (VISN) Data Warehouses share content from CDW and allow for greater reporting flexibility at the local level throughout the VHA organization.</p>",
-            "title": "Corporate Data Warehouse (CDW)",
-            "programCode": [
-                "029:041"
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
+            "title": "Corporate Data Warehouse (CDW)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fuce-2zbe",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "children",
-                "period of service",
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
-            "identifier": "VA-OEI-OEI-224",
             "description": "<p>Dataset shows Veterans by Period Of Service (POS) and Children: 2015</p>",
-            "title": "Veterans by Period Of Service (POS) and Children: 2015",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42991,44 +42973,42 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "VA-OEI-OEI-224",
+            "issued": "2017-07-26",
+            "keyword": [
+                "children",
+                "period of service",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fuce-2zbe",
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
+            "title": "Veterans by Period Of Service (POS) and Children: 2015"
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
-            "identifier": "VA-VBA-ABR2012-123",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Texas-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43036,40 +43016,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-123",
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
+            "title": "Texas-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/fv5j-6wit",
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
-            "identifier": "https://www.data.va.gov/api/views/fv5j-6wit",
             "description": "These data are based on the latest Veteran Population Projection Model, VetPop2020, provided by the National Center for Veterans Statistics and Analysis, published in 2023.",
-            "title": "FY 2021_NCVAS Vet Population by Race and Ethnicity For State Summaries",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43077,87 +43064,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fv5j-6wit/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fv5j-6wit/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fv5j-6wit/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/fv5j-6wit/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fv5j-6wit/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fv5j-6wit/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fv5j-6wit/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fv5j-6wit/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fv5j-6wit/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/fv5j-6wit",
+            "issued": "2023-06-14",
+            "landingPage": "https://www.data.va.gov/d/fv5j-6wit",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021_NCVAS Vet Population by Race and Ethnicity For State Summaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/fxhp-e4h2",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Puerto Rico FY2023",
+            "identifier": "https://www.data.va.gov/api/views/fxhp-e4h2",
             "issued": "2024-06-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "puerto rico"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/fxhp-e4h2",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/fxhp-e4h2",
-            "description": "NCVAS State Summary Puerto Rico FY2023",
-            "title": "NCVAS State Summary Puerto Rico FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Puerto Rico FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fyb9-nirf",
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
-            "identifier": "13cf5bdb-2343-44ce-a6bb-87f528a68507",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Montana FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43165,81 +43149,77 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "13cf5bdb-2343-44ce-a6bb-87f528a68507",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fyb9-nirf",
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
+            "title": "State Summary Montana FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fymr-nw8a",
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
-            "identifier": "70535216-31bf-416c-9ff4-3ec839abed4c",
+            "dataQuality": true,
             "description": "<p>VBA PROGRAM BENEFITS for Automobiles and Adaptive Equipment for Certain Disabled Veterans and Members of the Armed Forces. Veterans with honorable service and servicepersons on duty having a service-connected disability due to loss or permanent loss of use of one or both feet, one or both hands, or a permanent impairment of vision of both eyes to a prescribed degree. For adaptive equipment only, eligibility also exists if there is service-connected ankylosis of one or both knees or one or both hips. Personnel on active duty also qualify under the same criteria as veterans. Uses &amp; Use Restrictions:  Assistance toward purchase of an automobile or other conveyance is a one-time payment only. Necessary adaptive equipment may be furnished, repaired, replaced, or reinstalled on a conveyance which may be purchased with assistance or any other conveyance subsequently or previously acquired. Adaptive equipment will be provided for no more than two conveyances during any four-year period unless one of those two vehicles becomes unavailable to the veteran.</p>",
-            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE FY2019",
+            "identifier": "70535216-31bf-416c-9ff4-3ec839abed4c",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 100"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fymr-nw8a",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-14",
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
+            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE FY2019"
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
-            "identifier": "VA-VBA-ABR2012-020",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Most Prevalent Service Connected Disabilities for Veterans Receiving Compensation at the end of FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43247,45 +43227,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-020",
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
+            "title": "Most Prevalent Service Connected Disabilities for Veterans Receiving Compensation at the end of FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fyxy-5w6i",
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
-            "identifier": "https://www.data.va.gov/api/views/fyxy-5w6i",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE MAR2019",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43293,61 +43276,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fyxy-5w6i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fyxy-5w6i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fyxy-5w6i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/fyxy-5w6i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fyxy-5w6i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fyxy-5w6i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fyxy-5w6i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fyxy-5w6i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fyxy-5w6i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/fyxy-5w6i",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fyxy-5w6i",
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
+            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE MAR2019"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fzm8-ugan",
-            "bureauCode": [
-                "029:00"
-            ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "survey",
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
-            "identifier": "VA-OEI-OEI-143",
             "description": "<p>This survey is the second in a series of comprehensive nationwide surveys designed to help the Department of Veterans Affairs (VA) plan its future programs and services for Veterans.</p>",
-            "title": "1979 National Survey of Veterans",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43356,24 +43339,56 @@
                     "title": "1979 National Survey of Veterans"
                 }
             ],
+            "identifier": "VA-OEI-OEI-143",
+            "issued": "2017-07-26",
+            "keyword": [
+                "survey",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fzm8-ugan",
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
+            "title": "1979 National Survey of Veterans"
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
+                    "downloadURL": "https://www.va.gov/health/docs/March_2015_Completed_04302015.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Appointments 31 March 2015"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-104",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-02-28T05:00:00Z/2015-02-28T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -43387,71 +43402,38 @@
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
-            "identifier": "VA-VHA-OIA-104",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Mar 31",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/March_2015_Completed_04302015.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Appointments 31 March 2015"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
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
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Mar 31"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/g2jn-5rx5",
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
-            "identifier": "https://www.data.va.gov/api/views/g2jn-5rx5",
             "description": "",
-            "title": "Table 2 - U. S. Veterans Life Table for Female 1980-1989",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43459,131 +43441,130 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/g2jn-5rx5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/g2jn-5rx5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/g2jn-5rx5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/g2jn-5rx5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/g2jn-5rx5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/g2jn-5rx5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/g2jn-5rx5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/g2jn-5rx5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/g2jn-5rx5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/g2jn-5rx5",
+            "issued": "2023-04-18",
+            "keyword": [
+                "death rate",
+                "life expectancy",
+                "life table"
+            ],
+            "landingPage": "https://www.data.va.gov/d/g2jn-5rx5",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-19",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Table 2 - U. S. Veterans Life Table for Female 1980-1989"
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
+            "description": "<p>USA Spending- Direct Home Loan- January- 2014.</p>",
+            "identifier": "VA-VBA-USASPENDING012014-027",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING012014-027",
-            "description": "<p>USA Spending- Direct Home Loan- January- 2014.</p>",
-            "title": "USA Spending file- 01/2014-Direct Home Loan-  CFDA 64.118",
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
+            "title": "USA Spending file- 01/2014-Direct Home Loan-  CFDA 64.118"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/g3uq-5kqb",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-06",
-            "keyword": [
-                "arkansas",
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
-            "identifier": "https://www.data.va.gov/api/views/g3uq-5kqb",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Arkansas",
+            "identifier": "https://www.data.va.gov/api/views/g3uq-5kqb",
+            "issued": "2021-08-26",
+            "keyword": [
+                "arkansas",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/g3uq-5kqb",
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
+            "title": "State Summaries_Arkansas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/g4bg-kqnp",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "benefits",
-                "budget",
-                "statistics",
-                "veterans data"
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
-            "identifier": "VA-OEI-OEI-310",
             "description": "<p>NCVAS Pocket Card archives are a compilation of facts related to the count of Veterans Receiving Department of Veterans Affairs (VA) benefits and health care utilizaiton.</p>",
-            "title": "6 (Pocket Card) VA Benefits of Health Care Utilization",
-            "programCode": [
-                "029:089"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43592,69 +43573,66 @@
                     "title": "html"
                 }
             ],
+            "identifier": "VA-OEI-OEI-310",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "budget",
+                "statistics",
+                "veterans data"
+            ],
+            "landingPage": "https://www.data.va.gov/d/g4bg-kqnp",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:089"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "6 (Pocket Card) VA Benefits of Health Care Utilization"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/g5an-64bb",
-            "issued": "2023-08-11",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Washington FY2021",
+            "identifier": "https://www.data.va.gov/api/views/g5an-64bb",
+            "issued": "2023-08-11",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "washington"
             ],
-            "identifier": "https://www.data.va.gov/api/views/g5an-64bb",
+            "landingPage": "https://www.data.va.gov/d/g5an-64bb",
+            "modified": "2024-06-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Washington FY2021",
             "title": "NCVAS State Summary Washington FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_program_by_state.xls",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-04-01T04:00:00Z/2011-04-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Insurance_Technical_Notes_Face_Amount_by_Program.doc"
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
-            "identifier": "VA-VBA-INS2011-003",
+            "dataQuality": true,
             "description": "<p>Face value of insurance for each administered life insurance program listed by state. Data is current as of 4-30-11.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Face Amount of Life Insurance Coverage by Program by State",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43662,27 +43640,62 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-003",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_Amount_by_program_by_state.xls",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Insurance_Technical_Notes_Face_Amount_by_Program.doc"
+            ],
+            "temporal": "2011-04-01T04:00:00Z/2011-04-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Face Amount of Life Insurance Coverage by Program by State"
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
+                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX-FY04-000-Final.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-030",
             "issued": "2017-07-26",
-            "temporal": "2003-10-01T04:00:00Z/2004-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-19",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -43696,67 +43709,38 @@
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
-            "identifier": "VA-OEI-OEI-030",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY2004",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX-FY04-000-Final.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2003-10-01T04:00:00Z/2004-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/g7hr-mdrf",
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
-            "identifier": "https://www.data.va.gov/api/views/g7hr-mdrf",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist wartime veterans in need whose non-service- connected disabilities are permanent and total preventing them from following a substantially gainful occupation. A Veteran who meets the wartime service requirements is potential eligible if he/she is: \u2022 permanently and totally disabled for reasons not necessarily due to service, \u2022 age 65 or older, or \u2022 is presumed to be totally and permanently disabled for pension purposes because: o he/she is a patient in a nursing home for long-term care due to a disability, or o being disabled, as determined by the Commissioner of Social Security (SS) for purposes of any benefits administered by the Commissioner, such as SS disability benefits or Supplemental Security Income. Income restrictions are prescribed in 38 U.S.C. 1521. Pension is not payable to those whose estates are so large that it is reasonable they use the estate for maintenance. A Veteran meets wartime service requirements if he/she served: \u2022 a total of 90 days or more during one or more periods of war; \u2022 90 or more consecutive days that began or ended during a period of war; or \u2022 for any length of time during a period of war if he/she was discharged or released for a service-connected disability. Veterans entering service after September 7, 1980, must also meet the minimum active duty requirement of 24 months of continuous service or the full period to which the Veteran was called to active duty. (38 U.S.C.5303(A)).</p>",
-            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS APR2019",
-            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43764,46 +43748,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/g7hr-mdrf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/g7hr-mdrf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/g7hr-mdrf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/g7hr-mdrf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/g7hr-mdrf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/g7hr-mdrf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/g7hr-mdrf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/g7hr-mdrf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/g7hr-mdrf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/g7hr-mdrf",
+            "isPartOf": "279f1b11-a128-4135-825a-5530f04cb050",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 104"
+            ],
+            "landingPage": "https://www.data.va.gov/d/g7hr-mdrf",
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
+            "title": "USA SPENDING C&P B104 PENSION FOR NON-SERVICE CONNECTED FOR VETERANS APR2019"
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
-            "temporal": "2014-06-01T04:00:00Z/2014-06-01T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_20140619.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "June 19, 2014"
+                }
             ],
+            "identifier": "VA-VHA-OIA-057",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -43817,75 +43829,43 @@
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
-            "identifier": "VA-VHA-OIA-057",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.</p>",
-            "title": "Accelerating Access to Care Initiative - Report 2014 June 19",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/VAMC_Patient_Access_Data_20140619.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "June 19, 2014"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2014-06-01T04:00:00Z/2014-06-01T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative - Report 2014 June 19"
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
-            "identifier": "VA-VBA-ABR2012-131",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Tennessee-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43893,45 +43873,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-131",
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
+            "title": "Tennessee-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/g8wb-s6jf",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-05-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "rural",
-                "urban",
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
-            "identifier": "f6e72fd4-3a8b-4307-93a3-e1e2f63f4bfc",
+            "dataQuality": true,
             "description": "<p>Estimates of state counts of Veteran residing in rural and urban areas by age and sex, race and ethnicity and period of service.</p>",
-            "title": "Rural/Urban Veterans: 2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43939,23 +43922,43 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "f6e72fd4-3a8b-4307-93a3-e1e2f63f4bfc",
+            "issued": "2018-05-09",
+            "keyword": [
+                "rural",
+                "urban",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/g8wb-s6jf",
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
                 "Demographics"
-            ]
+            ],
+            "title": "Rural/Urban Veterans: 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/g97r-682x",
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
+            "description": "<p>The Contract Administration and Management System (CAMS) is a data management system designed specifically for the Veterans Health Administration Office of Facilities Management (FM) for the management of contract and funding data. It provides a means of sorting and tracking data related to major Architect-Engineer and construction contracts such as contract type, project locations, project status, and contract funding.</p>",
+            "identifier": "VA-VHA-FM-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1992-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "architect",
                 "construction",
@@ -43966,62 +43969,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/g97r-682x",
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
-            "identifier": "VA-VHA-FM-001",
-            "description": "<p>The Contract Administration and Management System (CAMS) is a data management system designed specifically for the Veterans Health Administration Office of Facilities Management (FM) for the management of contract and funding data. It provides a means of sorting and tracking data related to major Architect-Engineer and construction contracts such as contract type, project locations, project status, and contract funding.</p>",
-            "title": "Contract Administration Management System (CAMS)",
-            "programCode": [
-                "029:040"
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
+            "title": "Contract Administration Management System (CAMS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ga27-4pm5",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
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
-            "identifier": "https://www.data.va.gov/api/views/ga27-4pm5",
+            "dataQuality": true,
             "description": "2023 VA All Employee Survey (AES) deidentified individual-level public dataset",
-            "title": "AES 2023 PRDF",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44029,59 +44012,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ga27-4pm5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ga27-4pm5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ga27-4pm5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ga27-4pm5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ga27-4pm5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ga27-4pm5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ga27-4pm5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ga27-4pm5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ga27-4pm5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/ga27-4pm5",
+            "issued": "2025-01-30",
+            "keyword": [
+                "engagement",
+                "satisfaction",
+                "survey",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ga27-4pm5",
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
+            "title": "AES 2023 PRDF"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/garw-xrwf",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "oneva",
-                "strategy"
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
-            "identifier": "VA-OIT-OIT-057",
             "description": "<p>The outcomes/goals supported by effective use of an EA are: Improved Service Delivery, Functional Integration, Resource Optimization and Authoritative Reference. VA has recognized the four outcomes proposed by the CAF as consistent with meeting VA transformation objectives and adopted them to evolve the OneVA EA</p>",
-            "title": "OneVA EA Vision and Strategy",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44089,53 +44072,73 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "VA-OIT-OIT-057",
+            "issued": "2017-07-26",
+            "keyword": [
+                "oneva",
+                "strategy"
+            ],
+            "landingPage": "https://www.data.va.gov/d/garw-xrwf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
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
+            "title": "OneVA EA Vision and Strategy"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/gavm-n6bm",
-            "issued": "2019-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-30",
-            "keyword": [
-                "minority veterans"
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
-            "identifier": "https://www.data.va.gov/api/views/gavm-n6bm",
             "description": "Over the past 30 years, racial and ethnic minorities have entered the military in ever-increasing numbers. Ultimately, they will make the transition from Servicemember to Veteran.",
-            "title": "2014 Minority Veteran Report",
+            "identifier": "https://www.data.va.gov/api/views/gavm-n6bm",
+            "issued": "2019-09-10",
+            "keyword": [
+                "minority veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gavm-n6bm",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-01-30",
             "programCode": [
                 "029:058"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "2014 Minority Veteran Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/gb2p-c356",
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
+            "description": "<p>The Surgery Risk Assessment (SRA) database is part of the VA Surgical Quality Improvement Program (VASQIP). This database contains assessments of selected surgical operations performed at Veteran Affairs Medical Centers (VAMCs). Addition to the SRA database requires that the surgery is Major (as defined by the Current Procedural Terminology (CPT) codes assigned to the surgery), it must not be cardiac related, and it may not be concurrent with another surgery. Frequently performed other types of surgeries may also be excluded. Nurse reviewers at VAMCs gather the information from surgical data located in the Veterans Health Information Systems and Technology Architecture (VistA) environment. Information is also collected from pre-and post-operative charts and from interviews with patients. This information is entered into VistA and transmitted daily by a batch process to the Hines Office of Information &amp; Technology (OI&amp;T) Field Office. While the database has been in operation since 1995, the system only contains data for the current fiscal year. The data from previous fiscal years is archived if later retrieval is needed. Valid transmissions are sent to the VASQIP office at Denver for analysis. Information from non-assessed surgeries is transmitted from the VAMCs to the Hines OI Field Office monthly. This is also passed along to VASQIP at Denver. The users of this database include the VASQIP Executive Board.</p>",
+            "identifier": "VA-VHA-SS-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1991-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "assessment",
                 "improvement",
@@ -44148,43 +44151,43 @@
                 "vasqip",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/gb2p-c356",
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
-            "identifier": "VA-VHA-SS-001",
-            "description": "<p>The Surgery Risk Assessment (SRA) database is part of the VA Surgical Quality Improvement Program (VASQIP). This database contains assessments of selected surgical operations performed at Veteran Affairs Medical Centers (VAMCs). Addition to the SRA database requires that the surgery is Major (as defined by the Current Procedural Terminology (CPT) codes assigned to the surgery), it must not be cardiac related, and it may not be concurrent with another surgery. Frequently performed other types of surgeries may also be excluded. Nurse reviewers at VAMCs gather the information from surgical data located in the Veterans Health Information Systems and Technology Architecture (VistA) environment. Information is also collected from pre-and post-operative charts and from interviews with patients. This information is entered into VistA and transmitted daily by a batch process to the Hines Office of Information &amp; Technology (OI&amp;T) Field Office. While the database has been in operation since 1995, the system only contains data for the current fiscal year. The data from previous fiscal years is archived if later retrieval is needed. Valid transmissions are sent to the VASQIP office at Denver for analysis. Information from non-assessed surgeries is transmitted from the VAMCs to the Hines OI Field Office monthly. This is also passed along to VASQIP at Denver. The users of this database include the VASQIP Executive Board.</p>",
-            "title": "Surgery Risk Assessment (SRA) Database",
-            "programCode": [
-                "029:040"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1991-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Surgery Risk Assessment (SRA) Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/gbb5-khf8",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Privacy Act",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA NCOD",
+                "hasEmail": "mailto:VHANCOD@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Office of Personnel Management requires government agencies, at a minimum, to query employees on job satisfaction, organizational assessment and organizational culture.  VHA maintains response data for all census surveys such as the Voice of VA as well as the VA Entrance and Exit surveys.</p>",
+            "identifier": "VA-VHA-OHR-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1997-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "clinician",
                 "doctor",
@@ -44195,61 +44198,42 @@
                 "va",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA NCOD",
-                "hasEmail": "mailto:VHANCOD@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/gbb5-khf8",
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
-            "identifier": "VA-VHA-OHR-001",
-            "description": "<p>The Office of Personnel Management requires government agencies, at a minimum, to query employees on job satisfaction, organizational assessment and organizational culture.  VHA maintains response data for all census surveys such as the Voice of VA as well as the VA Entrance and Exit surveys.</p>",
-            "title": "All Employee Census Survey (AES)",
-            "programCode": [
-                "029:041"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Privacy Act",
+            "temporal": "1997-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "All Employee Census Survey (AES)"
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
-            "temporal": "2011-07-01T04:00:00Z/2011-09-30T04:00:00Z",
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
-            "identifier": "VA-OM-OM-092",
+            "dataQuality": true,
             "description": "<p>FY 2011 Fourth Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2011 Fourth Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44258,27 +44242,46 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-092",
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
+            "temporal": "2011-07-01T04:00:00Z/2011-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2011 Fourth Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/gbx4-ntxr",
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
+            "description": "<p>The Medical Care Cost Recovery National Database (MCCR NDB) provides a repository of summary Medical Care Collections Fund (MCCF) billing and collection information used by program management to compare facility performance. It stores summary information for Veterans Health Administration (VHA) receivables including the number of receivables and their summarized status information. This database is used to monitor the status of the VHA's collection process and to provide visibility on the types of bills and collections being done by the Department. The objective of the VA MCCF Program is to collect reimbursement from third party health insurers and co-payments from certain non-service-connected (NSC) Veterans for the cost of medical care furnished to Veterans.  Legislation has authorized VHA to: submit claims to and recover payments from Veterans' third party health insurance carriers for treatment of non-service-connected conditions; recover co-payments from certain Veterans for treatment of non-service-connected conditions; and recover co-payments for medications from certain Veterans for treatment of non-service-connected conditions. All of the information captured in the MCCR NDB is derived from the Accounts Receivable (AR) modules running at each medical center. MCCR NDB is not used for official collections figures; instead, the Department uses the Financial Management System (FMS).</p>",
+            "identifier": "VA-VHA-CBO-006",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1993-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "account",
                 "care",
@@ -44292,61 +44295,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/gbx4-ntxr",
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
-            "identifier": "VA-VHA-CBO-006",
-            "description": "<p>The Medical Care Cost Recovery National Database (MCCR NDB) provides a repository of summary Medical Care Collections Fund (MCCF) billing and collection information used by program management to compare facility performance. It stores summary information for Veterans Health Administration (VHA) receivables including the number of receivables and their summarized status information. This database is used to monitor the status of the VHA's collection process and to provide visibility on the types of bills and collections being done by the Department. The objective of the VA MCCF Program is to collect reimbursement from third party health insurers and co-payments from certain non-service-connected (NSC) Veterans for the cost of medical care furnished to Veterans.  Legislation has authorized VHA to: submit claims to and recover payments from Veterans' third party health insurance carriers for treatment of non-service-connected conditions; recover co-payments from certain Veterans for treatment of non-service-connected conditions; and recover co-payments for medications from certain Veterans for treatment of non-service-connected conditions. All of the information captured in the MCCR NDB is derived from the Accounts Receivable (AR) modules running at each medical center. MCCR NDB is not used for official collections figures; instead, the Department uses the Financial Management System (FMS).</p>",
-            "title": "Medical Care Cost Recovery National Database (MCCR NDB)",
-            "programCode": [
-                "029:041"
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
+            "title": "Medical Care Cost Recovery National Database (MCCR NDB)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gcd2-xw9m",
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
-            "identifier": "https://www.data.va.gov/api/views/gcd2-xw9m",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to help servicepersons adjust to civilian life after separation from military service, assist in the recruitment and retention of highly qualified personnel in the active and reserve components in the Armed Forces by providing education benefits, and to provide educational opportunities to the dependents of certain service members and veterans. Individuals who entered active duty after September 10, 2001 may be eligible for the Post-9/11 GI Bill. Individuals can use the Post-9/11 GI Bill after serving 90 days on active duty (excluding entry level and skill training). Only periods of active duty under title 10 will be used to establish eligibility for the Post 9/11 GI Bill. A high school diploma or equivalency certificate is always required for eligibility. Individuals who are eligible for the Montgomery GI Bill \u2013 Active Duty (chapter 30), the Montgomery GI Bill \u2013 Selected Reserve (chapter 1606), or the Reserve Educational Assistance Program (REAP) will have to make an irrevocable election to relinquish eligibility under one of those benefit programs to establish eligibility under the Post-9/11 GI Bill. The dependent children of a person who died in the line of duty while serving as a member of the Armed Forces may be eligible to use benefits under the Fry Scholarship provision of the Post-9/11 GI Bill. The spouse and/or child(ren) of a veteran or service member may be eligible for the Post 9/11 GI Bill if the veteran or service member transfers entitlement to those dependents. Eligibility to transfer entitlement to dependents is determined by the Department of Defense. This is not a complete list of eligibility requirements. For more information on the latest changes to the Post-9/11 GI Bill go to the VA web-site.</p>",
-            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE APR2019",
-            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44354,60 +44338,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gcd2-xw9m/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gcd2-xw9m/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gcd2-xw9m/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/gcd2-xw9m/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gcd2-xw9m/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gcd2-xw9m/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gcd2-xw9m/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gcd2-xw9m/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gcd2-xw9m/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/gcd2-xw9m",
+            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 028"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gcd2-xw9m",
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
+            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gcnf-26ic",
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
-            "title": "Equitable Relief Reports 2012",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44415,47 +44401,43 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gcnf-26ic",
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
+            "title": "Equitable Relief Reports 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gcqr-rc9e",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "ogc",
-                "opinion",
-                "specially adapted housing"
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
-            "identifier": "VA-OGC-018",
             "description": "<p>Specially Adapted Housing (SAH) Escrow Accounts Author: Simpson, J.</p>",
-            "title": "OGC Precedent Opinion 1-2012",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44464,55 +44446,88 @@
                     "title": "OGC Precedent Opinion 1-2012"
                 }
             ],
+            "identifier": "VA-OGC-018",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion",
+                "specially adapted housing"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gcqr-rc9e",
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
+            "title": "OGC Precedent Opinion 1-2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "landingPage": "https://www.data.va.gov/d/gd7b-q5ua",
-            "issued": "2020-03-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-27",
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
-            "identifier": "https://www.data.va.gov/api/views/gd7b-q5ua",
             "description": "Learn how to find data of interest and get started using the platform features of the PTSD Repository.",
-            "title": "How do I get started working with the PTSD Repository?",
-            "programCode": [
-                "029:000"
+            "identifier": "https://www.data.va.gov/api/views/gd7b-q5ua",
+            "issued": "2020-03-23",
+            "keyword": [
+                "ptsd-repository"
             ],
+            "landingPage": "https://www.data.va.gov/d/gd7b-q5ua",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2024-03-27",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for PTSD"
+            },
+            "rights": "All data is within the public domain and is currently available for download.",
+            "title": "How do I get started working with the PTSD Repository?"
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
+            "describedBy": "https://www.pbm.va.gov/nationalformulary.asp",
+            "description": "<p>The VA National Formulary is a listing of products (drugs and supplies) that must be available for prescription at all VA facilities, and cannot be made non-formulary by a Veteran Integrated Service Network (VISN) or individual medical center. Regarding chemical or biological entities that by law must be submitted to the United States (U.S.) Food and Drug Administration (FDA) for pre-marketing approval, only those entities that actually have been approved by FDA using New Drug Application (NDA), Abbreviated New Drug Application (ANDA), or biologics license, may be added to the VA National Formulary.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.pbm.va.gov/nationalformulary.asp",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "VA National Formulary"
+                }
+            ],
+            "identifier": "VA-VHA-PBM-006",
+            "isPartOf": "VA-VHA-PBM-008",
             "issued": "2017-07-26",
-            "temporal": "1998-10-01T04:00:00Z/2014-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "drug",
                 "fda",
@@ -44524,69 +44539,39 @@
                 "vanf",
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
-            "identifier": "VA-VHA-PBM-006",
-            "description": "<p>The VA National Formulary is a listing of products (drugs and supplies) that must be available for prescription at all VA facilities, and cannot be made non-formulary by a Veteran Integrated Service Network (VISN) or individual medical center. Regarding chemical or biological entities that by law must be submitted to the United States (U.S.) Food and Drug Administration (FDA) for pre-marketing approval, only those entities that actually have been approved by FDA using New Drug Application (NDA), Abbreviated New Drug Application (ANDA), or biologics license, may be added to the VA National Formulary.</p>",
-            "title": "VA National Formulary",
-            "isPartOf": "VA-VHA-PBM-008",
-            "programCode": [
-                "029:047"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.pbm.va.gov/nationalformulary.asp",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "VA National Formulary"
-                }
-            ],
-            "describedBy": "https://www.pbm.va.gov/nationalformulary.asp",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "1998-10-01T04:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Pharmacy"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA National Formulary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/geti-hxbb",
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
-            "identifier": "https://www.data.va.gov/api/views/geti-hxbb",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE MAY2019",
-            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44594,124 +44579,123 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/geti-hxbb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/geti-hxbb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/geti-hxbb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/geti-hxbb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/geti-hxbb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/geti-hxbb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/geti-hxbb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/geti-hxbb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/geti-hxbb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/geti-hxbb",
+            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
+            "issued": "2019-03-20",
+            "keyword": [
+                "cdfa 64.124"
+            ],
+            "landingPage": "https://www.data.va.gov/d/geti-hxbb",
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
+            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE MAY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gfqe-7vxi",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
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
-            "identifier": "e30045ea-2153-40e3-91bc-23c0014ae69c",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide direct loans to certain veterans who are, or whose spouses are, Native Americans for the purchase or construction of homes on trust lands. Veterans who are, or whose spouses are, recognized by a Federally Recognized Tribal Government as a Native American and who: (a) Served on active duty on or after September 16, 1940, and were discharged or released under conditions other than dishonorable. If service was any time during World War II, the Korean Conflict, the Vietnam-era, or the Persian Gulf War, then the Native American Veteran must have served on active duty for 90 days or more; peacetime service only must have served a minimum of 181 days continuous active duty. If separated from enlisted service which began after September 7, 1980, or service as an officer which began after October 16, 1981, a veteran must also have served at least 24 months of continuous active duty or the full period for which called or ordered to active duty. Veterans of such recent service may qualify with less service time if they have a compensable service-connected disability or were discharged after at least 181 days, under the authority of 10 U.S.C 1171 or 1173. (b) Any veteran in the above classes with less service but discharged with a service-connected disability. (c) If acknowledged as a Native American by a Federally Recognized Tribal Government, unmarried surviving spouses of otherwise eligible veterans who died in service or whose deaths were attributable to service-connected disabilities and spouses of members of the Armed Forces serving on active duty, who are listed as missing in action, or as prisoners of war and who have been so listed 90 days or more. (d) Members of the Selected Reservists who ae, or whose spouses ae, recognized by a Federally Recognized Tribal Government as Native Americans and who are not otherwise eligible for home loan benefits and who have completed a total of 6 years in the Selected Reserves followed by an honorable discharge, placement on the retired list, or continued service.</p>",
-            "title": "USA SPENDING LGY B126 NATIVE AMERICAN VETERAN DIRECT LOAN PROGRAM FY2019",
+            "identifier": "e30045ea-2153-40e3-91bc-23c0014ae69c",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 126"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gfqe-7vxi",
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
+            "title": "USA SPENDING LGY B126 NATIVE AMERICAN VETERAN DIRECT LOAN PROGRAM FY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/ggvb-7ke9",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "missouri"
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
-            "identifier": "https://www.data.va.gov/api/views/ggvb-7ke9",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Missouri",
+            "identifier": "https://www.data.va.gov/api/views/ggvb-7ke9",
+            "issued": "2021-08-26",
+            "keyword": [
+                "missouri"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ggvb-7ke9",
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
+            "title": "State Summaries_Missouri"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ghg2-4a5i",
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
-            "identifier": "ea707306-194e-4946-ab2b-14b258280f95",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Louisiana FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44719,42 +44703,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "ea707306-194e-4946-ab2b-14b258280f95",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ghg2-4a5i",
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
+            "title": "State Summary Louisiana FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/FY11_June_EDU_recp_by_Training_Type.csv",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-06-01T04:00:00Z/2011-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/FY11_June_EDU_recp_by_Training_Type.csv"
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
-            "identifier": "VA-VBA-EDU2011-003",
+            "dataQuality": true,
             "description": "<p>FY 11 Education Recipients by training type  and VA Education Benefit Program (Through June FY11). The data represents the number of individuals by VA education program who have used their VA education benefit during fiscal year 2011(Through the June FY11). Training type statistics may include individuals who used their education benefits in more than one training type, therefore the total within this table may be different than the total number of beneficiaries during the fiscal year.</p>",
-            "title": "FY 11 (June) Education Recipients by Training Type and VA Education Benefit Program",
-            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44762,61 +44742,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ghjs-83a9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ghjs-83a9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ghjs-83a9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ghjs-83a9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ghjs-83a9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ghjs-83a9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ghjs-83a9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ghjs-83a9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ghjs-83a9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-EDU2011-003",
+            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "education",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/FY11_June_EDU_recp_by_Training_Type.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/FY11_June_EDU_recp_by_Training_Type.csv"
+            ],
+            "temporal": "2011-06-01T04:00:00Z/2011-06-30T04:00:00Z",
             "theme": [
                 "Section 4. Education"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 11 (June) Education Recipients by Training Type and VA Education Benefit Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/gidu-8zyi",
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
-            "identifier": "https://www.data.va.gov/api/views/gidu-8zyi",
             "description": "These data are based on the latest Veteran Population Projection Model, VetPop2020, provided by the National Center for Veterans Statistics and Analysis, published in 2023.",
-            "title": "FY 2021_NCVAS Vet Pop Gender Over Time Data For State Summaries",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44824,42 +44811,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gidu-8zyi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gidu-8zyi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gidu-8zyi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/gidu-8zyi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gidu-8zyi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gidu-8zyi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gidu-8zyi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gidu-8zyi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gidu-8zyi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/gidu-8zyi",
+            "issued": "2023-06-14",
+            "landingPage": "https://www.data.va.gov/d/gidu-8zyi",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021_NCVAS Vet Pop Gender Over Time Data For State Summaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gism-vg66",
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
+            "description": "<p>Ventilator Associated Pnemonia, Central Line associate bacteremia, methicillin resistant staph aureus (MRSA), and hospital acquired pressure ulcers.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset7_Nosocomial.xml",
+                    "mediaType": "application/xml",
+                    "title": "Nosocomial Infection"
+                }
             ],
+            "identifier": "VA-VHA-OIA-043",
+            "isPartOf": "VA-VHA-OIA-584",
+            "issued": "2017-07-26",
             "keyword": [
                 "ambulatory",
                 "care",
@@ -44882,69 +44894,42 @@
                 "urban",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/gism-vg66",
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
-            "identifier": "VA-VHA-OIA-043",
-            "description": "<p>Ventilator Associated Pnemonia, Central Line associate bacteremia, methicillin resistant staph aureus (MRSA), and hospital acquired pressure ulcers.</p>",
-            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Nosocomial Infection",
-            "isPartOf": "VA-VHA-OIA-584",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset7_Nosocomial.xml",
-                    "mediaType": "application/xml",
-                    "title": "Nosocomial Infection"
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
+            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Nosocomial Infection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gjcf-cerz",
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
-            "identifier": "https://www.data.va.gov/api/views/gjcf-cerz",
+            "dataQuality": true,
             "description": "VA All Employee Survey (AES) 2021 deidentified individual-level public release data file.",
-            "title": "AES 2021 PRDF",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44952,59 +44937,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gjcf-cerz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gjcf-cerz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gjcf-cerz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/gjcf-cerz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gjcf-cerz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gjcf-cerz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gjcf-cerz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gjcf-cerz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gjcf-cerz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/gjcf-cerz",
+            "issued": "2023-03-16",
+            "keyword": [
+                "survey",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gjcf-cerz",
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
+            "title": "AES 2021 PRDF"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gjyg-vmxu",
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
-            "identifier": "https://www.data.va.gov/api/views/gjyg-vmxu",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to compensate veterans for disabilities incurred or aggravated during military service according to the average impairment in earning capacity such disability would cause in civilian occupations. Persons who have suffered disabilities resulting from service in the Armed Forces of the United States. The disability must have been incurred or aggravated by service in the line of duty. Separation from service must have been under other than dishonorable conditions for the period in which the disability was incurred or aggravated.</p>",
-            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY FEB2019",
-            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45012,61 +44996,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gjyg-vmxu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gjyg-vmxu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gjyg-vmxu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/gjyg-vmxu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gjyg-vmxu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gjyg-vmxu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gjyg-vmxu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gjyg-vmxu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gjyg-vmxu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/gjyg-vmxu",
+            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 109"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gjyg-vmxu",
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
+            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY FEB2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gk4d-q9ng",
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
-            "identifier": "b312c985-2a4d-4bdb-ac92-9b4859851908",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Rhode Island FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45074,44 +45058,42 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "b312c985-2a4d-4bdb-ac92-9b4859851908",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gk4d-q9ng",
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
+            "title": "State Summary Rhode Island FY2017"
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
-            "identifier": "VA-OEI-OEI-148",
             "description": "<p>This reports the activities of the Veterans Administration for the fiscal year ending September 30, 1985.</p>",
-            "title": "Annual Report:  1985",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45120,38 +45102,43 @@
                     "title": "Annual Report:  1985"
                 }
             ],
+            "identifier": "VA-OEI-OEI-148",
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
+            "title": "Annual Report:  1985"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/gku4-akgj",
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
-            "identifier": "https://www.data.va.gov/api/views/gku4-akgj",
             "description": "",
-            "title": "vetpop_race_ethnicity",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45159,39 +45146,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gku4-akgj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gku4-akgj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gku4-akgj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/gku4-akgj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gku4-akgj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gku4-akgj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gku4-akgj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gku4-akgj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gku4-akgj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/gku4-akgj",
+            "issued": "2024-04-19",
+            "landingPage": "https://www.data.va.gov/d/gku4-akgj",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-05-02",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "vetpop_race_ethnicity"
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
+            "description": "<p>This reports shows a summary level view of projects that comprise VA\u00ef\u00bf\u00bds IT development activities.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oit.va.gov/docs/dashboard/201301_OIT_PMAS_Dashboard_Summary_Jan_2013.pdf",
+                    "mediaType": "text/html",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-PD-03",
             "issued": "2017-07-26",
-            "temporal": "2012-09-30T04:00:00Z/2013-04-02T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "active",
                 "closed",
@@ -45211,50 +45223,53 @@
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
-            "identifier": "VA-OIT-PD-03",
-            "description": "<p>This reports shows a summary level view of projects that comprise VA\u00ef\u00bf\u00bds IT development activities.</p>",
-            "title": "Department of Veterans Affairs - Office of Information Technology Program Management Accountability Dashboard  Summary",
-            "programCode": [
-                "029:079"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oit.va.gov/docs/dashboard/201301_OIT_PMAS_Dashboard_Summary_Jan_2013.pdf",
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
+            "title": "Department of Veterans Affairs - Office of Information Technology Program Management Accountability Dashboard  Summary"
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR36_122015_Retrospective_Wait_Times_Desired_Date_by_Division.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Appointments 30 Nov 2015"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-434",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-11-30T05:00:00Z/2015-11-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -45268,51 +45283,49 @@
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
-            "identifier": "VA-VHA-OIA-434",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Nov 30",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR36_122015_Retrospective_Wait_Times_Desired_Date_by_Division.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Appointments 30 Nov 2015"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2015-11-30T05:00:00Z/2015-11-30T05:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Nov 30"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gnx8-swzk",
             "bureauCode": [
                 "029:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lighthouse Support",
+                "hasEmail": "mailto:api@va.gov"
+            },
+            "description": "Use the VA Facility API to find relevant information about a specific VA facility. For each VA facility, you'll find contact information, location, hours of operation and available services. For medical facilities only, we provide data on appointment wait times and patient satisfaction. The documentation is hosted by Lighthouse, a Veteran-centered API platform for securely accessing VA data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Use the VA Facility API to find relevant information about a specific VA facility. For each VA facility, you'll find contact information, location, hours of operation and available services. For medical facilities only, we provide data on appointment wait times and patient satisfaction. The documentation is hosted by Lighthouse, a Veteran-centered API platform for securely accessing VA data.",
+                    "downloadURL": "https://developer.va.gov/explore/facilities",
+                    "mediaType": "text/html",
+                    "title": "VA Facilities API"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/gnx8-swzk",
             "issued": "2021-01-22",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-22",
             "keyword": [
                 "api",
                 "api documentation",
@@ -45322,60 +45335,30 @@
                 "open data",
                 "va facilities"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lighthouse Support",
-                "hasEmail": "mailto:api@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/gnx8-swzk",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-01-22",
+            "programCode": [
+                "029:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/gnx8-swzk",
-            "description": "Use the VA Facility API to find relevant information about a specific VA facility. For each VA facility, you'll find contact information, location, hours of operation and available services. For medical facilities only, we provide data on appointment wait times and patient satisfaction. The documentation is hosted by Lighthouse, a Veteran-centered API platform for securely accessing VA data.",
-            "title": "VA Facilities API",
-            "programCode": [
-                "029:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://developer.va.gov/explore/facilities",
-                    "description": "Use the VA Facility API to find relevant information about a specific VA facility. For each VA facility, you'll find contact information, location, hours of operation and available services. For medical facilities only, we provide data on appointment wait times and patient satisfaction. The documentation is hosted by Lighthouse, a Veteran-centered API platform for securely accessing VA data.",
-                    "@type": "dcat:Distribution",
             "title": "VA Facilities API"
-                }
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/gprx-3uk9",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-09-25",
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
-            "identifier": "https://www.data.va.gov/api/views/gprx-3uk9",
             "description": "",
-            "title": "Race Ethnicity Distribution FY2023_FY2050",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45383,40 +45366,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gprx-3uk9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gprx-3uk9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gprx-3uk9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/gprx-3uk9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gprx-3uk9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gprx-3uk9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gprx-3uk9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gprx-3uk9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gprx-3uk9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/gprx-3uk9",
+            "issued": "2024-09-25",
+            "keyword": [
+                "veteran population",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gprx-3uk9",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-12-10",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Race Ethnicity Distribution FY2023_FY2050"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/gpsy-h2vx",
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
+            "description": "<p>The Community Residential Care Report is a listing of all facilities approved for residential care by the VA. These facilities are privately run operations not affiliated with the VA. They provide room, board, supervision, and other non-medical care to Veteran patients who cannot care for themselves but do not require the services of a Veterans Affairs Medical Center (VAMC). Information about these facilities is entered into the Fee Basis module of the Veterans Health Information Systems and Technology Architecture (VistA) by every VAMC that has an agreement with a facility. This information is sent via MailMan to the VA Austin Information Technology Center where it is collected in a queue and processed quarterly. VAMCs that have sent invalid data or VAMCs that are aligned with residential care facilities and did not send data are notified. Valid data is processed and used to update the database. Quarterly reports are sent to VAMCs, Veterans Integrated Service Networks (VISNs), Geriatrics &amp; Extended Care Strategic Health Care Group, VA Central Office (VACO), and researchers interested in residential care information.</p>",
+            "identifier": "VA-VHA-GER-002",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1982-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "approved",
                 "community",
@@ -45428,61 +45431,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/gpsy-h2vx",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:055"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-GER-002",
-            "description": "<p>The Community Residential Care Report is a listing of all facilities approved for residential care by the VA. These facilities are privately run operations not affiliated with the VA. They provide room, board, supervision, and other non-medical care to Veteran patients who cannot care for themselves but do not require the services of a Veterans Affairs Medical Center (VAMC). Information about these facilities is entered into the Fee Basis module of the Veterans Health Information Systems and Technology Architecture (VistA) by every VAMC that has an agreement with a facility. This information is sent via MailMan to the VA Austin Information Technology Center where it is collected in a queue and processed quarterly. VAMCs that have sent invalid data or VAMCs that are aligned with residential care facilities and did not send data are notified. Valid data is processed and used to update the database. Quarterly reports are sent to VAMCs, Veterans Integrated Service Networks (VISNs), Geriatrics &amp; Extended Care Strategic Health Care Group, VA Central Office (VACO), and researchers interested in residential care information.</p>",
-            "title": "Community Residential Care Report",
-            "programCode": [
-                "029:055"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1982-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Community Residential Care Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gq5a-76wh",
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
-            "identifier": "https://www.data.va.gov/api/views/gq5a-76wh",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to encourage membership in units of the Selected Reserve of the Ready Reserve and to provide educational assistance to members of the reserve components called or ordered to active service in response to a war or national emergency declared by the President or Congress. Generally, to qualify for benefits under MGIB-SR you must (1) Have a six-year obligation to serve in the Selected Reserve signed after June 30, 1985. If you are an officer, you must have agreed to serve six years in addition to your original obligation. For some types of training, it is necessary to have a six-year commitment that begins after September 30, 1990; (2) Complete your initial active duty for training (IADT); (3) Meet the requirement to receive a high school diploma or equivalency certificate before completing IADT. You may not use 12 hours toward a college degree to meet this requirement; and (4) Remain in good standing while serving in an active Selected Reserve unit. Generally, to qualify for benefits under REAP you must have served at least 90 consecutive days on active duty as a result of a call or order to active duty from a reserve component in response to a war or national emergency declared by the President or Congress. This is not a complete list of eligibility requirements. For more information on MGIB-SR and REAP visit <a href=\"http://www.gibill.va.gov\">http://www.gibill.va.gov</a>.</p>",
-            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM NOV2018",
-            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45490,62 +45474,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gq5a-76wh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gq5a-76wh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gq5a-76wh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/gq5a-76wh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gq5a-76wh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gq5a-76wh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gq5a-76wh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gq5a-76wh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gq5a-76wh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/gq5a-76wh",
+            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 032"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gq5a-76wh",
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
+            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM NOV2018"
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
-            "temporal": "2010-10-01T04:00:00Z/2010-12-31T05:00:00Z",
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
-            "identifier": "VA-OM-OM-089",
+            "dataQuality": true,
             "description": "<p>FY 2011 First Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2011 First Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45554,26 +45538,55 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-089",
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
+            "temporal": "2010-10-01T04:00:00Z/2010-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2011 First Quarter High-Dollar Overpayments Report"
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
+            "description": "<p>This map presents a visual portrayal of the state level data contained in the Geographic Distribution of VA Expenditures report.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/vetdata/Expenditures.asp",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-039",
             "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -45587,67 +45600,38 @@
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
-            "identifier": "VA-OEI-OEI-039",
-            "description": "<p>This map presents a visual portrayal of the state level data contained in the Geographic Distribution of VA Expenditures report.</p>",
-            "title": "Geographic Distribution of VA Expenditures State Map",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/vetdata/Expenditures.asp",
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
+            "title": "Geographic Distribution of VA Expenditures State Map"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gqje-dcyx",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-08-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-19",
-            "keyword": [
-                "gdx",
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
-            "identifier": "990a9c91-2375-4c36-8a7a-b2ff33d38ed4",
+            "dataQuality": true,
             "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also included.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY 2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45656,37 +45640,37 @@
                     "title": "GDX FY 2016"
                 }
             ],
+            "identifier": "990a9c91-2375-4c36-8a7a-b2ff33d38ed4",
+            "issued": "2017-08-15",
+            "keyword": [
+                "gdx",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gqje-dcyx",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2024-11-19",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Geographic Distribution of VA Expenditures FY 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gqp7-piic",
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
-            "identifier": "2adba268-cbbd-4892-8b3a-25650ae93a43",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Mississippi FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45694,37 +45678,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "2adba268-cbbd-4892-8b3a-25650ae93a43",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gqp7-piic",
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
+            "title": "State Summary Mississippi FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/grhe-aj8i",
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
-            "identifier": "https://www.data.va.gov/api/views/grhe-aj8i",
             "description": "",
-            "title": "Distribution of Veteran's Employment Status by Gender",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45732,57 +45715,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/grhe-aj8i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/grhe-aj8i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/grhe-aj8i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/grhe-aj8i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/grhe-aj8i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/grhe-aj8i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/grhe-aj8i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/grhe-aj8i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/grhe-aj8i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/grhe-aj8i",
+            "issued": "2024-07-29",
+            "keyword": [
+                "veterans",
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/grhe-aj8i",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-12-10",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Distribution of Veteran's Employment Status by Gender"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gsb2-dkk8",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2019-09-16",
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
-            "identifier": "https://www.data.va.gov/api/views/gsb2-dkk8",
             "description": "The National Veteran Health Equity Report details patterns and provides comparative rates of health conditions for vulnerable Veteran groups. Specifically, this report is designed to provide basic comparative information on the sociodemographics, utilization patterns and rates of diagnosed health conditions among the groups over which the VHA Office of Health Equity (OHE) has responsibility with respect to monitoring, evaluating and acting on identified disparities in access, use, care, quality and outcomes. The report allows the VA, Veterans, and stakeholders to monitor the care vulnerable Veterans receive and set goals for improving their care.",
-            "title": "National Veteran Health Equity Report - FY13",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45790,58 +45773,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gsb2-dkk8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gsb2-dkk8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gsb2-dkk8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/gsb2-dkk8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gsb2-dkk8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gsb2-dkk8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gsb2-dkk8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gsb2-dkk8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gsb2-dkk8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/gsb2-dkk8",
+            "issued": "2019-09-16",
+            "keyword": [
+                "healthcare",
+                "health equity"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gsb2-dkk8",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-07-19",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "National Veteran Health Equity Report - FY13"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gsbe-ntk4",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "2013",
-                "2020",
-                "roadmap"
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
-            "identifier": "VA-OIT-OIT-059",
             "description": "<p>This Department of Veterans Affairs (VA) IT Roadmap FY 2013-2020 describes VA\u2019s information technology (IT) vision. The Roadmap looks at specific emerging innovations, and projects their role and impact on future VA operations</p>",
-            "title": "2012 Information Technology Roadmap",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45850,43 +45832,42 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OIT-OIT-059",
+            "issued": "2017-07-26",
+            "keyword": [
+                "2013",
+                "2020",
+                "roadmap"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gsbe-ntk4",
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
+            "title": "2012 Information Technology Roadmap"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gsm5-6qui",
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
-            "identifier": "https://www.data.va.gov/api/views/gsm5-6qui",
             "description": "Percentage of Service-Connected Disable Who Did and Did Not Use Health Care, by Disability Rating, FY 2018. Data underlying the third figure of Part 3 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 16, Percentage of Service-Connected Disable Who Did and Did Not Use Health Care, by Disability Rating",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45894,58 +45875,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gsm5-6qui/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gsm5-6qui/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gsm5-6qui/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/gsm5-6qui/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gsm5-6qui/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gsm5-6qui/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gsm5-6qui/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gsm5-6qui/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gsm5-6qui/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/gsm5-6qui",
+            "issued": "2020-11-19",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gsm5-6qui",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2020-12-22",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 16, Percentage of Service-Connected Disable Who Did and Did Not Use Health Care, by Disability Rating"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/gtcd-azge",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-02-19",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-21",
-            "keyword": [
-                "take-up rate",
-                "va benefits",
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
-            "identifier": "https://www.data.va.gov/api/views/gtcd-azge",
             "description": "Take-up rate of Veterans within 2 years of transitioning out of military service by race and ethnicity",
-            "title": "Take-up Rate within 2 FYs by Race/Ethnicity",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45953,61 +45935,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gtcd-azge/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gtcd-azge/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gtcd-azge/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/gtcd-azge/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gtcd-azge/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gtcd-azge/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gtcd-azge/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gtcd-azge/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gtcd-azge/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/gtcd-azge",
+            "issued": "2021-02-19",
+            "keyword": [
+                "take-up rate",
+                "va benefits",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gtcd-azge",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-02-21",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Take-up Rate within 2 FYs by Race/Ethnicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VHA/blob/master/HIV%20Infected%20Veterans%20in%20VHA%20Care-2011-2015%20Nation-VISN-Station.xlsx",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-01-11T05:00:00Z/2015-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
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
-            "identifier": "VA-VHA-PCS-022",
-            "description": "<p>This report describes the number of HIV Infected Veterans in VHA care in each year, 2011 through 2015.</p>",
-            "title": "HIV Infected Veterans in VHA Care in 2011 through 2015, for the Nation, by VISN and by Station",
+            "dataQuality": true,
+            "describedBy": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VHA/blob/master/HIV%20Infected%20Veterans%20in%20VHA%20Care-2011-2015%20Nation-VISN-Station.xlsx",
             "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:041"
-            ],
+            "description": "<p>This report describes the number of HIV Infected Veterans in VHA care in each year, 2011 through 2015.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46016,45 +45999,45 @@
                     "title": "HIVInfectedVeterans2011-2015"
                 }
             ],
-            "describedBy": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VHA/blob/master/HIV%20Infected%20Veterans%20in%20VHA%20Care-2011-2015%20Nation-VISN-Station.xlsx",
-            "dataQuality": true,
+            "identifier": "VA-VHA-PCS-022",
+            "issued": "2017-07-26",
+            "keyword": [
+                "hiv",
+                "human immunodeficiency virus",
+                "veterans",
+                "vha"
+            ],
+            "landingPage": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VHA/blob/master/HIV%20Infected%20Veterans%20in%20VHA%20Care-2011-2015%20Nation-VISN-Station.xlsx",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-01-11T05:00:00Z/2015-12-31T05:00:00Z",
             "theme": [
                 "HIV Infected Veterans in VHA Care"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HIV Infected Veterans in VHA Care in 2011 through 2015, for the Nation, by VISN and by Station"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gvcn-mezt",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "massachusetts",
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
-            "identifier": "VA-OEI-OEI-108",
             "description": "<p>This is a summary of the programs and services provided by VA in Massachusetts in fiscal year 2014.</p>",
-            "title": "State Summary:  Massachusetts",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46063,40 +46046,45 @@
                     "title": "State Summary:  Massachusetts"
                 }
             ],
+            "identifier": "VA-OEI-OEI-108",
+            "issued": "2017-07-26",
+            "keyword": [
+                "massachusetts",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gvcn-mezt",
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
+            "title": "State Summary:  Massachusetts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gvvi-qbx9",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2025-01-30",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA National Center for Organization Development (NCOD)",
                 "hasEmail": "mailto:vhancod@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/gvvi-qbx9",
             "description": "2024 VA All Employee Survey (AES) deidentified individual-level public dataset",
-            "title": "AES 2024 PRDF",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46104,60 +46092,55 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gvvi-qbx9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gvvi-qbx9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gvvi-qbx9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/gvvi-qbx9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gvvi-qbx9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gvvi-qbx9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gvvi-qbx9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gvvi-qbx9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gvvi-qbx9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/gvvi-qbx9",
+            "issued": "2025-01-30",
+            "landingPage": "https://www.data.va.gov/d/gvvi-qbx9",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2025-01-30",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "AES 2024 PRDF"
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
-            "temporal": "2014-07-01T04:00:00Z/2014-09-30T04:00:00Z",
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
-            "identifier": "VA-OEI-OEI-055",
+            "dataQuality": true,
             "description": "<p>NCVAS Pocket Cards archives are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs (VA) benefits and health care utilization.</p>",
-            "title": "VA Benefits & Health Care Utilization",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46166,47 +46149,47 @@
                     "title": "VA Benefits and Health Care Utilization"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-055",
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
+            "temporal": "2014-07-01T04:00:00Z/2014-09-30T04:00:00Z",
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
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/gx6m-ae5x",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-04-28",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-12",
-            "keyword": [
-                "dic benefits",
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
-            "identifier": "https://www.data.va.gov/api/views/gx6m-ae5x",
+            "dataQuality": true,
             "description": "All DIC Recipients by the Period of Service of the Veterans. DIC is a tax-free monetary benefit generally payable to a surviving spouse, child, or parent of deceased Servicemembers or Veterans.",
-            "title": "All Dependency and Indemnity Compensation (DIC) Recipients By Veterans' Period of Service FY2020",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46214,41 +46197,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gx6m-ae5x/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gx6m-ae5x/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gx6m-ae5x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/gx6m-ae5x/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gx6m-ae5x/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gx6m-ae5x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gx6m-ae5x/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gx6m-ae5x/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gx6m-ae5x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/gx6m-ae5x",
+            "issued": "2022-04-28",
+            "keyword": [
+                "dic benefits",
+                "veterans",
+                "veterans surviving spouses and children"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gx6m-ae5x",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2022-05-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "All Dependency and Indemnity Compensation (DIC) Recipients By Veterans' Period of Service FY2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/gxdt-nw55",
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
+            "description": "<p>VA's Managerial Cost Accounting System is the designated Managerial Cost Accounting (MCA) System of the Department of Veterans Affairs. This system is the Department's only means of complying with Public Laws (e.g., PL 101-576 - the Chief Financial Officers Act of 1990) that mandate the use of a MCA system that can assign costs to the product level. MCA cost data is used at all levels of the VA for important functions, such as cost recovery (billing), budgeting and resource allocation. Additionally, the system contains a rich repository of clinical information which is used to promote a more proactive approach to the care of high risk (i.e., diabetes and acute coronary patients) and high cost patients. The data in MCA is also used to calculate and measure the productivity of physicians and other care providers.</p>",
+            "identifier": "VA-VHA-OF-002",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1999-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2022-10-05",
             "keyword": [
                 "accounting",
                 "billing",
@@ -46263,91 +46266,72 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/gxdt-nw55",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-10-05",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OF-002",
-            "description": "<p>VA's Managerial Cost Accounting System is the designated Managerial Cost Accounting (MCA) System of the Department of Veterans Affairs. This system is the Department's only means of complying with Public Laws (e.g., PL 101-576 - the Chief Financial Officers Act of 1990) that mandate the use of a MCA system that can assign costs to the product level. MCA cost data is used at all levels of the VA for important functions, such as cost recovery (billing), budgeting and resource allocation. Additionally, the system contains a rich repository of clinical information which is used to promote a more proactive approach to the care of high risk (i.e., diabetes and acute coronary patients) and high cost patients. The data in MCA is also used to calculate and measure the productivity of physicians and other care providers.</p>",
-            "title": "Managerial Cost Accounting System",
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
+            "title": "Managerial Cost Accounting System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/gy6f-knf3",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Pennsylvania FY2023",
+            "identifier": "https://www.data.va.gov/api/views/gy6f-knf3",
             "issued": "2024-06-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "pennsylvania"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/gy6f-knf3",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/gy6f-knf3",
-            "description": "NCVAS State Summary Pennsylvania FY2023",
-            "title": "NCVAS State Summary Pennsylvania FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Pennsylvania FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gydc-nbsc",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "center for women veterans",
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
-            "identifier": "7c949270-5727-4604-a295-f66bd065679f",
+            "dataQuality": true,
             "description": "<p>\u00a0The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.\u00a0</p>",
-            "title": "State Summary Idaho FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46355,48 +46339,44 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "7c949270-5727-4604-a295-f66bd065679f",
+            "issued": "2018-10-30",
+            "keyword": [
+                "center for women veterans",
+                "demographics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/gydc-nbsc",
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
+            "title": "State Summary Idaho FY2017"
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
-                "@type": "vcard:Contact",
-                "fn": "Thomas Elwell",
-                "hasEmail": "mailto:thomas.elwell@va.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
+                "@type": "vcard:Contact",
+                "fn": "Thomas Elwell",
+                "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "identifier": "VA-VBA-ABR2012-058",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Insurance Monthly Installment Award Payments to Policy holders at the End of Fiscal Year 2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46405,26 +46385,59 @@
                     "title": "Insurance Monthly Installment Award Payments to Policy holders at the End of Fiscal Year 2012"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-058",
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
+            "title": "Insurance Monthly Installment Award Payments to Policy holders at the End of Fiscal Year 2012"
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
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2005.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2005.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-09",
             "issued": "2017-07-26",
-            "temporal": "2004-10-01T04:00:00Z/2005-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "2005",
                 "appeals",
@@ -46441,73 +46454,41 @@
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
-            "identifier": "VA-OIT-ITIS-09",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2005.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2005",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2005.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2004-10-01T04:00:00Z/2005-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/gzft-mcxr",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2022-09-28",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-11",
-            "keyword": [
-                "parent study",
-                "primary study",
-                "ptsd-repository",
-                "reference",
-                "secondary study"
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
-            "identifier": "https://www.data.va.gov/api/views/gzft-mcxr",
+            "dataQuality": true,
             "description": "Records references to secondary studies and companion publications included with primary studies in the PTSD-Repository.\nThese secondary, referenced studies may or may not have contributed data to the abstraction of the listed primary study. The relationship of the secondary study to the primary study is described in some cases in the `Secondary Study Relationship` column.",
-            "title": "Secondary Studies",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46515,101 +46496,107 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gzft-mcxr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gzft-mcxr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gzft-mcxr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/gzft-mcxr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gzft-mcxr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gzft-mcxr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/gzft-mcxr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/gzft-mcxr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/gzft-mcxr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "PTSD-Repository"
+            "identifier": "https://www.data.va.gov/api/views/gzft-mcxr",
+            "issued": "2022-09-28",
+            "keyword": [
+                "parent study",
+                "primary study",
+                "ptsd-repository",
+                "reference",
+                "secondary study"
             ],
+            "landingPage": "https://www.data.va.gov/d/gzft-mcxr",
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
+            "title": "Secondary Studies"
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
+            "description": "<p>Benefits for Filipino Veterans</p>",
+            "identifier": "VA-VBA-MEDIAPUB-057",
+            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
             "issued": "2017-07-26",
-            "temporal": "2008-10-01T04:00:00Z/2008-10-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-04",
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
+            "modified": "2022-03-04",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-MEDIAPUB-057",
-            "description": "<p>Benefits for Filipino Veterans</p>",
-            "title": "Benefits for Filipino Veterans",
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
+            "title": "Benefits for Filipino Veterans"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/h288-dcw4",
-            "issued": "2023-06-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-25",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/h288-dcw4",
             "description": "These data are based on the latest Veteran Population Projection Model, VetPop2020, provided by the National Center for Veterans Statistics and Analysis, published in 2023.",
-            "title": "FY 2021_NCVAS Age Group over time Data For State Summary bar chart",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46617,64 +46604,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/h288-dcw4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h288-dcw4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h288-dcw4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/h288-dcw4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h288-dcw4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h288-dcw4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/h288-dcw4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h288-dcw4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h288-dcw4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/h288-dcw4",
+            "issued": "2023-06-14",
+            "landingPage": "https://www.data.va.gov/d/h288-dcw4",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-25",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021_NCVAS Age Group over time Data For State Summary bar chart"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Policyholders_by_Program_by_State_August2012.CSV",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-08-01T04:00:00Z/2012-08-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Policyholders_by_Program_August_2012.doc"
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
-            "identifier": "VA-VBA-INS2012-015",
+            "dataQuality": true,
             "description": "<p>Number of life insurance policyholders for each administered life insurance program listed by state. Data is current as of 08/31/12.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Provides number of life insurance policyholders for each program by state as of 08/31/12.",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46682,67 +46659,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/h2cv-5fuq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h2cv-5fuq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h2cv-5fuq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/h2cv-5fuq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h2cv-5fuq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h2cv-5fuq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/h2cv-5fuq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h2cv-5fuq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h2cv-5fuq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-015",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "county",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Policyholders_by_Program_by_State_August2012.CSV",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Policyholders_by_Program_August_2012.doc"
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
+            "title": "Provides number of life insurance policyholders for each program by state as of 08/31/12."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/h2hx-dr22",
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
-            "identifier": "VA-OGC-049",
             "description": "<p>Surviving Spouse's Benefit for Month of Veteran's Death - 38 U.S.C. \u00a7 5310(b)</p>",
-            "title": "OGC Precedent Opinion 2-2009",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46751,41 +46733,42 @@
                     "title": "OGC Precedent Opinion 2-2009"
                 }
             ],
+            "identifier": "VA-OGC-049",
+            "issued": "2017-07-26",
+            "keyword": [
+                "official opinion",
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.data.va.gov/d/h2hx-dr22",
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
+            "title": "OGC Precedent Opinion 2-2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/h34h-n6mf",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "north dakota",
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
-            "identifier": "VA-OEI-OEI-120",
             "description": "<p>This is a summary of the programs and services provided by VA in North Dakota in fiscal year 2014.</p>",
-            "title": "State Summary:  North Dakota",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46794,45 +46777,44 @@
                     "title": "State Summary:  North Dakota"
                 }
             ],
+            "identifier": "VA-OEI-OEI-120",
+            "issued": "2017-07-26",
+            "keyword": [
+                "north dakota",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/h34h-n6mf",
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
+            "title": "State Summary:  North Dakota"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/h3ca-xjk8",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-02-18",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-23",
-            "keyword": [
-                "life insurance",
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
-            "identifier": "https://www.data.va.gov/api/views/h3ca-xjk8",
             "description": "Life Insurance: All Veterans who had an active VA life insurance policy or were in receipt of a benefit from a policy that was administered or supervised by VA were included. VA insurance programs included in the analysis were National Service Life Insurance (NSLI), United States Government Life Insurance (USGLI), Veterans\u2019 Special Life Insurance (VSLI), Veterans\u2019 Reopened Insurance (VRI), Service-Disabled Veterans Insurance (S-DVI), Veterans\u2019 Mortgage Life Insurance (VMLI), Traumatic Injury Protection (TSGLI), and Veterans\u2019 Group Life Insurance (VGLI). The analysis does not include Service-members\u2019 Group Life Insurance (SGLI) and Family Service-members\u2019 Group Life Insurance (FSGLI). Veterans Benefits Administration (VBA) provides Life Insurance.",
-            "title": "Veterans who used VA Life Insurance Benefits",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46840,61 +46822,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/h3ca-xjk8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h3ca-xjk8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h3ca-xjk8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/h3ca-xjk8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h3ca-xjk8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h3ca-xjk8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/h3ca-xjk8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h3ca-xjk8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h3ca-xjk8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "State",
-            "license": "https://www.usa.gov/government-works",
+            "identifier": "https://www.data.va.gov/api/views/h3ca-xjk8",
+            "issued": "2021-02-18",
+            "keyword": [
+                "life insurance",
+                "veteran",
+                "veteran benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/h3ca-xjk8",
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
+            "title": "Veterans who used VA Life Insurance Benefits"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/h42r-hhyg",
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
                 "hasEmail": "mailto:Vikki.Soikup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-140",
+            "dataQuality": true,
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 145 July 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46902,43 +46886,43 @@
                     "mediaType": "text/plain"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-140",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/h42r-hhyg",
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
+            "title": "COIN 145 July 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/h47x-g42d",
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
-            "identifier": "d081c6f1-96e9-425e-961a-1c92bc96be31",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Maine FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46946,68 +46930,66 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "d081c6f1-96e9-425e-961a-1c92bc96be31",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/h47x-g42d",
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
+            "title": "State Summary Maine FY2017"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/h5jm-kreq",
-            "issued": "2023-07-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-09",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Massachusetts FY2021",
+            "identifier": "https://www.data.va.gov/api/views/h5jm-kreq",
+            "issued": "2023-07-03",
             "keyword": [
                 "fy2021 data",
                 "massachusetts",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/h5jm-kreq",
+            "landingPage": "https://www.data.va.gov/d/h5jm-kreq",
+            "modified": "2024-06-09",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Massachusetts FY2021",
             "title": "NCVAS State Summary Massachusetts FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/h5zp-pekf",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2021-02-19",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-19",
-            "keyword": [
-                "social determinanats of health",
-                "suicide prevention",
-                "synthetic"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Amanda Purnell",
-                "hasEmail": "mailto:amanda.purnell@va.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
+                "hasEmail": "mailto:amanda.purnell@va.gov"
             },
-            "identifier": "https://www.data.va.gov/api/views/h5zp-pekf",
             "description": "The included dataset contains 10,000 synthetic Veteran patient records generated by Synthea. The scope of the data includes over 500 clinical concepts across 90 disease modules, as well as additional social determinants of health (SDoH) data elements that are not traditionally tracked in electronic health records. Each synthetic patient conceptually represents one Veteran in the existing US population; each Veteran\nhas a name, sociodemographic profile, a series of documented clinical encounters and diagnoses, as well as associated cost and payer data. To learn more about Synthea, please visit the Synthea wiki at https://github.com/synthetichealth/synthea/wiki. To find a description of how this dataset is organized by data type, please visit the Synthea CSV File Data Dictionary at https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary.The included dataset contains 10,000 synthetic Veteran patient records generated by Synthea. The scope of the data includes over 500 clinical concepts across 90 disease modules, as well as additional social determinants of health (SDoH) data elements that are not traditionally tracked in electronic health records.\nEach synthetic patient conceptually represents one Veteran in the existing US population; each Veteran has a name, sociodemographic profile, a series of documented clinical encounters and diagnoses, as well as associated cost and payer data. To learn more about Synthea, please visit the Synthea wiki at https://github.com/synthetichealth/synthea/wiki. To find a description of how this dataset is organized by data type, please visit the Synthea CSV File Data Dictionary at\nhttps://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary.",
-            "title": "Synthetic Suicide Prevention Dataset with SDoH",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47015,36 +46997,38 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/h5zp-pekf",
+            "issued": "2021-02-19",
+            "keyword": [
+                "social determinanats of health",
+                "suicide prevention",
+                "synthetic"
+            ],
+            "landingPage": "https://www.data.va.gov/d/h5zp-pekf",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-02-19",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Synthetic Suicide Prevention Dataset with SDoH"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/h66j-6w57",
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
-            "identifier": "https://www.data.va.gov/api/views/h66j-6w57",
+            "dataQuality": true,
             "description": "<p>VBA SPECIALLY ADAPTED HOUSING BENEFIT PROGRAMS. The Specially Adapted Housing (SAH) grant program helps Veterans with certain service-connected disabilities live independently in a barrier-free environment. SAH grants can be used in one of the following ways: (1) construct a suitable home on suitable land either already owned or to be acquired by the veteran, or (2) remodel an existing home if it can be suitably adapted, or (3) acquire a suitably adapted home or reduce the outstanding mortgage on a suitably adapted home already owned by the veteran. b. The Special Housing Adaptation (SHA) grant program helps veterans with certain service-connected disabilities adapt or purchase a home to accommodate the disability. SHA grants can be used in one of the following ways: (1) adapt an existing home the veteran or a family member already owns in which the veteran lives; (2) adapt a home the veteran or family member intends to purchase in which the veteran will live; (3) help a veteran purchase a home already adapted in which the veteran will live. c. . The Temporary Residence Adaptations (TRA) program provides adaptation assistance to veterans who are residing, but do not intend to permanently reside, in the a residence owned by a family member. If a veteran is otherwise eligible for SAH or SHA, the assistance is limited. d. SAH and SHA grants may be used up to three times, as long as the aggregate grant amount does not exceed the statutory dollar limitation. TRA grants may only be used once (and count as a grant usage for purposes of the limit of three), and the amount of assistance provided will be subtracted from the veteran's available statutory maximum.</p>",
-            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS APR2019",
-            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47052,147 +47036,146 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/h66j-6w57/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h66j-6w57/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h66j-6w57/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/h66j-6w57/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h66j-6w57/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h66j-6w57/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/h66j-6w57/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h66j-6w57/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h66j-6w57/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/h66j-6w57",
+            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 106"
+            ],
+            "landingPage": "https://www.data.va.gov/d/h66j-6w57",
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
+            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS APR2019"
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
+            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- January 2014</p>",
+            "identifier": "VA-VBA-USASPENDING012014-029",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING012014-029",
-            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- January 2014</p>",
-            "title": "USA Spending file- 01/2014-Direct Payments for Veterans-Insurance -  CFDA 64.031",
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
+            "title": "USA Spending file- 01/2014-Direct Payments for Veterans-Insurance -  CFDA 64.031"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/h78n-myev",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Vicki Cordes",
+                "hasEmail": "mailto:vicki.cordes@va.gov"
+            },
+            "describedBy": "https://gravelocator.cem.va.gov/j2ee/servlet/NGL_v1",
+            "description": "<p>Gravesite locations of Veterans and beneficiaries includes burial records from many sources. These sources provide varied data; some searches may contain less information than others. Information on veterans buried in private cemeteries was collected for the purpose of furnishing government grave markers, and we do not have information available for burials prior to 1997.</p>",
+            "identifier": "VA-NCA-MS-002",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://gravelocator.cem.va.gov/j2ee/servlet/NGL_v1"
-            ],
             "keyword": [
                 "burial data",
                 "cemetaries",
                 "gravesites",
                 "veterans and beneficiaries"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Vicki Cordes",
-                "hasEmail": "mailto:vicki.cordes@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/h78n-myev",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-NCA-MS-002",
-            "description": "<p>Gravesite locations of Veterans and beneficiaries includes burial records from many sources. These sources provide varied data; some searches may contain less information than others. Information on veterans buried in private cemeteries was collected for the purpose of furnishing government grave markers, and we do not have information available for burials prior to 1997.</p>",
-            "title": "Veterans Burial Sites",
-            "programCode": [
-                "029:001"
+            "references": [
+                "https://gravelocator.cem.va.gov/j2ee/servlet/NGL_v1"
             ],
-            "describedBy": "https://gravelocator.cem.va.gov/j2ee/servlet/NGL_v1",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Burial Sites"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/h7cc-t4fw",
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
-            "identifier": "OM-OM-166",
             "description": "<p>COIN report 145 April 2016</p>",
-            "title": "COIN 145 April 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47200,24 +47183,53 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-166",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/h7cc-t4fw",
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
+            "title": "COIN 145 April 2016"
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
+                    "downloadURL": "https://www.va.gov/health/docs/1_May_2015_Public_data_Pending.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 1 May 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-105",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -47231,102 +47243,73 @@
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
-            "identifier": "VA-VHA-OIA-105",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 May 1",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/1_May_2015_Public_data_Pending.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 1 May 2015"
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
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 May 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/h7wz-vt37",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Vermont FY2023",
+            "identifier": "https://www.data.va.gov/api/views/h7wz-vt37",
             "issued": "2024-06-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "vermont"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/h7wz-vt37",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/h7wz-vt37",
-            "description": "NCVAS State Summary Vermont FY2023",
-            "title": "NCVAS State Summary Vermont FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Vermont FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/h853-xgs6",
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
-            "identifier": "https://www.data.va.gov/api/views/h853-xgs6",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE MAY2019",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47334,61 +47317,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/h853-xgs6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h853-xgs6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h853-xgs6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/h853-xgs6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h853-xgs6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h853-xgs6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/h853-xgs6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/h853-xgs6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/h853-xgs6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/h853-xgs6",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/h853-xgs6",
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
+            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE MAY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/h854-8r5g",
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
-            "identifier": "VA-OGC-044",
             "description": "<p>Individual Correspondence Records-VA</p>",
-            "title": "OGC Privacy Act System of Records Notice 05VA026",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47397,23 +47380,46 @@
                     "title": "OGC Privacy Act System of Records Notice 05VA026"
                 }
             ],
+            "identifier": "VA-OGC-044",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "system of records"
+            ],
+            "landingPage": "https://www.data.va.gov/d/h854-8r5g",
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
+            "title": "OGC Privacy Act System of Records Notice 05VA026"
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
+                "hasEmail": "mailto:Monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Reserve Educational Assistance Program (Chapter 1606/1607) for February 2014</p>",
+            "identifier": "VA-VBA-USASPENDING012014-037",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 028",
                 "chapter 1606 1607",
@@ -47421,68 +47427,40 @@
                 "reap",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:Monica.reyes@va.gov"
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
-            "identifier": "VA-VBA-USASPENDING012014-037",
-            "description": "<p>USA Spending- Reserve Educational Assistance Program (Chapter 1606/1607) for February 2014</p>",
-            "title": "USA Spending file- 02/2014-Education- Chapter 1606/1607- CFDA 64.032",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- 02/2014-Education- Chapter 1606/1607- CFDA 64.032"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Policies_in_Force_by_program_by_state.xls",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-04-01T04:00:00Z/2011-04-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Insurance_Technical_Notes_Policies_in_Force_by_Program.doc"
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
-            "identifier": "VA-VBA-INS2011-012",
+            "dataQuality": true,
             "description": "<p>Number of life insurance policies for each administered life insurance program listed by state. Data is current as of 4-30-11.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Number of Life Insurance Policies by Program by State",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47490,45 +47468,51 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-012",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Policies_in_Force_by_program_by_state.xls",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Insurance_Technical_Notes_Policies_in_Force_by_Program.doc"
+            ],
+            "temporal": "2011-04-01T04:00:00Z/2011-04-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Number of Life Insurance Policies by Program by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ha6c-irdm",
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
-            "identifier": "https://www.data.va.gov/api/views/ha6c-irdm",
+            "dataQuality": true,
             "description": "<p>VBA SPECIALLY ADAPTED HOUSING BENEFIT PROGRAMS. The Specially Adapted Housing (SAH) grant program helps Veterans with certain service-connected disabilities live independently in a barrier-free environment. SAH grants can be used in one of the following ways: (1) construct a suitable home on suitable land either already owned or to be acquired by the veteran, or (2) remodel an existing home if it can be suitably adapted, or (3) acquire a suitably adapted home or reduce the outstanding mortgage on a suitably adapted home already owned by the veteran. b. The Special Housing Adaptation (SHA) grant program helps veterans with certain service-connected disabilities adapt or purchase a home to accommodate the disability. SHA grants can be used in one of the following ways: (1) adapt an existing home the veteran or a family member already owns in which the veteran lives; (2) adapt a home the veteran or family member intends to purchase in which the veteran will live; (3) help a veteran purchase a home already adapted in which the veteran will live. c. . The Temporary Residence Adaptations (TRA) program provides adaptation assistance to veterans who are residing, but do not intend to permanently reside, in the a residence owned by a family member. If a veteran is otherwise eligible for SAH or SHA, the assistance is limited. d. SAH and SHA grants may be used up to three times, as long as the aggregate grant amount does not exceed the statutory dollar limitation. TRA grants may only be used once (and count as a grant usage for purposes of the limit of three), and the amount of assistance provided will be subtracted from the veteran's available statutory maximum.</p>",
-            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS DEC2018",
-            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47536,68 +47520,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ha6c-irdm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ha6c-irdm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ha6c-irdm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ha6c-irdm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ha6c-irdm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ha6c-irdm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ha6c-irdm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ha6c-irdm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ha6c-irdm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/ha6c-irdm",
+            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 106"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ha6c-irdm",
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
+            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_amount_by_Program_by_State_June2012.CSV",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-06-01T04:00:00Z/2012-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Face_Amount_by_Program_June_2012.doc"
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
-            "identifier": "VA-VBA-INS2012-005",
+            "dataQuality": true,
             "description": "<p>Face value of insurance for each administered life insurance program listed by state. Data is current as of 06/30/12.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Face Amount of Life Insurance Coverage by Program by State 2012-06-30",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47605,51 +47582,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ha7e-9rwu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ha7e-9rwu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ha7e-9rwu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ha7e-9rwu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ha7e-9rwu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ha7e-9rwu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ha7e-9rwu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ha7e-9rwu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ha7e-9rwu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-005",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "county",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Face_amount_by_Program_by_State_June2012.CSV",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Face_Amount_by_Program_June_2012.doc"
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
+            "title": "Face Amount of Life Insurance Coverage by Program by State 2012-06-30"
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
-            "temporal": "2016-02-15T05:00:00Z/2016-02-15T05:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR40_022016_Pending_and_EWL_Biweekly_Desired_Date_Division_PDFReady.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 15 February 2016"
+                }
             ],
+            "identifier": "VA-VHA-OIA-734",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -47663,113 +47675,86 @@
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
-            "identifier": "VA-VHA-OIA-734",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2016 February 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR40_022016_Pending_and_EWL_Biweekly_Desired_Date_Division_PDFReady.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 15 February 2016"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2016-02-15T05:00:00Z/2016-02-15T05:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2016 February 15"
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
+            "description": "<p>USA Spending- Non Service Connected Disability- December 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-006",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING122013-006",
-            "description": "<p>USA Spending- Non Service Connected Disability- December 2013.</p>",
-            "title": "USA Spending file- Compensation and Pension-  CFDA 64.104",
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
+            "title": "USA Spending file- Compensation and Pension-  CFDA 64.104"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hbky-mrqb",
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
-            "identifier": "https://www.data.va.gov/api/views/hbky-mrqb",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE DEC2018",
-            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47777,104 +47762,103 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hbky-mrqb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hbky-mrqb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hbky-mrqb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/hbky-mrqb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hbky-mrqb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hbky-mrqb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hbky-mrqb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hbky-mrqb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hbky-mrqb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/hbky-mrqb",
+            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
+            "issued": "2019-03-20",
+            "keyword": [
+                "cdfa 64.124"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hbky-mrqb",
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
+            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE DEC2018"
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
+            "description": "<p>USA Spending- Compensation and Pension- Burial Expenses Allowance for Vets for March 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING032014-045",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-03-01T05:00:00Z/2014-03-31T04:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING032014-045",
-            "description": "<p>USA Spending- Compensation and Pension- Burial Expenses Allowance for Vets for March 2013.</p>",
-            "title": "USA Spending file- 03/2014 Compensation and Pension-  CFDA 64.101",
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
+            "title": "USA Spending file- 03/2014 Compensation and Pension-  CFDA 64.101"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hc9x-vqak",
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
-            "identifier": "https://www.data.va.gov/api/views/hc9x-vqak",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located</p>",
-            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS NOV2018",
-            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47882,61 +47866,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hc9x-vqak/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hc9x-vqak/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hc9x-vqak/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/hc9x-vqak/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hc9x-vqak/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hc9x-vqak/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hc9x-vqak/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hc9x-vqak/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hc9x-vqak/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/hc9x-vqak",
+            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 118"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hc9x-vqak",
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
+            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS NOV2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hctd-9q3c",
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
-            "identifier": "OM-OM-180",
             "description": "<p>COIN report 146 for Feb 2017</p>",
-            "title": "COIN 146 Feb 2017",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47944,41 +47927,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-180",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hctd-9q3c",
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
+            "title": "COIN 146 Feb 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hcvm-9cqm",
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
-            "identifier": "https://www.data.va.gov/api/views/hcvm-9cqm",
+            "dataQuality": true,
             "description": "<p>VBA COMPENSTATION BENEFITS PRGOGRAM to provide vocational training and rehabilitation to certain children born with spina bifida or other covered birth defects who are children of Vietnam veterans and some Korean veterans. \u201cA child born with spina bifida or other covered birth defects, except spina bifida occulta, who is the natural child of a Vietnam veteran and some Korean veterans, regardless of the age or marital status of the child, conceived after the date on which the veteran first served in the Republic of Vietnam during the Vietnam era and in particular areas near the DMZ in the Korean conflict. VA must also determine that it is feasible for the child to achieve a vocational goal.\u201d</p>",
-            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA NOV2018",
-            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47986,66 +47970,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hcvm-9cqm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hcvm-9cqm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hcvm-9cqm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/hcvm-9cqm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hcvm-9cqm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hcvm-9cqm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hcvm-9cqm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hcvm-9cqm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hcvm-9cqm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/hcvm-9cqm",
+            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 127"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hcvm-9cqm",
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
+            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA NOV2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/ogc/",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "This content is available on the public-facing web site currently accessible through standard web browsing methods",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2014-10-01T04:00:00Z/2015-10-01T04:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "district counsel",
-                "offices",
-                "rc",
-                "regional counsel",
-                "web site"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Melinda Perritano",
                 "hasEmail": "mailto:Melinda.Perritano@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-003",
+            "dataQuality": true,
             "description": "<p>A listing of current Chief Counsels and District Offices</p>",
-            "title": "OGC Chief Counsel Districts",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48054,81 +48033,86 @@
                     "title": "OGC Chief Counsel Districts"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OGC-003",
+            "issued": "2017-07-26",
+            "keyword": [
+                "district counsel",
+                "offices",
+                "rc",
+                "regional counsel",
+                "web site"
+            ],
+            "landingPage": "https://www.va.gov/ogc/",
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
+            "rights": "This content is available on the public-facing web site currently accessible through standard web browsing methods",
+            "temporal": "2014-10-01T04:00:00Z/2015-10-01T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OGC Chief Counsel Districts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hdqw-r933",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Vicki Cordes",
+                "hasEmail": "mailto:noemailprovided@usa.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Data assets for <a href=\"https://www.data.va.gov/story/national-cemetery-administration\">https://www.data.va.gov/story/national-cemetery-administration</a>.</p>",
+            "identifier": "8ea07f95-2a7f-494d-a275-5420bcd938fb",
             "issued": "2017-01-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cemetaries",
                 "map",
                 "statistics"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Vicki Cordes",
-                "hasEmail": "mailto:noemailprovided@usa.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/hdqw-r933",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "8ea07f95-2a7f-494d-a275-5420bcd938fb",
-            "description": "<p>Data assets for <a href=\"https://www.data.va.gov/story/national-cemetery-administration\">https://www.data.va.gov/story/national-cemetery-administration</a>.</p>",
-            "title": "USVA Cemetery Locations",
-            "programCode": [
-                "029:001"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "USVA Cemetery Locations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hdwd-tvmk",
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
-            "identifier": "VA-OM-OM-156",
             "description": "<p>aged accounts receivable report</p>",
-            "title": "COIN 0017 September 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48136,39 +48120,38 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-156",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accounts receivable"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hdwd-tvmk",
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
+            "title": "COIN 0017 September 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/he4d-uxfc",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-03-01T05:00:00Z/2015-03-31T04:00:00Z",
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
-            "identifier": "VA-OM-OM-134",
             "description": "<p>COIN 0145 MONTHLY CRS TOTALS REPORT Nov 2014</p>",
-            "title": "COIN 0145 MONTHLY CRS TOTALS REPORT MAR 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48176,37 +48159,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-134",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/he4d-uxfc",
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
+            "title": "COIN 0145 MONTHLY CRS TOTALS REPORT MAR 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hevq-e649",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2024-08-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA National Center for Organization Development (NCOD)",
                 "hasEmail": "mailto:vhancod@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/hevq-e649",
-            "description": "VA All Employee Survey (AES) data from the 2023 & 2024 AES administrations. Scores are provided at the station level and up, and the occupation level within hospitals.",
-            "title": "All Employee Survey (AES) 2023 - 2024",
-            "programCode": [
-                "029:000"
-            ],
+            "description": "VA All Employee Survey (AES) data from the 2023 & 2024 AES administrations. Scores are provided at the station level and up, and the occupation level within hospitals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48214,58 +48202,53 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hevq-e649/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hevq-e649/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hevq-e649/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/hevq-e649/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hevq-e649/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hevq-e649/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hevq-e649/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hevq-e649/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hevq-e649/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/hevq-e649",
+            "issued": "2024-08-01",
+            "landingPage": "https://www.data.va.gov/d/hevq-e649",
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
+            "title": "All Employee Survey (AES) 2023 - 2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hfny-sxae",
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
-            "identifier": "OM-OM-168",
             "description": "<p>COIN report 0017 March 2016</p>",
-            "title": "COIN 0017 March 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48273,40 +48256,41 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-168",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hfny-sxae",
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
+            "title": "COIN 0017 March 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hgdd-6ia2",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "connecticut"
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
-            "identifier": "VA-OEI-OEI-176",
             "description": "<p>This summary describes the programs and services VA provided in Connecticut in fiscal year 2015.</p>",
-            "title": "State Summary: Connecticut",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48315,41 +48299,42 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-176",
+            "issued": "2017-07-26",
+            "keyword": [
+                "connecticut"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hgdd-6ia2",
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
+            "title": "State Summary: Connecticut"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hgh3-zwsa",
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
-            "identifier": "https://www.data.va.gov/api/views/hgh3-zwsa",
+            "dataQuality": true,
             "description": "VA All Employee Survey (AES) items also on Federal Employee Viewpoint Survey, reported as percents as required per Federal statute.",
-            "title": "AES 2021 FEVS Percents",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48357,23 +48342,50 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/hgh3-zwsa",
+            "issued": "2023-03-16",
+            "keyword": [
+                "survey",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hgh3-zwsa",
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
+            "title": "AES 2021 FEVS Percents"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN6FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 6 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-080",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -48389,77 +48401,43 @@
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
-            "identifier": "VA-VHA-OIA-080",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 6",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN6FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 6 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 6"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_Policies_by_Program_by_State_Feb_2012.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-02-01T05:00:00Z/2012-02-29T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Policies_in_Force_by_Program_Feb_2012.doc"
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
-            "identifier": "VA-VBA-INS2012-006",
+            "dataQuality": true,
             "description": "<p>Number of life insurance policies for each administered life insurance program listed by state. Data is current as of 02/29/12.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Number of Life Insurance Policies by Program by State 2012/02/29",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48467,69 +48445,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hh8w-hnii/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hh8w-hnii/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hh8w-hnii/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/hh8w-hnii/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hh8w-hnii/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hh8w-hnii/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hh8w-hnii/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hh8w-hnii/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hh8w-hnii/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-006",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_Policies_by_Program_by_State_Feb_2012.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Policies_in_Force_by_Program_Feb_2012.doc"
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
+            "title": "Number of Life Insurance Policies by Program by State 2012/02/29"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.vba.va.gov/pubs/forms/VBA-28-8832-ARE.pdf",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
-            "keyword": [
-                "education and career counseling",
-                "vba benefits",
-                "vre form"
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
-            "identifier": "VA-VBA-INFO-014",
+            "dataQuality": true,
             "description": "<p>VA's Education and Career Counseling program is a great opportunity for Servicemembers and Veterans to get personalized counseling and support to help guide their career paths, ensure most effective use of their VA benefits, and achieve their goals.</p>",
-            "title": "VRE   Career Counseling program -VRE Application form",
-            "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48538,47 +48519,48 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INFO-014",
+            "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "education and career counseling",
+                "vba benefits",
+                "vre form"
+            ],
+            "landingPage": "https://www.vba.va.gov/pubs/forms/VBA-28-8832-ARE.pdf",
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
+            "title": "VRE   Career Counseling program -VRE Application form"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hjvz-dsy5",
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
-            "identifier": "https://www.data.va.gov/api/views/hjvz-dsy5",
+            "dataQuality": true,
             "description": "<p>This dataset contains information on minority veteran healthcare usage, educational attainment, unemployment rates, median income, and projected population figures.</p>",
-            "title": "Educational Attainment of Minorities by Veteran Status: 2014",
-            "isPartOf": "1d427f8d-0018-4fac-905b-6008ead44b3d",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48586,48 +48568,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hjvz-dsy5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hjvz-dsy5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hjvz-dsy5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/hjvz-dsy5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hjvz-dsy5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hjvz-dsy5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hjvz-dsy5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hjvz-dsy5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hjvz-dsy5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/hjvz-dsy5",
+            "isPartOf": "1d427f8d-0018-4fac-905b-6008ead44b3d",
+            "issued": "2017-03-15",
+            "keyword": [
+                "health care",
+                "income",
+                "statistics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hjvz-dsy5",
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
+            "title": "Educational Attainment of Minorities by Veteran Status: 2014"
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
-            "temporal": "2015-09-01T04:00:00Z/2015-09-01T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/health/docs/Pending_Access_09012015RptDate.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 1 September 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-423",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -48641,70 +48653,42 @@
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
-            "identifier": "VA-VHA-OIA-423",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 September 1",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/Pending_Access_09012015RptDate.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 1 September 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-09-01T04:00:00Z/2015-09-01T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 September 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hnw5-8rid",
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
-            "identifier": "d79604ec-9053-4fef-84ba-4c9cf20c99a9",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary New Mexico FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48712,45 +48696,44 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "d79604ec-9053-4fef-84ba-4c9cf20c99a9",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hnw5-8rid",
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
+            "title": "State Summary New Mexico FY2017"
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
-            "temporal": "2000-01-01T05:00:00Z/2000-12-31T05:00:00Z",
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
-            "identifier": "VA-OM-OM-019",
+            "dataQuality": true,
             "description": "<p>2000 VA Performance and Accountability Report.</p>",
-            "title": "2000 VA Performance and Accountability Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48759,46 +48742,44 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-019",
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
+            "temporal": "2000-01-01T05:00:00Z/2000-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2000 VA Performance and Accountability Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hprb-az5y",
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
-            "identifier": "https://www.data.va.gov/api/views/hprb-az5y",
             "description": "Trend in Rate of Users by Gender over Time, FY 2009 - 2018. Data underlying the third figure of Part 1 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 4, Trend in Rate of Users by Gender over Time",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48806,62 +48787,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hprb-az5y/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hprb-az5y/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hprb-az5y/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/hprb-az5y/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hprb-az5y/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hprb-az5y/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hprb-az5y/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hprb-az5y/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hprb-az5y/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/hprb-az5y",
+            "issued": "2020-10-06",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hprb-az5y",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 4, Trend in Rate of Users by Gender over Time"
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
-            "identifier": "VA-VBA-ABR2012-050",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Summary of Home Loan Guaranty Entitlements and Other Eligibility Criteria",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48869,46 +48849,49 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-050",
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
+            "title": "Summary of Home Loan Guaranty Entitlements and Other Eligibility Criteria"
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
-            "temporal": "2013-04-01T04:00:00Z/2013-06-30T04:00:00Z",
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
-            "identifier": "VA-OEI-OEI-056",
+            "dataQuality": true,
             "description": "<p>NCVAS Pocket Cards archives are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs (VA) benefits and health care utilization.</p>",
-            "title": "VA Benefits and Health Care Utilization",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48917,61 +48900,90 @@
                     "title": "VA Benefits and Health Care Utilization"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-056",
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
+            "temporal": "2013-04-01T04:00:00Z/2013-06-30T04:00:00Z",
             "theme": [
                 "Veterans Benefits",
                 "Veteran Utilization",
                 "Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Benefits and Health Care Utilization"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/hrfz-ifrx",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary North Dakota FY2023",
+            "identifier": "https://www.data.va.gov/api/views/hrfz-ifrx",
             "issued": "2024-06-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "north dakota"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/hrfz-ifrx",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/hrfz-ifrx",
-            "description": "NCVAS State Summary North Dakota FY2023",
-            "title": "NCVAS State Summary North Dakota FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary North Dakota FY2023"
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
-            "temporal": "2016-03-01T05:00:00Z/2016-03-01T05:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR41-032016-Pending-and-EWL-Biweekly-Desired-Date-Division.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 1 March 2016"
+                }
             ],
+            "identifier": "VA-VHA-OIA-735",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -48985,71 +48997,43 @@
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
-            "identifier": "VA-VHA-OIA-735",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2016 March 1",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR41-032016-Pending-and-EWL-Biweekly-Desired-Date-Division.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 1 March 2016"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2016-03-01T05:00:00Z/2016-03-01T05:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2016 March 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hs88-6cuc",
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
-            "identifier": "4c028f22-434a-473a-b919-6dfebd0903df",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Maryland FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49057,37 +49041,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "4c028f22-434a-473a-b919-6dfebd0903df",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hs88-6cuc",
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
+            "title": "State Summary Maryland FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hseb-qib5",
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
-            "identifier": "VA-OM-OM-104",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 0146 MONTHLY TOP TOTALS REPORT Oct 2014",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49095,42 +49078,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-104",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referral"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hseb-qib5",
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
+            "title": "COIN 0146 MONTHLY TOP TOTALS REPORT Oct 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/Surveys.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2001-02-12T05:00:00Z/2001-11-12T05:00:00Z",
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
-            "identifier": "VA-OEI-OEI-052",
+            "dataQuality": true,
             "description": "<p>The 2001 National Survey of Veterans (NSV) is the fifth in a series of comprehensivenationwide surveys designed to help the Department of Veterans Affairs (VA) plan its future programsand services for veterans. The information gathered through these surveys will help VA to identify theneeds of veterans and then allocate resources in ways that will ensure these needs can be met. It also provides a snapshot profile of the veteranpopulation. Data collected through the NSV enables VA to: follow changing trends in the veteranpopulation; compare characteristics of veterans who use VA services with those of veterans who do not;study VA\u00ef\u00bf\u00bds role in the delivery of all benefits that veterans receive; and update information about veteransto help the Department develop its policies.</p>",
-            "title": "2001 National Survey of Veterans (NSV)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49139,43 +49122,44 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-052",
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
+            "temporal": "2001-02-12T05:00:00Z/2001-11-12T05:00:00Z",
             "theme": [
                 "Data on Veterans"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2001 National Survey of Veterans (NSV)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/huh3-96d4",
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
-            "identifier": "a7d44490-6bd6-486d-9c9d-f80cdfb790ba",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Nebraska FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49183,25 +49167,54 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "a7d44490-6bd6-486d-9c9d-f80cdfb790ba",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/huh3-96d4",
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
+            "title": "State Summary Nebraska FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hv96-m277",
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
+            "description": "Strategic Analytics for Improvement and Learning Value Model or SAIL, is a system for summarizing hospital system performance within Veterans Health Administration (VHA). SAIL assesses key Quality measures in areas such as death rate, complications, and patient satisfaction, as well as overall efficiency at individual VA Medical Centers (VAMCs).  This currently only has Q1 and Q4 data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/hv96-m277/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/hv96-m277",
+            "isPartOf": "VA-VHA-OIA-122",
             "issued": "2020-10-21",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-10-01/2020-09-30",
-            "modified": "2021-06-25",
             "keyword": [
                 "2020",
                 "analytics",
@@ -49222,136 +49235,104 @@
                 "sail",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Sail Operations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/hv96-m277",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-06-25",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/hv96-m277",
-            "description": "Strategic Analytics for Improvement and Learning Value Model or SAIL, is a system for summarizing hospital system performance within Veterans Health Administration (VHA). SAIL assesses key Quality measures in areas such as death rate, complications, and patient satisfaction, as well as overall efficiency at individual VA Medical Centers (VAMCs).  This currently only has Q1 and Q4 data.",
-            "title": "SAIL FY2020 Hospital Performance - All Facilities",
-            "isPartOf": "VA-VHA-OIA-122",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/hv96-m277/application/zip",
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
+            "title": "SAIL FY2020 Hospital Performance - All Facilities"
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
+            "description": "<p>USA Spending- Vocational Rehabilitation for Disabled Veterans - Chapter 31- January 2014</p>",
+            "identifier": "VA-VBA-USASPENDING012014-024",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2014-01-31T05:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING012014-024",
-            "description": "<p>USA Spending- Vocational Rehabilitation for Disabled Veterans - Chapter 31- January 2014</p>",
-            "title": "USA Spending file- Vocational Rehabilitation for Disabled Veterans-  CFDA 64.116",
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
+            "title": "USA Spending file- Vocational Rehabilitation for Disabled Veterans-  CFDA 64.116"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hveu-jiru",
-            "issued": "2023-07-04",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-12",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Missouri FY2021",
+            "identifier": "https://www.data.va.gov/api/views/hveu-jiru",
+            "issued": "2023-07-04",
             "keyword": [
                 "fy2021 data",
                 "missouri",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/hveu-jiru",
+            "landingPage": "https://www.data.va.gov/d/hveu-jiru",
+            "modified": "2024-06-12",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Missouri FY2021",
             "title": "NCVAS State Summary Missouri FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hvy5-4umv",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-11-17",
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
-            "identifier": "https://www.data.va.gov/api/views/hvy5-4umv",
             "description": "Veterans Utilization Profile FY18 - Fig 10, Percent Users vs Non-Users Distribution by Age Group - Males. Data underlying the second figure of Part 2 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 10, Percent Users vs Non-Users Distribution by Age Group - Males",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49359,58 +49340,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hvy5-4umv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hvy5-4umv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hvy5-4umv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/hvy5-4umv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hvy5-4umv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hvy5-4umv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hvy5-4umv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hvy5-4umv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hvy5-4umv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hw7z-nyrk",
-            "bureauCode": [
-                "029:00"
-            ],
-            "issued": "2021-02-18",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-23",
+            "identifier": "https://www.data.va.gov/api/views/hvy5-4umv",
+            "issued": "2020-11-17",
             "keyword": [
-                "disability compensation",
-                "veteran",
-                "veteran benefits"
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hvy5-4umv",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2020-12-22",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 10, Percent Users vs Non-Users Distribution by Age Group - Males"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "029:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/hw7z-nyrk",
             "description": "Compensation & Pension: All Veterans who received VA disability compensation or pension payments were included. Veterans who received Special Adaptive Housing benefits were also included in the analysis. Veterans with pending or denied claims were not included. Veterans Benefits Administration (VBA) provides Compensation and Pension disability benefits.",
-            "title": "Veterans who used Disability Compensation Benefits",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49418,67 +49400,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hw7z-nyrk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hw7z-nyrk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hw7z-nyrk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/hw7z-nyrk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hw7z-nyrk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hw7z-nyrk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hw7z-nyrk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hw7z-nyrk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hw7z-nyrk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "State",
-            "license": "https://www.usa.gov/government-works",
+            "identifier": "https://www.data.va.gov/api/views/hw7z-nyrk",
+            "issued": "2021-02-18",
+            "keyword": [
+                "disability compensation",
+                "veteran",
+                "veteran benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hw7z-nyrk",
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
+            "title": "Veterans who used Disability Compensation Benefits"
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
-            "modified": "2020-05-15",
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
-            "identifier": "VA-VBA-INS2010-001",
+            "dataQuality": true,
             "description": "<p>Fiscal Year 2010 life insurance payments, face value of Insurance, and total number of policies by state.  Data were derived from Actuarial reports, including FY 2010 Statement of Cash Flows, FY 2010 Policy Exhibit, and FY 2010 State of Residency Report.</p>",
-            "title": "FY10_Life Insurance Payments, Face Value of Insurance, and Number of Policies",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49487,76 +49466,80 @@
                     "title": "csv"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2010-001",
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
+            "modified": "2020-05-15",
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
+            "title": "FY10_Life Insurance Payments, Face Value of Insurance, and Number of Policies"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/hwwu-i9si",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Hawaii FY2023",
+            "identifier": "https://www.data.va.gov/api/views/hwwu-i9si",
             "issued": "2024-06-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "fy2023",
                 "hawaii",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/hwwu-i9si",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/hwwu-i9si",
-            "description": "NCVAS State Summary Hawaii FY2023",
-            "title": "NCVAS State Summary Hawaii FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Hawaii FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hx65-dgqy",
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
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-131",
             "description": "<p>Activity in terms of establishments and dispositions for CARS on a monthly basis</p>",
-            "title": "COIN 0022 CARS MONTHLY CRS TOTALS REPORT MAR 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49564,41 +49547,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-131",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cars",
+                "establishments"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hx65-dgqy",
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
+            "title": "COIN 0022 CARS MONTHLY CRS TOTALS REPORT MAR 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hx7p-w5cw",
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
-            "identifier": "d0d01f13-81fb-4da2-a6f8-1bae646bea97",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Wisconsin FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49606,45 +49590,44 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "d0d01f13-81fb-4da2-a6f8-1bae646bea97",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hx7p-w5cw",
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
+            "title": "State Summary Wisconsin FY2017"
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
-            "identifier": "VA-OM-OM-009",
+            "dataQuality": true,
             "description": "<p>2008 VA Performance and Accountability Report.</p>",
-            "title": "2008 VA Performance and Accountability Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49653,27 +49636,47 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-009",
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
+            "temporal": "2008-01-01T05:00:00Z/2008-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2008 VA Performance and Accountability Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/hyxi-ssta",
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
+            "description": "<p>The VA National Bed Control System records the levels of operating, unavailable and authorized beds at each VAMC, and it tracks requests for changes in these levels. For changes in operating, unavailable and authorized bed levels, the Director of a Medical Center or his/her authorized delegate enters a bed change request into the Bed Control Database. A Bed Control Database trigger automatically notifies the respective Veterans Integrated Support Network (VISN) director. The VISN director's designated staff reviews the request and either approves, disapproves, or cancels it through the Bed Control Database. If a medical center request is approved by the VISN director, a Bed Control Database trigger notifies staff in the Assistant Deputy Under Secretary for Health for Operations and Management (10N) to review and take action, followed by the appropriate VHA Program Office and then the Under Secretary for Health. Once a request has been approved, cancelled, or disapproved by either the Deputy Under Secretary for Health for Operations and Management, VHA Program Office, or the Under Secretary for Health, the medical center director and the appropriate VISN director are automatically notified of the action. The approval process is tracked and visible to the authorized user of the system. When changes are approved, the database updates its bed level information accordingly. Pertinent justification and documents associated with each bed change request are stored in the database.</p>",
+            "identifier": "VA-VHA-OM-002",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1992-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "authorized",
                 "bed",
@@ -49687,60 +49690,41 @@
                 "veteran",
                 "ward"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/hyxi-ssta",
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
-            "identifier": "VA-VHA-OM-002",
-            "description": "<p>The VA National Bed Control System records the levels of operating, unavailable and authorized beds at each VAMC, and it tracks requests for changes in these levels. For changes in operating, unavailable and authorized bed levels, the Director of a Medical Center or his/her authorized delegate enters a bed change request into the Bed Control Database. A Bed Control Database trigger automatically notifies the respective Veterans Integrated Support Network (VISN) director. The VISN director's designated staff reviews the request and either approves, disapproves, or cancels it through the Bed Control Database. If a medical center request is approved by the VISN director, a Bed Control Database trigger notifies staff in the Assistant Deputy Under Secretary for Health for Operations and Management (10N) to review and take action, followed by the appropriate VHA Program Office and then the Under Secretary for Health. Once a request has been approved, cancelled, or disapproved by either the Deputy Under Secretary for Health for Operations and Management, VHA Program Office, or the Under Secretary for Health, the medical center director and the appropriate VISN director are automatically notified of the action. The approval process is tracked and visible to the authorized user of the system. When changes are approved, the database updates its bed level information accordingly. Pertinent justification and documents associated with each bed change request are stored in the database.</p>",
-            "title": "VA National Bed Control System",
-            "programCode": [
-                "029:040"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1992-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA National Bed Control System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hz2d-y4sm",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-12-09",
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
-            "identifier": "https://www.data.va.gov/api/views/hz2d-y4sm",
             "description": "High-level/Summary data of NCA Acreage; provided in support of the NCA Data Story",
-            "title": "NCA Acreage Aggregate",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49748,59 +49732,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hz2d-y4sm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hz2d-y4sm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hz2d-y4sm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/hz2d-y4sm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hz2d-y4sm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hz2d-y4sm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/hz2d-y4sm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/hz2d-y4sm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/hz2d-y4sm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/hz2d-y4sm",
+            "issued": "2019-12-09",
+            "keyword": [
+                "cemeteries"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hz2d-y4sm",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "NCA Acreage Aggregate"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/Report.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2005-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "demographics",
-                "va benefits",
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
-            "identifier": "VA-OEI-OEI-082",
+            "dataQuality": true,
             "description": "<p>This report provides demographic, socio-economic, and utilization trends of Veterans who used at least one VA benefit or service each year between FY 2005 and FY 2013. It also includes a comparison of Veterans who used VA benefits to Veterans who did not use VA benefits.</p>",
-            "title": "Unique Veteran Users Report FY 2012",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49809,43 +49791,45 @@
                     "title": "Unique Veteran Users Report FY 2012"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-082",
+            "issued": "2017-07-26",
+            "keyword": [
+                "demographics",
+                "va benefits",
+                "veterans"
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
+            "temporal": "2005-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Demographics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Unique Veteran Users Report FY 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/hzf8-xk46",
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
-            "identifier": "33fea45c-dbde-42a8-b3a5-dc7586db432c",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Florida FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49853,67 +49837,66 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "33fea45c-dbde-42a8-b3a5-dc7586db432c",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/hzf8-xk46",
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
+            "title": "State Summary Florida FY2017"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/i2uf-q95k",
-            "issued": "2023-08-11",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Wisconsin FY2021",
+            "identifier": "https://www.data.va.gov/api/views/i2uf-q95k",
+            "issued": "2023-08-11",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "wisconsin"
             ],
-            "identifier": "https://www.data.va.gov/api/views/i2uf-q95k",
+            "landingPage": "https://www.data.va.gov/d/i2uf-q95k",
+            "modified": "2024-06-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Wisconsin FY2021",
             "title": "NCVAS State Summary Wisconsin FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/i3td-fn3i",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "oregon",
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
-            "identifier": "VA-OEI-OEI-123",
             "description": "<p>This is a summary of the programs and services provided by VA in Oregon in fiscal year 2014.</p>",
-            "title": "State Summary:  Oregon",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49922,106 +49905,105 @@
                     "title": "State Summary:  Oregon"
                 }
             ],
+            "identifier": "VA-OEI-OEI-123",
+            "issued": "2017-07-26",
+            "keyword": [
+                "oregon",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/i3td-fn3i",
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
+            "title": "State Summary:  Oregon"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/i4me-uk9x",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-21",
-            "keyword": [
-                "new mexico",
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
-            "identifier": "https://www.data.va.gov/api/views/i4me-uk9x",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_New Mexico",
+            "identifier": "https://www.data.va.gov/api/views/i4me-uk9x",
+            "issued": "2021-08-26",
+            "keyword": [
+                "new mexico",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/i4me-uk9x",
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
+            "title": "State Summaries_New Mexico"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/i56w-ym2m",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-21",
-            "keyword": [
-                "north carolina",
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
-            "identifier": "https://www.data.va.gov/api/views/i56w-ym2m",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_North Carolina",
+            "identifier": "https://www.data.va.gov/api/views/i56w-ym2m",
+            "issued": "2021-08-26",
+            "keyword": [
+                "north carolina",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/i56w-ym2m",
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
+            "title": "State Summaries_North Carolina"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/i59g-u4dw",
-            "bureauCode": [
-                "029:40"
-            ],
-            "rights": "Public",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2008-01-03T05:00:00Z/2018-01-03T05:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "donor",
-                "memorials"
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "029:40"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James Killens III",
                 "hasEmail": "mailto:james.killensiii@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-NCA-DCS-001",
+            "dataQuality": true,
             "description": "<p>Guidance on the appropriate design, size, and procedures for the acceptance of donation of memorials to NCA. This document contains criteria and information to instruct donor groups and national cemetery administration staff on the donation and acceptance of Commemorative Works and Standard Memorial Monuments.</p>",
-            "title": "Guidelines for Review and Acceptance of Memorials",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50030,108 +50012,107 @@
                     "title": "Guidelines for Review and Acceptance of Memorials"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-NCA-DCS-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "donor",
+                "memorials"
+            ],
+            "landingPage": "https://www.data.va.gov/d/i59g-u4dw",
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
+            "rights": "Public",
+            "temporal": "2008-01-03T05:00:00Z/2018-01-03T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Guidelines for Review and Acceptance of Memorials"
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
+            "description": "<p>USA Spending- Home Loan Guaranty- February 2014.</p>",
+            "identifier": "VA-VBA-USASPENDING022014-043",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-02-01T05:00:00Z/2014-02-28T05:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING022014-043",
-            "description": "<p>USA Spending- Home Loan Guaranty- February 2014.</p>",
-            "title": "USA Spending file- 02/2014 -Home Loan  Guaranty-  CFDA 64.114",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2013-02-01T05:00:00Z/2014-02-28T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- 02/2014 -Home Loan  Guaranty-  CFDA 64.114"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/i5q8-7s7q",
-            "issued": "2024-03-27",
             "@type": "dcat:Dataset",
-            "modified": "2024-03-27",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "Learn about this resource that brings together data from almost 500 published studies on a wide range of PTSD treatments.",
             "identifier": "https://www.data.va.gov/api/views/i5q8-7s7q",
+            "issued": "2024-03-27",
+            "landingPage": "https://www.data.va.gov/d/i5q8-7s7q",
+            "modified": "2024-03-27",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Learn about this resource that brings together data from almost 500 published studies on a wide range of PTSD treatments.",
             "title": "For Providers: About the PTSD Repository"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/i655-srxa",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-10-05",
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
-            "identifier": "https://www.data.va.gov/api/views/i655-srxa",
             "description": "Trend in the number and rate of veterans who used any benefit versus those who used none, FY 2009-2018. Data underlying the first figure of Part 2 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 3, Trend in Rate of Users over Time",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50139,59 +50120,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/i655-srxa/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/i655-srxa/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/i655-srxa/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/i655-srxa/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/i655-srxa/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/i655-srxa/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/i655-srxa/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/i655-srxa/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/i655-srxa/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/i655-srxa",
+            "issued": "2020-10-05",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/i655-srxa",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 3, Trend in Rate of Users over Time"
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
-            "temporal": "2011-01-01T05:00:00Z/2011-12-31T05:00:00Z",
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
-            "identifier": "VA-OM-OM-005",
+            "dataQuality": true,
             "description": "<p>2011 VA Performance and Accountability Report Highlights.</p>",
-            "title": "2011 VA Performance and Accountability Report Highlights",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50200,26 +50183,57 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-005",
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
+            "temporal": "2011-01-01T05:00:00Z/2011-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2011 VA Performance and Accountability Report Highlights"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/i6qj-stk3",
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
+            "description": "<p>Record-level data released on Freedom of Information Act (FOIA) Request 15-00242-F appeal.  Fields with value of b6 indicate data withheld in accordance with VHA Expert Determination methodology and/or VA Office of General Counsel direction.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/i6qj-stk3/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "VA-VHA-10N-005",
+            "isPartOf": "VA-VHA-10N-013",
             "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
             "keyword": [
                 "crisis",
                 "foia",
@@ -50232,69 +50246,39 @@
                 "veteran",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/i6qj-stk3",
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
-            "identifier": "VA-VHA-10N-005",
-            "description": "<p>Record-level data released on Freedom of Information Act (FOIA) Request 15-00242-F appeal.  Fields with value of b6 indicate data withheld in accordance with VHA Expert Determination methodology and/or VA Office of General Counsel direction.</p>",
-            "title": "Veterans Crisis Line calls FY2011 Record-Level Data",
-            "isPartOf": "VA-VHA-10N-013",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:042"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/i6qj-stk3/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
-            "describedBy": "https://github.com/vacobrydsk/VeteransCrisisLineDataDictionary/raw/master/VeteransCrisisLineDataDictionary.xlsx",
             "systemOfRecords": "https://www.federalregister.gov/articles/2015/04/24/2015-09567/privacy-act-of-1974-system-of-records",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
             "theme": [
                 "Suicide Prevention"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Crisis Line calls FY2011 Record-Level Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/i6ux-9vt8",
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
-            "identifier": "https://www.data.va.gov/api/views/i6ux-9vt8",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAMS to provide, through purchase and/or fabrication, prosthetic and related appliances, equipment and services to eligible veterans so that they may live and work as productive citizens. Veterans eligible for prosthetic services are service-connected veterans seeking care for a service-connected disability; veterans with compensable service-connected disabilities generally rated 10 percent or more; former prisoners of war, veterans discharged or released from active military service for a disability that was incurred or aggravated in the line of duty, and veterans who are in receipt of Section 1151 benefits; veterans who are in receipt of increased pension based on a need of regular aid and attendance or by reason of being permanently housebound; veterans who have annual income and net worth below the \"means test\" threshold; all other veterans who are not required to pay a copayment for their care, i.e., veterans of the Mexican border period and World War I, compensated zero (0) percent service-connected veterans who are receiving statutory awards, veterans exposed to a toxic substance, radiation or environmental hazard (limited to certain disabilities); and veterans who must pay a copayment for their care. Ineligible veterans are nonservice-connected veterans residing or sojourning in foreign lands.</p>",
-            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES DEC2018",
-            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50302,64 +50286,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/i6ux-9vt8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/i6ux-9vt8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/i6ux-9vt8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/i6ux-9vt8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/i6ux-9vt8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/i6ux-9vt8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/i6ux-9vt8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/i6ux-9vt8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/i6ux-9vt8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/i6ux-9vt8",
+            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 116"
+            ],
+            "landingPage": "https://www.data.va.gov/d/i6ux-9vt8",
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
+            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES DEC2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_Veterans_enrolled_in_VGLI_by_state_as_of_06_30_11.csv",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Number_of_Veterans_Enrolled_in_VGLI_by_State_2.doc"
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
-            "identifier": "VA-VBA-INS2011-020",
+            "dataQuality": true,
             "description": "<p>Provides the number of Veterans insured under the Veterans' Group Life Insurance (VGLI) program by state.  This report provides a snapshot of the active VGLI membership as of June 30, 2011.  For members who reside outside the United States, membership is not identified by individual country.  The total number of members was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "FY11_Number of Veterans Insured by VGLI by State as of 6-30-11",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50367,69 +50346,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/i73c-uyag/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/i73c-uyag/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/i73c-uyag/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/i73c-uyag/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/i73c-uyag/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/i73c-uyag/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/i73c-uyag/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/i73c-uyag/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/i73c-uyag/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-020",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_Veterans_enrolled_in_VGLI_by_state_as_of_06_30_11.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Number_of_Veterans_Enrolled_in_VGLI_by_State_2.doc"
+            ],
+            "temporal": "2010-10-01T04:00:00Z/2011-06-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY11_Number of Veterans Insured by VGLI by State as of 6-30-11"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/i7ri-kcad",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2002-10-01T04:00:00Z/2014-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "health care",
-                "outpatient",
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
-            "identifier": "VA-OEI-OEI-085",
             "description": "<p>This table shows a brief summary of enrollees, outpatient visits, and inpatient admissions.</p>",
-            "title": "Selected Veterans Health Administration Characteristics:  FY2002 to FY2014",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50438,24 +50419,58 @@
                     "title": "Selected Veterans Health Administration Characteristics:  FY2002 to FY2014"
                 }
             ],
+            "identifier": "VA-OEI-OEI-085",
+            "issued": "2017-07-26",
+            "keyword": [
+                "health care",
+                "outpatient",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/i7ri-kcad",
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
+            "temporal": "2002-10-01T04:00:00Z/2014-09-30T04:00:00Z",
             "theme": [
                 "Demographics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Selected Veterans Health Administration Characteristics:  FY2002 to FY2014"
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
+            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/Pending_Access_Data_using_Preferred_Date_11052014.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "November 5, 2014"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-067",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-10-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -50469,70 +50484,39 @@
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
-            "identifier": "VA-VHA-OIA-067",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments (Preferred Date)  - Report 2014 November 5",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/Pending_Access_Data_using_Preferred_Date_11052014.pdf",
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
+            "title": "Accelerating Access to Care Initiative Pending Appointments (Preferred Date)  - Report 2014 November 5"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/i8fc-ndim",
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
-            "identifier": "https://www.data.va.gov/api/views/i8fc-ndim",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located</p>",
-            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS APR2019",
-            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50540,43 +50524,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/i8fc-ndim/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/i8fc-ndim/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/i8fc-ndim/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/i8fc-ndim/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/i8fc-ndim/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/i8fc-ndim/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/i8fc-ndim/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/i8fc-ndim/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/i8fc-ndim/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/i8fc-ndim",
+            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 118"
+            ],
+            "landingPage": "https://www.data.va.gov/d/i8fc-ndim",
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
+            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/i8ru-da75",
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
+                    "downloadURL": "https://www.data.va.gov/download/i8ru-da75/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "VA-VHA-10N-007",
+            "isPartOf": "VA-VHA-10N-013",
             "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
             "keyword": [
                 "crisis",
                 "foia",
@@ -50589,73 +50603,40 @@
                 "veteran",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/i8ru-da75",
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
-            "identifier": "VA-VHA-10N-007",
-            "description": "<p>Record-level data released on Freedom of Information Act (FOIA) Request 15-00242-F appeal.  Fields with value of b6 indicate data withheld in accordance with VHA Expert Determination methodology and/or VA Office of General Counsel direction.</p>",
-            "title": "Veterans Crisis Line calls FY2013 Record-Level Data",
-            "isPartOf": "VA-VHA-10N-013",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:042"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/i8ru-da75/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
-            "describedBy": "https://raw.githubusercontent.com/vacobrydsk/VeteransCrisisLineDataDictionary/master/VeteransCrisisLineDataDictionary.xlsx",
             "systemOfRecords": "https://www.federalregister.gov/articles/2015/04/24/2015-09567/privacy-act-of-1974-system-of-records",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Suicide Prevention"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Crisis Line calls FY2013 Record-Level Data"
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
-            "issued": "2023-08-31",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-24",
-            "keyword": [
-                "ahrq",
-                "ahrq report",
-                "appendix f",
-                "appendix g1",
-                "appendix g2-3"
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
-            "identifier": "https://www.data.va.gov/api/views/i95r-ag3b",
+            "dataQuality": true,
             "description": "The U.S. Department of Veterans Affairs (VA) has established a long-term partnership to commission AHRQ to utilize its Evidence-based Practice Centers to develop update reviews to inform the VA\u2019s PTSD-Repository \u2013 a publicly accessible clinical trials database maintained by the National Center for PTSD (NCPTSD).\n\nThe 2022 Report and Evidence Tables (Appendix F, G1, & G2-3) are included in the downloadable .zip file. For more information, visit AHRQ's page: https://effectivehealthcare.ahrq.gov/products/ptsd-pharm-treatment/research",
-            "title": "AHRQ Report and Data Files (2022): Pharmacologic and Nonpharmacologic Treatments for Posttraumatic Stress Disorder (Update)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50663,29 +50644,60 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/i95r-ag3b",
+            "issued": "2023-08-31",
+            "keyword": [
+                "ahrq",
+                "ahrq report",
+                "appendix f",
+                "appendix g1",
+                "appendix g2-3"
+            ],
+            "landingPage": "https://www.ptsd.va.gov/repository",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-10-24",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for PTSD"
+            },
+            "rights": "All data is within the public domain and is currently available for download.",
             "spatial": "International",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "PTSD Randomized Controlled Trials"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AHRQ Report and Data Files (2022): Pharmacologic and Nonpharmacologic Treatments for Posttraumatic Stress Disorder (Update)"
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
-            "temporal": "2015-06-15T04:00:00Z/2015-06-15T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/PublicData_PendingAccess_20150615RptDate_Final.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 15 June 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-109",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -50699,71 +50711,42 @@
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
-            "identifier": "VA-VHA-OIA-109",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 June 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/PublicData_PendingAccess_20150615RptDate_Final.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 15 June 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-06-15T04:00:00Z/2015-06-15T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 June 15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/iakd-ir7s",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-07-30",
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
-            "identifier": "https://www.data.va.gov/api/views/iakd-ir7s",
             "description": "",
-            "title": "Employment Status of Women Veterans by Age",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50771,57 +50754,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/iakd-ir7s/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/iakd-ir7s/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/iakd-ir7s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/iakd-ir7s/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/iakd-ir7s/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/iakd-ir7s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/iakd-ir7s/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/iakd-ir7s/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/iakd-ir7s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/iakd-ir7s",
+            "issued": "2024-07-30",
+            "keyword": [
+                "veterans",
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/iakd-ir7s",
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
-            "landingPage": "https://www.data.va.gov/d/id7h-mm3j",
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
-            "identifier": "https://www.data.va.gov/api/views/id7h-mm3j",
+            "dataQuality": true,
             "description": "<p>VBA PROGRAM BENEFITS for Automobiles and Adaptive Equipment for Certain Disabled Veterans and Members of the Armed Forces. Veterans with honorable service and servicepersons on duty having a service-connected disability due to loss or permanent loss of use of one or both feet, one or both hands, or a permanent impairment of vision of both eyes to a prescribed degree. For adaptive equipment only, eligibility also exists if there is service-connected ankylosis of one or both knees or one or both hips. Personnel on active duty also qualify under the same criteria as veterans. Uses &amp; Use Restrictions:  Assistance toward purchase of an automobile or other conveyance is a one-time payment only. Necessary adaptive equipment may be furnished, repaired, replaced, or reinstalled on a conveyance which may be purchased with assistance or any other conveyance subsequently or previously acquired. Adaptive equipment will be provided for no more than two conveyances during any four-year period unless one of those two vehicles becomes unavailable to the veteran.</p>",
-            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE OCT2018",
-            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50829,66 +50813,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/id7h-mm3j/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/id7h-mm3j/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/id7h-mm3j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/id7h-mm3j/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/id7h-mm3j/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/id7h-mm3j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/id7h-mm3j/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/id7h-mm3j/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/id7h-mm3j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/id7h-mm3j",
+            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 100"
+            ],
+            "landingPage": "https://www.data.va.gov/d/id7h-mm3j",
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
+            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE OCT2018"
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
-                "benefits",
-                "compensation benefits fy12",
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
-            "identifier": "VA-VBA-ABR2012-003",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Age of Veterans Receiving Service Connected Compensation at the End of FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50896,27 +50876,46 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-003",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "abr",
+                "abr2012",
+                "benefits",
+                "compensation benefits fy12",
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
+            "title": "Age of Veterans Receiving Service Connected Compensation at the End of FY2012"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/iehx-efs9",
-            "issued": "2022-12-14",
             "@type": "dcat:Dataset",
-            "modified": "2023-01-12",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
+            "description": "Appendix for a three-part study on Veterans who have used at least one of 22 benefits or services (referred to as \"users\") provided by VA during Fiscal Years 2010 through 2021.",
+            "identifier": "https://www.data.va.gov/api/views/iehx-efs9",
+            "issued": "2022-12-14",
             "keyword": [
                 "utilization",
                 "va benefits",
@@ -50926,68 +50925,50 @@
                 "veterans",
                 "veterans benefits"
             ],
-            "identifier": "https://www.data.va.gov/api/views/iehx-efs9",
+            "landingPage": "https://www.data.va.gov/d/iehx-efs9",
+            "modified": "2023-01-12",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Appendix for a three-part study on Veterans who have used at least one of 22 benefits or services (referred to as \"users\") provided by VA during Fiscal Years 2010 through 2021.",
             "title": "Use of VA Benefits and Services: 2021 (Appendix)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ifcv-kkbm",
-            "issued": "2023-06-18",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary California 2023",
+            "identifier": "https://www.data.va.gov/api/views/ifcv-kkbm",
+            "issued": "2023-06-18",
             "keyword": [
                 "california",
                 "fy2021 data",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/ifcv-kkbm",
+            "landingPage": "https://www.data.va.gov/d/ifcv-kkbm",
+            "modified": "2024-05-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary California 2023",
             "title": "NCVAS State Summary California FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ig48-b5dn",
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
-            "identifier": "https://www.data.va.gov/api/views/ig48-b5dn",
             "description": "VetPop2023 projection of living Veterans by gender and race/ethnicity at the state level. \n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2023 State Race/Ethnicity Data, 8L",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50995,62 +50976,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ig48-b5dn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ig48-b5dn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ig48-b5dn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ig48-b5dn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ig48-b5dn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ig48-b5dn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ig48-b5dn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ig48-b5dn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ig48-b5dn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/ig48-b5dn",
+            "issued": "2024-09-09",
+            "keyword": [
+                "veteran population",
+                "veterans",
+                "vetpop",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ig48-b5dn",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-09",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 State Race/Ethnicity Data, 8L"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ig87-ri64",
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
-            "identifier": "https://www.data.va.gov/api/views/ig87-ri64",
             "description": "Percent Users vs Non-Users Distribution by Age Group - Females. Data underlying the third figure of Part 2 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Percentage Age Distribution of Female Users and Non-Users, FY 2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51058,88 +51036,92 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ig87-ri64/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ig87-ri64/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ig87-ri64/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ig87-ri64/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ig87-ri64/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ig87-ri64/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ig87-ri64/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ig87-ri64/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ig87-ri64/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/ig87-ri64",
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
+            "landingPage": "https://www.data.va.gov/d/ig87-ri64",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Percentage Age Distribution of Female Users and Non-Users, FY 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/ih24-d9xz",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:vancvas@va.gov"
+            },
+            "description": "NCVAS State Summary Wisconsin FY2023",
+            "identifier": "https://www.data.va.gov/api/views/ih24-d9xz",
             "issued": "2024-06-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "wisconsin"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:vancvas@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/ih24-d9xz",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/ih24-d9xz",
-            "description": "NCVAS State Summary Wisconsin FY2023",
-            "title": "NCVAS State Summary Wisconsin FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Wisconsin FY2023"
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
-            "identifier": "VA-OEI-OEI-153",
             "description": "<p>This table provides a summary of Veteran and Dependent interments by cemetery type by fiscal years 2000 through 2014.</p>",
-            "title": "National Cemetery Administration Summary of Veteran, Non-Veteran, and Dependent Interments by Cemetery Type: FY2000 to FY2014",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51148,44 +51130,45 @@
                     "title": "National Cemetery Administration Summary of Veteran, Non-Veteran, and Dependent Interments by Cemetery Type: FY2000 to FY2014"
                 }
             ],
+            "identifier": "VA-OEI-OEI-153",
+            "issued": "2017-07-26",
+            "keyword": [
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
+            "title": "National Cemetery Administration Summary of Veteran, Non-Veteran, and Dependent Interments by Cemetery Type: FY2000 to FY2014"
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
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
-            "keyword": [
-                "annual report",
-                "franchise fund",
-                "fy 2012"
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
-            "identifier": "VA-OM-OM-033",
+            "dataQuality": true,
             "description": "<p>Franchise Fund FY 2012 Annual Report</p>",
-            "title": "Franchise Fund FY 2012 Annual Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51194,90 +51177,87 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-033",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund",
+                "fy 2012"
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
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Franchise Fund FY 2012 Annual Report"
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
+            "description": "<p>Service members Group Life Insurance (SGLI)</p>",
+            "identifier": "VA-VBA-MEDIAPUB-045",
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
-            "identifier": "VA-VBA-MEDIAPUB-045",
-            "description": "<p>Service members Group Life Insurance (SGLI)</p>",
-            "title": "Service members Group Life Insurance (SGLI)",
-            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2012-09-01T04:00:00Z/2012-09-01T04:00:00Z",
             "theme": [
                 "General Benefit Information"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Service members Group Life Insurance (SGLI)"
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
-            "identifier": "VA-VBA-ABR2012-001",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Age of Children Who Began Receiving DIC Benefits During Fiscal Year 2012- ABR2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51285,89 +51265,89 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-001",
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
+            "title": "Age of Children Who Began Receiving DIC Benefits During Fiscal Year 2012- ABR2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://cfm.vaco.va.gov/va_pmdri/Default.aspx",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Non-Public access level is warranted because of the financial data aggreated in the system.  Knowledge of this information could possibly compromise contract negoiations for construction services.",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2017-07-26T22:54:31Z/2005-12-06T05:00:00Z",
-            "modified": "2024-08-26",
-            "keyword": [
-                "financial construction management",
-                "project management"
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
-            "identifier": "VA-CFM-PMDRI-003",
+            "dataQuality": true,
             "description": "<p>The Project Management Data Retrieval and Integration Database (PMDRI) is a system that presents data from the VA Financial Management System(FMS) in a structured format so that CFM engineering personnel have an up-to-date accounting of construction contract spending.  Due to the nature of the information, access is restricted to CFM personnel and select VA personnel working with construction projects.</p>",
-            "title": "Project Management Data Retrieval and Integration (PMDRI) Application",
+            "identifier": "VA-CFM-PMDRI-003",
+            "issued": "2017-07-26",
+            "keyword": [
+                "financial construction management",
+                "project management"
+            ],
+            "landingPage": "https://cfm.vaco.va.gov/va_pmdri/Default.aspx",
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
+            "rights": "Non-Public access level is warranted because of the financial data aggreated in the system.  Knowledge of this information could possibly compromise contract negoiations for construction services.",
+            "temporal": "2017-07-26T22:54:31Z/2005-12-06T05:00:00Z",
             "theme": [
                 "Construction Project Management"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Project Management Data Retrieval and Integration (PMDRI) Application"
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
-            "identifier": "VA-VBA-ABR2012-101",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Minnesota-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51375,49 +51355,49 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-101",
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
+            "title": "Minnesota-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ik8k-3hpf",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2024-12-11",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-10-01/2024-09-30",
-            "modified": "2024-12-11",
-            "keyword": [
-                "community care",
-                "diagnosis",
-                "fy24",
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
-            "identifier": "https://www.data.va.gov/api/views/ik8k-3hpf",
+            "dataQuality": true,
             "description": "Diagnosis entered during outpatient, inpatient, or Community Care that was paid for by VHA. This excludes Non-VA Care and Unknown.",
-            "title": "Diagnosis_FY24",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51425,63 +51405,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ik8k-3hpf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ik8k-3hpf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ik8k-3hpf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ik8k-3hpf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ik8k-3hpf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ik8k-3hpf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ik8k-3hpf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ik8k-3hpf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ik8k-3hpf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/ik8k-3hpf",
+            "issued": "2024-12-11",
+            "keyword": [
+                "community care",
+                "diagnosis",
+                "fy24",
+                "icd10",
+                "inpatient",
+                "outpatient"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ik8k-3hpf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2024-12-11",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "spatial": "U.S.",
+            "temporal": "2023-10-01/2024-09-30",
+            "title": "Diagnosis_FY24"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ik8k-96ns",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2024-03-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-08",
-            "keyword": [
-                "age groups",
-                "expenditures",
-                "pension benefits",
-                "residence",
-                "state"
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
-            "identifier": "https://www.data.va.gov/api/views/ik8k-96ns",
             "description": "1. This provides a count of Veterans on the rolls for Pension benefits in FY 2023 with expenditures for claims by state and the age groups of Veterans in each category.\n2. See VBA's Annual Benefits Report for additional information: www.benefits.va.gov/REPORTS/abr/\n3. To protect Veteran privacy any counts consisting of fewer than ten Veterans are not included.",
-            "title": "Veteran Pension Expenditures By State of Residence and Age Group FY 2023",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51489,63 +51470,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ik8k-96ns/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ik8k-96ns/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ik8k-96ns/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ik8k-96ns/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ik8k-96ns/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ik8k-96ns/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ik8k-96ns/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ik8k-96ns/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ik8k-96ns/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/ik8k-96ns",
+            "issued": "2024-03-08",
+            "keyword": [
+                "age groups",
+                "expenditures",
+                "pension benefits",
+                "residence",
+                "state"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ik8k-96ns",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2024-03-08",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veteran Pension Expenditures By State of Residence and Age Group FY 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ikru-krrb",
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
-            "identifier": "https://www.data.va.gov/api/views/ikru-krrb",
             "description": "Data underlying the third figure of Part 1 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Trend in Rate of Users by Sex, FY2010-2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51553,58 +51531,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ikru-krrb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ikru-krrb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ikru-krrb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ikru-krrb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ikru-krrb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ikru-krrb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ikru-krrb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ikru-krrb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ikru-krrb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/ikru-krrb",
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
+            "landingPage": "https://www.data.va.gov/d/ikru-krrb",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Trend in Rate of Users by Sex, FY2010-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/ikvt-cxqf",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-04",
-            "keyword": [
-                "dic benefits",
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
-            "identifier": "https://www.data.va.gov/api/views/ikvt-cxqf",
+            "dataQuality": true,
             "description": "All DIC Recipients by their Relationship to the Veterans. DIC is a tax-free monetary benefit generally payable to a surviving spouse, child, or parent of deceased Servicemembers or Veterans.",
-            "title": "All Dependency and Indemnity Compensation (DIC) Recipients By Relationship To Veteran FY2020",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51612,59 +51595,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ikvt-cxqf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ikvt-cxqf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ikvt-cxqf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ikvt-cxqf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ikvt-cxqf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ikvt-cxqf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ikvt-cxqf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ikvt-cxqf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ikvt-cxqf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/ikvt-cxqf",
+            "issued": "2022-04-29",
+            "keyword": [
+                "dic benefits",
+                "veterans",
+                "veterans surviving spouses and children"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ikvt-cxqf",
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
+            "title": "All Dependency and Indemnity Compensation (DIC) Recipients By Relationship To Veteran FY2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/im5v-7isu",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "benifits",
-                "services",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-161",
+            "dataQuality": true,
             "description": "<p>This reports shows the services and benefits the Department of Veterans Affairs provided in 1994.</p>",
-            "title": "Annual Report: 1994",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51673,47 +51656,46 @@
                     "title": "Annual Report 1994"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-161",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benifits",
+                "services",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/im5v-7isu",
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
+            "title": "Annual Report: 1994"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www1.va.gov/vetdata/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2000-01-01T05:00:00Z/2012-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-09-16",
-            "references": [
-                "https://www1.va.gov/vetdata/"
-            ],
-            "keyword": [
-                "population",
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
-            "identifier": "VA-OEI-OEI-009",
+            "dataQuality": true,
+            "describedBy": "https://www1.va.gov/vetdata/",
             "description": "<p>National Center for Veterans Analysis and Statistics (NCVAS) Web Site.  The web site contains a collection of statistics, data, and reports about Veterans and the utilization of VA benefits and services.</p>",
-            "title": "Veterans Affairs National Center for Veterans Analysis and Statistics",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51722,30 +51704,60 @@
                     "title": "Veterans Affairs National Center for Veterans Analysis and Statistics"
                 }
             ],
-            "describedBy": "https://www1.va.gov/vetdata/",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-009",
+            "issued": "2017-07-26",
+            "keyword": [
+                "population",
+                "veteran"
+            ],
+            "landingPage": "https://www1.va.gov/vetdata/",
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
+                "https://www1.va.gov/vetdata/"
+            ],
+            "temporal": "2000-01-01T05:00:00Z/2012-12-31T05:00:00Z",
             "theme": [
                 "Section 1. Population"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Affairs National Center for Veterans Analysis and Statistics"
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
-            "temporal": "2015-11-01T04:00:00Z/2015-11-01T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR33_112015_Pending_and_EWL_Biweekly_Desired_Date_Division.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 1 November 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-428",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -51759,73 +51771,43 @@
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
-            "identifier": "VA-VHA-OIA-428",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 November 1",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR33_112015_Pending_and_EWL_Biweekly_Desired_Date_Division.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 1 November 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-11-01T04:00:00Z/2015-11-01T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 November 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/education/benefit-rates/",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-17",
-            "keyword": [
-                "school",
-                "weams"
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
-            "identifier": "VA-VBA-INFO-011",
+            "dataQuality": true,
             "description": "Links to Veterans Benefits Administration current education benefit rates for multiple programs. \nFor questions refer to VBA Education Business Line: https://www.va.gov/contact-us/",
-            "title": "VA Veteran Education Program benefits rates",
-            "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
-            "programCode": [
-                "029:030"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51834,26 +51816,47 @@
                     "title": "html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INFO-011",
+            "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "school",
+                "weams"
+            ],
+            "landingPage": "https://www.va.gov/education/benefit-rates/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-17",
+            "programCode": [
+                "029:030"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
             "theme": [
                 "Education Service Rates for Various Education Benefits Programs"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Veteran Education Program benefits rates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/iqru-8v7y",
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
+            "description": "<p>The Patient Assessment File (PAF) database compiles the results of the Patient Assessment Instrument (PAI) questionnaire filled out for intermediate care Veterans Health Administration (VHA) patients. The PAI is filled out within two weeks of admission. It is also completed semi-annually on April 1st and October 1st for each patient by a registered nurse familiar with the patient. The PAI questions cover medical treatments, conditions, selected diagnoses, activities of daily living, behaviors, some rehabilitation therapies, and chronic respiratory support. The database is managed by the Geriatrics &amp; Extended Care Strategic Health Care Group in the Office of Patient Care Services. It is currently running at the Austin Information Technology Center (AITC) and is stored in flat files. PAF's primary customer is the Allocation Resource Center (ARC) in Braintree MA. The ARC receives the data from AITC and combines it with data from the Patient Treatment File (PTF) which contains more detailed demographic and treatment information. The ARC builds ORACLE tables, assigning RUG II (Resource Utilization Group II) scores and weighted work units reflecting the level and type of care needed. The 16 different weighted work units, ranging from 479 to 1800, are a factor in the resource allocation and budget decisions on long-term care, and are used to measure efficiency. The data is also used in other reports to Central Office, the Veterans Integrated Service Networks, and the facilities. Several other units also use PAF information including the Decision Support System (DSS). Currently, PAF is in the process of being replaced by the Resident Assessment Instrument/Minimum Data Set (RAI/MDS). RAI/MDS uses a much more extensive questionnaire as its source of information. The RAI/MDS provides clinical data and care protocols in addition to the newer RUG III scores, and is required by the Centers for Medicare and Medicaid Service funded hospitals.</p>",
+            "identifier": "VA-VHA-OIA-016",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1987-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "assessment",
                 "file",
@@ -51865,92 +51868,71 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/iqru-8v7y",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:054"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-016",
-            "description": "<p>The Patient Assessment File (PAF) database compiles the results of the Patient Assessment Instrument (PAI) questionnaire filled out for intermediate care Veterans Health Administration (VHA) patients. The PAI is filled out within two weeks of admission. It is also completed semi-annually on April 1st and October 1st for each patient by a registered nurse familiar with the patient. The PAI questions cover medical treatments, conditions, selected diagnoses, activities of daily living, behaviors, some rehabilitation therapies, and chronic respiratory support. The database is managed by the Geriatrics &amp; Extended Care Strategic Health Care Group in the Office of Patient Care Services. It is currently running at the Austin Information Technology Center (AITC) and is stored in flat files. PAF's primary customer is the Allocation Resource Center (ARC) in Braintree MA. The ARC receives the data from AITC and combines it with data from the Patient Treatment File (PTF) which contains more detailed demographic and treatment information. The ARC builds ORACLE tables, assigning RUG II (Resource Utilization Group II) scores and weighted work units reflecting the level and type of care needed. The 16 different weighted work units, ranging from 479 to 1800, are a factor in the resource allocation and budget decisions on long-term care, and are used to measure efficiency. The data is also used in other reports to Central Office, the Veterans Integrated Service Networks, and the facilities. Several other units also use PAF information including the Decision Support System (DSS). Currently, PAF is in the process of being replaced by the Resident Assessment Instrument/Minimum Data Set (RAI/MDS). RAI/MDS uses a much more extensive questionnaire as its source of information. The RAI/MDS provides clinical data and care protocols in addition to the newer RUG III scores, and is required by the Centers for Medicare and Medicaid Service funded hospitals.</p>",
-            "title": "Patient Assessment File (PAF)",
-            "programCode": [
-                "029:054"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1987-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Patient Assessment File (PAF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/iqxt-d2f3",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Nebraska FY2023",
+            "identifier": "https://www.data.va.gov/api/views/iqxt-d2f3",
             "issued": "2024-06-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "nebraska"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/iqxt-d2f3",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/iqxt-d2f3",
-            "description": "NCVAS State Summary Nebraska FY2023",
-            "title": "NCVAS State Summary Nebraska FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Nebraska FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/irca-ci2b",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-10-12",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-13",
-            "keyword": [
-                "branch",
-                "branch of service",
-                "vetpop2020"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/irca-ci2b",
             "description": "Percent of female Veterans in each branch for fiscal years 2000 to 2023.\n\n\u201cAll Others\u201d includes U.S. Coast Guard, U.S. Public Health Service, National Oceanic and Atmospheric Administration, and Reserves.",
-            "title": "VetPop2020 Branch Distribution, Females, FY2000-2023",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51958,42 +51940,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/irca-ci2b/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/irca-ci2b/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/irca-ci2b/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/irca-ci2b/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/irca-ci2b/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/irca-ci2b/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/irca-ci2b/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/irca-ci2b/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/irca-ci2b/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/irca-ci2b",
+            "issued": "2023-10-12",
+            "keyword": [
+                "branch",
+                "branch of service",
+                "vetpop2020"
+            ],
+            "landingPage": "https://www.data.va.gov/d/irca-ci2b",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-10-13",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020 Branch Distribution, Females, FY2000-2023"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN10FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 10 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-084",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -52009,71 +52021,44 @@
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
-            "identifier": "VA-VHA-OIA-084",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 10",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN10FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 10 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 10"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/isnh-negm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2023-03-17",
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
-            "identifier": "https://www.data.va.gov/api/views/isnh-negm",
+            "dataQuality": true,
             "description": "VA All Employee Survey (AES) items also on Federal Employee Viewpoint Survey, reported as percents as required per Federal statute.",
-            "title": "AES 2018 FEVS Percents",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52081,63 +52066,59 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/isnh-negm",
+            "issued": "2023-03-17",
+            "keyword": [
+                "survey",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/isnh-negm",
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
+            "title": "AES 2018 FEVS Percents"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/itju-mxjj",
-            "issued": "2022-10-24",
             "@type": "dcat:Dataset",
-            "modified": "2022-10-28",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
+            "description": "Veterans Day 2022 data story celebrating Honor Flights.",
+            "identifier": "https://www.data.va.gov/api/views/itju-mxjj",
+            "issued": "2022-10-24",
             "keyword": [
                 "veterans",
                 "veterans day"
             ],
-            "identifier": "https://www.data.va.gov/api/views/itju-mxjj",
+            "landingPage": "https://www.data.va.gov/d/itju-mxjj",
+            "modified": "2022-10-28",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Veterans Day 2022 data story celebrating Honor Flights.",
             "title": "Veterans Day 2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/itkw-ixir",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-08-10",
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
-            "identifier": "https://www.data.va.gov/api/views/itkw-ixir",
             "description": "FY2021 VA facilities data provided by the National Center for Veterans Statistics and Analysis, published in 2023 includes PR",
-            "title": "FY 2021_NCVAS Facilities Data For State Including PR",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52145,58 +52126,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/itkw-ixir/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/itkw-ixir/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/itkw-ixir/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/itkw-ixir/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/itkw-ixir/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/itkw-ixir/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/itkw-ixir/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/itkw-ixir/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/itkw-ixir/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/itkw-ixir",
+            "issued": "2023-08-10",
+            "keyword": [
+                "fy2021",
+                "ncvas",
+                "state summary",
+                "va facilities"
+            ],
+            "landingPage": "https://www.data.va.gov/d/itkw-ixir",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021_NCVAS Facilities Data For State Including PR"
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
-            "identifier": "VA-OEI-OEI-300",
+            "dataQuality": true,
             "description": "<p>NCVAS Pocket Cards are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs (VA) benefits and health care utilization.</p>",
-            "title": "VA Benefits & Health Care Utilization  FY16 (Q1)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52205,74 +52189,70 @@
                     "title": "Pocket Card \u2013 FY16 (Q1)"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-300",
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
+            "title": "VA Benefits & Health Care Utilization  FY16 (Q1)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/iucp-d3u4",
-            "issued": "2023-07-04",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-11",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Mississippi FY2021",
+            "identifier": "https://www.data.va.gov/api/views/iucp-d3u4",
+            "issued": "2023-07-04",
             "keyword": [
                 "fy2021 data",
                 "mississippi",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/iucp-d3u4",
+            "landingPage": "https://www.data.va.gov/d/iucp-d3u4",
+            "modified": "2024-06-11",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Mississippi FY2021",
             "title": "NCVAS State Summary Mississippi FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ivyp-z6pa",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "disability",
-                "income",
-                "rural",
-                "unemployment",
-                "urban",
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
-            "identifier": "VA-OEI-OEI-164",
+            "dataQuality": true,
             "description": "<p>This speadsheet contains data from the 2014 American Community Survey and shows the demographic and socioeconomic characteristics of Veterans who live in rural and urban areas. The spreadsheet includes variables like: raw numbers, umemployment rate, disability rate, median personal income, age groups, period of service and other variables.</p>",
-            "title": "Rural Veterans by State (2014)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52281,76 +52261,77 @@
                     "title": "Rural Veterans by State"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-164",
+            "issued": "2017-07-26",
+            "keyword": [
+                "disability",
+                "income",
+                "rural",
+                "unemployment",
+                "urban",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ivyp-z6pa",
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
+            "title": "Rural Veterans by State (2014)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/iztu-68ne",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "oregon",
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
-            "identifier": "https://www.data.va.gov/api/views/iztu-68ne",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Oregon",
+            "identifier": "https://www.data.va.gov/api/views/iztu-68ne",
+            "issued": "2021-08-26",
+            "keyword": [
+                "oregon",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/iztu-68ne",
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
+            "title": "State Summaries_Oregon"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://inquiry.vba.va.gov/weamspub/buildSearchNE.do",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
-            "keyword": [
-                "education",
-                "national exam serach",
-                "weams"
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
-            "identifier": "VA-VBA-INFO-012",
+            "dataQuality": true,
             "description": "<p>Web ENabled Approval Management System (WEAMS) National Exams Search web link</p>",
-            "title": "WEAMS National Exams Search",
-            "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52359,73 +52340,76 @@
                     "title": "html"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-VBA-INFO-012",
+            "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "education",
+                "national exam serach",
+                "weams"
+            ],
+            "landingPage": "https://inquiry.vba.va.gov/weamspub/buildSearchNE.do",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
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
                 "WEAMS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "WEAMS National Exams Search"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/j2kz-5jpp",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Mississippi FY2023",
+            "identifier": "https://www.data.va.gov/api/views/j2kz-5jpp",
             "issued": "2024-06-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2024",
                 "mississippi",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/j2kz-5jpp",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/j2kz-5jpp",
-            "description": "NCVAS State Summary Mississippi FY2023",
-            "title": "NCVAS State Summary Mississippi FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Mississippi FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/j2qk-6bd8",
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
-            "identifier": "35f9d2af-958b-4b25-8313-84dd3a47c916",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Arizona FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52433,57 +52417,88 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "35f9d2af-958b-4b25-8313-84dd3a47c916",
+            "issued": "2018-10-29",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/j2qk-6bd8",
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
+            "title": "State Summary Arizona FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/j3m2-dn8u",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-06",
-            "keyword": [
-                "alaska",
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
-            "identifier": "https://www.data.va.gov/api/views/j3m2-dn8u",
+            "dataQuality": true,
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State and Territories.",
-            "title": "State Summaries_Alaska",
+            "identifier": "https://www.data.va.gov/api/views/j3m2-dn8u",
+            "issued": "2021-08-26",
+            "keyword": [
+                "alaska",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/j3m2-dn8u",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-06",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Alaska"
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
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR38_012016_Retrospective_Wait_Times_Desired_Date_by_Division.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Appointments 30 Dec 2015"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-737",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-12-30T05:00:00Z/2015-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -52497,53 +52512,41 @@
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
-            "identifier": "VA-VHA-OIA-737",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Dec 30",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR38_012016_Retrospective_Wait_Times_Desired_Date_by_Division.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Appointments 30 Dec 2015"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2015-12-30T05:00:00Z/2015-12-30T05:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Dec 30"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/j3ss-2phg",
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
+            "description": "<p>Occupational Health Record-keeping System (OHRS) is part of the Clinical Information Support System (CISS) portal framework and the initial CISS partner system.  OHRS is a web-based application that enables employee occupational health staff to create, maintain, and monitor medical records for VA employees and generate national, Veterans Integrated Service Network (VISN), and site-specific reports.The focus of OHRS is to collect clinical data for wellness, medical surveillance, and appropriate treatment of work-based injury or illness. OHRS will capture and store information on patient encounters, such as encounter type, purpose, status, provider, and other pertinent clinical data obtained during the patient visit. Users with appropriate security privileges are allowed to add and sign or co-sign the encounter and, if needed, perform scheduled and unscheduled reporting on items such as vaccination rates, vaccination and immunity statuses. The OHRS application does not share patient-specific data, but will collect data elements limited to information deemed critical to the Occupational Health delivery of care processes in the OHRS database. Employee data is obtained from the central Personnel and Accounting Integrated Data System (PAID) while volunteer information is obtained from the Voluntary Service System (VSS). Other Non-Paid and non-VSS data is collected by direct data entry into OHRS at the time of the patient encounter. OHRS is further designed to document, track and report immunizations administered to other Federal Agency employees outside of VA.</p>",
+            "identifier": "VA-VHA-OPH-009",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2009-09-09T04:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "employee",
                 "health",
@@ -52552,73 +52555,40 @@
                 "veteran",
                 "wellness"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/j3ss-2phg",
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
-            "identifier": "VA-VHA-OPH-009",
-            "description": "<p>Occupational Health Record-keeping System (OHRS) is part of the Clinical Information Support System (CISS) portal framework and the initial CISS partner system.  OHRS is a web-based application that enables employee occupational health staff to create, maintain, and monitor medical records for VA employees and generate national, Veterans Integrated Service Network (VISN), and site-specific reports.The focus of OHRS is to collect clinical data for wellness, medical surveillance, and appropriate treatment of work-based injury or illness. OHRS will capture and store information on patient encounters, such as encounter type, purpose, status, provider, and other pertinent clinical data obtained during the patient visit. Users with appropriate security privileges are allowed to add and sign or co-sign the encounter and, if needed, perform scheduled and unscheduled reporting on items such as vaccination rates, vaccination and immunity statuses. The OHRS application does not share patient-specific data, but will collect data elements limited to information deemed critical to the Occupational Health delivery of care processes in the OHRS database. Employee data is obtained from the central Personnel and Accounting Integrated Data System (PAID) while volunteer information is obtained from the Voluntary Service System (VSS). Other Non-Paid and non-VSS data is collected by direct data entry into OHRS at the time of the patient encounter. OHRS is further designed to document, track and report immunizations administered to other Federal Agency employees outside of VA.</p>",
-            "title": "Occupational Health Record-keeping System (OHRS)",
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
+            "title": "Occupational Health Record-keeping System (OHRS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/j3tk-xaw5",
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
                 "fn": "Office of Health Equity",
                 "hasEmail": "mailto:healthequity@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/j3tk-xaw5",
             "description": "A subset of the FY13 National Veteran Health Equity Report, filtered by race/ethnicity.\n\nThe National Veteran Health Equity Report details patterns and provides comparative rates of health conditions for vulnerable Veteran groups. Specifically, this report is designed to provide basic comparative information on the sociodemographics, utilization patterns and rates of diagnosed health conditions among the groups over which the VHA Office of Health Equity (OHE) has responsibility with respect to monitoring, evaluating and acting on identified disparities in access, use, care, quality and outcomes. The report allows the VA, Veterans, and stakeholders to monitor the care vulnerable Veterans receive and set goals for improving their care.",
-            "title": "VA-OHE-NVHER-FY13-Diagnoses-Race/Ethnicity",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52626,69 +52596,112 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/j3tk-xaw5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/j3tk-xaw5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/j3tk-xaw5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/j3tk-xaw5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/j3tk-xaw5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/j3tk-xaw5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/j3tk-xaw5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/j3tk-xaw5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/j3tk-xaw5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode"
+            "identifier": "https://www.data.va.gov/api/views/j3tk-xaw5",
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
+            "landingPage": "https://www.data.va.gov/d/j3tk-xaw5",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
+            "modified": "2021-07-19",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VA-OHE-NVHER-FY13-Diagnoses-Race/Ethnicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/j59u-gwiz",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-08",
-            "keyword": [
-                "utah",
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
-            "identifier": "https://www.data.va.gov/api/views/j59u-gwiz",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Utah",
+            "identifier": "https://www.data.va.gov/api/views/j59u-gwiz",
+            "issued": "2021-08-26",
+            "keyword": [
+                "utah",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/j59u-gwiz",
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
+            "title": "State Summaries_Utah"
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
+                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX_FY09_2.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "xls"
+                }
+            ],
+            "identifier": "VA-OEI-OEI-035",
             "issued": "2017-07-26",
-            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-19",
             "keyword": [
                 "2012",
                 "compensation and pension",
@@ -52702,66 +52715,37 @@
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
-            "identifier": "VA-OEI-OEI-035",
-            "description": "<p>This report details VA expenditures at the state, county, and Congressional District level. It includes categories such as Compensation and Pension, Construction, Insurance, and Medical Care. Veteran population estimates and the number of unique patients who used VA health care services are also available.</p>",
-            "title": "Geographic Distribution of VA Expenditures FY2009",
-            "programCode": [
-                "029:086"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/vetdata/docs/GDX/GDX_FY09_2.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "xls"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
             "theme": [
                 "Expenditures"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geographic Distribution of VA Expenditures FY2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/j754-wu5e",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "nevada"
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
-            "identifier": "VA-OEI-OEI-199",
             "description": "<p>This summary describes the programs and services VA provided in Nevada in fiscal year 2015.</p>",
-            "title": "State Summary: Nevada FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52770,82 +52754,82 @@
                     "title": "Nevada"
                 }
             ],
+            "identifier": "VA-OEI-OEI-199",
+            "issued": "2017-07-26",
+            "keyword": [
+                "nevada"
+            ],
+            "landingPage": "https://www.data.va.gov/d/j754-wu5e",
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
+            "title": "State Summary: Nevada FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-03-01T05:00:00Z/2014-03-01T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
-            "keyword": [
-                "media publications",
-                "va",
-                "vba"
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
-            "identifier": "VA-VBA-MEDIAPUB-060",
+            "dataQuality": true,
             "description": "<p>The Many Advantages of Hiring veterans</p>",
-            "title": "The Many Advantages of Hiring veterans",
+            "identifier": "VA-VBA-MEDIAPUB-060",
             "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "media publications",
+                "va",
+                "vba"
+            ],
+            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
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
-            "accrualPeriodicity": "R/P1M",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-03-01T05:00:00Z/2014-03-01T05:00:00Z",
             "theme": [
                 "General Benefit Information"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "The Many Advantages of Hiring veterans"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jb8q-qegp",
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
-            "identifier": "https://www.data.va.gov/api/views/jb8q-qegp",
+            "dataQuality": true,
             "description": "<p>VBA PROGRAM BENEFITS for Automobiles and Adaptive Equipment for Certain Disabled Veterans and Members of the Armed Forces. Veterans with honorable service and servicepersons on duty having a service-connected disability due to loss or permanent loss of use of one or both feet, one or both hands, or a permanent impairment of vision of both eyes to a prescribed degree. For adaptive equipment only, eligibility also exists if there is service-connected ankylosis of one or both knees or one or both hips. Personnel on active duty also qualify under the same criteria as veterans. Uses &amp; Use Restrictions:  Assistance toward purchase of an automobile or other conveyance is a one-time payment only. Necessary adaptive equipment may be furnished, repaired, replaced, or reinstalled on a conveyance which may be purchased with assistance or any other conveyance subsequently or previously acquired. Adaptive equipment will be provided for no more than two conveyances during any four-year period unless one of those two vehicles becomes unavailable to the veteran.</p>",
-            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE MAY2019",
-            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52853,66 +52837,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jb8q-qegp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jb8q-qegp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jb8q-qegp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/jb8q-qegp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jb8q-qegp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jb8q-qegp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jb8q-qegp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jb8q-qegp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jb8q-qegp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/jb8q-qegp",
+            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 100"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jb8q-qegp",
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
+            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE MAY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jbse-k73h",
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
-            "identifier": "VA-OEI-OEI-004",
-            "description": "<p>The Geographic Distribution of VA Expenditures (GDX)  is an annual report that shows estimated VA expenditures for major programmatic areas by geographic area (state, county, and congressional district). The major programmatic areas are: Compensation and Pension; Readjustment (Education) and Vocational Rehabilitation; Insurance; Construction; and, Medical and Administrative.</p>",
-            "title": "Veterans Affairs Geographic Distribution of Expenditures FY07 by State and County",
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
@@ -52920,48 +52902,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jbse-k73h/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jbse-k73h/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jbse-k73h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/jbse-k73h/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jbse-k73h/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jbse-k73h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jbse-k73h/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jbse-k73h/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jbse-k73h/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/Datagov/DataGov_GDX_FY07_Technical_Notes.doc",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-004",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "veteran"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jbse-k73h",
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
+            "title": "Veterans Affairs Geographic Distribution of Expenditures FY07 by State and County"
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
+            "description": "<p>This is a monthly report that the VA Office of Information Technology provides to congress about data incidents that took place during the month (May 2014).  The report contains details about and total numbers of mis-handling incidents;  mis-mailed incidents; mis-mailed CMOP incidents; IT equipment inventory incidents; missing stolen PC incidents; missing/stolen laptop incident; lost blackberry incidents;  and lost non-blackberry mobile devices (tablets, iPhones, androids, etc.) incidents.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/ABOUT_VA/docs/monthly_rfc_may2014.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-19",
             "issued": "2017-07-26",
-            "temporal": "2014-05-05T04:00:00Z/2014-06-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "blackberry",
                 "congress",
@@ -52976,65 +52989,39 @@
                 "stolen",
                 "va"
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
-            "identifier": "VA-OIT-ITIS-19",
-            "description": "<p>This is a monthly report that the VA Office of Information Technology provides to congress about data incidents that took place during the month (May 2014).  The report contains details about and total numbers of mis-handling incidents;  mis-mailed incidents; mis-mailed CMOP incidents; IT equipment inventory incidents; missing stolen PC incidents; missing/stolen laptop incident; lost blackberry incidents;  and lost non-blackberry mobile devices (tablets, iPhones, androids, etc.) incidents.</p>",
-            "title": "Department of Veterans Affairs - Monthly Report to Congress of Data Incidents (May 2014)",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/ABOUT_VA/docs/monthly_rfc_may2014.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-05-05T04:00:00Z/2014-06-01T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs - Monthly Report to Congress of Data Incidents (May 2014)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/jbuc-hw42",
-            "issued": "2024-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/jbuc-hw42",
             "description": "This table supports the data story entitled: \"How to Access Synthetic Data in the VA\"",
-            "title": "Synthetic Data Table",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53042,89 +53029,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jbuc-hw42/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jbuc-hw42/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jbuc-hw42/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/jbuc-hw42/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jbuc-hw42/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jbuc-hw42/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jbuc-hw42/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jbuc-hw42/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jbuc-hw42/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/jbuc-hw42",
+            "issued": "2024-10-31",
+            "landingPage": "https://www.data.va.gov/d/jbuc-hw42",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-10-31",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Synthetic Data Table"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/jbvh-nyt8",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Oregon FY2023",
+            "identifier": "https://www.data.va.gov/api/views/jbvh-nyt8",
             "issued": "2024-06-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "oregon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/jbvh-nyt8",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/jbvh-nyt8",
-            "description": "NCVAS State Summary Oregon FY2023",
-            "title": "NCVAS State Summary Oregon FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Oregon FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jce9-efvy",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-12-21",
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
-            "identifier": "https://www.data.va.gov/api/views/jce9-efvy",
             "description": "Data underlying the first figure in the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 1, Utilization by Program",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53132,57 +53113,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jce9-efvy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jce9-efvy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jce9-efvy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/jce9-efvy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jce9-efvy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jce9-efvy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jce9-efvy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jce9-efvy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jce9-efvy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/jce9-efvy",
+            "issued": "2020-12-21",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jce9-efvy",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 1, Utilization by Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jckr-i5ky",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2023-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-11",
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
-            "identifier": "https://www.data.va.gov/api/views/jckr-i5ky",
             "description": "The Study Interventions dataset includes information about each of the specific treatment arms that were studied in all RCTs. Each study arm was coded to indicate the type of intervention or comparison condition. This dataset includes the study-level Study Class as well as individual variables for each category of treatment, coded as Yes or No for each arm. Study arm treatment category variables are as follows: Pharmacotherapy (as well as a subclass such as antidepressant, antianxiety, etc.); Psychotherapy (as well as a subclass to identify trauma-focused or non-trauma-focused therapy); Complementary and Integrative Health (CIH; as well as a subclass such as relaxation or meditation); Nonpharmacologic Biological; Nonpharmacologic Cognitive; Collaborative Care; Other Treatments; Control\nThe Study Intervention dataset also includes information on the format of the treatment (individual, group, couples, mixed); treatment delivery method (in person, by phone, by video, technology alone, technology assisted, written or mixed); dose or amount of treatment and, treatment completion and adherence. Use this dataset to learn about treatment studies of a particular type\n\nEach record is an arm of the study, labeled as A, B, C, or D. Values abstracted as not applicable (\"NA\") or not reported (\"NR\") from the study are null values (empty cells).",
-            "title": "Study Interventions",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53190,60 +53174,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jckr-i5ky/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jckr-i5ky/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jckr-i5ky/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/jckr-i5ky/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jckr-i5ky/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jckr-i5ky/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jckr-i5ky/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jckr-i5ky/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jckr-i5ky/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/jckr-i5ky",
+            "issued": "2023-10-31",
+            "keyword": [
+                "ptsd-repository"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jckr-i5ky",
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
+            "title": "Study Interventions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jcqp-kqv6",
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
-            "identifier": "https://www.data.va.gov/api/views/jcqp-kqv6",
+            "dataQuality": true,
             "description": "VA All Employee Survey (AES) 2020 deidentified individual-level public release data file.",
-            "title": "AES 2020 PRDF",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53251,44 +53236,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jcqp-kqv6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jcqp-kqv6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jcqp-kqv6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/jcqp-kqv6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jcqp-kqv6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jcqp-kqv6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jcqp-kqv6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jcqp-kqv6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jcqp-kqv6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/jcqp-kqv6",
+            "issued": "2023-03-16",
+            "keyword": [
+                "survey",
+                "veterans affairs"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jcqp-kqv6",
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
+            "title": "AES 2020 PRDF"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN1FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 1 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-075",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -53304,76 +53316,44 @@
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
-            "identifier": "VA-VHA-OIA-075",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 1",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN1FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 1 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 1"
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
-            "identifier": "VA-VBA-ABR2012-007",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Beneficiaries Who Began Receiving DIC by Fiscal Year",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53381,50 +53361,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-007",
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
+            "title": "Beneficiaries Who Began Receiving DIC by Fiscal Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/DividendsByStateAndCounty.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Dividends_by_State_and_County.doc"
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
-            "identifier": "VA-VBA-INS2011-019",
+            "dataQuality": true,
             "description": "<p>The Dividends by State and County dataset provides the amount of insurance dividends paid in FY 2010 by state and county.  The data is reported at the state level, plus insureds in Military America, Military Europe, Military Pacific, American Samoa, Federated States of Micronesia, Guam, Marshall Islands, Northern Mariana Islands, Puerto Rico, and the Virgin Islands.</p>",
-            "title": "FY10_Insurance Dividends by State and County",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53432,66 +53410,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jdjt-6vn7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jdjt-6vn7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jdjt-6vn7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/jdjt-6vn7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jdjt-6vn7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jdjt-6vn7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jdjt-6vn7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jdjt-6vn7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jdjt-6vn7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-019",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/DividendsByStateAndCounty.csv",
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
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Dividends_by_State_and_County.doc"
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
+            "title": "FY10_Insurance Dividends by State and County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jdy9-43tk",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "kentucky",
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
-            "identifier": "VA-OEI-OEI-104",
             "description": "<p>This is a summary of the programs and services provided by VA in Kentucky in fiscal year 2014.</p>",
-            "title": "State Summary:  Kentucky",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53500,44 +53483,45 @@
                     "title": "State Summary:  Kentucky"
                 }
             ],
+            "identifier": "VA-OEI-OEI-104",
+            "issued": "2017-07-26",
+            "keyword": [
+                "kentucky",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jdy9-43tk",
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
+            "title": "State Summary:  Kentucky"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/je5m-2da5",
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
-            "identifier": "9732b5e2-28bf-44ef-9de8-ede45ab0b1ed",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Massachusetts FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53545,38 +53529,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "identifier": "9732b5e2-28bf-44ef-9de8-ede45ab0b1ed",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/je5m-2da5",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary Massachusetts FY2016"
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
-            "temporal": "2012-01-01T05:00:00Z/2012-03-31T04:00:00Z",
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
-            "identifier": "VA-OM-OM-086",
+            "dataQuality": true,
             "description": "<p>FY 2012 Second Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2012 Second Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53585,44 +53569,43 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-086",
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
+            "temporal": "2012-01-01T05:00:00Z/2012-03-31T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2012 Second Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jezp-webt",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "alaska",
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
-            "identifier": "VA-OEI-OEI-087",
             "description": "<p>This describes the services and programs VA provided in Alaska in fiscal year 2014</p>",
-            "title": "State Summary:  Alaska",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53631,47 +53614,46 @@
                     "title": "State Summary:  Alaska"
                 }
             ],
+            "identifier": "VA-OEI-OEI-087",
+            "issued": "2017-07-26",
+            "keyword": [
+                "alaska",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jezp-webt",
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
+            "title": "State Summary:  Alaska"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VBA/blob/master/VGLI%20Coverage%20Amount%20as%20of%2011-30-13.xls",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-11-01T04:00:00Z/2013-11-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "2013",
-                "life insurance policies",
-                "vgli"
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
-            "identifier": "VA-VBA-INS2014-005",
+            "dataQuality": true,
             "description": "<p>VBA- Insurance Lob- VGLI Coverage Amount as of 11-30-2013.</p>",
-            "title": "VGLI Coverage Amount as of 11/30/2013",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53680,135 +53662,136 @@
                     "title": "xls"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2014-005",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "2013",
+                "life insurance policies",
+                "vgli"
+            ],
+            "landingPage": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VBA/blob/master/VGLI%20Coverage%20Amount%20as%20of%2011-30-13.xls",
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
+            "temporal": "2013-11-01T04:00:00Z/2013-11-30T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VGLI Coverage Amount as of 11/30/2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/jfc9-shq4",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-19",
-            "keyword": [
-                "california",
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
-            "identifier": "https://www.data.va.gov/api/views/jfc9-shq4",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_California",
+            "identifier": "https://www.data.va.gov/api/views/jfc9-shq4",
+            "issued": "2021-08-26",
+            "keyword": [
+                "california",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jfc9-shq4",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-04-19",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_California"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/jfpg-kfan",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Alabama FY2023",
+            "identifier": "https://www.data.va.gov/api/views/jfpg-kfan",
             "issued": "2024-05-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-10",
             "keyword": [
                 "alabama",
                 "fy2024 data",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/jfpg-kfan",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-07-10",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/jfpg-kfan",
-            "description": "NCVAS State Summary Alabama FY2023",
-            "title": "NCVAS State Summary Alabama FY2023",
-            "programCode": [
-                "029:086"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "title": "NCVAS State Summary Alabama FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/jfrq-ifuv",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Ohio FY2023",
+            "identifier": "https://www.data.va.gov/api/views/jfrq-ifuv",
             "issued": "2024-06-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "ohio"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/jfrq-ifuv",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/jfrq-ifuv",
-            "description": "NCVAS State Summary Ohio FY2023",
-            "title": "NCVAS State Summary Ohio FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Ohio FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jgap-k4zf",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "veterans",
-                "west virginia"
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
-            "identifier": "VA-OEI-OEI-136",
             "description": "<p>This is a summary of the programs and services provided by VA in West Virginia in fiscal year 2014.</p>",
-            "title": "State Summary:  Wisconsin",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53817,45 +53800,45 @@
                     "title": "State Summary:  Wisconsin"
                 }
             ],
+            "identifier": "VA-OEI-OEI-136",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans",
+                "west virginia"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jgap-k4zf",
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
+            "title": "State Summary:  Wisconsin"
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
-            "identifier": "VA-OEI-OEI-147",
+            "dataQuality": true,
             "description": "<p>This reports the activities of the Veterans Administration for the fiscal year ending September 30, 1984.</p>",
-            "title": "Annual Report:  1984",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53864,45 +53847,45 @@
                     "title": "Annual Report:  1984"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-147",
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
+            "title": "Annual Report:  1984"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jiqc-7zwi",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "public",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2012-01-01T05:00:00Z/2012-01-01T05:00:00Z",
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
-            "identifier": "VA-OEI-OEI-062",
+            "dataQuality": true,
             "description": "<p>Minority Veterans Profile 2012 uses data from the 2012 American Community Survey to compare the demographic and socioeconomic characteristics of minority Veterans and minority non-Veterans.</p>",
-            "title": "Minority Veterans Profile 2012",
-            "programCode": [
-                "029:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53911,111 +53894,112 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-062",
+            "issued": "2017-07-26",
+            "keyword": [
+                "minority",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jiqc-7zwi",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
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
+            "title": "Minority Veterans Profile 2012"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jix8-dw27",
-            "issued": "2023-08-10",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-19",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Tennessee FY2021",
+            "identifier": "https://www.data.va.gov/api/views/jix8-dw27",
+            "issued": "2023-08-10",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "tennessee"
             ],
-            "identifier": "https://www.data.va.gov/api/views/jix8-dw27",
+            "landingPage": "https://www.data.va.gov/d/jix8-dw27",
+            "modified": "2024-06-19",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Tennessee FY2021",
             "title": "NCVAS State Summary Tennessee FY2021"
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
+            "description": "<p>USA Spending- Compensation and Pension- Burial Expenses Allowance for Vets for February 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING012014-031",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
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
-            "identifier": "VA-VBA-USASPENDING012014-031",
-            "description": "<p>USA Spending- Compensation and Pension- Burial Expenses Allowance for Vets for February 2013.</p>",
-            "title": "USA Spending file- 02/2014 Compensation and Pension-  CFDA 64.101",
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
+            "title": "USA Spending file- 02/2014 Compensation and Pension-  CFDA 64.101"
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
-                "employment",
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
-            "identifier": "VA-OEI-OEI-235",
+            "dataQuality": true,
             "description": "<p>This quick facts summarizes the Veteran new hires into the Federal government by disabled and by 30 percent and higher disabled groups for 2008 to 2015. It shows the Veteran new hires by agency for 2015 and Veterans by occupation for 2015.</p>",
-            "title": "Employment of Veterans in Executive Branch",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54024,48 +54008,46 @@
                     "title": "Employment of Veterans in Federal Executive Branch: FY 2008 to FY2015"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-235",
+            "issued": "2017-07-26",
+            "keyword": [
+                "employment",
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
+            "title": "Employment of Veterans in Executive Branch"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/jksy-jd4d",
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
-            "identifier": "f710f309-f11c-450c-ac67-a77ec0e57a66",
+            "dataQuality": true,
             "description": "<p>Beginning with the Government Paperwork Elimination Act of 1998 (GPEA), the Federal government has encouraged the use of electronic / digital signatures to enable electronic transactions with agencies, while still providing a means for proof of user consent and non-repudiation. To support this capability, some means of reliable user identity management must exist. Currently, Veterans have to physically print, sign, and mail various documents that, in turn, need to be processed by VA. This process creates a huge inconvenience on the part of the veteran and a financial burden on VA. eSig enables veterans and their surrogates to digitally sign forms that require a high level of verification that the user signing the document is a legitimate and authorized user. In addition, eSig provides a mechanism for VA applications to verify the authenticity of user documents and data integrity on user forms. This capability is enabled by the eSig service. The eSig service signing process includes the following steps: 1. Form Signing Attestation: The user affirms their intent to electronically sign the document and understands re-authentication is part of that process. 2. Re-Authentication: The user must refresh their authentication by repeating the authentication process. 3. Form Signing: The form and the identity of the user are presented to the eSig service, where they are digitally bound and secured. 4. Form Storage: The signed form must be stored for later validation. In this process, the application is entirely responsible for steps 1, 2, and 4. In step 3, the application must use the eSig web service to request signing of the document. The following table lists the detailed functions offered by the eSig service.</p>",
-            "title": "Electronic Signature (eSig)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54074,67 +54056,68 @@
                     "title": "Electronic Signature (eSig)"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "f710f309-f11c-450c-ac67-a77ec0e57a66",
+            "issued": "2018-02-23",
+            "keyword": [
+                "access",
+                "identity",
+                "security"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jksy-jd4d",
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
+            "title": "Electronic Signature (eSig)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/jmm5-cgfz",
-            "issued": "2021-08-27",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
-            "keyword": [
-                "guam",
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
-            "identifier": "https://www.data.va.gov/api/views/jmm5-cgfz",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Guam",
+            "identifier": "https://www.data.va.gov/api/views/jmm5-cgfz",
+            "issued": "2021-08-27",
+            "keyword": [
+                "guam",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jmm5-cgfz",
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
+            "title": "State Summaries_Guam"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jndj-wi8n",
-            "bureauCode": [
-                "029:40"
-            ],
-            "issued": "2017-07-26",
             "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "ogc",
-                "opinion"
+            "accessLevel": "public",
+            "bureauCode": [
+                "029:40"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OGC Law Library",
                 "hasEmail": "mailto:OGCLawLibrary@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-041",
             "description": "<p>Applicability of 38 U.S.C. \u00a7 3677(c)(7) for Approval of On-The-Job Program for Employees of State Approving Authorities</p>",
-            "title": "OGC Precedent Opinion 5-2010",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54143,66 +54126,95 @@
                     "title": "OGC Precedent Opinion 5-2010"
                 }
             ],
+            "identifier": "VA-OGC-041",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jndj-wi8n",
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
+            "title": "OGC Precedent Opinion 5-2010"
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
-            "identifier": "VA-VBA-MEDIAPUB-062",
+            "dataQuality": true,
             "description": "<p>Summary of VA Benefits for Disabled Veterans</p>",
-            "title": "Summary of VA Benefits for Disabled Veterans",
+            "identifier": "VA-VBA-MEDIAPUB-062",
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
+            "title": "Summary of VA Benefits for Disabled Veterans"
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
-            "temporal": "2015-06-01T04:00:00Z/2015-06-01T04:00:00Z",
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
+                    "downloadURL": "https://www.va.gov/health/docs/June_1_2015_Pending_Public_Data_06182015.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 1 June 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-108",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -54216,113 +54228,85 @@
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
-            "identifier": "VA-VHA-OIA-108",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 June 1",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/June_1_2015_Pending_Public_Data_06182015.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 1 June 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-06-01T04:00:00Z/2015-06-01T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 June 1"
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
+            "description": "<p>Benepisyo Para Sa Mga Nakaligtas Na Mga Beteranong Pilipino</p>",
+            "identifier": "VA-VBA-MEDIAPUB-041",
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
-                "fn": "Thomas Elwell",
-                "hasEmail": "mailto:thomas.elwell@va.gov"
-            },
+            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
+            "language": [
+                "fil-PH"
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
-            "identifier": "VA-VBA-MEDIAPUB-041",
-            "description": "<p>Benepisyo Para Sa Mga Nakaligtas Na Mga Beteranong Pilipino</p>",
-            "title": "Benepisyo Para Sa Mga Nakaligtas Na Mga Beteranong Pilipino",
-            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2008-10-01T04:00:00Z/2008-10-01T04:00:00Z",
             "theme": [
                 "General Benefit Information"
             ],
-            "language": [
-                "fil-PH"
-            ]
+            "title": "Benepisyo Para Sa Mga Nakaligtas Na Mga Beteranong Pilipino"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jp6r-ri7w",
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
-            "identifier": "https://www.data.va.gov/api/views/jp6r-ri7w",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE APR2019",
-            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54330,63 +54314,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jp6r-ri7w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jp6r-ri7w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jp6r-ri7w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/jp6r-ri7w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jp6r-ri7w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jp6r-ri7w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jp6r-ri7w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jp6r-ri7w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jp6r-ri7w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/jp6r-ri7w",
+            "isPartOf": "556ed405-3a6a-44b5-9911-7ce62cff5edf",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 120"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jp6r-ri7w",
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
+            "title": "USA SPENDING EDUCATION CH32 B120 POST-VIETNAM ERA VETERANS' EDUCATIONAL ASSISTANCE APR2019"
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
-            "identifier": "VA-VBA-ABR2012-042",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Entitlement Loans Guaranteed by Fiscal Year",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54394,44 +54374,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-042",
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
+            "title": "Entitlement Loans Guaranteed by Fiscal Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jpcs-ee9q",
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
-            "identifier": "https://www.data.va.gov/api/views/jpcs-ee9q",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to help servicepersons adjust to civilian life after separation from military service, assist in the recruitment and retention of highly qualified personnel in the active and reserve components in the Armed Forces by providing education benefits, and to provide educational opportunities to the dependents of certain service members and veterans. Individuals who entered active duty after September 10, 2001 may be eligible for the Post-9/11 GI Bill. Individuals can use the Post-9/11 GI Bill after serving 90 days on active duty (excluding entry level and skill training). Only periods of active duty under title 10 will be used to establish eligibility for the Post 9/11 GI Bill. A high school diploma or equivalency certificate is always required for eligibility. Individuals who are eligible for the Montgomery GI Bill \u2013 Active Duty (chapter 30), the Montgomery GI Bill \u2013 Selected Reserve (chapter 1606), or the Reserve Educational Assistance Program (REAP) will have to make an irrevocable election to relinquish eligibility under one of those benefit programs to establish eligibility under the Post-9/11 GI Bill. The dependent children of a person who died in the line of duty while serving as a member of the Armed Forces may be eligible to use benefits under the Fry Scholarship provision of the Post-9/11 GI Bill. The spouse and/or child(ren) of a veteran or service member may be eligible for the Post 9/11 GI Bill if the veteran or service member transfers entitlement to those dependents. Eligibility to transfer entitlement to dependents is determined by the Department of Defense. This is not a complete list of eligibility requirements. For more information on the latest changes to the Post-9/11 GI Bill go to the VA web-site.</p>",
-            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE APR2019",
-            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54439,63 +54423,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jpcs-ee9q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jpcs-ee9q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jpcs-ee9q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/jpcs-ee9q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jpcs-ee9q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jpcs-ee9q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jpcs-ee9q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jpcs-ee9q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jpcs-ee9q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/jpcs-ee9q",
+            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 028"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jpcs-ee9q",
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
+            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jpz2-637p",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-04-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-17",
-            "keyword": [
-                "ethnicity",
-                "historical period estimate",
-                "race",
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
-            "identifier": "https://www.data.va.gov/api/views/jpz2-637p",
             "description": "The Department of Veterans Affairs provides official estimates and projections of the Veteran population using the Veteran Population Projection Model (VetPop). Based on the available information through September 30, 2020, the latest model VetPop2020 estimated the Veteran population for the period from 2000 to 2020. This data table shows the number of living Veterans at the end of each fiscal year from 2000 to 2020 by race, ethnicity, gender, and age group for Veterans residing in the U.S. (50 states and D.C.).",
-            "title": "VetPop2020 National Estimates by Race 2000 to 2020",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54503,59 +54484,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jpz2-637p/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jpz2-637p/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jpz2-637p/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/jpz2-637p/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jpz2-637p/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jpz2-637p/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jpz2-637p/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jpz2-637p/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jpz2-637p/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/jpz2-637p",
+            "issued": "2024-04-17",
+            "keyword": [
+                "ethnicity",
+                "historical period estimate",
+                "race",
+                "veteran population"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jpz2-637p",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-04-17",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020 National Estimates by Race 2000 to 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jrjd-qghv",
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
-            "identifier": "https://www.data.va.gov/api/views/jrjd-qghv",
             "description": "VetPop2023 projection of living Veterans by gender and 4 age groups at the county level. \n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2023 County Data, 9L",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54563,87 +54544,90 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jrjd-qghv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jrjd-qghv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jrjd-qghv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/jrjd-qghv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jrjd-qghv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jrjd-qghv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jrjd-qghv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jrjd-qghv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jrjd-qghv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/jrjd-qghv",
+            "issued": "2024-09-09",
+            "keyword": [
+                "veteran population",
+                "veterans",
+                "vetpop",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jrjd-qghv",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-09",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 County Data, 9L"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/js9q-3wam",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary California FY2023",
+            "identifier": "https://www.data.va.gov/api/views/js9q-3wam",
             "issued": "2024-05-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "california",
                 "fy2023 data",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/js9q-3wam",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/js9q-3wam",
-            "description": "NCVAS State Summary California FY2023",
-            "title": "NCVAS State Summary California FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary California FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jsft-ntzb",
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
-            "identifier": "https://www.data.va.gov/api/views/jsft-ntzb",
+            "dataQuality": true,
             "description": "<p>VBA COMPENSTATION BENEFITS PRGOGRAM to provide vocational training and rehabilitation to certain children born with spina bifida or other covered birth defects who are children of Vietnam veterans and some Korean veterans. \u201cA child born with spina bifida or other covered birth defects, except spina bifida occulta, who is the natural child of a Vietnam veteran and some Korean veterans, regardless of the age or marital status of the child, conceived after the date on which the veteran first served in the Republic of Vietnam during the Vietnam era and in particular areas near the DMZ in the Korean conflict. VA must also determine that it is feasible for the child to achieve a vocational goal.\u201d</p>",
-            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA APR2019",
-            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54651,46 +54635,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jsft-ntzb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jsft-ntzb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jsft-ntzb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/jsft-ntzb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jsft-ntzb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jsft-ntzb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jsft-ntzb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jsft-ntzb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jsft-ntzb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/jsft-ntzb",
+            "isPartOf": "faff9e4c-e7ad-440d-bd48-6843c4358f8a",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 127"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jsft-ntzb",
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
+            "title": "USA SPENDING COMPENSATION CH18 B127 ALLOWANCE FOR CHILDREN OF VIETNAM VETERANS BORN WITH SPINA BIFIDA APR2019"
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
+                    "downloadURL": "https://www.va.gov/health/docs/VISN15FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 15 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-087",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -54706,54 +54718,45 @@
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
-            "identifier": "VA-VHA-OIA-087",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN15FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 15 Fact Sheet"
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
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/jvmd-8fgj",
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
+            "description": "<p>The Veterans Affairs Central Cancer Registry (VACCR) receives and stores information on cancer diagnosis and treatment constraints compiled and sent in by the local cancer registry staff at each of the 132 Veterans Affairs Medical Centers that diagnose and/or treat Veterans with cancer. The information sent is encoded to meet the site-specific requirements for registry inclusion as established by several oversight bodies, including the North American Association of Central Cancer Registries, the American College of Surgeons' Commission on Cancer, and the American Joint Commission on Cancer, among others. The information is obtained from a wide variety of medical record documents at the local medical center pertaining to each Veterans Health Administration (VHA) cancer patient. The information is then transmitted to the VACCR. Details collected include extensive demographics, cancer identification, extent of disease and staging, first course of treatment, and outcomes. Data extraction is available to researchers with VA approved Institutional Review Board studies, peer review, and Data Use Agreements.</p>",
+            "identifier": "VA-VHA-PCS-015",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1995-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "cancer",
                 "diagnosis",
@@ -54766,61 +54769,41 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/jvmd-8fgj",
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
-            "identifier": "VA-VHA-PCS-015",
-            "description": "<p>The Veterans Affairs Central Cancer Registry (VACCR) receives and stores information on cancer diagnosis and treatment constraints compiled and sent in by the local cancer registry staff at each of the 132 Veterans Affairs Medical Centers that diagnose and/or treat Veterans with cancer. The information sent is encoded to meet the site-specific requirements for registry inclusion as established by several oversight bodies, including the North American Association of Central Cancer Registries, the American College of Surgeons' Commission on Cancer, and the American Joint Commission on Cancer, among others. The information is obtained from a wide variety of medical record documents at the local medical center pertaining to each Veterans Health Administration (VHA) cancer patient. The information is then transmitted to the VACCR. Details collected include extensive demographics, cancer identification, extent of disease and staging, first course of treatment, and outcomes. Data extraction is available to researchers with VA approved Institutional Review Board studies, peer review, and Data Use Agreements.</p>",
-            "title": "Veterans Affairs Central Cancer Registry (VACCR)",
-            "programCode": [
-                "029:040"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1995-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Affairs Central Cancer Registry (VACCR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jvpw-w3g3",
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
-            "identifier": "VA-OM-OM-179",
             "description": "<p>COIN 146 report  for June 2016</p>",
-            "title": "COIN 146 report  for June 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54829,44 +54812,41 @@
                     "title": "COIN 146 June 2016"
                 }
             ],
+            "identifier": "VA-OM-OM-179",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jvpw-w3g3",
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
+            "title": "COIN 146 report  for June 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jwup-zh9z",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-02-02",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-08",
-            "keyword": [
-                "compensation and pension",
-                "fy20",
-                "fy 20",
-                "fy2020",
-                "fy 2020",
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
-            "identifier": "https://www.data.va.gov/api/views/jwup-zh9z",
+            "dataQuality": true,
             "description": "This report provides state-level estimates of the number of Veterans who received VA Pension benefits during fiscal year 2020.  It includes the Veterans\u2019 gender.  Blank values represent small cell counts that have been suppressed to protect the identity of Veterans.  Some categories may not sum to the total due to missing information (e.g., gender, etc.).\n                                                                                                    \nSource: Department of Veterans Affairs, Office of Enterprise Integration, United States Veterans Eligibility Trends & Statistics (USVETS) 2020 and Veterans Benefits Administration VETSNET FY 2020 pension data.\n \nPrepared by National Center for Veterans Analysis & Statistics, www.va.gov/vetdata.",
-            "title": "FY 2020 Pension Recipients by State",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54874,61 +54854,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jwup-zh9z/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jwup-zh9z/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jwup-zh9z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/jwup-zh9z/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jwup-zh9z/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jwup-zh9z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jwup-zh9z/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jwup-zh9z/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jwup-zh9z/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/jwup-zh9z",
+            "issued": "2022-02-02",
+            "keyword": [
+                "compensation and pension",
+                "fy20",
+                "fy 20",
+                "fy2020",
+                "fy 2020",
+                "pension",
+                "state"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jwup-zh9z",
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
+            "title": "FY 2020 Pension Recipients by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jxjh-pik9",
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
-            "identifier": "VA-OEI-OEI-106",
             "description": "<p>This is a summary of the programs and services provided by VA in Maine in fiscal year 2014.</p>",
-            "title": "State Summary:  Maine",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54937,50 +54921,44 @@
                     "title": "State Summary:  Maine"
                 }
             ],
+            "identifier": "VA-OEI-OEI-106",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jxjh-pik9",
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
+            "title": "State Summary:  Maine"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Enrollment_by_State_April_2012.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-01-01T05:00:00Z/2012-04-30T04:00:00Z",
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
-            "identifier": "VA-VBA-INS2012-009",
+            "dataQuality": true,
             "description": "<p>Provides the number of Veterans insured under the Veterans' Group Life Insurance (VGLI) program by state.  This report provides a snapshot of the active VGLI membership as of April 30, 2012.  For members who reside outside the United States, membership is not identified by individual country.  The total number of members was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "Number of Veterans Insured by VGLI by State as of April 30, 2012",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54988,96 +54966,104 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jy9v-bi8z/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jy9v-bi8z/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jy9v-bi8z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/jy9v-bi8z/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jy9v-bi8z/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jy9v-bi8z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/jy9v-bi8z/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/jy9v-bi8z/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/jy9v-bi8z/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-009",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Enrollment_by_State_April_2012.csv",
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
+            "temporal": "2012-01-01T05:00:00Z/2012-04-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Number of Veterans Insured by VGLI by State as of April 30, 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jyb7-yupa",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2020-06-21",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
-            "keyword": [
-                "data stories",
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
-            "identifier": "https://www.data.va.gov/api/views/jyb7-yupa",
             "description": "A collection of the stories in the PTSD Repository.",
-            "title": "PTSD Repository Data Stories",
+            "identifier": "https://www.data.va.gov/api/views/jyb7-yupa",
+            "issued": "2020-06-21",
+            "keyword": [
+                "data stories",
+                "ptsd-repository"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jyb7-yupa",
+            "modified": "2024-09-04",
             "programCode": [
                 "029:000"
             ],
-            "accrualPeriodicity": "R/P1Y"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for PTSD"
+            },
+            "rights": "All data is within the public domain and is currently available for download.",
+            "title": "PTSD Repository Data Stories"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/jycc-4qrh",
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
-            "title": "Equitable Relief Reports 2014",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55085,28 +55071,57 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/jycc-4qrh",
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
+            "title": "Equitable Relief Reports 2014"
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
+                    "downloadURL": "https://www.va.gov/health/docs/April_2015_Completed_Public_Data.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Appointments 30 Apr 2015"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-107",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-04-30T04:00:00Z/2015-04-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -55120,75 +55135,40 @@
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
-            "identifier": "VA-VHA-OIA-107",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Apr 30",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/April_2015_Completed_Public_Data.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Appointments 30 Apr 2015"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2015-04-30T04:00:00Z/2015-04-30T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 Apr 30"
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
-            "identifier": "VA-VBA-ABR2012-029",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Summary of Active Compensation Benefit Accounts at the End of FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55196,46 +55176,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-029",
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
+            "title": "Summary of Active Compensation Benefit Accounts at the End of FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/Surveys.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2004-12-01T05:00:00Z/2005-05-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "disability compensation",
-                "ratings",
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
-            "identifier": "VA-OEI-OEI-51",
+            "dataQuality": true,
             "description": "<p>The paper provids analytical support to the VA by reporting on the state-by-state and VA regional office variation in disability compensation claims, ratings, and monetary benefits.</p>",
-            "title": "Analysis of Differences in Disability Compensation in the Department of Veterans Affairs",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55244,25 +55226,56 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-51",
+            "issued": "2017-07-26",
+            "keyword": [
+                "disability compensation",
+                "ratings",
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
+            "temporal": "2004-12-01T05:00:00Z/2005-05-31T04:00:00Z",
             "theme": [
                 "Compensation Data on Veterans"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Analysis of Differences in Disability Compensation in the Department of Veterans Affairs"
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
+            "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/k2gq-ejqe/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                }
+            ],
+            "identifier": "VA-VBA-ABR2012-087",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
             "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
             "keyword": [
                 "fy2012 benefits",
                 "fy2012 vba",
@@ -55270,67 +55283,37 @@
                 "vba benefits",
                 "vba benefits by state"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Elwell",
-                "hasEmail": "mailto:thomas.elwell@va.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-087",
-            "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Florida-FY12  Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-02",
             "programCode": [
                 "029:003"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/k2gq-ejqe/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
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
+            "title": "Florida-FY12  Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/k2yg-eepq",
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
-            "identifier": "OM-OM-164",
             "description": "<p>Coin report 0017 for April 2016</p>",
-            "title": "COIN 0017 April 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55338,46 +55321,43 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-164",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/k2yg-eepq",
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
+            "title": "COIN 0017 April 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/k42f-3ku6",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2024-08-07",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
-            "keyword": [
-                "compensation",
-                "county",
-                "disability",
-                "fy19",
-                "fy 19",
-                "fy2019",
-                "fy 2019"
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
-            "identifier": "https://www.data.va.gov/api/views/k42f-3ku6",
+            "dataQuality": true,
             "description": "This report provides county-level estimates of the number of Veterans who received VA Disability Compensation benefits during fiscal year 2019. It includes the Veterans\u2019 total service-connected disability (SCD) rating, age group, and gender. Blank values represent small cell counts that have been suppressed to protect the identity of Veterans. Some categories may not sum to the total due to missing information (e.g., age, gender, etc.).\n\nSource: Department of Veterans Affairs, Office of Enterprise Integration, United States Veterans Eligibility Trends & Statistics (USVETS) 2019\n\nPrepared by National Center for Veterans Analysis & Statistics, www.va.gov/vetdata",
-            "title": "FY 2019 Disability Compensation Recipients by County",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55385,47 +55365,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/k42f-3ku6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k42f-3ku6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k42f-3ku6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/k42f-3ku6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k42f-3ku6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/k42f-3ku6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/k42f-3ku6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/k42f-3ku6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
```

