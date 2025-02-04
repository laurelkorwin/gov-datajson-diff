# Change History for dol.json (Part 2)

### Changes from 31606f9 to dd2190f (Part 2/2)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "description": "Historical series of Unemployment Insurance (UI) Financial Transaction Summary Reports (ETA-2112) in which states report monthly transactions summaries from state unemployment trust fund. The reports include the clearing account, the Unemployment Trust Fund Account (UTF) and the Benefit Payment Account.",
+            "identifier": "ETA-5-012:013-472",
             "keyword": [
                 "ETA",
                 "benefits",
@@ -14980,79 +14974,79 @@
                 "financial transactions",
                 "unemployment trust fund"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_2112",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:35:00.058Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Unemployment Insurance Clearing Account Transactions (ETA-8405)",
-            "description": "Historical series of Monthly Analsysis of Clearing Account Reports (ETA-8405) in which states provide monthly summaries of transactions in the state's Unemployment Insurance  clearing accounts in which employer contributions are initially deposited.",
-            "modified": "2024-03-29T16:27:48.046Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-474",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_8405",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Unemployment Insurance Financial Transaction Data (ETA-2112)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
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
+            "description": "Historical series of Monthly Analsysis of Clearing Account Reports (ETA-8405) in which states provide monthly summaries of transactions in the state's Unemployment Insurance  clearing accounts in which employer contributions are initially deposited.",
+            "identifier": "ETA-5-012:013-474",
             "keyword": [
                 "ETA",
                 "clearing account",
                 "deposits",
                 "employer refunds"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_8405",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:27:48.046Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Certifications data",
-            "description": "List of National Certifications. Dataset includes information on certification name, acronym, certifying organization, related O*NET occupation and NAICS industry codes, and accrediting agencies. Dataset also includes indicators to identify if the certification is in-demand, if it is included in the military COOL database, as well as other data sets. Certifying organization data includes address, contact information, and acronyms. \n\nNational certifications are nationally recognized awards that can attest to skills and knowledge in a particular area. \n\nCareerOneStop.org web service available upon request.",
-            "modified": "2024-02-13T19:01:24.593Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:018-454",
-            "landingPage": "https://www.careeronestop.org/Developers/Data/certifications.aspx",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "State Unemployment Insurance Clearing Account Transactions (ETA-8405)"
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
                 "fn": "Steve Rietzke",
                 "hasEmail": "mailto:rietzke.steven@dol.gov"
             },
+            "description": "List of National Certifications. Dataset includes information on certification name, acronym, certifying organization, related O*NET occupation and NAICS industry codes, and accrediting agencies. Dataset also includes indicators to identify if the certification is in-demand, if it is included in the military COOL database, as well as other data sets. Certifying organization data includes address, contact information, and acronyms. \n\nNational certifications are nationally recognized awards that can attest to skills and knowledge in a particular area. \n\nCareerOneStop.org web service available upon request.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.careeronestop.org/Developers/Data/certifications.aspx",
-                    "title": "Certifications",
-                    "description": "Information for certifications includes: name, acronym, related O*NET and NAICS codes, and accrediting agencies. There are also indicators to identify if the certification is in-demand, if it is included in the military COOL database, as well as other data sets. Certifying organization data includes address, contact information, and acronyms."
+                    "description": "Information for certifications includes: name, acronym, related O*NET and NAICS codes, and accrediting agencies. There are also indicators to identify if the certification is in-demand, if it is included in the military COOL database, as well as other data sets. Certifying organization data includes address, contact information, and acronyms.",
+                    "title": "Certifications"
                 }
             ],
+            "identifier": "ETA-5-012:018-454",
             "keyword": [
                 "ETA",
                 "certifications",
@@ -15061,39 +15055,39 @@
                 "occupataional requirements",
                 "occupational codes"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.careeronestop.org/Developers/Data/certifications.aspx",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-02-13T19:01:24.593Z",
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
+            "rights": "true",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "National Certifications data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Office of Trade Adjustment Assistance (OTAA) Petition Data",
-            "description": "Contains a list of all Trade Adjustment Assistance Act petitions going back to 1974 and is used for tracking petition statistics, internal process timings, and dissemination on the website.  Processing data is not captured for all years in the period.  This includes both internally created data and data collected through OMB Control No. 1205-0342.",
-            "modified": "2024-07-11T15:21:05.987Z",
             "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:011-504",
-            "describedBy": "https://www.dol.gov/sites/dolgov/files/ETA/tradeact/pdfs/Petition_Data_Dictionary.pdf",
-            "landingPage": "https://www.dol.gov/agencies/eta/tradeact/data/petitions-determinations",
-            "rights": "Not Available",
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
                 "fn": "Susan Manikowski",
                 "hasEmail": "mailto:manikowski.susan@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/sites/dolgov/files/ETA/tradeact/pdfs/Petition_Data_Dictionary.pdf",
+            "description": "Contains a list of all Trade Adjustment Assistance Act petitions going back to 1974 and is used for tracking petition statistics, internal process timings, and dissemination on the website.  Processing data is not captured for all years in the period.  This includes both internally created data and data collected through OMB Control No. 1205-0342.",
+            "identifier": "ETA-5-012:011-504",
             "keyword": [
                 "ETA",
                 "case",
@@ -15105,39 +15099,39 @@
                 "taa",
                 "trade"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/tradeact/data/petitions-determinations",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-07-11T15:21:05.987Z",
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
+            "title": "Office of Trade Adjustment Assistance (OTAA) Petition Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "National Agricultural Workers Survey (Restricted Use)",
-            "description": "The National Agricultural Workers Survey (NAWS) is an employment-based, random-sample survey of U.S. crop workers that collects demographic, employment, and health data in face-to-face interviews.  The survey began in fiscal year 1989 and nearly 70,000 workers have been interviewed since then.  There are three data files. The primary or National Agricultural Workers Survey Public Access Data (NAWSPAD) file corresponds to the base questionnaire; two smaller files correspond to supplemental questions that ETA administered for the National Institute for Occupational Safety and Health (NIOSH) and the Environmental Protection Agency (EPA).",
-            "modified": "2023-03-14T00:00:00Z",
             "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:018-515",
-            "describedBy": "https://www.dol.gov/agencies/eta/national-agricultural-workers-survey/data",
-            "landingPage": "https://www.dol.gov/agencies/eta/national-agricultural-workers-survey/data",
-            "rights": "Not Available",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Wayne Gordon",
                 "hasEmail": "mailto:gordon.wayne@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/national-agricultural-workers-survey/data",
+            "description": "The National Agricultural Workers Survey (NAWS) is an employment-based, random-sample survey of U.S. crop workers that collects demographic, employment, and health data in face-to-face interviews.  The survey began in fiscal year 1989 and nearly 70,000 workers have been interviewed since then.  There are three data files. The primary or National Agricultural Workers Survey Public Access Data (NAWSPAD) file corresponds to the base questionnaire; two smaller files correspond to supplemental questions that ETA administered for the National Institute for Occupational Safety and Health (NIOSH) and the Environmental Protection Agency (EPA).",
+            "identifier": "ETA-5-012:018-515",
             "keyword": [
                 "ETA",
                 "agricuture",
@@ -15145,36 +15139,36 @@
                 "farmworker",
                 "survey"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/national-agricultural-workers-survey/data",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-14T00:00:00Z",
             "programCode": [
                 "012:018"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Unemployment Insurance Claims and Payment Activities (ETA-5159)",
-            "description": "Historical series of the State UI Claims and Payment Activities Reports (ETA-5159) including monthly summaries of UI claims and benefit payment activities under state unemployment compensation programs.",
-            "modified": "2024-03-29T16:39:01.369Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-468",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_5159",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "National Agricultural Workers Survey (Restricted Use)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
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
+            "description": "Historical series of the State UI Claims and Payment Activities Reports (ETA-5159) including monthly summaries of UI claims and benefit payment activities under state unemployment compensation programs.",
+            "identifier": "ETA-5-012:013-468",
             "keyword": [
                 "ETA",
                 "benefits",
@@ -15185,141 +15179,141 @@
                 "weeks claimed",
                 "weeks paid"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_5159",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:39:01.369Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Income Expense Analysis, Unemployment Compensation Fund, Benefit Payment Account (ETA-8413)",
-            "description": "Historical series of Income Expense Analysis, Unemployment Compensation Fund, Benefit Payment Account Reports (ETA-8413) which provide monthly analysis of daily transactions in state payment accounts from the books of the bank on which benefit checks or warrents are issued. This report includes information on bank charges, account balances, and bank compensation associated with the state benefit payment accounts.",
-            "modified": "2024-03-29T16:26:34.810Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-475",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_8413",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Unemployment Insurance Claims and Payment Activities (ETA-5159)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
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
+            "description": "Historical series of Income Expense Analysis, Unemployment Compensation Fund, Benefit Payment Account Reports (ETA-8413) which provide monthly analysis of daily transactions in state payment accounts from the books of the bank on which benefit checks or warrents are issued. This report includes information on bank charges, account balances, and bank compensation associated with the state benefit payment accounts.",
+            "identifier": "ETA-5-012:013-475",
             "keyword": [
                 "ETA",
                 "benefit payment account",
                 "expense analysis",
                 "income analysis"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_8413",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:26:34.810Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Unemployment Insurance Overpayment Detection and Recovery Activities (ETA-227)",
-            "description": "Historical series of Overpayment Detection and Recovery Activities Reports (ETA-227) which provide information on benefit overpayments and overpayment recoveries of intrastate and interstate claims under the regular state unemployment insurance (UI) program, and under Federal UI programs including the Unemployment Compensation for Federal Employees (UCFE) and Unemployment Compensation for Ex- Servicemembers (UCX) programs. Additional datasets are also available for certain temporary Federal programs.",
-            "modified": "2024-03-29T16:23:43.682Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-478",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_227",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Income Expense Analysis, Unemployment Compensation Fund, Benefit Payment Account (ETA-8413)"
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
+            "description": "Historical series of Overpayment Detection and Recovery Activities Reports (ETA-227) which provide information on benefit overpayments and overpayment recoveries of intrastate and interstate claims under the regular state unemployment insurance (UI) program, and under Federal UI programs including the Unemployment Compensation for Federal Employees (UCFE) and Unemployment Compensation for Ex- Servicemembers (UCX) programs. Additional datasets are also available for certain temporary Federal programs.",
+            "identifier": "ETA-5-012:013-478",
             "keyword": [
                 "ETA",
                 "overpayments",
                 "recovery"
             ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_227",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Historical Unemployment Insurance Seasonally Adjusted and Unadjusted Weekly Claims Data",
-            "description": "Historical archive of Unemployment Insurance (UI) Weekly Claims data reflecting regular UI claims data as published in the UI Weekly Claims news release. Revisions to the national series are included per standard weekly and annual revision policies. Data goes back to 1967.",
-            "modified": "2022-12-21T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-463",
-            "landingPage": "https://oui.doleta.gov/unemploy/claims_arch.asp",
-            "rights": "TRUE",
+            ],
+            "modified": "2024-03-29T16:23:43.682Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Unemployment Insurance Overpayment Detection and Recovery Activities (ETA-227)"
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
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "description": "Historical archive of Unemployment Insurance (UI) Weekly Claims data reflecting regular UI claims data as published in the UI Weekly Claims news release. Revisions to the national series are included per standard weekly and annual revision policies. Data goes back to 1967.",
+            "identifier": "ETA-5-012:013-463",
             "keyword": [
                 "ETA",
                 "seasonally adjusted claims",
                 "weekly claims"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://oui.doleta.gov/unemploy/claims_arch.asp",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-12-21T00:00:00Z",
             "programCode": [
                 "012:013"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Unemployment Insurance Nonmonetary Determination Activity Data (ETA-207)",
-            "description": "Historical series of the State Unemployment Insurance (UI) Nonmonetary Determination Activity Reports (ETA-207) including information on the volume and nature of nonmonetary determinations and denials under state, Unemployment Compensation for Federal Employees (UCFE), and Unemployment Compensation for Ex- Servicemembers (UCX) unemployment insurance programs.",
-            "modified": "2024-03-29T16:41:48.757Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-465",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_207",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Historical Unemployment Insurance Seasonally Adjusted and Unadjusted Weekly Claims Data"
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
+            "description": "Historical series of the State Unemployment Insurance (UI) Nonmonetary Determination Activity Reports (ETA-207) including information on the volume and nature of nonmonetary determinations and denials under state, Unemployment Compensation for Federal Employees (UCFE), and Unemployment Compensation for Ex- Servicemembers (UCX) unemployment insurance programs.",
+            "identifier": "ETA-5-012:013-465",
             "keyword": [
                 "ETA",
                 "able and available",
@@ -15332,36 +15326,36 @@
                 "remands",
                 "voluntary quit"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_207",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:41:48.757Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Unemployment Insurance Benefit Appeals Data (ETA-5130)",
-            "description": "Historical series of the State Unemployment Insurance (UI) Benefit Appeals Reports (ETA-5130) including information on appeals case workloads by state under the regular UI, Unemployment Compensation for Federal Employees (UCFE), and Unemployment Compensation for Ex-Servicemembers (UCX) programs.",
-            "modified": "2024-03-29T16:39:49.757Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-467",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_5130",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Unemployment Insurance Nonmonetary Determination Activity Data (ETA-207)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
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
+            "description": "Historical series of the State Unemployment Insurance (UI) Benefit Appeals Reports (ETA-5130) including information on appeals case workloads by state under the regular UI, Unemployment Compensation for Federal Employees (UCFE), and Unemployment Compensation for Ex-Servicemembers (UCX) programs.",
+            "identifier": "ETA-5-012:013-467",
             "keyword": [
                 "ETA",
                 "able and available",
@@ -15374,105 +15368,105 @@
                 "remands",
                 "voluntary quit"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_5130",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:39:49.757Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Young Parents Demonstration Evaluation",
-            "description": "Under the Young Parents Demonstration (YPD), a federal initiative to test the effectiveness of providing enhanced services to young parents and expectant parents ages 16 to 24 and determine whether such services improved their educational and employment outcomes, ETA awarded 17 grants in three rounds between June 2009 (13 Rounds I/II grantees) and June 2011 (4 Rounds III grantess). The grants ended in December 2012 and December 2015, respectively. As part of the YPD, grantees were required to implement a differential experimental research design whereby treatment group members received an additional level of service above and beyond the base level of services provided to the control group. The treatment interventions varied across grantees, with some providing mentoring services and others providing guided employment, education, training and related supports. More than 3,700 young parents and expectant parents were randomly assigned to treatment and control groups.",
-            "modified": "2023-03-14T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:018-512",
-            "describedBy": "https://www.dol.gov/agencies/eta/research/young-parents-demonstration",
-            "landingPage": "https://www.dol.gov/agencies/eta/research/young-parents-demonstration",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Unemployment Insurance Benefit Appeals Data (ETA-5130)"
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
+            "describedBy": "https://www.dol.gov/agencies/eta/research/young-parents-demonstration",
+            "description": "Under the Young Parents Demonstration (YPD), a federal initiative to test the effectiveness of providing enhanced services to young parents and expectant parents ages 16 to 24 and determine whether such services improved their educational and employment outcomes, ETA awarded 17 grants in three rounds between June 2009 (13 Rounds I/II grantees) and June 2011 (4 Rounds III grantess). The grants ended in December 2012 and December 2015, respectively. As part of the YPD, grantees were required to implement a differential experimental research design whereby treatment group members received an additional level of service above and beyond the base level of services provided to the control group. The treatment interventions varied across grantees, with some providing mentoring services and others providing guided employment, education, training and related supports. More than 3,700 young parents and expectant parents were randomly assigned to treatment and control groups.",
+            "identifier": "ETA-5-012:018-512",
             "keyword": [
                 "ETA",
                 "evaluation",
                 "young parents"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/research/young-parents-demonstration",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-14T00:00:00Z",
             "programCode": [
                 "012:018"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Nonmonetary Determination Quality Data Collection Instrument (ETA-9056)",
-            "description": "Historical series of Nonmonetary Determination Quality Data Collection Instrument reports (ETA-9056) in which states provide quarterly information on the quality of nonmonetary determinations that state agencies issue to claimants and employers in the report period.",
-            "modified": "2024-03-29T16:05:05.628Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-492",
-            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Young Parents Demonstration Evaluation"
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
+            "description": "Historical series of Nonmonetary Determination Quality Data Collection Instrument reports (ETA-9056) in which states provide quarterly information on the quality of nonmonetary determinations that state agencies issue to claimants and employers in the report period.",
+            "identifier": "ETA-5-012:013-492",
             "keyword": [
                 "ETA",
                 "nonmonetary determinations",
                 "quality"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:05:05.628Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "First Payments Time Lapse (ETA-9050)",
-            "description": "Historical series of Time Lapse of First Payments reports (ETA-9050) in which states provide monthly information on first payment time lapse. This data concerns the time it takes states to pay benefits to claimants for the first compensable week of unemployment.",
-            "modified": "2024-03-29T16:12:37.548Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-487",
-            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9050",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Nonmonetary Determination Quality Data Collection Instrument (ETA-9056)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
+            "description": "Historical series of Time Lapse of First Payments reports (ETA-9050) in which states provide monthly information on first payment time lapse. This data concerns the time it takes states to pay benefits to claimants for the first compensable week of unemployment.",
+            "identifier": "ETA-5-012:013-487",
             "keyword": [
                 "ETA",
                 "first payment",
@@ -15480,72 +15474,72 @@
                 "performance",
                 "time lapse"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9050",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:12:37.548Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Advance Weekly Initial and Continued Claims (ETA-538)",
-            "description": "Historical series of Advance Weekly Initial and Continued Claims reports (ETA 538). This information is provided by states on a weekly basis and includes the advance weekly claims data as reported by states in the ETA 538 report. These data are not revised after the initial submission and subsequent publication in the UI weekly claims news release.",
-            "modified": "2024-03-29T15:53:10.328Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:013-462",
-            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "First Payments Time Lapse (ETA-9050)"
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
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
+            "description": "Historical series of Advance Weekly Initial and Continued Claims reports (ETA 538). This information is provided by states on a weekly basis and includes the advance weekly claims data as reported by states in the ETA 538 report. These data are not revised after the initial submission and subsequent publication in the UI weekly claims news release.",
+            "identifier": "ETA-5-012:013-462",
             "keyword": [
                 "ETA",
                 "initial claims",
                 "ui",
                 "unemployment insurance"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T15:53:10.328Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Department of Labor (DOL) Grant Award Data",
-            "description": "This dataset contains information on grants awarded by the Department of Labor such as: the grant number, the name of the organization receiving funds, the dollar amount of the award, the period of performance, the Catalog of Federal Domestic Assistance (CFDA) number and the accounting codes for the funds awarded.",
-            "modified": "2024-12-26T19:00:52.805Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:018-524",
-            "describedBy": "https://www.usaspending.gov/data-dictionary",
-            "describedByType": "text/html",
-            "landingPage": "https://www.usaspending.gov/",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "Advance Weekly Initial and Continued Claims (ETA-538)"
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
                 "fn": "Subri Raman",
                 "hasEmail": "mailto:raman.subri@dol.gov"
             },
+            "describedBy": "https://www.usaspending.gov/data-dictionary",
+            "describedByType": "text/html",
+            "description": "This dataset contains information on grants awarded by the Department of Labor such as: the grant number, the name of the organization receiving funds, the dollar amount of the award, the period of performance, the Catalog of Federal Domestic Assistance (CFDA) number and the accounting codes for the funds awarded.",
+            "identifier": "ETA-5-012:018-524",
             "keyword": [
                 "ETA",
                 "award data",
@@ -15555,39 +15549,39 @@
                 "grants",
                 "grants data"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.usaspending.gov/",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-26T19:00:52.805Z",
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
+            "title": "Department of Labor (DOL) Grant Award Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Workforce Development Boards and Areas Finder data",
-            "description": "List  of Workforce Development Boards including name, address, contact information, as well as contact names and geographic location coding.",
-            "modified": "2023-03-14T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:018-436",
-            "describedBy": "https://www.careeronestop.org/TridionMultimedia/tcm24-44484_StateWorkforceDevelopmentBoards_DataDownloadReadme.docx",
-            "landingPage": "https://www.careeronestop.org/Developers/Data/local-workforce-development-boards.aspx",
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
+            "describedBy": "https://www.careeronestop.org/TridionMultimedia/tcm24-44484_StateWorkforceDevelopmentBoards_DataDownloadReadme.docx",
+            "description": "List  of Workforce Development Boards including name, address, contact information, as well as contact names and geographic location coding.",
+            "identifier": "ETA-5-012:018-436",
             "keyword": [
                 "ETA",
                 "boards",
@@ -15595,39 +15589,39 @@
                 "state boards",
                 "wdb"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.careeronestop.org/Developers/Data/local-workforce-development-boards.aspx",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-14T00:00:00Z",
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
+            "title": "Workforce Development Boards and Areas Finder data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Unemployment Insurance Employer Experience Rating Distributions (ETA-204)",
-            "description": "Historical series of Expereince Rating Reports (ETA-204) which include the distributions used by states to assign state Unemployment Insurance (UI) contribution rates. The reports include employer counts and wage data broken out by UI experience/average tax rates.",
-            "modified": "2024-03-29T16:36:42.418Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:013-470",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_204",
-            "rights": "TRUE",
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
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
+            "description": "Historical series of Expereince Rating Reports (ETA-204) which include the distributions used by states to assign state Unemployment Insurance (UI) contribution rates. The reports include employer counts and wage data broken out by UI experience/average tax rates.",
+            "identifier": "ETA-5-012:013-470",
             "keyword": [
                 "ETA",
                 "experience rating",
@@ -15637,36 +15631,36 @@
                 "total benefits",
                 "total wages"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_204",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:36:42.418Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Unemployment Insurance Benefit Payment Account Transactions (ETA-8401)",
-            "description": "Historical series of Monthly Analsysis of Benefit Payment Account Reports (ETA-8401) in which states provide monthly summaries of transactions in the state benefit payment accounts from which Unemployment Insurance (UI) benefits are paid.",
-            "modified": "2024-03-29T16:29:01.403Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-473",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_8401",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Unemployment Insurance Employer Experience Rating Distributions (ETA-204)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
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
+            "description": "Historical series of Monthly Analsysis of Benefit Payment Account Reports (ETA-8401) in which states provide monthly summaries of transactions in the state benefit payment accounts from which Unemployment Insurance (UI) benefits are paid.",
+            "identifier": "ETA-5-012:013-473",
             "keyword": [
                 "ETA",
                 "benefit payments",
@@ -15674,107 +15668,108 @@
                 "deposits",
                 "ui trust fund"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_8401",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:29:01.403Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Historical Series of Unemployment Insurance Alien Claims Activities (ETA-9016)",
-            "description": "Historical series of Alien Claims Activities reports (ETA-9016) in which states provide quarterly information on claimants' legal status, corresponding state workloads related to the verification process and the magnitude of the impact of alien claims issues on unemployment insurance (UI) eligibility as required by Immigration Reform and Control Act of 1986.",
-            "modified": "2024-03-29T16:20:01.623Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-481",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9016",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "State Unemployment Insurance Benefit Payment Account Transactions (ETA-8401)"
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
+            "description": "Historical series of Alien Claims Activities reports (ETA-9016) in which states provide quarterly information on claimants' legal status, corresponding state workloads related to the verification process and the magnitude of the impact of alien claims issues on unemployment insurance (UI) eligibility as required by Immigration Reform and Control Act of 1986.",
+            "identifier": "ETA-5-012:013-481",
             "keyword": [
                 "ETA",
                 "alien claims",
                 "immigration",
                 "initial claims"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9016",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:20:01.623Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Continued Weeks Compensated Time Lapse Counts (ETA-9051)",
-            "description": "Historical series of Time Lapse Counts for Continued Weeks Compensated reports (ETA-9051) in states provide monthly information on continued weeks compensated time lapse. This report concerns the time it takes states to pay benefits to claimants for compensable weeks of unemployment other than the \"first payment.\"",
-            "modified": "2024-03-29T16:11:32.997Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-488",
-            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9051",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Historical Series of Unemployment Insurance Alien Claims Activities (ETA-9016)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
+            "description": "Historical series of Time Lapse Counts for Continued Weeks Compensated reports (ETA-9051) in states provide monthly information on continued weeks compensated time lapse. This report concerns the time it takes states to pay benefits to claimants for compensable weeks of unemployment other than the \"first payment.\"",
+            "identifier": "ETA-5-012:013-488",
             "keyword": [
                 "ETA",
                 "continued weeks",
                 "performance",
                 "time lapse"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9051",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:11:32.997Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Unemployment Insurance Data Validation (DV) Data",
-            "description": "This dataset includes the historical series of State Unemployment Insurance (UI) Data Validation program results. The purpose of the Data Validation (DV) program is to verify the accuracy of the Unemployment Insurance Required Reports (UIRR) system data. States report UI data to the U.S. Department of Labor (DOL) on a monthly and quarterly basis under the UIRR system. The UIRR data are used for gathering economic statistics, allocating UI administrative funding, measuring state performance, and accounting for fund utilization. Therefore, it is important that states report UIRR data accurately and uniformly. States use the DV software provided by DOL to conduct the validation and submit results.",
-            "modified": "2023-01-03T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-494",
-            "describedBy": "https://wdr.doleta.gov/directives/attach/et_handbook_412.pdf",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Continued Weeks Compensated Time Lapse Counts (ETA-9051)"
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
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://wdr.doleta.gov/directives/attach/et_handbook_412.pdf",
+            "description": "This dataset includes the historical series of State Unemployment Insurance (UI) Data Validation program results. The purpose of the Data Validation (DV) program is to verify the accuracy of the Unemployment Insurance Required Reports (UIRR) system data. States report UI data to the U.S. Department of Labor (DOL) on a monthly and quarterly basis under the UIRR system. The UIRR data are used for gathering economic statistics, allocating UI administrative funding, measuring state performance, and accounting for fund utilization. Therefore, it is important that states report UIRR data accurately and uniformly. States use the DV software provided by DOL to conduct the validation and submit results.",
+            "identifier": "ETA-5-012:013-494",
             "keyword": [
                 "ETA",
                 "data quality",
@@ -15783,73 +15778,71 @@
                 "report validation",
                 "reporting quality"
             ],
-            "bureauCode": [
-                "012:05"
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
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Historical Series of Expenditures and Financial Adjustments of Federal Funds for Unemployment Compensation for Federal Employees and Ex-Servicemembers (ETA-191)",
-            "description": "Historical series of the quarterly Statements of Expenditures and Financial Adjustments of Federal Funds for Unemployment Compensation for Federal Employees and Ex-Servicemembers report (ETA-191) in which states submit data on state Federal Employees Compensation Act (FECA) activities and summaries by Federal and military agencies used for reimbursement of FECA funds.",
-            "modified": "2024-03-29T16:38:16.552Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-469",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_191",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "State Unemployment Insurance Data Validation (DV) Data"
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
+            "description": "Historical series of the quarterly Statements of Expenditures and Financial Adjustments of Federal Funds for Unemployment Compensation for Federal Employees and Ex-Servicemembers report (ETA-191) in which states submit data on state Federal Employees Compensation Act (FECA) activities and summaries by Federal and military agencies used for reimbursement of FECA funds.",
+            "identifier": "ETA-5-012:013-469",
             "keyword": [
                 "ETA",
                 "federal funds",
                 "ucfe",
                 "ucfx"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_191",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:38:16.552Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Income Expense Analysis, Unemployment Compensation Fund, Clearing Account (ETA-8415)",
-            "description": "Historical series of Income Expense Analysis, Unemployment Compensation Fund, Clearing Account Reports (ETA-8414) which provide monthly analysis of daily transactions in state clearing accounts from the books of the bank in which employer contributions and payments are deposited and transferred to the US Treasury. This report includes information on bank charges, account balances, and bank compensation associated with the state clearing accounts.",
-            "modified": "2024-09-27T15:02:04.346Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-476",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "describedByType": "application/pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_8414",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Historical Series of Expenditures and Financial Adjustments of Federal Funds for Unemployment Compensation for Federal Employees and Ex-Servicemembers (ETA-191)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
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
+            "describedByType": "application/pdf",
+            "description": "Historical series of Income Expense Analysis, Unemployment Compensation Fund, Clearing Account Reports (ETA-8414) which provide monthly analysis of daily transactions in state clearing accounts from the books of the bank in which employer contributions and payments are deposited and transferred to the US Treasury. This report includes information on bank charges, account balances, and bank compensation associated with the state clearing accounts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15857,42 +15850,43 @@
                     "title": "Income-Expense Analysis, UC Fund, Clearing Account"
                 }
             ],
+            "identifier": "ETA-5-012:013-476",
             "keyword": [
                 "ETA",
                 "expense analysis",
                 "income analysis",
                 "uc fund clearing account"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_8414",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-27T15:02:04.346Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Historical Series of Disaster Unemployment Assistance Activities (ETA-902)",
-            "description": "Historical series of Disaster Unemployment Assistance Activities reports (ETA-902) in which states provide monthly data on Disaster Unemployment Assistance activities when there is a disaster declared by the President.",
-            "modified": "2024-03-29T16:21:08.358Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-480",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_902",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "true",
+            "title": "Income Expense Analysis, Unemployment Compensation Fund, Clearing Account (ETA-8415)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
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
+            "description": "Historical series of Disaster Unemployment Assistance Activities reports (ETA-902) in which states provide monthly data on Disaster Unemployment Assistance activities when there is a disaster declared by the President.",
+            "identifier": "ETA-5-012:013-480",
             "keyword": [
                 "ETA",
                 "disaster",
@@ -15900,105 +15894,105 @@
                 "dua",
                 "fema"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_902",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:21:08.358Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Nonmonetary Determination Time Lapse Detection (ETA-9052)",
-            "description": "Historical series of Nonmonetary Determination Time Lapse Detection reports (ETA-9052) in which states provide monthly information on the time it takes to issue nonmonetary determinations from the date the issues are first detected by the agency.",
-            "modified": "2024-03-29T16:09:13.875Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-489",
-            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9052",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Historical Series of Disaster Unemployment Assistance Activities (ETA-902)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
+            "description": "Historical series of Nonmonetary Determination Time Lapse Detection reports (ETA-9052) in which states provide monthly information on the time it takes to issue nonmonetary determinations from the date the issues are first detected by the agency.",
+            "identifier": "ETA-5-012:013-489",
             "keyword": [
                 "ETA",
                 "nonmonetary determinations",
                 "time lapse"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9052",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:09:13.875Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Reemployment Services and Eligibility Assessment Workloads (ETA-9128)",
-            "description": "Historical series of Reemployment Services and Eligibility Assessment Workload reports (ETA-9128) in which states provide quarterly information on the Reemployment Services and Eligibility Assessment (RESEA) activities of claimants selected to participate in the RESEA program.  The data in this dataset is used for evaluation and monitoring of the RESEA initiative.",
-            "modified": "2024-03-29T16:16:37.592Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-484",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9128",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Nonmonetary Determination Time Lapse Detection (ETA-9052)"
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
+            "description": "Historical series of Reemployment Services and Eligibility Assessment Workload reports (ETA-9128) in which states provide quarterly information on the Reemployment Services and Eligibility Assessment (RESEA) activities of claimants selected to participate in the RESEA program.  The data in this dataset is used for evaluation and monitoring of the RESEA initiative.",
+            "identifier": "ETA-5-012:013-484",
             "keyword": [
                 "ETA",
                 "reemployment services and eligibility assessment workload"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9128",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:16:37.592Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Office of Trade Adjustment Assistance (OTAA) Administrative Collection of States",
-            "description": "The TAA Adminstrative Collection of States (TAAACS) includes data on state implementation of the TAA Program across seven categories: state organization and staffing, determinations of eligibility and training, program integration, IT systems and reporting, staff training, outreach, job search and relocaton, and barriers.  Data is collected annually through OMB Control No. 1205-0540.",
-            "modified": "2024-07-11T15:26:05.421Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:011-509",
-            "describedBy": "https://www.dol.gov/agencies/eta/tradeact/data/administration",
-            "landingPage": "https://www.dol.gov/agencies/eta/tradeact/data/administration",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Reemployment Services and Eligibility Assessment Workloads (ETA-9128)"
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
                 "fn": "Susan Manikowski",
                 "hasEmail": "mailto:manikowski.susan@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/tradeact/data/administration",
+            "description": "The TAA Adminstrative Collection of States (TAAACS) includes data on state implementation of the TAA Program across seven categories: state organization and staffing, determinations of eligibility and training, program integration, IT systems and reporting, staff training, outreach, job search and relocaton, and barriers.  Data is collected annually through OMB Control No. 1205-0540.",
+            "identifier": "ETA-5-012:011-509",
             "keyword": [
                 "ETA",
                 "otaa",
@@ -16008,107 +16002,107 @@
                 "taa",
                 "trade"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/tradeact/data/administration",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-07-11T15:26:05.421Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Government Performance & Results Act (GPRA) Results - Unemployment Insurance",
-            "description": "This dataset is contains the results of the annual Government Performance & Results Act (GPRA) which was designed to improve program management throughout the Federal government and became effective in 1993. Under this Act, agencies are required to develop a five-year strategic plan outlining its mission, long-term goals for the agency's major functions, performance measures, and reporting results. These results present GPRA performance results for the Unemployment Insurance Program.",
-            "modified": "2023-09-26T17:14:46.967Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-499",
-            "landingPage": "https://oui.doleta.gov/unemploy/gpra.asp",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "Office of Trade Adjustment Assistance (OTAA) Administrative Collection of States"
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
+            "description": "This dataset is contains the results of the annual Government Performance & Results Act (GPRA) which was designed to improve program management throughout the Federal government and became effective in 1993. Under this Act, agencies are required to develop a five-year strategic plan outlining its mission, long-term goals for the agency's major functions, performance measures, and reporting results. These results present GPRA performance results for the Unemployment Insurance Program.",
+            "identifier": "ETA-5-012:013-499",
             "keyword": [
                 "ETA",
                 "gpra",
                 "performance measures",
                 "state performance rankings"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/gpra.asp",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-09-26T17:14:46.967Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "YouthBuild Quarterly Performance Report data (QPR)",
-            "description": "The YouthBuild QPR collects aggregate data on a quarterly, annual, and program-to-date basis on number of participants, characteristics of participants, and interim and long-term performance outcomes.",
-            "modified": "2023-03-07T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:007-438",
-            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Government Performance & Results Act (GPRA) Results - Unemployment Insurance"
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
                 "fn": "Stephanie Pena",
                 "hasEmail": "mailto:pena.stephanie.l@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "description": "The YouthBuild QPR collects aggregate data on a quarterly, annual, and program-to-date basis on number of participants, characteristics of participants, and interim and long-term performance outcomes.",
+            "identifier": "ETA-5-012:007-438",
             "keyword": [
                 "ETA",
                 "youth employment and training",
                 "youthbuild"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-07T00:00:00Z",
             "programCode": [
                 "012:007"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Reentry Employment Opportunities (REO)  Quarterly Performance Report data(QPR)",
-            "description": "The Reentry Employment Opportunities (REO) Adult QPR report collects aggregate data on number of participants, services provided, and performance outcomes. There is no individual data in the data set, only summary level quarterly data by individual grantee.",
-            "modified": "2024-12-26T19:32:52.258Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:008-441",
-            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "describedByType": "text/html",
-            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "YouthBuild Quarterly Performance Report data (QPR)"
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
+            "describedByType": "text/html",
+            "description": "The Reentry Employment Opportunities (REO) Adult QPR report collects aggregate data on number of participants, services provided, and performance outcomes. There is no individual data in the data set, only summary level quarterly data by individual grantee.",
+            "identifier": "ETA-5-012:008-441",
             "keyword": [
                 "Adult",
                 "ETA",
@@ -16119,176 +16113,176 @@
                 "reentry",
                 "youth"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-26T19:32:52.258Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Historical Series of Profiling and Reemployment Services Outcomes (ETA-9049)",
-            "description": "Historical series of Profiling and Reemployment Services Outcome reports (ETA-9049) in which states provide information on the employment outcomes of claimants who were identified as likely to exhaust their UI benefits through the Worker Profiling and Reemployment Services (WPRS) program. The population for this report is the claimants who were selected for referral to reemployment services and referred to such services.",
-            "modified": "2024-03-29T16:18:01.043Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-483",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9049",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "Reentry Employment Opportunities (REO)  Quarterly Performance Report data(QPR)"
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
+            "description": "Historical series of Profiling and Reemployment Services Outcome reports (ETA-9049) in which states provide information on the employment outcomes of claimants who were identified as likely to exhaust their UI benefits through the Worker Profiling and Reemployment Services (WPRS) program. The population for this report is the claimants who were selected for referral to reemployment services and referred to such services.",
+            "identifier": "ETA-5-012:013-483",
             "keyword": [
                 "ETA",
                 "employment",
                 "reemployment",
                 "unemployment insurance"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9049",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:18:01.043Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Reemployment Services and Eligibility Assessment Outcomes (ETA-9129)",
-            "description": "Historical series of Reemployment Services and Eligibility Assessment (RESEA) Outcomes reports (ETA-9129) in which states provide quarterly information on the unemployment insurance (UI) and reemployment outcomes of claimants who are selected for RESEA activities.",
-            "modified": "2024-03-29T16:15:20.742Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-485",
-            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9129",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Historical Series of Profiling and Reemployment Services Outcomes (ETA-9049)"
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
+            "description": "Historical series of Reemployment Services and Eligibility Assessment (RESEA) Outcomes reports (ETA-9129) in which states provide quarterly information on the unemployment insurance (UI) and reemployment outcomes of claimants who are selected for RESEA activities.",
+            "identifier": "ETA-5-012:013-485",
             "keyword": [
                 "ETA",
                 "reemployment services and eligibility assessment outcome"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9129",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:15:20.742Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Appeals Case Aging (ETA-9055)",
-            "description": "Historical series of Appeals Case Aging reports (ETA-9055) in which states provide monthly information on the inventory of lower authority and higher authority single claimant appeals cases that have been filed but not decided. Appeals case aging provides information about the number of days from the date an appeal was filed through the end of the month covered by the report. Also included are the average and median ages of the pending single claimant appeals cases.",
-            "modified": "2024-03-29T16:06:25.107Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-491",
-            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9055",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Reemployment Services and Eligibility Assessment Outcomes (ETA-9129)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
+            "description": "Historical series of Appeals Case Aging reports (ETA-9055) in which states provide monthly information on the inventory of lower authority and higher authority single claimant appeals cases that have been filed but not decided. Appeals case aging provides information about the number of days from the date an appeal was filed through the end of the month covered by the report. Also included are the average and median ages of the pending single claimant appeals cases.",
+            "identifier": "ETA-5-012:013-491",
             "keyword": [
                 "ETA",
                 "higher authority appeals",
                 "lower authority appeals",
                 "time lapse"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9055",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:06:25.107Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Lower Authority Appeals Quality Review State Evaluation Score Sheet (ETA-9057)",
-            "description": "Historical series of Lower Authority Appeals Quality Review State Evaluation Score Sheet reports (ETA-9057) provides quarterly information on the quality of state agencies' single and two party lower authority appeals hearings and decisions in the report period.",
-            "modified": "2024-03-29T16:02:38.949Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-493",
-            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Appeals Case Aging (ETA-9055)"
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
+            "description": "Historical series of Lower Authority Appeals Quality Review State Evaluation Score Sheet reports (ETA-9057) provides quarterly information on the quality of state agencies' single and two party lower authority appeals hearings and decisions in the report period.",
+            "identifier": "ETA-5-012:013-493",
             "keyword": [
                 "ETA",
                 "appeals",
                 "quality"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:02:38.949Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Pandemic Unemployment Assistance Activities (ETA-902P)",
-            "description": "Historical series of Pandemic Unemployment Assistance Activities reports (ETA-902P) is specific to the temporary Pandemic Unemployment Assistance (PUA) program enacted by Congress in response to the COVID-19 pandemic. This dataset contains information on PUA claims/workload and payment activities, PUA appeals activities, and PUA overpayment and recovery activities.",
-            "modified": "2024-03-29T15:57:46.074Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-503",
-            "describedBy": "https://wdr.doleta.gov/directives/attach/UIPL/UIPL_16-20_Attachment_6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_902P",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Lower Authority Appeals Quality Review State Evaluation Score Sheet (ETA-9057)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://wdr.doleta.gov/directives/attach/UIPL/UIPL_16-20_Attachment_6.pdf",
+            "description": "Historical series of Pandemic Unemployment Assistance Activities reports (ETA-902P) is specific to the temporary Pandemic Unemployment Assistance (PUA) program enacted by Congress in response to the COVID-19 pandemic. This dataset contains information on PUA claims/workload and payment activities, PUA appeals activities, and PUA overpayment and recovery activities.",
+            "identifier": "ETA-5-012:013-503",
             "keyword": [
                 "ETA",
                 "benefits",
@@ -16304,36 +16298,36 @@
                 "weeks claimed",
                 "weeks paid"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_902P",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T15:57:46.074Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Unemployment Trust Fund (UTF) Quarterly Webschedule",
-            "description": "Unemployment Trust Fund (UTF) Quarterly Webschedule is data detailing UTF balances due from all Federal Agencies. Agency Liability for Federal Employees' Unemployment Insurance Benefits (FEC AR).",
-            "modified": "2023-04-10T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:018-534",
-            "describedBy": "https://www.dol.gov/agencies/ocfo/publications",
-            "landingPage": "https://www.dol.gov/agencies/ocfo/publications",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Pandemic Unemployment Assistance Activities (ETA-902P)"
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
                 "fn": "Jessie Bergstresser",
                 "hasEmail": "mailto:bergstresser.jessie@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/ocfo/publications",
+            "description": "Unemployment Trust Fund (UTF) Quarterly Webschedule is data detailing UTF balances due from all Federal Agencies. Agency Liability for Federal Employees' Unemployment Insurance Benefits (FEC AR).",
+            "identifier": "ETA-5-012:018-534",
             "keyword": [
                 "ETA",
                 "fec",
@@ -16343,37 +16337,36 @@
                 "unemployment trust fund",
                 "utf"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/ocfo/publications",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-04-10T00:00:00Z",
             "programCode": [
                 "012:018"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Professional Associations data",
-            "description": "Dataset is a list of national professional and industry associations and includes information such as name, website URL, and related occupation and industry codes to industries and occupations. Data include the name of the association and a URL link for each association.\n\nCareerOneStop.org web  service available upon request.",
-            "modified": "2024-07-11T16:34:10.764Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:018-456",
-            "describedBy": "https://www.careeronestop.org/Developers/Data/professional-associations.aspx",
-            "describedByType": "text/html",
-            "landingPage": "https://www.careeronestop.org/Developers/Data/professional-associations.aspx",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Unemployment Trust Fund (UTF) Quarterly Webschedule"
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
                 "fn": "Steve Rietzke",
                 "hasEmail": "mailto:rietzke.steven@dol.gov"
             },
+            "describedBy": "https://www.careeronestop.org/Developers/Data/professional-associations.aspx",
+            "describedByType": "text/html",
+            "description": "Dataset is a list of national professional and industry associations and includes information such as name, website URL, and related occupation and industry codes to industries and occupations. Data include the name of the association and a URL link for each association.\n\nCareerOneStop.org web  service available upon request.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16381,42 +16374,43 @@
                     "title": "Professional Associations Data Downloads"
                 }
             ],
+            "identifier": "ETA-5-012:018-456",
             "keyword": [
                 "ETA",
                 "industry code",
                 "occupation code",
                 "occupational and industry codes"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.careeronestop.org/Developers/Data/professional-associations.aspx",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-07-11T16:34:10.764Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Archived historical versions of the Occupational Information Network (O*NET) database for research purposes",
-            "description": "Historical versions of the Occupational Information Network (O*NET) database starting with the prototype O*NET 98 db, and from O*NET 3.0 (8/2000) through O*NET 26.3 (May 2022).\n\nDownloadable files from www.ONETCenter.org",
-            "modified": "2023-05-23T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:018-437",
-            "describedBy": "https://www.onetcenter.org/db_releases.html",
-            "landingPage": "https://www.onetcenter.org/db_releases.html",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Professional Associations data"
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
+            "describedBy": "https://www.onetcenter.org/db_releases.html",
+            "description": "Historical versions of the Occupational Information Network (O*NET) database starting with the prototype O*NET 98 db, and from O*NET 3.0 (8/2000) through O*NET 26.3 (May 2022).\n\nDownloadable files from www.ONETCenter.org",
+            "identifier": "ETA-5-012:018-437",
             "keyword": [
                 "ETA",
                 "abilities",
@@ -16425,35 +16419,35 @@
                 "skills",
                 "tasks"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.onetcenter.org/db_releases.html",
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
-            "title": "Improper Payments Information Act Improper Payment Rates",
-            "description": "The unemployment insurance  (UI) Improper Payment Rate dataset is derived from the Benefit Accuracy Measurement (BAM) program. BAM is a statistical survey used to identify and support resolutions of deficiencies in the state\u2019s  (UI) system as well as to estimate state UI improper payments to be reported to DOL as required by the Improper Payments Information Act (IPIA) and the Elimination and Recovery Act (IPERA).",
-            "modified": "2023-01-03T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-496",
-            "landingPage": "https://www.dol.gov/general/maps/data",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Archived historical versions of the Occupational Information Network (O*NET) database for research purposes"
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
                 "fn": "Subri Raman",
                 "hasEmail": "mailto:raman.subri@dol.gov"
             },
+            "description": "The unemployment insurance  (UI) Improper Payment Rate dataset is derived from the Benefit Accuracy Measurement (BAM) program. BAM is a statistical survey used to identify and support resolutions of deficiencies in the state\u2019s  (UI) system as well as to estimate state UI improper payments to be reported to DOL as required by the Improper Payments Information Act (IPIA) and the Elimination and Recovery Act (IPERA).",
+            "identifier": "ETA-5-012:013-496",
             "keyword": [
                 "ETA",
                 "benefit accuracy measurement",
@@ -16462,71 +16456,71 @@
                 "payment accuracy",
                 "root causes"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/general/maps/data",
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
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Unemployment Insurance Performance Management Rankings",
-            "description": "This dataset includesstate performance rankings for the core measures and Secretary Standards. Results are ranked according to performance for all measures except Tax Quality. Any number of measures and quarters can be selected. All states, the District of Columbia, Puerto Rico and the Virgin Islands are included in the report output.",
-            "modified": "2023-01-03T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-498",
-            "describedBy": "https://oui.doleta.gov/unemploy/pdf/Core_Measures.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/uiagency.asp",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Improper Payments Information Act Improper Payment Rates"
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
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://oui.doleta.gov/unemploy/pdf/Core_Measures.pdf",
+            "description": "This dataset includesstate performance rankings for the core measures and Secretary Standards. Results are ranked according to performance for all measures except Tax Quality. Any number of measures and quarters can be selected. All states, the District of Columbia, Puerto Rico and the Virgin Islands are included in the report output.",
+            "identifier": "ETA-5-012:013-498",
             "keyword": [
                 "ETA",
                 "performance measures",
                 "state performance rankings"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://oui.doleta.gov/unemploy/uiagency.asp",
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
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Office of Trade Adjustment Assistance (OTAA) Trade Act Participant Report Data",
-            "description": "Individual participant records for TAA program FY 2009 to FY 2017. Only aggregate reports are publicly releasable.  This includes data collected through OMB Control No. 1205-0392 through FY 2017.",
-            "modified": "2024-07-11T15:23:22.022Z",
-            "accessLevel": "non-public",
-            "identifier": "ETA-5-012:011-506",
-            "describedBy": "https://www.dol.gov/agencies/eta/advisories/training-and-employment-guidance-letter-no-06-09-change-2",
-            "landingPage": "https://www.dol.gov/agencies/eta/tradeact/data/participants",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Unemployment Insurance Performance Management Rankings"
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
                 "fn": "Robert Hoekstra",
                 "hasEmail": "mailto:hoekstra.robert@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/advisories/training-and-employment-guidance-letter-no-06-09-change-2",
+            "description": "Individual participant records for TAA program FY 2009 to FY 2017. Only aggregate reports are publicly releasable.  This includes data collected through OMB Control No. 1205-0392 through FY 2017.",
+            "identifier": "ETA-5-012:011-506",
             "keyword": [
                 "ETA",
                 "otaa",
@@ -16534,70 +16528,70 @@
                 "taa",
                 "trade"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/tradeact/data/participants",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-07-11T15:23:22.022Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The WIA Adult and Dislocated Worker Programs Gold Standard Evaluation (Restricted Use File)",
-            "description": "The WIA Adult and Dislocated Worker Programs Gold Standard Evaluation assessed the effectiveness of the intensive and training services provided through the Adult and Dislocated Worker formula-funded programs.  The study used an experimental research design to ensure the study findings are representative of national WIA Adult and Dislocated Worker programs, with the following features: Twenty-eight randomly-selected local workforce investment areas (LWIAs) participated.  With few exceptions (e.g., veterans), all eligible adults and dislocated workers in the LWIAs were randomly assigned to one of three research groups defined by the WIA-funded services that they could receive: (1) all WIA services, including training, (2) core and intensive services but not training, and (3) core services but not intensive or training services. Random assignment took place just after customers were found eligible to receive WIA-funded intensive services.",
-            "modified": "2023-03-14T00:00:00Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012-001, 012-002-513",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "Office of Trade Adjustment Assistance (OTAA) Trade Act Participant Report Data"
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
+            "description": "The WIA Adult and Dislocated Worker Programs Gold Standard Evaluation assessed the effectiveness of the intensive and training services provided through the Adult and Dislocated Worker formula-funded programs.  The study used an experimental research design to ensure the study findings are representative of national WIA Adult and Dislocated Worker programs, with the following features: Twenty-eight randomly-selected local workforce investment areas (LWIAs) participated.  With few exceptions (e.g., veterans), all eligible adults and dislocated workers in the LWIAs were randomly assigned to one of three research groups defined by the WIA-funded services that they could receive: (1) all WIA services, including training, (2) core and intensive services but not training, and (3) core services but not intensive or training services. Random assignment took place just after customers were found eligible to receive WIA-funded intensive services.",
+            "identifier": "ETA-5-012-001, 012-002-513",
             "keyword": [
                 "ETA",
                 "adult and dislocated workers",
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
-            "title": "Public Workforce System Dataset (PWSD)",
-            "description": "The PWSD is a dataset that can be used to answer questions about various public workforce system programs and how these programs fit in with the overall public workforce system and the economy. It was designed primarily to be used as a tool to understand what has been occurring in the Wagner-Peyser program and contains data from quarter 1 of 1995 through quarter 4 of 2008. Also, it was designed to understand the relationship and flow of participants as they go through the public workforce system. The PWSD can be used to analyze these programs both individually and in combination. The PWSD contains economic variables, Unemployment Insurance System data, and data on programs funded by the Workforce Investment Act and Employment Service. Economic variables included are labor force, employment, unemployment, unemployment rate, and gross domestic product data.",
-            "modified": "2023-03-14T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:014-520",
-            "describedBy": "https://www.doleta.gov/reports/pwsd",
-            "landingPage": "https://www.doleta.gov/reports/pwsd",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "The WIA Adult and Dislocated Worker Programs Gold Standard Evaluation (Restricted Use File)"
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
+            "describedBy": "https://www.doleta.gov/reports/pwsd",
+            "description": "The PWSD is a dataset that can be used to answer questions about various public workforce system programs and how these programs fit in with the overall public workforce system and the economy. It was designed primarily to be used as a tool to understand what has been occurring in the Wagner-Peyser program and contains data from quarter 1 of 1995 through quarter 4 of 2008. Also, it was designed to understand the relationship and flow of participants as they go through the public workforce system. The PWSD can be used to analyze these programs both individually and in combination. The PWSD contains economic variables, Unemployment Insurance System data, and data on programs funded by the Workforce Investment Act and Employment Service. Economic variables included are labor force, employment, unemployment, unemployment rate, and gross domestic product data.",
+            "identifier": "ETA-5-012:014-520",
             "keyword": [
                 "ETA",
                 "employment",
@@ -16606,72 +16600,72 @@
                 "training programs",
                 "workforce system"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.doleta.gov/reports/pwsd",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-14T00:00:00Z",
             "programCode": [
                 "012:014"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Registered Apprenticeship Partners Information Database System (RAPIDS) Dataset",
-            "description": "Apprenticeship data for Office of Apprenticeship states and SAA states.  All states are available on the Data and Statistics page.",
-            "modified": "2024-07-11T16:22:22.134Z",
-            "accessLevel": "non-public",
-            "identifier": "ETA-5-012:017-537",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Public Workforce System Dataset (PWSD)"
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
                 "fn": "Alex Jordan",
                 "hasEmail": "mailto:jordan.alexander@dol.gov"
             },
+            "description": "Apprenticeship data for Office of Apprenticeship states and SAA states.  All states are available on the Data and Statistics page.",
+            "identifier": "ETA-5-012:017-537",
             "keyword": [
                 "ETA",
                 "apprenticeship",
                 "registered apprenticeship"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-07-11T16:22:22.134Z",
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
+            "title": "Registered Apprenticeship Partners Information Database System (RAPIDS) Dataset"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Eligible Training Provider Results Data (ETA-9171)",
-            "description": "States are required to report aggregate performance information related to Eligible Training Provider outcomes for WIOA Adult, WIOA Dislocated Worker and WIOA Youth individuals served by each approved program of study. Information includes completion, employment, program of study and others. States report this information annually through the WIOA ETP Performance Report (ETA-9171) as detailed in TEGL 03-18, Eligible Training Provider (ETP) Reporting Guidance under the Workforce Innovation and Opportunity Act (WIOA).  The results are posted on TrainingProviderResults.gov",
-            "modified": "2022-11-10T00:00:00Z",
             "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:016-521",
-            "describedBy": "https://www.dol.gov/agencies/eta/performance",
-            "landingPage": "https://www.trainingproviderresults.gov/#!/about",
-            "rights": "Not Available",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kellen Grode",
                 "hasEmail": "mailto:grode.kellen.m@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/performance",
+            "description": "States are required to report aggregate performance information related to Eligible Training Provider outcomes for WIOA Adult, WIOA Dislocated Worker and WIOA Youth individuals served by each approved program of study. Information includes completion, employment, program of study and others. States report this information annually through the WIOA ETP Performance Report (ETA-9171) as detailed in TEGL 03-18, Eligible Training Provider (ETP) Reporting Guidance under the Workforce Innovation and Opportunity Act (WIOA).  The results are posted on TrainingProviderResults.gov",
+            "identifier": "ETA-5-012:016-521",
             "keyword": [
                 "ETA",
                 "eligible training provider",
@@ -16680,104 +16674,105 @@
                 "wioa eligible training provider",
                 "wioa performance"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.trainingproviderresults.gov/#!/about",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-11-10T00:00:00Z",
             "programCode": [
                 "012:016"
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
+            "title": "Eligible Training Provider Results Data (ETA-9171)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Work Opportunity Tax Credit (WOTC) certification data",
-            "description": "State workforce agencies submit performance data on WOTC certification activities to ETA through the quarterly electronic submission of ETA Form 9058 via the web-based Tax Credit Reporting System (TCRS) of the Enterprise Business Services System (EBSS).  ETA 9058 - Report 1- WOTC Certification Workload and Characteristics of Certified Individuals Form, provides state workforce agencies with a standardized e-reporting format to accurately report program activities and outcomes (e.g., certifications, denials, total workload, etc.).  Data is aggregated by State.",
-            "modified": "2023-01-01T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:018-447",
-            "landingPage": "https://www.dol.gov/agencies/eta/wotc/performance",
-            "rights": "TRUE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Employment and Training Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steve Rietzke",
                 "hasEmail": "mailto:rietzke.steven@dol.gov"
             },
+            "description": "State workforce agencies submit performance data on WOTC certification activities to ETA through the quarterly electronic submission of ETA Form 9058 via the web-based Tax Credit Reporting System (TCRS) of the Enterprise Business Services System (EBSS).  ETA 9058 - Report 1- WOTC Certification Workload and Characteristics of Certified Individuals Form, provides state workforce agencies with a standardized e-reporting format to accurately report program activities and outcomes (e.g., certifications, denials, total workload, etc.).  Data is aggregated by State.",
+            "identifier": "ETA-5-012:018-447",
             "keyword": [
                 "ETA",
                 "work opportunity tax credit",
                 "wotc"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/wotc/performance",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-01T00:00:00Z",
             "programCode": [
                 "012:018"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "(YouthBuild) Joint Quarterly Narrative Report data (QNR) (ETA -9179)",
-            "description": "YouthBuild Joint Quarterly Narrative Performance Report dataset is a collection of qualitative narratives on YouthBuild grantees.  ETA  collects qualitative information on grantee efforts, challenges, and outcomes (ETA-9179).  ETA-9179 allows grantees to provide a detailed account of all activities undertaken during the quarter, including in-depth information on accomplishments, promising approaches, progress toward performance outcomes, and upcoming grant activities.",
-            "modified": "2023-03-07T00:00:00Z",
-            "accessLevel": "non-public",
-            "identifier": "ETA-5-012:007-439",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Work Opportunity Tax Credit (WOTC) certification data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephanie Pena",
                 "hasEmail": "mailto:pena.stephanie.l@dol.gov"
             },
+            "description": "YouthBuild Joint Quarterly Narrative Performance Report dataset is a collection of qualitative narratives on YouthBuild grantees.  ETA  collects qualitative information on grantee efforts, challenges, and outcomes (ETA-9179).  ETA-9179 allows grantees to provide a detailed account of all activities undertaken during the quarter, including in-depth information on accomplishments, promising approaches, progress toward performance outcomes, and upcoming grant activities.",
+            "identifier": "ETA-5-012:007-439",
             "keyword": [
                 "ETA",
                 "youth employment and training",
                 "youthbuild"
             ],
-            "bureauCode": [
-                "012:05"
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-07T00:00:00Z",
             "programCode": [
                 "012:007"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Office of Trade Adjustment Assistance (OTAA) Efforts to Improve Outcomes",
-            "description": "State descriptions of their efforts to improve outcomes collected quarterly from FY 2009 to Present. Data collected through OMB Control No. 1205-0392.",
-            "modified": "2024-07-11T15:25:07.433Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:011-507",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "(YouthBuild) Joint Quarterly Narrative Report data (QNR) (ETA -9179)"
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
                 "fn": "Susan Manikowski",
                 "hasEmail": "mailto:manikowski.susan@dol.gov"
             },
+            "description": "State descriptions of their efforts to improve outcomes collected quarterly from FY 2009 to Present. Data collected through OMB Control No. 1205-0392.",
+            "identifier": "ETA-5-012:011-507",
             "keyword": [
                 "ETA",
                 "efforts to improve outcomes",
@@ -16785,69 +16780,68 @@
                 "taa",
                 "trade"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-07-11T15:25:07.433Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Enhanced Transitional Jobs Demonstration Evaluation (Restricted Use File)",
-            "description": "Transitional jobs programs offer temporary subsidized jobs that aim to teach participants basic work skills or help them get a foot in the door with an employer. They also help participants address personal issues that impede their ability to work and assist them in finding unsubsidized jobs when the transitional jobs end. Prior studies of transitional jobs programs have shown mixed results. ETJD tested seven employment programs serving unemployed noncustodial parents or individuals recently released from prison. Although all of the programs were based on the same basic model, each program incorporated different enhancements to address the shortcomings of previously evaluated programs, with the goal of improving outcomes across a range of domains, including employment, criminal justice involvement, child support, and economic and personal well-being. There was a total of 7,000 sample members, roughly 1,000 per site. Impact analyses were conducted at both the pooled and site levels.",
-            "modified": "2023-03-14T00:00:00Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:018-514",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "Office of Trade Adjustment Assistance (OTAA) Efforts to Improve Outcomes"
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
+            "description": "Transitional jobs programs offer temporary subsidized jobs that aim to teach participants basic work skills or help them get a foot in the door with an employer. They also help participants address personal issues that impede their ability to work and assist them in finding unsubsidized jobs when the transitional jobs end. Prior studies of transitional jobs programs have shown mixed results. ETJD tested seven employment programs serving unemployed noncustodial parents or individuals recently released from prison. Although all of the programs were based on the same basic model, each program incorporated different enhancements to address the shortcomings of previously evaluated programs, with the goal of improving outcomes across a range of domains, including employment, criminal justice involvement, child support, and economic and personal well-being. There was a total of 7,000 sample members, roughly 1,000 per site. Impact analyses were conducted at both the pooled and site levels.",
+            "identifier": "ETA-5-012:018-514",
             "keyword": [
                 "ETA",
                 "enhanced transitional jobs",
                 "evaluation"
             ],
-            "bureauCode": [
-                "012:05"
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-14T00:00:00Z",
             "programCode": [
                 "012:018"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Unemployment Insurance Contribution Operations (ETA-581)",
-            "description": "Historical series of Contribution Operations Reports (ETA-581) which provide quarterly information on state tax operations which are used to measure the effectiveness of the state Unemployment Insurance (UI) tax programs.",
-            "modified": "2024-03-29T16:35:46.724Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-471",
-            "describedBy": "https://oui.doleta.gov/dmstree/handbooks/402/402_4/4024c6/4024c6.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_581",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "Enhanced Transitional Jobs Demonstration Evaluation (Restricted Use File)"
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
+            "description": "Historical series of Contribution Operations Reports (ETA-581) which provide quarterly information on state tax operations which are used to measure the effectiveness of the state Unemployment Insurance (UI) tax programs.",
+            "identifier": "ETA-5-012:013-471",
             "keyword": [
                 "ETA",
                 "audit",
@@ -16856,36 +16850,36 @@
                 "employers",
                 "tax"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_581",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:35:46.724Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Unemployment Insurance Benefit Accuracy Measurement (BAM) Data",
-            "description": "This dataset includes the historical series of sample Unemployment Insurance (UI) data collected through the benefit accuracy measurement (BAM) program. BAM is a statistical survey used to identify and support resolutions of deficiencies in the state\u2019s (UI) system as well as to estimate state UI improper payments to be reported to DOL as required by the Improper Payments Information Act (IPIA) and the Elimination and Recovery Act (IPERA). BAM is also used to identify the root causes of improper payments and supports other analyses conducted by DOL to highlight improper payment prevention strategies and measure progress in meeting improper payment reduction targets.",
-            "modified": "2024-03-29T16:00:16.653Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-495",
-            "describedBy": "https://wdr.doleta.gov/directives/corr_doc.cfm?DOCN=2834",
-            "landingPage": "https://oui.doleta.gov/unemploy/bqc.asp",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "State Unemployment Insurance Contribution Operations (ETA-581)"
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
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://wdr.doleta.gov/directives/corr_doc.cfm?DOCN=2834",
+            "description": "This dataset includes the historical series of sample Unemployment Insurance (UI) data collected through the benefit accuracy measurement (BAM) program. BAM is a statistical survey used to identify and support resolutions of deficiencies in the state\u2019s (UI) system as well as to estimate state UI improper payments to be reported to DOL as required by the Improper Payments Information Act (IPIA) and the Elimination and Recovery Act (IPERA). BAM is also used to identify the root causes of improper payments and supports other analyses conducted by DOL to highlight improper payment prevention strategies and measure progress in meeting improper payment reduction targets.",
+            "identifier": "ETA-5-012:013-495",
             "keyword": [
                 "ETA",
                 "benefit accuracy measurement",
@@ -16894,36 +16888,36 @@
                 "payment accuracy",
                 "root causes"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/bqc.asp",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:00:16.653Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "H-2A Program Historical Data",
-            "description": "This dataset includes data that ETA's Office of Foreign Labor Certification (OFLC) collected from H-2A applications during previous fiscal years. It includes information on employers, geography, and job details for participants in the H-2A program. Historical H-2A public disclosure data is available on the OFLC website in the Performance Data section. Data is available as Excel files in aggregate form at  https://www.dol.gov/agencies/eta/foreign-labor/performance.",
-            "modified": "2023-05-15T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:015-525",
-            "describedBy": "https://www.dol.gov/agencies/eta/foreign-labor/performance",
-            "landingPage": "https://www.dol.gov/agencies/eta/foreign-labor/performance",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Unemployment Insurance Benefit Accuracy Measurement (BAM) Data"
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
                 "fn": "Rob Jordan",
                 "hasEmail": "mailto:jordan.rob@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/foreign-labor/performance",
+            "description": "This dataset includes data that ETA's Office of Foreign Labor Certification (OFLC) collected from H-2A applications during previous fiscal years. It includes information on employers, geography, and job details for participants in the H-2A program. Historical H-2A public disclosure data is available on the OFLC website in the Performance Data section. Data is available as Excel files in aggregate form at  https://www.dol.gov/agencies/eta/foreign-labor/performance.",
+            "identifier": "ETA-5-012:015-525",
             "keyword": [
                 "ETA",
                 "h-2a",
@@ -16933,39 +16927,39 @@
                 "h-2a participants",
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
+            "title": "H-2A Program Historical Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "H-2B Program Historical Data",
-            "description": "This dataset includes data that the Employment and Training Administration's Office of Foreign Labor Certification (OFLC) collected from H-2B applications during previous fiscal years. It includes information on employers, geography, and job details for participants in the H-2B program. Historical H-2B public disclosure data is available on the OFLC website in the Performance Data section. Data is available as  Excel files in aggregate form at https://www.dol.gov/agencies/eta/foreign-labor/performance.",
-            "modified": "2023-05-15T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:015-526",
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
+            "description": "This dataset includes data that the Employment and Training Administration's Office of Foreign Labor Certification (OFLC) collected from H-2B applications during previous fiscal years. It includes information on employers, geography, and job details for participants in the H-2B program. Historical H-2B public disclosure data is available on the OFLC website in the Performance Data section. Data is available as  Excel files in aggregate form at https://www.dol.gov/agencies/eta/foreign-labor/performance.",
+            "identifier": "ETA-5-012:015-526",
             "keyword": [
                 "ETA",
                 "h-2b",
@@ -16975,116 +16969,116 @@
                 "h-2b participants",
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
+            "title": "H-2B Program Historical Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Prevailing Wage Program Historical Data",
-            "description": "The historical Prevailing Wage public disclosure data available on the Office of Foreign Labor Certification (OFLC) web page in the Performance Data section.  This dataset includes data collected from Prevailing Wage applications during previous fiscal years. It includes information on employers, geography, job details, etc. for participants in the Prevailing Wage program. Historical Prevailing Wage public disclosure data is available on the OFLC website in the Performance Data section. Data is available as Excel files in aggregate form for previous fiscal years at https://www.dol.gov/agencies/eta/foreign-labor/performance.",
-            "modified": "2023-05-15T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:015-528",
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
+            "description": "The historical Prevailing Wage public disclosure data available on the Office of Foreign Labor Certification (OFLC) web page in the Performance Data section.  This dataset includes data collected from Prevailing Wage applications during previous fiscal years. It includes information on employers, geography, job details, etc. for participants in the Prevailing Wage program. Historical Prevailing Wage public disclosure data is available on the OFLC website in the Performance Data section. Data is available as Excel files in aggregate form for previous fiscal years at https://www.dol.gov/agencies/eta/foreign-labor/performance.",
+            "identifier": "ETA-5-012:015-528",
             "keyword": [
                 "ETA",
                 "oflc employers",
                 "oflc performance data",
                 "prevailing wage"
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
+            "title": "Prevailing Wage Program Historical Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Labor Condition Application for Nonimmigrant Workers (LCA)  Program Historical Data",
-            "description": "This dataset includes data that the Employment and Training Administration's Office of Foreign Labor Certification (OFLC) collected from Labor Condition Applications for Nonimmigrant Workers (LCAs) during previous fiscal years. It includes information on employers, geography, and job details for participants in the LCA program. Historical LCA public disclosure data is available on the OFLC website in the Performance Data section. Data is available as Excel files in aggregate form at  https://www.dol.gov/agencies/eta/foreign-labor/performance.",
-            "modified": "2023-05-15T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:015-529",
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
+            "description": "This dataset includes data that the Employment and Training Administration's Office of Foreign Labor Certification (OFLC) collected from Labor Condition Applications for Nonimmigrant Workers (LCAs) during previous fiscal years. It includes information on employers, geography, and job details for participants in the LCA program. Historical LCA public disclosure data is available on the OFLC website in the Performance Data section. Data is available as Excel files in aggregate form at  https://www.dol.gov/agencies/eta/foreign-labor/performance.",
+            "identifier": "ETA-5-012:015-529",
             "keyword": [
                 "ETA",
                 "lca applications",
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
+            "title": "Labor Condition Application for Nonimmigrant Workers (LCA)  Program Historical Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Permanent Employment Certification (PERM) Program Historical Data",
-            "description": "This dataset includes data that the Employment and Training Administration's Office of Foreign Labor Certification (OFLC) collected from Permanent Employment Certification (PERM) applications during previous fiscal years. It includes information on employers, geography, and job details for participants in the PERM program. Historical PERM public disclosure data is available on the OFLC website in the Performance Data section. Data is available as Excel files in aggregate form at https://www.dol.gov/agencies/eta/foreign-labor/performance.",
-            "modified": "2023-05-15T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:015-527",
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
+            "description": "This dataset includes data that the Employment and Training Administration's Office of Foreign Labor Certification (OFLC) collected from Permanent Employment Certification (PERM) applications during previous fiscal years. It includes information on employers, geography, and job details for participants in the PERM program. Historical PERM public disclosure data is available on the OFLC website in the Performance Data section. Data is available as Excel files in aggregate form at https://www.dol.gov/agencies/eta/foreign-labor/performance.",
+            "identifier": "ETA-5-012:015-527",
             "keyword": [
                 "ETA",
                 "oflc performance data",
@@ -17092,38 +17086,38 @@
                 "perm",
                 "perm employers"
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
+            "title": "Permanent Employment Certification (PERM) Program Historical Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "National Farmworkers Jobs Program (NFJP) Joint Quarterly Narrative Report (QNR) (ETA -9179)",
-            "description": "Joint Quarterly Narrative Performance Report (ETA-9179) is used to collect qualitative information on grantee efforts, challenges, and outcomes. The ETA-9179 allows grantees to provide a detailed account of all activities undertaken during the quarter including in-depth information on accomplishments, promising approaches, progress toward performance outcomes, and upcoming grant activities. This is largely a communication tool and does not contain quantitative data sets. This is unstructured and unorganized data.",
-            "modified": "2022-12-12T00:00:00Z",
             "accessLevel": "public",
-            "identifier": "ETA-5-012:006-446",
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
+            "description": "Joint Quarterly Narrative Performance Report (ETA-9179) is used to collect qualitative information on grantee efforts, challenges, and outcomes. The ETA-9179 allows grantees to provide a detailed account of all activities undertaken during the quarter including in-depth information on accomplishments, promising approaches, progress toward performance outcomes, and upcoming grant activities. This is largely a communication tool and does not contain quantitative data sets. This is unstructured and unorganized data.",
+            "identifier": "ETA-5-012:006-446",
             "keyword": [
                 "ETA",
                 "farmworker",
@@ -17131,72 +17125,72 @@
                 "msfw",
                 "nfjp"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-12-12T00:00:00Z",
             "programCode": [
                 "012:006"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "H-1B Skills Training Grant Programs' Quarterly Performance Report (QPR) Data",
-            "description": "The H-1B skills training grant programs are competitive grants that focus on specific interventions, populations, partnerships, or structures in job training. The H-1B grants Quarterly Performance Report (QPR) dataset contains aggregate data on the number of participants, services provided, and performance outcomes. There is no individual data in the dataset, only summary level quarterly data by  grantee.",
-            "modified": "2023-05-15T00:00:00Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:018-546",
-            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "National Farmworkers Jobs Program (NFJP) Joint Quarterly Narrative Report (QNR) (ETA -9179)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P6M",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jenn Smith",
                 "hasEmail": "mailto:smith.jenn@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "description": "The H-1B skills training grant programs are competitive grants that focus on specific interventions, populations, partnerships, or structures in job training. The H-1B grants Quarterly Performance Report (QPR) dataset contains aggregate data on the number of participants, services provided, and performance outcomes. There is no individual data in the dataset, only summary level quarterly data by  grantee.",
+            "identifier": "ETA-5-012:018-546",
             "keyword": [
                 "ETA",
                 "competitive grants",
                 "discretionary grants",
                 "h-1b employment and training"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-05-15T00:00:00Z",
             "programCode": [
                 "012:018"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Dislocated Workers Grants (NDWG) Joint Quarterly Performance Report (QPR) Data",
-            "description": "National Dislocated Workers Grants (NDWG) Joint Quarterly Performance Report data (QPR) collects aggregate data on number of participants, services provided, and performance outcomes. There is no individual data in the dataset, only summary level quarterly data by individual grantee.",
-            "modified": "2023-03-09T00:00:00Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:002-545",
-            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "H-1B Skills Training Grant Programs' Quarterly Performance Report (QPR) Data"
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
                 "fn": "Robert Kight",
                 "hasEmail": "mailto:kight.Robert@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "description": "National Dislocated Workers Grants (NDWG) Joint Quarterly Performance Report data (QPR) collects aggregate data on number of participants, services provided, and performance outcomes. There is no individual data in the dataset, only summary level quarterly data by individual grantee.",
+            "identifier": "ETA-5-012:002-545",
             "keyword": [
                 "ETA",
                 "dislocated worker program",
@@ -17204,36 +17198,36 @@
                 "national dislocated worker program",
                 "ndwg"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-09T00:00:00Z",
             "programCode": [
                 "012:002"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Mixed Earner Unemployment Compensation (ETA-902M)",
-            "description": "This dataset contains the historical series of Mixed Earner Unemployment Compensation (MEUC) reports (ETA-902M), which are specific to the MEUC program enacted by Congress in response to the COVID-19 pandemic. The MEUC program was enacted by the Continued Assistance Act signed into law on December 27, 2020. This dataset includes MEUC claims/workload and payment activities, MEUC appeals activities, and MEUC workload funding amounts.",
-            "modified": "2024-03-29T15:54:16.651Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-542",
-            "describedBy": "https://wdr.doleta.gov/directives/attach/UIPL/UIPL_15-20_Change_3_Attachment-3_acc.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_902M",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "National Dislocated Workers Grants (NDWG) Joint Quarterly Performance Report (QPR) Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://wdr.doleta.gov/directives/attach/UIPL/UIPL_15-20_Change_3_Attachment-3_acc.pdf",
+            "description": "This dataset contains the historical series of Mixed Earner Unemployment Compensation (MEUC) reports (ETA-902M), which are specific to the MEUC program enacted by Congress in response to the COVID-19 pandemic. The MEUC program was enacted by the Continued Assistance Act signed into law on December 27, 2020. This dataset includes MEUC claims/workload and payment activities, MEUC appeals activities, and MEUC workload funding amounts.",
+            "identifier": "ETA-5-012:013-542",
             "keyword": [
                 "ETA",
                 "appeals",
@@ -17248,43 +17242,43 @@
                 "mixed earner unemployment compensation",
                 "weeks paid"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_902M",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T15:54:16.651Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Adult - Indian and Native American Program (INAP) Grantee Performance Management System (GPMS)",
-            "description": "The Workforce Innovation Opportunity Act (WIOA) Section 166, Indian and Native American Adult Program, collects data from tribal grantees on a quarterly basis for a rolling 4-quarter and quarterly period. This dataset includes information specific to the WIOA Section 166 Comprehensive Services Program (CSP) for performance accountability purposes.  The aggregate quarterly program report (ETA-9173-DINAP) and participant individual record layout (PIRL - ETA-9172) include data on individual characteristics, types of services received, and WIOA performance outcomes attained as a result of participating in the program. Data is available in aggregate and modified public use files on ETA\u2019s website (doleta.gov/performance).",
-            "modified": "2024-12-26T19:13:16.971Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:005-543",
-            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Mixed Earner Unemployment Compensation (ETA-902M)"
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
                 "fn": "Nathaniel Coley",
                 "hasEmail": "mailto:coley.nathaniel.d@dol.gov"
             },
+            "description": "The Workforce Innovation Opportunity Act (WIOA) Section 166, Indian and Native American Adult Program, collects data from tribal grantees on a quarterly basis for a rolling 4-quarter and quarterly period. This dataset includes information specific to the WIOA Section 166 Comprehensive Services Program (CSP) for performance accountability purposes.  The aggregate quarterly program report (ETA-9173-DINAP) and participant individual record layout (PIRL - ETA-9172) include data on individual characteristics, types of services received, and WIOA performance outcomes attained as a result of participating in the program. Data is available in aggregate and modified public use files on ETA\u2019s website (doleta.gov/performance).",
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
+            "identifier": "ETA-5-012:005-543",
             "keyword": [
                 "ETA",
                 "dinap",
@@ -17292,108 +17286,108 @@
                 "indian native american program",
                 "native american"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-26T19:13:16.971Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "JobCorps Individual Performance Records",
-            "description": "Job Corps submits individual performance records to the Workforce Integrated Performance System (WIPS) site on a quarterly basis. This data is used for Job Corps performance reporting on the WIOA performance measures in the same manner as other programs. Each quarterly file includes data elements, as specified by the Participant Individual Record Layout (PIRL), for participants served, reportable individuals, and participants who have exited from the program. Each quarterly submission contains results for a rolling 14 calendar quarter period.",
-            "modified": "2023-09-07T19:46:52.665Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-012:05-012:009-596",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Adult - Indian and Native American Program (INAP) Grantee Performance Management System (GPMS)"
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
                 "fn": "Shao Zhang",
                 "hasEmail": "mailto:zhang.shao@dol.gov"
             },
+            "description": "Job Corps submits individual performance records to the Workforce Integrated Performance System (WIPS) site on a quarterly basis. This data is used for Job Corps performance reporting on the WIOA performance measures in the same manner as other programs. Each quarterly file includes data elements, as specified by the Participant Individual Record Layout (PIRL), for participants served, reportable individuals, and participants who have exited from the program. Each quarterly submission contains results for a rolling 14 calendar quarter period.",
+            "identifier": "ETA-012:05-012:009-596",
             "keyword": [
                 "ETA",
                 "particpant individual record layout",
                 "pirl",
                 "wioa jobcorps"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-09-07T19:46:52.665Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Outcome Measurement System - OMS",
-            "description": "The Outcome Measurement System (OMS) is Job Corps' primary tool for performance accountability, composed of various specific report cards that cover specific areas of operation. The OMS report cards measure and account for performance across Job Corps' outreach and admission, center operation, and career transition services areas. The performance measures are primarily derived from the program\u2019s authorizing legislation, the Workforce Innovation and Opportunity Act (WIOA), and U.S. Department of Labor (DOL) priorities, with goals and weights assigned.",
-            "modified": "2023-09-26T19:23:33.191Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-012:05-012:009-595",
-            "describedBy": "https://www.jobcorps.gov/reports",
-            "describedByType": "text/html",
-            "landingPage": "https://www.jobcorps.gov/reports",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "JobCorps Individual Performance Records"
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
                 "fn": "Shao Zhang",
                 "hasEmail": "mailto:Zhang.Shao@dol.gov"
             },
+            "describedBy": "https://www.jobcorps.gov/reports",
+            "describedByType": "text/html",
+            "description": "The Outcome Measurement System (OMS) is Job Corps' primary tool for performance accountability, composed of various specific report cards that cover specific areas of operation. The OMS report cards measure and account for performance across Job Corps' outreach and admission, center operation, and career transition services areas. The performance measures are primarily derived from the program\u2019s authorizing legislation, the Workforce Innovation and Opportunity Act (WIOA), and U.S. Department of Labor (DOL) priorities, with goals and weights assigned.",
+            "identifier": "ETA-012:05-012:009-595",
             "keyword": [
                 "ETA",
                 "jobcorps",
                 "oms",
                 "outcome measurement system"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.jobcorps.gov/reports",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-09-26T19:23:33.191Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "WIOA State Plan Portal",
-            "description": "The Workforce Innovation and Opportunity Act (WIOA) State Plan Dataset contains state plans submitted through the WIOA State Plan portal for ETA review.  State plans establish how the States will administer their WIOA funds along with associated performance accountability requirements.  State plans are developed every 4 years with a modification every 2 years.",
-            "modified": "2023-09-07T19:37:19.293Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-012:05-012:018-594",
-            "describedBy": "https://www.dol.gov/agencies/eta/wioa/resources",
-            "describedByType": "text/html",
-            "landingPage": "https://wioaplans.ed.gov/",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "Outcome Measurement System - OMS"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Heather Fleck",
                 "hasEmail": "mailto:Fleck.Heather@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/wioa/resources",
+            "describedByType": "text/html",
+            "description": "The Workforce Innovation and Opportunity Act (WIOA) State Plan Dataset contains state plans submitted through the WIOA State Plan portal for ETA review.  State plans establish how the States will administer their WIOA funds along with associated performance accountability requirements.  State plans are developed every 4 years with a modification every 2 years.",
+            "identifier": "ETA-012:05-012:018-594",
             "keyword": [
                 "ETA",
                 "planning",
@@ -17402,36 +17396,36 @@
                 "workforce development",
                 "workforce system"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://wioaplans.ed.gov/",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-09-07T19:37:19.293Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "H-1B Joint Quarterly Narrative Performance Report",
-            "description": "The H-1B Joint Quarterly Narrative Performance Report dataset is a collection of qualitative narratives on H-1B grantees.  ETA collects qualitative information on grantee efforts, challenges, and outcomes (ETA-9179).  ETA-9179 allows grantees to provide a detailed account of all activities undertaken during the quarter, including in-depth information on accomplishments, promising approaches, progress toward performance outcomes, and upcoming grant activities.",
-            "modified": "2023-05-15T00:00:00Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-012:05-012:007-582",
-            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "WIOA State Plan Portal"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P6M",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jenn Smith",
                 "hasEmail": "mailto:smith.jenn@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "description": "The H-1B Joint Quarterly Narrative Performance Report dataset is a collection of qualitative narratives on H-1B grantees.  ETA collects qualitative information on grantee efforts, challenges, and outcomes (ETA-9179).  ETA-9179 allows grantees to provide a detailed account of all activities undertaken during the quarter, including in-depth information on accomplishments, promising approaches, progress toward performance outcomes, and upcoming grant activities.",
+            "identifier": "ETA-012:05-012:007-582",
             "keyword": [
                 "ETA",
                 "competitive grants",
@@ -17439,34 +17433,35 @@
                 "employment and training",
                 "h-1b"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/qwsr",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-05-15T00:00:00Z",
             "programCode": [
                 "012:007"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Dislocated Workers Grants (NDWG) Joint Quarterly Narrative Report (QNR) data (ETA-9179)",
-            "description": "Joint Quarterly Narrative Performance Report dataset is a collection of qualitative narratives on NDWG grantees.  ETA--9179 is used to collect qualitative information on grantee efforts, challenges, and outcomes.  The ETA-9179 allows grantees to provide a detailed account of all activities undertaken during the quarter, including in-depth information on accomplishments, promising approaches, progress toward performance outcomes, and upcoming grant activities.",
-            "modified": "2023-03-09T00:00:00Z",
-            "accessLevel": "non-public",
-            "identifier": "ETA-5-012:002-448",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "H-1B Joint Quarterly Narrative Performance Report"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Robert Kight",
                 "hasEmail": "mailto:kight.robert@dol.gov"
             },
+            "description": "Joint Quarterly Narrative Performance Report dataset is a collection of qualitative narratives on NDWG grantees.  ETA--9179 is used to collect qualitative information on grantee efforts, challenges, and outcomes.  The ETA-9179 allows grantees to provide a detailed account of all activities undertaken during the quarter, including in-depth information on accomplishments, promising approaches, progress toward performance outcomes, and upcoming grant activities.",
+            "identifier": "ETA-5-012:002-448",
             "keyword": [
                 "ETA",
                 "dislocated worker program",
@@ -17474,70 +17469,68 @@
                 "national dislocated worker program",
                 "ndwg"
             ],
-            "bureauCode": [
-                "012:05"
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-09T00:00:00Z",
             "programCode": [
                 "012:002"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Bonding Program data",
-            "description": "The Federal Bonding Program dataset includes information on the individuals and employers who are covered by bonds issued by the program. Data includes the address, gender, race, and Hispanic ethnicity of the individual being covered; the occupation, wage, and hours for work of the job the individual is being hired for; and the industry, sector (public/private/non-profit), and the number of employees of the firm being covered.",
-            "modified": "2022-12-20T00:00:00Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:018-445",
-            "describedBy": "https://www.govinfo.gov/content/pkg/FR-2019-09-05/pdf/2019-19142.pdf#page=1",
-            "landingPage": "https://www.govinfo.gov/content/pkg/FR-2019-09-05/pdf/2019-19142.pdf#page=1",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "National Dislocated Workers Grants (NDWG) Joint Quarterly Narrative Report (QNR) data (ETA-9179)"
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
+            "describedBy": "https://www.govinfo.gov/content/pkg/FR-2019-09-05/pdf/2019-19142.pdf#page=1",
+            "description": "The Federal Bonding Program dataset includes information on the individuals and employers who are covered by bonds issued by the program. Data includes the address, gender, race, and Hispanic ethnicity of the individual being covered; the occupation, wage, and hours for work of the job the individual is being hired for; and the industry, sector (public/private/non-profit), and the number of employees of the firm being covered.",
+            "identifier": "ETA-5-012:018-445",
             "keyword": [
                 "ETA",
                 "federal bonding"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.govinfo.gov/content/pkg/FR-2019-09-05/pdf/2019-19142.pdf#page=1",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-12-20T00:00:00Z",
             "programCode": [
                 "012:018"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Office of Trade Adjustment Assistance (OTAA) Participant Aggregates",
-            "description": "Aggregate participant records for TAA Program FY 2018 to Present.  Aggregates by state are posted publicly.",
-            "modified": "2024-09-27T14:52:22.779Z",
-            "accessLevel": "non-public",
-            "identifier": "ETA-5-012:011-505",
-            "describedBy": "https://www.dol.gov/agencies/eta/performance/wips/",
-            "landingPage": "https://www.dol.gov/agencies/eta/tradeact/data/participants",
-            "rights": "Not Available",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "Federal Bonding Program data"
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
                 "fn": "Susan Manikowski",
                 "hasEmail": "mailto:manikowski.susan@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/performance/wips/",
+            "description": "Aggregate participant records for TAA Program FY 2018 to Present.  Aggregates by state are posted publicly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17545,6 +17538,7 @@
                     "title": "Participants Data"
                 }
             ],
+            "identifier": "ETA-5-012:011-505",
             "keyword": [
                 "ETA",
                 "otaa",
@@ -17552,34 +17546,35 @@
                 "taa",
                 "trade"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/tradeact/data/participants",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-27T14:52:22.779Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Military to Civilian Crosswalk",
-            "description": "The Military to Civilian Crosswalk cross-references military occupation codes in the Air Force, Army, Navy, Marine Corps, and Coast Guard with their related civilian Standard Occupational Classification and O*NET codes and titles.\n\nO*NET web service available upon sign up.",
-            "modified": "2022-12-12T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:018-458",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "Not Available",
+            "title": "Office of Trade Adjustment Assistance (OTAA) Participant Aggregates"
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
                 "fn": "Steve Rietzke",
                 "hasEmail": "mailto:rietzke.steven@dol.gov"
             },
+            "description": "The Military to Civilian Crosswalk cross-references military occupation codes in the Air Force, Army, Navy, Marine Corps, and Coast Guard with their related civilian Standard Occupational Classification and O*NET codes and titles.\n\nO*NET web service available upon sign up.",
+            "identifier": "ETA-5-012:018-458",
             "keyword": [
                 "ETA",
                 "civilian jobs",
@@ -17587,35 +17582,34 @@
                 "military jobs",
                 "military ratings and skills"
             ],
-            "bureauCode": [
-                "012:05"
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-12-12T00:00:00Z",
             "programCode": [
                 "012:018"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Significant Provisions Report of State Unemployment Insurance Laws",
-            "description": "This bi-annual publication provides information on each state\u2019s wage requirements for unemployment insurance benefit eligibility, computation and amount of the weekly benefit, number of allowable benefit weeks and benefit week calculation, and the amount of earnings that will be disregarded for those individuals who are working part-time. It also provides information on the size of employer payroll required to pay unemployment taxes, the amount of wages subject to unemployment taxes, and the tax rates specific to each state\u2019s program.",
-            "modified": "2023-01-03T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-501",
-            "landingPage": "https://oui.doleta.gov/unemploy/statelaws.asp#RecentStatelaw",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Military to Civilian Crosswalk"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P6M",
+            "bureauCode": [
+                "012:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michelle Beebe",
                 "hasEmail": "mailto:beebe.michelle.e@dol.gov"
             },
+            "description": "This bi-annual publication provides information on each state\u2019s wage requirements for unemployment insurance benefit eligibility, computation and amount of the weekly benefit, number of allowable benefit weeks and benefit week calculation, and the amount of earnings that will be disregarded for those individuals who are working part-time. It also provides information on the size of employer payroll required to pay unemployment taxes, the amount of wages subject to unemployment taxes, and the tax rates specific to each state\u2019s program.",
+            "identifier": "ETA-5-012:013-501",
             "keyword": [
                 "ETA",
                 "benefit eligibility",
@@ -17623,133 +17617,118 @@
                 "unemployment taxes",
                 "weekly benefit amount"
             ],
-            "bureauCode": [
-                "012:05"
-            ],
+            "landingPage": "https://oui.doleta.gov/unemploy/statelaws.asp#RecentStatelaw",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-01-03T00:00:00Z",
             "programCode": [
                 "012:013"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Appeals Time Lapse (ETA-9054)",
-            "description": "Historical series of Appeals Time Lapse reports (ETA-9054) in which states provide monthly information on the time it take to issue lower authority and higher authority appeals decisions from the date the request for a lower authority hearing or a higher authority appeal is filed to the date on the decision",
-            "modified": "2024-03-29T16:10:32.755Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:013-490",
-            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
-            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9054",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Significant Provisions Report of State Unemployment Insurance Laws"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Stapleton",
                 "hasEmail": "mailto:stapleton.kevin@dol.gov"
             },
+            "describedBy": "https://wdr.doleta.gov/directives/attach/ETAH/ETHand401_5th.pdf",
+            "description": "Historical series of Appeals Time Lapse reports (ETA-9054) in which states provide monthly information on the time it take to issue lower authority and higher authority appeals decisions from the date the request for a lower authority hearing or a higher authority appeal is filed to the date on the decision",
+            "identifier": "ETA-5-012:013-490",
             "keyword": [
                 "ETA",
                 "higher authority appeals",
                 "lower authority appeals",
                 "time lapse"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_9054",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-29T16:10:32.755Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Project GATE (Growing America Through Entrepreneurship) Final Evaluation Dataset",
-            "description": "Project GATE was a random-assignment demonstration project designed to help public workforce system clients create, sustain or expand their own business. The cornerstone of the evaluation of Project GATE was random assignment. A total of 4,198 applicants to Project GATE were randomly assigned to either the program group or the control group. Members of the program group were offered GATE services; members of the control group were not. This dataset is the final data from the evaluation and includes administrative data from the six and eighteen month follow-ups and survey data from the six month, eighteen month, and sixty month follow-ups of program participants.",
-            "modified": "2023-03-14T00:00:00Z",
-            "accessLevel": "public",
-            "identifier": "ETA-5-012:018-511",
-            "landingPage": "https://www.dol.gov/agencies/eta/reports/project-gate-dataset",
-            "rights": "TRUE",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration"
             },
+            "rights": "TRUE",
+            "title": "Appeals Time Lapse (ETA-9054)"
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
+            "description": "Project GATE was a random-assignment demonstration project designed to help public workforce system clients create, sustain or expand their own business. The cornerstone of the evaluation of Project GATE was random assignment. A total of 4,198 applicants to Project GATE were randomly assigned to either the program group or the control group. Members of the program group were offered GATE services; members of the control group were not. This dataset is the final data from the evaluation and includes administrative data from the six and eighteen month follow-ups and survey data from the six month, eighteen month, and sixty month follow-ups of program participants.",
+            "identifier": "ETA-5-012:018-511",
             "keyword": [
                 "ETA",
                 "entreprenuership",
                 "gate",
                 "self-employment"
             ],
-            "bureauCode": [
-                "012:05"
+            "landingPage": "https://www.dol.gov/agencies/eta/reports/project-gate-dataset",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-14T00:00:00Z",
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
+            "title": "Project GATE (Growing America Through Entrepreneurship) Final Evaluation Dataset"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOL Enforcement Data - Accident",
-            "description": "This dataset provides information regarding accident investigations completed by OSHA, including narrative text about the accident.",
-            "modified": "2024-12-16T18:08:58.686Z",
             "accessLevel": "public",
-            "identifier": "OSHA-18-012:029-410",
-            "landingPage": "https://enforcedata.dol.gov/views/data_summary.php",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Chief Information Officer",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Chief Information Officer"
-                }
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "This dataset provides information regarding accident investigations completed by OSHA, including narrative text about the accident.",
+            "identifier": "OSHA-18-012:029-410",
             "keyword": [
                 "OSHA",
                 "accident"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://enforcedata.dol.gov/views/data_summary.php",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:08:58.686Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DOL Enforcement Data - Accident Abstract",
-            "description": "This dataset provides summary information about accidents investigated by OSHA.",
-            "modified": "2024-09-27T13:26:12.690Z",
-            "accessLevel": "public",
-            "identifier": "OSHA-18-012:029-411",
-            "landingPage": "https://enforcedata.dol.gov/views/data_summary.php",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Chief Information Officer",
@@ -17758,59 +17737,70 @@
                     "name": "Office of the Chief Information Officer"
                 }
             },
+            "rights": "true",
+            "title": "DOL Enforcement Data - Accident"
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
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "description": "This dataset provides summary information about accidents investigated by OSHA.",
+            "identifier": "OSHA-18-012:029-411",
             "keyword": [
                 "OSHA",
                 "accident",
                 "accident abstract"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://enforcedata.dol.gov/views/data_summary.php",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-27T13:26:12.690Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Senior Community Service Employment Program (SCSEP) National and State Local Grantees Contact List",
-            "description": "There are currently 75 SCSEP grantees: 19 national nonprofit organizations and 56 units of state and territorial governments. These two list contains contact information, including addresses, of the 19 national grantees and 56 state grantees.",
-            "modified": "2024-02-13T19:06:58.099Z",
-            "accessLevel": "public",
-            "identifier": "ETA-012:05-012:010-679",
-            "landingPage": "https://d2leuf3vilid4d.cloudfront.net/-/media/Communities/olderworkers/Files/2021/Communication-and-Contact-lists/SCSEP-NATIONAL-GRANTEES-3-18-2022.ashx",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Employment and Training Administration",
+                "name": "Office of the Chief Information Officer",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Employment and Training Administration"
+                    "name": "Office of the Chief Information Officer"
                 }
             },
+            "rights": "true",
+            "title": "DOL Enforcement Data - Accident Abstract"
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
                 "fn": "Toni Wilson",
                 "hasEmail": "mailto:Wilson.Toni.K@dol.gov"
             },
+            "description": "There are currently 75 SCSEP grantees: 19 national nonprofit organizations and 56 units of state and territorial governments. These two list contains contact information, including addresses, of the 19 national grantees and 56 state grantees.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "title": "Senior Community Service Employment Program (SCSEP) National and State/Local Grantees Contact List",
                     "description": "There are currently 75 SCSEP grantees: 19 national nonprofit organizations and 56 units of state and territorial governments. These two list contains contact information, including addresses, of the 19 national grantees and 56 state grantees.",
-                    "downloadURL": "https://d2leuf3vilid4d.cloudfront.net/-/media/Communities/olderworkers/Files/2021/Communication-and-Contact-lists/SCSEP-NATIONAL-GRANTEES-3-18-2022.ashx"
+                    "downloadURL": "https://d2leuf3vilid4d.cloudfront.net/-/media/Communities/olderworkers/Files/2021/Communication-and-Contact-lists/SCSEP-NATIONAL-GRANTEES-3-18-2022.ashx",
+                    "mediaType": "application/pdf",
+                    "title": "Senior Community Service Employment Program (SCSEP) National and State/Local Grantees Contact List"
                 }
             ],
+            "identifier": "ETA-012:05-012:010-679",
             "keyword": [
                 "ETA",
                 "Older Workers Grantee Contact Information",
@@ -17818,50 +17808,50 @@
                 "SCSEP National Grantees",
                 "Senior Community Service Employment Program Grantees"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://d2leuf3vilid4d.cloudfront.net/-/media/Communities/olderworkers/Files/2021/Communication-and-Contact-lists/SCSEP-NATIONAL-GRANTEES-3-18-2022.ashx",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-02-13T19:06:58.099Z",
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
-            "title": "Jobs for Veterans State Grants (JVSG) Performance Outcomes",
-            "description": "The Veterans' Employment and Training Service (VETS) tracks three participant outcome measures for the JVSG program. Programmatic performance outcomes are collected from JVSG recipients through the Department of Labor\u2019s Workforce Integrated Performance System. VETS shares JVSG outcomes with the public. These data show the national and state-level targets and outcomes for each of the three WIOA outcome measures by Program Year (PY), including breakouts by eligibility characteristics, gender, ethnicity, race, age, and significant barrier to employment category. The three outcome measures are:\nEmployment Rate - 2nd Quarter After Exit - the percentage of participants who are in unsubsidized employment during the second quarter after exit from the program.\nEmployment Rate - 4th Quarter After Exit - the percentage of participants who are in unsubsidized employment during the fourth quarter after exit from the program.\nMedian Earnings - 2nd Quarter After Exit - the median earnings of participants who are in unsubsidized employment during the second quarter after exit from the program.",
-            "modified": "2024-12-17T13:24:53.278Z",
-            "accessLevel": "public",
-            "identifier": "VETS-29-012:040-688",
-            "describedBy": "https://www.dol.gov/sites/dolgov/files/ETA/Performance/pdfs/ETA-9173-Program-Performance-Report-Templates-and-Specification-1.18.18s.pdf",
-            "describedByType": "application/pdf",
-            "landingPage": "https://www.dol.gov/agencies/vets/vetoutcomes",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Veterans\u2019 Employment and Training Service",
+                "name": "Employment and Training Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Veterans\u2019 Employment and Training Service"
+                    "name": "Employment and Training Administration"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Senior Community Service Employment Program (SCSEP) National and State Local Grantees Contact List"
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
                 "fn": "DOL-VETS-JVSG",
                 "hasEmail": "mailto:JVSG@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/sites/dolgov/files/ETA/Performance/pdfs/ETA-9173-Program-Performance-Report-Templates-and-Specification-1.18.18s.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Veterans' Employment and Training Service (VETS) tracks three participant outcome measures for the JVSG program. Programmatic performance outcomes are collected from JVSG recipients through the Department of Labor\u2019s Workforce Integrated Performance System. VETS shares JVSG outcomes with the public. These data show the national and state-level targets and outcomes for each of the three WIOA outcome measures by Program Year (PY), including breakouts by eligibility characteristics, gender, ethnicity, race, age, and significant barrier to employment category. The three outcome measures are:\nEmployment Rate - 2nd Quarter After Exit - the percentage of participants who are in unsubsidized employment during the second quarter after exit from the program.\nEmployment Rate - 4th Quarter After Exit - the percentage of participants who are in unsubsidized employment during the fourth quarter after exit from the program.\nMedian Earnings - 2nd Quarter After Exit - the median earnings of participants who are in unsubsidized employment during the second quarter after exit from the program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/vets/vetoutcomes"
                 }
             ],
+            "identifier": "VETS-29-012:040-688",
             "keyword": [
                 "American Job Centers",
                 "DVOP",
@@ -17879,27 +17869,14 @@
                 "veterans",
                 "veterans served"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/vets/vetoutcomes",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T13:24:53.278Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Jobs for Veterans State Grants (JVSG) Uniform National Threshold Entered Employment Rate (UNTEER)",
-            "description": "The Uniform National Threshold Entered Employment Rate (UNTEER) is a national threshold Veterans\u2019 Entered Employment Rate (VEER) for veterans and other eligible persons served by the Jobs for Veterans State Grants (JVSG) program and the Wagner-Peyser funded Employment Service. This data table shows the percentage of exiters who were unemployed or received notice of termination/layoff at program entry and were then employed in the first quarter after exit for each state, ranked from highest to lowest VEER.",
-            "modified": "2024-12-17T13:26:44.188Z",
-            "accessLevel": "public",
-            "identifier": "VETS-29-012:040-689",
-            "describedBy": "https://wdr.doleta.gov/directives/attach/tegl/tegl2-13acc.pdf",
-            "describedByType": "application/pdf",
-            "landingPage": "https://www.dol.gov/agencies/vets/programs/grants/state/jvsg/unteer",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Veterans\u2019 Employment and Training Service",
@@ -17908,18 +17885,31 @@
                     "name": "Veterans\u2019 Employment and Training Service"
                 }
             },
+            "rights": "true",
+            "title": "Jobs for Veterans State Grants (JVSG) Performance Outcomes"
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
                 "fn": "DOL-VETS-JVSG",
                 "hasEmail": "mailto:JVSG@dol.gov"
             },
+            "describedBy": "https://wdr.doleta.gov/directives/attach/tegl/tegl2-13acc.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Uniform National Threshold Entered Employment Rate (UNTEER) is a national threshold Veterans\u2019 Entered Employment Rate (VEER) for veterans and other eligible persons served by the Jobs for Veterans State Grants (JVSG) program and the Wagner-Peyser funded Employment Service. This data table shows the percentage of exiters who were unemployed or received notice of termination/layoff at program entry and were then employed in the first quarter after exit for each state, ranked from highest to lowest VEER.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/vets/programs/grants/state/jvsg/unteer"
                 }
             ],
+            "identifier": "VETS-29-012:040-689",
             "keyword": [
                 "JVSG",
                 "Jobs for Veterans State Grants",
@@ -17931,27 +17921,14 @@
                 "veterans",
                 "vets"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/vets/programs/grants/state/jvsg/unteer",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T13:26:44.188Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Jobs for Veterans State Grants (JVSG) Performance - State Performance Target Tool",
-            "description": "The Veterans' Employment and Training Service (VETS) tracks three participant outcome measures for the JVSG program. Programmatic performance outcomes are collected from JVSG recipients through the Department of Labor\u2019s Workforce Integrated Performance System. VETS shares JVSG outcomes with the public. These data show the historical state-level targets and outcomes for each of the three WIOA outcome measures by Program Year (PY). The three outcome measures are:\nEmployment Rate - 2nd Quarter After Exit - the percentage of participants who are in unsubsidized employment during the second quarter after exit from the program.\nEmployment Rate - 4th Quarter After Exit - the percentage of participants who are in unsubsidized employment during the fourth quarter after exit from the program.\nMedian Earnings - 2nd Quarter After Exit - the median earnings of participants who are in unsubsidized employment during the second quarter after exit from the program.\nFind performance outcomes for each state over the last several years.",
-            "modified": "2024-12-17T13:28:44.298Z",
-            "accessLevel": "public",
-            "identifier": "VETS-29-012:040-690",
-            "describedBy": "https://www.dol.gov/sites/dolgov/files/ETA/Performance/pdfs/ETA-9173-Program-Performance-Report-Templates-and-Specification-1.18.18s.pdf",
-            "describedByType": "application/pdf",
-            "landingPage": "https://www.dol.gov/agencies/vets/programs/grants/state/jvsg/performance",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Veterans\u2019 Employment and Training Service",
@@ -17960,19 +17937,32 @@
                     "name": "Veterans\u2019 Employment and Training Service"
                 }
             },
+            "rights": "true",
+            "title": "Jobs for Veterans State Grants (JVSG) Uniform National Threshold Entered Employment Rate (UNTEER)"
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
                 "fn": "DOL-VETS-JVSG",
                 "hasEmail": "mailto:JVSG@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/sites/dolgov/files/ETA/Performance/pdfs/ETA-9173-Program-Performance-Report-Templates-and-Specification-1.18.18s.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Veterans' Employment and Training Service (VETS) tracks three participant outcome measures for the JVSG program. Programmatic performance outcomes are collected from JVSG recipients through the Department of Labor\u2019s Workforce Integrated Performance System. VETS shares JVSG outcomes with the public. These data show the historical state-level targets and outcomes for each of the three WIOA outcome measures by Program Year (PY). The three outcome measures are:\nEmployment Rate - 2nd Quarter After Exit - the percentage of participants who are in unsubsidized employment during the second quarter after exit from the program.\nEmployment Rate - 4th Quarter After Exit - the percentage of participants who are in unsubsidized employment during the fourth quarter after exit from the program.\nMedian Earnings - 2nd Quarter After Exit - the median earnings of participants who are in unsubsidized employment during the second quarter after exit from the program.\nFind performance outcomes for each state over the last several years.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "downloadURL": "https://www.dol.gov/sites/dolgov/files/VETS/files/JVSG_State_Performance_Target_Tool_revJan2024.xlsx"
+                    "downloadURL": "https://www.dol.gov/sites/dolgov/files/VETS/files/JVSG_State_Performance_Target_Tool_revJan2024.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "VETS-29-012:040-690",
             "keyword": [
                 "JVSG",
                 "Jobs for Veterans State Grants",
@@ -17985,26 +17975,14 @@
                 "veterans",
                 "vets"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/vets/programs/grants/state/jvsg/performance",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T13:28:44.298Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Homeless Veteran Reintegration Program (HVRP) Outcomes",
-            "description": "The Veterans' Employment and Training Service (VETS) tracks participant outcome measures for the HVRP program. Programmatic performance outcomes are collected from grant recipients through the Technical Performance Report (TPR) form. VETS shares HVRP outcomes with the public. These data show the national level targets and outcomes for eleven (11) measures by Program Year (PY), including breakouts by subpopulation, gender, ethnicity, race, and age. The 11 measures are:\n1. Number of Participants Served\n2. Percentage of Total Participants Served\n3. Number of Exiters\n4. Percentage of Total Number of Exiters\n5. Number of Participants Co-Enrolled at American Job Centers (AJCs)\n6. Average Hourly Wage at Placement\n7. Placement Rate (exit-based)\n8. Placement Rate \u2013 Episodically Homeless (exit-based)\n9. Employment Rate 2nd Quarter After Exit\n10. Employment Rate 4th Quarter After Exit\n11. Median Earnings 2nd Quarter After Exit",
-            "modified": "2024-12-17T13:33:16.196Z",
-            "accessLevel": "public",
-            "identifier": "VETS-29-012:042-691",
-            "describedBy": "https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fwww.dol.gov%2Fsites%2Fdolgov%2Ffiles%2FVETS%2Ffiles%2FHVRP-Glossary-of-Terms-revAug2023.docx&wdOrigin=BROWSELINK",
-            "landingPage": "https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fwww.dol.gov%2Fsites%2Fdolgov%2Ffiles%2FVETS%2Flegacy%2Ffiles%2FHVRP_PY21_Targets_and_Outcomes.xlsx&wdOrigin=BROWSELINK",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Veterans\u2019 Employment and Training Service",
@@ -18013,12 +17991,24 @@
                     "name": "Veterans\u2019 Employment and Training Service"
                 }
             },
+            "rights": "true",
+            "title": "Jobs for Veterans State Grants (JVSG) Performance - State Performance Target Tool"
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
                 "fn": "DOL-VETS-HVRP",
                 "hasEmail": "mailto:HVRP@dol.gov"
             },
+            "describedBy": "https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fwww.dol.gov%2Fsites%2Fdolgov%2Ffiles%2FVETS%2Ffiles%2FHVRP-Glossary-of-Terms-revAug2023.docx&wdOrigin=BROWSELINK",
+            "description": "The Veterans' Employment and Training Service (VETS) tracks participant outcome measures for the HVRP program. Programmatic performance outcomes are collected from grant recipients through the Technical Performance Report (TPR) form. VETS shares HVRP outcomes with the public. These data show the national level targets and outcomes for eleven (11) measures by Program Year (PY), including breakouts by subpopulation, gender, ethnicity, race, and age. The 11 measures are:\n1. Number of Participants Served\n2. Percentage of Total Participants Served\n3. Number of Exiters\n4. Percentage of Total Number of Exiters\n5. Number of Participants Co-Enrolled at American Job Centers (AJCs)\n6. Average Hourly Wage at Placement\n7. Placement Rate (exit-based)\n8. Placement Rate \u2013 Episodically Homeless (exit-based)\n9. Employment Rate 2nd Quarter After Exit\n10. Employment Rate 4th Quarter After Exit\n11. Median Earnings 2nd Quarter After Exit",
+            "identifier": "VETS-29-012:042-691",
             "keyword": [
                 "701",
                 "HVRP",
@@ -18030,67 +18020,54 @@
                 "veterans",
                 "vets"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fwww.dol.gov%2Fsites%2Fdolgov%2Ffiles%2FVETS%2Flegacy%2Ffiles%2FHVRP_PY21_Targets_and_Outcomes.xlsx&wdOrigin=BROWSELINK",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T13:33:16.196Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DOL Enforcement Data - Accident Injury",
-            "description": "This dataset provides coded information about injured workers related to an OSHA investigation or inspection.",
-            "modified": "2024-12-16T18:12:05.795Z",
-            "accessLevel": "public",
-            "identifier": "OSHA-18-012:029-412",
-            "describedBy": "https://enforcedata.dol.gov/views/data_dictionary.php",
-            "describedByType": "application/vnd.ms-excel",
-            "landingPage": "https://enforcedata.dol.gov/views/data_summary.php",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Chief Information Officer",
+                "name": "Veterans\u2019 Employment and Training Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Chief Information Officer"
+                    "name": "Veterans\u2019 Employment and Training Service"
                 }
             },
+            "rights": "true",
+            "title": "Homeless Veteran Reintegration Program (HVRP) Outcomes"
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
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "describedBy": "https://enforcedata.dol.gov/views/data_dictionary.php",
+            "describedByType": "application/vnd.ms-excel",
+            "description": "This dataset provides coded information about injured workers related to an OSHA investigation or inspection.",
+            "identifier": "OSHA-18-012:029-412",
             "keyword": [
                 "OSHA",
                 "accident",
                 "accident injury"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://enforcedata.dol.gov/views/data_summary.php",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:12:05.795Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DOL Enforcement Data - Accident Lookup2",
-            "description": "This dataset provides a lookup table that matches codes with different occupations of workers who suffered an occupational injury or illness.",
-            "modified": "2024-12-16T18:14:22.466Z",
-            "accessLevel": "public",
-            "identifier": "OSHA-18-012:029-413",
-            "describedBy": "https://enforcedata.dol.gov/views/data_dictionary.php",
-            "describedByType": "application/vnd.ms-excel",
-            "landingPage": "https://enforcedata.dol.gov/views/data_summary.php",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Chief Information Officer",
@@ -18099,40 +18076,39 @@
                     "name": "Office of the Chief Information Officer"
                 }
             },
+            "rights": "true",
+            "title": "DOL Enforcement Data - Accident Injury"
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
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "describedBy": "https://enforcedata.dol.gov/views/data_dictionary.php",
+            "describedByType": "application/vnd.ms-excel",
+            "description": "This dataset provides a lookup table that matches codes with different occupations of workers who suffered an occupational injury or illness.",
+            "identifier": "OSHA-18-012:029-413",
             "keyword": [
                 "OSHA",
                 "accident",
                 "accident lookup",
                 "accident lookup2"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://enforcedata.dol.gov/views/data_summary.php",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:14:22.466Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "DOL Enforcement Data - Inspection",
-            "description": "This dataset provides summary information about inspections conducted by OSHA.",
-            "modified": "2024-12-16T18:09:38.484Z",
-            "accessLevel": "public",
-            "identifier": "OSHA-18-012:029-414",
-            "describedBy": "https://enforcedata.dol.gov/views/data_dictionary.php",
-            "describedByType": "application/vnd.ms-excel",
-            "landingPage": "https://enforcedata.dol.gov/views/data_summary.php",
-            "rights": "true",
-            "spatial": "Address",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Chief Information Officer",
@@ -18141,62 +18117,76 @@
                     "name": "Office of the Chief Information Officer"
                 }
             },
+            "rights": "true",
+            "title": "DOL Enforcement Data - Accident Lookup2"
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
                 "fn": "Thomas 'Nate' Benz",
                 "hasEmail": "mailto:benz.thomas.n@dol.gov"
             },
+            "describedBy": "https://enforcedata.dol.gov/views/data_dictionary.php",
+            "describedByType": "application/vnd.ms-excel",
+            "description": "This dataset provides summary information about inspections conducted by OSHA.",
+            "identifier": "OSHA-18-012:029-414",
             "keyword": [
                 "OSHA",
                 "inspection"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://enforcedata.dol.gov/views/data_summary.php",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-16T18:09:38.484Z",
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
-            "title": "State Paid Family and Medical Leave Laws",
-            "description": "State Paid Family and Medical Leave Laws (Available in English and Spanish)",
-            "modified": "2024-03-13T13:43:42.067Z",
-            "accessLevel": "public",
-            "identifier": "WB-12-012:038-692",
-            "dataQuality": true,
-            "issued": "2023-09-01",
-            "landingPage": "https://www.dol.gov/agencies/wb/paid-leave/State-Paid-Family-Medical-Leave-Laws",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Women's Bureau",
+                "name": "Office of the Chief Information Officer",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Women's Bureau"
+                    "name": "Office of the Chief Information Officer"
                 }
             },
+            "rights": "true",
+            "spatial": "Address",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "DOL Enforcement Data - Inspection"
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
+            "dataQuality": true,
+            "description": "State Paid Family and Medical Leave Laws (Available in English and Spanish)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/wb/paid-leave/State-Paid-Family-Medical-Leave-Laws",
-                    "title": "State Paid Family and Medical Leave Laws",
-                    "description": "State Paid Family and Medical Leave Laws"
+                    "description": "State Paid Family and Medical Leave Laws",
+                    "title": "State Paid Family and Medical Leave Laws"
                 }
             ],
+            "identifier": "WB-12-012:038-692",
+            "issued": "2023-09-01",
             "keyword": [
                 "English",
                 "Spanish",
@@ -18204,29 +18194,14 @@
                 "paid leave",
                 "state"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/wb/paid-leave/State-Paid-Family-Medical-Leave-Laws",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-03-13T13:43:42.067Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Database of Childcare Prices: 2022 State-Level Estimates",
-            "description": "National Database of Childcare Prices: 2022 State-Level Estimates",
-            "modified": "2024-11-27T19:50:58.464Z",
-            "accessLevel": "public",
-            "identifier": "WB-12-012:038-693",
-            "dataQuality": true,
-            "describedBy": "https://www.dol.gov/sites/dolgov/files/WB/NDCP2022-Technical-Report-508.pdf",
-            "describedByType": "application/pdf",
-            "issued": "2024-11-15",
-            "landingPage": "https://www.dol.gov/agencies/wb/topics/featured-childcare",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Women's Bureau",
@@ -18235,49 +18210,49 @@
                     "name": "Women's Bureau"
                 }
             },
+            "rights": "true",
+            "title": "State Paid Family and Medical Leave Laws"
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
+            "dataQuality": true,
+            "describedBy": "https://www.dol.gov/sites/dolgov/files/WB/NDCP2022-Technical-Report-508.pdf",
+            "describedByType": "application/pdf",
+            "description": "National Database of Childcare Prices: 2022 State-Level Estimates",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "National Database of Childcare Prices: State-Level Estimates and Affordability Rankings 2022 (XLSX)",
                     "description": "Source: National Database of Childcare Prices 2022, Women's Bureau, U.S. Department of Labor\nNote: Childcare prices are derived from each state's childcare Market Rate Survey. Prices are median yearly prices for one child at the market rate. School-age prices reflect the school-year arrangement (part day). Childcare prices are based on the 2019-2022 data collection cycle  and are presented in 2022 real dollars using the CPI-U for child care (day care and preschool in the U.S. city average). \nNDCP data are intended to be used at the county level; caution is advised when using state averages. State averages are created by weighting county childcare price estimates by county population for counties with available childcare price data. Some states have more missing data than others which could impact the estimated state averages. \nAs a result, state averages may not meet the higher quality standards developed for the NDCP county-level estimates. This product is experimental and may be revised as estimation methodologies improve and additional data become available.",
-                    "downloadURL": "https://www.dol.gov/sites/dolgov/files/WB/NDCP2022-state-level-estimates-and-rankings.xlsx"
+                    "downloadURL": "https://www.dol.gov/sites/dolgov/files/WB/NDCP2022-state-level-estimates-and-rankings.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "National Database of Childcare Prices: State-Level Estimates and Affordability Rankings 2022 (XLSX)"
                 }
             ],
+            "identifier": "WB-12-012:038-693",
+            "issued": "2024-11-15",
             "keyword": [
                 "WB",
                 "childcare prices",
                 "state"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/wb/topics/featured-childcare",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-11-27T19:50:58.464Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Maps-Childcare Prices by Age of Children and Care Setting 2022",
-            "description": "Maps: Childcare Prices by Age of Children and Care Setting, 2022",
-            "modified": "2024-11-27T19:47:12.430Z",
-            "accessLevel": "public",
-            "identifier": "WB-12-012:038-694",
-            "dataQuality": true,
-            "describedBy": "https://www.dol.gov/sites/dolgov/files/WB/NDCP2022-Technical-Report-508.pdf",
-            "describedByType": "application/pdf",
-            "issued": "2024-11-15",
-            "landingPage": "https://www.dol.gov/agencies/wb/topics/featured-childcare",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Women's Bureau",
@@ -18286,97 +18261,112 @@
                     "name": "Women's Bureau"
                 }
             },
+            "rights": "true",
+            "title": "National Database of Childcare Prices: 2022 State-Level Estimates"
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
+            "dataQuality": true,
+            "describedBy": "https://www.dol.gov/sites/dolgov/files/WB/NDCP2022-Technical-Report-508.pdf",
+            "describedByType": "application/pdf",
+            "description": "Maps: Childcare Prices by Age of Children and Care Setting, 2022",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/wb/topics/childcare/price-by-age-care-setting/",
-                    "title": "Maps: Childcare Prices by Age of Children and Care Setting, 2022",
-                    "description": "Maps: Childcare Prices by Age of Children and Care Setting, 2022"
+                    "description": "Maps: Childcare Prices by Age of Children and Care Setting, 2022",
+                    "title": "Maps: Childcare Prices by Age of Children and Care Setting, 2022"
                 }
             ],
+            "identifier": "WB-12-012:038-694",
+            "issued": "2024-11-15",
             "keyword": [
                 "WB",
                 "childcare prices",
                 "county"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/wb/topics/featured-childcare",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-11-27T19:47:12.430Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Foreign Labor Recruiter List",
-            "description": "The list contains the name and location of persons or entities identified on Appendix C of the Form ETA-9142B that were hired by, or working for, the recruiter that employers have indicated they engaged, or planned to engage, in the recruitment of prospective H-2B workers to perform the work described on their H-2B application. By providing this Foreign Labor Recruiter List, the U.S. Department of Labor is in a better position to enforce recruitment violations and workers are better protected against fraudulent recruiting schemes. Specifically, they will be able to verify whether a recruiter is recruiting for legitimate H-2B job opportunities in the United States. Workers can use the case number(s) associated with a recruiter in this list to identify the job order(s) in OFLC's Electronic Job Registry for which the recruiter is seeking workers.",
-            "modified": "2024-12-26T19:40:59.950Z",
-            "accessLevel": "public",
-            "identifier": "ETA-012:05-12:017-703",
-            "describedBy": "https://www.dol.gov/agencies/eta/foreign-labor/recruiter-list",
-            "landingPage": "https://www.dol.gov/agencies/eta/foreign-labor/recruiter-list",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Employment and Training Administration",
+                "name": "Women's Bureau",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Employment and Training Administration"
+                    "name": "Women's Bureau"
                 }
             },
+            "rights": "true",
+            "title": "Maps-Childcare Prices by Age of Children and Care Setting 2022"
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
                 "fn": "Rob Jordan",
                 "hasEmail": "mailto:jordan.rob@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/foreign-labor/recruiter-list",
+            "description": "The list contains the name and location of persons or entities identified on Appendix C of the Form ETA-9142B that were hired by, or working for, the recruiter that employers have indicated they engaged, or planned to engage, in the recruitment of prospective H-2B workers to perform the work described on their H-2B application. By providing this Foreign Labor Recruiter List, the U.S. Department of Labor is in a better position to enforce recruitment violations and workers are better protected against fraudulent recruiting schemes. Specifically, they will be able to verify whether a recruiter is recruiting for legitimate H-2B job opportunities in the United States. Workers can use the case number(s) associated with a recruiter in this list to identify the job order(s) in OFLC's Electronic Job Registry for which the recruiter is seeking workers.",
+            "identifier": "ETA-012:05-12:017-703",
             "keyword": [
                 "ETA"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/foreign-labor/recruiter-list",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-26T19:40:59.950Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "VETS-401 - Jobs for Veterans State Grants (JVSG) Budget Information Summary",
-            "description": "States initially use the Jobs for Veterans State Grants (JVSG) Budget Information Summary form when applying for the formula level of funds available for the Disabled Veterans\u2019 Outreach Program (DVOP) specialist positions, Local Veterans\u2019 Employment Representative (LVER) staff positions, Consolidated (DVOP/LVER) positions, Incentive Award Funds, and Management and Administrative Costs.\n\nState funding requests must summarize how the formula allocated funding and any additional funding will be budgeted by cost category and by quarter. States must update the form and include it with any modification request that affects either the planned budget or staffing levels.",
-            "modified": "2024-12-17T13:36:09.883Z",
-            "accessLevel": "non-public",
-            "identifier": "VETS-29-012:040-698",
-            "describedBy": "https://www.dol.gov/sites/dolgov/files/VETS/files/VETS-401-Instructions-rev2022.06.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
-            "rights": "Sensitive Financial information",
-            "spatial": "State",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Veterans\u2019 Employment and Training Service",
+                "name": "Employment and Training Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Veterans\u2019 Employment and Training Service"
+                    "name": "Employment and Training Administration"
                 }
             },
+            "rights": "true",
+            "title": "Foreign Labor Recruiter List"
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
                 "fn": "DOL-VETS-JVSG",
                 "hasEmail": "mailto:JVSGE-TPARSupport@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/sites/dolgov/files/VETS/files/VETS-401-Instructions-rev2022.06.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "States initially use the Jobs for Veterans State Grants (JVSG) Budget Information Summary form when applying for the formula level of funds available for the Disabled Veterans\u2019 Outreach Program (DVOP) specialist positions, Local Veterans\u2019 Employment Representative (LVER) staff positions, Consolidated (DVOP/LVER) positions, Incentive Award Funds, and Management and Administrative Costs.\n\nState funding requests must summarize how the formula allocated funding and any additional funding will be budgeted by cost category and by quarter. States must update the form and include it with any modification request that affects either the planned budget or staffing levels.",
+            "identifier": "VETS-29-012:040-698",
             "keyword": [
                 "401",
                 "Budget Information Summary",
@@ -18390,25 +18380,13 @@
                 "veterans",
                 "vets"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T13:36:09.883Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "VETS-402 - Jobs for Veterans State Grants Expenditure Detail Report (EDR)",
-            "description": "\"Use the Jobs for Veterans State Grants (JVSG) EDR to report obligation, expenditure, and staffing information for each grant award. The U.S. Department of Labor, Veterans\u2019 Employment and Training Service (VETS) uses the required, detailed information to monitor administrative costs, staff utilization, and planned spending compared to actual spending for the staffing grant.\n\nThe VETS-402 expiring June 30, 2025, must be used for all JVSG quarterly financial reports relating to Fiscal Year (FY) 2023 and beyond until OMB approves a new version.\n\nFY monies must be segregated and separately tracked. Therefore, states must complete one JVSG EDR per grant award, and update each quarter until all available funding has been expended.\"",
-            "modified": "2024-09-27T17:37:34.122Z",
-            "accessLevel": "non-public",
-            "identifier": "VETS-29-012:040-699",
-            "rights": "Sensitive Financial information",
-            "spatial": "State",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Veterans\u2019 Employment and Training Service",
@@ -18417,12 +18395,24 @@
                     "name": "Veterans\u2019 Employment and Training Service"
                 }
             },
+            "rights": "Sensitive Financial information",
+            "spatial": "State",
+            "title": "VETS-401 - Jobs for Veterans State Grants (JVSG) Budget Information Summary"
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
                 "fn": "DOL-VETS-JVSG",
                 "hasEmail": "mailto:JVSGE-TPARSupport@dol.gov"
             },
+            "description": "\"Use the Jobs for Veterans State Grants (JVSG) EDR to report obligation, expenditure, and staffing information for each grant award. The U.S. Department of Labor, Veterans\u2019 Employment and Training Service (VETS) uses the required, detailed information to monitor administrative costs, staff utilization, and planned spending compared to actual spending for the staffing grant.\n\nThe VETS-402 expiring June 30, 2025, must be used for all JVSG quarterly financial reports relating to Fiscal Year (FY) 2023 and beyond until OMB approves a new version.\n\nFY monies must be segregated and separately tracked. Therefore, states must complete one JVSG EDR per grant award, and update each quarter until all available funding has been expended.\"",
+            "identifier": "VETS-29-012:040-699",
             "keyword": [
                 "402",
                 "Consolidated Plan",
@@ -18437,61 +18427,50 @@
                 "veterans",
                 "vets"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-27T17:37:34.122Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ServiceNow Asset Inventory",
-            "description": "Asset Inventory",
-            "modified": "2024-09-23T13:24:07.989Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM OCIO -25-012:044-699",
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
+            "rights": "Sensitive Financial information",
+            "spatial": "State",
+            "title": "VETS-402 - Jobs for Veterans State Grants Expenditure Detail Report (EDR)"
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
                 "fn": "Harry Council Jr",
                 "hasEmail": "mailto:CouncilJr.Harry@dol.gov"
             },
+            "description": "Asset Inventory",
+            "identifier": "OASAM OCIO -25-012:044-699",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:24:07.989Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "OASIS",
-            "description": "OASIS is a complete, concise statement of the specific financial terms and conditions by which a Customer occupies GSA-controlled space, whether it is government-owned or leased by GSA on the Customer\u2019s behalf. When a project is initiated, a draft OA is created. Designed to provide the greatest amount of flexibility and choice, the OA documents the Customer\u2019s requirements as they evolve. It provides important information to guide decision making with regard to budget and other issues. It also records and finalizes all the agreed-upon terms and conditions of tenant occupancy, so that the Customer and GSA enter the agreement with the same understanding and expectations. The OA lets the Customer see what its costs will be and how various decisions will affect its rent bill.\n\nOASIS is a Customer-facing application where real-time Occupancy Agreement information and documentation is available to enhance the Customer experience and support decision making.\nOASIS is a Customer-facing application where real-time Occupancy Agreement information and documentation is available to enhance the Customer experience and support decision making.",
-            "modified": "2024-06-27T13:55:10.547Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM BOC-25-012:044-213",
-            "rights": "restricted",
-            "spatial": "location characteristics, address",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -18500,12 +18479,23 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "restricted",
+            "title": "ServiceNow Asset Inventory"
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
                 "hasEmail": "mailto:ehkop.christopher.h@dol.gov"
             },
+            "description": "OASIS is a complete, concise statement of the specific financial terms and conditions by which a Customer occupies GSA-controlled space, whether it is government-owned or leased by GSA on the Customer\u2019s behalf. When a project is initiated, a draft OA is created. Designed to provide the greatest amount of flexibility and choice, the OA documents the Customer\u2019s requirements as they evolve. It provides important information to guide decision making with regard to budget and other issues. It also records and finalizes all the agreed-upon terms and conditions of tenant occupancy, so that the Customer and GSA enter the agreement with the same understanding and expectations. The OA lets the Customer see what its costs will be and how various decisions will affect its rent bill.\n\nOASIS is a Customer-facing application where real-time Occupancy Agreement information and documentation is available to enhance the Customer experience and support decision making.\nOASIS is a Customer-facing application where real-time Occupancy Agreement information and documentation is available to enhance the Customer experience and support decision making.",
+            "identifier": "OASAM BOC-25-012:044-213",
             "keyword": [
                 "BOC",
                 "GSA",
@@ -18513,28 +18503,13 @@
                 "OASAM",
                 "eOA"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-06-27T13:55:10.547Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://www.gsa.gov/tools-overview/buildings-real-estate-etools/electronic-occupancy-agreement-eoa"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Motor Vehicle Fleet data GSAFleet.gov",
-            "description": "GSAFleet.gov",
-            "modified": "2024-06-27T14:05:08.301Z",
-            "accessLevel": "restricted public",
-            "identifier": "OASAM-BOC-25-012:044-686",
-            "rights": "restricted",
-            "spatial": "location characteristics, address",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -18543,41 +18518,40 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "references": [
+                "https://www.gsa.gov/tools-overview/buildings-real-estate-etools/electronic-occupancy-agreement-eoa"
+            ],
+            "rights": "restricted",
+            "spatial": "location characteristics, address",
+            "title": "OASIS"
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
+            "description": "GSAFleet.gov",
+            "identifier": "OASAM-BOC-25-012:044-686",
             "keyword": [
                 "BOC",
                 "GSA",
                 "GSAFleet.gov",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-06-27T14:05:08.301Z",
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
-            "title": "TeleworkXpress",
-            "description": "Automated Telework Application for requesting and approving telework agreements.",
-            "modified": "2024-09-23T13:41:34.383Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM-25-012:044-683",
-            "landingPage": "https://labornet.dol.gov/me/hr/HRIS/HRXpress.htm",
-            "rights": "private",
-            "spatial": "location characteristics, addresses",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -18586,12 +18560,27 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "restricted",
+            "spatial": "location characteristics, address",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Motor Vehicle Fleet data GSAFleet.gov"
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
                 "fn": "Lisa Anderson",
                 "hasEmail": "mailto:anderson.lisa.m1@dol.gov"
             },
+            "description": "Automated Telework Application for requesting and approving telework agreements.",
+            "identifier": "OASAM-25-012:044-683",
             "keyword": [
                 "OASAM",
                 "OHR",
@@ -18599,29 +18588,14 @@
                 "Remote work",
                 "telework"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://labornet.dol.gov/me/hr/HRIS/HRXpress.htm",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:41:34.383Z",
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
-            "title": "TransitXpress",
-            "description": "Automated Transit Application for requesting and approving Transit Subsidy Benefits.",
-            "modified": "2024-09-23T13:42:56.360Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM-25-012:044-684",
-            "landingPage": "https://labornet.dol.gov/me/hr/HRIS/HRXpress.htm",
-            "rights": "private",
-            "spatial": "location characteristics, addresses",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -18630,39 +18604,40 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "spatial": "location characteristics, addresses",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "TeleworkXpress"
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
                 "fn": "Lisa Anderson",
                 "hasEmail": "mailto:anderson.lisa.m1@dol.gov"
             },
+            "description": "Automated Transit Application for requesting and approving Transit Subsidy Benefits.",
+            "identifier": "OASAM-25-012:044-684",
             "keyword": [
                 "OASAM",
                 "OHR",
                 "Transit"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://labornet.dol.gov/me/hr/HRIS/HRXpress.htm",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:42:56.360Z",
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
-            "title": "Applicant and Manager Satisfaction with Hiring",
-            "description": "Survey on overall hiring manager satisfaction, meeting hiring manager expectations and how the hiring process compares with an ideal hiring process.",
-            "modified": "2024-09-23T13:40:05.683Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OHR-25-012:044-242",
-            "landingPage": "https://login.max.gov/cas/login?service=https%3A%2F%2Fcommunity.connect.gov%2Fpages%2Ftinyurl.action%3FurlIdentifier%3DTSJ0ZQ%2F",
-            "rights": "private",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -18671,35 +18646,39 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "spatial": "location characteristics, addresses",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "TransitXpress"
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
                 "fn": "Lauren Haring",
                 "hasEmail": "mailto:haring.lauren.n@dol.gov"
             },
+            "description": "Survey on overall hiring manager satisfaction, meeting hiring manager expectations and how the hiring process compares with an ideal hiring process.",
+            "identifier": "OASAM OHR-25-012:044-242",
             "keyword": [
                 "OASAM",
                 "OHR"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://login.max.gov/cas/login?service=https%3A%2F%2Fcommunity.connect.gov%2Fpages%2Ftinyurl.action%3FurlIdentifier%3DTSJ0ZQ%2F",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:40:05.683Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "FEVS",
-            "description": "Survey of employee perceptions.",
-            "modified": "2024-09-23T13:34:31.016Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OHR-25-012:044-238",
-            "landingPage": "https://labornet.dol.gov/me/hr/OEE/FEVS.htm",
-            "rights": "private",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -18708,37 +18687,36 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "title": "Applicant and Manager Satisfaction with Hiring"
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
                 "fn": "Kristin McNally",
                 "hasEmail": "mailto:McNally.Kristin.N@dol.gov"
             },
+            "description": "Survey of employee perceptions.",
+            "identifier": "OASAM OHR-25-012:044-238",
             "keyword": [
                 "FEVS",
                 "OASAM",
                 "OHR"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://labornet.dol.gov/me/hr/OEE/FEVS.htm",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:34:31.016Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Single Sign On (SSO)",
-            "description": "Single sign-on (SSO) is a session and user authentication service that permits a user to use one set of login credentials -- for example, a username and password -- to access multiple applications. SSO can be used by enterprises, small and midsize organizations, and individuals to ease the management of multiple credentials.",
-            "modified": "2024-09-23T12:50:42.741Z",
-            "accessLevel": "public",
-            "identifier": "OASAM OCIO-25-012:044-257",
-            "landingPage": "https://usdol.sharepoint.com/sites/OASAM-OCIO-ICAM/SitePages/Single%20Sign%20On%20Application%20List%20for%20DOL,%20OIG,%20and%20BLS.aspx?xsdata=MDV8MDF8fGI1N2RmNWM5ZmRjMjRjNWEwZTA5MDhkYmNiMzBmY2I3fDc1YTYzMDU0NzIwNDRlMGM5MTI2YWRhYjk3MWQ0YWNhfDB8MHw2MzgzMjcxODM0NjE3ODEwMDF8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxMMk5vWVhSekx6RTVPakZpTmpabFpEVmlMVFZtWm1JdE5HRXdZaTA1T0RCa0xUZ3pOamhpTVdKbFptUmxNbDlpTmpOaFkyVXlaUzB4TkRCakxUUTFPVGN0WVdVMlpTMDJNRFkyTURFeE9XTm1OMkpBZFc1eExtZGliQzV6Y0dGalpYTXZiV1Z6YzJGblpYTXZNVFk1TnpFeU1UVTBOVGd3TVE9PXw3NTczN2M2ZmVjOWU0ODdjMGUwOTA4ZGJjYjMwZmNiN3w5YzNkOGE4MTc3NTE0NjgyOGE1ZjcxNTFlMDM5ZGM4OQ%3d%3d&sdata=UnVDd1owQVpWNDQ3OTUzdXFmakFzYUlabUVna3I4UVM3NlFCNml4dC85VT0%3d&ovuser=75a63054-7204-4e0c-9126-adab971d4aca%2cHelmy.Amer.S%40dol.gov&SafelinksUrl=https%3a%2f%2fusdol.sharepoint.com%2fsites%2fOASAM-OCIO-ICAM%2fSitePages%2fSingle%2520Sign%2520On%2520Application%2520List%2520for%2520DOL%2c%2520OIG%2c%2520and%2520BLS.aspx&OR=Teams-HL&CT=1697121626662&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMzA5MDExMjI3OCIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D",
-            "rights": "true",
-            "spatial": "location characteristics",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -18747,37 +18725,35 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "title": "FEVS"
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
                 "fn": "Amer Helmy",
                 "hasEmail": "mailto:helmy.amer.s@dol.gov"
             },
+            "description": "Single sign-on (SSO) is a session and user authentication service that permits a user to use one set of login credentials -- for example, a username and password -- to access multiple applications. SSO can be used by enterprises, small and midsize organizations, and individuals to ease the management of multiple credentials.",
+            "identifier": "OASAM OCIO-25-012:044-257",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://usdol.sharepoint.com/sites/OASAM-OCIO-ICAM/SitePages/Single%20Sign%20On%20Application%20List%20for%20DOL,%20OIG,%20and%20BLS.aspx?xsdata=MDV8MDF8fGI1N2RmNWM5ZmRjMjRjNWEwZTA5MDhkYmNiMzBmY2I3fDc1YTYzMDU0NzIwNDRlMGM5MTI2YWRhYjk3MWQ0YWNhfDB8MHw2MzgzMjcxODM0NjE3ODEwMDF8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxMMk5vWVhSekx6RTVPakZpTmpabFpEVmlMVFZtWm1JdE5HRXdZaTA1T0RCa0xUZ3pOamhpTVdKbFptUmxNbDlpTmpOaFkyVXlaUzB4TkRCakxUUTFPVGN0WVdVMlpTMDJNRFkyTURFeE9XTm1OMkpBZFc1eExtZGliQzV6Y0dGalpYTXZiV1Z6YzJGblpYTXZNVFk1TnpFeU1UVTBOVGd3TVE9PXw3NTczN2M2ZmVjOWU0ODdjMGUwOTA4ZGJjYjMwZmNiN3w5YzNkOGE4MTc3NTE0NjgyOGE1ZjcxNTFlMDM5ZGM4OQ%3d%3d&sdata=UnVDd1owQVpWNDQ3OTUzdXFmakFzYUlabUVna3I4UVM3NlFCNml4dC85VT0%3d&ovuser=75a63054-7204-4e0c-9126-adab971d4aca%2cHelmy.Amer.S%40dol.gov&SafelinksUrl=https%3a%2f%2fusdol.sharepoint.com%2fsites%2fOASAM-OCIO-ICAM%2fSitePages%2fSingle%2520Sign%2520On%2520Application%2520List%2520for%2520DOL%2c%2520OIG%2c%2520and%2520BLS.aspx&OR=Teams-HL&CT=1697121626662&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMzA5MDExMjI3OCIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T12:50:42.741Z",
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
-            "title": "KnowBe4",
-            "description": "The Department is required by OMB to provide the total number of users that successfully passed the Department\u2019s quarterly phishing exercise and is collected as a part of OMB\u2019s CIO FISMA metric reporting process.",
-            "modified": "2024-09-23T13:02:36.270Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM OCIO-25-012:044-251",
-            "rights": "private",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -18786,36 +18762,38 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "true",
+            "spatial": "location characteristics",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Single Sign On (SSO)"
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
                 "fn": "Emery Dussold",
                 "hasEmail": "mailto:dussold.emery@dol.gov"
             },
+            "description": "The Department is required by OMB to provide the total number of users that successfully passed the Department\u2019s quarterly phishing exercise and is collected as a part of OMB\u2019s CIO FISMA metric reporting process.",
+            "identifier": "OASAM OCIO-25-012:044-251",
             "keyword": [
                 "OASAM",
                 "OCIO"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-09-23T13:02:36.270Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Department of Labor USA Staffing",
-            "description": "USA Staffing fully automates the hiring process for recruiting, assessing, evaluating, certifying, selecting, and onboarding quality candidates for Federal positions.",
-            "modified": "2024-09-23T13:46:10.146Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM-25-012:044-682",
-            "landingPage": "https://signin.usastaffing.gov/Account/SignIn?",
-            "license": "https://opensource.org/licenses/MIT-0",
-            "rights": "private",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -18824,12 +18802,23 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "title": "KnowBe4"
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
+            "description": "USA Staffing fully automates the hiring process for recruiting, assessing, evaluating, certifying, selecting, and onboarding quality candidates for Federal positions.",
+            "identifier": "OASAM-25-012:044-682",
             "keyword": [
                 "Applications",
                 "OASAM",
@@ -18838,116 +18827,101 @@
                 "Vacancies",
                 "certificates"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://signin.usastaffing.gov/Account/SignIn?",
+            "language": [
+                "en-US"
             ],
+            "license": "https://opensource.org/licenses/MIT-0",
+            "modified": "2024-09-23T13:46:10.146Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Map: Equal Pay and Pay Transparency Protections",
-            "description": "This map provides information on federal and state-level equal pay and pay transparency protections for workers. More information about protection, coverage and available remedies are listed in an accompanying table at the link provided.",
-            "modified": "2024-06-05T12:45:59.115Z",
-            "accessLevel": "public",
-            "identifier": "WB-12-012:038-549",
-            "dataQuality": true,
-            "describedBy": "https://www.dol.gov/agencies/wb/equal-pay-protections",
-            "describedByType": "text/html",
-            "issued": "2023-03-01",
-            "landingPage": "https://www.dol.gov/agencies/wb/equal-pay-protections",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Women's Bureau",
+                "name": "Office of the Assistant Secretary for Administration and Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "title": "Department of Labor USA Staffing"
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
+            "dataQuality": true,
+            "describedBy": "https://www.dol.gov/agencies/wb/equal-pay-protections",
+            "describedByType": "text/html",
+            "description": "This map provides information on federal and state-level equal pay and pay transparency protections for workers. More information about protection, coverage and available remedies are listed in an accompanying table at the link provided.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/wb/equal-pay-protections",
-                    "title": "Map: Equal Pay and Pay Transparency Protections",
+                    "conformsTo": "https://www.dol.gov/agencies/wb/equal-pay-protections",
                     "description": "This map provides information on federal and state-level equal pay and pay transparency protections for workers. More information about protection, coverage and available remedies are listed in an accompanying table at the link provided.",
-                    "conformsTo": "https://www.dol.gov/agencies/wb/equal-pay-protections"
+                    "title": "Map: Equal Pay and Pay Transparency Protections"
                 }
             ],
+            "identifier": "WB-12-012:038-549",
+            "issued": "2023-03-01",
             "keyword": [
                 "WB",
                 "equal pay"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/wb/equal-pay-protections",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-06-05T12:45:59.115Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Complaint Tracking and Reporting System - OCAP Module",
-            "description": "DOL's internal computerized system used by Civil Rights Center management and employees to record and track EEO complaints and compliance reviews.",
-            "modified": "2025-01-06T12:49:51.711Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM-CRC-25-012:044-231",
-            "rights": "private",
-            "spatial": "location characteristics, addresses",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of the Assistant Secretary for Administration and Management",
+                "name": "Women's Bureau",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Assistant Secretary for Administration and Management"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "true",
+            "title": "Map: Equal Pay and Pay Transparency Protections"
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
                 "fn": "Miguel Escobar",
                 "hasEmail": "mailto:escobar.miguel@dol.gov"
             },
+            "description": "DOL's internal computerized system used by Civil Rights Center management and employees to record and track EEO complaints and compliance reviews.",
+            "identifier": "OASAM-CRC-25-012:044-231",
             "keyword": [
                 "CRC",
                 "OASAM"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2025-01-06T12:49:51.711Z",
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
-            "title": "Complaint Tracking and Reporting System - All Modules",
-            "description": "DOL's internal computerized system used by Civil Rights Center management and employees to record and track EEO complaints (internal and external) and compliance reviews.",
-            "modified": "2025-01-06T12:49:24.236Z",
-            "accessLevel": "non-public",
-            "identifier": "OASAM-CRC-25-012:044-230",
-            "landingPage": "https://cmp.dol.gov/suite/sites/ctrs-tl7",
-            "rights": "private",
-            "spatial": "location characteristics, addresses",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Assistant Secretary for Administration and Management",
@@ -18956,54 +18930,69 @@
                     "name": "Office of the Assistant Secretary for Administration and Management"
                 }
             },
+            "rights": "private",
+            "spatial": "location characteristics, addresses",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Complaint Tracking and Reporting System - OCAP Module"
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
                 "fn": "Lissette Gean",
                 "hasEmail": "mailto:gean.lissette@dol.gov"
             },
+            "description": "DOL's internal computerized system used by Civil Rights Center management and employees to record and track EEO complaints (internal and external) and compliance reviews.",
+            "identifier": "OASAM-CRC-25-012:044-230",
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
+            "modified": "2025-01-06T12:49:24.236Z",
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
-            "title": "NAWS Public Access Data 1989-2022",
-            "description": "The NAWS Public Access Data contains 357 variables regarding the demographics, employment, and health characteristics of U.S. crop workers.  Like the restricted-use file, there are 73,909 observations from interviews that were administered in fiscal years 1989-2022.",
-            "modified": "2024-12-26T19:45:58.874Z",
-            "accessLevel": "public",
-            "identifier": "ETA-012:05-12:017-706",
-            "describedBy": "https://www.dol.gov/agencies/eta/national-agricultural-workers-survey/data",
-            "describedByType": "text/html",
-            "landingPage": "https://www.dol.gov/agencies/eta/national-agricultural-workers-survey/data",
-            "rights": "true",
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
+            "rights": "private",
+            "spatial": "location characteristics, addresses",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Complaint Tracking and Reporting System - All Modules"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Emily Finchum",
                 "hasEmail": "mailto:finchum.emily.a@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/national-agricultural-workers-survey/data",
+            "describedByType": "text/html",
+            "description": "The NAWS Public Access Data contains 357 variables regarding the demographics, employment, and health characteristics of U.S. crop workers.  Like the restricted-use file, there are 73,909 observations from interviews that were administered in fiscal years 1989-2022.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19011,44 +19000,46 @@
                     "title": "National Agricultural Workers Survey Public Data"
                 }
             ],
+            "identifier": "ETA-012:05-12:017-706",
             "keyword": [
                 "ETA",
                 "NAWS",
                 "NAWSPAD",
                 "National Agricultural Workers Survey"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/national-agricultural-workers-survey/data",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-26T19:45:58.874Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Apprenticeship Grantee Quarterly Performance Data",
-            "description": "This dataset contains Quarterly Performance Report data (QPR) for state and competitive apprenticeship grants beginning 7/1/2019 or later.  The dataset contains  aggregate-level  data on the number of new participants and others impacted by the grant, services provided, and performance outcomes.  Data is aggregated and summarized at the grantee level on a quarterly basis.",
-            "modified": "2024-07-11T16:19:05.046Z",
-            "accessLevel": "non-public",
-            "identifier": "ETA-5-012:017-541",
-            "rights": "Data is not public.",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Employment and Training Administration"
                 }
             },
+            "rights": "true",
+            "title": "NAWS Public Access Data 1989-2022"
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
                 "fn": "Shelia Lewis",
                 "hasEmail": "mailto:Lewis.Shelia.F@DOL.GOV"
             },
+            "description": "This dataset contains Quarterly Performance Report data (QPR) for state and competitive apprenticeship grants beginning 7/1/2019 or later.  The dataset contains  aggregate-level  data on the number of new participants and others impacted by the grant, services provided, and performance outcomes.  Data is aggregated and summarized at the grantee level on a quarterly basis.",
+            "identifier": "ETA-5-012:017-541",
             "keyword": [
                 "apprentice",
                 "eta",
@@ -19056,41 +19047,39 @@
                 "registered apprenticeship",
                 "training"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-07-11T16:19:05.046Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Agricultural Workers Survey Public Access Data (NAWSPAD)",
-            "description": "The NAWSPAD file contains 232 questionnaire variables and 125 summary and analytic variables from 71,311 in-person interviews that were administered in 48 states during federal fiscal years 1989-2020 (October 1, 1988, to September 30, 2020). Users can analyze these data for the United States and six regions. California is the only single-state region. County-level data are not available.",
-            "modified": "2024-12-26T19:45:11.857Z",
-            "accessLevel": "public",
-            "identifier": "ETA-012:05-12:017-704",
-            "describedBy": "https://www.dol.gov/agencies/eta/national-agricultural-workers-survey/data",
-            "describedByType": "text/html",
-            "landingPage": "https://www.dol.gov/agencies/eta/national-agricultural-workers-survey/data",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Employment and Training Administration"
+                    "name": "Department of Labor"
                 }
             },
+            "rights": "Data is not public.",
+            "title": "Apprenticeship Grantee Quarterly Performance Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Emily Finchum",
                 "hasEmail": "mailto:finchum.emily.a@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/national-agricultural-workers-survey/data",
+            "describedByType": "text/html",
+            "description": "The NAWSPAD file contains 232 questionnaire variables and 125 summary and analytic variables from 71,311 in-person interviews that were administered in 48 states during federal fiscal years 1989-2020 (October 1, 1988, to September 30, 2020). Users can analyze these data for the United States and six regions. California is the only single-state region. County-level data are not available.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19098,30 +19087,20 @@
                     "title": "NAWSPAD"
                 }
             ],
+            "identifier": "ETA-012:05-12:017-704",
             "keyword": [
                 "Agriculture",
                 "ETA",
                 "farm labor"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/national-agricultural-workers-survey/data",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-26T19:45:11.857Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Apprenticeship Enterprise Data Platform (EDP)",
-            "description": "A Snowflake-hosted (cloud-based) Enterprise Data Platform that ingests RAPIDS data daily and arranges it through varying levels of data schema. The underlying data can be queried through a Tableau connection or a Tableau Server and used to power live data visualizations for OA staff.",
-            "modified": "2024-12-26T19:38:52.655Z",
-            "accessLevel": "non-public",
-            "identifier": "ETA-012:05-12:017-702",
-            "rights": "NA",
-            "spatial": "Address",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration",
@@ -19130,12 +19109,23 @@
                     "name": "Employment and Training Administration"
                 }
             },
+            "rights": "true",
+            "title": "National Agricultural Workers Survey Public Access Data (NAWSPAD)"
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
                 "fn": "Alex Jordan",
                 "hasEmail": "mailto:jordan.alexander@dol.gov"
             },
+            "description": "A Snowflake-hosted (cloud-based) Enterprise Data Platform that ingests RAPIDS data daily and arranges it through varying levels of data schema. The underlying data can be queried through a Tableau connection or a Tableau Server and used to power live data visualizations for OA staff.",
+            "identifier": "ETA-012:05-12:017-702",
             "keyword": [
                 "EDP",
                 "Enterprise Data Platform",
@@ -19144,39 +19134,39 @@
                 "Tableau",
                 "apprenticeship"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-26T19:38:52.655Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Employment Navigators and Partnership Program (ENPP) Locations List",
-            "description": "This dataset is a list of locations for the Employment Navigators and Partnership Program (ENPP) administered by the US Department of Labor Veterans' Employment and Training Service (VETS) for fiscal year (FY) 2024.",
-            "modified": "2024-12-17T14:12:16.376Z",
-            "accessLevel": "public",
-            "identifier": "VETS-29-012:041-700",
-            "landingPage": "https://www.dol.gov/agencies/vets/programs/tap/employment-navigator-partnership",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Veterans\u2019 Employment and Training Service",
+                "name": "Employment and Training Administration",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Labor"
+                    "name": "Employment and Training Administration"
                 }
             },
+            "rights": "NA",
+            "spatial": "Address",
+            "title": "Apprenticeship Enterprise Data Platform (EDP)"
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
                 "fn": "DOL-VETS-ENPP",
                 "hasEmail": "mailto:TAPPartnerships@dol.gov"
             },
+            "description": "This dataset is a list of locations for the Employment Navigators and Partnership Program (ENPP) administered by the US Department of Labor Veterans' Employment and Training Service (VETS) for fiscal year (FY) 2024.",
+            "identifier": "VETS-29-012:041-700",
             "keyword": [
                 "ENPP",
                 "Employment Navigators",
@@ -19187,52 +19177,52 @@
                 "transitioning service member",
                 "vets"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/vets/programs/tap/employment-navigator-partnership",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-17T14:12:16.376Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://www.dol.gov/sites/dolgov/files/VETS/files/tap/InstallationToolkit20211015.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual State Obligations and Quarterly State Expenditures",
-            "description": "Workforce Innovation and Opportunity Act (WIOA) State and Outlying Areas Quarterly Spending Summary for Adult, Youth, and Dislocated Worker by Program - State and Local spending combined, and by Report Activity - State spending separated from Local spending. WIOA annual obligation reports are also posted in the same formats. The data is extracted from the ETA-9130 Financial Reports and aggregated in user friendly summary reports. Data is available on ETA\u2019s website at https://www.dol.gov/agencies/eta/budget/spending-updates/quarterly and https://www.dol.gov/agencies/eta/budget/spending-updates/annual.",
-            "modified": "2024-12-26T19:39:52.268Z",
-            "accessLevel": "public",
-            "identifier": "ETA-012:05-12:017-701",
-            "describedBy": "https://www.dol.gov/agencies/eta/budget",
-            "describedByType": "text/html",
-            "landingPage": "https://www.dol.gov/agencies/eta/budget",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Employment and Training Administration",
+                "name": "Veterans\u2019 Employment and Training Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Employment and Training Administration"
+                    "name": "Department of Labor"
                 }
             },
+            "references": [
+                "https://www.dol.gov/sites/dolgov/files/VETS/files/tap/InstallationToolkit20211015.pdf"
+            ],
+            "rights": "true",
+            "title": "Employment Navigators and Partnership Program (ENPP) Locations List"
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
                 "fn": "Anita Harvey",
                 "hasEmail": "mailto:harvey.anita@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/budget",
+            "describedByType": "text/html",
+            "description": "Workforce Innovation and Opportunity Act (WIOA) State and Outlying Areas Quarterly Spending Summary for Adult, Youth, and Dislocated Worker by Program - State and Local spending combined, and by Report Activity - State spending separated from Local spending. WIOA annual obligation reports are also posted in the same formats. The data is extracted from the ETA-9130 Financial Reports and aggregated in user friendly summary reports. Data is available on ETA\u2019s website at https://www.dol.gov/agencies/eta/budget/spending-updates/quarterly and https://www.dol.gov/agencies/eta/budget/spending-updates/annual.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dol.gov/agencies/eta/budget",
-                    "title": "ETA-9130 Financial Reports",
-                    "description": "The data is extracted from the ETA-9130 Financial Reports and aggregated in user friendly summary reports. Data is available on ETA\u2019s website at https://www.dol.gov/agencies/eta/budget/spending-updates/quarterly and https://www.dol.gov/agencies/eta/budget/spending-updates/annual."
+                    "description": "The data is extracted from the ETA-9130 Financial Reports and aggregated in user friendly summary reports. Data is available on ETA\u2019s website at https://www.dol.gov/agencies/eta/budget/spending-updates/quarterly and https://www.dol.gov/agencies/eta/budget/spending-updates/annual.",
+                    "title": "ETA-9130 Financial Reports"
                 }
             ],
+            "identifier": "ETA-012:05-12:017-701",
             "keyword": [
                 "ETA 9130 data",
                 "financial data",
@@ -19243,27 +19233,14 @@
                 "wioa annual state obligation reports",
                 "wioa quarterly state expenditure reports"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/budget",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-12-26T19:39:52.268Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Workforce Individual Performance Record Data",
-            "description": "Workforce Individual Performance Record Data: The Workforce Individual Performance Record Data is data ETA collects from grantees on a quarterly basis via form ETA-9172 (DOL Participant Individual Record Layout (PIRL)). This dataset includes information on the WIOA Title I Adult, Dislocated Worker, Youth, WIOA Title III Wagner-Peyser Employment Service, Trade Adjustment Assistance, National Dislocated Worker Grants, National Farmworker Jobs Program (Career Services and Training), National Farmworker Jobs Program (Housing), Indian and Native American Program (Adult), Indian and Native American Program (Youth), Reentry Employment Opportunities (REO) (Adult), Reentry Employment Opportunities (REO) (Youth), YouthBuild, H-1B, Job Corps, Senior Community Service Employment Program (SCSEP), Registered Apprenticeship Grants Program, and the Veteran\u2019s Employment Service\u2019s Jobs for Veterans State Grant programs for performance accountability purposes. The participant individual record data include data on the individual's characteristics, types of services received, and outcomes attained as a result of participating in the program for each of these programs. The individual records from programs with state grantees include Wage Data provided by state UI Offices and through the SWIS Agreement. For some of these programs, data is available in aggregate and modified public use files on ETA\u2019s website (https://www.dol.gov/agencies/eta/performance/results/national).",
-            "modified": "2025-01-08T20:43:59.494Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:016-511",
-            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/national",
-            "describedByType": "text/html",
-            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/national",
-            "rights": "NA",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration",
@@ -19272,12 +19249,24 @@
                     "name": "Employment and Training Administration"
                 }
             },
+            "rights": "true",
+            "title": "Annual State Obligations and Quarterly State Expenditures"
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
                 "fn": "Cesar Acevedo",
                 "hasEmail": "mailto:Acevedo.Cesar@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/national",
+            "describedByType": "text/html",
+            "description": "Workforce Individual Performance Record Data: The Workforce Individual Performance Record Data is data ETA collects from grantees on a quarterly basis via form ETA-9172 (DOL Participant Individual Record Layout (PIRL)). This dataset includes information on the WIOA Title I Adult, Dislocated Worker, Youth, WIOA Title III Wagner-Peyser Employment Service, Trade Adjustment Assistance, National Dislocated Worker Grants, National Farmworker Jobs Program (Career Services and Training), National Farmworker Jobs Program (Housing), Indian and Native American Program (Adult), Indian and Native American Program (Youth), Reentry Employment Opportunities (REO) (Adult), Reentry Employment Opportunities (REO) (Youth), YouthBuild, H-1B, Job Corps, Senior Community Service Employment Program (SCSEP), Registered Apprenticeship Grants Program, and the Veteran\u2019s Employment Service\u2019s Jobs for Veterans State Grant programs for performance accountability purposes. The participant individual record data include data on the individual's characteristics, types of services received, and outcomes attained as a result of participating in the program for each of these programs. The individual records from programs with state grantees include Wage Data provided by state UI Offices and through the SWIS Agreement. For some of these programs, data is available in aggregate and modified public use files on ETA\u2019s website (https://www.dol.gov/agencies/eta/performance/results/national).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19285,6 +19274,7 @@
                     "title": "National Performance Data"
                 }
             ],
+            "identifier": "ETA-5-012:016-511",
             "keyword": [
                 "JVSG",
                 "RA",
@@ -19307,27 +19297,14 @@
                 "workforce system",
                 "youthbuild"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/national",
+            "language": [
+                "en-US"
             ],
+            "modified": "2025-01-08T20:43:59.494Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Workforce Programs Quarterly Performance Report (QPR) Data",
-            "description": "Workforce Programs Quarterly Performance Report (QPR) Data: The Programs Quarterly Performance Report  Data is data ETA collects from grantees on a quarterly basis via form ETA-9173 (Quarterly Performance Report (QPR). These data are aggregate values that are generated by ETA in the Workforce Integrated Performance System (WIPS) using individual record data reported by grantees using the DOL PIRL (ETA-9172). This dataset includes information on the WIOA Title I Adult, Dislocated Worker, Youth, WIOA Title III Wagner-Peyser Employment Service, Trade Adjustment Assistance, National Dislocated Worker Grants, National Farmworker Jobs Program (Career Services and Training), National Farmworker Jobs Program (Housing), Indian and Native American Program (Adult), Indian and Native American Program (Youth), Reentry Employment Opportunities (REO) (Adult), Reentry Employment Opportunities (REO) (Youth), YouthBuild, H-1B, Job Corps, Senior Community Service Employment Program (SCSEP), Registered Apprenticeship Grants Program, and the Veteran\u2019s Employment Service\u2019s Jobs for Veterans State Grant programs for performance accountability purposes. The QPR data include data on the demographics, types of services received, and outcomes of the participants served by the grant, for each of these programs. For some of these programs, some of these data is available by grant on ETA\u2019s website (https://www.dol.gov/agencies/eta/performance/results/national).",
-            "modified": "2025-01-08T20:41:54.675Z",
-            "accessLevel": "restricted public",
-            "identifier": "ETA-5-012:016-510",
-            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/national",
-            "describedByType": "text/html",
-            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/national",
-            "rights": "NA",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Employment and Training Administration",
@@ -19336,12 +19313,24 @@
                     "name": "Employment and Training Administration"
                 }
             },
+            "rights": "NA",
+            "title": "Workforce Individual Performance Record Data"
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
                 "fn": "Cesar Acevedo",
                 "hasEmail": "mailto:Acevedo.Cesar@dol.gov"
             },
+            "describedBy": "https://www.dol.gov/agencies/eta/performance/results/national",
+            "describedByType": "text/html",
+            "description": "Workforce Programs Quarterly Performance Report (QPR) Data: The Programs Quarterly Performance Report  Data is data ETA collects from grantees on a quarterly basis via form ETA-9173 (Quarterly Performance Report (QPR). These data are aggregate values that are generated by ETA in the Workforce Integrated Performance System (WIPS) using individual record data reported by grantees using the DOL PIRL (ETA-9172). This dataset includes information on the WIOA Title I Adult, Dislocated Worker, Youth, WIOA Title III Wagner-Peyser Employment Service, Trade Adjustment Assistance, National Dislocated Worker Grants, National Farmworker Jobs Program (Career Services and Training), National Farmworker Jobs Program (Housing), Indian and Native American Program (Adult), Indian and Native American Program (Youth), Reentry Employment Opportunities (REO) (Adult), Reentry Employment Opportunities (REO) (Youth), YouthBuild, H-1B, Job Corps, Senior Community Service Employment Program (SCSEP), Registered Apprenticeship Grants Program, and the Veteran\u2019s Employment Service\u2019s Jobs for Veterans State Grant programs for performance accountability purposes. The QPR data include data on the demographics, types of services received, and outcomes of the participants served by the grant, for each of these programs. For some of these programs, some of these data is available by grant on ETA\u2019s website (https://www.dol.gov/agencies/eta/performance/results/national).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19349,6 +19338,7 @@
                     "title": "National Performance Data"
                 }
             ],
+            "identifier": "ETA-5-012:016-510",
             "keyword": [
                 "JVSG",
                 "REO",
@@ -19371,15 +19361,25 @@
                 "workforce system",
                 "youthbuild"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.dol.gov/agencies/eta/performance/results/national",
+            "language": [
+                "en-US"
             ],
+            "modified": "2025-01-08T20:41:54.675Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Employment and Training Administration",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Employment and Training Administration"
                 }
-    ]
+            },
+            "rights": "NA",
+            "title": "Workforce Programs Quarterly Performance Report (QPR) Data"
+        }
+    ],
+    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
 }
```

