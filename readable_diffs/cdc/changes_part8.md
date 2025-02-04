# Change History for cdc.json (Part 8)

### Changes from 9cd27cf to 452e48f (Part 8/8)
**Author:** Automated

**Date:** 2025-02-03 20:01:08+00:00

**Message:** Updated data: Mon Feb  3 20:01:08 UTC 2025

```diff
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wrev-kwxu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/wrev-kwxu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wrev-kwxu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wrev-kwxu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Pa/wrev-kwxu",
+            "identifier": "https://data.cdc.gov/api/views/wrev-kwxu",
+            "issued": "2023-07-18",
+            "keyword": [
+                "art",
+                "assisted reproductive technology",
+                "clinic",
+                "fertility",
+                "infertility",
+                "services",
+                "success rates"
+            ],
+            "landingPage": "https://www.cdc.gov/art/index.html",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Assisted Reproductive Technology (ART)"
-            ]
+            ],
+            "title": "2022 Final Assisted Reproductive Technology (ART) Patient and Cycle Characteristics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/wrrd-u9wx",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "meningococcal disease",
-                "nedss",
-                "netss",
-                "nndss",
-                "other serogroups",
-                "unknown serogroup",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/wrrd-u9wx",
             "description": "NNDSS - TABLE 1X. Meningococcal disease, Other serogroups to Meningococcal disease, Unknown serogroup - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1X. Meningococcal disease, Other serogroups to Meningococcal disease, Unknown serogroup",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74177,43 +74297,96 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/wrrd-u9wx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wrrd-u9wx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wrrd-u9wx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/wrrd-u9wx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wrrd-u9wx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wrrd-u9wx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/wrrd-u9wx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wrrd-u9wx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wrrd-u9wx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wrrd-u9wx",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "meningococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "other serogroups",
+                "unknown serogroup",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/wrrd-u9wx",
+            "modified": "2022-02-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1X. Meningococcal disease, Other serogroups to Meningococcal disease, Unknown serogroup"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "references": [
-                "https://chronicdata.cdc.gov/d/5amh-5sx3"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/Behavioral-Risk-Factor-Data-Tobacco-Use-2011-to-pr/wsas-xwh5",
+            "description": "2011-2019. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. BRFSS Survey Data. The BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. The data for the STATE System were extracted from the annual BRFSS surveys from participating states. Tobacco topics included are cigarette and e-cigarette use prevalence by demographics, cigarette and e-cigarette use frequency, and quit attempts. NOTE: these data are not to be compared with BRFSS data collected 2010 and prior, as the methodologies were changed. Please refer to the FAQs / Methodology sections for more details.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/wsas-xwh5/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/wsas-xwh5/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/wsas-xwh5/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wsas-xwh5",
+            "issued": "2025-01-31",
             "keyword": [
                 "adult",
                 "age",
@@ -74240,87 +74413,44 @@
                 "sex",
                 "smoker",
                 "smoking",
-                "smoking status",
-                "some days",
-                "state system",
-                "surveillance",
-                "survey",
-                "tobacco",
-                "tobacco use"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "OSHData Support",
-                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/wsas-xwh5",
-            "description": "2011-2019. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. BRFSS Survey Data. The BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. The data for the STATE System were extracted from the annual BRFSS surveys from participating states. Tobacco topics included are cigarette and e-cigarette use prevalence by demographics, cigarette and e-cigarette use frequency, and quit attempts. NOTE: these data are not to be compared with BRFSS data collected 2010 and prior, as the methodologies were changed. Please refer to the FAQs / Methodology sections for more details.",
-            "title": "Behavioral Risk Factor Data: Tobacco Use (2011 to present)",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/wsas-xwh5/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/wsas-xwh5/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/wsas-xwh5/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
+                "smoking status",
+                "some days",
+                "state system",
+                "surveillance",
+                "survey",
+                "tobacco",
+                "tobacco use"
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/Behavioral-Risk-Factor-Data-Tobacco-Use-2011-to-pr/wsas-xwh5",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://chronicdata.cdc.gov/d/5amh-5sx3"
+            ],
             "theme": [
                 "Survey Data"
-            ]
+            ],
+            "title": "Behavioral Risk Factor Data: Tobacco Use (2011 to present)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/wtvk-6zfr",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division, Allergy and Clinical Immunology Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/wtvk-6zfr",
             "description": "SARS-CoV-2 can be spread by droplets and aerosols expelled by infected people when they cough, talk, sing, or exhale. To reduce exposure to these droplets and aerosols while indoors, CDC recommends measures including physical distancing, universal mask wearing, and room ventilation. Ventilation systems can be supplemented with portable air cleaners to remove infectious material from the air more quickly and provide greater protection. We conducted a case study using respiratory simulators to examine the efficacy of portable High Efficiency Particulate Air (HEPA) air cleaners and universal masking at reducing exposure to simulated exhaled aerosol particles from an infected meeting participant in a conference room. We found that, in a room with good air mixing, the use of two HEPA air cleaners meeting the EPA recommended Clean Air Delivery Rate (CADR) reduced the overall exposure by up to 65%, and that the combination of the HEPA air cleaners and universal masking reduced exposure by up to 90%. The air cleaners were most effective when they were close to the aerosol source. Our results demonstrate that portable HEPA cleaners can be an effective method to reduce exposure to airborne particles while meeting indoors, especially in combination with universal masking.",
-            "title": "Efficacy of Portable Air Cleaners and Masking for Reducing Indoor Exposure to Simulated Exhaled SARS-CoV-2 Aerosols \u2014 United States, 2021",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74328,40 +74458,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wtvk-6zfr",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/wtvk-6zfr",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Efficacy of Portable Air Cleaners and Masking for Reducing Indoor Exposure to Simulated Exhaled SARS-CoV-2 Aerosols \u2014 United States, 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-09",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-08-05",
-            "keyword": [
-                "covid-19 vaccination",
-                "iis",
-                "immunization information system"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/wtw5-4wi3",
             "description": "Monthly Cumulative Percent of Persons Who Received 1+ updated 2023-24 COVID-19 Vaccination Doses by Age Group and Jurisdiction\n\n\u2022 Estimated Number of COVID-19 vaccinations among children 6 months\u201317 years and adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems (IIS) data, submitted from jurisdictions to CDC monthly in aggregate by age group.\n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19. (https://www.cdc.gov/coronavirus/2019-ncov/vaccines/stay-up-to-date.html)",
-            "title": "Monthly Cumulative Number and Percent of Persons Who Received 1+ updated 2023-24 COVID-19 Vaccination Doses by Age Group and Jurisdiction, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74369,48 +74494,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/wtw5-4wi3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wtw5-4wi3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wtw5-4wi3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/wtw5-4wi3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wtw5-4wi3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wtw5-4wi3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/wtw5-4wi3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wtw5-4wi3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wtw5-4wi3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Jurisdictions - States, District of Columbia, Islands, and US cities",
+            "identifier": "https://data.cdc.gov/api/views/wtw5-4wi3",
+            "issued": "2024-02-09",
+            "keyword": [
+                "covid-19 vaccination",
+                "iis",
+                "immunization information system"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2024-08-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
+            },
+            "spatial": "Jurisdictions - States, District of Columbia, Islands, and US cities",
+            "temporal": "2023-2024",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Monthly Cumulative Number and Percent of Persons Who Received 1+ updated 2023-24 COVID-19 Vaccination Doses by Age Group and Jurisdiction, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/ahcd/ahcd_questionnaires.htm",
+            "accrualPeriodicity": "Dataset will no longer be updated.",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm\u201d",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:ambcare@cdc.gov"
+            },
+            "describedBy": "Findings are based on a sample of visits to nonfederally employed office-based physicians who are primarily engaged in direct patient care. The sampling frame for NAMCS (core sample, not including CHC delivery sites) was composed of all physicians listed in the master files maintained by the AMA and AOA who met the following criteria: -- Office-based or hospital-employed, as defined by the AMA and AOA; -- Principally engaged in patient care activities; -- Nonfederally employed; -- Not in specialties of anesthesiology, pathology, or radiology -- Younger than 85 years of age at the time of the survey. Physicians whom the AMA classifies as \u201chospital-employed\u201d were added to the sampling frame starting with the 2014 NAMCS. This expansion of the NAMCS physician sampling frame is due to concerns that NAMCS was not covering visits made to office-based practices which are owned by hospitals, and to increases in reported hospital purchases of physician practices in recent years.",
+            "description": "The National Ambulatory Medical Care Survey (NAMCS) is a national survey designed to meet the need for objective, reliable information about the provision and use of ambulatory medical care services in the United States. Findings are based on a sample of visits to non-federally employed office-based physicians who are primarily engaged in direct patient care. Physicians in the specialties (including designated sub-specialties) of anesthesiology, pathology, and radiology are excluded from the survey. The survey was conducted annually from 1973 to 1981, again in 1985, and annually since 1989. \nData collection from the physician, rather than from the patient, provides an analytic base that expands information on ambulatory care collected through other NCHS surveys. Data about the physician and their practice characteristics are collected during a survey induction interview.\nFor survey years 1973 to 1991, there are two data files: one for patient visit data and a second for drug mention data. The second file is limited to those visits with mention of medication therapy. For the 1991 data, it is possible to link information on the drug file with information on the patient visit file. Beginning with the 1992 survey year through 2011, one main data file was produced annually that contains both patient visit and drug information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/userestricdt.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/wwei-z7f5",
+            "isPartOf": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
             "issued": "2023-11-21",
-            "@type": "dcat:Dataset",
-            "temporal": "1973, 1975-1981, 1985, 1989-2016, 2018-2019",
-            "modified": "2023-11-21",
             "keyword": [
                 "ambulatory-care",
                 "namcs",
@@ -74421,76 +74576,35 @@
                 "restricted",
                 "visit characteristics"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:ambcare@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/ahcd/ahcd_questionnaires.htm",
+            "modified": "2023-11-21",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/wwei-z7f5",
-            "description": "The National Ambulatory Medical Care Survey (NAMCS) is a national survey designed to meet the need for objective, reliable information about the provision and use of ambulatory medical care services in the United States. Findings are based on a sample of visits to non-federally employed office-based physicians who are primarily engaged in direct patient care. Physicians in the specialties (including designated sub-specialties) of anesthesiology, pathology, and radiology are excluded from the survey. The survey was conducted annually from 1973 to 1981, again in 1985, and annually since 1989. \nData collection from the physician, rather than from the patient, provides an analytic base that expands information on ambulatory care collected through other NCHS surveys. Data about the physician and their practice characteristics are collected during a survey induction interview.\nFor survey years 1973 to 1991, there are two data files: one for patient visit data and a second for drug mention data. The second file is limited to those visits with mention of medication therapy. For the 1991 data, it is possible to link information on the drug file with information on the patient visit file. Beginning with the 1992 survey year through 2011, one main data file was produced annually that contains both patient visit and drug information.",
-            "title": "National Ambulatory Medical Care Survey, Restricted data, 1973, 1975-1981, 1985, 1989-2016, 2018-2019",
-            "isPartOf": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/userestricdt.htm",
-                    "mediaType": "text/html"
-                }
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm\u201d",
             "spatial": "United States",
-            "describedBy": "Findings are based on a sample of visits to nonfederally employed office-based physicians who are primarily engaged in direct patient care. The sampling frame for NAMCS (core sample, not including CHC delivery sites) was composed of all physicians listed in the master files maintained by the AMA and AOA who met the following criteria: -- Office-based or hospital-employed, as defined by the AMA and AOA; -- Principally engaged in patient care activities; -- Nonfederally employed; -- Not in specialties of anesthesiology, pathology, or radiology -- Younger than 85 years of age at the time of the survey. Physicians whom the AMA classifies as \u201chospital-employed\u201d were added to the sampling frame starting with the 2014 NAMCS. This expansion of the NAMCS physician sampling frame is due to concerns that NAMCS was not covering visits made to office-based practices which are owned by hospitals, and to increases in reported hospital purchases of physician practices in recent years.",
-            "accrualPeriodicity": "Dataset will no longer be updated.",
+            "temporal": "1973, 1975-1981, 1985, 1989-2016, 2018-2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Ambulatory Medical Care Survey, Restricted data, 1973, 1975-1981, 1985, 1989-2016, 2018-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nhis/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-11-18",
-            "temporal": "2019/2023",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-22",
-            "keyword": [
-                "nhis",
-                "sdoh-access-to-health-care",
-                "sdoh-employment",
-                "sdoh-food-access",
-                "sdoh-food-insecurity",
-                "sdoh-higher-education",
-                "sdoh-high-school",
-                "sdoh-housing-stability",
-                "sdoh-poverty-income",
-                "sdoh-source-of-health-care",
-                "sdoh-use-of-health-care",
-                "sdoh-workplace",
-                "summary health statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/wxz7-ekz9",
             "description": "Interactive Summary Health Statistics for Children provide annual estimates of selected health topics for children under age 18 years based on final data from the National Health Interview Survey.",
-            "title": "NHIS Child Summary Health Statistics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74498,65 +74612,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/wxz7-ekz9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wxz7-ekz9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wxz7-ekz9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/wxz7-ekz9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wxz7-ekz9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wxz7-ekz9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/wxz7-ekz9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wxz7-ekz9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wxz7-ekz9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wxz7-ekz9",
+            "issued": "2021-11-18",
+            "keyword": [
+                "nhis",
+                "sdoh-access-to-health-care",
+                "sdoh-employment",
+                "sdoh-food-access",
+                "sdoh-food-insecurity",
+                "sdoh-higher-education",
+                "sdoh-high-school",
+                "sdoh-housing-stability",
+                "sdoh-poverty-income",
+                "sdoh-source-of-health-care",
+                "sdoh-use-of-health-care",
+                "sdoh-workplace",
+                "summary health statistics"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nhis/index.htm",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-07-22",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "temporal": "2019/2023",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NHIS Child Summary Health Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/wycc-ffia",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "cholera",
-                "coccidioidomycosis",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/wycc-ffia",
             "description": "NNDSS - Table 1H. Cholera to Coccidioidomycosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1H. Cholera to Coccidioidomycosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74564,66 +74685,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/wycc-ffia/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wycc-ffia/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wycc-ffia/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/wycc-ffia/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wycc-ffia/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wycc-ffia/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/wycc-ffia/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wycc-ffia/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wycc-ffia/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wycc-ffia",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "cholera",
+                "coccidioidomycosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/wycc-ffia",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1H. Cholera to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/wzwe-859x",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "ehrlichia ewingii infection",
-                "ehrlichiosis and anaplasmosis",
-                "giardiasis",
-                "nedss",
-                "netss",
-                "nndss",
-                "undetermined ehrlichiosis/anaplasmosis",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/wzwe-859x",
             "description": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74631,65 +74750,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/wzwe-859x/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wzwe-859x/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wzwe-859x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/wzwe-859x/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wzwe-859x/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wzwe-859x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/wzwe-859x/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/wzwe-859x/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/wzwe-859x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wzwe-859x",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "ehrlichia ewingii infection",
+                "ehrlichiosis and anaplasmosis",
+                "giardiasis",
+                "nedss",
+                "netss",
+                "nndss",
+                "undetermined ehrlichiosis/anaplasmosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/wzwe-859x",
+            "modified": "2022-02-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/x2iq-5477",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-04",
-            "keyword": [
-                "2018",
-                "acute",
-                "by type) c",
-                "hepatitis (viral",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/x2iq-5477",
             "description": "NNDSS - Table II. Hepatitis (viral, acute, by type) C - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\r\n \r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.  \r\n\r\n\u2020 For acute Hepatitis C, only confirmed cases were verified.",
-            "title": "NNDSS - Table II. Hepatitis (viral, acute, by type) C",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74697,49 +74817,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x2iq-5477/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x2iq-5477/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x2iq-5477/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/x2iq-5477/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x2iq-5477/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x2iq-5477/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x2iq-5477/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x2iq-5477/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x2iq-5477/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/x2iq-5477",
+            "issued": "2019-01-04",
+            "keyword": [
+                "2018",
+                "acute",
+                "by type) c",
+                "hepatitis (viral",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/x2iq-5477",
+            "modified": "2019-01-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Hepatitis (viral, acute, by type) C"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/x4dz-rafm",
-            "issued": "2024-07-24",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-24",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/x4dz-rafm",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74747,57 +74880,49 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x4dz-rafm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x4dz-rafm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x4dz-rafm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/x4dz-rafm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x4dz-rafm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x4dz-rafm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x4dz-rafm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x4dz-rafm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x4dz-rafm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/x4dz-rafm",
+            "issued": "2024-07-24",
+            "landingPage": "https://data.cdc.gov/d/x4dz-rafm",
+            "modified": "2024-07-24",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "dhds_dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/x66v-w5ka",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-05-04",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-04",
-            "keyword": [
-                "centers for disease control and prevention",
-                "environmental health",
-                "foodborne"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "The National Environmental Assessment Reporting System (NEARS)",
                 "hasEmail": "mailto:nears@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Cambridge University - Epidemiology and Infection"
-            },
-            "identifier": "https://data.cdc.gov/api/views/x66v-w5ka",
             "description": "This study examined relationships between foodborne outbreak investigation characteristics, such as the epidemiological methods used, and the success of the investigation, as determined by whether the investigation identified an outbreak agent (i.e., pathogen), food item, and contributing factor. This study used data from the Centers for Disease Control and Prevention\u2019s (CDC) National Outbreak Reporting System (NORS) and National Environmental Assessment Reporting System (NEARS) to identify outbreak investigation characteristics associated with outbreak investigation success. We identified investigation characteristics that increase the probability of successful outbreak investigations: a robust epidemiology investigation method; a thorough environmental assessment, as measured by number of visits to complete the assessment; and the collection of clinical samples. This research highlights the importance of a comprehensive outbreak investigation, which includes epidemiology, environmental health, and laboratory personnel working together to solve the outbreak.",
-            "title": "Characteristics Associated with Successful Foodborne Outbreak Investigations, NEARS 2014 - 2016",
-            "programCode": [
-                "009:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74805,106 +74930,156 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x66v-w5ka/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x66v-w5ka/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x66v-w5ka/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/x66v-w5ka/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x66v-w5ka/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x66v-w5ka/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x66v-w5ka/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x66v-w5ka/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x66v-w5ka/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/x66v-w5ka",
+            "issued": "2023-05-04",
+            "keyword": [
+                "centers for disease control and prevention",
+                "environmental health",
+                "foodborne"
+            ],
+            "landingPage": "https://data.cdc.gov/d/x66v-w5ka",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-05-04",
+            "programCode": [
+                "009:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Cambridge University - Epidemiology and Infection"
+            },
             "theme": [
                 "Foodborne, Waterborne, and Related Diseases"
-            ]
+            ],
+            "title": "Characteristics Associated with Successful Foodborne Outbreak Investigations, NEARS 2014 - 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "describedBy": "https://chronicdata.cdc.gov/Global-Survey-Data/Global-Tobacco-Surveillance-System-GTSS-Global-Hea/x6ag-8y7r",
+            "description": "2005-2011. The World Health Organization, CDC, and the Canadian Public Health Association, developed the GHPSS to collect data on tobacco use and cessation counseling among health professional students in all WHO member states. GHPSS is a standardized school-based survey of third-year students pursuing advanced degrees in dentistry, medicine, nursing, or pharmacy. It is conducted in schools during regular class sessions. GHPSS follows an anonymous, self-administered format for data collection. GHPSS uses a core questionnaire on demographics, prevalence of cigarette smoking and other tobacco use, knowledge and attitudes about tobacco use, exposure to secondhand smoke, desire for smoking cessation, and training received regarding patient counseling on smoking cessation techniques. Questionnaires are translated into local languages as needed. GHPSS has a standardized methodology for selecting participating schools and classes and uniform data processing procedures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x6ag-8y7r/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/x6ag-8y7r/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/x6ag-8y7r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/x6ag-8y7r/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/x6ag-8y7r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/x6ag-8y7r/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/x6ag-8y7r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/x6ag-8y7r",
+            "issued": "2025-01-31",
+            "keyword": [
+                "ghpss",
+                "gtss",
+                "osh",
+                "students",
+                "tobacco"
+            ],
             "landingPage": "http://www.cdc.gov/STATESystem",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "theme": [
+                "Global Survey Data"
+            ],
+            "title": "Global Tobacco Surveillance System (GTSS) - Global Health Professions Student Survey (GHPSS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "keyword": [
-                "ghpss",
-                "gtss",
-                "osh",
-                "students",
-                "tobacco"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
-                "fn": "OSHData Support",
-                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/x6ag-8y7r",
-            "description": "2005-2011. The World Health Organization, CDC, and the Canadian Public Health Association, developed the GHPSS to collect data on tobacco use and cessation counseling among health professional students in all WHO member states. GHPSS is a standardized school-based survey of third-year students pursuing advanced degrees in dentistry, medicine, nursing, or pharmacy. It is conducted in schools during regular class sessions. GHPSS follows an anonymous, self-administered format for data collection. GHPSS uses a core questionnaire on demographics, prevalence of cigarette smoking and other tobacco use, knowledge and attitudes about tobacco use, exposure to secondhand smoke, desire for smoking cessation, and training received regarding patient counseling on smoking cessation techniques. Questionnaires are translated into local languages as needed. GHPSS has a standardized methodology for selecting participating schools and classes and uniform data processing procedures.",
-            "title": "Global Tobacco Surveillance System (GTSS) - Global Health Professions Student Survey (GHPSS)",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "[1] Status is determined using the baseline, final, and target value. The statuses used in Healthy People 2020 were: \n\n1 - Target met or exceeded\u2014One of the following applies: (i) At baseline, the target was not met or exceeded, and the most recent value was equal to or exceeded the target. (The percentage of targeted change achieved was equal to or greater than 100%.); (ii) The baseline and most recent values were equal to or exceeded the target. (The percentage of targeted change achieved was not assessed.) \n\n2 - Improved\u2014One of the following applies: (i) Movement was toward the target, standard errors were available, and the percentage of targeted change achieved was statistically significant; (ii) Movement was toward the target, standard errors were not available, and the objective had achieved 10% or more of the targeted change.\n\n3 - Little or no detectable change\u2014One of the following applies: (i) Movement was toward the target, standard errors were available, and the percentage of targeted change achieved was not statistically significant; (ii) Movement was toward the target, standard errors were not available, and the objective had achieved less than 10% of the targeted change; (iii) Movement was away from the baseline and target, standard errors were available, and the percent change relative to the baseline was not statistically significant; (iv) Movement was away from the baseline and target, standard errors were not available, and the objective had moved less than 10% relative to the baseline; (v) No change was observed between the baseline and the final data point.\n\n4 - Got worse\u2014One of the following applies: (i) Movement was away from the baseline and target, standard errors were available, and the percent change relative to the baseline was statistically significant; (ii) Movement was away from the baseline and target, standard errors were not available, and the objective had moved 10% or more relative to the baseline.\n\n5 - Baseline only\u2014The objective only had one data point, so progress toward target attainment could not be assessed. Note that if additional data points did not meet the criteria for statistical reliability, data quality, or confidentiality, the objective was categorized as baseline only. \n\n6 - Informational\u2014A target was not set for this objective, so progress toward target attainment could not be assessed.\n\n\n[2] The final value is generally based on data available on the Healthy People 2020 website as of January 2020. For objectives that are continuing into Healthy People 2030, more recent data are available on the Healthy People 2030 website: https://health.gov/healthypeople. \n\n\n[3] For objectives that moved toward their targets, movement toward the target was measured as the percentage of targeted change achieved (unless the target was already met or exceeded at baseline): \n\nPercentage of targeted change achieved = (Final value - Baseline value) / (HP2020 target - Baseline value) * 100\n\n\n[4] For objectives that were not improving, did not meet or exceed their targets, and did not move towards their targets, movement away from the baseline was measured as the magnitude of the percent change from baseline: \n\nMagnitude of percent change from baseline = |Final value - Baseline value| / Baseline value * 100\n\n\n[5] Statistical significance was tested when the objective had a target, at least two data points (of unequal value), and available standard errors of the data. A normal distribution was assumed. All available digits were used to test statistical significance. Statistical significance of the percentage of targeted change achieved or the magnitude of the percentage change from baseline was assessed at the 0.05 level using a normal one-sided test. \n\n\n[6] For more information on the Healthy People 2020 methodology for measuring progress toward target attainment and the elimination of health disparities, see: Healthy People Statistical Notes, no 27; available from: https://www.cdc.gov/nchs/data/sta",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/x6ag-8y7r/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/x749-vh2i/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x6ag-8y7r/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/x6ag-8y7r/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/x749-vh2i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x749-vh2i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/x6ag-8y7r/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/x6ag-8y7r/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/x749-vh2i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x749-vh2i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x6ag-8y7r/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/x6ag-8y7r/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/x749-vh2i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x749-vh2i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Global-Survey-Data/Global-Tobacco-Surveillance-System-GTSS-Global-Hea/x6ag-8y7r",
-            "theme": [
-                "Global Survey Data"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/progress-tables.htm",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/x749-vh2i",
             "issued": "2022-01-22",
-            "@type": "dcat:Dataset",
-            "temporal": "1988-01-01/2019-12-31",
-            "modified": "2023-08-23",
             "keyword": [
                 "healthy people 2020",
                 "sdoh-access-to-health-care",
@@ -74932,83 +75107,38 @@
                 "sdoh-use-of-health-care",
                 "sdoh-workplace"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/x749-vh2i",
-            "description": "[1] Status is determined using the baseline, final, and target value. The statuses used in Healthy People 2020 were: \n\n1 - Target met or exceeded\u2014One of the following applies: (i) At baseline, the target was not met or exceeded, and the most recent value was equal to or exceeded the target. (The percentage of targeted change achieved was equal to or greater than 100%.); (ii) The baseline and most recent values were equal to or exceeded the target. (The percentage of targeted change achieved was not assessed.) \n\n2 - Improved\u2014One of the following applies: (i) Movement was toward the target, standard errors were available, and the percentage of targeted change achieved was statistically significant; (ii) Movement was toward the target, standard errors were not available, and the objective had achieved 10% or more of the targeted change.\n\n3 - Little or no detectable change\u2014One of the following applies: (i) Movement was toward the target, standard errors were available, and the percentage of targeted change achieved was not statistically significant; (ii) Movement was toward the target, standard errors were not available, and the objective had achieved less than 10% of the targeted change; (iii) Movement was away from the baseline and target, standard errors were available, and the percent change relative to the baseline was not statistically significant; (iv) Movement was away from the baseline and target, standard errors were not available, and the objective had moved less than 10% relative to the baseline; (v) No change was observed between the baseline and the final data point.\n\n4 - Got worse\u2014One of the following applies: (i) Movement was away from the baseline and target, standard errors were available, and the percent change relative to the baseline was statistically significant; (ii) Movement was away from the baseline and target, standard errors were not available, and the objective had moved 10% or more relative to the baseline.\n\n5 - Baseline only\u2014The objective only had one data point, so progress toward target attainment could not be assessed. Note that if additional data points did not meet the criteria for statistical reliability, data quality, or confidentiality, the objective was categorized as baseline only. \n\n6 - Informational\u2014A target was not set for this objective, so progress toward target attainment could not be assessed.\n\n\n[2] The final value is generally based on data available on the Healthy People 2020 website as of January 2020. For objectives that are continuing into Healthy People 2030, more recent data are available on the Healthy People 2030 website: https://health.gov/healthypeople. \n\n\n[3] For objectives that moved toward their targets, movement toward the target was measured as the percentage of targeted change achieved (unless the target was already met or exceeded at baseline): \n\nPercentage of targeted change achieved = (Final value - Baseline value) / (HP2020 target - Baseline value) * 100\n\n\n[4] For objectives that were not improving, did not meet or exceed their targets, and did not move towards their targets, movement away from the baseline was measured as the magnitude of the percent change from baseline: \n\nMagnitude of percent change from baseline = |Final value - Baseline value| / Baseline value * 100\n\n\n[5] Statistical significance was tested when the objective had a target, at least two data points (of unequal value), and available standard errors of the data. A normal distribution was assumed. All available digits were used to test statistical significance. Statistical significance of the percentage of targeted change achieved or the magnitude of the percentage change from baseline was assessed at the 0.05 level using a normal one-sided test. \n\n\n[6] For more information on the Healthy People 2020 methodology for measuring progress toward target attainment and the elimination of health disparities, see: Healthy People Statistical Notes, no 27; available from: https://www.cdc.gov/nchs/data/sta",
-            "title": "Healthy People 2020 Final Progress Table",
+            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/progress-tables.htm",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-08-23",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/x749-vh2i/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x749-vh2i/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/x749-vh2i/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/x749-vh2i/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/x749-vh2i/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x749-vh2i/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/x749-vh2i/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
             "spatial": "US",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "temporal": "1988-01-01/2019-12-31",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Healthy People 2020 Final Progress Table"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/x7xw-nitb",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Allergy and Clinical Immunology Branch (ACIB), Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/x7xw-nitb",
             "description": "Perfluoroheptaoinc acid (PFHpA), perfluorohexanoic acid (PFHxA), and perfluoropentanoic acid (PFPeA) are synthetic chemicals belonging to the per- and polyfluoroalkyl substances (PFAS) group that includes over 5,000 chemicals.  PFHpA, PFHxA, and PFPeA are short-chain PFAS (C7, C6, C5, respectively) that have been labeled as a safer alternative to the legacy PFAS perfluorooctanoic acid (PFOA) and perfluorooctane sulfate (PFOS) which have been linked to numerous health effects.  This class of chemicals are incorporated into consumer products such as stain resistant carpeting and textiles, nanosprays, medical devices, and fire-fighting foams.  There is a high potential for occupational exposure and in the environment, short-chain PFAS have been detected in a variety of water sources leading to concerns for dermal exposure, however, these studies are lacking.  In previous studies from our lab, PFOA was demonstrated to be absorbed via the skin and immunomodulatory.  Also, the short-chain PFAS, PFBA, was found to have systemic toxic effects on mice with dermal exposure.  In the present study, the systemic toxicity of a 28-day dermal PFHpA, PFHxA, and PFPeA (1.25-5% w/v or v/v, or 31.25-125 mg/kg/dose) exposure was evaluated in a murine model.",
-            "title": "Systemic toxicity induced by topical application of perfluoroheptanoic acid (PFHpA), perfluorohexanoic acid (PFHxA), and perfluoropentanoic acid (PFPeA) in a murine model",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75016,38 +75146,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/x7xw-nitb",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/x7xw-nitb",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Systemic toxicity induced by topical application of perfluoroheptanoic acid (PFHpA), perfluorohexanoic acid (PFHxA), and perfluoropentanoic acid (PFPeA) in a murine model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/x7ys-5vpn",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "glossary",
-                "methodology"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/x7ys-5vpn",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "Medicaid Coverage Of Cessation Treatments And Barriers To Treatments Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75055,40 +75181,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/x7ys-5vpn",
+            "issued": "2015-01-21",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "https://data.cdc.gov/d/x7ys-5vpn",
+            "modified": "2023-08-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Cessation Coverage "
-            ]
+            ],
+            "title": "Medicaid Coverage Of Cessation Treatments And Barriers To Treatments Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/x7zy-2xmx",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2016-11-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
-            "keyword": [
-                "500cities",
-                "boundaries",
-                "census tract",
-                "shapefile"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "500 Cities Public Inquiries",
                 "hasEmail": "mailto:places@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/x7zy-2xmx",
             "description": "This census tract shapefile for the 500 Cities project was extracted from the Census 2010 Tiger/Line database and modified to remove portions of census tracts that were outside of city boundaries. This shapefile can be joined with 500 Cities census tract-level Data (GIS Friendly Format) in a geographic information system (GIS) to make maps at the census tract level.",
-            "title": "500 Cities: Census Tract Boundaries",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75096,44 +75220,40 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/x7zy-2xmx",
+            "issued": "2016-11-08",
+            "keyword": [
+                "500cities",
+                "boundaries",
+                "census tract",
+                "shapefile"
+            ],
+            "landingPage": "https://data.cdc.gov/d/x7zy-2xmx",
+            "modified": "2024-10-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "500 Cities: Census Tract Boundaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/x8jf-txib",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "nedss",
-                "netss",
-                "nndss",
-                "severe acute respiratory syndrome-associated coronavirus disease",
-                "shiga toxin-producing escherichia coli (stec)",
-                "shigellosis",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/x8jf-txib",
             "description": "Notice: For data on COVID-19 in the United States, please see https://www.cdc.gov/coronavirus/2019-ncov/cases-in-us.html.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis \u2013 2020.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75141,66 +75261,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x8jf-txib/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x8jf-txib/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x8jf-txib/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/x8jf-txib/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x8jf-txib/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x8jf-txib/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x8jf-txib/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x8jf-txib/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x8jf-txib/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/x8jf-txib",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "nedss",
+                "netss",
+                "nndss",
+                "severe acute respiratory syndrome-associated coronavirus disease",
+                "shiga toxin-producing escherichia coli (stec)",
+                "shigellosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/x8jf-txib",
+            "modified": "2021-01-07",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/x8ni-jytx",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "junin virus",
-                "lassa virus",
-                "lujo virus",
-                "nedss",
-                "netss",
-                "nndss",
-                "viral hemorrhagic fevers",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/x8ni-jytx",
             "description": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers\". NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
-            "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75208,63 +75327,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x8ni-jytx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x8ni-jytx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x8ni-jytx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/x8ni-jytx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x8ni-jytx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x8ni-jytx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x8ni-jytx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x8ni-jytx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x8ni-jytx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/x8ni-jytx",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "junin virus",
+                "lassa virus",
+                "lujo virus",
+                "nedss",
+                "netss",
+                "nndss",
+                "viral hemorrhagic fevers",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/x8ni-jytx",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/x9gk-5huc",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "keyword": [
-                "2022",
-                "2023",
-                "2024",
-                "2025",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NNDSS Team",
                 "hasEmail": "mailto:NNDSSWeb@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/x9gk-5huc",
             "description": "NNDSS - In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\n\nNotes:\n\n\u2022 These are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/infectious-disease/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data.\n\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page https://www.cdc.gov/nndss/infectious-disease/notice-to-data-users.html.\n\n\u2022 The list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2024 and 2025 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\n\u2022 Please refer to the Stacks publication for weekly updates to the footnote for influenza-associated pediatric mortality.\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS Weekly Data",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75272,59 +75394,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x9gk-5huc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x9gk-5huc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x9gk-5huc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/x9gk-5huc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x9gk-5huc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x9gk-5huc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x9gk-5huc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x9gk-5huc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x9gk-5huc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/x9gk-5huc",
+            "issued": "2022-01-18",
+            "keyword": [
+                "2022",
+                "2023",
+                "2024",
+                "2025",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/x9gk-5huc",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS Weekly Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/x9gq-59r3",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-09-14",
-            "@type": "dcat:Dataset",
-            "modified": "2016-09-14",
-            "keyword": [
-                "cdc",
-                "centers for disease control and prevention"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/x9gq-59r3",
             "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 10 - Seattle",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75332,62 +75458,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x9gq-59r3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x9gq-59r3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x9gq-59r3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/x9gq-59r3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x9gq-59r3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x9gq-59r3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/x9gq-59r3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/x9gq-59r3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/x9gq-59r3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/x9gq-59r3",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/x9gq-59r3",
+            "modified": "2016-09-14",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Motor Vehicle"
-            ]
+            ],
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 10 - Seattle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/reduced-access-to-care.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-05-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-04-23/2021-07-05",
-            "modified": "2023-04-14",
-            "keyword": [
-                "covid-19",
-                "delayed care",
-                "sdoh-access-to-health-care",
-                "unmet need"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xb3p-q62w",
-            "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, gender, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
-            "title": "Indicators of Reduced Access to Care Due to the Coronavirus Pandemic During Last 4 Weeks",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, sex, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75395,65 +75519,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xb3p-q62w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xb3p-q62w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xb3p-q62w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xb3p-q62w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xb3p-q62w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xb3p-q62w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xb3p-q62w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xb3p-q62w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xb3p-q62w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/xb3p-q62w",
+            "issued": "2020-05-20",
+            "keyword": [
+                "delayed care",
+                "unmet need",
+                "covid-19",
+                "sdoh-access-to-health-care"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/reduced-access-to-care.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2025-02-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "US",
+            "temporal": "2020-04-23/2021-07-05",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Indicators of Reduced Access to Care Due to the Coronavirus Pandemic During Last 4 Weeks"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xbk2-5i4e",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2018-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-27",
-            "keyword": [
-                "drought",
-                "environmental health"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Craig Kassinger",
                 "hasEmail": "mailto:nephtrackingsupport@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xbk2-5i4e",
             "description": "This dataset provides data at the county level for the contiguous United States. It includes monthly Standardized Precipitation Index (SPI) data from 1895-2016 provided by the Cooperative Institute for Climate and Satellites - North Carolina. Please refer to the metadata attachment for more information.\r\n\r\nLearn more about drought on the Tracking Network's website: https://ephtracking.cdc.gov/showDroughtLanding.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking. \r\n\r\nProblems or Questions? \r\nEmail trackingsupport@cdc.gov.",
-            "title": "Standardized Precipitation Index, 1895-2016",
-            "programCode": [
-                "009:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75461,64 +75587,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xbk2-5i4e/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xbk2-5i4e/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xbk2-5i4e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xbk2-5i4e/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xbk2-5i4e/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xbk2-5i4e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xbk2-5i4e/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xbk2-5i4e/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xbk2-5i4e/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "Environmental Health & Toxicology"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-visualization/drug-poisoning-mortality/",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2017-12-06",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-30",
+            "identifier": "https://data.cdc.gov/api/views/xbk2-5i4e",
+            "issued": "2018-07-26",
             "keyword": [
-                "deaths",
-                "drug poisoning",
-                "mortality",
-                "national",
-                "nchs",
-                "state",
-                "united states"
+                "drought",
+                "environmental health"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xbk2-5i4e",
+            "modified": "2018-11-27",
+            "programCode": [
+                "009:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "theme": [
+                "Environmental Health & Toxicology"
+            ],
+            "title": "Standardized Precipitation Index, 1895-2016"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xbxb-epbu",
             "description": "This dataset describes drug poisoning deaths at the U.S. and state level by selected demographic characteristics, and includes age-adjusted death rates for drug poisoning. \r\n\r\nDeaths are classified using the International Classification of Diseases, Tenth Revision (ICD\u201310). Drug-poisoning deaths are defined as having ICD\u201310 underlying cause-of-death codes X40\u2013X44 (unintentional), X60\u2013X64 (suicide), X85 (homicide), or Y10\u2013Y14 (undetermined intent).\r\n\r\nEstimates are based on the National Vital Statistics System multiple cause-of-death mortality files (1). Age-adjusted death rates (deaths per 100,000 U.S. standard population for 2000) are calculated using the direct method. Populations used for computing death rates for 2011\u20132016 are postcensal estimates based on the 2010 U.S. census. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for noncensus years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published.\r\n\r\nDeath rates for some states and years may be low due to a high number of unresolved pending cases or misclassification of ICD\u201310 codes for unintentional poisoning as R99, \u201cOther ill-defined and unspecified causes of mortality\u201d (2). For example, this issue is known to affect New Jersey in 2009 and West Virginia in 2005 and 2009 but also may affect other years and other states. Drug poisoning death rates may be underestimated in those instances.\r\n\r\nREFERENCES\r\n1. National Center for Health Statistics. National Vital Statistics System: Mortality data. Available from: http://www.cdc.gov/nchs/deaths.htm.\r\n\r\n2. CDC. CDC Wonder: Underlying cause of death 1999\u20132016. Available from: http://wonder.cdc.gov/wonder/help/ucd.html.",
-            "title": "NCHS - Drug Poisoning Mortality by State: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75526,61 +75647,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xbxb-epbu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xbxb-epbu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xbxb-epbu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xbxb-epbu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xbxb-epbu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xbxb-epbu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xbxb-epbu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xbxb-epbu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xbxb-epbu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/xbxb-epbu",
+            "issued": "2017-12-06",
+            "keyword": [
+                "deaths",
+                "drug poisoning",
+                "mortality",
+                "national",
+                "nchs",
+                "state",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/drug-poisoning-mortality/",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-03-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - Drug Poisoning Mortality by State: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "accrualPeriodicity": "NA",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-03-04",
-            "temporal": "1999-2018",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-01",
-            "references": [
-                "https://www.cdc.gov/nchs/nhanes/visualization/"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:CDCINFO@CDC.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xcc8-2jrh",
+            "describedBy": "https://www.cdc.gov/nchs/nhanes/visualization/",
             "description": "These data represent mean intake, on a given day, estimates of nutrients from foods and beverages from the National Health and Nutrition Examination Survey (NHANES).\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS NHANES Select Mean Dietary Intake Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75588,49 +75716,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xcc8-2jrh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xcc8-2jrh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xcc8-2jrh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xcc8-2jrh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xcc8-2jrh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xcc8-2jrh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xcc8-2jrh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xcc8-2jrh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xcc8-2jrh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "identifier": "https://data.cdc.gov/api/views/xcc8-2jrh",
+            "issued": "2024-03-04",
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "NA",
+            "modified": "2024-11-01",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/nhanes/visualization/"
+            ],
+            "spatial": "United States",
+            "temporal": "1999-2018",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS NHANES Select Mean Dietary Intake Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/hud-restricted.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-06-16",
-            "@type": "dcat:Dataset",
-            "temporal": "1996/2019",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data/datalinkage/weight-file.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCHS Data Linkage Program",
+                "hasEmail": "mailto:DataLinkage@cdc.gov"
+            },
+            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/NCHS-HUD-Match-Rate-Tables-final.pdf",
+            "describedByType": "application/pdf",
+            "description": "NCHS has linked 1999-2018 National Health Interview Survey (NHIS) and 1999-2018 National Health and Nutrition Examination Survey (NHANES) to administrative data through 2019 for the Department of Housing and Urban Development\u2019s (HUD) largest housing assistance programs: the Housing Choice Voucher program, public housing, and privately owned, subsidized multifamily housing. Linkage of NCHS survey participants with HUD administrative records provides the opportunity to examine relationships between housing and health.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xcz7-jei9",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-06-16",
             "keyword": [
                 "linked hud files",
                 "nchs surveys",
@@ -75656,60 +75808,38 @@
                 "sdoh-use-of-health-care",
                 "sdoh-workplace"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NCHS Data Linkage Program",
-                "hasEmail": "mailto:DataLinkage@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/hud-restricted.htm",
+            "modified": "2024-10-11",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/xcz7-jei9",
-            "description": "NCHS has linked 1999-2018 National Health Interview Survey (NHIS) and 1999-2018 National Health and Nutrition Examination Survey (NHANES) to administrative data through 2019 for the Department of Housing and Urban Development\u2019s (HUD) largest housing assistance programs: the Housing Choice Voucher program, public housing, and privately owned, subsidized multifamily housing. Linkage of NCHS survey participants with HUD administrative records provides the opportunity to examine relationships between housing and health.",
-            "title": "NCHS Survey Data Linked to the Department of Housing and Urban Development (HUD) Housing Assistance Program Files",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "mediaType": "text/html"
-                }
+            "references": [
+                "https://www.cdc.gov/nchs/data/datalinkage/weight-file.pdf"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/NCHS-HUD-Match-Rate-Tables-final.pdf",
+            "temporal": "1996/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Survey Data Linked to the Department of Housing and Urban Development (HUD) Housing Assistance Program Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/xd2k-siai",
-            "issued": "2024-11-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Pathology and Physiology Research Branch, Health Effects Laboratory Division",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xd2k-siai",
             "description": "In the lung, carcinogenesis is a multi-stage process that includes initiation by a genotoxic agent, promotion that expands the population of cells with damaged DNA to form a tumor, and progression from benign to malignant neoplasms. We have previously shown that Mitsui-7, a long and rigid multi-walled carbon nanotube (MWCNT), promotes pulmonary carcinogenesis in a mouse model. To investigate the potential exposure threshold and dose-response for tumor promotion by this MWCNT, 3-methylcholanthrene (MC) initiated (10 \u03bcg/g, i.p., once) or vehicle (corn oil) treated B6C3F1 mice were exposed by inhalation to filtered air or MWCNT (5 mg/m3) for 5 hours/day for 0, 2, 5, or 10 days and were followed for 17 months  post-exposure for evidence of lung tumors.",
-            "title": "Potent Lung Tumor Promotion by Inhaled MWCNT",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75717,42 +75847,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xd2k-siai",
+            "issued": "2024-11-18",
+            "landingPage": "https://data.cdc.gov/d/xd2k-siai",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Potent Lung Tumor Promotion by Inhaled MWCNT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xdg2-nh8n",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2016-01-20",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-27",
-            "keyword": [
-                "casinos",
-                "fact sheet",
-                "gaming",
-                "infographic",
-                "secondhand smoke",
-                "smokefree"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OSHData Support",
                 "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xdg2-nh8n",
             "description": "Explore the Going Smokefree Matters - Casinos Infographic which outlines key facts related to the effects of secondhand smoke exposure in casinos.",
-            "title": "Going Smokefree Matters - Casinos Infographic",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75760,42 +75882,42 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xdg2-nh8n",
+            "issued": "2016-01-20",
+            "keyword": [
+                "casinos",
+                "fact sheet",
+                "gaming",
+                "infographic",
+                "secondhand smoke",
+                "smokefree"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xdg2-nh8n",
+            "modified": "2023-07-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Policy"
-            ]
+            ],
+            "title": "Going Smokefree Matters - Casinos Infographic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-10-07",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-12",
-            "keyword": [
-                "flu vaccination",
-                "immunization",
-                "influenza",
-                "vaccination",
-                "vaccination coverage",
-                "vaxviews"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCIRD",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xerk-pcm8",
             "description": "Vaccination Coverage among Health Care Personnel\n\n\u2022 Data on influenza vaccination performance measurement from the National Healthcare Safety Network (NHSN) for hospital-based health care personnel (HCP) at the national and state levels by personnel group.\n\n\u2022 Additional information available at https://www.cdc.gov/flu/fluvaxview/index.htm",
-            "title": "Vaccination Coverage among Health Care Personnel",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75803,49 +75925,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xerk-pcm8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xerk-pcm8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xerk-pcm8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xerk-pcm8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xerk-pcm8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xerk-pcm8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xerk-pcm8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xerk-pcm8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xerk-pcm8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xerk-pcm8",
+            "issued": "2021-10-07",
+            "keyword": [
+                "flu vaccination",
+                "immunization",
+                "influenza",
+                "vaccination",
+                "vaccination coverage",
+                "vaxviews"
+            ],
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/index.htm",
+            "modified": "2024-09-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "Vaccination Coverage among Health Care Personnel"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xf9s-d895",
-            "issued": "2024-07-23",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/xf9s-d895",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75853,52 +75986,49 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xf9s-d895/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xf9s-d895/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xf9s-d895/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xf9s-d895/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xf9s-d895/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xf9s-d895/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xf9s-d895/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xf9s-d895/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xf9s-d895/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/xf9s-d895",
+            "issued": "2024-07-23",
+            "landingPage": "https://data.cdc.gov/d/xf9s-d895",
+            "modified": "2024-07-23",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "dhds_dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/xfk2-6xmb",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Allergy and Clinical Immunology Branch (ACIB), Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xfk2-6xmb",
             "description": "Per- and polyfluoroalkyl substances (PFAS) are a large group of synthetic man-made surfactants of over 12,000 compounds that are incorporated into numerous products for their chemical and physical properties.  Numerous PFAS have been associated with adverse health effects.  Although there is a high potential for dermal exposure, these studies are lacking.  The present study evaluated the systemic and immunotoxicity of sub-chronic 28- or 10-day dermal exposure, respectively, to of PFHpS (0.3125-2.5% or 7.82-62.5 mg/kg/dose) or PFOS (0.5% or 12.5 mg/kg/dose) in a murine model.",
-            "title": "Systemic and immunotoxicity induced by topical application of perfluoroheptane sulfonic acid (PFHpS) or perfluorooctane sulfonic acid (PFOS) in a murine model",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75906,43 +76036,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xfk2-6xmb",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/xfk2-6xmb",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Systemic and immunotoxicity induced by topical application of perfluoroheptane sulfonic acid (PFHpS) or perfluorooctane sulfonic acid (PFOS) in a murine model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xgy8-wnft",
             "bureauCode": [
                 "009:15"
             ],
-            "issued": "2021-10-28",
-            "@type": "dcat:Dataset",
-            "temporal": "Weekly",
-            "modified": "2025-01-17",
-            "keyword": [
-                "and economic security act",
-                "coronavirus aid",
-                "coronavirus preparedness and response supplemental appropriations act",
-                "covid-19",
-                "paycheck protection program and health care enhancement act",
-                "relief"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HRSA Chief Data Officer",
                 "hasEmail": "mailto:PRFdata@hrsa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "HRSA"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xgy8-wnft",
             "description": "The COVID-19 Coverage Assistance Fund provides reimbursements on a rolling basis directly to eligible health care entities for costs associated with administering COVID-19 vaccines to underinsured individuals, who are defined for this purpose as having a health plan that either does not include COVID-19 vaccine administration as a covered benefit or covers COVID-19 vaccine administration but with cost-sharing.\n\nThe program funding information is as follows: The Coronavirus Aid, Relief, and Economic Security (CARES) Act (P.L. 116-136), appropriated $100 billion to reimburse eligible health care providers for health care related expenses or lost revenues that are attributable to coronavirus. The Paycheck Protection Program and Health Care Enhancement Act or PPPHCEA (P.L. 116-139) appropriated an additional $75 billion for relief funds, and the Coronavirus Response and Relief Supplemental Appropriations (CRRSA) Act appropriated an additional $3 billion.  HRSA established the Provider Relief Fund (PRF) to administer payments to eligible providers. A portion of the PRF funds are being used to provide reimbursement to providers for administering Food and Drug Administration (FDA) authorized COVID-19 vaccines under an Emergency Use Authorization (EUA) or FDA-licensed COVID-19 vaccines under a Biologics License Application (BLA) to underinsured individuals. To learn more about the program, visit: https://www.hrsa.gov/covid19-coverage-assistance\n\nThis dataset represents the list of health care entities who have agreed to the Terms and Conditions and received claims reimbursement for costs associated with administering COVID-19 vaccines to underinsured individuals.\n\nFor Provider Relief Fund Data - https://data.cdc.gov/Administrative/HHS-Provider-Relief-Fund/kh8y-3es6",
-            "title": "COVID-19 Coverage Assistance Fund: Claims Reimbursement to Health Care Providers and Facilities for Services to the Underinsured",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75950,77 +76071,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xgy8-wnft/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xgy8-wnft/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xgy8-wnft/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xgy8-wnft/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xgy8-wnft/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xgy8-wnft/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xgy8-wnft/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xgy8-wnft/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xgy8-wnft/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/xgy8-wnft",
+            "issued": "2021-10-28",
+            "keyword": [
+                "and economic security act",
+                "coronavirus aid",
+                "coronavirus preparedness and response supplemental appropriations act",
+                "covid-19",
+                "paycheck protection program and health care enhancement act",
+                "relief"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xgy8-wnft",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "HRSA"
+            },
+            "spatial": "US",
+            "temporal": "Weekly",
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "COVID-19 Coverage Assistance Fund: Claims Reimbursement to Health Care Providers and Facilities for Services to the Underinsured"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/drug-overdose-data.htm",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2018-03-06",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-01-01/2024-08-31",
-            "modified": "2025-01-15",
-            "keyword": [
-                "cocaine",
-                "deaths",
-                "drug",
-                "drug overdose",
-                "heroin",
-                "methadone",
-                "monthly",
-                "mortality",
-                "nchs",
-                "nvss",
-                "opiate",
-                "opioid",
-                "provisional",
-                "psychostimulants",
-                "state",
-                "united states",
-                "vsrr"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xkb8-kh2a",
             "description": "This data presents provisional counts for drug overdose deaths based on a current flow of mortality data in the National Vital Statistics System. Counts for the most recent final annual data are provided for comparison. National provisional counts include deaths occurring within the 50 states and the District of Columbia as of the date specified and may not include all deaths that occurred during a given time period. Provisional counts are often incomplete and causes of death may be pending investigation resulting in an underestimate relative to final counts. To address this, methods were developed to adjust provisional counts for reporting delays by generating a set of predicted provisional counts.\n\nSeveral data quality metrics, including the percent completeness in overall death reporting, percentage of deaths with cause of death pending further investigation, and the percentage of drug overdose deaths with specific drugs or drug classes reported are included to aid in interpretation of provisional data as these measures are related to the accuracy of provisional counts. Reporting of the specific drugs and drug classes involved in drug overdose deaths varies by jurisdiction, and comparisons of death rates involving specific drugs across selected jurisdictions should not be made. Provisional data presented will be updated on a monthly basis as additional records are received.\n\nFor more information please visit: https://www.cdc.gov/nchs/nvss/vsrr/drug-overdose-data.htm",
-            "title": "VSRR Provisional Drug Overdose Death Counts",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76028,73 +76139,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xkb8-kh2a/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xkb8-kh2a/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xkb8-kh2a/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xkb8-kh2a/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xkb8-kh2a/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xkb8-kh2a/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xkb8-kh2a/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xkb8-kh2a/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xkb8-kh2a/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
-            "theme": [
-                "NCHS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2020-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-27",
+            "identifier": "https://data.cdc.gov/api/views/xkb8-kh2a",
+            "issued": "2018-03-06",
             "keyword": [
-                "all causes",
-                "coronavirus",
-                "covid-19",
+                "cocaine",
                 "deaths",
-                "excess deaths",
+                "drug",
+                "drug overdose",
+                "heroin",
+                "methadone",
+                "monthly",
                 "mortality",
                 "nchs",
                 "nvss",
+                "opiate",
+                "opioid",
                 "provisional",
-                "puerto rico",
+                "psychostimulants",
                 "state",
                 "united states",
-                "weekly"
+                "vsrr"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/drug-overdose-data.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "2015-01-01/2024-08-31",
+            "theme": [
+                "NCHS"
+            ],
+            "title": "VSRR Provisional Drug Overdose Death Counts"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xkkf-xrst",
             "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nEstimates of excess deaths can provide information about the burden of mortality potentially related to COVID-19, beyond the number of deaths that are directly attributed to COVID-19. Excess deaths are typically defined as the difference between observed numbers of deaths and expected numbers. This visualization provides weekly data on excess deaths by jurisdiction of occurrence. Counts of deaths in more recent weeks are compared with historical trends to determine whether the number of deaths is significantly higher than expected.\n\nEstimates of excess deaths can be calculated in a variety of ways, and will vary depending on the methodology and assumptions about how many deaths are expected to occur. Estimates of excess deaths presented in this webpage were calculated using Farrington surveillance algorithms (1). For each jurisdiction, a model is used to generate a set of expected counts, and the upper bound of the 95% Confidence Intervals (95% CI) of these expected counts is used as a threshold to estimate excess deaths. Observed counts are compared to these upper bound estimates to determine whether a significant increase in deaths has occurred. Provisional counts are weighted to account for potential underreporting in the most recent weeks. However, data for the most recent week(s) are still likely to be incomplete. Only about 60% of deaths are reported within 10 days of the date of death, and there is considerable variation by jurisdiction. More detail about the methods, weighting, data, and limitations can be found in the Technical Notes.",
-            "title": "Excess Deaths Associated with COVID-19",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76102,58 +76218,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xkkf-xrst/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xkkf-xrst/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xkkf-xrst/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xkkf-xrst/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xkkf-xrst/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xkkf-xrst/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xkkf-xrst/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xkkf-xrst/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xkkf-xrst/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xkkf-xrst",
+            "issued": "2020-04-29",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "excess deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "puerto rico",
+                "state",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-09-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
             "spatial": "United States, Puerto Rico",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Excess Deaths Associated with COVID-19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/xm7q-e7uu",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Physical Effects Research Branch (PERB), Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xm7q-e7uu",
             "description": "Working with vibrating hand tools is associated with the development of hand-arm vibration syndrome (HAVS).  HAVS is characterized by cold-induced vasospasms, finger blanching and changes in sensory function.  Vibration plays a major role in the development of the symptoms that are characteristic of HAVS, however, the hands and fingers of worker using tools are also exposed to pressure applied as the workers grip tools.  The pressure applied by gripping a tool might also affect blood flow and sensorineural function.  Therefore, this study examined the effects of applied pressure [2 and 4 newtons (N)] on peripheral vascular and sensorineural function using a characterized rat tail model.  The tails of rats were exposed to 0, 2 or 4N of applied force for 10 days.  Blood flow (laser doppler) and sensitivity of the tail to pressure (Randall-Selitto pressure test) was measured on days 1, 5 and 10 of the exposure.  The sensitivity of the tail nerves to electrical stimulation was measured on days 2 and 9.",
-            "title": "Applied force alters sensorineural and peripheral vascular function in an animal model of hand-arm vibration syndrome",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76161,40 +76291,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xm7q-e7uu",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/xm7q-e7uu",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Applied force alters sensorineural and peripheral vascular function in an animal model of hand-arm vibration syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xm94-zmtx",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-05-28",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-07",
-            "keyword": [
-                "air pollution",
-                "asthma",
-                "environmental health",
-                "ozone"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Craig Kassinger",
                 "hasEmail": "mailto:trackingsupport@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xm94-zmtx",
             "description": "This dataset provides modeled predictions of ozone levels from the EPA's Downscaler model. Data are at the census tract level for 2006-2010. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\n\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\n\nBy using these data, you signify your agreement to comply with the following requirements:\n1. Use the data for statistical reporting and analysis only.\n2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals.\n3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov.\n4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.\n5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC.\n6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily Census Tract-Level Ozone Concentrations, 2006-2010",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76202,73 +76326,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xm94-zmtx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xm94-zmtx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xm94-zmtx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xm94-zmtx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xm94-zmtx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xm94-zmtx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xm94-zmtx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xm94-zmtx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xm94-zmtx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xm94-zmtx",
+            "issued": "2020-05-28",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "ozone"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xm94-zmtx",
+            "modified": "2021-07-07",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Environmental Health & Toxicology"
-            ]
+            ],
+            "title": "Daily Census Tract-Level Ozone Concentrations, 2006-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-03-05",
-            "temporal": "2000/2018",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-08",
-            "keyword": [
-                "ambulatory care",
-                "black or african american",
-                "child and adolescent",
-                "emergency department visits",
-                "emergency service",
-                "health care use",
-                "health us",
-                "hospital use",
-                "men",
-                "office visits",
-                "older persons",
-                "physician office visits",
-                "physicians",
-                "white",
-                "women"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:healthus@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xmjk-wh9b",
             "description": "Data on visits to physician offices and hospital emergency departments in the United States, by age, sex, and race. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Ambulatory Medical Care Survey and National Hospital Ambulatory Medical Care Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Visits to physician offices, hospital outpatient departments, and hospital emergency departments, by age, sex, and race: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76276,57 +76389,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xmjk-wh9b/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xmjk-wh9b/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xmjk-wh9b/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xmjk-wh9b/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xmjk-wh9b/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xmjk-wh9b/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xmjk-wh9b/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xmjk-wh9b/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xmjk-wh9b/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xmjk-wh9b",
+            "issued": "2024-03-05",
+            "keyword": [
+                "ambulatory care",
+                "black or african american",
+                "child and adolescent",
+                "emergency department visits",
+                "emergency service",
+                "health care use",
+                "health us",
+                "hospital use",
+                "men",
+                "office visits",
+                "older persons",
+                "physician office visits",
+                "physicians",
+                "white",
+                "women"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "modified": "2024-11-08",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "temporal": "2000/2018",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS Visits to physician offices, hospital outpatient departments, and hospital emergency departments, by age, sex, and race: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/xmn2-yrqr",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Physical Effects Research Branch (PERB), Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xmn2-yrqr",
             "description": "The development of vibration-induced finger disorders is likely associated with combined static and dynamic responses of the fingers to vibration exposure. To study the mechanisms of these disorders, a new rat-tail model has been established to mimic the finger pressure and vibration exposures. However, the mechanical behavior of the tail during compression needs to be better understood to improve the model and its applications. The purpose of the current study was to investigate the static and time-dependent force responses of the rat tail during compression. Compression tests were conducted on male Sprague-Dawley cadaver rat tails using a micromechanical testing system at three deformation velocities and three deformation magnitudes. Contact-width, and the time-histories of force and deformation were measured. Additionally, force-relaxation tests were conducted and a Prony series was used to model the force-relaxation behavior of the tail.",
-            "title": "Quantification of mechanical behavior of rat tail under compression",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76334,51 +76464,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xmn2-yrqr",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/xmn2-yrqr",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Quantification of mechanical behavior of rat tail under compression"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-04-28",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2020-12-31",
-            "modified": "2023-04-03",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "coronavirus",
-                "county",
-                "covid-19",
-                "deaths",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "sdoh-environmental",
-                "united states",
-                "yearly"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xmrr-rw5u",
             "description": "Provisional counts of deaths involving coronavirus disease 2019 (COVID-19) by United States county of residence and age group, from January 1, 2020 through December 31, 2020.",
-            "title": "AH Provisional COVID-19 Deaths by County and Age for 2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76386,68 +76500,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xmrr-rw5u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xmrr-rw5u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xmrr-rw5u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xmrr-rw5u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xmrr-rw5u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xmrr-rw5u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xmrr-rw5u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xmrr-rw5u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xmrr-rw5u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/xmrr-rw5u",
+            "issued": "2021-04-28",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "county",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "sdoh-environmental",
+                "united states",
+                "yearly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-04-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "2020-01-01/2020-12-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by County and Age for 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xna8-x7qg",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "hepatitis c",
-                "influenza-associated pediatric mortality",
-                "nedss",
-                "netss",
-                "nndss",
-                "perinatal infection",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xna8-x7qg",
             "description": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Since [INSERT DATE], XXX influenza-associated pediatric deaths occurring during the 2017-18 season have been reported.",
-            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76455,62 +76575,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xna8-x7qg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xna8-x7qg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xna8-x7qg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xna8-x7qg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xna8-x7qg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xna8-x7qg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xna8-x7qg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xna8-x7qg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xna8-x7qg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xna8-x7qg",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "hepatitis c",
+                "influenza-associated pediatric mortality",
+                "nedss",
+                "netss",
+                "nndss",
+                "perinatal infection",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xna8-x7qg",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xnjn-rdmd",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "N/A",
-            "issued": "2024-09-23",
-            "@type": "dcat:Dataset",
-            "temporal": "October 1, 2024 - no specified end date",
-            "modified": "2025-01-31",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "hospitalizations"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC-INFO",
                 "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDC"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xnjn-rdmd",
             "description": "This dataset represents preliminary weekly estimates of cumulative U.S. COVID-19-associated hospitalizations for the 2024-2025 period. The weekly cumulatve COVID-19 \u2013associated hospitalization estimates are preliminary, and use reported weekly hospitalizations among laboratory-confirmed severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) infections. The data are updated week-by-week as new COVID-19 hospitalizations are reported to CDC from the COVID-NET system and include both new admissions that occurred during the reporting week, as well as those admitted in previous weeks that may not have been included in earlier reporting. Each week CDC estimates a range (i.e., lower estimate and an upper estimate) of COVID-19 -associated hospitalizations that have occurred since October 1, 2024. For details, please refer to the publication [7]. \n \n<b>Note:</b> Data are preliminary and subject to change as more data become available. Rates for recent COVID-19-associated hospital admissions are subject to reporting delays; as new data are received each week, previous rates are updated accordingly.\n\n<b>References</b>\n<ol><li>Reed C, Chaves SS, Daily Kirley P, et al. Estimating influenza disease burden from population-based surveillance data in the United States. PLoS One. 2015;10(3):e0118369. https://doi.org/10.1371/journal.pone.0118369\u202f </li><li>Rolfes, MA, Foppa, IM, Garg, S, et al. Annual estimates of the burden of seasonal influenza in the United States: A tool for strengthening influenza surveillance and preparedness. Influenza Other Respi Viruses. 2018; 12: 132\u2013 137. https://doi.org/10.1111/irv.12486</li><li>Tokars  JI, Rolfes  MA, Foppa  IM, Reed  C.  An evaluation and update of methods for estimating the number of influenza cases averted by vaccination in the United States.   Vaccine. 2018;36(48):7331-7337. doi:10.1016/j.vaccine.2018.10.026\u202f</li><li>Collier SA, Deng L, Adam EA, Benedict KM, Beshearse EM, Blackstock AJ, Bruce BB, Derado G, Edens C, Fullerton KE, Gargano JW, Geissler AL, Hall AJ, Havelaar AH, Hill VR, Hoekstra RM, Reddy SC, Scallan E, Stokes EK, Yoder JS, Beach MJ. Estimate of Burden and Direct Healthcare Cost of Infectious Waterborne Disease in the United States. Emerg Infect Dis. 2021 Jan;27(1):140-149. doi: 10.3201/eid2701.190676. PMID: 33350905; PMCID: PMC7774540.</li><li>Reed C, Kim IK, Singleton JA,\u202f et al. Estimated influenza illnesses and hospitalizations averted by vaccination\u2013United States, 2013-14 influenza season. MMWR Morb Mortal Wkly Rep. 2014 Dec 12;63(49):1151-4. https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6349a2.htm\u202f</li><li>Reed C, Angulo FJ, Swerdlow DL, et al. Estimates of the Prevalence of Pandemic (H1N1) 2009, United States, April\u2013July 2009. Emerg Infect Dis. 2009;15(12):2004-2007. https://dx.doi.org/10.3201/eid1512.091413 \u202f</li><li>Devine O, Pham H, Gunnels B, et al. Extrapolating Sentinel Surveillance Information to Estimate National COVID-19 Hospital Admission Rates: A Bayesian Modeling Approach. Influenza and Other Respiratory Viruses. https://onlinelibrary.wiley.com/doi/10.1111/irv.70026. Volume18, Issue10. October 2024.</li><li><a ref=\"https://www.cdc.gov/covid/php/covid-net/index.html\">COVID-NET | COVID-19 | CDC\u202f</a></li><li>https://www.cdc.gov/covid/hcp/clinical-care/systematic-review-process.html\u202f </li><li><a ref=\"https://academic.oup.com/pnasnexus/article/1/3/pgac079/6604394?login=false\">Excess natural-cause deaths in California by cause and setting: March 2020 through February 2021 | PNAS Nexus | Oxford Academic (oup.com)</a></li><li>Kruschke, J. K. 2011. Doing Bayesian data analysis: a tutorial with R and BUGS. Elsevier, Amsterdam, Section 3.3.5.</li></ol>",
-            "title": "Preliminary Estimates of Cumulative COVID-19-associated Hospitalizations by Week for 2024-2025",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76518,70 +76642,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xnjn-rdmd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xnjn-rdmd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xnjn-rdmd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xnjn-rdmd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xnjn-rdmd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xnjn-rdmd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xnjn-rdmd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xnjn-rdmd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xnjn-rdmd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/xnjn-rdmd",
+            "issued": "2024-09-23",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "hospitalizations"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xnjn-rdmd",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
+            },
+            "rights": "N/A",
+            "spatial": "US",
+            "temporal": "October 1, 2024 - no specified end date",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Preliminary Estimates of Cumulative COVID-19-associated Hospitalizations by Week for 2024-2025"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/npals/index.html",
+            "accrualPeriodicity": "Irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/application-process/submission.html",
-            "issued": "2022-06-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2021-07-21",
-            "modified": "2025-01-13",
-            "keyword": [
-                "adult day services centers",
-                "covid-19",
-                "long-term care",
-                "research-data-center",
-                "sdoh-access-to-health-care",
-                "sdoh-transportation",
-                "sdoh-use-of-health-care"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xqjn-3jef",
-            "description": "The National Post-acute and Long-term Care Study (NPALS) is a biennial study of major post-acute and long-term care providers and their services users. Seven provider settings are in included. NPALS collects survey data on the residential care community and adult day services sectors, and uses administrative data (available from CMS) for home health, nursing home, hospice, inpatient rehabilitation, and long-term care hospital sectors.\nThe goals of the study are to: estimate the supply of paid, regulated post-acute and long-term care services providers; estimate key policy-relevant characteristics and practices of these providers; estimate the number of post-acute and long-term care services users; estimate key policy-relevant characteristics of these users; produce national and state estimates where feasible; compare across provider sectors; and monitor trends over time.",
-            "title": "National Post-acute and Long-term Care Study: Adult Day Service Provider Restricted Dataset",
+            "describedBy": "https://www.cdc.gov/nchs/data/npals/2020-NPALS-ADSC-Questionnaire-Center.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The National Post-acute and Long-term Care Study (NPALS) is a biennial study of major post-acute and long-term care providers and their services users. Seven provider settings are in included. NPALS collects survey data on the residential care community and adult day services sectors, and uses administrative data (available from CMS) for home health, nursing home, hospice, inpatient rehabilitation, and long-term care hospital sectors.\nThe goals of the study are to: estimate the supply of paid, regulated post-acute and long-term care services providers; estimate key policy-relevant characteristics and practices of these providers; estimate the number of post-acute and long-term care services users; estimate key policy-relevant characteristics of these users; produce national and state estimates where feasible; compare across provider sectors; and monitor trends over time.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76590,40 +76711,49 @@
                     "title": "National Post-acute and Long-term Care Study: Adult Day Service Provider Restricted Dataset"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xqjn-3jef",
+            "issued": "2022-06-16",
+            "keyword": [
+                "adult day services centers",
+                "covid-19",
+                "long-term care",
+                "research-data-center",
+                "sdoh-access-to-health-care",
+                "sdoh-transportation",
+                "sdoh-use-of-health-care"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/npals/index.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/application-process/submission.html",
             "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data/npals/2020-NPALS-ADSC-Questionnaire-Center.pdf",
-            "accrualPeriodicity": "Irregular",
+            "temporal": "2020-01-01/2021-07-21",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Post-acute and Long-term Care Study: Adult Day Service Provider Restricted Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/xqmi-ykpp",
-            "issued": "2024-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Research, Pathology and Physiology Research Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xqmi-ykpp",
             "description": "Adipose tissue (AT), an endocrine organ, plays a central role in maintenance of whole-body energy homeostasis through its release of adipokines. Obesity, affecting over 40% of American adults, disrupts adipocyte metabolism leading to chronic systemic inflammation and metabolic dysfunction (MetDys). MetDys is associated with impaired lung function, pulmonary hypertension, and asthma. The aim of this study was to investigate the effects of silica inhalation in a pre-existing MetDys animal model to determine if an occupational exposure of silica dust has the potential to initiate or further the progression of MetDys associated conditions.",
-            "title": "Effects of Crystalline Silica Inhalation in a High-Fat Western Diet",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76631,43 +76761,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xqmi-ykpp",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/xqmi-ykpp",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Effects of Crystalline Silica Inhalation in a High-Fat Western Diet"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xsi2-33p5",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "cholera",
-                "coccidioidomycosis",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xsi2-33p5",
             "description": "NNDSS - Table 1H. Cholera to Coccidioidomycosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1H. Cholera to Coccidioidomycosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76675,64 +76796,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xsi2-33p5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xsi2-33p5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xsi2-33p5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xsi2-33p5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xsi2-33p5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xsi2-33p5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xsi2-33p5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xsi2-33p5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xsi2-33p5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xsi2-33p5",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "cholera",
+                "coccidioidomycosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xsi2-33p5",
+            "modified": "2020-01-02",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1H. Cholera to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xssa-9qw5",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "nedss",
-                "netss",
-                "nndss",
-                "rubella",
-                "rubella congenital syndrome",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xssa-9qw5",
             "description": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76740,66 +76861,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xssa-9qw5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xssa-9qw5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xssa-9qw5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xssa-9qw5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xssa-9qw5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xssa-9qw5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xssa-9qw5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xssa-9qw5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xssa-9qw5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xssa-9qw5",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "rubella",
+                "rubella congenital syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xssa-9qw5",
+            "modified": "2022-02-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-10",
-            "references": [
-                "https://chronicdata.cdc.gov/d/5qag-uzp2"
-            ],
-            "keyword": [
-                "legislation",
-                "osh",
-                "policy",
-                "preemption",
-                "state system",
-                "tobacco"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OSHData Support",
                 "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xsta-sbh5",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Preemption/xsta-sbh5",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation\u2014Preemption. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies.  Data are reported on a quarterly basis. Data include information related to statutory state preemption of more stringent local laws on advertising, smokefree indoor air, youth access and licensure.",
-            "title": "CDC STATE System Tobacco Legislation - Preemption",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76807,61 +76927,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xsta-sbh5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xsta-sbh5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xsta-sbh5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xsta-sbh5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xsta-sbh5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xsta-sbh5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xsta-sbh5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xsta-sbh5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xsta-sbh5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Preemption/xsta-sbh5",
+            "identifier": "https://data.cdc.gov/api/views/xsta-sbh5",
+            "issued": "2023-07-18",
+            "keyword": [
+                "legislation",
+                "osh",
+                "policy",
+                "preemption",
+                "state system",
+                "tobacco"
+            ],
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2025-01-10",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://chronicdata.cdc.gov/d/5qag-uzp2"
+            ],
             "theme": [
                 "Legislation"
-            ]
+            ],
+            "title": "CDC STATE System Tobacco Legislation - Preemption"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xsu4-4sk9",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-10-18",
-            "@type": "dcat:Dataset",
-            "modified": "2016-10-18",
-            "keyword": [
-                "cdc",
-                "centers for disease control and prevention"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xsu4-4sk9",
             "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014,  Region 9 - San Francisco",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76869,72 +76995,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xsu4-4sk9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xsu4-4sk9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xsu4-4sk9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xsu4-4sk9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xsu4-4sk9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xsu4-4sk9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xsu4-4sk9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xsu4-4sk9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xsu4-4sk9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xsu4-4sk9",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xsu4-4sk9",
+            "modified": "2016-10-18",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Motor Vehicle"
-            ]
+            ],
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014,  Region 9 - San Francisco"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-06-03",
-            "@type": "dcat:Dataset",
-            "temporal": "2000/2018",
-            "modified": "2023-08-28",
-            "keyword": [
-                "african americans",
-                "age",
-                "continental population groups",
-                "disasters",
-                "emergency service",
-                "european continental ancestry group",
-                "health us",
-                "hospital",
-                "hospitals",
-                "outpatients",
-                "physicians",
-                "physicians' offices",
-                "sdoh-use-of-health-care",
-                "sex"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:healthus@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xt86-xqxz",
             "description": "Data on visits to physician offices, hospital outpatient departments and hospital emergency departments by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. Note that the data file available here has more recent years of data than what is shown in the PDF or Excel version. Data for 2017 physician office visits are not available.\n\nSOURCE: NCHS, National Ambulatory Medical Care Survey and National Hospital Ambulatory Medical Care Survey. For more information on the National Ambulatory Medical Care Survey and the National Hospital Ambulatory Medical Care Survey, see the corresponding Appendix entries at https://www.cdc.gov/nchs/data/hus/hus17_appendix.pdf.",
-            "title": "Visits to physician offices, hospital outpatient departments, and hospital emergency departments, by age, sex, and race: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76942,67 +77055,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xt86-xqxz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xt86-xqxz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xt86-xqxz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xt86-xqxz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xt86-xqxz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xt86-xqxz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xt86-xqxz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xt86-xqxz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xt86-xqxz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/xt86-xqxz",
+            "issued": "2021-06-03",
+            "keyword": [
+                "african americans",
+                "age",
+                "continental population groups",
+                "disasters",
+                "emergency service",
+                "european continental ancestry group",
+                "health us",
+                "hospital",
+                "hospitals",
+                "outpatients",
+                "physicians",
+                "physicians' offices",
+                "sdoh-use-of-health-care",
+                "sex"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-08-28",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "2000/2018",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Visits to physician offices, hospital outpatient departments, and hospital emergency departments, by age, sex, and race: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xuah-ug7z",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "babesiosis",
-                "campylobacteriosis",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xuah-ug7z",
             "description": "NNDSS - Table II. Babesiosis to Campylobacteriosis - 2017. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions.\r\n \r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Babesiosis to Campylobacteriosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77010,55 +77130,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xuah-ug7z/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xuah-ug7z/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xuah-ug7z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xuah-ug7z/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xuah-ug7z/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xuah-ug7z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xuah-ug7z/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xuah-ug7z/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xuah-ug7z/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xuah-ug7z",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "babesiosis",
+                "campylobacteriosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xuah-ug7z",
+            "modified": "2018-01-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Babesiosis to Campylobacteriosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/xup8-ahj8",
-            "issued": "2024-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Division of Safety Research, Protective Technology Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xup8-ahj8",
             "description": "Up-to-date anthropometric information (body dimensions) of the U.S. firefighter population is needed for updating ergonomic and safety specifications for fire apparatus and firefighter protective equipment. Seventy-one measurements relevant to the design of seats, seat belts, cabs, turnout gear, gloves, and head-and-face gear are presented in this webpage. Forty of the 71 measurements were collected with the participants in fitted shorts in both standing and seated postures. Twenty-one of the 71 measurements were collected while the participants were wearing their personal turnout gear, including personal selection of tools stored in their pockets, in both standing and seated postures. Ten of the 71 measurements were hand- and head/face-related dimensions extracted from hand and head/face scans. The data obtained in this study provide the first available U.S. national firefighter anthropometric information which will benefit the design of future fire apparatus and protective equipment to better protect firefi",
-            "title": "Firefighter Body Dimensions for Updating Safety Specifications for Fire Apparatus and Firefighter Protective Equipment",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77066,45 +77196,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xup8-ahj8",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/xup8-ahj8",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Firefighter Body Dimensions for Updating Safety Specifications for Fire Apparatus and Firefighter Protective Equipment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xv7k-8e7s",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "keyword": [
-                "2016",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "shiga toxin-producing e. coli",
-                "shigellosis",
-                "stec",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xv7k-8e7s",
             "description": "NNDSS - Table II. Shiga toxin to Shigellosis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.   NP:  Nationally notifiable but not published.   Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n \r\n* Case counts for reporting year 2016 are provisional and subject to change.   For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.   Data for TB are displayed in Table IV, which appears quarterly.  \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table II to facilitate case count verification with reporting jurisdictions.\r\n\u00a7 Includes E. coli O157:H7; Shiga toxin-positive, serogroup non-O157; and Shiga toxin-positive, not serogrouped.",
-            "title": "NNDSS - Table II. Shiga toxin to Shigellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77112,66 +77231,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xv7k-8e7s/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xv7k-8e7s/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xv7k-8e7s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xv7k-8e7s/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xv7k-8e7s/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xv7k-8e7s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xv7k-8e7s/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xv7k-8e7s/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xv7k-8e7s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xv7k-8e7s",
+            "issued": "2017-01-05",
+            "keyword": [
+                "2016",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "shiga toxin-producing e. coli",
+                "shigellosis",
+                "stec",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xv7k-8e7s",
+            "modified": "2017-01-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Shiga toxin to Shigellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xvdv-hq7x",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "all ages",
-                "confirmed",
-                "invasive pneumococcal disease",
-                "nedss",
-                "netss",
-                "nndss",
-                "probable",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xvdv-hq7x",
             "description": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77179,44 +77298,97 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xvdv-hq7x/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xvdv-hq7x/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xvdv-hq7x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xvdv-hq7x/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xvdv-hq7x/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xvdv-hq7x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xvdv-hq7x/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/xvdv-hq7x/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xvdv-hq7x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xvdv-hq7x",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "all ages",
+                "confirmed",
+                "invasive pneumococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xvdv-hq7x",
+            "modified": "2022-02-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/prams/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-05",
-            "references": [
-                "https://www.cdc.gov/prams/index.htm",
-                "https://www.cdc.gov/prams/pramstat/index.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DRH Public Inquiries",
+                "hasEmail": "mailto:PRAMSProposals@cdc.gov"
+            },
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2010/xvu4-xjdb",
+            "description": "2010. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xvu4-xjdb/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xvu4-xjdb/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/xvu4-xjdb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xvu4-xjdb/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/xvu4-xjdb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xvu4-xjdb/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/xvu4-xjdb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xvu4-xjdb",
+            "issued": "2023-07-18",
             "keyword": [
                 "abuse",
                 "alcohol use",
@@ -77238,63 +77410,67 @@
                 "unintended pregnancy",
                 "wic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DRH Public Inquiries",
-                "hasEmail": "mailto:PRAMSProposals@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/prams/index.htm",
+            "modified": "2023-09-05",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/xvu4-xjdb",
-            "description": "2010. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2010",
-            "programCode": [
-                "009:020"
+            "references": [
+                "https://www.cdc.gov/prams/index.htm",
+                "https://www.cdc.gov/prams/pramstat/index.html"
             ],
+            "theme": [
+                "Maternal & Child Health"
+            ],
+            "title": "CDC PRAMStat Data for 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
+            "bureauCode": [
+                "009:20"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC-INFO",
+                "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
+            },
+            "description": "COVID-19 Deaths Among Healthcare Personnel, by week",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/xvu4-xjdb/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/xwa7-cukt/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xvu4-xjdb/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xvu4-xjdb/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xwa7-cukt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xwa7-cukt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xvu4-xjdb/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xvu4-xjdb/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xwa7-cukt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xwa7-cukt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xvu4-xjdb/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xvu4-xjdb/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xwa7-cukt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xwa7-cukt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2010/xvu4-xjdb",
-            "theme": [
-                "Maternal & Child Health"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xwa7-cukt",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/xwa7-cukt",
             "issued": "2023-09-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
             "keyword": [
                 "coronavirus",
                 "covid-19",
@@ -77303,67 +77479,63 @@
                 "healthcare worker",
                 "ncird-corvd"
             ],
+            "landingPage": "https://data.cdc.gov/d/xwa7-cukt",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "spatial": "US",
+            "theme": [
+                "Case Surveillance"
+            ],
+            "title": "COVID-19 Deaths Among Healthcare Personnel, by week - ARCHIVED"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
-                "fn": "CDC-INFO",
-                "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
+                "fn": "PLACES Public Inquiries",
+                "hasEmail": "mailto:places@cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/xwa7-cukt",
-            "description": "COVID-19 Deaths Among Healthcare Personnel, by week",
-            "title": "COVID-19 Deaths Among Healthcare Personnel, by week - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "This dataset contains model-based place (incorporated and census designated places) estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia \u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. These data can be joined with the 2019 Census TIGER/Line place boundary file in a GIS system to produce maps for 36 measures at the place level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=2c3deb0c05a748b391ea8c9cf9903588",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/xwa7-cukt/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/xx8k-iu94/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xwa7-cukt/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xwa7-cukt/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xx8k-iu94/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xx8k-iu94/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xwa7-cukt/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xwa7-cukt/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xx8k-iu94/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xx8k-iu94/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xwa7-cukt/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xwa7-cukt/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xx8k-iu94/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xx8k-iu94/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
-            "accrualPeriodicity": "No longer updated (dataset archived)",
-            "theme": [
-                "Case Surveillance"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/xx8k-iu94",
             "issued": "2024-07-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
             "keyword": [
                 "behaviors",
                 "city",
@@ -77378,96 +77550,54 @@
                 "risk",
                 "status"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "PLACES Public Inquiries",
-                "hasEmail": "mailto:places@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xx8k-iu94",
-            "description": "This dataset contains model-based place (incorporated and census designated places) estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia \u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. These data can be joined with the 2019 Census TIGER/Line place boundary file in a GIS system to produce maps for 36 measures at the place level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=2c3deb0c05a748b391ea8c9cf9903588",
-            "title": "PLACES: Place Data (GIS Friendly Format), 2023 release",
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "modified": "2024-08-26",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/xx8k-iu94/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xx8k-iu94/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xx8k-iu94/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xx8k-iu94/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xx8k-iu94/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xx8k-iu94/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xx8k-iu94/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
             ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "PLACES: Place Data (GIS Friendly Format), 2023 release"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xxzc-cs4a",
-            "issued": "2023-06-20",
             "@type": "dcat:Dataset",
-            "modified": "2023-07-10",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jimmy Yun, CTR",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
+            "description": "",
             "identifier": "https://data.cdc.gov/api/views/xxzc-cs4a",
+            "issued": "2023-06-20",
+            "landingPage": "https://data.cdc.gov/d/xxzc-cs4a",
+            "modified": "2023-07-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.cdc.gov"
             },
-            "description": "",
             "title": "We Are Moving"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/xy5u-nzbq",
-            "issued": "2024-12-03",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-03",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xy5u-nzbq",
             "description": "Workers that regularly use vibrating hand tools as part of their job are at risk of developing hand-arm vibration syndrome (HAVS).  HAVS is characterized by cold-induced vasospasms that result in blanching of the fingers and hands, loss of sensation, pain, and reductions in manual dexterity, all of which can affect a worker\u2019s ability to perform their job and their quality of life.  Vibration exposure significantly contributes to the development of these symptoms by increasing the stress and strain within exposed tissues, which in turn can affect functioning of blood vessels, nerves and sensory receptors in those tissues.",
-            "title": "Applied pressure alters circulating hormone levels and biomarkers of peripheral vascular, sensorineural dysfunction",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77475,20 +77605,65 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xy5u-nzbq",
+            "issued": "2024-12-03",
+            "landingPage": "https://data.cdc.gov/d/xy5u-nzbq",
+            "modified": "2024-12-03",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Applied pressure alters circulating hormone levels and biomarkers of peripheral vascular, sensorineural dysfunction"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "Provisional deaths involving coronavirus disease 2019 (COVID-19) and deaths from all causes reported to NCHS by week the death occurred, HHS region of occurrence, race and Hispanic origin, and age group (0-24, 25-64, 65+ years), from 2015-2021.\n\nUnited States death counts include the 50 states, plus the District of Columbia and New York City. The ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York, New York City; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xy7w-35q7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xy7w-35q7/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/xy7w-35q7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xy7w-35q7/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/xy7w-35q7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xy7w-35q7/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/xy7w-35q7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/xy7w-35q7",
             "issued": "2021-09-15",
-            "temporal": "2015/2021",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
             "keyword": [
                 "age",
                 "age group",
@@ -77506,67 +77681,64 @@
                 "united states",
                 "weekly"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-01",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/xy7w-35q7",
-            "description": "Provisional deaths involving coronavirus disease 2019 (COVID-19) and deaths from all causes reported to NCHS by week the death occurred, HHS region of occurrence, race and Hispanic origin, and age group (0-24, 25-64, 65+ years), from 2015-2021.\n\nUnited States death counts include the 50 states, plus the District of Columbia and New York City. The ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York, New York City; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.",
-            "title": "AH Provisional COVID-19 Deaths by HHS Region, Race, and Age, 2015-2021",
-            "programCode": [
-                "009:020"
+            "temporal": "2015/2021",
+            "theme": [
+                "NCHS"
+            ],
+            "title": "AH Provisional COVID-19 Deaths by HHS Region, Race, and Age, 2015-2021"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "PLACES Public Inquiries",
+                "hasEmail": "mailto:places@cdc.gov"
+            },
+            "description": "This dataset contains model-based county-level estimates for the PLACES 2022 release in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. Project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2020 or 2019 county population estimates, and American Community Survey (ACS) 2016\u20132020 or 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. These data can be joined with the census 2020 county boundary file in a GIS system to produce maps for 29 measures at the county level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software. https://cdcarcgis.maps.arcgis.com/home/item.html?id=3b7221d4e47740cab9235b839fa55cd7",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/xy7w-35q7/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/xyst-f73f/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xy7w-35q7/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xy7w-35q7/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xyst-f73f/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xyst-f73f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xy7w-35q7/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xy7w-35q7/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xyst-f73f/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xyst-f73f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xy7w-35q7/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xy7w-35q7/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xyst-f73f/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xyst-f73f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
-            "theme": [
-                "NCHS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/xyst-f73f",
             "issued": "2023-06-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
             "keyword": [
                 "behaviors",
                 "county",
@@ -77579,66 +77751,66 @@
                 "risk",
                 "status"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "PLACES Public Inquiries",
-                "hasEmail": "mailto:places@cdc.gov"
-            },
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "modified": "2023-08-25",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/xyst-f73f",
-            "description": "This dataset contains model-based county-level estimates for the PLACES 2022 release in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. Project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2020 or 2019 county population estimates, and American Community Survey (ACS) 2016\u20132020 or 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. These data can be joined with the census 2020 county boundary file in a GIS system to produce maps for 29 measures at the county level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software. https://cdcarcgis.maps.arcgis.com/home/item.html?id=3b7221d4e47740cab9235b839fa55cd7",
-            "title": "PLACES: County Data (GIS Friendly Format), 2022 release",
-            "programCode": [
-                "009:020"
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "theme": [
+                "500 Cities & Places"
+            ],
+            "title": "PLACES: County Data (GIS Friendly Format), 2022 release"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DRH Public Inquiries",
+                "hasEmail": "mailto:PRAMSProposals@cdc.gov"
+            },
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2004/xyxp-dxa9",
+            "description": "2004. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/xyst-f73f/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/xyxp-dxa9/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xyst-f73f/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xyst-f73f/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xyxp-dxa9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xyxp-dxa9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xyst-f73f/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xyst-f73f/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xyxp-dxa9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xyxp-dxa9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xyst-f73f/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xyst-f73f/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/xyxp-dxa9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/xyxp-dxa9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "500 Cities & Places"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/prams/index.htm",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/xyxp-dxa9",
             "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-05",
-            "references": [
-                "https://www.cdc.gov/prams/index.htm",
-                "https://www.cdc.gov/prams/pramstat/index.html"
-            ],
             "keyword": [
                 "abuse",
                 "alcohol use",
@@ -77660,102 +77832,37 @@
                 "unintended pregnancy",
                 "wic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DRH Public Inquiries",
-                "hasEmail": "mailto:PRAMSProposals@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xyxp-dxa9",
-            "description": "2004. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2004",
+            "landingPage": "https://www.cdc.gov/prams/index.htm",
+            "modified": "2023-09-05",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/xyxp-dxa9/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xyxp-dxa9/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xyxp-dxa9/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/xyxp-dxa9/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xyxp-dxa9/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/xyxp-dxa9/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/xyxp-dxa9/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
+            "references": [
+                "https://www.cdc.gov/prams/index.htm",
+                "https://www.cdc.gov/prams/pramstat/index.html"
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2004/xyxp-dxa9",
             "theme": [
                 "Maternal & Child Health"
-            ]
+            ],
+            "title": "CDC PRAMStat Data for 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "public",
-            "issued": "2015-12-02",
-            "@type": "dcat:Dataset",
-            "temporal": "1990-01-01/2018-12-31",
-            "modified": "2022-05-09",
-            "references": [
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr51/nvsr51_12.pdf",
-                "ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/NVSR/62_09/",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr63/nvsr63_04.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr62/nvsr62_09.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr64/nvsr64_01.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr64/nvsr64_12.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr67/nvsr67_01.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr67/nvsr67_08-508.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13-508.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr70/nvsr70-02-508.pdf"
-            ],
-            "keyword": [
-                "nchs",
-                "state teen birth trends",
-                "teen births",
-                "united states",
-                "u.s. and state trends on teen births",
-                "u.s. teen birth rate"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:births@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/y268-sna3",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "This dataset assembles all final birth data for females aged 15\u201319, 15\u201317, and 18\u201319 for the United States and each of the 50 states.\r\n\r\nData are based on 100% of birth certificates filed in all 50 states. All the teen birth rates in this dashboard reflect the latest revisions to Census populations (i.e., the intercensal populations) and thus provide a consistent series of accurate rates for the past 25 years. The denominators of the teen birth rates for 1991\u20131999 have been revised to incorporate the results of the 2000 Census. The denominators of the teen birth rates for 2001\u20132009 have revised to incorporate the results of the 2010 Census.",
-            "title": "NCHS - U.S. and State Trends on Teen Births",
-            "isPartOf": "Teen births by state 1990 through most current data",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77763,73 +77870,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y268-sna3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y268-sna3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y268-sna3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/y268-sna3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y268-sna3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y268-sna3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y268-sna3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y268-sna3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y268-sna3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/y268-sna3",
+            "isPartOf": "Teen births by state 1990 through most current data",
+            "issued": "2015-12-02",
+            "keyword": [
+                "nchs",
+                "state teen birth trends",
+                "teen births",
+                "united states",
+                "u.s. and state trends on teen births",
+                "u.s. teen birth rate"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-05-09",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr51/nvsr51_12.pdf",
+                "ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/NVSR/62_09/",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr63/nvsr63_04.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr62/nvsr62_09.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr64/nvsr64_01.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr64/nvsr64_12.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr67/nvsr67_01.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr67/nvsr67_08-508.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13-508.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr70/nvsr70-02-508.pdf"
+            ],
+            "rights": "public",
+            "spatial": "50 states and District of Columbia",
+            "temporal": "1990-01-01/2018-12-31",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - U.S. and State Trends on Teen Births"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/y2iy-8irm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2021-09-10",
-            "keyword": [
-                "covid-19",
-                "executive order",
-                "government order",
-                "legal epidemiology",
-                "mitigation",
-                "proclamation",
-                "public health order",
-                "shelter-in-place",
-                "social distancing",
-                "stay-at-home"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Craig Kassinger",
                 "hasEmail": "mailto:cak8@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Environmental Public Health Tracking"
-            },
-            "identifier": "https://data.cdc.gov/api/views/y2iy-8irm",
             "description": "State and territorial executive orders, administrative orders, resolutions, and proclamations are collected from government websites and cataloged and coded using Microsoft Excel by one coder with one or more additional coders conducting quality assurance.\n\nData were collected to determine when individuals in states and territories were subject to executive orders, administrative orders, resolutions, and proclamations for COVID-19 that require or recommend people stay in their homes. Data consists exclusively of state and territorial orders, many of which apply to specific counties within their respective state or territory; therefore, data is broken down to the county level.\n\nThese data are derived from the publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly require or recommend individuals stay at home found by the CDC, COVID-19 Community Intervention and At-Risk Task Force, Monitoring and Evaluation Team & CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 15, 2020 through August 15, 2021. These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded; news media reports on restrictions were excluded. Recommendations not included in an order are not included in these data. These data do not include mandatory business closures, curfews, or limitations on public or private gatherings. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
-            "title": "U.S. State and Territorial Stay-At-Home Orders: March 15, 2020 \u2013 August 15, 2021 by County by Day",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77837,62 +77955,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y2iy-8irm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y2iy-8irm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y2iy-8irm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/y2iy-8irm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y2iy-8irm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y2iy-8irm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y2iy-8irm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y2iy-8irm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y2iy-8irm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/y2iy-8irm",
+            "issued": "2021-09-10",
+            "keyword": [
+                "covid-19",
+                "executive order",
+                "government order",
+                "legal epidemiology",
+                "mitigation",
+                "proclamation",
+                "public health order",
+                "shelter-in-place",
+                "social distancing",
+                "stay-at-home"
+            ],
+            "landingPage": "https://data.cdc.gov/d/y2iy-8irm",
+            "modified": "2021-09-10",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Environmental Public Health Tracking"
+            },
             "theme": [
                 "Policy Surveillance"
-            ]
+            ],
+            "title": "U.S. State and Territorial Stay-At-Home Orders: March 15, 2020 \u2013 August 15, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/brfss/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-06",
-            "keyword": [
-                "behavioral",
-                "brfss",
-                "factor",
-                "risk",
-                "survey"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DPH Public Inquiries",
                 "hasEmail": "mailto:PublicInquiriesDPH@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/y4ft-s73h",
             "description": "1995-2010. BRFSS land line only prevalence data. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Data will be updated annually as it becomes available. Detailed information on sampling methodology and quality assurance can be found on the BRFSS website (http://www.cdc.gov/brfss). Methodology: http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf Glossary: https://chronicdata.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct/data",
-            "title": "Behavioral Risk Factor Surveillance System (BRFSS) Prevalence Data (2010 and prior)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77900,68 +78023,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y4ft-s73h/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y4ft-s73h/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y4ft-s73h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/y4ft-s73h/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y4ft-s73h/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y4ft-s73h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y4ft-s73h/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y4ft-s73h/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y4ft-s73h/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/y4ft-s73h",
+            "issued": "2023-07-19",
+            "keyword": [
+                "behavioral",
+                "brfss",
+                "factor",
+                "risk",
+                "survey"
+            ],
+            "landingPage": "https://www.cdc.gov/brfss/",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-09-06",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Behavioral Risk Factors"
-            ]
+            ],
+            "title": "Behavioral Risk Factor Surveillance System (BRFSS) Prevalence Data (2010 and prior)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/y4ut-ybj7",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "confirmed",
-                "hepatitis b",
-                "hepatitis c acute",
-                "nedss",
-                "netss",
-                "nndss",
-                "perinatal infection",
-                "probable",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/y4ut-ybj7",
             "description": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 For acute Hepatitis C, only confirmed cases were verified.",
-            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77969,67 +78087,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y4ut-ybj7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y4ut-ybj7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y4ut-ybj7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/y4ut-ybj7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y4ut-ybj7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y4ut-ybj7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y4ut-ybj7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y4ut-ybj7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y4ut-ybj7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/y4ut-ybj7",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "confirmed",
+                "hepatitis b",
+                "hepatitis c acute",
+                "nedss",
+                "netss",
+                "nndss",
+                "perinatal infection",
+                "probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/y4ut-ybj7",
+            "modified": "2021-01-07",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/y4x9-2nqn",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "acute",
-                "by type) a",
-                "by type) b",
-                "hemolytic uremic syndrome post-diarrheal",
-                "hepatitis (viral",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/y4x9-2nqn",
             "description": "NNDSS - TABLE 1P.  Hemolytic uremic syndrome post-diarrheal to Hepatitis (viral, acute, by type), B - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1P.  Hemolytic uremic syndrome post-diarrheal to Hepatitis (viral, acute, by type), B",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78037,49 +78155,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y4x9-2nqn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y4x9-2nqn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y4x9-2nqn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/y4x9-2nqn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y4x9-2nqn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y4x9-2nqn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y4x9-2nqn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y4x9-2nqn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y4x9-2nqn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/y4x9-2nqn",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "acute",
+                "by type) a",
+                "by type) b",
+                "hemolytic uremic syndrome post-diarrheal",
+                "hepatitis (viral",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/y4x9-2nqn",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1P.  Hemolytic uremic syndrome post-diarrheal to Hepatitis (viral, acute, by type), B"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/y52v-k5rz",
-            "issued": "2024-07-23",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/y52v-k5rz",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78087,66 +78220,50 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y52v-k5rz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y52v-k5rz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y52v-k5rz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/y52v-k5rz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y52v-k5rz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y52v-k5rz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y52v-k5rz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y52v-k5rz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y52v-k5rz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/y52v-k5rz",
+            "issued": "2024-07-23",
+            "landingPage": "https://data.cdc.gov/d/y52v-k5rz",
+            "modified": "2024-07-23",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "dhds_dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-05-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-27",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "deaths",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "puerto rico",
-                "state",
-                "united states",
-                "weekly"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/y5bj-9g5w",
             "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nThis visualization provides weekly data on the number of deaths from all causes by jurisdiction of occurrence and age group. Counts of deaths in more recent weeks can be compared with counts from earlier years to determine if the number is higher than expected.",
-            "title": "Weekly Counts of Deaths by Jurisdiction and Age",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78154,69 +78271,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y5bj-9g5w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y5bj-9g5w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y5bj-9g5w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/y5bj-9g5w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y5bj-9g5w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y5bj-9g5w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y5bj-9g5w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y5bj-9g5w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y5bj-9g5w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/y5bj-9g5w",
+            "issued": "2020-05-28",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "puerto rico",
+                "state",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-09-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States, Puerto Rico",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Weekly Counts of Deaths by Jurisdiction and Age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/y6uv-t34t",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-01-08",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "2014",
-                "lyme disease",
-                "malaria",
-                "meningococcal invasive all serogroups",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/y6uv-t34t",
             "description": "NNDSS - Table II. Lyme disease to Meningococcal - 2014In this Table, all conditions with a 5-year average annual national total of more than or equals 1,000 cases but less than or equals 10,000 cases will be displayed (\ufffd\ufffd\ufffd 1,000 and \ufffd\ufffd_ 10,000). The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Case counts for reporting years 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd\ufffd Data for meningococcal disease, invasive caused by serogroups A, C, Y, & W-135; serogroup B; other serogroup; and unknown serogroup are available in Table I.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
-            "title": "NNDSS - Table II. Lyme disease to Meningococcal",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78224,59 +78343,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y6uv-t34t/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y6uv-t34t/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y6uv-t34t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/y6uv-t34t/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y6uv-t34t/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y6uv-t34t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y6uv-t34t/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y6uv-t34t/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y6uv-t34t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/y6uv-t34t",
+            "issued": "2015-01-08",
+            "keyword": [
+                "2014",
+                "lyme disease",
+                "malaria",
+                "meningococcal invasive all serogroups",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/y6uv-t34t",
+            "modified": "2015-08-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Lyme disease to Meningococcal"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/y8pa-p62q",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-09-14",
-            "@type": "dcat:Dataset",
-            "modified": "2016-09-14",
-            "keyword": [
-                "cdc",
-                "centers for disease control and prevention"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/y8pa-p62q",
             "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2014 national data: National Occupant Protection Use Survey (NOPUS), 2014.  Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 state data: Seat Belt Use in 2014- Use Rates in the States and Territories",
-            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 7 - Kansas City",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78284,55 +78410,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y8pa-p62q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y8pa-p62q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y8pa-p62q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/y8pa-p62q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y8pa-p62q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y8pa-p62q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/y8pa-p62q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/y8pa-p62q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/y8pa-p62q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/y8pa-p62q",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/y8pa-p62q",
+            "modified": "2016-09-14",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Motor Vehicle"
-            ]
+            ],
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 7 - Kansas City"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/y93j-qcuq",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division, Toxicology and Molecular Biology Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/y93j-qcuq",
             "description": "In the oil and gas industry, workers are potentially exposed to crude oil or crude oil vapor (COV) during upstream (drilling and extraction), midstream (transportation and storage), as well as downstream (refining) activities.  Worker exposure to various fractions of crude oil have been linked to mortality, as well as musculoskeletal, respiratory, gastrointestinal, circulatory problems, and cancer.  During the Gulf of Mexico Deepwater Horizon (DWH) oil spill, response workers were exposed to a variety of chemical hazards including volatile organic compounds (VOCs), polycyclic aromatic hydrocarbons (PAHs), heavy metals, as well as components of the oil dispersants employed to disperse the oil.  The Gulf Long-term Follow-up (GuLF) STUDY had reported that workers involved in the cleanup operations experienced adverse hematologic, pulmonary, hepatic, and cardiac problems.  However, long-term neurological effects remain unknown.\n\nHealth Hazard Evaluation (HHE) surveys conducted by NIOSH among the cleanup workers identified a variety of health effects, including neurological symptoms.  Unfortunately, as a significant number of response workers who experienced health symptoms were exposed to both crude oil and the oil dispersant that was aerially sprayed to the contain the spill, the health effects of crude oil exposures alone were difficult to discern from these surveys.  It is here that laboratory-based studies are advantageous as they can provide ample health risk information to establish the toxicological potential of the various chemical hazards at the workplace.  To that end, the present work evaluated the neurotoxic risks of COV generated from the Macondo well crude oil that was used as a surrogate for the DWH crude oil.",
-            "title": "Biological effects of inhaled crude oil vapor VI. Altered biogenic amine neurotransmitters and neural protein expression",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78340,34 +78470,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/y93j-qcuq",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/y93j-qcuq",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Biological effects of inhaled crude oil vapor VI. Altered biogenic amine neurotransmitters and neural protein expression"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/ya5p-jf7v",
-            "issued": "2024-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Research, Allergy and Clinical Immunology Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ya5p-jf7v",
             "description": "Occupational immune diseases are some of the most common illnesses that affect workers in the United States.  The Healthcare and Social Assistance Sector (HCSA) has one of the highest incidence of allergic disease compared to other industrial sectors. Individuals in this sector are frequently exposed to a variety of high-level cleaners and disinfectants along with antiseptics for the purposes of sterilization of surfaces, medical and surgical instruments, and reducing the incidence of nosocomial infections.  The range of specificity and effectiveness of these agents is very diverse based on the type of chemical used.  Commonly used antimicrobials include: alcohol, chlorine, iodine based agents; phenols; hydrogen peroxide; and quaternary ammonium compounds (QAC).   While the importance of these kinds of chemicals is understood, many of these agents are also known to directly contribute to allergic disease.  Antimicrobials including disinfectants and antiseptics are unique in that they have been identified to c",
-            "title": "Antimicrobials and Allergic Disease: Identifying Novel Biomarkers and Mechanisms of Action",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78375,40 +78505,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ya5p-jf7v",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/ya5p-jf7v",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Antimicrobials and Allergic Disease: Identifying Novel Biomarkers and Mechanisms of Action"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ya9m-pyut",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-12-05",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "brfss",
-                "current smokers",
-                "former smoker",
-                "non-smoker"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ya9m-pyut",
             "description": "The 2011 BRFSS data reflects a change in weighting methodology (raking) and the addition of cell phone only respondents. Shifts in observed prevalence from 2010 to 2011 for BRFSS measures will likely reflect the new methods of measuring risk factors, rather than true trends in risk-factor prevalence. A break in trend lines after 2010 is used to reflect this change in methodolgy. Percentages are weighted to population characteristics. Data are not available if it did not meet BRFSS stability requirements.For more information on these requirements, as well as risk factors and calculated variables, see the Technical Documents and Survey Data for a specific year - http://www.cdc.gov/brfss/annual_data/annual_data.htm.Recommended citation: Centers for Disease Control and Prevention (CDC). Behavioral Risk Factor Surveillance System. Atlanta, Georgia: U.S. Department of Health and Human Services, Centers for Disease Control and Prevention, [appropriate year].",
-            "title": "BRFSS Prevalence and Trends Data: Tobacco Use - Four Level Smoking Data for 2011",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78416,67 +78540,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ya9m-pyut/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ya9m-pyut/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ya9m-pyut/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ya9m-pyut/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ya9m-pyut/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ya9m-pyut/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ya9m-pyut/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ya9m-pyut/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ya9m-pyut/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ya9m-pyut",
+            "issued": "2013-12-05",
+            "keyword": [
+                "brfss",
+                "current smokers",
+                "former smoker",
+                "non-smoker"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ya9m-pyut",
+            "modified": "2015-08-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Smoking & Tobacco Use"
-            ]
+            ],
+            "title": "BRFSS Prevalence and Trends Data: Tobacco Use - Four Level Smoking Data for 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/yakh-mjxn",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "cryptosporidiosis",
-                "dengue",
-                "dengue virus infection",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "severe dengue",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yakh-mjxn",
             "description": "NNDSS - Table II. Cryptosporidiosis to Dengue - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Includes data for dengue and dengue-like illness.",
-            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78484,64 +78602,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yakh-mjxn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yakh-mjxn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yakh-mjxn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/yakh-mjxn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yakh-mjxn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yakh-mjxn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yakh-mjxn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yakh-mjxn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yakh-mjxn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/yakh-mjxn",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "cryptosporidiosis",
+                "dengue",
+                "dengue virus infection",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "severe dengue",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/yakh-mjxn",
+            "modified": "2018-01-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ybum-psnc",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "nedss",
-                "netss",
-                "nndss",
-                "vancomycin-resistant staphylococcus aureus",
-                "varicella morbidity",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ybum-psnc",
             "description": "NNDSS - TABLE 1KK. Vancomycin-resistant Staphylococcus aureus to Varicella morbidity - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1KK. Vancomycin-resistant Staphylococcus aureus to Varicella morbidity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78549,60 +78670,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ybum-psnc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ybum-psnc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ybum-psnc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ybum-psnc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ybum-psnc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ybum-psnc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ybum-psnc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ybum-psnc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ybum-psnc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ybum-psnc",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "vancomycin-resistant staphylococcus aureus",
+                "varicella morbidity",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ybum-psnc",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1KK. Vancomycin-resistant Staphylococcus aureus to Varicella morbidity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/children-coverage-vaccination.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-07",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2025-01-31",
-            "keyword": [
-                "covid-19 vaccination",
-                "nis"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yctb-fv7w",
             "description": "\u2022 COVID-19 vaccination coverage among children 6 months to 17 years is assessed through the National Immunization Survey providing weekly COVID-19 vaccination coverage estimates (https://www.cdc.gov/vaccines/imz-managers/nis/about.html). \n\n\u2022 Weekly estimates of COVID-19 vaccination coverage and parental intent for vaccination among children through December 31, 2023, were calculated using data from the National Immunization Survey-Child COVID Module (NIS-CCM) (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-ccm). Beginning January 2, 2024, the NIS-CCM was discontinued, and questions regarding receipt of COVID-19 vaccination among children were added to the NIS-Flu (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-cim). \n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19 (https://www.cdc.gov/coronavirus/2019-ncov/vaccines/stay-up-to-date.html).",
-            "title": "Cumulative Percentage of Children Ages 6 Months -17 Years Who Are Up to Date with the Updated 2023-24 COVID-19 Vaccine",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78610,65 +78736,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yctb-fv7w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yctb-fv7w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yctb-fv7w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/yctb-fv7w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yctb-fv7w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yctb-fv7w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yctb-fv7w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yctb-fv7w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yctb-fv7w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/yctb-fv7w",
+            "issued": "2023-11-07",
+            "keyword": [
+                "covid-19 vaccination",
+                "nis"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/children-coverage-vaccination.html",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2023-2024",
             "theme": [
                 "Child Vaccinations"
-            ]
+            ],
+            "title": "Cumulative Percentage of Children Ages 6 Months -17 Years Who Are Up to Date with the Updated 2023-24 COVID-19 Vaccine"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/dhcs/ed-visits/index.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-06-01",
-            "temporal": "2016/2022",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-25",
-            "keyword": [
-                "emergency department",
-                "national hospital ambulatory medical care survey",
-                "primary diagnosis",
-                "reason for visit"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:ambcare@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ycxr-emue",
             "description": "The National Hospital Ambulatory Medical Care Survey (NHAMCS), conducted by the National Center for Health Statistics (NCHS), collects annual data on visits to emergency departments to describe patterns of utilization and provision of ambulatory care delivery in the United States. Data are collected from nonfederal, general, and short-stay hospitals from all 50 U.S. states and the District of Columbia, and are used to develop nationally representative estimates. \n\nThe data include counts and rates of emergency department visits from 2016-2022 for the 10 leading primary diagnoses and reasons for visit, stratified by selected patient and hospital characteristics. Rankings for the 10 leading categories were identified using weighted data from 2022 and were then assessed in prior years.",
-            "title": "Estimates of Emergency Department Visits in the United States from 2016-2022",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78676,71 +78800,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ycxr-emue/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ycxr-emue/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ycxr-emue/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ycxr-emue/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ycxr-emue/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ycxr-emue/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ycxr-emue/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ycxr-emue/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ycxr-emue/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ycxr-emue",
+            "issued": "2022-06-01",
+            "keyword": [
+                "emergency department",
+                "national hospital ambulatory medical care survey",
+                "primary diagnosis",
+                "reason for visit"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/dhcs/ed-visits/index.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2024-07-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "temporal": "2016/2022",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Estimates of Emergency Department Visits in the United States from 2016-2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ydsy-yh5w",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
-            "keyword": [
-                "2015",
-                "invasive pneumococcal disease",
-                "legionellosis",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "pneumococcal",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ydsy-yh5w",
             "description": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease. This condition was previously named Streptococcus pneumoniae invasive disease and cases were reported to CDC using different event codes to specify whether the cases were drug resistant or in a defined age group, such as <5 years. Since 2010, case notifications for this condition were consolidated under one event code for Invasive pneumococcal disease.",
-            "title": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78748,66 +78867,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ydsy-yh5w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ydsy-yh5w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ydsy-yh5w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ydsy-yh5w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ydsy-yh5w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ydsy-yh5w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ydsy-yh5w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ydsy-yh5w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ydsy-yh5w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ydsy-yh5w",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
+                "invasive pneumococcal disease",
+                "legionellosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "pneumococcal",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ydsy-yh5w",
+            "modified": "2016-01-07",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ygrm-jkkz",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "nedss",
-                "netss",
-                "nndss",
-                "q fever",
-                "q fever acute",
-                "q fever chronic",
-                "total",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ygrm-jkkz",
             "description": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78815,66 +78934,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ygrm-jkkz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ygrm-jkkz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ygrm-jkkz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ygrm-jkkz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ygrm-jkkz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ygrm-jkkz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ygrm-jkkz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ygrm-jkkz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ygrm-jkkz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ygrm-jkkz",
+            "issued": "2019-04-23",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "q fever",
+                "q fever acute",
+                "q fever chronic",
+                "total",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ygrm-jkkz",
+            "modified": "2020-01-02",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-10",
-            "references": [
-                "https://chronicdata.cdc.gov/d/5qag-uzp2"
-            ],
-            "keyword": [
-                "legislation",
-                "osh",
-                "policy",
-                "smokefree campus",
-                "state system",
-                "tobacco"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OSHData Support",
                 "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yhkp-cczf",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Smokefree-Cam/yhkp-cczf",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC).  State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation \u2013 Smokefree Campuses. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include state smokefree indoor air policies in areas such as: Smokefree campuses for private and public colleges and schools (K-12).",
-            "title": "CDC STATE System Tobacco Legislation - Smokefree Campus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78882,73 +79002,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yhkp-cczf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yhkp-cczf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yhkp-cczf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/yhkp-cczf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yhkp-cczf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yhkp-cczf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yhkp-cczf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yhkp-cczf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yhkp-cczf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Smokefree-Cam/yhkp-cczf",
+            "identifier": "https://data.cdc.gov/api/views/yhkp-cczf",
+            "issued": "2023-07-18",
+            "keyword": [
+                "legislation",
+                "osh",
+                "policy",
+                "smokefree campus",
+                "state system",
+                "tobacco"
+            ],
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2025-01-10",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://chronicdata.cdc.gov/d/5qag-uzp2"
+            ],
             "theme": [
                 "Legislation"
-            ]
+            ],
+            "title": "CDC STATE System Tobacco Legislation - Smokefree Campus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-08-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-23",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
-            "keyword": [
-                "behaviors",
-                "census tract",
-                "disability",
-                "gis",
-                "health",
-                "outcomes",
-                "places",
-                "prevalence",
-                "prevention",
-                "risk",
-                "status"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PLACES Public Inquiries",
                 "hasEmail": "mailto:places@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yjkw-uj5s",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
             "description": "This dataset contains model-based census tract level estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2022 or 2021 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2024 release uses 2022 BRFSS data for 36 measures and 2021 BRFSS data for 4 measures (high blood pressure, high cholesterol, cholesterol screening, and taking medicine for high blood pressure control among those with high blood pressure) that the survey collects data on every other year. These data can be joined with the Census tract 2022 boundary file in a GIS system to produce maps for 40 measures at the census tract level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=3b7221d4e47740cab9235b839fa55cd7",
-            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2024 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78956,62 +79071,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yjkw-uj5s/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yjkw-uj5s/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yjkw-uj5s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/yjkw-uj5s/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yjkw-uj5s/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yjkw-uj5s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yjkw-uj5s/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yjkw-uj5s/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yjkw-uj5s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
+            "identifier": "https://data.cdc.gov/api/views/yjkw-uj5s",
+            "issued": "2024-08-23",
+            "keyword": [
+                "behaviors",
+                "census tract",
+                "disability",
+                "gis",
+                "health",
+                "outcomes",
+                "places",
+                "prevalence",
+                "prevention",
+                "risk",
+                "status"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "modified": "2024-08-23",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2024 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/mental-health-care.htm",
+            "accrualPeriodicity": "R/P2W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-09-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-08-19/2022-05-09",
-            "modified": "2023-04-14",
-            "keyword": [
-                "covid-19",
-                "mental health",
-                "sdoh-use-of-health-care"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yni7-er2q",
             "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, gender, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
-            "title": "Mental Health Care in the Last 4 Weeks",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79019,79 +79144,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yni7-er2q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yni7-er2q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yni7-er2q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/yni7-er2q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yni7-er2q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yni7-er2q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yni7-er2q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yni7-er2q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yni7-er2q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/yni7-er2q",
+            "issued": "2020-09-23",
+            "keyword": [
+                "covid-19",
+                "mental health",
+                "sdoh-use-of-health-care"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/mental-health-care.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P2W",
+            "modified": "2023-04-14",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "US",
+            "temporal": "2020-08-19/2022-05-09",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Mental Health Care in the Last 4 Weeks"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-09-24",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-09",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "hhs region",
-                "influenza",
-                "mortality",
-                "nchs",
-                "nvss",
-                "pneumonia",
-                "provisional",
-                "state",
-                "united states",
-                "weekly"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ynw2-4viq",
             "description": "Deaths counts for influenza, pneumonia, and COVID-19 reported to NCHS by week ending date, by state and HHS region, and age group.",
-            "title": "Provisional Death Counts for Influenza, Pneumonia, and COVID-19",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79099,58 +79212,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ynw2-4viq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ynw2-4viq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ynw2-4viq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ynw2-4viq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ynw2-4viq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ynw2-4viq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ynw2-4viq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ynw2-4viq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ynw2-4viq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/ynw2-4viq",
+            "issued": "2020-09-24",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hhs region",
+                "influenza",
+                "mortality",
+                "nchs",
+                "nvss",
+                "pneumonia",
+                "provisional",
+                "state",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-11-09",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional Death Counts for Influenza, Pneumonia, and COVID-19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/yp23-fq9k",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division, Allergy and Clinical Immunology Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yp23-fq9k",
             "description": "SARS-CoV-2 spreads by infectious aerosols and droplets expelled from the respiratory tract. Masks and respirators can reduce the transmission of infectious respiratory diseases like SARS-CoV-2 by blocking these aerosols and droplets at the source. The ability of source control devices to block aerosols can be tested by expelling an aerosol through a headform wearing the device. These tests may be performed using constant airflows, which are simpler, or cyclic airflows, which are more realistic but require more complex methods. The purpose of these experiments was to compare the results found using constant vs. cyclic airflows.\n\nA source control measurement system was used to measure the efficacy of two cloth face masks, two medical masks with and without an elastic mask brace, a neck gaiter, and an N95 respirator as source control devices for simulated respiratory aerosols. With this system, the aerosol flows from the inside of the mask toward the outside; that is, the aerosol flows in the same direction as it would flow during an exhalation by a person wearing the source control device. The experiments were conducted under four airflow conditions: cyclic breathing at 15 liters/minute (L/min), cyclic breathing at 85 L/min, constant outward airflow at 15 L/min, and constant outward airflow at 85 L/min. Each experiment began by placing the source control device on the headform and performing a fit test. The measurement system collection chamber was then sealed, and the cyclic or constant airflow and the aerosol generation were initiated. The aerosol concentration in the collection chamber was measured using an optical particle spectrometer (OPS). The source control collection efficiency was determined by comparing the steady-state concentration of aerosol particles in the collection chamber when the source control device was worn with the concentration when no source control device was used.",
-            "title": "Constant vs. cyclic flow when testing face masks and respirators as source control devices for simulated respiratory aerosols",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79158,48 +79288,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/yp23-fq9k",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/yp23-fq9k",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Constant vs. cyclic flow when testing face masks and respirators as source control devices for simulated respiratory aerosols"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ype6-idgy",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-10-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
-            "references": [
-                "COVID Data Tracker hospital data displays: https://covid.cdc.gov/covid-data-tracker/#hospitalizations-nhsn   NHSN Hospital Data Reporting: COVID-19 Hospital Data Reporting | NHSN | CDC  Full reporting guidance: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf"
-            ],
-            "keyword": [
-                "admissions",
-                "coronavirus",
-                "covid-19",
-                "hospital capacity",
-                "hospitalizations",
-                "hospital occupancy",
-                "icu beds",
-                "influenza",
-                "inpatient beds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DHQP",
                 "hasEmail": "mailto:nhsn@cdc.gov (subject line: weekly NHSN hospital data)"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDC"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ype6-idgy",
             "description": "<b>Note:</b> \nAfter November 1, 2024, this dataset will no longer be updated due to a transition in NHSN Hospital Respiratory Data reporting that occurred on Friday, November 1, 2024. For more information on NHSN Hospital Respiratory Data reporting, please visit https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html.\n\nDue to a recent update in voluntary NHSN Hospital Respiratory Data reporting that occurred on Wednesday, October 9, 2024, reporting levels and other data displayed on this page may fluctuate week-over-week beginning Friday, October 18, 2024. For more information on NHSN Hospital Respiratory Data reporting, please visit https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html.  Find more information about the updated CMS requirements: https://www.federalregister.gov/documents/2024/08/28/2024-17021/medicare-and-medicaid-programs-and-the-childrens-health-insurance-program-hospital-inpatient.\u202f  \n.\nThis dataset represents weekly respiratory virus-related hospitalization data and metrics aggregated to national and state/territory levels reported during two periods: 1) data for collection dates from August 1, 2020 to April 30, 2024, represent data reported by hospitals during a mandated reporting period as specified by the HHS Secretary; and 2) data for collection dates beginning May 1, 2024, represent data reported voluntarily by hospitals to CDC\u2019s National Healthcare Safety Network (NHSN). NHSN monitors national and local trends in healthcare system stress and capacity for up to approximately 6,000 hospitals in the United States. Data reported represent aggregated counts and include metrics capturing information specific to COVID-19- and influenza-related hospitalizations, hospital occupancy, and hospital capacity. Find more information about reporting to NHSN at: https://www.cdc.gov/nhsn/covid19/hospital-reporting.html\n\n<b>Source: COVID-19 hospitalization data reported to CDC\u2019s National Healthcare Safety Network (NHSN).</b>\n<ul><li><b>Data source description(updated October 18, 2024):</b> As of October 9, 2024, Hospital Respiratory Data (HRD; formerly Respiratory Pathogen, Hospital Capacity, and Supply data or \u2018COVID-19 hospital data\u2019) are reported to HHS through CDC\u2019s National Healthcare Safety Network based on updated requirements from the Centers for Medicare and Medicaid Services (CMS). These data are voluntarily reported to NHSN as of May 1, 2024 until November 1, 2024, at which time CMS will require acute care and critical access hospitals to electronically report information via NHSN about COVID-19, Influenza, and RSV, hospital bed census and capacity, and limited patient demographic information, including age. Data for collection dates prior to May 1, 2024, represent data reported during a previously mandated reporting period as specified by the HHS Secretary. Data for collection dates May 1, 2024, and onwards represent data reported voluntarily to NHSN; as such, data included represents reporting hospitals only for a given week and might not be complete or representative of all hospitals. NHSN monitors national and local trends in healthcare system stress and capacity for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Find more information about reporting to NHSN: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html. Find more information about the updated CMS requirements: https://www.federalregister.gov/documents/2024/08/28/2024-17021/medicare-and-medicaid-programs-and-the-childrens-health-insurance-program-hospital-inpatient.</li><li><b>Data quality:</b> While CDC reviews reported data for completeness and errors and corrects those found, some reporting errors might still exist within the data. CDC and partners work with reporters to correct these errors and update the data in subsequent weeks",
-            "title": "Weekly United States Hospitalization Metrics by Jurisdiction, During Mandatory Reporting Period from August 1, 2020 to April 30, 2024, and for Data Reported Voluntarily Beginning May 1, 2024, National Healthcare Safety Network (NHSN) (Historical)-ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79207,78 +79324,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ype6-idgy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ype6-idgy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ype6-idgy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ype6-idgy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ype6-idgy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ype6-idgy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ype6-idgy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ype6-idgy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ype6-idgy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/ype6-idgy",
+            "issued": "2024-10-18",
+            "keyword": [
+                "admissions",
+                "coronavirus",
+                "covid-19",
+                "hospital capacity",
+                "hospitalizations",
+                "hospital occupancy",
+                "icu beds",
+                "influenza",
+                "inpatient beds"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ype6-idgy",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2024-11-15",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
+            },
+            "references": [
+                "COVID Data Tracker hospital data displays: https://covid.cdc.gov/covid-data-tracker/#hospitalizations-nhsn   NHSN Hospital Data Reporting: COVID-19 Hospital Data Reporting | NHSN | CDC  Full reporting guidance: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf"
+            ],
+            "spatial": "US",
             "theme": [
                 "Public Health Surveillance"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly United States Hospitalization Metrics by Jurisdiction, During Mandatory Reporting Period from August 1, 2020 to April 30, 2024, and for Data Reported Voluntarily Beginning May 1, 2024, National Healthcare Safety Network (NHSN) (Historical)-ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-04-28",
-            "temporal": "2020-01-01/2020-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-03",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "coronavirus",
-                "county",
-                "covid-19",
-                "deaths",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "quarterly",
-                "sdoh-environmental",
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ypxr-mz8e",
             "description": "Provisional counts of deaths involving coronavirus disease 2019 (COVID-19) by United States county of residence and age group, for 2020 by quarter.",
-            "title": "AH Provisional COVID-19 Deaths by Quarter, County and Age for 2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79286,68 +79400,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ypxr-mz8e/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ypxr-mz8e/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ypxr-mz8e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ypxr-mz8e/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ypxr-mz8e/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ypxr-mz8e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ypxr-mz8e/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ypxr-mz8e/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ypxr-mz8e/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ypxr-mz8e",
+            "issued": "2021-04-28",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "county",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "quarterly",
+                "sdoh-environmental",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-04-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "temporal": "2020-01-01/2020-12-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by Quarter, County and Age for 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/yqwx-bvu7",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "keyword": [
-                "2016",
-                "invasive pneumococcal disease",
-                "legionellosis",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "pneumococcal",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yqwx-bvu7",
             "description": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.  NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change.   For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease. This condition was previously named Streptococcus pneumoniae invasive disease and cases were reported to CDC using different event codes to specify whether the cases were drug resistant or in a defined age group, such as <5 years.",
-            "title": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79355,72 +79474,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yqwx-bvu7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yqwx-bvu7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yqwx-bvu7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/yqwx-bvu7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yqwx-bvu7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yqwx-bvu7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yqwx-bvu7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yqwx-bvu7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yqwx-bvu7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/yqwx-bvu7",
+            "issued": "2017-01-05",
+            "keyword": [
+                "2016",
+                "invasive pneumococcal disease",
+                "legionellosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "pneumococcal",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/yqwx-bvu7",
+            "modified": "2017-01-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/yrur-wghw",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-14",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
-            "keyword": [
-                "age",
-                "age group",
-                "coronavirus",
-                "covid-19",
-                "death rate",
-                "deaths",
-                "hhs region",
-                "hispanic origin",
-                "monthly",
-                "mortality",
-                "nchs",
-                "nvss",
-                "race",
-                "sex",
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yrur-wghw",
             "description": "This file contains COVID-19 death counts and rates by month and year of death, jurisdiction of residence (U.S., HHS Region) and demographic characteristics (sex, age, race and Hispanic origin, and age/race and Hispanic origin). United States death counts and rates include the 50 states, plus the District of Columbia.\n\nDeaths with confirmed or presumed COVID-19, coded to ICD\u201310 code U07.1. Number of deaths reported in this file are the total number of COVID-19 deaths received and coded as of the date of analysis and may not represent all deaths that occurred in that period. Counts of deaths occurring before or after the reporting period are not included in the file.\n\nData during recent periods are incomplete because of the lag in time between when the death occurred and when the death certificate is completed, submitted to NCHS and processed for reporting purposes. This delay can range from 1 week to 8 weeks or more, depending on the jurisdiction and cause of death.\n\nDeath counts should not be compared across jurisdictions. Data timeliness varies by state. Some states report deaths on a daily basis, while other states report deaths weekly or monthly.\n\nThe ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.\n\nRates were calculated using the population estimates for 2021, which are estimated as of July 1, 2021 based on the Blended Base produced by the US Census Bureau in lieu of the April 1, 2020 decennial population count. The Blended Base consists of the blend of Vintage 2020 postcensal population estimates, 2020 Demographic Analysis Estimates, and 2020 Census PL 94-171 Redistricting File (see https://www2.census.gov/programs-surveys/popest/technical-documentation/methodology/2020-2021/methods-statement-v2021.pdf).\n\nRate are based on deaths occurring in the specified week and are age-adjusted to the 2000 standard population using the direct method (see https://www.cdc.gov/nchs/data/nvsr/nvsr70/nvsr70-08-508.pdf). These rates differ from annual age-adjusted rates, typically presented in NCHS publications based on a full year of data and annualized weekly age-adjusted rates which have been adjusted to allow comparison with annual rates. Annualization rates presents deaths per year per 100,000 population that would be expected in a year if the observed period specific (weekly) rate prevailed for a full year.\n\nSub-national death counts between 1-9 are suppressed in accordance with NCHS data confidentiality standards. Rates based on death counts less than 20 are suppressed in accordance with NCHS standards of reliability as specified in NCHS Data Presentation Standards for Proportions (available from: https://www.cdc.gov/nchs/data/series/sr_02/sr02_175.pdf.).",
-            "title": "Provisional COVID-19 death counts and rates by month, jurisdiction of residence, and demographic characteristics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79428,67 +79542,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yrur-wghw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yrur-wghw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yrur-wghw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/yrur-wghw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yrur-wghw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yrur-wghw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yrur-wghw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yrur-wghw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yrur-wghw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/yrur-wghw",
+            "issued": "2023-12-14",
+            "keyword": [
+                "age",
+                "age group",
+                "coronavirus",
+                "covid-19",
+                "death rate",
+                "deaths",
+                "hhs region",
+                "hispanic origin",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "race",
+                "sex",
+                "united states"
+            ],
+            "landingPage": "https://data.cdc.gov/d/yrur-wghw",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional COVID-19 death counts and rates by month, jurisdiction of residence, and demographic characteristics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-29",
-            "@type": "dcat:Dataset",
-            "temporal": "2024-2025",
-            "modified": "2025-01-31",
-            "keyword": [
-                "flu vaccination",
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "nis-flu",
-                "vsd"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ysd3-txwj",
             "description": "Weekly Cumulative Estimated Number of Influenza Vaccinations Administered in Pharmacies and Physical Medical Offices, Adults 18 Years and Older, United States \n\nArchived data are here: https://data.cdc.gov/resource/uxgd-cqqc\n\n- Estimated number of influenza vaccinations among adults 18 years and older is assessed through IQVIA (https://www.iqvia.com/) as a source of information on vaccinations administered in retail pharmacies (include chain, mass merchandise, stores, and independent pharmacies) and physician medical offices.",
-            "title": "Weekly Cumulative Estimated Number of Influenza Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, by Flu Season and Age Group, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79496,69 +79618,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ysd3-txwj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ysd3-txwj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ysd3-txwj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ysd3-txwj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ysd3-txwj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ysd3-txwj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ysd3-txwj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ysd3-txwj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ysd3-txwj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/ysd3-txwj",
+            "issued": "2025-01-29",
+            "keyword": [
+                "flu vaccination",
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "nis-flu",
+                "vsd"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2024-2025",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Estimated Number of Influenza Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, by Flu Season and Age Group, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-12-02",
-            "@type": "dcat:Dataset",
-            "temporal": "1940/2018",
-            "modified": "2022-03-29",
-            "keyword": [
-                "age of mother",
-                "birth rates",
-                "nchs",
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:births@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yt7u-eiyg",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "This dataset includes birth rates for females by age group in the United States since 1940.\n\nThe number of states in the reporting area differ historically. In 1915 (when the birth registration area was established), 10 states and the District of Columbia reported births; by 1933, 48 states and the District of Columbia were reporting births, with the last two states, Alaska and Hawaii, added to the registration area in 1959 and 1960, when these regions gained statehood. Reporting area information is detailed in references 1 and 2 below. Trend lines for 1909\u20131958 are based on live births adjusted for under-registration; beginning with 1959, trend lines are based on registered live births.",
-            "title": "NCHS - Birth Rates for Females by Age Group: United States",
-            "isPartOf": "NCHS - Birth Rates for Females by Age Group: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79566,61 +79689,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yt7u-eiyg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yt7u-eiyg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yt7u-eiyg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/yt7u-eiyg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yt7u-eiyg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yt7u-eiyg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yt7u-eiyg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yt7u-eiyg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yt7u-eiyg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/yt7u-eiyg",
+            "isPartOf": "NCHS - Birth Rates for Females by Age Group: United States",
+            "issued": "2015-12-02",
+            "keyword": [
+                "age of mother",
+                "birth rates",
+                "nchs",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-03-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "50 states and District of Columbia",
+            "temporal": "1940/2018",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - Birth Rates for Females by Age Group: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/yu68-juzt",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Division of Safety Research, Protective Technology Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yu68-juzt",
             "description": "The accommodation of worker anthropometric variability in the workplace and personal protective equipment (PPE) is key to safe and efficient completion of work tasks. Previously, the best data available was 46 years old, which has largely become outdated due to demographic changes. These data tables consist of 34 traditional semi-nude body dimensions without gear (e.g., chest depth, standing; foot breadth, horizontal, standing; hip circumference; stature; elbow rest height, sitting; and eye height, sitting) and 15 dimension measurements over clothing and with gear (e.g., abdominal extension depth, sitting; hip breadth, sitting; and should-grip length, sitting) of 756 male and 218 female Law Enforcement Officers (LEOs). For many LEOs, patrol vehicles are the workplace where they spend significant portions of their workday and PPE is vital gear to safeguard LEOs from the harm of assaults. Design improvements of vehicle console space, vehicle ingress/egress, and LEO body-worn equipment can result in reduced LEO fatigue, pain, or injury.",
-            "title": "Anthropometry of Law Enforcement Officers",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79628,40 +79758,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/yu68-juzt",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/yu68-juzt",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Anthropometry of Law Enforcement Officers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/yviw-z6j5",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-06-06",
-            "temporal": "2020-01-22/2023-05-10",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "covid",
-                "covid-19",
-                "surveillance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Surveillance Review and Response Group",
                 "hasEmail": "mailto:eocevent394@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yviw-z6j5",
             "description": "<b>Note:</b> \nThe cumulative case count for some counties (with small population) is higher than expected due to the inclusion of non-permanent residents in COVID-19 case counts. \n\nReporting of Aggregate Case and Death Count data was discontinued on May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. Although these data will continue to be publicly available, this dataset will no longer be updated.\n\n<b>Aggregate Data Collection Process\nSince the beginning of the COVID-19 pandemic, data were reported through a robust process with the following steps:</b><ul><li>Aggregate county-level counts were obtained indirectly, via automated overnight web collection, or directly, via a data submission process.</li><li>If more than one official county data source existed, CDC used a comprehensive data selection process comparing each official county data source to retrieve the highest case and death counts, unless otherwise specified by the state.</li><li>A CDC data team reviewed counts for congruency prior to integration. CDC routinely compiled these data and post the finalized information on COVID Data Tracker.</li><li>Cases and deaths are based on date of report and not on the date of symptom onset. CDC calculates rates in this data by using population estimates provided by the US Census Bureau Population Estimates Program (2019 Vintage).</li><li>COVID-19 aggregate case and death data were organized in a time series that includes cumulative number of cases and deaths as reported by a jurisdiction on a given date.  New case and death counts were calculated as the week-to-week change in reported cumulative cases and deaths (i.e., newly reported cases and deaths = cumulative number of cases/deaths reported this week minus the cumulative total reported the week before.</li></ul>\n\nThis process was collaborative, with CDC and jurisdictions working together to ensure the accuracy of COVID-19 case and death numbers. County counts provided the most up-to-date numbers on cases and deaths by report date. Throughout data collection, CDC retrospectively updated counts to correct known data quality issues. CDC also worked with jurisdictions after the end of the public health emergency declaration to finalize county data. \n<ul><li><b>Source:</b> The weekly archived dataset is based on county-level aggregate count data</li><li><b>Confirmed/Probable Cases/Death breakdown:</b> Cumulative cases and deaths for each county are included.  Total reported cases include probable and confirmed cases.</li><li><b>Time Series Frequency:</b> The weekly archived dataset contains weekly time series data (i.e., one record per week per county)</li></ul>\n \n<b>Important note:</b> The counts reflected during a given time period in this dataset may not match the counts reflected for the same time period in the daily archived dataset noted above. Discrepancies may exist due to differences between county and state COVID-19 case surveillance and reconciliation efforts.\n\nThe surveillance case definition for COVID-19, a nationally notifiable disease, was first described in a <a href=\"https://ndc.services.cdc.gov/case-definitions/coronavirus-disease-2019-covid-19/\">position statement</a> from the Council for State and Territorial Epidemiologists, which was later <a href=\"https://ndc.services.cdc.gov/case-definitions/coronavirus-disease-2019-covid-19/\">revised</a>. However, there is some variation in how jurisdictions implement these case classifications. More information on how CDC collects COVID-19 case surveillance data can be found at <a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html\">FAQ: COVID-19 Data and Surveillance</a>.\n\n<b>Confirmed and Probable Counts</b>\nIn this dataset, counts by jurisdiction are not displayed by confirmed or probable status. Instead, counts of confirmed and probable cases and deaths are included in the Total Cases and Total Deaths columns, when available. Not all jurisdictions report",
-            "title": "Weekly United States COVID-19 Cases and Deaths by County - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79669,62 +79794,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yviw-z6j5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yviw-z6j5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yviw-z6j5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/yviw-z6j5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yviw-z6j5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yviw-z6j5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yviw-z6j5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yviw-z6j5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yviw-z6j5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "No longer updated (dataset archived)"
+            "identifier": "https://data.cdc.gov/api/views/yviw-z6j5",
+            "issued": "2023-06-06",
+            "keyword": [
+                "covid",
+                "covid-19",
+                "surveillance"
+            ],
+            "landingPage": "https://data.cdc.gov/d/yviw-z6j5",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "temporal": "2020-01-22/2023-05-10",
+            "title": "Weekly United States COVID-19 Cases and Deaths by County - ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/yvsw-8ht9",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "mumps",
-                "nedss",
-                "netss",
-                "nndss",
-                "novel influenza a virus infections",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/yvsw-8ht9",
             "description": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Novel influenza A virus infections are human infections with influenza A viruses that are different from currently circulating human seasonal influenza viruses. With the exception of one avian lineage influenza A (H7N2) virus, all novel influenza A virus infections reported to CDC since 2012 have been variant influenza viruses.",
-            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79732,30 +79853,52 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yvsw-8ht9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yvsw-8ht9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yvsw-8ht9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/yvsw-8ht9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yvsw-8ht9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yvsw-8ht9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/yvsw-8ht9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/yvsw-8ht9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/yvsw-8ht9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/yvsw-8ht9",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "novel influenza a virus infections",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/yvsw-8ht9",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections"
         }
-    ]
+    ],
+    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
 }
```

### Changes from eb01078 to 9cd27cf
**Author:** Automated

**Date:** 2025-01-31 22:10:57+00:00

**Message:** Updated data: Fri Jan 31 22:10:57 UTC 2025

```diff
diff --git a/cdc.json b/cdc.json
index e2e78ba..bdb75b7 100644
--- a/cdc.json
+++ b/cdc.json
@@ -6325,68 +6325,6 @@
                 "National Center for Health Statistics"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#vaccinations-pregnant-women",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2021-11-24",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-22",
-            "keyword": [
-                "covid-19 vaccine",
-                "covid tracker",
-                "pregnancy",
-                "vsd"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Assessment Branch, Immunization Services Division, NCIRD, CDC",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4ht3-nbmd",
-            "description": "These archived cumulative COVID-19 vaccination coverage estimates are for persons who were pregnant anytime from December 20, 2020, to January 20, 2022, and received at least 1 dose of COVID-19 vaccine during pregnancy based on data from the Vaccine Safety Datalink*. As of January 20, 2022, after moving to reporting weekly estimates, the figures on https://covid.cdc.gov/covid-data-tracker/#vaccinations-pregnant-women no longer present cumulative estimates, and these   archived data are no longer updated.\n\nFor these cumulative data, on December 15, 2021, an error was identified where pregnant people who had received an additional or booster dose of a COVID-19 vaccine were not included in the coverage estimates. After correcting the error, coverage estimates for the week of December 11, 2021, increased overall and by race/ethnicity. The persons that were inadvertently excluded have been counted in the December 11, 2021, estimates. Prior weeks\u2019 estimates have not been updated.",
-            "title": "Archived Cumulative Data: Percent of pregnant people aged 18-49 years receiving at least one dose of a COVID-19 vaccine during pregnancy overall, by race/ethnicity, and date reported to CDC-Vaccine Safety Datalink*, United States | December 20, 2020 \u2013 Jan",
-            "programCode": [
-                "009:026"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4ht3-nbmd/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/4ht3-nbmd/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/4ht3-nbmd/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/4ht3-nbmd/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/4ht3-nbmd/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/4ht3-nbmd/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/4ht3-nbmd/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "theme": [
-                "Vaccinations"
-            ]
-        },
         {
             "accessLevel": "public",
             "bureauCode": [
@@ -25023,7 +24961,7 @@
             "landingPage": "https://data.cdc.gov/d/bc4h-zh8r",
             "issued": "2023-06-29",
             "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
+            "modified": "2025-01-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "v-safe inquiries team",
@@ -41297,62 +41235,6 @@
                 }
             ]
         },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "landingPage": "https://data.cdc.gov/d/hv7b-3sw8",
-            "issued": "2023-06-22",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Surveillance and Epidemiology Branch, Immunization Services Division, NCIRD, CDC",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hv7b-3sw8",
-            "description": "Estimates are for pregnant women who are up-to-date with COVID-19 vaccines, overall and by race and ethnicity based on data from the Vaccine Safety Datalink*.",
-            "title": "Data: COVID-19 vaccination among pregnant women aged 18-49 years overall, by race and ethnicity, and date reported to CDC - Vaccine Safety Datalink,* United States",
-            "programCode": [
-                "009:026"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hv7b-3sw8/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hv7b-3sw8/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/hv7b-3sw8/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hv7b-3sw8/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/hv7b-3sw8/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hv7b-3sw8/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/hv7b-3sw8/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "theme": [
-                "Pregnancy & Vaccination"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/hwk8-wu83",
@@ -46463,77 +46345,6 @@
                 "National Institute for Occupational Safety and Health"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/rsvvaxview/",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-09-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2024-2025",
-            "modified": "2025-01-31",
-            "keyword": [
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "nis-flu",
-                "rsv vaccination",
-                "vsd"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/k4cb-dxd7",
-            "description": "\u2022 Weekly Cumulative RSV Vaccination Coverage and Intent Among Adults 75 Years and Older and 60\u250074 Years with High Risk Conditions Ever Vaccinated with RSV Vaccine by Demographic Characteristics and Jurisdiction \n\n\u2022 Weekly estimates of RSV vaccination coverage and intent among adults 75 years and older and 60\u250074 years with high risk conditions are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/index.html). \n\n\u2022 In June 2023, the Advisory Committee on Immunization Practices (ACIP) voted to recommend that adults aged \u226560 years may receive a single dose of an RSV vaccine, using shared clinical decision-making. In June 2024, the ACIP voted to recommend a single dose of RSV vaccine for all adults 75 years and older and adults 60\u201374 years who are at increased risk for severe RSV disease. The data below captures ever receiving a dose of an RSV vaccine by adults 60 years and older.",
-            "title": "Weekly Cumulative RSV Vaccination Coverage and Intent, Overall, by Selected Demographics and Jurisdiction, Among Adults 75 and Older and 60-74 Years with High-Risk Conditions Ever Vaccinated, United States",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/k4cb-dxd7/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/k4cb-dxd7/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/k4cb-dxd7/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
-            "theme": [
-                "Vaccinations"
-            ],
-            "language": [
-                "English"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/k4xj-uge6",
@@ -47482,74 +47293,6 @@
                 "English"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adult-coverage-vaccination.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-12-11",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2025-01-31",
-            "keyword": [
-                "adults",
-                "covid-19 vaccination",
-                "nis-acm"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/kevv-m5vs",
-            "description": "Weekly COVID-19 Vaccination Coverage of Adults 18 Years and Older by Jurisdiction \n\n\u2022 COVID-19 vaccination coverage among adults 18 years and older is assessed through the National Immunization Survey-Adult COVID Module, providing weekly COVID-19 vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html) \n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine for adults ages 18 years and older.",
-            "title": "Weekly Differences in Cumulative Percentage of Adults 18 Years and Older Vaccinated with the Updated 2023-24 COVID-19 Vaccine by Selected Demographics",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/kevv-m5vs/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kevv-m5vs/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/kevv-m5vs/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kevv-m5vs/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/kevv-m5vs/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kevv-m5vs/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/kevv-m5vs/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "spatial": "United States- National, Region, State",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
-            "theme": [
-                "Vaccinations"
-            ],
-            "language": [
-                "English"
-            ]
-        },
         {
             "accessLevel": "public",
             "bureauCode": [
@@ -49130,77 +48873,6 @@
                 "Motor Vehicle"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/adult-vaccination-coverage.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-09-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2024-2025",
-            "modified": "2025-01-31",
-            "keyword": [
-                "covid-19 vaccination",
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "nis-flu",
-                "vsd"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ksfb-ug5d",
-            "description": "Weekly COVID-19 Vaccination Coverage and intent among adults 18 Years and Older by Demographic Characteristics and Jurisdiction \u2022 Weekly estimates of COVID-19 vaccination coverage and intent among adults 18 years and older are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/). \n\nWeekly comparisons to previous season should take into account differences between seasons in vaccine availability dates. 2023\u201324 COVID-19 vaccines were first available mid-September 2023, and 2024\u201325 COVID-19 vaccines were first available at the end of August 2024.",
-            "title": "Weekly Cumulative COVID-19 Vaccination Coverage and Intent, Overall, by Selected Demographics and Jurisdiction, Among Adults 18 Years and Older",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ksfb-ug5d/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ksfb-ug5d/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ksfb-ug5d/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "spatial": "United States- National, Region, State",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
-            "theme": [
-                "Vaccinations"
-            ],
-            "language": [
-                "English"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/ktba-rcfx",
@@ -65316,77 +64988,6 @@
                 "NCHS"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/fluvaxview/dashboard/adult-coverage.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-10-10",
-            "@type": "dcat:Dataset",
-            "temporal": "2024-2025",
-            "modified": "2025-01-31",
-            "keyword": [
-                "flu vaccination",
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "nis-flu",
-                "vsd"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/sw5n-wg2p",
-            "description": "\u2022 Weekly Influenza Vaccination Coverage and intent among adults 18 Years and Older by Demographic Characteristics and Jurisdiction \n\n \u2022 Weekly estimates of influenza vaccination coverage and intent for vaccination among adults 18 years and older are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/index.html).",
-            "title": "Weekly Influenza Vaccination Coverage and Intent for Vaccination, Overall, by Selected Demographics and Jurisdiction, Among Adults 18 Years and Older",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/sw5n-wg2p/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/sw5n-wg2p/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/sw5n-wg2p/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/sw5n-wg2p/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/sw5n-wg2p/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/sw5n-wg2p/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/sw5n-wg2p/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "spatial": "United States- National, Region, State",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
-            "theme": [
-                "Flu Vaccinations"
-            ],
-            "language": [
-                "English"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "http://www.cdc.gov/nccdphp/dph/",
@@ -70781,77 +70382,6 @@
                 "NCHS"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/rsvvaxview/",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-09-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2024-2025",
-            "modified": "2025-01-31",
-            "keyword": [
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "nis-flu",
-                "rsv vaccination",
-                "vsd"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/vdz4-qrri",
-            "description": "Infant Protection Against RSV by Maternal RSV Vaccination or Receipt of Nirsevimab and Intent for Nirsevimab Receipt, Reported by Females Aged 18-49 Years Who Have an Infant <8 Months During the RSV Season (born since April 1, 2024)\n\nMonthly estimates of infant protection against RSV by maternal RSV vaccination or receipt of nirsevimab, as well as intent for nirsevimab receipt, were calculated using data from the from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM). (https://www.cdc.gov/nis/about/index.html). Data were reported by adult females aged 18-49 years with infants under the age of 8 months during the RSV season (born since April 1, 2024). The NIS\u2013ACM is an ongoing random-digit-dial cellular telephone survey of households with adults 18 years and older. All estimates are based upon parent-reported receipt of nirsevimab.",
-            "title": "Infant Protection Against Respiratory Syncytial Virus (RSV) by Maternal RSV Vaccination or Receipt of Nirsevimab, and Intent for Nirsevimab Receipt, United States",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/vdz4-qrri/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/vdz4-qrri/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/vdz4-qrri/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "spatial": "United States- National, Region, State",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
-            "theme": [
-                "Pregnancy & Vaccination"
-            ],
-            "language": [
-                "English"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
@@ -73185,62 +72715,6 @@
                 "NCHS"
             ]
         },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "landingPage": "https://data.cdc.gov/d/w6be-99qd",
-            "issued": "2022-02-01",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Surveillance and Epidemiology Branch, Immunization Services Division, NCIRD, CDC",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/w6be-99qd",
-            "description": "These weekly COVID-19 vaccination coverage estimates are for pregnant women who are fully vaccinated before and during pregnancy based on data from the Vaccine Safety Datalink*.",
-            "title": "Weekly Data: COVID-19 vaccination among pregnant women ages 18-49 years before and during pregnancy overall, by race/ethnicity, and week ending date - Vaccine Safety Datalink,* United States",
-            "programCode": [
-                "009:026"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/w6be-99qd/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/w6be-99qd/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/w6be-99qd/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/w6be-99qd/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/w6be-99qd/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/w6be-99qd/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/w6be-99qd/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "theme": [
-                "Pregnancy & Vaccination"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
```

### Changes from 29aa757 to eb01078
**Author:** Automated

**Date:** 2025-01-31 21:10:22+00:00

**Message:** Updated data: Fri Jan 31 21:10:22 UTC 2025

```diff
diff --git a/cdc.json b/cdc.json
index 0098ac5..e2e78ba 100644
--- a/cdc.json
+++ b/cdc.json
@@ -784,21 +784,21 @@
             "@type": "dcat:Dataset",
             "modified": "2025-01-31",
             "keyword": [
-                "rsv",
-                "surveillance",
-                "respiratory disease",
-                "respiratory syncytial virus",
-                "respiratory illness",
-                "respiratory virus response",
-                "hospitalizations",
+                "age-adjusted rates",
+                "age-adjusted rates by race and ethnicity",
                 "hospitalization",
                 "hospitalization rate",
+                "hospitalizations",
                 "rate",
                 "rates by race and ethnicity",
-                "rsv-net",
+                "respiratory disease",
+                "respiratory illness",
+                "respiratory syncytial virus",
+                "respiratory virus response",
+                "rsv",
                 "rsvnet",
-                "age-adjusted rates",
-                "age-adjusted rates by race and ethnicity"
+                "rsv-net",
+                "surveillance"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -1915,76 +1915,6 @@
                 }
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-09-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-21",
-            "references": [
-                "http://www.cdc.gov/nchs/nhis/about_nhis.htm",
-                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/national-health-interview-survey.html"
-            ],
-            "keyword": [
-                "blind",
-                "contact lenses",
-                "glasses",
-                "nhis",
-                "vision correction",
-                "visual function"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/2t2r-sf6s",
-            "description": "2014-15 merged, 2016-17 merged. This dataset is a de-identified summary table of vision and eye health data indicators from NHIS, stratified by all available combinations of age group, race/ethnicity, gender, and risk factor. NHIS is an annual household survey conducted by the National Center for Health Statistics at CDC that monitors trends in illness, disabilities, and progress towards national health objectives. Approximate sample size is 35,000 households and 87,500 persons annually. NHIS data for VEHSS includes questions related to Visual Function. Data were suppressed for cell sizes less than 30 persons, or where the relative standard error more than 30% of the mean. Data will be updated as it becomes available. Detailed information on VEHSS NHIS analyses can be found on the VEHSS NHIS webpage (link). Additional information about NHIS can be found on the NHIS website (http://www.cdc.gov/nchs/nhis/about_nhis.htm). The VEHSS NHIS dataset was last updated in November 2019.",
-            "title": "National Health Interview Survey (NHIS) \u2013 Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/2t2r-sf6s/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/2t2r-sf6s/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/2t2r-sf6s/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/2t2r-sf6s/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/2t2r-sf6s/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/2t2r-sf6s/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/2t2r-sf6s/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/National-Health-Interview-Survey-NHIS-Vision-and-E/2t2r-sf6s",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "theme": [
-                "Vision & Eye Health"
-            ]
-        },
         {
             "accessLevel": "public",
             "bureauCode": [
@@ -6901,73 +6831,6 @@
                 "NNDSS"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-09-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-21",
-            "references": [
-                "https://www.vsp.com",
-                "https://www.cdc.gov/visionhealth/vehss/data/claims/vsp.html"
-            ],
-            "keyword": [
-                "claims",
-                "medical diagnoses",
-                "vsp"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4r3g-hv9c",
-            "description": "2016. This dataset is a de-identified summary table of vision and eye health data indicators from VSP, stratified by all available combinations of age group, race/ethnicity, gender, and state. VSP claims for VEHSS provides a convenience sample of vision insurance members representing approximately more than 1 in 4 of the U.S. population. VSP uses a web-based claims submissions system to collect and process claims. The denominator of the rates represents persons with VSP benefits as reported by employers, and is subject to some uncertainty.  VSP data for VEHSS include Service Utilization and Eye Health Condition indicators.  Certain ophthalmic conditions and procedures are covered by health insurance and are not covered by managed vision insurance, claims based eye disease prevalence may therefore be expected to undercount true prevalence.  Person level claims and person counts are not publically available.  Reported rates were suppressed for de-identification to ensure protection of patient privacy. Detailed information on VEHSS VSP analyses can be found on the VEHSS VSP webpage (link). Information on VSP data can be found on the VSP website (www.vsp.com). The VEHSS VSP dataset was last updated in June 2018.",
-            "title": "Vision Service Plan (VSP) \u2013 Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4r3g-hv9c/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/4r3g-hv9c/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/4r3g-hv9c/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/4r3g-hv9c/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/4r3g-hv9c/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/4r3g-hv9c/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/4r3g-hv9c/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Vision-Service-Plan-VSP-Vision-and-Eye-Health-Surv/4r3g-hv9c",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "theme": [
-                "Vision & Eye Health"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/4r49-eadb",
@@ -9110,15 +8973,15 @@
             "temporal": "2023-2024 respiratory virus season",
             "modified": "2025-01-31",
             "keyword": [
-                "ncird",
-                "rsv",
-                "covid19",
                 "coronavirus",
-                "vaccination",
+                "covid19",
                 "immunization",
+                "ncird",
                 "nis-acm",
                 "nis-ccm",
                 "respiratory-virus-response",
+                "rsv",
+                "vaccination",
                 "vaccination-coverage"
             ],
             "contactPoint": {
@@ -10552,75 +10415,6 @@
                 "Public Health Surveillance"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/adults-60-coverage-intent.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-12-11",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2025-01-31",
-            "keyword": [
-                "vaccination",
-                "rsv",
-                "older adults",
-                "nis-acm"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5vw4-awn6",
-            "description": "Weekly RSV Vaccination Coverage of Adults 60 Years and Older by Jurisdiction \n\n\u2022 RSV vaccination coverage among adults 60 years and older is assessed through the National Immunization Survey-Adult COVID Module, providing weekly RSV vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n \u2022 The CDC recommended the RSV vaccine for adults 60 years and older in July 2023. (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)",
-            "title": "Differences in Weekly Cumulative Percentage of Adults 60 Years and Older Vaccinated with Respiratory Syncytial Virus (RSV) Vaccine by Selected Demographics",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/5vw4-awn6/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/5vw4-awn6/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/5vw4-awn6/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/5vw4-awn6/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/5vw4-awn6/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/5vw4-awn6/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/5vw4-awn6/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "spatial": "United States- National, Region, State",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
-            "theme": [
-                "Vaccinations"
-            ],
-            "language": [
-                "English"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/5wdd-3g8t",
@@ -11849,21 +11643,21 @@
             "@type": "dcat:Dataset",
             "modified": "2025-01-31",
             "keyword": [
-                "covid19",
                 "covid",
+                "covid19",
                 "covid-19",
-                "surveillance",
-                "hospitalizations",
-                "respiratory virus response",
-                "respiratory illness",
-                "covid-net",
-                "resp-net",
                 "covidnet",
-                "respnet",
+                "covid-net",
                 "hospitalization rate",
+                "hospitalizations",
                 "rate",
+                "rates by age group",
                 "rates by race and ethnicity",
-                "rates by age group"
+                "respiratory illness",
+                "respiratory virus response",
+                "respnet",
+                "resp-net",
+                "surveillance"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -16785,12 +16579,12 @@
             "temporal": "2024-2025",
             "modified": "2025-01-31",
             "keyword": [
+                "flu vaccination",
+                "iis",
                 "iqvia",
                 "nis-acm",
-                "vsd",
-                "iis",
                 "nis-flu",
-                "flu vaccination"
+                "vsd"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -21224,75 +21018,6 @@
                 "Motor Vehicle"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2021-03-10",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
-            "references": [
-                "Vaccine Safety Datalink"
-            ],
-            "keyword": [
-                "flu",
-                "influenza",
-                "pregnant persons",
-                "vaccine coverage"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Vax Views",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9wzx-rwzv",
-            "description": "Monthly Cumulative Influenza Vaccination Coverage, by Race/Ethnicity, Pregnant Persons 18 years to 49 years, United States",
-            "title": "Monthly Cumulative Influenza Vaccination Coverage, by Race/Ethnicity, Pregnant Persons 18 years to 49 years, United States",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/9wzx-rwzv/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9wzx-rwzv/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9wzx-rwzv/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9wzx-rwzv/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9wzx-rwzv/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9wzx-rwzv/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9wzx-rwzv/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "theme": [
-                "Pregnancy & Vaccination"
-            ],
-            "language": [
-                "English"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/9x7v-wy9u",
@@ -21902,77 +21627,6 @@
                 "National Institute for Occupational Safety and Health"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-12-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-20",
-            "references": [
-                "https://wwwdev.cdc.gov/visionhealth/vehss/data/claims/marketscan.html",
-                "https://marketscan.truvenhealth.com/marketscanportal/"
-            ],
-            "keyword": [
-                "claims",
-                "diagnosed prevalence",
-                "eye exams",
-                "marketscan",
-                "medical diagnoses",
-                "service utilization",
-                "truven"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/a35h-9yn4",
-            "description": "2016. This dataset is a de-identified summary table of prevalence rates for vision and eye health data indicators from the 2016 MarketScan\u00ae Commercial Claims and Encounters Data (CCAE) is produced by Truven Health Analytics, a division of IBM Watson Health.  The CCEA data contain a convenience sample of insurance claims information from person with employer-sponsored insurance and their dependents, including 43.6 million person years of data. Prevalence estimates are stratified by all available combinations of age group, gender, and state.  Detailed information on VEHSS MarketScan analyses can be found on the VEHSS MarketScan webpage (cdc.gov/visionhealth/vehss/data/claims/marketscan.html). Information on available Medicare claims data can be found on the IBM MarketScan website (https://marketscan.truvenhealth.com). The VEHSS MarketScan summary dataset was last updated November 2019.",
-            "title": "Commercial Medical Insurance (MSCANCC) - Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/a35h-9yn4/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/a35h-9yn4/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/a35h-9yn4/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/a35h-9yn4/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/a35h-9yn4/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/a35h-9yn4/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/a35h-9yn4/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Shell-Commercial-Medical-Insurance-MSCANCC-Vision-/a35h-9yn4",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "theme": [
-                "Vision & Eye Health"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/a37y-w96i",
@@ -25855,23 +25509,23 @@
             "@type": "dcat:Dataset",
             "modified": "2025-01-31",
             "keyword": [
-                "covid-19",
-                "covid19",
                 "covid",
-                "surveillance",
-                "hospitalizations",
-                "respiratory virus response",
-                "respiratory illness",
-                "covid-net",
+                "covid19",
+                "covid-19",
                 "covidnet",
-                "respnet",
-                "resp-net",
+                "covid-net",
+                "epi curve",
+                "hospitalizations",
                 "icu",
                 "in-hospital death",
                 "percent icu",
                 "percent in-hospital death",
                 "percent mechanically ventilated",
-                "epi curve"
+                "respiratory illness",
+                "respiratory virus response",
+                "respnet",
+                "resp-net",
+                "surveillance"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -25976,66 +25630,6 @@
                 }
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/binw-6h77",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-10-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-30",
-            "keyword": [
-                "vision"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CDC Info",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/binw-6h77",
-            "description": "The Department of Defense Health Agency\u2019s (DHA) Vision Center of Excellence (VCE) analyzed data from the MHS MART database on behalf of the VEHSS project.  MHS MART is a data management and reporting system used to support decision-making, health care analysis, and operational reporting. MART integrates various sources within MHS to provide a centralized repository for health care data, facilitating access to information that aids in managing health care services, resources, and performance across MHS.\n\nData are based on claims and encounter records in the MHS Management Analysis and Reporting Tool (MART) database. The population includes all active-duty and retired military members and their dependents in the MHS. The sample size is approximately 9.08 million persons.\n\nThese data are also available in the VEHSS Data Explorer, an interactive data visualization tool reporting prevalence information from more than 10 data sources: https://www.cdc.gov/vision-health-data/index.html",
-            "title": "Military Health System (MHS) - Vision and Eye Health Surveillance System (VEHSS)",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/binw-6h77/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/binw-6h77/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/binw-6h77/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/binw-6h77/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/binw-6h77/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/binw-6h77/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/binw-6h77/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "theme": [
-                "Vision & Eye Health"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://www.cdc.gov/nchs/hus",
@@ -27134,78 +26728,6 @@
                 "National Institute for Occupational Safety and Health"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-09-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-21",
-            "references": [
-                "https://wwwdev.cdc.gov/visionhealth/vehss/data/claims/medicaid.html",
-                "https://www.medicaid.gov/medicaid/index.html"
-            ],
-            "keyword": [
-                "claims",
-                "diagnosed prevalence",
-                "eye exams",
-                "max",
-                "medicaid",
-                "medical diagnoses",
-                "screening",
-                "service utilization"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/bwx3-gx66",
-            "description": "2016-2019. This dataset is a de-identified summary table of prevalence rates for vision and eye health data indicators from the Medicaid Analytic eXtract (MAX) data. Medicaid MAX are a set of de-identified person-level data files with information on Medicaid eligibility, service utilization, diagnoses, and payments. The MAX data contain a convenience sample of claims processed by Medicaid and Children\u2019s Health Insurance Program (CHIP) fee for service and managed care plans.  Not all states are included in MAX in all years, and as of November 2019, 2014 data is the latest available.  Prevalence estimates are stratified by all available combinations of age group, gender, and state.  Detailed information on VEHSS Medicare analyses can be found on the VEHSS Medicaid MAX webpage (cdc.gov/visionhealth/vehss/data/claims/medicaid.html). Information on available Medicare claims data can be found on the ResDac website (www.resdac.org). The VEHSS Medicaid MAX dataset was last updated May 2023.",
-            "title": "Medicaid Claims (MAX) - Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/bwx3-gx66/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bwx3-gx66/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/bwx3-gx66/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bwx3-gx66/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/bwx3-gx66/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bwx3-gx66/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/bwx3-gx66/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Private-Medicaid-Claims-MAX-Vision-and-Eye-Health-/bwx3-gx66",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "theme": [
-                "Vision & Eye Health"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/bx8m-di6q",
@@ -28049,23 +27571,23 @@
             "@type": "dcat:Dataset",
             "modified": "2025-01-31",
             "keyword": [
-                "covid-19",
-                "covid19",
                 "covid",
-                "surveillance",
-                "hospitalizations",
-                "respiratory virus response",
-                "respiratory-virus-response",
-                "respiratory disease",
-                "respiratory illness",
+                "covid19",
+                "covid-19",
                 "covidnet",
                 "covid-net",
-                "respnet",
-                "resp-net",
                 "hospitalization rate",
+                "hospitalizations",
                 "rate",
+                "rates by age group",
                 "rates by race and ethnicity",
-                "rates by age group"
+                "respiratory disease",
+                "respiratory illness",
+                "respiratory virus response",
+                "respiratory-virus-response",
+                "respnet",
+                "resp-net",
+                "surveillance"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -30301,75 +29823,6 @@
                 "NCHS"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-09-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-21",
-            "references": [
-                "http://childhealthdata.org/learn/NSCH",
-                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/national-survey-of-childrens-health.html"
-            ],
-            "keyword": [
-                "contact lenses",
-                "glasses",
-                "nsch",
-                "vision impairment",
-                "visual function"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/de4p-4g3k",
-            "description": "2016-17 merged. This dataset is a de-identified summary table of vision and eye health data indicators from the National Survye of Chilrens Health (NSCH), stratified by all available combinations of age group, race/ethnicity, gender, risk factor and state. NSCH is a telephone survey conducted by the National Center for Health Statistics at CDC (currently conducted by the U.S. Census Bureau) that examines the physical and emotional health of children 0-17 years of age. Approximate sample size is 95,000 over two rounds of data collection. Data were suppressed for cell sizes less than 30 persons, or where the relative standard error more than 30% of the mean. Detailed information on VEHSS NSCH analyses can be found on the VEHSS NSCH webpage (cdc.gov/visionhealth/vehss/data/national-surveys/national-survey-of-childrens-health.html). Additional information about NSCH can be found on the NSCH website (http://childhealthdata.org/learn/NSCH). The VEHSS NSCH dataset was last updated in November 2019.",
-            "title": "National Survey of Children\u2019s Health (NSCH) \u2013 Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:029"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/de4p-4g3k/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/de4p-4g3k/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/de4p-4g3k/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/de4p-4g3k/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/de4p-4g3k/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/de4p-4g3k/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/de4p-4g3k/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/d/de4p-4g3k",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "theme": [
-                "Vision & Eye Health"
-            ]
-        },
         {
             "accessLevel": "public",
             "bureauCode": [
@@ -32040,76 +31493,6 @@
                 "NNDSS"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2021-06-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-21",
-            "references": [
-                "https://www.resdac.org",
-                "https://www.cdc.gov/visionhealth/vehss/data/claims/medicare.html"
-            ],
-            "keyword": [
-                "claims",
-                "eye exams",
-                "medical diagnoses",
-                "medicare",
-                "service utilization",
-                "treated prevalence"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/e28h-tx85",
-            "description": "2014-2019. This dataset is a de-identified summary table of vision and eye health data indicators from Medicare claims, stratified by all available combinations of age group, race/ethnicity, gender, and state. Medicare claims for VEHSS includes beneficiaries who were fully enrolled in Medicare Part B Fee-for-Service (FFS) for the duration of the year. Medicare claims provide a convenience sample that includes approximately 30 million individuals annually, which represents nearly 89% of the US population aged 65 and older and 3.3% of the US population younger than 65, including persons disabled due to blindness. Medicare data for VEHSS include Service Utilization and Medical Diagnoses indicators. Data were suppressed for de-identification to ensure protection of patient privacy. Data will be updated as it becomes available. Detailed information on VEHSS Medicare analyses can be found on the VEHSS Medicare webpage (cdc.gov/visionhealth/vehss/data/claims/medicare.html). Information on available Medicare claims data can be found on the ResDac website (www.resdac.org). The VEHSS Medicare dataset was last updated May 2023.",
-            "title": "Medicare Claims \u2013 Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/e28h-tx85/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e28h-tx85/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/e28h-tx85/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/e28h-tx85/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/e28h-tx85/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e28h-tx85/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/e28h-tx85/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/d/e28h-tx85",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "theme": [
-                "Vision & Eye Health"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/provisional-maternal-deaths.htm",
@@ -37050,8 +36433,8 @@
             "modified": "2025-01-31",
             "keyword": [
                 "pregnancy",
-                "vsd",
-                "rsv"
+                "rsv",
+                "vsd"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -39026,75 +38409,6 @@
                 "NNDSS"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/adults-60-coverage-intent.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-11-07",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-08-28",
-            "keyword": [
-                "nis-acm",
-                "older adults",
-                "rsv",
-                "vaccination"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/gzbv-dn9g",
-            "description": "Weekly Intent for Vaccination and Cumulative Percentage of Adults 60 Years and Older Vaccinated with RSV Vaccine.\n\n \u2022 RSV vaccination coverage among adults ages 60 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly RSV vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n \u2022 The CDC recommended the RSV vaccine for adults ages 60 years and older in July 2023. (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)",
-            "title": "Weekly Intent for Vaccination and Cumulative Percentage of Adults 60 Years and Older Vaccinated with RSV Vaccine",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/gzbv-dn9g/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gzbv-dn9g/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/gzbv-dn9g/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gzbv-dn9g/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/gzbv-dn9g/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gzbv-dn9g/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/gzbv-dn9g/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "spatial": "United States- National, Region, State",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
-            "theme": [
-                "Vaccinations"
-            ],
-            "language": [
-                "English"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/h28b-t43q",
@@ -41991,7 +41305,7 @@
             "landingPage": "https://data.cdc.gov/d/hv7b-3sw8",
             "issued": "2023-06-22",
             "@type": "dcat:Dataset",
-            "modified": "2023-08-02",
+            "modified": "2025-01-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Surveillance and Epidemiology Branch, Immunization Services Division, NCIRD, CDC",
@@ -42002,8 +41316,8 @@
                 "name": "data.cdc.gov"
             },
             "identifier": "https://data.cdc.gov/api/views/hv7b-3sw8",
-            "description": "Estimates are for pregnant persons who are up-to-date with COVID-19 vaccines, overall and by race and ethnicity based on data from the Vaccine Safety Datalink*.",
-            "title": "Data: COVID-19 vaccination among pregnant people aged 18-49 years overall, by race and ethnicity, and date reported to CDC - Vaccine Safety Datalink,* United States",
+            "description": "Estimates are for pregnant women who are up-to-date with COVID-19 vaccines, overall and by race and ethnicity based on data from the Vaccine Safety Datalink*.",
+            "title": "Data: COVID-19 vaccination among pregnant women aged 18-49 years overall, by race and ethnicity, and date reported to CDC - Vaccine Safety Datalink,* United States",
             "programCode": [
                 "009:026"
             ],
@@ -48179,9 +47493,9 @@
             "temporal": "2023-2024",
             "modified": "2025-01-31",
             "keyword": [
+                "adults",
                 "covid-19 vaccination",
-                "nis-acm",
-                "adults"
+                "nis-acm"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -50093,30 +49407,30 @@
             "@type": "dcat:Dataset",
             "modified": "2025-01-31",
             "keyword": [
-                "covid-19",
-                "covid19",
                 "covid",
-                "respiratory syncytial virus",
-                "rsv",
+                "covid19",
+                "covid-19",
+                "covidnet",
+                "covid-net",
                 "flu",
-                "influenza",
-                "hospitalizations",
+                "flunet",
+                "flu-net",
+                "flusurvnet",
+                "flusurv-net",
                 "hospitalization",
                 "hospitalization rate",
-                "respnet",
-                "resp-net",
-                "respiratory virus response",
-                "respiratory illness",
-                "surveillance",
+                "hospitalizations",
+                "influenza",
                 "rate",
-                "rates by race and ethnicity",
                 "rates by age group",
-                "covidnet",
-                "covid-net",
-                "flusurvnet",
-                "flusurv-net",
-                "flunet",
-                "flu-net"
+                "rates by race and ethnicity",
+                "respiratory illness",
+                "respiratory syncytial virus",
+                "respiratory virus response",
+                "respnet",
+                "resp-net",
+                "rsv",
+                "surveillance"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -53372,75 +52686,6 @@
                 "NNDSS"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/adults-60-coverage-intent.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-11-07",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-08-28",
-            "keyword": [
-                "nis-acm",
-                "older adults",
-                "rsv",
-                "vaccination"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mx2d-yjrk",
-            "description": "Weekly RSV Vaccination Coverage of Adults 60 Years and Older by Demographic Characteristics \n\n\u2022 RSV vaccination coverage among adults 60 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly RSV vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n\u2022 The CDC recommended the RSV vaccine for adults 60 years and older in July 2023.  (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)",
-            "title": "Cumulative Percentage of Adults 60 Years and Older Vaccinated with RSV Vaccine by Demographic Characteristics",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/mx2d-yjrk/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mx2d-yjrk/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/mx2d-yjrk/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mx2d-yjrk/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/mx2d-yjrk/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mx2d-yjrk/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/mx2d-yjrk/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "spatial": "United States- National, Region, State",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
-            "theme": [
-                "Vaccinations"
-            ],
-            "language": [
-                "English"
-            ]
-        },
         {
             "accessLevel": "restricted public",
             "landingPage": "https://www.cdc.gov/nchs/nehrs/about.htm",
@@ -54992,11 +54237,11 @@
                 "Vaccine Safety Datalink"
             ],
             "keyword": [
-                "influenza",
+                "children",
                 "flu",
+                "influenza",
                 "nis",
                 "nis-flu",
-                "children",
                 "vaccine coverage"
             ],
             "contactPoint": {
@@ -56282,74 +55527,6 @@
                 "Policy"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adult-coverage-vaccination.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-11-03",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-08-28",
-            "keyword": [
-                "adults",
-                "covid-19 vaccination",
-                "nis-acm"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/pakc-hru3",
-            "description": "\u2022 COVID-19 vaccination coverage and intent among adults 18 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly COVID-19 vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine for adults ages 18 years and older.",
-            "title": "Weekly Intent for Vaccination and Cumulative Percentage of Adults 18 Years and Older Vaccinated with Updated 2023-24 COVID-19 Vaccine",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pakc-hru3/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/pakc-hru3/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/pakc-hru3/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/pakc-hru3/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/pakc-hru3/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/pakc-hru3/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/pakc-hru3/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "spatial": "United States- National, Region, State",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
-            "theme": [
-                "Vaccinations"
-            ],
-            "language": [
-                "English"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/paqx-33a8",
@@ -56610,21 +55787,21 @@
             "@type": "dcat:Dataset",
             "modified": "2025-01-31",
             "keyword": [
-                "rsv",
-                "surveillance",
-                "respiratory disease",
-                "respiratory syncytial virus",
-                "respiratory illness",
-                "respiratory virus response",
-                "hospitalizations",
+                "age-adjusted rates",
+                "age-adjusted rates by race and ethnicity",
                 "hospitalization rate",
+                "hospitalizations",
                 "rate",
                 "rates by age group",
                 "rates by race and ethnicity",
-                "age-adjusted rates",
-                "age-adjusted rates by race and ethnicity",
+                "respiratory disease",
+                "respiratory illness",
+                "respiratory syncytial virus",
+                "respiratory virus response",
+                "rsv",
                 "rsvnet",
-                "rsv-net"
+                "rsv-net",
+                "surveillance"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -57847,75 +57024,6 @@
                 "Injury & Violence"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-09-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-21",
-            "keyword": [
-                "diabetes",
-                "eye diseases",
-                "heart diseases",
-                "hypertension",
-                "physical activity",
-                "smoking",
-                "state",
-                "stroke",
-                "vhi",
-                "vision impairment"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/pttf-ck53",
-            "description": "2005-2016. This dataset includes data from the retired BRFSS Vision Module. From 2005-2011 the BRFSS employed a ten question vision module regarding vision impairment, access and utilization of eye care, and self-reported eye diseases. In 2013 and subsequently, one question in the core of BRFSS asks about vision: \u201cAre you blind or do you have serious difficulty seeing, even when wearing glasses?\u201d The latest data for this core question can be found in the Vision and Eye Health Surveillance System (VEHSS). VEHSS is intended to provide population estimates of vision loss function, eye diseases, health disparities, as well as barriers and facilitators to access to vision and eye care. This information can be used for designing, implementing, and evaluating vision and eye health prevention programs. To access the latest BRFSS data, (2013-2017) view the Behavioral Risk Factors \u2013 Vision and Eye Health Surveillance dataset (https://chronicdata.cdc.gov/Vision-Eye-Health/Behavioral-Risk-Factors-Vision-and-Eye-Health-Surv/vkwg-yswv).",
-            "title": "BRFSS Vision Module Data \u2013 Vision & Eye Health",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pttf-ck53/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/pttf-ck53/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/pttf-ck53/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/pttf-ck53/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/pttf-ck53/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/pttf-ck53/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/pttf-ck53/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Behavioral-Risk-Factors-Vision-Eye-Health/pttf-ck53",
-            "theme": [
-                "Vision & Eye Health"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/puin-6ss7",
@@ -59732,73 +58840,6 @@
                 "NCHS"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/estimates/amd-prevalence.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-08-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-18",
-            "references": [
-                "JAMA-Opthalmology forthcoming",
-                "https://jamanetwork.com/journals/jamaophthalmology"
-            ],
-            "keyword": [
-                "blind",
-                "blindness",
-                "prevalence",
-                "vision",
-                "visual"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CDC Info",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/qeru-k2y2",
-            "description": "VEHSS Composite Prevalence Estimates\n2017, 2019, 2021, 2022. This dataset contains estimates of the prevalence of visual acuity loss and major eye diseases generated using a Bayesian meta-analytic modeling approach that combines information from multiple data sources to produce comprehensive estimates of prevalence by age, race, and gender at the national, state and county levels. These composite prevalence estimates are the primary surveillance measures developed by the Centers for Disease Control and Prevention\u2019s Vision & Eye Health Surveillance System (VEHSS).  \n\nFor more information about these estimates including summary tables and maps, methods, and links to related publications visit https://www.cdc.gov/visionhealth/vehss/estimates/index.html\nTo view this data in the VEHSS interactive data visualization application, visit https://ddt-vehss.cdc.gov/ and search for \u201cVEHSS Composite Prevalence Estimate\u201d.\n\n\nVisual Acuity Loss:\nVisual acuity loss prevalence estimates represent best-corrected visual acuity in the better-seeing eye and are included in rows where Category=\u2019Measured Visual Acuity\u2019.  Rows with Subgroup = \u2018Any vision loss' represents any impairment or blindness of 20/40 or worse; rows with Subgroup = 'US-defined blindness' refers to the subset of vision loss that is 20/200 or worse.\n\n\nAge Related Macular Degeneration:\nThe age-related macular degeneration (AMD) estimates represent AMD as measured with retinal imaging examination, and are included in rows where Category = \u2018Age Related Macular Degeneration\u2019.  The Subgroup \u2018Vision threatening AMD\u2019 includes patients with geographic atrophy, wet-form AMD, or choroidal neovascularization in either eye. The Subgroup \u2018Non-vision threatening AMD\u2019 includes patients with early or intermediate dry-form AMD defined as retinal pigment epithelium abnormalities or drusen \u2265125 \u00b5m in the worse-affected eye, and do not have vision threatening AMD.\n\n\nDiabetic Retinopathy:\nThe diabetic retinopathy (DR) estimates represent DR as measured with retinal imaging examination, and are included in rows where Category=\u2019Diabetic Eye Diseases\u2019.  The Subgroup \u2018Vision threatening DR\u2019 includes patients with severe non-proliferative DR, proliferative DR, and diabetic macular edema. The Subgroup \u2018Non-vision threatening DR\u2019 is defined as patients with mild-moderate non-proliferative DR or unspecified DR, and do not have vision threatening DR.\n\n\nGlaucoma:\nThe glaucoma estimates represent glaucoma as measured with retinal imaging examination and are included in rows where Category=\u2019Glaucoma\u2019. The Subgroup \u2018Vision affecting glaucoma\u2019 includes people with glaucoma and abnormal visual field. The Subgroup \u2018Non-vision affecting glaucoma\u2019 is defined as people with glaucoma without an abnormal visual field.\n\n\nAge Groups:\nThe VEHSS Composite Prevalence Estimates are available by major age groups (All ages, ages 0-17, 18-39, 40-64, 65-84, 85+) and detailed (5-year) age groups, which are indicated by the text \u201cby detailed age groups\u201d in the \u2018Indicator\u2019 field. \n\n\nPrevalence Data Type:\nThese estimates are also available as crude (Data_Value_Type = \u2018Crude Prevalence\u2019) or adjusted data (Data_Value_Type=\u2019Adjusted Prevalence).  Crude Prevalence is the estimate of the actual number and percentage of people living with each condition.  Adjusted Prevalence estimates are adjusted to match the national population by age, race/ethnicity, and gender.  Adjusted prevalence estimates can be used to help identify disparities in prevalence between geographic areas that are not explained by differences in demographic characteristics.\n\n  \nData Sources:\nData sources for VEHSS Composite Prevalence Estimates include the National Health and Nutrition Examination Survey (NHANES), the American Community Survey (ACS), the National Survey of Children\u2019s Health (NSCH), the Behavioral Risk Factor Surveillance System (BRFSS), Medicare Fee-For-Service claims, the Transformed Medicaid Statistical Information System, MarketScan commercial insurance",
-            "title": "VEHSS Composite Prevalence Estimates",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/qeru-k2y2/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/qeru-k2y2/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/qeru-k2y2/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/qeru-k2y2/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/qeru-k2y2/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/qeru-k2y2/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/qeru-k2y2/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "theme": [
-                "Vision & Eye Health"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
@@ -66832,79 +65873,6 @@
                 }
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-09-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-21",
-            "references": [
-                "https://www.cdc.gov/nchs/nhanes/index.htm",
-                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/national-health-and-nutrition-examination-survey.html"
-            ],
-            "keyword": [
-                "blind",
-                "cataract",
-                "diabetes",
-                "glaucoma",
-                "nhanes",
-                "service utilization",
-                "vision exam measures",
-                "visual acuity",
-                "visual function"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/tdbk-8ubw",
-            "description": "1999-2008; 2005-2008. This dataset is a de-identified summary table of vision and eye health data indicators from NHANES, stratified by all available combinations of age group, race/ethnicity, gender, and risk factor. NHANES is a program of studies conducted by the National Center for Health Statistics at CDC designed to assess the health and nutritional status of adults and children in the U.S, and combines interviews and physical examinations. NHANES stopped collecting vision and eye health data in 2008. Approximate sample size is 5,000 persons per year. NHANES data for VEHSS includes questions and examinations related to Visual Function, Vision Exam Measures, Eye Health Conditions, Service Utilization, and Examination Measures. Data were suppressed for cell sizes less than 30 persons, or where the relative standard error more than 30% of the mean. Detailed information on VEHSS NHANES analyses can be found on the VEHSS NHANES webpage (https://www.cdc.gov/visionhealth/vehss/data/national-surveys/national-health-and-nutrition-examination-survey.html). Additional information about NHANES can be found on the NHANES website (https://www.cdc.gov/nchs/nhanes/index.htm). The VEHSS NHANES dataset was last updated in June 2018.",
-            "title": "National Health and Nutrition Examination Survey (NHANES) \u2013 Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tdbk-8ubw/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/tdbk-8ubw/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/tdbk-8ubw/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/tdbk-8ubw/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/tdbk-8ubw/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/tdbk-8ubw/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/tdbk-8ubw/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/National-Health-and-Nutrition-Examination-Survey-N/tdbk-8ubw",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "theme": [
-                "Vision & Eye Health"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/tdge-ieq8",
@@ -67262,74 +66230,6 @@
                 "en-US"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "references": [
-                "https://www.census.gov/content/dam/Census/programs-surveys/acs/about/ACS_Information_Guide.pdf",
-                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/american-community-survey.html"
-            ],
-            "keyword": [
-                "acs",
-                "contact lenses",
-                "glasses",
-                "visual function"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/thir-stei",
-            "description": "2014 - 2022 (excluding 2020). This dataset is a de-identified summary table of vision and eye health data indicators from ACS, stratified by all available combinations of age group, race/ethnicity, gender, and state. ACS is an annual nationwide survey conducted by the U.S. Census Bureau that collects information on demographic, social, economic, and housing characteristics of the U.S. population. Approximate sample size is 3 million annually. ACS data for VEHSS includes one question related to Visual Function. Data were suppressed for cell sizes less than 30 persons, or where the relative standard error more than 30% of the mean. Data will be updated as it becomes available. Detailed information on VEHSS ACS analyses can be found on the VEHSS ACS webpage (link). Additional information about ACS can be found on the U.S. Census Bureau website (https://www.census.gov/content/dam/Census/programs-surveys/acs/about/ACS_Information_Guide.pdf). The VEHSS ACS dataset was last updated April 2024",
-            "title": "American Community Survey (ACS) \u2013 Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/thir-stei/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/thir-stei/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/thir-stei/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/thir-stei/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/thir-stei/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/thir-stei/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/thir-stei/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/d/thir-stei",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "theme": [
-                "Vision & Eye Health"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://www.cdc.gov/statesystem/index.html",
@@ -70038,11 +68938,11 @@
             "temporal": "2024-2025",
             "modified": "2025-01-31",
             "keyword": [
-                "nis-acm",
                 "iis",
                 "iqvia",
-                "vsd",
-                "rsv vaccination"
+                "nis-acm",
+                "rsv vaccination",
+                "vsd"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -72209,74 +71109,6 @@
                 "Flu Vaccinations"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-03-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-20",
-            "references": [
-                "https://www.cdc.gov/brfss",
-                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/behavioral-risk-factors-surveillance-system.html"
-            ],
-            "keyword": [
-                "brfss",
-                "contact lenses",
-                "glasses",
-                "visual function"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/vkwg-yswv",
-            "description": "2013-2018. This dataset is a de-identified summary table of vision and eye health data indicators from BRFSS, stratified by all available combinations of age group, race/ethnicity, gender, risk factor and state. BRFSS is a system of telephone surveys conducted by CDC that collect state data about U.S. residents regarding their health-related risk behaviors, chronic health conditions, and use of preventive services. BRFSS completes more than 400,000 adult interviews each year across 50 states, the District of Columbia, and three U.S. territories. BRFSS data for VEHSS includes one question from the core component related to Visual Function. Data were suppressed following NCHS standards. Data will be updated as it becomes available. Detailed information on VEHSS BRFSS analyses can be found on the VEHSS BRFSS webpage (link). General information about BRFSS can be found on the BRFSS website (https://www.cdc.gov/brfss). The VEHSS BRFSS dataset was last updated in November 2019.",
-            "title": "Behavioral Risk Factors \u2013 Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vkwg-yswv/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/vkwg-yswv/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/vkwg-yswv/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/vkwg-yswv/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/vkwg-yswv/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/vkwg-yswv/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/vkwg-yswv/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/d/vkwg-yswv",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "theme": [
-                "Vision & Eye Health"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "http://www.cdc.gov/tobacco/stateandcommunity/best_practices/",
@@ -74361,7 +73193,7 @@
             "landingPage": "https://data.cdc.gov/d/w6be-99qd",
             "issued": "2022-02-01",
             "@type": "dcat:Dataset",
-            "modified": "2023-06-23",
+            "modified": "2025-01-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Surveillance and Epidemiology Branch, Immunization Services Division, NCIRD, CDC",
@@ -74372,8 +73204,8 @@
                 "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
             },
             "identifier": "https://data.cdc.gov/api/views/w6be-99qd",
-            "description": "These weekly COVID-19 vaccination coverage estimates are for pregnant persons who are fully vaccinated before and during pregnancy based on data  from the Vaccine Safety Datalink*.",
-            "title": "Weekly Data: COVID-19 vaccination among pregnant people ages 18-49 years before and during pregnancy overall, by race/ethnicity, and week ending date - Vaccine Safety Datalink,* United States",
+            "description": "These weekly COVID-19 vaccination coverage estimates are for pregnant women who are fully vaccinated before and during pregnancy based on data from the Vaccine Safety Datalink*.",
+            "title": "Weekly Data: COVID-19 vaccination among pregnant women ages 18-49 years before and during pregnancy overall, by race/ethnicity, and week ending date - Vaccine Safety Datalink,* United States",
             "programCode": [
                 "009:026"
             ],
@@ -76937,12 +75769,12 @@
             "@type": "dcat:Dataset",
             "modified": "2025-01-31",
             "keyword": [
-                "nndss",
                 "2022",
-                "wonder",
                 "2023",
                 "2024",
-                "2025"
+                "2025",
+                "nndss",
+                "wonder"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -80279,8 +79111,8 @@
             "temporal": "2023-2024",
             "modified": "2025-01-31",
             "keyword": [
-                "nis",
-                "covid-19 vaccination"
+                "covid-19 vaccination",
+                "nis"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
```

### Changes from 792c471 to 29aa757
**Author:** Automated

**Date:** 2025-01-31 20:10:42+00:00

**Message:** Updated data: Fri Jan 31 20:10:42 UTC 2025

```diff
diff --git a/cdc.json b/cdc.json
index 80fa566..0098ac5 100644
--- a/cdc.json
+++ b/cdc.json
@@ -41401,74 +41401,6 @@
                 "500 Cities & Places"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adult-coverage-vaccination.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-11-07",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-08-28",
-            "keyword": [
-                "adults",
-                "covid-19 vaccination",
-                "nis-acm"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hm35-qkiu",
-            "description": "Weekly COVID-19 Vaccination Coverage of Adults 18 Years and Older by Demographic Characteristics \n\n\u2022 COVID-19 vaccination coverage among adults 18 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly COVID-19 vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n \n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine for adults ages 18 years and older.",
-            "title": "Cumulative Percentage of Adults 18 Years and Older Vaccinated with the Updated 2023-24 COVID-19 Vaccine",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hm35-qkiu/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hm35-qkiu/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/hm35-qkiu/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hm35-qkiu/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/hm35-qkiu/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hm35-qkiu/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/hm35-qkiu/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "spatial": "United States- National, Region, State",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
-            "theme": [
-                "Vaccinations"
-            ],
-            "language": [
-                "English"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/hm3s-vk7u",
@@ -43859,7 +43791,7 @@
             "issued": "2024-02-07",
             "temporal": "1999-2018",
             "@type": "dcat:Dataset",
-            "modified": "2024-09-17",
+            "modified": "2025-01-31",
             "references": [
                 "https://www.cdc.gov/nchs/nhanes/visualization/"
             ],
@@ -47399,71 +47331,6 @@
                 "500 Cities & Places"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/healthyyouth/about/index.htm",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "keyword": [
-                "middle school",
-                "risk behavior",
-                "survey",
-                "youth online",
-                "yrbs"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DASH Public Inquiries",
-                "hasEmail": "mailto:nccddashinfo@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/k5bc-k3g8",
-            "description": "1991-2017. Middle School Dataset. The Youth Risk Behavior Surveillance System (YRBSS) monitors six categories of priority health behaviors \r\namong youth and young adults: 1) behaviors that contribute to unintentional injuries and violence; 2) tobacco use; 3) alcohol and \r\nother drug use; 4) sexual behaviors related to unintended pregnancy and sexually transmitted infections (STIs), including human \r\nimmunodeficiency virus (HIV) infection; 5) unhealthy dietary behaviors; and 6) physical inactivity. In addition, YRBSS monitors \r\nthe prevalence of obesity and asthma and other priority health behaviors.",
-            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): Middle School",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/k5bc-k3g8/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k5bc-k3g8/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/k5bc-k3g8/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/k5bc-k3g8/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/k5bc-k3g8/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k5bc-k3g8/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/k5bc-k3g8/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/k5bc-k3g8",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "theme": [
-                "Youth Risk Behaviors"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
@@ -58624,72 +58491,6 @@
                 "NNDSS"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/healthyyouth/about/index.htm",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "keyword": [
-                "global",
-                "gshs",
-                "risk behavior",
-                "student health",
-                "survey",
-                "youth online"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DASH Publc Inquiries",
-                "hasEmail": "mailto:nccdDashInfo@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/pxpe-pgrg",
-            "description": "2003-2015. Global School dataset.  The Global School-based Student Health Survey (GSHS) was developed by the World Health Organization (WHO) in collaboration with the United Nations' UNICEF, UNESCO, and UNAIDS; and with technical assistance from CDC.  The GSHS is a school-based survey conducted primarily among students aged 13-17 years in countries around the world.  It uses core questionnaire modules that address the leading causes of morbidity and mortality among children and adults worldwide: 1) Alcohol use, 2) dietary behaviors, 3) drug use, 4) hygiene, 5) mental health, 6) physical activity, 7) protective factors, 8) sexual behaviors that contribute to HIV infection, other sexually-transmitted infections, and unintended pregnancy, 9) tobacco use, and 10) violence and unintentional injury.  This dataset contains global data from 2003 \u2013 2015.  Additional information about the GSHS can be found at https://www.cdc.gov/gshs/index.htm.",
-            "title": "DASH - Global School-based Student Health Survey (GSHS)",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pxpe-pgrg/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/pxpe-pgrg/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/pxpe-pgrg/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/pxpe-pgrg/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/pxpe-pgrg/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/pxpe-pgrg/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/pxpe-pgrg/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Global-School-based-Student-Health-Survey-GSH/pxpe-pgrg",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "theme": [
-                "Youth Risk Behaviors"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/q2dj-esu7",
@@ -58829,73 +58630,6 @@
                 "en-US"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/healthyyouth/about/index.htm",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-07-14",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "keyword": [
-                "high school",
-                "risk behavior",
-                "sexual contacts",
-                "sexual identity",
-                "sexual orientation",
-                "survey",
-                "youth online",
-                "yrbs"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DASH Public Inquiries",
-                "hasEmail": "mailto:nccddashinfo@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/q6p7-56au",
-            "description": "2015-2017. High School Dataset \u2013 Including Sexual Orientation. The Youth Risk Behavior Surveillance System (YRBSS) monitors six categories of priority health behaviors\r\namong youth and young adults: 1) behaviors that contribute to unintentional injuries and violence; 2) tobacco use; 3) alcohol and\r\nother drug use; 4) sexual behaviors related to unintended pregnancy and sexually transmitted infections (STIs), including human\r\nimmunodeficiency virus (HIV) infection; 5) unhealthy dietary behaviors; and 6) physical inactivity. In addition, YRBSS monitors\r\nthe prevalence of obesity and asthma and other priority health behaviors.  This dataset contains national, state, and local data from 2015 that includes two aspects of sexual orientation \u2013 sexual identity and sex of sexual contacts.  Additional information about the YRBSS can be found at www.cdc.gov/yrbss.",
-            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): High School \u2013  Including Sexual Orientation",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/q6p7-56au/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/q6p7-56au/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/q6p7-56au/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/q6p7-56au/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/q6p7-56au/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/q6p7-56au/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/q6p7-56au/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/q6p7-56au",
-            "theme": [
-                "Youth Risk Behaviors"
-            ]
-        },
         {
             "accessLevel": "restricted public",
             "landingPage": "https://data.cdc.gov/d/q78n-cpzf",
@@ -66541,70 +66275,6 @@
                 "NCHS"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/healthyyouth/data/yrbs/index.htm",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-22",
-            "keyword": [
-                "behaviors",
-                "dash",
-                "youth risk",
-                "youth risk behavior surveillance system",
-                "yrbss"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DASH Public Inquiries",
-                "hasEmail": "mailto:nccddashinfo@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/svam-8dhg",
-            "description": "1991-2017. High School Dataset. The Youth Risk Behavior Surveillance System (YRBSS) monitors six categories of priority health behaviors \r\namong youth and young adults: 1) behaviors that contribute to unintentional injuries and violence; 2) tobacco use; 3) alcohol and \r\nother drug use; 4) sexual behaviors related to unintended pregnancy and sexually transmitted infections (STIs), including human \r\nimmunodeficiency virus (HIV) infection; 5) unhealthy dietary behaviors; and 6) physical inactivity. In addition, YRBSS monitors \r\nthe prevalence of obesity and asthma and other priority health behaviors.",
-            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): High School - Excluding Sexual Identity",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/svam-8dhg/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/svam-8dhg/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/svam-8dhg/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/svam-8dhg/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/svam-8dhg/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/svam-8dhg/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/svam-8dhg/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/svam-8dhg",
-            "theme": [
-                "Youth Risk Behaviors"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://www.cdc.gov/fluvaxview/dashboard/adult-coverage.html",
@@ -70368,11 +70038,11 @@
             "temporal": "2024-2025",
             "modified": "2025-01-31",
             "keyword": [
+                "nis-acm",
                 "iis",
                 "iqvia",
-                "nis-acm",
-                "rsv vaccination",
-                "vsd"
+                "vsd",
+                "rsv vaccination"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -77265,14 +76935,14 @@
             ],
             "issued": "2022-01-18",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
+            "modified": "2025-01-31",
             "keyword": [
+                "nndss",
                 "2022",
+                "wonder",
                 "2023",
                 "2024",
-                "2025",
-                "nndss",
-                "wonder"
+                "2025"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
```

### Changes from b8668a8 to 792c471
**Author:** Automated

**Date:** 2025-01-31 19:12:14+00:00

**Message:** Updated data: Fri Jan 31 19:12:14 UTC 2025

```diff
diff --git a/cdc.json b/cdc.json
index 5f81ca8..80fa566 100644
--- a/cdc.json
+++ b/cdc.json
@@ -782,23 +782,23 @@
             ],
             "issued": "2024-07-23",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "keyword": [
-                "age-adjusted rates",
-                "age-adjusted rates by race and ethnicity",
+                "rsv",
+                "surveillance",
+                "respiratory disease",
+                "respiratory syncytial virus",
+                "respiratory illness",
+                "respiratory virus response",
+                "hospitalizations",
                 "hospitalization",
                 "hospitalization rate",
-                "hospitalizations",
                 "rate",
                 "rates by race and ethnicity",
-                "respiratory disease",
-                "respiratory illness",
-                "respiratory syncytial virus",
-                "respiratory virus response",
-                "rsv",
-                "rsvnet",
                 "rsv-net",
-                "surveillance"
+                "rsvnet",
+                "age-adjusted rates",
+                "age-adjusted rates by race and ethnicity"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -5579,19 +5579,19 @@
                 "https://www.cdc.gov/nchs/data/nhis/SHS_Tech_Notes.pdf"
             ],
             "keyword": [
-                "summary health statistics",
                 "nhis",
-                "sdoh-poverty-income",
+                "sdoh-access-to-health-care",
                 "sdoh-employment",
+                "sdoh-food-access",
                 "sdoh-food-insecurity",
-                "sdoh-housing-stability",
-                "sdoh-high-school",
                 "sdoh-higher-education",
-                "sdoh-access-to-health-care",
+                "sdoh-high-school",
+                "sdoh-housing-stability",
+                "sdoh-poverty-income",
                 "sdoh-source-of-health-care",
                 "sdoh-use-of-health-care",
-                "sdoh-food-access",
-                "sdoh-workplace"
+                "sdoh-workplace",
+                "summary health statistics"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -10561,12 +10561,12 @@
             "issued": "2023-12-11",
             "@type": "dcat:Dataset",
             "temporal": "2023-2024",
-            "modified": "2024-09-11",
+            "modified": "2025-01-31",
             "keyword": [
-                "nis-acm",
-                "older adults",
+                "vaccination",
                 "rsv",
-                "vaccination"
+                "older adults",
+                "nis-acm"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -11847,23 +11847,23 @@
             ],
             "issued": "2024-06-26",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "keyword": [
-                "covid",
                 "covid19",
+                "covid",
                 "covid-19",
-                "covidnet",
+                "surveillance",
+                "hospitalizations",
+                "respiratory virus response",
+                "respiratory illness",
                 "covid-net",
+                "resp-net",
+                "covidnet",
+                "respnet",
                 "hospitalization rate",
-                "hospitalizations",
                 "rate",
-                "rates by age group",
                 "rates by race and ethnicity",
-                "respiratory illness",
-                "respiratory virus response",
-                "respnet",
-                "resp-net",
-                "surveillance"
+                "rates by age group"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -16785,12 +16785,12 @@
             "temporal": "2024-2025",
             "modified": "2025-01-31",
             "keyword": [
-                "flu vaccination",
-                "iis",
                 "iqvia",
                 "nis-acm",
+                "vsd",
+                "iis",
                 "nis-flu",
-                "vsd"
+                "flu vaccination"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -23049,13 +23049,13 @@
             "temporal": "October 1, 2024 - no specified end date",
             "modified": "2025-01-31",
             "keyword": [
-                "covid-19",
-                "hospitalizations",
                 "coronavirus",
+                "covid-19",
                 "deaths",
+                "disease burden",
+                "hospitalizations",
                 "illnesses",
-                "outpatient visits",
-                "disease burden"
+                "outpatient visits"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -25853,25 +25853,25 @@
             ],
             "issued": "2023-09-22",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "keyword": [
-                "covid",
-                "covid19",
                 "covid-19",
-                "covidnet",
-                "covid-net",
-                "epi curve",
+                "covid19",
+                "covid",
+                "surveillance",
                 "hospitalizations",
+                "respiratory virus response",
+                "respiratory illness",
+                "covid-net",
+                "covidnet",
+                "respnet",
+                "resp-net",
                 "icu",
                 "in-hospital death",
                 "percent icu",
                 "percent in-hospital death",
                 "percent mechanically ventilated",
-                "respiratory illness",
-                "respiratory virus response",
-                "respnet",
-                "resp-net",
-                "surveillance"
+                "epi curve"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -28047,25 +28047,25 @@
             ],
             "issued": "2024-06-26",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "keyword": [
-                "covid",
-                "covid19",
                 "covid-19",
-                "covidnet",
-                "covid-net",
-                "hospitalization rate",
+                "covid19",
+                "covid",
+                "surveillance",
                 "hospitalizations",
-                "rate",
-                "rates by age group",
-                "rates by race and ethnicity",
-                "respiratory disease",
-                "respiratory illness",
                 "respiratory virus response",
                 "respiratory-virus-response",
+                "respiratory disease",
+                "respiratory illness",
+                "covidnet",
+                "covid-net",
                 "respnet",
                 "resp-net",
-                "surveillance"
+                "hospitalization rate",
+                "rate",
+                "rates by race and ethnicity",
+                "rates by age group"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -37047,11 +37047,11 @@
             "issued": "2023-12-11",
             "@type": "dcat:Dataset",
             "temporal": "2023-2024",
-            "modified": "2024-04-17",
+            "modified": "2025-01-31",
             "keyword": [
                 "pregnancy",
-                "rsv",
-                "vsd"
+                "vsd",
+                "rsv"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -37063,8 +37063,8 @@
                 "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
             },
             "identifier": "https://data.cdc.gov/api/views/g4jn-64pd",
-            "description": "Weekly RSV Vaccination Coverage, Pregnant Persons 18-49 Years Old\n\n\u2022 RSV vaccination coverage among pregnant persons is assessed through the Vaccine Safety Datalink*\n\n\u2022 Data on RSV vaccinations among pregnant persons was available starting September 22, 2023, and includes doses received starting September 24, 2023.",
-            "title": "Weekly Respiratory Syncytial Virus (RSV) Vaccination Coverage among Pregnant Persons by Race and Ethnicity",
+            "description": "Weekly RSV Vaccination Coverage, Pregnant Women 18-49 Years Old\n\n\u2022 RSV vaccination coverage among pregnant women is assessed through the Vaccine Safety Datalink*\n\n\u2022 Data on RSV vaccinations among pregnant women was available starting September 22, 2023, and includes doses received starting September 24, 2023.",
+            "title": "Weekly Respiratory Syncytial Virus (RSV) Vaccination Coverage among Pregnant Women by Race and Ethnicity",
             "programCode": [
                 "009:020"
             ],
@@ -38373,18 +38373,18 @@
                 "https://wwwn.cdc.gov/NHISDataQueryTool/SHS_adult/SHS_Tech_Notes.pdf"
             ],
             "keyword": [
-                "summary health statistics",
                 "nhis",
-                "sdoh-poverty-income",
+                "sdoh-access-to-health-care",
                 "sdoh-employment",
+                "sdoh-food-access",
                 "sdoh-food-insecurity",
-                "sdoh-housing-stability",
                 "sdoh-higher-education",
-                "sdoh-access-to-health-care",
+                "sdoh-housing-stability",
+                "sdoh-poverty-income",
                 "sdoh-source-of-health-care",
                 "sdoh-use-of-health-care",
-                "sdoh-food-access",
-                "sdoh-workplace"
+                "sdoh-workplace",
+                "summary health statistics"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -40534,79 +40534,6 @@
                 "English"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/aging/index.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-29",
-            "references": [
-                "https://www.cdc.gov/aging/index.html"
-            ],
-            "keyword": [
-                "aging",
-                "alcohol",
-                "caregiver",
-                "cognitive health",
-                "falls",
-                "fruits and vegetables",
-                "obesity",
-                "overall health",
-                "screenings",
-                "smoking",
-                "vaccines"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DPH Public Inquiries",
-                "hasEmail": "mailto:PublicInquiriesDPH@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hfr9-rurv",
-            "description": "2015-2022. This data set contains data from BRFSS.",
-            "title": "Alzheimer's Disease and Healthy Aging Data",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hfr9-rurv/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hfr9-rurv/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/hfr9-rurv/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hfr9-rurv/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/hfr9-rurv/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hfr9-rurv/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/hfr9-rurv/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/Healthy-Aging/Alzheimer-s-Disease-and-Healthy-Aging-Data/hfr9-rurv",
-            "theme": [
-                "Healthy Aging"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/hget-9fst",
@@ -41622,9 +41549,9 @@
             "temporal": "October 1, 2024 - no specified end date",
             "modified": "2025-01-31",
             "keyword": [
-                "rsv",
                 "hospitalizations",
-                "respiratory syncytial virus"
+                "respiratory syncytial virus",
+                "rsv"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -46568,9 +46495,9 @@
             "temporal": "2023-2024 & 2024-2025",
             "modified": "2025-01-31",
             "keyword": [
+                "flu vaccination",
                 "nis-ccm",
-                "nis-flu",
-                "flu vaccination"
+                "nis-flu"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -48318,8 +48245,8 @@
             "temporal": "2023-2024 & 2024-2025",
             "modified": "2025-01-31",
             "keyword": [
-                "nis-ccm",
-                "covid-19 vaccination"
+                "covid-19 vaccination",
+                "nis-ccm"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -48383,11 +48310,11 @@
             "issued": "2023-12-11",
             "@type": "dcat:Dataset",
             "temporal": "2023-2024",
-            "modified": "2024-08-28",
+            "modified": "2025-01-31",
             "keyword": [
-                "adults",
                 "covid-19 vaccination",
-                "nis-acm"
+                "nis-acm",
+                "adults"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -50297,32 +50224,32 @@
             ],
             "issued": "2024-05-03",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "keyword": [
-                "covid",
-                "covid19",
                 "covid-19",
-                "covidnet",
-                "covid-net",
+                "covid19",
+                "covid",
+                "respiratory syncytial virus",
+                "rsv",
                 "flu",
-                "flunet",
-                "flu-net",
-                "flusurvnet",
-                "flusurv-net",
+                "influenza",
+                "hospitalizations",
                 "hospitalization",
                 "hospitalization rate",
-                "hospitalizations",
-                "influenza",
-                "rate",
-                "rates by age group",
-                "rates by race and ethnicity",
-                "respiratory illness",
-                "respiratory syncytial virus",
-                "respiratory virus response",
                 "respnet",
                 "resp-net",
-                "rsv",
-                "surveillance"
+                "respiratory virus response",
+                "respiratory illness",
+                "surveillance",
+                "rate",
+                "rates by race and ethnicity",
+                "rates by age group",
+                "covidnet",
+                "covid-net",
+                "flusurvnet",
+                "flusurv-net",
+                "flunet",
+                "flu-net"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -54492,8 +54419,8 @@
             "temporal": "2023-2024 & 2024-2025",
             "modified": "2025-01-31",
             "keyword": [
-                "nis-ccm",
-                "covid-19 vaccination"
+                "covid-19 vaccination",
+                "nis-ccm"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -56814,23 +56741,23 @@
             ],
             "issued": "2024-07-23",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "keyword": [
-                "age-adjusted rates",
-                "age-adjusted rates by race and ethnicity",
-                "hospitalization rate",
+                "rsv",
+                "surveillance",
+                "respiratory disease",
+                "respiratory syncytial virus",
+                "respiratory illness",
+                "respiratory virus response",
                 "hospitalizations",
+                "hospitalization rate",
                 "rate",
                 "rates by age group",
                 "rates by race and ethnicity",
-                "respiratory disease",
-                "respiratory illness",
-                "respiratory syncytial virus",
-                "respiratory virus response",
-                "rsv",
+                "age-adjusted rates",
+                "age-adjusted rates by race and ethnicity",
                 "rsvnet",
-                "rsv-net",
-                "surveillance"
+                "rsv-net"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -58263,11 +58190,11 @@
             "temporal": "2023-24 & 2024-25",
             "modified": "2025-01-31",
             "keyword": [
-                "nis-acm",
-                "vsd",
+                "covid-19 vaccination",
                 "iis",
                 "iqvia",
-                "covid-19 vaccination"
+                "nis-acm",
+                "vsd"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -63159,18 +63086,18 @@
                 "NHSN Hospital Respiratory Data (HRD) Reporting: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html  NHSN Hospital Respiratory Data (HRD) Dashboard: https://wwwdev.cdc.gov/nhsn/psc/hospital-respiratory-dashboard.html#anchor_83745  Centers for Medicare and Medicaid Services (CMS) requirements: Updates to the Condition of Participation (CoP) Requirements for Hospitals and Critical Access Hospitals (CAHs) To Report Acute Respiratory Illnesses."
             ],
             "keyword": [
-                "covid-19",
-                "influenza",
-                "respiratory syncytial virus",
-                "rsv",
                 "admissions",
-                "hospitalizations",
+                "coronavirus",
+                "covid-19",
                 "hospital capacity",
+                "hospitalizations",
                 "hospital occupancy",
-                "inpatient beds",
                 "icu beds",
-                "coronavirus",
-                "respiratory"
+                "influenza",
+                "inpatient beds",
+                "respiratory",
+                "respiratory syncytial virus",
+                "rsv"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -66487,12 +66414,12 @@
             "temporal": "October 1, 2024 - no specified end date",
             "modified": "2025-01-31",
             "keyword": [
-                "rsv",
+                "deaths",
+                "disease burden",
                 "hospitalizations",
-                "respiratory syncytial virus",
                 "outpatient visits",
-                "deaths",
-                "disease burden"
+                "respiratory syncytial virus",
+                "rsv"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -69503,18 +69430,18 @@
                 "NHSN Hospital Respiratory Data (HRD) Reporting: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html  NHSN Hospital Respiratory Data (HRD) Dashboard: https://wwwdev.cdc.gov/nhsn/psc/hospital-respiratory-dashboard.html#anchor_83745  Centers for Medicare and Medicaid Services (CMS) requirements: Updates to the Condition of Participation (CoP) Requirements for Hospitals and Critical Access Hospitals (CAHs) To Report Acute Respiratory Illnesses."
             ],
             "keyword": [
-                "covid-19",
-                "influenza",
-                "respiratory syncytial virus",
-                "rsv",
                 "admissions",
-                "hospitalizations",
+                "coronavirus",
+                "covid-19",
                 "hospital capacity",
+                "hospitalizations",
                 "hospital occupancy",
-                "inpatient beds",
                 "icu beds",
-                "coronavirus",
-                "respiratory"
+                "influenza",
+                "inpatient beds",
+                "respiratory",
+                "respiratory syncytial virus",
+                "rsv"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -72828,9 +72755,9 @@
             "temporal": "2023-2024 & 2024-2025",
             "modified": "2025-01-31",
             "keyword": [
+                "flu vaccination",
                 "nis-ccm",
-                "nis-flu",
-                "flu vaccination"
+                "nis-flu"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -78589,9 +78516,9 @@
             "temporal": "October 1, 2024 - no specified end date",
             "modified": "2025-01-31",
             "keyword": [
+                "coronavirus",
                 "covid-19",
-                "hospitalizations",
-                "coronavirus"
+                "hospitalizations"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -80680,10 +80607,10 @@
             "issued": "2023-11-07",
             "@type": "dcat:Dataset",
             "temporal": "2023-2024",
-            "modified": "2024-08-28",
+            "modified": "2025-01-31",
             "keyword": [
-                "covid-19 vaccination",
-                "nis"
+                "nis",
+                "covid-19 vaccination"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
```

### Changes from a03f576 to b8668a8
**Author:** Automated

**Date:** 2025-01-31 18:30:37+00:00

**Message:** Updated data: Fri Jan 31 18:30:37 UTC 2025

```diff
diff --git a/cdc.json b/cdc.json
index f295953..5f81ca8 100644
--- a/cdc.json
+++ b/cdc.json
@@ -46568,9 +46568,9 @@
             "temporal": "2023-2024 & 2024-2025",
             "modified": "2025-01-31",
             "keyword": [
-                "flu vaccination",
                 "nis-ccm",
-                "nis-flu"
+                "nis-flu",
+                "flu vaccination"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -48318,8 +48318,8 @@
             "temporal": "2023-2024 & 2024-2025",
             "modified": "2025-01-31",
             "keyword": [
-                "covid-19 vaccination",
-                "nis-ccm"
+                "nis-ccm",
+                "covid-19 vaccination"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -54492,8 +54492,8 @@
             "temporal": "2023-2024 & 2024-2025",
             "modified": "2025-01-31",
             "keyword": [
-                "covid-19 vaccination",
-                "nis-ccm"
+                "nis-ccm",
+                "covid-19 vaccination"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -55184,6 +55184,80 @@
             ],
             "accrualPeriodicity": "No longer updated (dataset archived)"
         },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2025-01-31",
+            "@type": "dcat:Dataset",
+            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
+            "modified": "2025-01-31",
+            "references": [
+                "Vaccine Safety Datalink"
+            ],
+            "keyword": [
+                "influenza",
+                "flu",
+                "nis",
+                "nis-flu",
+                "children",
+                "vaccine coverage"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
+            },
+            "identifier": "https://data.cdc.gov/api/views/nkr7-scx6",
+            "description": "Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Pregnant Women 18-49 years\n\n\u2022 These monthly flu vaccination coverage estimates for pregnant women are based on electronic health record (EHR) data from the Vaccine Safety Datalink (VSD), a collaboration between CDC\u2019s Immunization Safety Office and nine integrated health care organizations.\u00a7 This system has been used annually to estimate vaccination coverage among pregnant women. COVID-19 vaccination coverage for pregnant women is available here.\n\n\u2022 Figure 3A. Monthly Cumulative Influenza Vaccination Coverage*, by Flu Season and Race/Ethnicity, Pregnant Women 18-49 years, United States, Data Source: Vaccine Safety Datalink\n\n\u2022 Figure 3B. Cumulative Influenza Vaccination Coverage*, by Month, Flu Season, and Race/Ethnicity, Pregnant Women 18-49 years, United States, Data Source: Vaccine Safety Datalink\n\n\u2022 For any month\u2019s coverage estimate, the denominator is the number of women with a pregnancy during the current flu season (defined as August through March) beginning before or during the specified month. The numerator is the subset of the denominator who have received flu vaccination prior to, during, or after pregnancy. The denominator increases as more women are identified as pregnant or having been pregnant during the flu season. Cumulative vaccination coverage for one month may be lower than cumulative coverage for a previous month due to addition to the denominator of women who are less likely to have received vaccination.",
+            "title": "Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Pregnant Women 18-49 years",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nkr7-scx6/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "mediaType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/nkr7-scx6/rows.rdf?accessType=DOWNLOAD",
+                    "describedBy": "https://data.cdc.gov/api/views/nkr7-scx6/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "@type": "dcat:Distribution"
+                },
+                {
+                    "mediaType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/nkr7-scx6/rows.json?accessType=DOWNLOAD",
+                    "describedBy": "https://data.cdc.gov/api/views/nkr7-scx6/columns.json",
+                    "describedByType": "application/json",
+                    "@type": "dcat:Distribution"
+                },
+                {
+                    "mediaType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/nkr7-scx6/rows.xml?accessType=DOWNLOAD",
+                    "describedBy": "https://data.cdc.gov/api/views/nkr7-scx6/columns.xml",
+                    "describedByType": "application/xml",
+                    "@type": "dcat:Distribution"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Vaccinations"
+            ],
+            "language": [
+                "English"
+            ]
+        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/nkri-ptxd",
@@ -55953,78 +56027,6 @@
                 "500 Cities & Places"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "http://www.cdc.gov/nccdphp/DNPAO"
-            ],
-            "keyword": [
-                "body mass index (bmi)",
-                "built environment",
-                "farm",
-                "fruits and vegetables",
-                "nutrition",
-                "obesity",
-                "physical activity",
-                "physical activity education",
-                "transportation",
-                "zoning"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DNPAO Public Inquiries",
-                "hasEmail": "mailto:dnpaoinfo@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/nxst-x9p4",
-            "description": "This dataset contains policy data for 50 US states and DC from 2001 to 2017. Data include information related to state legislation and regulations on nutrition, physical activity, and obesity in settings such as early care and education centers, restaurants, schools, work places, and others. To identify individual bills, use the identifier ProvisionID.  A bill or citation may appear more than once because it could apply to multiple health or policy topics, settings, or states. As of Q 2 2016, data include only enacted legislation.",
-            "title": "CDC Nutrition, Physical Activity, and Obesity - Legislation",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/nxst-x9p4/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/nxst-x9p4/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/nxst-x9p4/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/nxst-x9p4/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/nxst-x9p4/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/nxst-x9p4/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/nxst-x9p4/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/CDC-Nutrition-Physical-Activity-and-Obesity-Legisl/nxst-x9p4",
-            "theme": [
-                "Nutrition, Physical Activity, and Obesity"
-            ]
-        },
         {
             "accessLevel": "restricted public",
             "landingPage": "https://www.cdc.gov/nchs/data-linkage/va-restricted.htm",
@@ -72826,9 +72828,9 @@
             "temporal": "2023-2024 & 2024-2025",
             "modified": "2025-01-31",
             "keyword": [
-                "flu vaccination",
                 "nis-ccm",
-                "nis-flu"
+                "nis-flu",
+                "flu vaccination"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
```

### Changes from 0445c5a to a03f576
**Author:** Automated

**Date:** 2025-01-31 18:11:13+00:00

**Message:** Updated data: Fri Jan 31 18:11:13 UTC 2025

```diff
diff --git a/cdc.json b/cdc.json
index 398eed2..f295953 100644
--- a/cdc.json
+++ b/cdc.json
@@ -9110,15 +9110,15 @@
             "temporal": "2023-2024 respiratory virus season",
             "modified": "2025-01-31",
             "keyword": [
-                "coronavirus",
+                "ncird",
+                "rsv",
                 "covid19",
+                "coronavirus",
+                "vaccination",
                 "immunization",
-                "ncird",
                 "nis-acm",
                 "nis-ccm",
                 "respiratory-virus-response",
-                "rsv",
-                "vaccination",
                 "vaccination-coverage"
             ],
             "contactPoint": {
@@ -21517,7 +21517,7 @@
             "landingPage": "https://data.cdc.gov/d/9xt5-u42s",
             "issued": "2024-02-16",
             "@type": "dcat:Dataset",
-            "modified": "2024-12-23",
+            "modified": "2025-01-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
@@ -36650,80 +36650,6 @@
                 "NNDSS"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2022-09-30",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
-            "modified": "2024-05-03",
-            "references": [
-                "Vaccine Safety Datalink"
-            ],
-            "keyword": [
-                "children",
-                "flu",
-                "influenza",
-                "nis",
-                "nis-flu",
-                "vaccine coverage"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Vax Views",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/fz77-au2z",
-            "description": "Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Pregnant Persons 18-49 years\n\t\n\u2022  These monthly flu vaccination coverage estimates for pregnant persons are based on electronic health record (EHR) data from the Vaccine Safety Datalink (VSD), a collaboration between CDC\u2019s Immunization Safety Office and nine integrated health care organizations.\u00a7 This system has been used annually to estimate vaccination coverage among pregnant persons. COVID-19 vaccination coverage for pregnant persons is available here. \n\n\u2022\tFigure 3A. Monthly Cumulative Influenza Vaccination Coverage*, by Flu Season and Race/Ethnicity, Pregnant Persons 18-49 years, United States, Data Source: Vaccine Safety Datalink \n\n\u2022\tFigure 3B. Cumulative Influenza Vaccination Coverage*, by Month, Flu Season, and Race/Ethnicity, Pregnant Persons 18-49 years, United States, Data Source: Vaccine Safety Datalink \n\n\u2022\tFor any month\u2019s coverage estimate, the denominator is the number of persons with a pregnancy during the current flu season (defined as August through March) beginning before or during the specified month. The numerator is the subset of the denominator who have received flu vaccination prior to, during, or after pregnancy. The denominator increases as more persons are identified as pregnant or having been pregnant during the flu season. Cumulative vaccination coverage for one month may be lower than cumulative coverage for a previous month due to addition to the denominator of persons who are less likely to have received vaccination.",
-            "title": "Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Pregnant Persons 18-49 years",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/fz77-au2z/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fz77-au2z/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/fz77-au2z/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fz77-au2z/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/fz77-au2z/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fz77-au2z/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/fz77-au2z/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
-            "theme": [
-                "Vaccinations"
-            ],
-            "language": [
-                "English"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "https://data.cdc.gov/d/fztq-uwup",
@@ -63226,23 +63152,23 @@
             "issued": "2024-12-19",
             "@type": "dcat:Dataset",
             "temporal": "N/A",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "references": [
                 "NHSN Hospital Respiratory Data (HRD) Reporting: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html  NHSN Hospital Respiratory Data (HRD) Dashboard: https://wwwdev.cdc.gov/nhsn/psc/hospital-respiratory-dashboard.html#anchor_83745  Centers for Medicare and Medicaid Services (CMS) requirements: Updates to the Condition of Participation (CoP) Requirements for Hospitals and Critical Access Hospitals (CAHs) To Report Acute Respiratory Illnesses."
             ],
             "keyword": [
-                "admissions",
-                "coronavirus",
                 "covid-19",
-                "hospital capacity",
+                "influenza",
+                "respiratory syncytial virus",
+                "rsv",
+                "admissions",
                 "hospitalizations",
+                "hospital capacity",
                 "hospital occupancy",
-                "icu beds",
-                "influenza",
                 "inpatient beds",
-                "respiratory",
-                "respiratory syncytial virus",
-                "rsv"
+                "icu beds",
+                "coronavirus",
+                "respiratory"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
```

### Changes from 4d47585 to 0445c5a
**Author:** Automated

**Date:** 2025-01-31 17:10:16+00:00

**Message:** Updated data: Fri Jan 31 17:10:16 UTC 2025

```diff
diff --git a/cdc.json b/cdc.json
index a6c0989..398eed2 100644
--- a/cdc.json
+++ b/cdc.json
@@ -5574,24 +5574,24 @@
             "issued": "2024-02-27",
             "@type": "dcat:Dataset",
             "temporal": "2019-2023",
-            "modified": "2024-08-12",
+            "modified": "2025-01-31",
             "references": [
                 "https://www.cdc.gov/nchs/data/nhis/SHS_Tech_Notes.pdf"
             ],
             "keyword": [
+                "summary health statistics",
                 "nhis",
-                "sdoh-access-to-health-care",
+                "sdoh-poverty-income",
                 "sdoh-employment",
-                "sdoh-food-access",
                 "sdoh-food-insecurity",
-                "sdoh-higher-education",
-                "sdoh-high-school",
                 "sdoh-housing-stability",
-                "sdoh-poverty-income",
+                "sdoh-high-school",
+                "sdoh-higher-education",
+                "sdoh-access-to-health-care",
                 "sdoh-source-of-health-care",
                 "sdoh-use-of-health-care",
-                "sdoh-workplace",
-                "summary health statistics"
+                "sdoh-food-access",
+                "sdoh-workplace"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -38442,23 +38442,23 @@
             "issued": "2024-04-08",
             "@type": "dcat:Dataset",
             "temporal": "2019-2023",
-            "modified": "2024-12-05",
+            "modified": "2025-01-31",
             "references": [
                 "https://wwwn.cdc.gov/NHISDataQueryTool/SHS_adult/SHS_Tech_Notes.pdf"
             ],
             "keyword": [
+                "summary health statistics",
                 "nhis",
-                "sdoh-access-to-health-care",
+                "sdoh-poverty-income",
                 "sdoh-employment",
-                "sdoh-food-access",
                 "sdoh-food-insecurity",
-                "sdoh-higher-education",
                 "sdoh-housing-stability",
-                "sdoh-poverty-income",
+                "sdoh-higher-education",
+                "sdoh-access-to-health-care",
                 "sdoh-source-of-health-care",
                 "sdoh-use-of-health-care",
-                "sdoh-workplace",
-                "summary health statistics"
+                "sdoh-food-access",
+                "sdoh-workplace"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -66557,14 +66557,14 @@
             "issued": "2024-10-04",
             "@type": "dcat:Dataset",
             "temporal": "October 1, 2024 - no specified end date",
-            "modified": "2025-01-17",
+            "modified": "2025-01-31",
             "keyword": [
-                "deaths",
-                "disease burden",
+                "rsv",
                 "hospitalizations",
-                "outpatient visits",
                 "respiratory syncytial virus",
-                "rsv"
+                "outpatient visits",
+                "deaths",
+                "disease burden"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -69570,23 +69570,23 @@
             "issued": "2024-12-19",
             "@type": "dcat:Dataset",
             "temporal": "N/A",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "references": [
                 "NHSN Hospital Respiratory Data (HRD) Reporting: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html  NHSN Hospital Respiratory Data (HRD) Dashboard: https://wwwdev.cdc.gov/nhsn/psc/hospital-respiratory-dashboard.html#anchor_83745  Centers for Medicare and Medicaid Services (CMS) requirements: Updates to the Condition of Participation (CoP) Requirements for Hospitals and Critical Access Hospitals (CAHs) To Report Acute Respiratory Illnesses."
             ],
             "keyword": [
-                "admissions",
-                "coronavirus",
                 "covid-19",
-                "hospital capacity",
+                "influenza",
+                "respiratory syncytial virus",
+                "rsv",
+                "admissions",
                 "hospitalizations",
+                "hospital capacity",
                 "hospital occupancy",
-                "icu beds",
-                "influenza",
                 "inpatient beds",
-                "respiratory",
-                "respiratory syncytial virus",
-                "rsv"
+                "icu beds",
+                "coronavirus",
+                "respiratory"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
```

### Changes from 81df1a4 to 4d47585
**Author:** Automated

**Date:** 2025-01-31 17:07:36+00:00

**Message:** Updated data: Fri Jan 31 17:07:36 UTC 2025

```diff
diff --git a/cdc.json b/cdc.json
index dcc4584..a6c0989 100644
--- a/cdc.json
+++ b/cdc.json
@@ -6261,12 +6261,12 @@
             "temporal": "2023-2024, 2024-2025",
             "modified": "2025-01-31",
             "keyword": [
+                "flu vaccination",
+                "iis",
                 "iqvia",
                 "nis-acm",
-                "vsd",
-                "iis",
                 "nis-flu",
-                "flu vaccination"
+                "vsd"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -7408,11 +7408,11 @@
             "@type": "dcat:Dataset",
             "modified": "2025-01-31",
             "keyword": [
-                "tobacco",
-                "osh",
-                "gtss",
+                "adult",
                 "gats",
-                "adult"
+                "gtss",
+                "osh",
+                "tobacco"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -8776,12 +8776,12 @@
             "@type": "dcat:Dataset",
             "modified": "2025-01-31",
             "keyword": [
-                "tobacco",
-                "osh",
+                "global",
                 "gtss",
                 "gyts",
-                "youth",
-                "global"
+                "osh",
+                "tobacco",
+                "youth"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -23047,15 +23047,15 @@
             "issued": "2024-10-04",
             "@type": "dcat:Dataset",
             "temporal": "October 1, 2024 - no specified end date",
-            "modified": "2025-01-17",
+            "modified": "2025-01-31",
             "keyword": [
-                "coronavirus",
                 "covid-19",
-                "deaths",
-                "disease burden",
                 "hospitalizations",
+                "coronavirus",
+                "deaths",
                 "illnesses",
-                "outpatient visits"
+                "outpatient visits",
+                "disease burden"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -34085,48 +34085,6 @@
                 "Environmental Health & Toxicology"
             ]
         },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/epap-ayij",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-10-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-16",
-            "keyword": [
-                "care cascade",
-                "cascade of care",
-                "latent tuberculosis infection (ltbi)",
-                "tuberculosis (tb)"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Tuberculosis Epidemiologic Studies Consortium",
-                "hasEmail": "mailto:tbesc3@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDC"
-            },
-            "identifier": "https://data.cdc.gov/api/views/epap-ayij",
-            "description": "This study focused on describing and quantifying the steps in the tuberculosis (TB) prevention cascade of care within health department clinics. This included better understanding the proportions of patients with latent TB infection who are identified, offered treatment, accept treatment, and complete treatment.",
-            "title": "Tuberculosis Epidemiologic Studies Consortium (TBESC)-II Part B: Strengthening Public Health Surveillance for Latent Tuberculosis Infection",
-            "programCode": [
-                "009:027"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/download/epap-ayij/application/x-zip-compressed",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "theme": [
-                "National Center for HIV, Viral Hepatitis, STD, and TB Prevention"
-            ]
-        },
         {
             "accessLevel": "public",
             "landingPage": "http://www.cdc.gov/nccdphp/dph/",
@@ -41736,11 +41694,11 @@
             "issued": "2024-10-04",
             "@type": "dcat:Dataset",
             "temporal": "October 1, 2024 - no specified end date",
-            "modified": "2025-01-17",
+            "modified": "2025-01-31",
             "keyword": [
+                "rsv",
                 "hospitalizations",
-                "respiratory syncytial virus",
-                "rsv"
+                "respiratory syncytial virus"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -46549,12 +46507,12 @@
             "@type": "dcat:Dataset",
             "modified": "2025-01-31",
             "keyword": [
-                "sars-cov-2",
                 "covid-19",
+                "nowcasting",
+                "sars-cov-2",
                 "surveillance",
-                "variant surveillance",
                 "variant proportion",
-                "nowcasting"
+                "variant surveillance"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -47417,12 +47375,12 @@
             "temporal": "2024-2025",
             "modified": "2025-01-31",
             "keyword": [
-                "nis-acm",
-                "vsd",
                 "iis",
                 "iqvia",
+                "nis-acm",
                 "nis-flu",
-                "rsv vaccination"
+                "rsv vaccination",
+                "vsd"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -50149,12 +50107,12 @@
             "temporal": "2024-2025",
             "modified": "2025-01-31",
             "keyword": [
-                "nis-acm",
-                "vsd",
+                "covid-19 vaccination",
                 "iis",
                 "iqvia",
+                "nis-acm",
                 "nis-flu",
-                "covid-19 vaccination"
+                "vsd"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -54799,12 +54757,12 @@
             "temporal": "2024-2025",
             "modified": "2025-01-31",
             "keyword": [
-                "nis-acm",
                 "iis",
                 "iqvia",
-                "vsd",
+                "nis-acm",
                 "nis-flu",
-                "rsv vaccination"
+                "rsv vaccination",
+                "vsd"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -58377,11 +58335,11 @@
             "temporal": "2023-24 & 2024-25",
             "modified": "2025-01-31",
             "keyword": [
-                "covid-19 vaccination",
+                "nis-acm",
+                "vsd",
                 "iis",
                 "iqvia",
-                "nis-acm",
-                "vsd"
+                "covid-19 vaccination"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -66803,12 +66761,12 @@
             "temporal": "2024-2025",
             "modified": "2025-01-31",
             "keyword": [
-                "nis-acm",
-                "iqvia",
+                "flu vaccination",
                 "iis",
-                "vsd",
+                "iqvia",
+                "nis-acm",
                 "nis-flu",
-                "flu vaccination"
+                "vsd"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -77052,11 +77010,11 @@
             "@type": "dcat:Dataset",
             "modified": "2025-01-31",
             "keyword": [
-                "tobacco",
-                "osh",
-                "gtss",
                 "ghpss",
-                "students"
+                "gtss",
+                "osh",
+                "students",
+                "tobacco"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
@@ -78701,11 +78659,11 @@
             "issued": "2024-09-23",
             "@type": "dcat:Dataset",
             "temporal": "October 1, 2024 - no specified end date",
-            "modified": "2025-01-17",
+            "modified": "2025-01-31",
             "keyword": [
-                "coronavirus",
                 "covid-19",
-                "hospitalizations"
+                "hospitalizations",
+                "coronavirus"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
```

