# Change History for healthdata.json (Part 4)

### Changes from 31606f9 to dd2190f (Part 3/11)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2010-nid13541",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -27829,41 +27842,54 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2010",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2010-nid13541",
-            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and<br />\nhashish, heroin, nonprescription methadone, other opiates and<br />\nsynthetics, PCP, other hallucinogens, methamphetamine, other amphetamines,<br />\nother stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2010)",
-            "programCode": [
-                "009:030"
+            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2010)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "Final counts of deaths by the month the deaths occurred and by select causes of death for 2014-2019.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2010-nid13541",
-                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2010) \n",
                     "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2010-nid13541"
-                }
-            ]
+                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
                 },
                 {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
-            "bureauCode": [
-                "009:20"
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bxq8-mugm",
             "issued": "2021-02-03",
-            "@type": "dcat:Dataset",
-            "temporal": "2014/2019",
-            "modified": "2022-04-04",
             "keyword": [
                 "all causes",
                 "alzheimer disease",
@@ -27891,89 +27917,44 @@
                 "unintentional injuries",
                 "united states"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/bxq8-mugm",
-            "description": "Final counts of deaths by the month the deaths occurred and by select causes of death for 2014-2019.",
-            "title": "Monthly Counts of Deaths by Select Causes, 2014-2019",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-04",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Monthly Counts of Deaths by Select Causes, 2014-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/quality-of-care/nursing-home-affiliated-entity-performance-measures",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-06-29",
-            "temporal": "2023-06-01/2024-11-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-11",
-            "references": [
-                "https://data.cms.gov/resources/nursing-home-affiliated-entity-performance-measures-methodology"
-            ],
-            "keyword": [
-                "hospitals & facilities",
-                "medicare",
-                "skilled nursing"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NH_Affiliation_Inquiries - CCSQ",
                 "hasEmail": "mailto:NH_Affiliation_Inquiries@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/97ecfad1-d3f1-4d42-b774-d74661d830bc/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/nursing-home-affiliated-entity-performance-measures-data-dictionary",
             "description": "The Nursing Home Affiliated Entity Performance Measures dataset provides select quality and performance measures from Care Compare\u00a0for groups of nursing homes that share common individual or organizational owners, officers, or entities with operational/managerial control. The data include measures such as average health and staffing star ratings, staffing measures, average quality star ratings, select enforcement remedies, claims-based and Minimum Data Set (MDS) measures, average Skilled Nursing Facility Quality Reporting Program (SNF QRP) metrics, and COVID-19 vaccination rates.",
-            "title": "Nursing Home Affiliated Entity Performance Measures",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/97ecfad1-d3f1-4d42-b774-d74661d830bc/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/97ecfad1-d3f1-4d42-b774-d74661d830bc/data",
+                    "mediaType": "text/html",
                     "title": "Nursing Home Affiliated Entity Performance Measures : 2024-11-01"
                 },
                 {
@@ -28181,44 +28162,48 @@
                     "title": "Nursing Home Affiliated Entity Performance Measures : 2023-06-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/nursing-home-affiliated-entity-performance-measures-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/97ecfad1-d3f1-4d42-b774-d74661d830bc/data-viewer",
+            "issued": "2023-06-29",
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "skilled nursing"
+            ],
+            "landingPage": "https://data.cms.gov/quality-of-care/nursing-home-affiliated-entity-performance-measures",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2024-12-11",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/nursing-home-affiliated-entity-performance-measures-methodology"
+            ],
+            "temporal": "2023-06-01/2024-11-30",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nursing Home Affiliated Entity Performance Measures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7s5z-v32b",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-15",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "bd782837-31ac-41ae-9569-52182bc038e9",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-11-06-to-2023-11-12",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28227,33 +28212,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-11-06-to-2023-11-12"
                 }
             ],
+            "identifier": "bd782837-31ac-41ae-9569-52182bc038e9",
+            "issued": "2023-11-15",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/7s5z-v32b",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-11-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-11-06-to-2023-11-12"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/y93j-qcuq",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -28261,40 +28248,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/y93j-qcuq",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/y93j-qcuq",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://healthdata.gov/d/7ssb-cv9j",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-09-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-11",
-            "keyword": [
-                "core sets",
-                "performance rates",
-                "quality measures"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "a058ef78-e18b-4435-94aa-b70ab6ce5904",
             "description": "Performance rates on frequently reported health care quality measures in the CMS Medicaid/CHIP Child and Adult Core Sets, for FFY 2021 reporting.\r\n\r\nSource: Mathematica analysis of MACPro and Form CMS-416 reports for the FFY 2021 reporting cycle. Dataset revised September 2023. For more information, see the Children's Health Care Quality Measures and Adult Health Care Quality Measures webpages.",
-            "title": "2021 Child and Adult Health Care Quality Measures Quality",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28302,45 +28285,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "a058ef78-e18b-4435-94aa-b70ab6ce5904",
+            "issued": "2023-09-13",
+            "keyword": [
+                "core sets",
+                "performance rates",
+                "quality measures"
+            ],
+            "landingPage": "https://healthdata.gov/d/7ssb-cv9j",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-09-11",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Quality"
-            ]
+            ],
+            "title": "2021 Child and Adult Health Care Quality Measures Quality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://blast.ncbi.nlm.nih.gov/Blast.cgi",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2012-08-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "api",
-                "biochemistry",
-                "biotechnology",
-                "computational biology",
-                "dataset",
-                "protein",
-                "tools & utilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/qn84-sbuf",
             "description": "BLAST (Basic Local Alignment Search Tool) finds regions of similarity between biological sequences. \n\nBLAST includes several specialized search interfaces: SmartBLAST, Primer-BLAST, Global Align, CD-Search, IgBLAST, VecScreen, CDART, Multiple Alignment, MOLE-BLAST, Searches at a Cloud Provider, BLAST+ Docker Image",
-            "title": "BLAST (Basic Local Alignment Search Tool)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28361,47 +28339,44 @@
                     "title": "BLAST API"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/qn84-sbuf",
+            "issued": "2012-08-22",
+            "keyword": [
+                "api",
+                "biochemistry",
+                "biotechnology",
+                "computational biology",
+                "dataset",
+                "protein",
+                "tools & utilities"
+            ],
+            "landingPage": "http://blast.ncbi.nlm.nih.gov/Blast.cgi",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-04",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Molecular biology/Genetics"
-            ]
+            ],
+            "title": "BLAST (Basic Local Alignment Search Tool)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/gz3p-wzwf",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "anaplasma phagocytophilum",
-                "ehrlichia chaffeensis",
-                "ehrlichiosis and anaplasmosis",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "undetermined",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/gz3p-wzwf",
             "description": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. \r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n *Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Please refer to the MMWR publication for weekly updates to the footnote for this condition.",
-            "title": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28424,39 +28399,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/gz3p-wzwf",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "anaplasma phagocytophilum",
+                "ehrlichia chaffeensis",
+                "ehrlichiosis and anaplasmosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "undetermined",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/gz3p-wzwf",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-01-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfAdvisory/search.cfm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "temporal": "2001-01-01/2009-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2009-12-31",
-            "keyword": [
-                "labeling"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "a76c0c50-76f5-42bc-911c-703287648b52",
             "description": "This database contains historical information about CDRH Advisory Committees and Panel meetings through 2008, including summaries and transcripts.",
-            "title": "CDRH Advisory Meeting Materials Archive",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28464,51 +28447,46 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "a76c0c50-76f5-42bc-911c-703287648b52",
+            "issued": "2021-02-25",
+            "keyword": [
+                "labeling"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfAdvisory/search.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2009-12-31",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "temporal": "2001-01-01/2009-12-31",
+            "title": "CDRH Advisory Meeting Materials Archive"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/skilled-nursing-facility-all-owners",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-09-27",
-            "temporal": "2022-09-01/2025-01-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-12/1ea55414-f441-4694-a13c-6400d4e28ef6/SNF_Data_Guidance.pdf"
-            ],
-            "keyword": [
-                "hospitals & facilities",
-                "medicare",
-                "medicare advantage",
-                "original medicare",
-                "provider enrollment",
-                "skilled nursing"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/afe44b85-cc6d-40d7-b5df-00ae8910d1d2/data-viewer",
-            "description": "The Skilled Nursing Facility (SNF) All Owners dataset provides information on all owners of SNFs currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.\n\n\u00a0\n\nOn November 17, 2023, CMS published in the Federal Register a final rule titled, \u201cMedicare and Medicaid Programs; Disclosures of Ownership and Additional Disclosable Parties Information for Skilled Nursing Facilities and Nursing Facilities; Medicare Providers\u2019 and Suppliers\u2019 Disclosure of Private Equity Companies and Real Estate Investment Trusts\u201d (88 FR 80141). This final rule implements parts of section 1124(c) of the Act which requires SNFs to disclose detailed information about their ownership and management as well as additional data regarding: (1) other parties with which the SNF is associated; and (2) the ownership structures of these other parties.\u00a0 Refer to Medicare Enrollment for Providers & Suppliers for more information on the Skilled Nursing Facility disclosure requirements. \n\n\u00a0Section 6101(b) of the Affordable Care Act states that no later than 1 year after final regulations promulgated under section 1124(c) of the Act are published in the\u00a0Federal Register, the Secretary shall make the information reported available to the public.\n\n\u00a0On November 21, 2024 CMS updated this dataset to include this reported information.",
-            "title": "Skilled Nursing Facility All Owners",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-12/7a976b38-70d9-4332-a913-446c89641840/SNF_All_Owners_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Skilled Nursing Facility (SNF) All Owners dataset provides information on all owners of SNFs currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.\n\n\u00a0\n\nOn November 17, 2023, CMS published in the Federal Register a final rule titled, \u201cMedicare and Medicaid Programs; Disclosures of Ownership and Additional Disclosable Parties Information for Skilled Nursing Facilities and Nursing Facilities; Medicare Providers\u2019 and Suppliers\u2019 Disclosure of Private Equity Companies and Real Estate Investment Trusts\u201d (88 FR 80141). This final rule implements parts of section 1124(c) of the Act which requires SNFs to disclose detailed information about their ownership and management as well as additional data regarding: (1) other parties with which the SNF is associated; and (2) the ownership structures of these other parties.\u00a0 Refer to Medicare Enrollment for Providers & Suppliers for more information on the Skilled Nursing Facility disclosure requirements. \n\n\u00a0Section 6101(b) of the Affordable Care Act states that no later than 1 year after final regulations promulgated under section 1124(c) of the Act are published in the\u00a0Federal Register, the Secretary shall make the information reported available to the public.\n\n\u00a0On November 21, 2024 CMS updated this dataset to include this reported information.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/afe44b85-cc6d-40d7-b5df-00ae8910d1d2/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/afe44b85-cc6d-40d7-b5df-00ae8910d1d2/data",
+                    "mediaType": "text/html",
                     "title": "Skilled Nursing Facility All Owners : 2025-01-01"
                 },
                 {
@@ -28848,52 +28826,50 @@
                     "title": "Skilled Nursing Facility All Owners : 2022-09-20"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-12/7a976b38-70d9-4332-a913-446c89641840/SNF_All_Owners_Data_Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/afe44b85-cc6d-40d7-b5df-00ae8910d1d2/data-viewer",
+            "issued": "2022-09-27",
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment",
+                "skilled nursing"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/skilled-nursing-facility-all-owners",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-12/1ea55414-f441-4694-a13c-6400d4e28ef6/SNF_Data_Guidance.pdf"
+            ],
+            "temporal": "2022-09-01/2025-01-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Skilled Nursing Facility All Owners"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/2i8i-dz8i",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "crimean-congo hemorrhagic fever virus",
-                "ebola virus",
-                "guanarito virus",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/2i8i-dz8i",
             "description": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers'. NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
-            "title": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28916,44 +28892,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/2i8i-dz8i",
+            "issued": "2019-04-23",
+            "keyword": [
+                "2019",
+                "crimean-congo hemorrhagic fever virus",
+                "ebola virus",
+                "guanarito virus",
+                "nedss",
+                "netss",
+                "nndss",
+                "viral hemorrhagic fevers",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/2i8i-dz8i",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2020-01-02",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ht29-hwxw",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ht29-hwxw",
             "description": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome  - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28976,58 +28954,89 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "theme": [
-                "NNDSS"
-            ]
+            "identifier": "https://data.cdc.gov/api/views/ht29-hwxw",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "rubella",
+                "rubella congenital syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ht29-hwxw",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "theme": [
+                "NNDSS"
+            ],
+            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://ndar.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "autism",
-                "autism spectrum disorder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Farber, Greg",
                 "hasEmail": "mailto:farberg@mail.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "47fd0b8c-191e-4395-8cd1-823c18ce8689",
+            "dataQuality": true,
             "description": "<p>National Database for Autism Research (NDAR) is an extensible, scalable informatics platform for autism spectrum disorder-relevant data at all levels of biological and behavioral organization (molecules, genes, neural tissue, behavioral, social and environmental interactions) and for all data types (text, numeric, image, time series, etc.). NDAR was developed to share data across the entire ASD field and to facilitate collaboration across laboratories, as well as interconnectivity with other informatics platforms.</p>\n\n<p> NDAR Homepage: http://ndar.nih.gov/</p>",
-            "title": "National Database for Autism Research (NDAR)",
+            "identifier": "47fd0b8c-191e-4395-8cd1-823c18ce8689",
+            "issued": "2016-07-17",
+            "keyword": [
+                "autism",
+                "autism spectrum disorder"
+            ],
+            "landingPage": "http://ndar.nih.gov/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:060"
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "National Database for Autism Research (NDAR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/centers-medicare-medicaid-services-cms-ehr-incentive-program-measures",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2017-08-01",
-            "references": [
-                "https://www.healthit.gov/data/quickstats/office-based-health-care-professionals-participating-cms-ehr-incentive-programs",
-                "https://www.healthit.gov/data/quickstats/hospitals-participating-cms-ehr-incentive-programs"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/centers-medicare-medicaid-services-cms-ehr-incentive-program-measures",
+            "description": "The CMS EHR Incentive Programs provide incentives to eligible office-based providers and hospitals to adopt electronic health records. Both the Medicare and Medicaid programs have separate criteria and eligible participants. These measures track the percentage of physicians, nurse practitioners, physician assistants, short-term general, Critical Access, and Children's hospitals that have demonstrated meaningul use of certified electronic health record technology and/or adopted, implemented, or ugraded any electronic health record. These measures track the rate of adoption and use of EHR technology certified by HHS in addition to adoption of other non-certified EHR technology. These measures are cumulative, representing the most recent data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/Meaningful-Use-Acceleration-Scorecard.csv",
+                    "mediaType": "text/csv",
+                    "title": "Meaningful-Use-Acceleration-Scorecard.csv"
+                }
             ],
+            "identifier": "deraq33a-rn2x-aa1j-jhzz-4gp7d0wf8cys",
+            "issued": "2023-10-03",
             "keyword": [
                 "adoption",
                 "certified electronic health record technology",
@@ -29041,55 +29050,33 @@
                 "office-based physicians",
                 "physicians"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/centers-medicare-medicaid-services-cms-ehr-incentive-program-measures",
+            "modified": "2017-08-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "deraq33a-rn2x-aa1j-jhzz-4gp7d0wf8cys",
-            "description": "The CMS EHR Incentive Programs provide incentives to eligible office-based providers and hospitals to adopt electronic health records. Both the Medicare and Medicaid programs have separate criteria and eligible participants. These measures track the percentage of physicians, nurse practitioners, physician assistants, short-term general, Critical Access, and Children's hospitals that have demonstrated meaningul use of certified electronic health record technology and/or adopted, implemented, or ugraded any electronic health record. These measures track the rate of adoption and use of EHR technology certified by HHS in addition to adoption of other non-certified EHR technology. These measures are cumulative, representing the most recent data.",
-            "title": "Centers for Medicare &amp; Medicaid Services (CMS) EHR Incentive Program Measures",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/Meaningful-Use-Acceleration-Scorecard.csv",
-                    "mediaType": "text/csv",
-                    "title": "Meaningful-Use-Acceleration-Scorecard.csv"
-                }
+            "references": [
+                "https://www.healthit.gov/data/quickstats/office-based-health-care-professionals-participating-cms-ehr-incentive-programs",
+                "https://www.healthit.gov/data/quickstats/hospitals-participating-cms-ehr-incentive-programs"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/centers-medicare-medicaid-services-cms-ehr-incentive-program-measures"
+            "title": "Centers for Medicare &amp; Medicaid Services (CMS) EHR Incentive Program Measures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/2juy-3evq",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-12-27",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-03",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division (HELD), National Institute for Occupational Safety and Health (NIOSH)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/2juy-3evq",
             "description": "Inhalation exposure to respirable crystalline silica (RCS) during fabrication of engineered stone-based kitchen countertops has been on the rise in recent years and has become a significant occupational health problem in the United States and globally. Little is known about the presence of nano-crystalline silica (NCS), i.e., particles below 100 nm. We present a methodology to quantify the crystalline silica content in the sub-100 nm size fraction of the aerosol released during engineered stone fabrication using X-ray diffraction (XRD) and Fourier transform Infrared (FT-IR) spectroscopy. Aerosol was generated in test chamber designed per EN 1093-3 and sampled using cascade impactors. XRD and FT-IR analysis showed the presence of both \u03b1-quartz (15 \u2013 60 %) and cristobalite (10 \u2013 50 %) polymorphs in all size fractions. With increasing particle size, the cristobalite content increased. 70 % of the total aerosol mass in the sub-100 nm fraction was found to be crystalline silica, qualitatively confirmed by electron diffraction and electron energy loss spectroscopy. Presence of other minerals was detected in all size fractions; no polymeric resin binder was detected in the sub-100 nm fraction. Although, the sub-100 nm fraction was about 1 % of the aerosol mass, it accounted for 4 \u2013 24 % of the aerosol surface area based on total lung deposition. If the surface area is a more relevant exposure metric, the assessment of efficacy of current engineering control systems using mass as an exposure metric may not provide adequate protection.",
-            "title": "Release of Crystalline Silica Nanoparticles During Engineered Stone Fabrication",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29097,41 +29084,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/2juy-3evq",
+            "issued": "2024-12-27",
+            "landingPage": "https://data.cdc.gov/d/2juy-3evq",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-03",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Release of Crystalline Silica Nanoparticles During Engineered Stone Fabrication"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5ekf-pmct",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-08-02",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "adults",
-                "brfss",
-                "health care coverage",
-                "heath care access"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5ekf-pmct",
             "description": "The 2011 BRFSS data reflects a change in weighting methodology (raking) and the addition of cell phone only respondents. Shifts in observed prevalence from 2010 to 2011 for BRFSS measures will likely reflect the new methods of measuring risk factors, rather than true trends in risk-factor prevalence. A break in trend lines after 2010 is used to reflect this change in methodolgy. Percentages are weighted to population characteristics. Data are not available if it did not meet BRFSS stability requirements. For more information on these requirements, as well as risk factors and calculated variables, see the Technical Documents and Survey Data for a specific year - http://www.cdc.gov/brfss/annual_data/annual_data.htm. Recommended citation: Centers for Disease Control and Prevention (CDC). Behavioral Risk Factor Surveillance System. Atlanta, Georgia: U.S. Department of Health and Human Services, Centers for Disease Control and Prevention, [appropriate year].",
-            "title": "BRFSS Prevalence And Trends Data: Health Care Access/Coverage for 2011",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29154,86 +29135,88 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5ekf-pmct",
+            "issued": "2013-08-02",
+            "keyword": [
+                "adults",
+                "brfss",
+                "health care coverage",
+                "heath care access"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5ekf-pmct",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2015-08-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Health Statistics"
-            ]
+            ],
+            "title": "BRFSS Prevalence And Trends Data: Health Care Access/Coverage for 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7vz3-rzuw",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "68786904-807e-57d8-93f2-a0c7bdc70e2c",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt pillar v2.10.23 (coreset-prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.23/20241029/pillar.csv",
-                    "description": "CoreSEt pillar v2.10.23 (coreset-prod)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt pillar v2.10.23 (coreset-prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.23/20241029/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt pillar v2.10.23 (coreset-prod)"
                 }
             ],
+            "identifier": "68786904-807e-57d8-93f2-a0c7bdc70e2c",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/7vz3-rzuw",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-11-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSEt pillar v2.10.23 (coreset-prod)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7w4j-52y7",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2014-11-07",
-            "temporal": "2013-01-01T00:00:00+00:00/2014-01-01T00:00:00+00:00",
-            "@type": "dcat:Dataset",
-            "modified": "2021-08-23",
-            "keyword": [
-                "drug acquisition cost",
-                "nadac"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "1fe73992-cbfd-5109-97bc-dee8b33fdcff",
             "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
-            "title": "NADAC (National Average Drug Acquisition Cost) 2013",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29242,48 +29225,41 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "1fe73992-cbfd-5109-97bc-dee8b33fdcff",
+            "issued": "2014-11-07",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "landingPage": "https://healthdata.gov/d/7w4j-52y7",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2021-08-23",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "temporal": "2013-01-01T00:00:00+00:00/2014-01-01T00:00:00+00:00",
             "theme": [
                 "National Average Drug Acquisition Cost",
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "NADAC (National Average Drug Acquisition Cost) 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-10-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-04",
-            "references": [
-                "https://www.census.gov/programs-surveys/acs/data.html",
-                "https://www.census.gov/programs-surveys/acs/library/handbooks/general.html"
-            ],
-            "keyword": [
-                "acs",
-                "estimates",
-                "places",
-                "sdoh",
-                "tract"
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
-            "identifier": "https://data.cdc.gov/api/views/e539-uadk",
             "description": "This dataset contains census tract-level social determinants of health (SDOH) measures from the American Community Survey 5-year data for the entire United States\u201450 states and the District of Columbia. Data were downloaded from data.census.gov using Census API and processed by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. These measures complement existing PLACES measures, including PLACES SDOH measures (e.g., health insurance, routine check-up). These data can be used together with PLACES data to identify which health and SDOH issues overlap in a community to help inform public health planning.  \n\nTo access spatial data, please use the ArcGIS Online service:  https://cdcarcgis.maps.arcgis.com/home/item.html?id=d51009ea78b54635be95c6ec9955ec17.",
-            "title": "SDOH Measures for Census Tract, ACS 2017-2021",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29306,41 +29282,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/e539-uadk",
+            "issued": "2023-10-26",
+            "keyword": [
+                "acs",
+                "estimates",
+                "places",
+                "sdoh",
+                "tract"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-12-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.census.gov/programs-surveys/acs/data.html",
+                "https://www.census.gov/programs-surveys/acs/library/handbooks/general.html"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "SDOH Measures for Census Tract, ACS 2017-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-14",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-09-10",
-            "keyword": [
-                "older adults",
-                "rsv",
-                "vaccination"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/55uq-699y",
             "description": "Weekly Cumulative RSV Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged 65 years\n\n\u2022 Estimated COVID-19 vaccination coverage among Medicare fee-for-service beneficiaries >65 years is assessed using data files from the Medicare Fee-For-Service (FFS) administrative claims data managed by the Centers for Medicare & Medicaid Services (CMS). \n\n\u2022 Starting in July 2023, the CDC recommended the RSV vaccine to protect against serious illness from RSV. (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html",
-            "title": "Weekly Cumulative RSV Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States, Data Source: Centers for Medicare & Medicaid Services Chronic Conditions Warehouse",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29363,95 +29345,91 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/55uq-699y",
+            "issued": "2024-02-14",
+            "keyword": [
+                "older adults",
+                "rsv",
+                "vaccination"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2024-09-10",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National",
+            "temporal": "2023-2024",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative RSV Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States, Data Source: Centers for Medicare & Medicaid Services Chronic Conditions Warehouse"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7wic-wdxb",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-06-21",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-08",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "f2845568-e795-5d58-9c4b-a4271c9a8df4",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard version v2.11.16 (cmsdev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/version.csv",
-                    "description": "Scorecard version v2.11.16 (cmsdev)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard version v2.11.16 (cmsdev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/version.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard version v2.11.16 (cmsdev)"
                 }
             ],
+            "identifier": "f2845568-e795-5d58-9c4b-a4271c9a8df4",
+            "issued": "2023-06-21",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/7wic-wdxb",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2025-01-08",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Scorecard version v2.11.16 (cmsdev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7rci-qmm9",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "nedss",
-                "netss",
-                "nndss",
-                "smallpox",
-                "streptococcal toxic shock syndrome",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7rci-qmm9",
             "description": "NNDSS - TABLE 1GG. Smallpox to Streptococcal toxic shock syndrome \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1GG. Smallpox to Streptococcal toxic shock syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29474,267 +29452,266 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7rci-qmm9",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "nedss",
+                "netss",
+                "nndss",
+                "smallpox",
+                "streptococcal toxic shock syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7rci-qmm9",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1GG. Smallpox to Streptococcal toxic shock syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7xdq-w6w8",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-03-12",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-23",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "9ec430cb-fefd-5985-a232-841f9ea55deb",
             "description": "This is a dataset created for use by the Scorecard website, and is not intended for use outside that application.",
-            "title": "Scorecard measure",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/measure.csv",
-                    "description": "Scorecard Example CSV updated at Thu, 23 Mar 2023 16:35:57 by TVZS",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard Example CSV updated at Thu, 23 Mar 2023 16:35:57 by TVZS",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard Example CSV"
                 }
             ],
+            "identifier": "9ec430cb-fefd-5985-a232-841f9ea55deb",
+            "issued": "2023-03-12",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/7xdq-w6w8",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2023-03-23",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Scorecard measure"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7xjb-k6wa",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "ba72705c-3425-5c51-8d17-276fe6d7bafc",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt measure_value v2.10.23 (coreset-prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.23/20241029/measure_value.csv",
-                    "description": "CoreSEt measure_value v2.10.23 (coreset-prod)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt measure_value v2.10.23 (coreset-prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.23/20241029/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt measure_value v2.10.23 (coreset-prod)"
                 }
             ],
+            "identifier": "ba72705c-3425-5c51-8d17-276fe6d7bafc",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/7xjb-k6wa",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-11-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSEt measure_value v2.10.23 (coreset-prod)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/books/about/openaccess/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-07-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "books",
-                "literature",
-                "open access"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/rzrc-ykmq",
             "description": "A subset of the total collection of books and documents in the NLM Literature Archive (NLM LitArch), accessible through the Bookshelf website, are available through the NLM LitArch Open Access subset. Contents in the NLM LitArch Open Access subset generally include works which are in the public domain, works which are available under a Creative Commons or similar license, and works whose authors or publishers have explicitly agreed to the terms of the NLM LitArch Open Access subset. Except for public domain works, works in the NLM LitArch Open Access subset are still protected by copyright, but are made available under a Creative Commons or similar license that generally allows more liberal redistribution and reuse than a traditional copyrighted work. The license terms are not the same for each work. Read the license text which is available with each downloadable file to determine terms of use.",
-            "title": "NLM LitArch Open Access Subset",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/books/about/openaccess/",
-                    "description": "Except for public domain works, works in the NLM LitArch Open Access subset are still protected by copyright, but are made available under a Creative Commons or similar license that generally allows more liberal redistribution and reuse than a traditional copyrighted work. The license terms are not the same for each work. Read the license text which is available with each downloadable file to determine terms of use.",
                     "@type": "dcat:Distribution",
+                    "description": "Except for public domain works, works in the NLM LitArch Open Access subset are still protected by copyright, but are made available under a Creative Commons or similar license that generally allows more liberal redistribution and reuse than a traditional copyrighted work. The license terms are not the same for each work. Read the license text which is available with each downloadable file to determine terms of use.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/books/about/openaccess/",
+                    "mediaType": "text/html",
                     "title": "About the NLM LitArch Open Access Subset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/books/n/about/ftp/",
-                    "description": "The NLM LitArch FTP service is the only service that may be used for automated downloading of content from this open access subset.  Use the FTP service to download the complete sets of files for books and documents in this subset. Each downloadable file typically consists of the following data file types: XML, images, and PDF.",
                     "@type": "dcat:Distribution",
+                    "description": "The NLM LitArch FTP service is the only service that may be used for automated downloading of content from this open access subset.  Use the FTP service to download the complete sets of files for books and documents in this subset. Each downloadable file typically consists of the following data file types: XML, images, and PDF.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/books/n/about/ftp/",
+                    "mediaType": "text/html",
                     "title": "Download NLM LitArch Open Access Subset Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/rzrc-ykmq",
+            "issued": "2022-07-06",
+            "keyword": [
+                "books",
+                "literature",
+                "open access"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/books/about/openaccess/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Literature"
-            ]
+            ],
+            "title": "NLM LitArch Open Access Subset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7yi8-8e5i",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-30",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "4cc85461-9e3a-5914-979d-189492472e18",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard measure_value v2.12.1-test (local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/measure_value.csv",
-                    "description": "Scorecard measure_value v2.12.1-test (local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard measure_value v2.12.1-test (local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard measure_value v2.12.1-test (local)"
                 }
             ],
+            "identifier": "4cc85461-9e3a-5914-979d-189492472e18",
+            "issued": "2023-08-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/7yi8-8e5i",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-30",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Scorecard measure_value v2.12.1-test (local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/cnd2-a6zw",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Joel Ruhter",
+                "hasEmail": "mailto:joel.ruhter@hhs.gov"
+            },
+            "description": "To support state and local communication and outreach efforts, ASPE developed state, county, and sub-state level predictions of hesitancy rates using the most recently available federal survey data.",
+            "identifier": "https://data.cdc.gov/api/views/cnd2-a6zw",
             "issued": "2021-04-09",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-17",
             "keyword": [
                 "coronavirus",
                 "covid-19",
                 "vaccine hesitancy"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Joel Ruhter",
-                "hasEmail": "mailto:joel.ruhter@hhs.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/cnd2-a6zw",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2021-06-17",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/cnd2-a6zw",
-            "description": "To support state and local communication and outreach efforts, ASPE developed state, county, and sub-state level predictions of hesitancy rates using the most recently available federal survey data.",
-            "title": "Vaccine Hesitancy for COVID-19",
-            "programCode": [
-                "009:020"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "Vaccine Hesitancy for COVID-19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4ewf-ciy6",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "arboviral diseases",
-                "nedss",
-                "netss",
-                "nndss",
-                "st. louis encephalitis virus disease",
-                "western equine encephalitis virus disease",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4ewf-ciy6",
             "description": "NNDSS - Table 1C. Arboviral diseases, neuroinvasive and non-neuroinvasive,  St. Louis encephalitis virus disease to Western equine encephalitis virus disease - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1C. Arboviral diseases, St. Louis encephalitis virus to Western equine encephalitis virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29757,21 +29734,70 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4ewf-ciy6",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "arboviral diseases",
+                "nedss",
+                "netss",
+                "nndss",
+                "st. louis encephalitis virus disease",
+                "western equine encephalitis virus disease",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/4ewf-ciy6",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1C. Arboviral diseases, St. Louis encephalitis virus to Western equine encephalitis virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/COVID19/index.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "Provisional death counts of sickle cell disease and coronavirus disease 2019 (COVID-19), by quarter, age, and race or Hispanic origin from 2019 through Quarter 1, 2021.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3sh4-uqpm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3sh4-uqpm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3sh4-uqpm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3sh4-uqpm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/3sh4-uqpm",
             "issued": "2020-09-25",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-01-01/2021-03-31",
-            "modified": "2022-04-01",
             "keyword": [
                 "age",
                 "age group",
@@ -29788,60 +29814,60 @@
                 "sickle cell disease",
                 "united states"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/COVID19/index.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-01",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/3sh4-uqpm",
-            "description": "Provisional death counts of sickle cell disease and coronavirus disease 2019 (COVID-19), by quarter, age, and race or Hispanic origin from 2019 through Quarter 1, 2021.",
-            "title": "AH Sickle Cell Disease Provisional Death Counts 2019-2021",
-            "programCode": [
-                "009:020"
+            "spatial": "United States",
+            "temporal": "2019-01-01/2021-03-31",
+            "theme": [
+                "NCHS"
             ],
+            "title": "AH Sickle Cell Disease Provisional Death Counts 2019-2021"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "Annual",
+            "bureauCode": [
+                "009:20"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:healthus@cdc.gov"
+            },
+            "description": "Data on use of selected substances in the past 30 days among 12th graders, 10th graders, and 8th graders in the United States, by sex and race. Data are from Health, United States. Source: Monitoring the Future, Institute for Social Research, University of Michigan, supported by National Institutes of Health, National Institute on Drug Abuse.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/3sh4-uqpm/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/4kn2-jirk/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/3sh4-uqpm/rows.rdf?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/4kn2-jirk/rows.rdf?accessType=DOWNLOAD",
                     "mediaType": "application/rdf+xml"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/3sh4-uqpm/rows.json?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/4kn2-jirk/rows.json?accessType=DOWNLOAD",
                     "mediaType": "application/json"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/3sh4-uqpm/rows.xml?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/4kn2-jirk/rows.xml?accessType=DOWNLOAD",
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
-            "theme": [
-                "NCHS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/4kn2-jirk",
             "issued": "2024-09-04",
-            "temporal": "1980/2022",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-13",
             "keyword": [
                 "10th grade",
                 "12th grade",
@@ -29875,87 +29901,36 @@
                 "vaping",
                 "white"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:healthus@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4kn2-jirk",
-            "description": "Data on use of selected substances in the past 30 days among 12th graders, 10th graders, and 8th graders in the United States, by sex and race. Data are from Health, United States. Source: Monitoring the Future, Institute for Social Research, University of Michigan, supported by National Institutes of Health, National Institute on Drug Abuse.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Use of selected substances in the past 30 days among 12th graders, 10th graders, and 8th graders, by sex and race: United States",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-13",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4kn2-jirk/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4kn2-jirk/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4kn2-jirk/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4kn2-jirk/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "temporal": "1980/2022",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "DQS Use of selected substances in the past 30 days among 12th graders, 10th graders, and 8th graders, by sex and race: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/dataset/NREVSS-RSV",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-10-21",
-            "@type": "dcat:Dataset",
-            "temporal": "July 2010 - June 2020",
-            "modified": "2022-10-25",
-            "references": [
-                "https://www.cdc.gov/surveillance/nrevss/rsv/reports.html"
-            ],
-            "keyword": [
-                "ari",
-                "bronchiolitis",
-                "bronchitis",
-                "lri",
-                "nrevss",
-                "respiratory disease",
-                "respiratory syncytial virus",
-                "rsv"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Virologic Unit, Surveillance and Analytics Team",
                 "hasEmail": "mailto:nrevss@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/52kb-ccu2",
+            "describedBy": "https://www.cdc.gov/surveillance/nrevss/",
             "description": "Approximately 600 public health and clinical laboratories located throughout the United States, participate in surveillance for respiratory syncytial virus (RSV) through CDC's National Respiratory and Enteric Virus Surveillance System (NREVSS). The dataset contains a weekly summary of the total RSV tests and RSV detections reported to NREVSS. These data are reported on a voluntary basis. Clinical laboratories do not report demographic data through NREVSS. Testing practices and the number of participating laboratories may change from year to year. Results can be changed two years after the initial reporting week. However, discrepancies may be noted and updated at the discretion of the data stewards and key stakeholders.\n\nData are collected from collaborating university and community hospital laboratories, select states and county public health laboratories, and commercial laboratories. This information is submitted and updated on a weekly basis. \n\nWhile NREVSS strives to present the most precise national, regional and state respiratory viral trends with the least amount of burden possible for participating laboratories, there are a number of inherent limitations to this surveillance system. \n\nNREVSS does not collect patient-data or demographic information. Multiple samples may be collected from a single patient, so NREVSS results do not necessarily reflect the number of patients tested nor does it reflect hospitalizations or deaths related to a particular virus. \n\nParticipating laboratories vary in size, testing capabilities, and areas served. Some institutions may receive and test samples from sites across a given state or even from multiple states. Without direct knowledge of the population base, NREVSS cannot be used to determine the prevalence or incidence of infection.\n\n\nFor more information on RSV surveillance and research please visit: https://www.cdc.gov/surveillance/nrevss and https://www.cdc.gov/rsv/research/us-surveillance.html",
-            "title": "Respiratory Syncytial Virus Laboratory Data (NREVSS)",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29978,57 +29953,59 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "All US Jurisdictions",
-            "describedBy": "https://www.cdc.gov/surveillance/nrevss/",
+            "identifier": "https://data.cdc.gov/api/views/52kb-ccu2",
+            "issued": "2022-10-21",
+            "keyword": [
+                "ari",
+                "bronchiolitis",
+                "bronchitis",
+                "lri",
+                "nrevss",
+                "respiratory disease",
+                "respiratory syncytial virus",
+                "rsv"
+            ],
+            "landingPage": "https://data.cdc.gov/dataset/NREVSS-RSV",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-10-25",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/surveillance/nrevss/rsv/reports.html"
+            ],
+            "spatial": "All US Jurisdictions",
+            "temporal": "July 2010 - June 2020",
             "theme": [
                 "Laboratory Surveillance"
-            ]
+            ],
+            "title": "Respiratory Syncytial Virus Laboratory Data (NREVSS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/innovation-center-data-and-reports",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2024-12-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-20",
-            "references": [
-                "https://data.cms.gov/resources/data-and-reports-methodology"
-            ],
-            "keyword": [
-                "children's health insurance program",
-                "medicare",
-                "medicare advantage",
-                "medicare prescription drug",
-                "original medicare",
-                "payment models",
-                "value-based care"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CMS Innovation Center - CMMI",
                 "hasEmail": "mailto:cmmi-dataset-support@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/c0451a3a-a86c-4bd4-a0b7-c93e6b1f1257/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/data-and-reports-data-dictionary",
             "description": "The Innovation Center Data and Reports dataset contains a variety of contributions from CMS Innovation Center models, demonstrations, initiatives and programs. These resources include evaluation reports and associated materials, reports to Congress, and case studies among others.",
-            "title": "Innovation Center Data and Reports",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c0451a3a-a86c-4bd4-a0b7-c93e6b1f1257/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c0451a3a-a86c-4bd4-a0b7-c93e6b1f1257/data",
+                    "mediaType": "text/html",
                     "title": "Innovation Center Data and Reports : 2024-12-20"
                 },
                 {
@@ -30044,46 +30021,53 @@
                     "title": "Innovation Center Data and Reports : 2024-12-20"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/data-and-reports-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/c0451a3a-a86c-4bd4-a0b7-c93e6b1f1257/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "children's health insurance program",
+                "medicare",
+                "medicare advantage",
+                "medicare prescription drug",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/innovation-center-data-and-reports",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2024-12-20",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/data-and-reports-methodology"
+            ],
+            "temporal": "2024-12-01/2024-12-31",
             "theme": [
                 "Medicare",
                 "Children's Health Insurance Program"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Innovation Center Data and Reports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm080123.htm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-01-02",
-            "keyword": [
-                "cder",
-                "inactive ingredient"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "61f4a54b-daf5-4eb0-82fa-30dc89cd9699",
+            "describedBy": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm075230.htm",
             "description": "According to 21 CFR 210.3(b)(8), an inactive ingredient is any component of a drug product other than the active ingredient. Only inactive ingredients in the final dosage forms of drug products are in this database.",
-            "title": "Inactive ingredient Search for Approved Drug Products",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30091,43 +30075,37 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm075230.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "61f4a54b-daf5-4eb0-82fa-30dc89cd9699",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cder",
+                "inactive ingredient"
+            ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm080123.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-01-02",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Inactive ingredient Search for Approved Drug Products"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fpsi-y8tj",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-13",
-            "temporal": "2019-01-01/Present",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "deaths",
-                "drug overdose",
-                "firearm injury",
-                "homicide",
-                "mortality",
-                "nchs",
-                "suicide"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCIPC",
                 "hasEmail": "mailto:injurydashboard@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/fpsi-y8tj",
             "description": "This file contains death counts and death rates for drug overdose, suicide, homicide and firearm injuries by state of residence (additional datasets exist for other levels of geography). The data is grouped by 2 different time periods including yearly and trailing twelve months. Please see data dictionary for intents and mechanisms included in each measure.",
-            "title": "Mapping Injury, Overdose, and Violence - State",
-            "programCode": [
-                "009:033"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30150,42 +30128,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
-            "theme": [
-                "Injury & Violence"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#vaccinations-pregnant-women",
-            "bureauCode": [
-                "009:20"
+            "identifier": "https://data.cdc.gov/api/views/fpsi-y8tj",
+            "issued": "2025-01-13",
+            "keyword": [
+                "deaths",
+                "drug overdose",
+                "firearm injury",
+                "homicide",
+                "mortality",
+                "nchs",
+                "suicide"
             ],
-            "issued": "2021-11-24",
+            "landingPage": "https://data.cdc.gov/d/fpsi-y8tj",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:033"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2019-01-01/Present",
+            "theme": [
+                "Injury & Violence"
+            ],
+            "title": "Mapping Injury, Overdose, and Violence - State"
+        },
+        {
             "@type": "dcat:Dataset",
-            "modified": "2022-04-22",
-            "keyword": [
-                "covid-19 vaccine",
-                "covid tracker",
-                "pregnancy",
-                "vsd"
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Assessment Branch, Immunization Services Division, NCIRD, CDC",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4ht3-nbmd",
             "description": "These archived cumulative COVID-19 vaccination coverage estimates are for persons who were pregnant anytime from December 20, 2020, to January 20, 2022, and received at least 1 dose of COVID-19 vaccine during pregnancy based on data from the Vaccine Safety Datalink*. As of January 20, 2022, after moving to reporting weekly estimates, the figures on https://covid.cdc.gov/covid-data-tracker/#vaccinations-pregnant-women no longer present cumulative estimates, and these   archived data are no longer updated.\n\nFor these cumulative data, on December 15, 2021, an error was identified where pregnant people who had received an additional or booster dose of a COVID-19 vaccine were not included in the coverage estimates. After correcting the error, coverage estimates for the week of December 11, 2021, increased overall and by race/ethnicity. The persons that were inadvertently excluded have been counted in the December 11, 2021, estimates. Prior weeks\u2019 estimates have not been updated.",
-            "title": "Archived Cumulative Data: Percent of pregnant people aged 18-49 years receiving at least one dose of a COVID-19 vaccine during pregnancy overall, by race/ethnicity, and date reported to CDC-Vaccine Safety Datalink*, United States | December 20, 2020 \u2013 Jan",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30208,43 +30189,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4ht3-nbmd",
+            "issued": "2021-11-24",
+            "keyword": [
+                "covid-19 vaccine",
+                "covid tracker",
+                "pregnancy",
+                "vsd"
+            ],
+            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#vaccinations-pregnant-women",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-04-22",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "Archived Cumulative Data: Percent of pregnant people aged 18-49 years receiving at least one dose of a COVID-19 vaccine during pregnancy overall, by race/ethnicity, and date reported to CDC-Vaccine Safety Datalink*, United States | December 20, 2020 \u2013 Jan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-visualization/mortality-trends/index.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-07-14",
-            "@type": "dcat:Dataset",
-            "temporal": "1900/2017",
-            "modified": "2022-04-01",
-            "keyword": [
-                "children",
-                "death rates",
-                "mortality",
-                "nchs",
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/v6ab-adf5",
             "description": "This dataset of U.S. mortality trends since 1900 highlights childhood mortality rates by age group for age at death.\n\nAge-adjusted death rates (deaths per 100,000) after 1998 are calculated based on the 2000 U.S. standard population. Populations used for computing death rates for 2011\u20132017 are postcensal estimates based on the 2010 census, estimated as of July 1, 2010. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for noncensus years between 2000 and 2010 are revised using updated intercensal population estimates and may differ from rates previously published. Data on age-adjusted death rates prior to 1999 are taken from historical data (see References below).\n\nAge groups for childhood death rates are based on age at death.\n\nSOURCES\n\nCDC/NCHS, National Vital Statistics System, historical data, 1900-1998 (see https://www.cdc.gov/nchs/nvss/mortality_historical_data.htm); CDC/NCHS, National Vital Statistics System, mortality data (see http://www.cdc.gov/nchs/deaths.htm); and CDC WONDER (see http://wonder.cdc.gov).\n\nREFERENCES\n\n1. National Center for Health Statistics, Data Warehouse. Comparability of cause-of-death between ICD revisions. 2008. Available from: http://www.cdc.gov/nchs/nvss/mortality/comparability_icd.htm.\n\n2. National Center for Health Statistics. Vital statistics data available. Mortality multiple cause files. Hyattsville, MD: National Center for Health Statistics. Available from: https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm.\n\n3. Kochanek KD, Murphy SL, Xu JQ, Arias E. Deaths: Final data for 2017. National Vital Statistics Reports; vol 68 no 9. Hyattsville, MD: National Center for Health Statistics. 2019. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_09-508.pdf.\n\n4. Arias E, Xu JQ. United States life tables, 2017. National Vital Statistics Reports; vol 68 no 7. Hyattsville, MD: National Center for Health Statistics. 2019. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_07-508.pdf.\n\n5. National Center for Health Statistics. Historical Data, 1900-1998. 2009. Available from: https://www.cdc.gov/nchs/nvss/mortality_historical_data.htm.",
-            "title": "NCHS - Childhood Mortality Rates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30267,45 +30247,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/v6ab-adf5",
+            "issued": "2015-07-14",
+            "keyword": [
+                "children",
+                "death rates",
+                "mortality",
+                "nchs",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/mortality-trends/index.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2022-04-01",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "1900/2017",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - Childhood Mortality Rates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/web-based-injury-statistics-query-and-reporting-system-wisqars",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "community health",
-                "injury deaths",
-                "nonfatal injuries",
-                "safety",
-                "violent deaths",
-                "ypll"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Data",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
-            },
-            "identifier": "bb0ead59-b3fd-4b14-8d12-439e8240fc82",
             "description": "<p>WISQARS is an interactive query system that provides data on injury deaths, violent deaths, and nonfatal injuries treated in U.S. emergency departments.</p>",
-            "title": "Web-based Injury Statistics Query and Reporting System (WISQARS)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30314,22 +30293,47 @@
                     "title": "Query Tool"
                 }
             ],
+            "identifier": "bb0ead59-b3fd-4b14-8d12-439e8240fc82",
+            "issued": "2012-05-30",
+            "keyword": [
+                "community health",
+                "injury deaths",
+                "nonfatal injuries",
+                "safety",
+                "violent deaths",
+                "ypll"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/web-based-injury-statistics-query-and-reporting-system-wisqars",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
             "theme": [
                 "Health",
                 "Community"
-            ]
+            ],
+            "title": "Web-based Injury Statistics Query and Reporting System (WISQARS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/head-start-program-information-report-hspir",
             "bureauCode": [
                 "001:05"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Head Start Enterprise System (HSES) Help Desk",
+                "hasEmail": "mailto:help@hsesinfo.org"
+            },
+            "dataQuality": true,
+            "description": "<p>Information about children enrolled in the Head Start program and information about their families.  Data about the children include: age, type of program attended, health status, and health treatment and/or special services required during enrollment.  Data about the parents include: income, employment status and special services required during child(ren)\u2019s enrollment.  Contact the Head Start Enterprise System (HSES) Help Desk to request access <a href=\"mailto:help@hsesinfo.org\">help@hsesinfo.org</a>.</p>",
+            "identifier": "f9951be4-221c-4964-903e-9060cf42973a",
             "issued": "2014-06-26",
-            "temporal": "2003-01-01T00:00:00-05:00/2003-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "children's health",
                 "fihet",
@@ -30337,57 +30341,35 @@
                 "population statistics",
                 "social determinates of health"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Head Start Enterprise System (HSES) Help Desk",
-                "hasEmail": "mailto:help@hsesinfo.org"
-            },
+            "landingPage": "https://healthdata.gov/dataset/head-start-program-information-report-hspir",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:103"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Administration for Children and Families, Department of Health & Human Services"
             },
-            "identifier": "f9951be4-221c-4964-903e-9060cf42973a",
-            "description": "<p>Information about children enrolled in the Head Start program and information about their families.  Data about the children include: age, type of program attended, health status, and health treatment and/or special services required during enrollment.  Data about the parents include: income, employment status and special services required during child(ren)\u2019s enrollment.  Contact the Head Start Enterprise System (HSES) Help Desk to request access <a href=\"mailto:help@hsesinfo.org\">help@hsesinfo.org</a>.</p>",
-            "title": "Head Start Program Information Report (HSPIR)",
-            "programCode": [
-                "009:103"
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "2003-01-01T00:00:00-05:00/2003-01-01T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "Head Start Program Information Report (HSPIR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datatools.ahrq.gov",
             "bureauCode": [
                 "009:33"
             ],
-            "issued": "2022-06-03",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
-                "insurance",
-                "medical expenditure",
-                "meps"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MEPS Project Director",
                 "hasEmail": "mailto:mepsprojectdirector@ahrq.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
-            },
-            "identifier": "https://healthdata.gov/api/views/835z-2bza",
+            "describedBy": "https://datatools.ahrq.gov/meps-ic",
             "description": "The Medical Expenditure Panel Survey Insurance Component (MEPS-IC) is an annual survey of private employers and State and local governments. The MEPS-IC produces national and State level estimates of employer-sponsored insurance, including offered plans, costs, employee eligibility, and number of enrollees. With the MEPS-IC Data Tools, users can interactively explore maps, trends, and cross-sectional bar charts for topics related to national and state-level employer-based health insurance for employer characteristics/offerings; employee take-up; premiums; contributions; and cost-sharing. The MEPS-IC is sponsored by the Agency for Healthcare Research and Quality and is fielded by the U.S. Census Bureau.",
-            "title": "Medical Expenditure Panel Survey (MEPS) Insurance Component Data Tools",
-            "programCode": [
-                "009:072"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30396,67 +30378,72 @@
                     "title": "Query Tool "
                 }
             ],
-            "describedBy": "https://datatools.ahrq.gov/meps-ic"
+            "identifier": "https://healthdata.gov/api/views/835z-2bza",
+            "issued": "2022-06-03",
+            "keyword": [
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "insurance",
+                "medical expenditure",
+                "meps"
+            ],
+            "landingPage": "https://datatools.ahrq.gov",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:072"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
+            },
+            "title": "Medical Expenditure Panel Survey (MEPS) Insurance Component Data Tools"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://ndct.nimh.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Farber, Greg",
+                "hasEmail": "mailto:farberg@mail.nih.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The National Database for Clinical Trials Related to Mental Illness (NDCT) is an extensible informatics platform for relevant data at all levels of biological and behavioral organization (molecules, genes, neural tissue, behavioral, social and environmental interactions) and for all data types (text, numeric, image, time series, etc.) related to clinical trials funded by the National Institute of Mental Health. Sharing data, associated tools, methodologies and results, rather than just summaries or interpretations, accelerates research progress. Community-wide sharing requires common data definitions and standards, as well as comprehensive and coherent informatics approaches for the sharing of de-identified human subject research data. Built on the National Database for Autism Research (NDAR) informatics platform, NDCT provides a comprehensive data sharing platform for NIMH grantees supporting clinical trials.</p>",
+            "identifier": "ed15583e-8ed9-451c-9724-5b98bde9f068",
             "issued": "2016-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "clinical trials",
                 "mental health",
                 "mental illness"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Farber, Greg",
-                "hasEmail": "mailto:farberg@mail.nih.gov"
-            },
+            "landingPage": "http://ndct.nimh.nih.gov/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:060"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Institutes of Health (NIH)"
             },
-            "identifier": "ed15583e-8ed9-451c-9724-5b98bde9f068",
-            "description": "<p>The National Database for Clinical Trials Related to Mental Illness (NDCT) is an extensible informatics platform for relevant data at all levels of biological and behavioral organization (molecules, genes, neural tissue, behavioral, social and environmental interactions) and for all data types (text, numeric, image, time series, etc.) related to clinical trials funded by the National Institute of Mental Health. Sharing data, associated tools, methodologies and results, rather than just summaries or interpretations, accelerates research progress. Community-wide sharing requires common data definitions and standards, as well as comprehensive and coherent informatics approaches for the sharing of de-identified human subject research data. Built on the National Database for Autism Research (NDAR) informatics platform, NDCT provides a comprehensive data sharing platform for NIMH grantees supporting clinical trials.</p>",
-            "title": "National Database for Clinical Trials Related to Mental Illness (NDCT)",
-            "programCode": [
-                "009:060"
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "National Database for Clinical Trials Related to Mental Illness (NDCT)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bc4h-zh8r",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-06-29",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "v-safe inquiries team",
                 "hasEmail": "mailto:vsafe@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/bc4h-zh8r",
             "description": "Users of the v-safe mpox data are required to adhere to the following standards for the analysis and reporting of research data. All research results must be presented and/or published in a manner that protects the confidentiality of participants. v-safe mpox data will not be presented and/or published in any way in which an individual can be identified. \n<br>\n<br>Therefore, users will:\n<br>\n<br>1. Not attempt to link or permit others to link the data with individually identified records in another database.\n<br>2. Not attempt to learn the identity of any participant in the data and will not deliberately combine these data with other CDC or non-CDC data for the purpose of matching records to identify individuals. If you should inadvertently discover the identity of any participant, you will ensure the identity of any participant is kept confidential, and will not be used in any publications and/or presentations.\n<br>3. Not imply or state, either in written or oral form, that interpretations based on analysis of the data reflect official CDC policies or positions.\n<br>4. Understand that sub-national analyses are not appropriate for this national sample and will not be conducted. \n<br>5. Understand that v-safe mpox is a voluntary self-enrollment program requiring smartphone access; therefore, information from v-safe mpox might not be representative or generalizable to the US population.\n\n<br>By clicking on the weblink below to download and use these v-safe data, you signify your agreement to comply with the above-stated terms.\n<br>\n<br>v-safe mpox is an active surveillance program to monitor the safety of mpox vaccines during the period when the vaccines are authorized for use under Food and Drug Administration (FDA) Emergency Use Authorization (EUA) and after vaccine licensure.\n<br>\n<br>These data include registrant information (deidentified), health check-in, and vaccination data collected through the mpox response.",
-            "title": "v-safe mpox",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30464,35 +30451,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bc4h-zh8r",
+            "issued": "2023-06-29",
+            "landingPage": "https://data.cdc.gov/d/bc4h-zh8r",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:028"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "v-safe mpox"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/62a3-8df5",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-12-30",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-08",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Pathology and Physiology Research Branch (PPRB), Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/62a3-8df5",
             "description": "Chemerin, a non-chemokine chemoattractant, and resolvin E1 (RvE1), a specialized pro-resolving lipid mediator, are endogenous ligands for chemerin-like receptor 1 (CMKLR1), a Gi/o protein-coupled receptor expressed by leukocytes and non-leukocytes.  In mice, exogenous administration of chemerin or RvE1 diminishes the severity of lung inflammation and airway hyperresponsiveness (AHR) induced by antigen sensitization and challenge, which mimics phenotypic features of atopic asthma in humans.  However, the contribution of chemerin or RvE1 to features of non-atopic asthma is unknown.  Therefore, to indirectly assess if chemerin or RvE1 facilitates development of a non-atopic asthma phenotype, which includes AHR to acetyl-\u03b2-methylcholine chloride, lung hyperpermeability, airway epithelial cell desquamation, and lung inflammation, we quantified features of these sequelae in wild-type mice and mice failing to express CMKLR1 (CMKLR1-deficient mice) following cessation of acute inhalation exposure to either filtered room air or ozone, a criteria pollutant and non-atopic asthma stimulus.",
-            "title": "Inconsequential Role for Chemerin-Like Receptor 1 in a Manifestation of Ozone-Induced Lung Pathophysiology in Male Mice",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30500,39 +30487,37 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/62a3-8df5",
+            "issued": "2024-12-30",
+            "landingPage": "https://data.cdc.gov/d/62a3-8df5",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-08",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Inconsequential Role for Chemerin-Like Receptor 1 in a Manifestation of Ozone-Induced Lung Pathophysiology in Male Mice"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -30555,43 +30540,40 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
             "accessLevel": "public",
-            "landingPage": "https://openi.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "images",
-                "literature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/cyyg-r75d",
             "description": "Open-i service provides search and retrieval of abstracts and images (including charts, graphs, clinical images, etc.) from the open source literature, and biomedical image collections. Searching may be done by text queries as well as by query images.",
-            "title": "Open-i",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30606,41 +30588,42 @@
                     "title": "Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/cyyg-r75d",
+            "issued": "2021-06-30",
+            "keyword": [
+                "api",
+                "images",
+                "literature"
+            ],
+            "landingPage": "https://openi.nlm.nih.gov/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Images"
-            ]
+            ],
+            "title": "Open-i"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://eldercare.acl.gov/Public/index.aspx",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-03",
-            "keyword": [
-                "aging",
-                "caregiving",
-                "eldercare",
-                "health care providers"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "rhornyak",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Administration for Community Living, Department of Health & Human Services"
-            },
-            "identifier": "70d2b79b-1339-4fd9-b6cb-3db41d3c430a",
+            "dataQuality": true,
+            "describedBy": "http://www.eldercare.gov/Eldercare.NET/Public/Site_Utilities/Private_Data1/Private_Data2/Private_Data3/Index.aspx",
             "description": "<p>The Eldercare Locator is a searchable database that allows a user to search via zip code or city/ state for agencies at the State and local levels that provide services to older adults.</p>",
-            "title": "Eldercare Locator Database",
-            "programCode": [
-                "009:044"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30649,37 +30632,39 @@
                     "title": "Query Tool "
                 }
             ],
-            "describedBy": "http://www.eldercare.gov/Eldercare.NET/Public/Site_Utilities/Private_Data1/Private_Data2/Private_Data3/Index.aspx",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "70d2b79b-1339-4fd9-b6cb-3db41d3c430a",
+            "issued": "2012-05-30",
+            "keyword": [
+                "aging",
+                "caregiving",
+                "eldercare",
+                "health care providers"
+            ],
+            "landingPage": "https://eldercare.acl.gov/Public/index.aspx",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2024-06-03",
+            "programCode": [
+                "009:044"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Community Living, Department of Health & Human Services"
+            },
+            "title": "Eldercare Locator Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/84ne-7i7r",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-01-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-16",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "4eaa5ebe-62f7-402e-a407-963cd380688b",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-08-to-2024-01-14",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30688,39 +30673,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-08-to-2024-01-14"
                 }
             ],
+            "identifier": "4eaa5ebe-62f7-402e-a407-963cd380688b",
+            "issued": "2024-01-17",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/84ne-7i7r",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-01-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-08-to-2024-01-14"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/Software.cgi",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "computational biology",
-                "genomics",
-                "software",
-                "tools & utilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/a7mv-2ucw",
             "description": "GRAF (Genetic Relationship and Fingerprinting) is a C++ program that quickly finds the closely related subjects, infers subject ancestry, determines subject sexes using genotypes and compares the results derived from genotypes with those reported in the phenotype datasets",
-            "title": "GRAF (Genetic Relationship and Fingerprinting)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30729,41 +30710,41 @@
                     "title": "GRAF (Genetic Relationship and Fingerprinting) Homepage"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/a7mv-2ucw",
+            "issued": "2021-06-30",
+            "keyword": [
+                "computational biology",
+                "genomics",
+                "software",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/Software.cgi",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-04",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Molecular biology/Genetics"
-            ]
+            ],
+            "title": "GRAF (Genetic Relationship and Fingerprinting)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rppv-wbiv",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2014-10-16",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
-            "keyword": [
-                "cdc.gov",
-                "page views",
-                "syndication",
-                "web pages"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rppv-wbiv",
             "description": "The CDC Content Syndication site at https://tools.cdc.gov/syndication/ allows you to import content from CDC websites directly into your own website or application. These services are provided free of charge from CDC. The data shown in this table represent the weekly top page views from CDC.gov offered by syndication.",
-            "title": "Top syndicated pages from CDC.gov by weekly page views",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30786,44 +30767,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rppv-wbiv",
+            "issued": "2014-10-16",
+            "keyword": [
+                "cdc.gov",
+                "page views",
+                "syndication",
+                "web pages"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rppv-wbiv",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-21",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Web Metrics"
-            ]
+            ],
+            "title": "Top syndicated pages from CDC.gov by weekly page views"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/medlineplus-health-topic-web-service",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-05-30",
-            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "biomedical research",
-                "community health",
-                "health",
-                "health services",
-                "medicine",
-                "wellness"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "admin",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "de0c318c-5a83-4a99-9bc6-2feb7e24b204",
+            "dataQuality": true,
             "description": "<p>A search-based Web service that provides access to disease, condition and wellness information via MedlinePlus health topic data in XML format.  The service accepts keyword searches as requests and returns relevant MedlinePlus health topics in ranked order.  The service also returns health topics summaries, search result snippets and other associated data.</p>",
-            "title": "MedlinePlus Health Topic Web Service",
-            "programCode": [
-                "009:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30832,50 +30811,45 @@
                     "title": "API"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "de0c318c-5a83-4a99-9bc6-2feb7e24b204",
+            "issued": "2012-05-30",
+            "keyword": [
+                "biomedical research",
+                "community health",
+                "health",
+                "health services",
+                "medicine",
+                "wellness"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/medlineplus-health-topic-web-service",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:046"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
             "theme": [
                 "Community",
                 "Health"
-            ]
+            ],
+            "title": "MedlinePlus Health Topic Web Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-09-29",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
-            "keyword": [
-                "behaviors",
-                "county",
-                "gis",
-                "outcomes",
-                "places",
-                "prevalence",
-                "prevention",
-                "unhealthy"
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
-            "identifier": "https://data.cdc.gov/api/views/mssc-ksj7",
             "description": "This dataset contains model-based county-level estimates for the PLACES project 2020 release in GIS-friendly format. The PLACES project is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code tabulation Areas (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2018 or 2017 data, Census Bureau 2018 or 2017 county population estimates, and American Community Survey (ACS) 2014-2018 or 2013-2017 estimates. The 2020 release uses 2018 BRFSS data for 23 measures and 2017 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening). Four measures are based on the 2017 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the census 2015 county boundary file in a GIS system to produce maps for 27 measures at the county level. An ArcGIS Online feature service is also available at https://www.arcgis.com/home/item.html?id=8eca985039464f4d83467b8f6aeb1320 for users to make maps online or to add data to desktop GIS software.",
-            "title": "PLACES: County Data (GIS Friendly Format), 2020 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30898,43 +30872,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mssc-ksj7",
+            "issued": "2021-09-29",
+            "keyword": [
+                "behaviors",
+                "county",
+                "gis",
+                "outcomes",
+                "places",
+                "prevalence",
+                "prevention",
+                "unhealthy"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-25",
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
+            "title": "PLACES: County Data (GIS Friendly Format), 2020 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5jp2-pgaw",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-10-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-25",
-            "keyword": [
-                "covid-19",
-                "providers",
-                "vaccination locations",
-                "vaccination sites",
-                "vaccinefinder",
-                "vaccines"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC",
                 "hasEmail": "mailto:vaccinefinder@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5jp2-pgaw",
             "description": "Because inventory reporting is no longer required, Vaccines.gov information will not be updated on this site after July 2024.",
-            "title": "Vaccines.gov: COVID-19 vaccinating provider locations",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30957,44 +30936,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5jp2-pgaw",
+            "issued": "2023-10-17",
+            "keyword": [
+                "covid-19",
+                "providers",
+                "vaccination locations",
+                "vaccination sites",
+                "vaccinefinder",
+                "vaccines"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5jp2-pgaw",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-09-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "Vaccines.gov: COVID-19 vaccinating provider locations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/art/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "art",
-                "assisted reproductive technology",
-                "clinic",
-                "fertility",
-                "infertility",
-                "services",
-                "success rates"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ARTINFO",
                 "hasEmail": "mailto:ARTINFO@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6ryw-hetw",
+            "describedBy": "https://data.cdc.gov/dataset/2021-Final-Assisted-Reproductive-Technology-ART-Pa/6ryw-hetw",
             "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Patient and Cycle Characteristics dataset summarizes the types of ART services performed and the kinds of patients who received ART procedures in a specific clinic. Please note patient characteristics are presented per cycle rather than per patient. As a result, patients who had more than one ART cycle within the reporting year are represented more than once.",
-            "title": "2021 Final Assisted Reproductive Technology (ART) Patient and Cycle Characteristics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31017,53 +30996,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/dataset/2021-Final-Assisted-Reproductive-Technology-ART-Pa/6ryw-hetw",
+            "identifier": "https://data.cdc.gov/api/views/6ryw-hetw",
+            "issued": "2023-01-01",
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
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
+            "title": "2021 Final Assisted Reproductive Technology (ART) Patient and Cycle Characteristics"
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
-                "brfss",
-                "disability",
-                "health",
-                "outcomes",
-                "places",
-                "prevalence",
-                "prevention",
-                "risk",
-                "status",
-                "zcta",
-                "zip code"
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
-            "identifier": "https://data.cdc.gov/api/views/qnzd-25i4",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-ZCTA-Data-2020/qnzd-25i4",
             "description": "This dataset contains model-based ZIP Code Tabulation Area (ZCTA) level estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 40 measures: 12 for health outcomes, 7 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, 3 for health status, and 7 for health-related scocial needs. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2022 or 2021 data, Census Bureau 2020 population data, and American Community Survey 2018\u20132022 estimates. The 2024 release uses 2022 BRFSS data for 36 measures and 2021 BRFSS data for 4 measures (high blood pressure, high cholesterol, cholesterol screening, and taking medicine for high blood pressure control among those with high blood pressure) that the survey collects data on every other year. More information about the methodology can be found at   www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, ZCTA Data 2024 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31086,48 +31057,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-ZCTA-Data-2020/qnzd-25i4",
+            "identifier": "https://data.cdc.gov/api/views/qnzd-25i4",
+            "issued": "2024-08-23",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "disability",
+                "health",
+                "outcomes",
+                "places",
+                "prevalence",
+                "prevention",
+                "risk",
+                "status",
+                "zcta",
+                "zip code"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
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
+            "title": "PLACES: Local Data for Better Health, ZCTA Data 2024 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nnhs/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
-            "issued": "2009-06-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2004-08-01/2004-12-31",
-            "modified": "2024-03-25",
-            "keyword": [
-                "current nursing home residents",
-                "icd-9-cm",
-                "long-term care",
-                "national nursing home survey",
-                "research-data-center",
-                "resident health status"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/s5en-5rpd",
-            "description": "The 2004 National Nursing Home Survey (NNHS), conducted between August and December of 2004, was reintroduced into the field after a five-year break, during which time the survey was redesigned and expanded to collect many new data items. All nursing homes that participated in the NNHS had at least three beds and were either certified (by Medicare or Medicaid) or had a state license to operate as a nursing home. The redesigned survey was administered using a computer-assisted personal interviewing (CAPI) system. The National Nursing Home Survey provides information on nursing homes from two perspectives-that of the provider of services and that of the recipient of care. Data about the facilities include characteristics such as size, ownership, Medicare/Medicaid certification, services provided and specialty programs offered, and charges. For recipients, data were obtained on demographic characteristics, health status and medications taken, services received, and sources of payment.\n\nData for the survey were obtained through personal interviews with facility administrators and designated staff who used administrative records to answer questions about the facilities, staff, services and programs, and medical records to answer questions about the residents.\n\nThe total number of nursing home facilities that participated in NNHS is 1,174.",
-            "title": "2004 National Nursing Home Survey - Restricted Current Resident Dataset",
-            "isPartOf": "https://www.cdc.gov/nchs/nnhs/nnhs_questionnaires.htm",
+            "describedBy": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NNHS/nnhs04/2004ResidentFile_DataDictionary_061609.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The 2004 National Nursing Home Survey (NNHS), conducted between August and December of 2004, was reintroduced into the field after a five-year break, during which time the survey was redesigned and expanded to collect many new data items. All nursing homes that participated in the NNHS had at least three beds and were either certified (by Medicare or Medicaid) or had a state license to operate as a nursing home. The redesigned survey was administered using a computer-assisted personal interviewing (CAPI) system. The National Nursing Home Survey provides information on nursing homes from two perspectives-that of the provider of services and that of the recipient of care. Data about the facilities include characteristics such as size, ownership, Medicare/Medicaid certification, services provided and specialty programs offered, and charges. For recipients, data were obtained on demographic characteristics, health status and medications taken, services received, and sources of payment.\n\nData for the survey were obtained through personal interviews with facility administrators and designated staff who used administrative records to answer questions about the facilities, staff, services and programs, and medical records to answer questions about the residents.\n\nThe total number of nursing home facilities that participated in NNHS is 1,174.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31136,45 +31113,50 @@
                     "title": "2004 National Nursing Home Survey - Current Resident Restricted Dataset"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NNHS/nnhs04/2004ResidentFile_DataDictionary_061609.pdf",
+            "identifier": "https://data.cdc.gov/api/views/s5en-5rpd",
+            "isPartOf": "https://www.cdc.gov/nchs/nnhs/nnhs_questionnaires.htm",
+            "issued": "2009-06-16",
+            "keyword": [
+                "current nursing home residents",
+                "icd-9-cm",
+                "long-term care",
+                "national nursing home survey",
+                "research-data-center",
+                "resident health status"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nnhs/index.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-03-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
+            "spatial": "United States",
+            "temporal": "2004-08-01/2004-12-31",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2004 National Nursing Home Survey - Restricted Current Resident Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/w9zu-fywh",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-02-26",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-05",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "vaccination"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ASPA Media",
                 "hasEmail": "mailto:media@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/w9zu-fywh",
             "description": "New weekly allocations of doses are posted every Tuesday.  Beginning the following Thursday, states can begin ordering doses from that week\u2019s new allocation of 1st doses.  Beginning two weeks (Pfizer) or three weeks (Moderna) from the following Sunday, states can begin ordering doses from that week\u2019s new allocation of 2nd doses. After doses are ordered by states, shipments begin the following Monday. The entire order may not arrive in one shipment or on one day, but over the course of the week.\n\nSecond doses are opened up for orders on Sundays, at the appropriate interval two or three weeks later according to the manufacturer\u2019s label, with shipments occurring after jurisdictions place orders. \n\nShipments of an FDA-authorized safe and effective COVID-19 vaccine continue to arrive at sites across America. Vaccinations began on December 14, 2020. \n\nhttps://www.hhs.gov/coronavirus/covid-19-vaccines/index.html\n\nPfizer Vaccine Data - https://data.cdc.gov/Vaccinations/COVID-19-Vaccine-Initial-Allocations-Pfizer/saz5-9hgg\n\nModerna Vaccine Data- https://data.cdc.gov/Vaccinations/COVID-19-Vaccine-Distribution-Allocations-by-Juris/b7pe-5nws",
-            "title": "COVID-19 Vaccine Distribution Allocations by Jurisdiction - Janssen",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31197,68 +31179,67 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/w9zu-fywh",
+            "issued": "2021-02-26",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/w9zu-fywh",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2021-05-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "COVID-19 Vaccine Distribution Allocations by Jurisdiction - Janssen"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pubchem.ncbi.nlm.nih.gov/pug/pughelp.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2012-08-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "biochemistry",
-                "chemistry",
-                "dataset"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/84c4-vbci",
             "description": "PUG provides access to PubChem services via a programmatic interface. Users may download data, initiate chemical structure searches, standardize chemical structures and interact with E-utilities. Access PUG with standard URLs or via SOAP.  Technical documentation at http://pubchem.ncbi.nlm.nih.gov/pug/pughelp.html",
-            "title": "PubChem Power User Gateway (PUG)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://pubchemdocs.ncbi.nlm.nih.gov/power-user-gateway",
-                    "description": "The PubChem Power User Gateway (PUG) provides access to PubChem services via a programmatic interface. The basic design principle is straightforward. There is a single CGI (pug.cgi, referred to hereafter as simply PUG) that is the central gateway to multiple PubChem functions. PUG takes no URL arguments; all communication with PUG is through XML.",
                     "@type": "dcat:Distribution",
+                    "description": "The PubChem Power User Gateway (PUG) provides access to PubChem services via a programmatic interface. The basic design principle is straightforward. There is a single CGI (pug.cgi, referred to hereafter as simply PUG) that is the central gateway to multiple PubChem functions. PUG takes no URL arguments; all communication with PUG is through XML.",
+                    "downloadURL": "https://pubchemdocs.ncbi.nlm.nih.gov/power-user-gateway",
+                    "mediaType": "text/html",
                     "title": "API - PubChem Power User Gateway (PUG)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest-tutorial",
-                    "description": "This REST-style interface is intended to be a simple access route to PubChem for things like scripts, javascript embedded in web pages, and 3rd party applications, without the overhead of XML, SOAP envelopes, etc. that are required for other versions of PUG. PUG REST also provides convenient access to information on PubChem records that is not possible with any other service.",
                     "@type": "dcat:Distribution",
+                    "description": "This REST-style interface is intended to be a simple access route to PubChem for things like scripts, javascript embedded in web pages, and 3rd party applications, without the overhead of XML, SOAP envelopes, etc. that are required for other versions of PUG. PUG REST also provides convenient access to information on PubChem records that is not possible with any other service.",
+                    "downloadURL": "https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest-tutorial",
+                    "mediaType": "text/html",
                     "title": "REST - PubChem Power User Gateway (PUG)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://pubchemdocs.ncbi.nlm.nih.gov/pug-view",
-                    "description": "PUG View is a REST-style web service that provides information content that is not directly contained within the primary PubChem Substance, Compound, or BioAssay records. Its purpose is primarily to drive the PubChem database summary record web pages, but can also be used independently as a programmatic web service. PUG View is mainly designed to provide complete summary reports on individual PubChem records. Users may also be interested in PUG REST (https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest-tutorial), a different style of service that gives smaller bits of information about one or more PubChem records.",
                     "@type": "dcat:Distribution",
+                    "description": "PUG View is a REST-style web service that provides information content that is not directly contained within the primary PubChem Substance, Compound, or BioAssay records. Its purpose is primarily to drive the PubChem database summary record web pages, but can also be used independently as a programmatic web service. PUG View is mainly designed to provide complete summary reports on individual PubChem records. Users may also be interested in PUG REST (https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest-tutorial), a different style of service that gives smaller bits of information about one or more PubChem records.",
+                    "downloadURL": "https://pubchemdocs.ncbi.nlm.nih.gov/pug-view",
+                    "mediaType": "text/html",
                     "title": "View - PubChem Power User Gateway (PUG)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://pubchemdocs.ncbi.nlm.nih.gov/pug-soap",
-                    "description": "PUG SOAP is a web services access layer to PubChem functionality, and is an interface to PubChem\u2019s specialized search and analysis services \u2013 chemical structure searches, full record downloads, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "PUG SOAP is a web services access layer to PubChem functionality, and is an interface to PubChem\u2019s specialized search and analysis services \u2013 chemical structure searches, full record downloads, etc.",
+                    "downloadURL": "https://pubchemdocs.ncbi.nlm.nih.gov/pug-soap",
+                    "mediaType": "text/html",
                     "title": "SOAP - PubChem Power User Gateway (PUG)"
                 },
                 {
@@ -31268,41 +31249,41 @@
                     "title": "E-utilities API"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/84c4-vbci",
+            "issued": "2012-08-22",
+            "keyword": [
+                "api",
+                "biochemistry",
+                "chemistry",
+                "dataset"
+            ],
+            "landingPage": "https://pubchem.ncbi.nlm.nih.gov/pug/pughelp.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Molecular biology/Genetics"
-            ]
+            ],
+            "title": "PubChem Power User Gateway (PUG)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/refseq/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "computational biology",
-                "dataset",
-                "genetics",
-                "genomics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/v53t-3qjy",
             "description": "A comprehensive, integrated, non-redundant, well-annotated set of reference sequences including genomic, transcript, and protein.",
-            "title": "RefSeq: NCBI Reference Sequence Database",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31323,54 +31304,49 @@
                     "title": "RefSeq genomes FTP"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/refseq/rsg/",
-                    "description": "RefSeqGene defines genomic sequences to be used as reference standards for well-characterized genes and is part of the Locus Reference Genomic (LRG) Project.",
                     "@type": "dcat:Distribution",
+                    "description": "RefSeqGene defines genomic sequences to be used as reference standards for well-characterized genes and is part of the Locus Reference Genomic (LRG) Project.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/refseq/rsg/",
+                    "mediaType": "text/html",
                     "title": "RefSeqGene"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/v53t-3qjy",
+            "issued": "2021-08-26",
+            "keyword": [
+                "computational biology",
+                "dataset",
+                "genetics",
+                "genomics"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/refseq/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Molecular biology/Genetics"
-            ]
+            ],
+            "title": "RefSeq: NCBI Reference Sequence Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9t9r-e5a3",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-03",
-            "@type": "dcat:Dataset",
-            "temporal": "8/1/2020 - 5/3/2024",
-            "modified": "2024-10-18",
-            "keyword": [
-                "admissions",
-                "coronavirus",
-                "covid-19",
-                "hospital capacity",
-                "hospitalizations",
-                "icu beds",
-                "inpatient beds",
-                "ncezid",
-                "respiratory-virus-response"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DHQP",
                 "hasEmail": "mailto:nhsn@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9t9r-e5a3",
             "description": "<b>Note:</b> After May 3, 2024, this dataset will no longer be updated because hospitals are no longer required to report data on COVID-19 and influenza hospital admissions, hospital capacity, or occupancy data to HHS through CDC\u2019s National Healthcare Safety Network (NHSN). \n\nThis dataset represents hospitalization data and metrics aggregated to country, HHS region, and state/territory. Hospitalization data are reported to CDC\u2019s National Healthcare Safety Network, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN and included in this dataset represent aggregated counts and include metrics capturing information specific to hospital admissions, and inpatient and ICU bed capacity occupancy.\n\nData fields for new admissions of pediatric patients with confirmed COVID-19 for ages 0-4 years, 5-11 years, and 12-17 years were not required for reporting until February 2022; therefore, data for the following fields in this dataset begin on March 1, 2022 to account for delays in initial reporting of these fields:\n \nadm_00_04_covid_confirmed\navg_adm_00_04_covid_confirmed\navg_adm_00_04_covid_confirmed_per_100k\nadm_05_11_covid_confirmed\navg_adm_05_11_covid_confirmed\navg_adm_05_11_covid_confirmed_per_100k\nadm_12_17_covid_confirmed\navg_adm_12_17_covid_confirmed\navg_adm_12_17_covid_confirmed_per_100k\n\nUpdated weekly each Friday at noon, ET.",
-            "title": "Respiratory Virus Response (RVR) United States Hospitalization Metrics by Jurisdiction, Timeseries \u2013 ARCHIVED",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31393,48 +31369,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US, State/Territory, HHS Region",
+            "identifier": "https://data.cdc.gov/api/views/9t9r-e5a3",
+            "issued": "2023-11-03",
+            "keyword": [
+                "admissions",
+                "coronavirus",
+                "covid-19",
+                "hospital capacity",
+                "hospitalizations",
+                "icu beds",
+                "inpatient beds",
+                "ncezid",
+                "respiratory-virus-response"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9t9r-e5a3",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "No longer updated (dataset archived)",
+            "modified": "2024-10-18",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US, State/Territory, HHS Region",
+            "temporal": "8/1/2020 - 5/3/2024",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Respiratory Virus Response (RVR) United States Hospitalization Metrics by Jurisdiction, Timeseries \u2013 ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bfe6-2gyq",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "keyword": [
-                "2016",
-                "mmwr",
-                "mumps",
-                "nedss",
-                "netss",
-                "nndss",
-                "pertussis",
-                "rabies animal",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/bfe6-2gyq",
             "description": "NNDSS - Table II. Mumps to Rabies, animal - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.  The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.   NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n * Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n \u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions.",
-            "title": "NNDSS - Table II. Mumps to Rabies, animal",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31457,35 +31433,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bfe6-2gyq",
+            "issued": "2017-01-05",
+            "keyword": [
+                "2016",
+                "mmwr",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "pertussis",
+                "rabies animal",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bfe6-2gyq",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2017-01-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Mumps to Rabies, animal"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/unxy-rdyx",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division, Chemical and Biochemical Monitoring Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/unxy-rdyx",
             "description": "Measurement of vapors from solutions containing propylene glycol methyl ether (PGME) released inside a closed chamber were evaluated. Data used to quantify limits of detection, limits of quantification, bias, precision, and accuracy of Fourier Transform Infrared Spectroscopy (FTIR) measurements of vapors from 2.5 M PGME solutions are presented. The effects of ethanol as a component of the PGME solution were also evaluated. Liquid drops of PGME solutions and headspace vapors above PGME solutions were released to simulate leaks from Closed System Drug-Transfer Devices (CSTD)s. Using a calibration apparatus, an instrumental LOD of 0.25 ppmv and a LOQ of 0.8 ppmv were determined for PGME vapor. A LOD of 1.1 \u00b5L and a LOQ of 3.5 \u00b5L was determined for liquid aliquots of 2.5 M PGME solution released in the NIOSH chamber. Accurate quantitation of liquid leaks required complete evaporation of droplets. With the upper end of the usable quantitation range limited by slow evaporation of relatively large droplets and the lower end defined by the method LOQ, the method has a narrow quantitative range for liquid droplets. Displacement of 45 mL of vial headspace containing PGME vapor is the largest amount expected when using the draft NIOSH testing protocol. Release of an unfiltered 45 mL headspace aliquot within the NIOSH chamber was calculated to produce a concentration of 0.8 ppmv based on the Henry\u2019s constant, which is right at the instrumental LOQ.  Therefore, the sensitivity of the method was not adequate to determine leaks of PGME vapor from a headspace release through an air filtering CSTD when using the draft NIOSH testing protocols with an FTIR analyzer.",
-            "title": "Evaluation of Propylene Glycol Methyl Ether as a Potential Challenge Agent for Leak Detection of Liquid and Headspace from Closed System Drug Transfer Devices using Fourier Transform Infrared Spectroscopy",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31493,35 +31480,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/unxy-rdyx",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/unxy-rdyx",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Evaluation of Propylene Glycol Methyl Ether as a Potential Challenge Agent for Leak Detection of Liquid and Headspace from Closed System Drug Transfer Devices using Fourier Transform Infrared Spectroscopy"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ndit-r2zk",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division, Chemical and Biochemical Monitoring Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ndit-r2zk",
             "description": "Closed system drug-transfer devices (CSTDs) are devices which replace traditional needles, septa, and other connectors used for transferring hazardous drugs (HDs). NIOSH recommends using CSTDs to limit occupational exposure to hazardous materials and sharps when compounding and administering these drugs (NIOSH 2004). One of the engineering challenges associated with CSTDs is management of the headspace that is either compressed or displaced when transferring liquids in and out of drug vials. CSTD designs and components employing various technologies include creating a physical barrier to contain the displaced volume of air or filters to clean the displaced volume of air when transferring HD solutions. In 2015, NIOSH developed a protocol to test material containment of barrier type CSTDs (NIOSH 2015). NIOSH presented a plan to update the testing protocol so that it was applicable to both barrier and air cleaning types of CSTDs (NIOSH 2016). Both barrier type CSTDs and air cleaning type CSTDs may be susceptible to either liquid or headspace vapor leaks. Air-cleaning type CSTDs allow free passage of air but are expected to remove semi-volatile hazardous drugs (HD)s from the exiting airstream. Barrier type CSTDs have been designed to contain air rather than clean it, and it is reasonable to conclude that a headspace leak with a barrier type CSTD would contain the drug at the same concentration as the headspace inside the vial. As a result, the procedure described in this paper can adequately assess the efficacy of barrier type CSTDs based on the volume of liquid and headspace vapor leak measured. However, the volatile compounds used in this procedure will readily pass through an air-cleaning CSTD, regardless of the ability to retain a semi-volatile HD. Therefore, testing the efficacy of an air-cleaning CSTD requires coupling the procedure described herein with an assessment of the ability of air cleaning CSTDs to retain an appropriate semi-volatile surrogate when volumes of headspace containing that surrogate are passed through the CSTDs. The difference in the amount of HD contained in liquid versus headspace vapor leaks may be several orders of magnitude. The work presented herein is a test method that can distinguish the origin and volumetric quantity of liquid and headspace vapor leaked.\n\nCSTD evaluation involves operation of CSTDs during normal use tasks, such as transferring a solution between two drug vials (NIOSH 2015). A test solution containing two volatile organic compounds (VOCs), acetone and methyl t-butyl ether (MTBE), was used in the evaluation. Leaks were measured by detecting the VOCs in a glove chamber using Selected Ion Flow Tube Mass Spectrometry (SIFT-MS) as the detector. Liquid and headspace leaks are differentiated by the ratios of the two VOCs measured as a result of leaks from the CSTD. The compounds, acetone and MTBE, at equal concentrations in a test solution have a concentration ratio in the headspace vapor of the test solution that is very different, as predicted by their Henry\u2019s constants. The ratio of acetone to MTBE detected in the glove chamber can be used to elucidate the source, liquid or headspace, and the magnitude of a leak. The analytical strategy is similar to stable isotope mixing models used to determine contributions from various sources by measuring isotopic ratios (Phillips and Gregg 2001). Propylene glycol (PG) was included in the testing solution as a surrogate for a HD component, though it was not quantified. Fluorescein was included as a visual qualitative indicator of a liquid leak location. SIFT-MS offers low limits of detection and real-time response. The real-time response has the benefit of enabling leaks to be temporally correlated with tasks involving manipulation of CSTD components.",
-            "title": "Source Apportionment and Quantification of Liquid and Headspace Leaks from Closed System Transfer Devices via Selected Ion Flow Tube Mass Spectrometry (SIFT-MS)",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31529,20 +31516,46 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ndit-r2zk",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/ndit-r2zk",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Source Apportionment and Quantification of Liquid and Headspace Leaks from Closed System Transfer Devices via Selected Ion Flow Tube Mass Spectrometry (SIFT-MS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2012",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.</p>\n<p>A sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.</p>\n<p>TEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".</p>\n<p>Variables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).</p>\n<p>Substances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.</p>\n<p>Created variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.<br />\nThis study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2012) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2012-nid13587",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2012-nid13587"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2012-nid13587",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -31555,41 +31568,40 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2012",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2012-nid13587",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.</p>\n<p>A sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.</p>\n<p>TEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".</p>\n<p>Variables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).</p>\n<p>Substances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.</p>\n<p>Created variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.<br />\nThis study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2012)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2012-nid13587",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2012) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2012-nid13587"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2012)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.ahrq.gov/data/innovations/syh-dr.html",
             "bureauCode": [
                 "009:00"
             ],
-            "rights": "AHRQ approval is required for access to SyH-DR. To request access to SyH-DR, follow the steps included in the\u00a0Getting Started Guide\u00a0and submit the required application form and\u00a0data use agreement. Completed applications will be reviewed by AHRQ.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "SyH-DR help desk",
+                "hasEmail": "mailto:SyH-DR@ahrq.hhs.gov"
+            },
+            "description": "The Agency for Healthcare Research and Quality (AHRQ) created SyH-DR from eligibility and claims files for Medicare, Medicaid, and commercial insurance plans in calendar year 2016. SyH-DR contains data from a nationally representative sample of insured individuals for the 2016 calendar year. SyH-DR uses synthetic data elements at the claim level to resemble the marginal distribution of the original data elements. SyH-DR person-level data elements are not synthetic, but identifying information is aggregated or masked.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The Synthetic Healthcare Database for Research (SyH-DR) is an all-payer, nationally representative claims database. The database consists of a sample of inpatient, outpatient, and prescription drug claims, including utilization, payment, and enrollment data, for people insured by Medicare, Medicaid, or commercial health insurance in 2016. AHRQ created SyH-DR, in part, as a resource to facilitate improvements to price and quality transparency in healthcare.\n\nSyH-DR is a synthetic database that replicates the structure and statistical properties of the original claims data while protecting privacy and confidentiality of people and institutions. Synthetic data are created by statistically modeling or changing original data so that new values or data elements are generated while maintaining the original data's statistical properties. Additional steps, such as masking, are taken to reduce the risk of identifying people and institutions so that the data may be made publicly available to a broad community of researchers.                                                                                                                                                                                   AHRQ approval is required for access to SyH-DR. User must submit an application and\u00a0data use agreement. ",
+                    "downloadURL": "https://www.ahrq.gov/data/innovations/syh-dr.html",
+                    "mediaType": "text/html",
+                    "title": "\u00a0Synthetic Healthcare Database for Research (SyH-DR)"
+                }
+            ],
+            "identifier": "https://healthdata.gov/api/views/88gj-w5in",
             "issued": "2023-09-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-15",
             "keyword": [
                 "all payer claims",
                 "all payer claims database",
@@ -31599,113 +31611,80 @@
                 "linked medicare files",
                 "synthetic data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "SyH-DR help desk",
-                "hasEmail": "mailto:SyH-DR@ahrq.hhs.gov"
-            },
+            "landingPage": "https://www.ahrq.gov/data/innovations/syh-dr.html",
+            "modified": "2023-09-15",
+            "programCode": [
+                "009:074"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Agency for Healthcare Research and Quality"
             },
-            "identifier": "https://healthdata.gov/api/views/88gj-w5in",
-            "description": "The Agency for Healthcare Research and Quality (AHRQ) created SyH-DR from eligibility and claims files for Medicare, Medicaid, and commercial insurance plans in calendar year 2016. SyH-DR contains data from a nationally representative sample of insured individuals for the 2016 calendar year. SyH-DR uses synthetic data elements at the claim level to resemble the marginal distribution of the original data elements. SyH-DR person-level data elements are not synthetic, but identifying information is aggregated or masked.",
-            "title": "\u00a0Synthetic Healthcare Database for Research (SyH-DR)",
-            "programCode": [
-                "009:074"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ahrq.gov/data/innovations/syh-dr.html",
-                    "description": "The Synthetic Healthcare Database for Research (SyH-DR) is an all-payer, nationally representative claims database. The database consists of a sample of inpatient, outpatient, and prescription drug claims, including utilization, payment, and enrollment data, for people insured by Medicare, Medicaid, or commercial health insurance in 2016. AHRQ created SyH-DR, in part, as a resource to facilitate improvements to price and quality transparency in healthcare.\n\nSyH-DR is a synthetic database that replicates the structure and statistical properties of the original claims data while protecting privacy and confidentiality of people and institutions. Synthetic data are created by statistically modeling or changing original data so that new values or data elements are generated while maintaining the original data's statistical properties. Additional steps, such as masking, are taken to reduce the risk of identifying people and institutions so that the data may be made publicly available to a broad community of researchers.                                                                                                                                                                                   AHRQ approval is required for access to SyH-DR. User must submit an application and\u00a0data use agreement. ",
-                    "@type": "dcat:Distribution",
-                    "title": "\u00a0Synthetic Healthcare Database for Research (SyH-DR)"
-                }
-            ],
+            "rights": "AHRQ approval is required for access to SyH-DR. To request access to SyH-DR, follow the steps included in the\u00a0Getting Started Guide\u00a0and submit the required application form and\u00a0data use agreement. Completed applications will be reviewed by AHRQ.",
             "spatial": "United States",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "\u00a0Synthetic Healthcare Database for Research (SyH-DR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/88mm-fzse",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-06",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-10",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "e9aa0d65-4e3e-5872-be66-c2edd3447f24",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet filters v2.10.64 (coreset-dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/filters.csv",
-                    "description": "CoreSet filters v2.10.64 (coreset-dev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet filters v2.10.64 (coreset-dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet filters v2.10.64 (coreset-dev)"
                 }
             ],
+            "identifier": "e9aa0d65-4e3e-5872-be66-c2edd3447f24",
+            "issued": "2024-11-06",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/88mm-fzse",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2025-01-10",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSet filters v2.10.64 (coreset-dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/oralhealth/about/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-27",
-            "keyword": [
-                "community water fluoridation",
-                "county level",
-                "fluoridation",
-                "oral health",
-                "state level",
-                "wfrs"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Oral Health Inquiries",
                 "hasEmail": "mailto:oralhealth@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hgyx-uuxz",
             "description": "State, 2016 \u20132020; County, 2020. The report includes both state and county level water fluoridation data generated from the Water Fluoridation Reporting System (WFRS). State level statistics include data from the biennial report originally published at https://www.cdc.gov/fluoridation/statistics/reference_stats.htm. State and county data include percentage of people, number of people, and number of water systems receiving fluoridated water. County level data is not displayed for all states. Participation in sharing county level data is voluntary and state programs determine if data will be shown.",
-            "title": "Community Water Fluoridation \u2013 State and County Level Statistics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31728,82 +31707,90 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hgyx-uuxz",
+            "issued": "2023-07-18",
+            "keyword": [
+                "community water fluoridation",
+                "county level",
+                "fluoridation",
+                "oral health",
+                "state level",
+                "wfrs"
+            ],
+            "landingPage": "https://www.cdc.gov/oralhealth/about/index.htm",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-09-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Oral Health"
-            ]
+            ],
+            "title": "Community Water Fluoridation \u2013 State and County Level Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/88t6-f6cq",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-06",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "98ff950b-2dc6-592e-bbc2-56be79cb2841",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt measure v2.10.14 (coreset-dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.14/20241029/measure.csv",
-                    "description": "CoreSEt measure v2.10.14 (coreset-dev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt measure v2.10.14 (coreset-dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.14/20241029/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt measure v2.10.14 (coreset-dev)"
                 }
             ],
+            "identifier": "98ff950b-2dc6-592e-bbc2-56be79cb2841",
+            "issued": "2024-11-06",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/88t6-f6cq",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-11-06",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSEt measure v2.10.14 (coreset-dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/3rge-nu2a",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-21",
-            "temporal": "April 4, 2021-September 24, 2022",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vaccine Breakthrough Unit, Surveillance and Analytics Team",
                 "hasEmail": "mailto:vbtsurveillance@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/3rge-nu2a",
             "description": "Data for CDC\u2019s COVID Data Tracker site on Rates of COVID-19 Cases and Deaths by Vaccination Status.\nClick 'More' for important dataset description and footnotes\n\nDataset and data visualization details:\nThese data were posted on October 21, 2022, archived on November 18, 2022, and revised on February 22, 2023. These data reflect cases among persons with a positive specimen collection date through September 24, 2022, and deaths among persons with a positive specimen collection date through September 3, 2022. \n\nVaccination status: A person vaccinated with a primary series had SARS-CoV-2 RNA or antigen detected on a respiratory specimen collected \u226514 days after verifiably completing the primary series of an FDA-authorized or approved COVID-19 vaccine. An unvaccinated person had SARS-CoV-2 RNA or antigen detected on a respiratory specimen and has not been verified to have received COVID-19 vaccine. Excluded were partially vaccinated people who received at least one FDA-authorized vaccine dose but did not complete a primary series \u226514 days before collection of a specimen where SARS-CoV-2 RNA or antigen was detected.\nAdditional or booster dose: A person vaccinated with a primary series and an additional or booster dose had SARS-CoV-2 RNA or antigen detected on a respiratory specimen collected \u226514 days after receipt of an additional or booster dose of any COVID-19 vaccine on or after August 13, 2021. For people ages 18 years and older, data are graphed starting the week including September 24, 2021, when a COVID-19 booster dose was first recommended by CDC for adults 65+ years old and people in certain populations and high risk occupational and institutional settings. For people ages 12-17 years, data are graphed starting the week of December 26, 2021, 2 weeks after the first recommendation for a booster dose for adolescents ages 16-17 years. For people ages 5-11 years, data are included starting the week of June 5, 2022, 2 weeks after the first recommendation for a booster dose for children aged 5-11 years. For people ages 50 years and older, data on second booster doses are graphed starting the week including March 29, 2022, when the recommendation was made for second boosters. Vertical lines represent dates when changes occurred in U.S. policy for COVID-19 vaccination (details provided above). Reporting is by primary series vaccine type rather than additional or booster dose vaccine type. The booster dose vaccine type may be different than the primary series vaccine type. \n** Because data on the immune status of cases and associated deaths are unavailable, an additional dose in an immunocompromised person cannot be distinguished from a booster dose. This is a relevant consideration because vaccines can be less effective in this group.\nDeaths: A COVID-19\u2013associated death occurred in a person with a documented COVID-19 diagnosis who died; health department staff reviewed to make a determination using vital records, public health investigation, or other data sources. Rates of COVID-19 deaths by vaccination status are reported based on when the patient was tested for COVID-19, not the date they died. Deaths usually occur up to 30 days after COVID-19 diagnosis.\nParticipating jurisdictions: Currently, these 31 health departments that regularly link their case surveillance to immunization information system data are included in these incidence rate estimates: Alabama, Arizona, Arkansas, California, Colorado, Connecticut, District of Columbia, Florida, Georgia, Idaho, Indiana, Kansas, Kentucky, Louisiana, Massachusetts, Michigan, Minnesota, Nebraska, New Jersey, New Mexico, New York, New York City (New York), North Carolina, Philadelphia (Pennsylvania), Rhode Island, South Dakota, Tennessee, Texas, Utah, Washington, and West Virginia; 30 jurisdictions also report deaths among vaccinated and unvaccinated people. These jurisdictions represent 72% of the total U.S. population and all ten of the Health and Human Services Regions. Data on cases",
-            "title": "Rates of COVID-19 Cases or Deaths by Age Group and Vaccination Status",
-            "programCode": [
-                "009:038"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31826,50 +31813,41 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Select US Jurisdictions",
+            "identifier": "https://data.cdc.gov/api/views/3rge-nu2a",
+            "issued": "2022-01-21",
+            "landingPage": "https://data.cdc.gov/d/3rge-nu2a",
+            "language": [
+                "English"
+            ],
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2023-07-20",
+            "programCode": [
+                "009:038"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "Select US Jurisdictions",
+            "temporal": "April 4, 2021-September 24, 2022",
             "theme": [
                 "Public Health Surveillance"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Rates of COVID-19 Cases or Deaths by Age Group and Vaccination Status"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/v2pi-w3up",
+            "accrualPeriodicity": "On a continuous basis",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2020-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-10",
-            "references": [
-                "https://www.cms.gov/files/document/Accelerated-and-Advanced-Payments-Fact-Sheet.pdf"
-            ],
-            "keyword": [
-                "accelerated and advance payments",
-                "cares act",
-                "coronavirus",
-                "covid-19",
-                "provider relief fund"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Megan Worstell",
                 "hasEmail": "mailto:HIGLASServiceDesk@gdit.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/v2pi-w3up",
             "description": "We are releasing data that compares the HHS Provider Relief Fund and the CMS Accelerated and Advance Payments by State and provider as of May 15, 2020.  This data is already available on other websites, but this chart brings the information together into one view for comparison.  You can find additional information on the Accelerated and Advance Payments at the following links: \n\nFact Sheet: https://www.cms.gov/files/document/Accelerated-and-Advanced-Payments-Fact-Sheet.pdf; \n\nZip file on providers in each state: https://www.cms.gov/files/zip/accelerated-payment-provider-details-state.zip\n\nMedicare Accelerated and Advance Payments State-by-State information and by Provider Type: https://www.cms.gov/files/document/covid-accelerated-and-advance-payments-state.pdf.\n\nThis file was assembled by HHS via CMS, HRSA and reviewed by leadership and compares the HHS Provider Relief Fund and the CMS Accelerated and Advance Payments by State and provider as of December 4, 2020.  \n\nHHS Provider Relief Fund \nPresident Trump is providing support to healthcare providers fighting the coronavirus disease 2019 (COVID-19) pandemic through the bipartisan Coronavirus Aid, Relief, & Economic Security Act and the Paycheck Protection Program and Health Care Enhancement Act, which provide a total of $175 billion for relief funds to hospitals and other healthcare providers on the front lines of the COVID-19 response. This funding supports healthcare-related expenses or lost revenue attributable to COVID-19 and ensures uninsured Americans can get treatment for COVID-19. HHS is distributing this Provider Relief Fund money and these payments do not need to be repaid.\nThe Department allocated $50 billion of the Provider Relief Fund for general distribution to Medicare facilities and providers impacted by COVID-19, based on eligible providers' net reimbursement. It allocated another $22 billion to providers in areas particularly impacted by the COVID-19 outbreak, rural providers, and providers who serve low-income populations and uninsured Americans.  HHS will be allocating the remaining funds in the near future.\n  \nAs part of the Provider Relief Fund distribution, all providers have 45 days to attest that they meet certain criteria to keep the funding they received, including public disclosure.  As of May 15, 2020, there has been a total of $34 billion in attested payments.  The chart only includes those providers that have attested to the payments by that date.  We will continue to update this information and add the additional providers and payments once their attestation is complete. \n\nCMS Accelerated and Advance Payments Program\nOn March 28, 2020, to increase cash flow to providers of services and suppliers impacted by the coronavirus disease 2019 (COVID-19) pandemic, the Centers for Medicare & Medicaid Services (CMS) expanded the Accelerated and Advance Payment Program to a broader group of Medicare Part A providers and Part B suppliers. Beginning on April 26, 2020, CMS stopped accepting new applications for the Advance Payment Program, and CMS began reevaluating all pending and new applications for Accelerated Payments in light of the availability of direct payments made through HHS\u2019s Provider Relief Fund.\n\nSince expanding the AAP program on March 28, 2020, CMS approved over 21,000 applications totaling $59.6 billion in payments to Part A providers, which includes hospitals, through May 18, 2020. For Part B suppliers\u2014including doctors, non-physician practitioners and durable medical equipment suppliers\u2014 during the same time period, CMS approved almost 24,000 applications advancing $40.4 billion in payments. The AAP program is not a grant, and providers and suppliers are required to repay the loan.\n\nCMS has published AAP data, as required by the Continuing Appropriations and Other Extensions Act of 2021, on this website: https://www.cms.gov/files/document/covid-medicare-accelerated-and-advance-payments-program-covid-19-public-health-emergency-payment.pdf",
-            "title": "Provider Relief Fund & Accelerated and Advance Payments",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31892,22 +31870,55 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/v2pi-w3up",
+            "issued": "2020-05-21",
+            "keyword": [
+                "accelerated and advance payments",
+                "cares act",
+                "coronavirus",
+                "covid-19",
+                "provider relief fund"
+            ],
+            "landingPage": "https://data.cdc.gov/d/v2pi-w3up",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "On a continuous basis",
+            "modified": "2024-07-10",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cms.gov/files/document/Accelerated-and-Advanced-Payments-Fact-Sheet.pdf"
+            ],
+            "spatial": "US",
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "Provider Relief Fund & Accelerated and Advance Payments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/3ahs-wye3",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "description": "Download the latest version of the Glossary and Methodology.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/3ahs-wye3/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/3ahs-wye3",
             "issued": "2017-08-23",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
             "keyword": [
                 "adult",
                 "age",
@@ -31943,60 +31954,34 @@
                 "tobacco use",
                 "user"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "OSHData Support",
-                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/3ahs-wye3",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/3ahs-wye3",
-            "description": "Download the latest version of the Glossary and Methodology.",
-            "title": "National Adult Tobacco Survey (NATS) Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/download/3ahs-wye3/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
             "theme": [
                 "Survey Data"
-            ]
+            ],
+            "title": "National Adult Tobacco Survey (NATS) Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/8aa7-7ry6",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-10-26",
-            "@type": "dcat:Dataset",
-            "modified": "2021-10-26",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "c1428b7a-16de-4bfb-88c3-6e2d9be2c9cb",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20211018 to 20211024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32004,45 +31989,36 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "c1428b7a-16de-4bfb-88c3-6e2d9be2c9cb",
+            "issued": "2021-10-26",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/8aa7-7ry6",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2021-10-26",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20211018 to 20211024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/BRFSS/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-14",
-            "references": [
-                "http://www.cdc.gov/BRFSS/"
-            ],
-            "keyword": [
-                "age-adjusted",
-                "behavioral",
-                "brfss",
-                "factor",
-                "risk",
-                "surveillance",
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
-            "identifier": "https://data.cdc.gov/api/views/at7e-uhkc",
+            "describedBy": "https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factors-Selected-Metropolitan-Area/at7e-uhkc",
             "description": "2011 to present. BRFSS SMART MMSA age-adjusted prevalence combined land line and cell phone data. The Selected Metropolitan Area Risk Trends (SMART) project uses the Behavioral Risk Factor Surveillance System (BRFSS) to analyze the data of selected metropolitan statistical areas (MMSAs) with 500 or more respondents. BRFSS data can be used to identify emerging health problems, establish and track health objectives, and develop and evaluate public health policies and programs. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Data will be updated annually as it becomes available. Detailed information on sampling methodology and quality assurance can be found on the BRFSS website (http://www.cdc.gov/brfss). Methodology: http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf Glossary:  https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct",
-            "title": "Behavioral Risk Factors: Selected Metropolitan Area Risk Trends (SMART) MMSA Age-adjusted Prevalence Data (2011 to Present)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32065,50 +32041,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factors-Selected-Metropolitan-Area/at7e-uhkc",
+            "identifier": "https://data.cdc.gov/api/views/at7e-uhkc",
+            "issued": "2023-07-19",
+            "keyword": [
+                "age-adjusted",
+                "behavioral",
+                "brfss",
+                "factor",
+                "risk",
+                "surveillance",
+                "survey"
+            ],
+            "landingPage": "http://www.cdc.gov/BRFSS/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-14",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "http://www.cdc.gov/BRFSS/"
+            ],
             "theme": [
                 "Behavioral Risk Factors"
-            ]
+            ],
+            "title": "Behavioral Risk Factors: Selected Metropolitan Area Risk Trends (SMART) MMSA Age-adjusted Prevalence Data (2011 to Present)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/medicare-current-beneficiary-survey-mcbs/medicare-current-beneficiary-survey-cost-supplement",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-01-19",
-            "temporal": "2018-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2025-01/CSPUF2022_DUG.pdf"
-            ],
-            "keyword": [
-                "health equity",
-                "medicare",
-                "medicare advantage",
-                "medicare prescription drug",
-                "national",
-                "original medicare",
-                "patient experience"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicare Current Beneficiary Survey - OEDA",
                 "hasEmail": "mailto:MCBS@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/91ded8c4-7e64-42ff-a595-4a4eb55df910/data-viewer",
-            "description": "The Medicare Current Beneficiary Survey (MCBS) - Cost Supplement File Microdata Public Use File (PUF) dataset provides information on expenditures and payment sources for all services used by Medicare beneficiaries, including co-payments, deductibles, and non-covered services.",
-            "title": "Medicare Current Beneficiary Survey - Cost Supplement",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2025-01/CSPUF2022_Codebook.txt",
             "describedByType": "text/plain",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Medicare Current Beneficiary Survey (MCBS) - Cost Supplement File Microdata Public Use File (PUF) dataset provides information on expenditures and payment sources for all services used by Medicare beneficiaries, including co-payments, deductibles, and non-covered services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32141,26 +32118,75 @@
                     "title": "Medicare Current Beneficiary Survey - Cost Supplement : 2018-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2025-01/CSPUF2022_Codebook.txt",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/91ded8c4-7e64-42ff-a595-4a4eb55df910/data-viewer",
+            "issued": "2023-01-19",
+            "keyword": [
+                "health equity",
+                "medicare",
+                "medicare advantage",
+                "medicare prescription drug",
+                "national",
+                "original medicare",
+                "patient experience"
+            ],
+            "landingPage": "https://data.cms.gov/medicare-current-beneficiary-survey-mcbs/medicare-current-beneficiary-survey-cost-supplement",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2025-01/CSPUF2022_DUG.pdf"
+            ],
+            "temporal": "2018-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Current Beneficiary Survey - Cost Supplement"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5fyu-rtk3",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "NNDSS - Table I. infrequently reported notifiable diseases - 2018. In this Table, provisional cases of selected infrequently reported notifiable diseases (<1,000 cases reported during the preceding year) are displayed.  This tables excludes U.S. territories.\n\nNotice:  The case counts for Haemophilus influenzae, invasive disease Nontypeable\" and \"Non-b serotype\" were switched for 2018 weeks 1-52.\n\nNote:\nThese are provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia are collated and published weekly on the NNDSS Data and Statistic web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\n\nFootnote:\n\u2014: No reported cases. N: Not reportable. NA: Not available. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. \n\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.  \n\n\u2020 This table does not include cases from the U.S. territories. \n\n\u00a7 Calculated by summing the incidence counts for the current week, the 2 weeks preceding the current week, and the 2 weeks following the current week, for a total of 5 preceding years. Additional information is available at https://wwwn.cdc.gov/nndss/document/5yearweeklyaverage.pdf.\n\n\u00b6 Not reportable in all jurisdictions. Data from states where the condition is not reportable are excluded from this table, except for the arboviral diseases and influenza-associated pediatric mortality. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.\n\n** Please refer to the CDC WONDER for weekly updates to the footnote for this condition.   \n\n\u2020\u2020 Please refer to the CDC WONDER for weekly updates to the footnote for this condition.  \n\n\u00a7\u00a7 Novel influenza A virus infections are human infections with influenza A viruses that are different from currently circulating human seasonal influenza viruses. With the exception of one avian lineage influenza A (H7N2) virus, all novel influenza A virus infections reported to CDC since 2013 have been variant influenza viruses.\n\n\u00b6\u00b6 Prior to 2018, cases of paratyphoid fever were included with salmonellosis cases (see Table II). \n\n*** Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers'. NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5fyu-rtk3/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5fyu-rtk3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5fyu-rtk3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5fyu-rtk3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/5fyu-rtk3",
             "issued": "2019-02-12",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-20",
             "keyword": [
                 "2018",
                 "acute",
@@ -32245,83 +32271,33 @@
                 "wonder",
                 "yellow fever"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CDC INFO",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5fyu-rtk3",
-            "description": "NNDSS - Table I. infrequently reported notifiable diseases - 2018. In this Table, provisional cases of selected infrequently reported notifiable diseases (<1,000 cases reported during the preceding year) are displayed.  This tables excludes U.S. territories.\n\nNotice:  The case counts for Haemophilus influenzae, invasive disease Nontypeable\" and \"Non-b serotype\" were switched for 2018 weeks 1-52.\n\nNote:\nThese are provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia are collated and published weekly on the NNDSS Data and Statistic web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\n\nFootnote:\n\u2014: No reported cases. N: Not reportable. NA: Not available. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. \n\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.  \n\n\u2020 This table does not include cases from the U.S. territories. \n\n\u00a7 Calculated by summing the incidence counts for the current week, the 2 weeks preceding the current week, and the 2 weeks following the current week, for a total of 5 preceding years. Additional information is available at https://wwwn.cdc.gov/nndss/document/5yearweeklyaverage.pdf.\n\n\u00b6 Not reportable in all jurisdictions. Data from states where the condition is not reportable are excluded from this table, except for the arboviral diseases and influenza-associated pediatric mortality. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.\n\n** Please refer to the CDC WONDER for weekly updates to the footnote for this condition.   \n\n\u2020\u2020 Please refer to the CDC WONDER for weekly updates to the footnote for this condition.  \n\n\u00a7\u00a7 Novel influenza A virus infections are human infections with influenza A viruses that are different from currently circulating human seasonal influenza viruses. With the exception of one avian lineage influenza A (H7N2) virus, all novel influenza A virus infections reported to CDC since 2013 have been variant influenza viruses.\n\n\u00b6\u00b6 Prior to 2018, cases of paratyphoid fever were included with salmonellosis cases (see Table II). \n\n*** Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers'. NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
-            "title": "NNDSS - Table I. infrequently reported notifiable diseases",
+            "landingPage": "https://data.cdc.gov/d/5fyu-rtk3",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2020-03-20",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/5fyu-rtk3/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/5fyu-rtk3/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/5fyu-rtk3/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/5fyu-rtk3/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table I. infrequently reported notifiable diseases"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ju63-2fep",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-28",
-            "keyword": [
-                "2021",
-                "anthrax",
-                "arboviral diseases",
-                "chikungunya virus disease",
-                "eastern equine encephalitis virus disease",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ju63-2fep",
             "description": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32344,38 +32320,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ju63-2fep",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "anthrax",
+                "arboviral diseases",
+                "chikungunya virus disease",
+                "eastern equine encephalitis virus disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ju63-2fep",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-01-28",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/8bit-b38v",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-01-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-08",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "b3619ac3-3c2c-4db4-b6fe-4e701d513df6",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-01-to-2024-01-07",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32384,19 +32369,47 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-01-to-2024-01-07"
                 }
             ],
+            "identifier": "b3619ac3-3c2c-4db4-b6fe-4e701d513df6",
+            "issued": "2024-01-10",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/8bit-b38v",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-01-08",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-01-to-2024-01-07"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-mortality-multiple-cause-death",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/mcd.html",
+            "description": "<p>The Mortality - Multiple Cause of Death data on CDC WONDER are county-level national mortality and population data spanning the years 1999-2009. Data are based on death certificates for U.S. residents. Each death certificate contains a single underlying cause of death, up to twenty additional multiple causes (Boolean set analysis), and demographic data. The number of deaths, crude death rates, age-adjusted death rates, standard errors and 95% confidence intervals for death rates can be obtained by place of residence (total U.S., region, state, and county), age group (including infants and single-year-of-age cohorts), race (4 groups), Hispanic ethnicity, gender, year of death, and cause-of-death (4-digit ICD-10 code or group of codes, injury intent and mechanism categories, or drug and alcohol related causes), year, month and week day of death, place of death and whether an autopsy was performed. The data are produced by the National Center for Health Statistics.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "http://wonder.cdc.gov/mcd.html",
+                    "format": "API",
+                    "title": "API "
+                }
+            ],
+            "identifier": "516a8229-7208-4df5-987e-24ba926077a7",
             "issued": "2012-08-03",
-            "temporal": "1999-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "age",
                 "births",
@@ -32416,72 +32429,35 @@
                 "state",
                 "urbanization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-mortality-multiple-cause-death",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "516a8229-7208-4df5-987e-24ba926077a7",
-            "description": "<p>The Mortality - Multiple Cause of Death data on CDC WONDER are county-level national mortality and population data spanning the years 1999-2009. Data are based on death certificates for U.S. residents. Each death certificate contains a single underlying cause of death, up to twenty additional multiple causes (Boolean set analysis), and demographic data. The number of deaths, crude death rates, age-adjusted death rates, standard errors and 95% confidence intervals for death rates can be obtained by place of residence (total U.S., region, state, and county), age group (including infants and single-year-of-age cohorts), race (4 groups), Hispanic ethnicity, gender, year of death, and cause-of-death (4-digit ICD-10 code or group of codes, injury intent and mechanism categories, or drug and alcohol related causes), year, month and week day of death, place of death and whether an autopsy was performed. The data are produced by the National Center for Health Statistics.</p>",
-            "title": "CDC WONDER: Mortality - Multiple Cause of Death",
-            "programCode": [
-                "009:048"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "http://wonder.cdc.gov/mcd.html",
-                    "format": "API",
-                    "title": "API "
-                }
-            ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/mcd.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1999-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
             "theme": [
                 "Health",
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Mortality - Multiple Cause of Death"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9axm-gjt8",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "dengue",
-                "dengue-like illness",
-                "dengue virus infections",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9axm-gjt8",
             "description": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32504,40 +32480,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9axm-gjt8",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "dengue",
+                "dengue-like illness",
+                "dengue virus infections",
+                "nedss",
+                "netss",
+                "nndss",
+                "severe dengue",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9axm-gjt8",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/njmz-dpbc",
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
-                "covid-19"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Surveillance Review and Response Group",
                 "hasEmail": "mailto:eocevent394@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/njmz-dpbc",
             "description": "Reporting of Aggregate Case and Death Count data was discontinued on May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. Although these data will continue to be publicly available, this dataset will no longer be updated.\n\nThe surveillance case definition for COVID-19, a nationally notifiable disease, was first described in a <a href=\"https://ndc.services.cdc.gov/case-definitions/coronavirus-disease-2019-2021/\">position statement</a> from the Council for State and Territorial Epidemiologists, which was later <a href=\"https://ndc.services.cdc.gov/case-definitions/coronavirus-disease-2019-covid-19/\">revised</a>. However, there is some variation in how jurisdictions implemented these case definitions. More information on how CDC collects COVID-19 case surveillance data can be found at <a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html\">FAQ: COVID-19 Data and Surveillance</a>.\n\n<b>Aggregate Data Collection Process</b>\nSince the beginning of the COVID-19 pandemic, data were reported from state and local health departments through a robust process with the following steps:\n<ul><li>Aggregate county-level counts were obtained indirectly, via automated overnight web collection, or directly, via a data submission process.</li><li>If more than one official county data source existed, CDC used a comprehensive data selection process comparing each official county data source to retrieve the highest case and death counts, unless otherwise specified by the state.</li><li>A CDC data team reviewed counts for congruency prior to integration and set up alerts to monitor for discrepancies in the data.</li><li>CDC routinely compiled these data and post the finalized information on COVID Data Tracker.</li><li>County level data were aggregated to obtain state- and territory- specific totals.</li><li>Counting of cases and deaths is based on date of report and not on the date of symptom onset. CDC calculates rates in these data by using population estimates provided by the US Census Bureau Population Estimates Program (2019 Vintage).</li><li>COVID-19 aggregate case and death data are organized in a time series that includes cumulative number of cases and deaths as reported by a jurisdiction on a given date.  New case and death counts are calculated as the week-to-week change in cumulative counts of cases and deaths reported (i.e., newly reported cases and deaths = cumulative number of cases/deaths reported this week minus the cumulative total reported the prior week.</li></ul>\n\nThis process was collaborative, with CDC and jurisdictions working together to ensure the accuracy of COVID-19 case and death numbers. County counts provided the most up-to-date numbers on cases and deaths by report date. Throughout data collection, CDC retrospectively updated counts to correct known data quality issues.\n\n<b>Description</b>\nThis archived public use dataset focuses on the cumulative and weekly case and death rates per 100,000 persons within various sociodemographic factors across all states and their counties. All resulting data are expressed as rates calculated as the number of cases or deaths per 100,000 persons in counties meeting various classification criteria using <a href=\"https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html\">the US Census Bureau Population Estimates Program</a> (2019 Vintage).\n\nEach county within jurisdictions is classified into multiple categories for each factor. All rates in this dataset are based on classification of counties by the characteristics of their population, not individual-level factors.  This applies to each of the available factors observed in this dataset. Specific factors and their corresponding categories are detailed below.\n\n<b>Population-level factors</b>\nEach unique population factor is detailed below. Please note that the \u201cClassification\u201d column describes each of the 12 factors in the dataset, including a data dict",
-            "title": "Trends in COVID-19 Cases and Deaths in the United States, by County-level Population Factors - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32560,40 +32543,37 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/njmz-dpbc",
+            "issued": "2023-06-06",
+            "keyword": [
+                "covid",
+                "covid-19"
+            ],
+            "landingPage": "https://data.cdc.gov/d/njmz-dpbc",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "No longer updated (dataset archived)"
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2020-01-22/2023-05-10",
+            "title": "Trends in COVID-19 Cases and Deaths in the United States, by County-level Population Factors - ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ujra-cbx5",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-05-29",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-07",
-            "keyword": [
-                "air pollution",
-                "asthma",
-                "environmental health",
-                "particulate matter",
-                "pm2.5"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Craig Kassinger",
                 "hasEmail": "mailto:cak8@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ujra-cbx5",
             "description": "This dataset provides modeled predictions of PM2.5 levels from the EPA's Downscaler model. Data are at the census tract level for 2006-2010. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\n\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\n\nBy using these data, you signify your agreement to comply with the following requirements:\n1. Use the data for statistical reporting and analysis only.\n2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals.\n3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov.\n4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.\n5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC.\n6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2006-2010",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32616,22 +32596,54 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ujra-cbx5",
+            "issued": "2020-05-29",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "particulate matter",
+                "pm2.5"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ujra-cbx5",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2021-07-07",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Environmental Health & Toxicology"
-            ]
+            ],
+            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2006-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/ahcd/about_ahcd.htm",
+            "accrualPeriodicity": "Survey has ended. 2022 data will be released Summer 2024.",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training, and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "For the survey, findings are based on a national sample of visits to emergency departments (EDs) in noninstitutional general and short-stay hospitals, exclusive of Federal, military, and Veterans Administration hospitals, located in the 50 States and the District of Columbia. The sampling frame for the 2021 NHAMCS was constructed from IQVIA\u2019s database. A three-stage probability sampling design is used. The first stage consists of a sample of geographically defined areas also known as Primary Sampling Units (PSU). In the second stage, is of hospitals within those PSU and all emergency service areas within the emergency department are selected. Emergency service areas (ESAs) are not sampled at this stage. In the third stage ESAs are sampled.",
+            "description": "The National Hospital Ambulatory Medical Care Survey (NHAMCS) has been fielded annually since 1992 to collect data on the utilization and provision of ambulatory care services in hospital emergency and outpatient departments. Data collection from hospital-based ambulatory surgery centers began in 2009. And between 2010 and 2012 NHAMCS gathered data on visits to freestanding ambulatory surgery centers. In 2018, the survey began focusing on just the ambulatory visits made to emergency departments.\nEach emergency department is randomly assigned to a 4-week reporting period. During this period, data for a systematic random sample of visits are recorded by Census interviewers using a computerized Patient Record Form. Data are obtained on patient characteristics such as age, sex, race, and ethnicity, and visit characteristics such as patient\u2019s reason for visit, provider\u2019s diagnosis, services ordered or provided, and treatments, including medication therapy. In addition, data about the facility are collected as part of a survey induction interview.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/8ucz-ra9b",
+            "isPartOf": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
             "issued": "2003-04-07",
-            "@type": "dcat:Dataset",
-            "temporal": "1992-2021",
-            "modified": "2024-02-21",
             "keyword": [
                 "cause of injury",
                 "diagnosis",
@@ -32645,65 +32657,36 @@
                 "reason for visit",
                 "research-data-center"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/ahcd/about_ahcd.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-02-21",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/8ucz-ra9b",
-            "description": "The National Hospital Ambulatory Medical Care Survey (NHAMCS) has been fielded annually since 1992 to collect data on the utilization and provision of ambulatory care services in hospital emergency and outpatient departments. Data collection from hospital-based ambulatory surgery centers began in 2009. And between 2010 and 2012 NHAMCS gathered data on visits to freestanding ambulatory surgery centers. In 2018, the survey began focusing on just the ambulatory visits made to emergency departments.\nEach emergency department is randomly assigned to a 4-week reporting period. During this period, data for a systematic random sample of visits are recorded by Census interviewers using a computerized Patient Record Form. Data are obtained on patient characteristics such as age, sex, race, and ethnicity, and visit characteristics such as patient\u2019s reason for visit, provider\u2019s diagnosis, services ordered or provided, and treatments, including medication therapy. In addition, data about the facility are collected as part of a survey induction interview.",
-            "title": "National Hospital Ambulatory Medical Care Survey, 1992-2021, Restricted",
-            "isPartOf": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "mediaType": "text/html"
-                }
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training, and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "United States",
-            "describedBy": "For the survey, findings are based on a national sample of visits to emergency departments (EDs) in noninstitutional general and short-stay hospitals, exclusive of Federal, military, and Veterans Administration hospitals, located in the 50 States and the District of Columbia. The sampling frame for the 2021 NHAMCS was constructed from IQVIA\u2019s database. A three-stage probability sampling design is used. The first stage consists of a sample of geographically defined areas also known as Primary Sampling Units (PSU). In the second stage, is of hospitals within those PSU and all emergency service areas within the emergency department are selected. Emergency service areas (ESAs) are not sampled at this stage. In the third stage ESAs are sampled.",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Survey has ended. 2022 data will be released Summer 2024.",
+            "temporal": "1992-2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Hospital Ambulatory Medical Care Survey, 1992-2021, Restricted"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/abgz-qs4g",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-17",
-            "keyword": [
-                "clostridioides difficile",
-                "haicviz"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HAIC",
                 "hasEmail": "mailto:erib@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/abgz-qs4g",
             "description": "<p>The healthcare-associated infection component of CDC\u2019s <a href=\"https://www.cdc.gov/ncezid/dpei/eip/index.html\" target=\"_blank\">EIP</a> engages a <a href=\"https://www.cdc.gov/ncezid/dpei/eip/eip-sites.html\" target=\"_blank\">network</a> of state health departments and their academic medical center partners to help answer critical questions about emerging HAI threats, advanced infection tracking methods, and antibiotic resistance in the United States. Information gathered through this activity will play a key role in shaping future policies and recommendations targeting HAI prevention. </p>",
-            "title": "HAICViz - CDI",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32726,43 +32709,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/abgz-qs4g",
+            "issued": "2022-11-17",
+            "keyword": [
+                "clostridioides difficile",
+                "haicviz"
+            ],
+            "landingPage": "https://data.cdc.gov/d/abgz-qs4g",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-11-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "HAICViz - CDI"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-28",
-            "@type": "dcat:Dataset",
-            "temporal": "2024-2025",
-            "modified": "2025-01-29",
-            "keyword": [
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "rsv vaccination",
-                "vsd"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hea5-6w9c",
             "description": "\u2022Weekly Cumulative Estimated Number of RSV Vaccinations Administered in Retail Pharmacies and Physicians\u2019 Medical Offices, Adults 60 to 74 Years and 75 Years and Older, United States  \n\n\u2022 Estimated Number of RSV vaccinations among adults 60 years and older is assessed through IQVIA (https://www.iqvia.com/) as a source of information on vaccinations administered in retail pharmacies (include chain, mass merchandise, food stores, and independent pharmacies) and physician medical offices.",
-            "title": "Weekly Cumulative Estimated Number of RSV Vaccinations Administered in Retail Pharmacies and Physicians\u2019 Medical Offices, Adults 60 to 74 Years and 75 years and older, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32785,26 +32765,59 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
-            "theme": [
-                "Vaccinations"
+            "identifier": "https://data.cdc.gov/api/views/hea5-6w9c",
+            "issued": "2025-01-28",
+            "keyword": [
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "rsv vaccination",
+                "vsd"
             ],
+            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National",
+            "temporal": "2024-2025",
+            "theme": [
+                "Vaccinations"
+            ],
+            "title": "Weekly Cumulative Estimated Number of RSV Vaccinations Administered in Retail Pharmacies and Physicians\u2019 Medical Offices, Adults 60 to 74 Years and 75 years and older, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/departmental-appeals-board-decisions",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.hhs.gov/dab/decisions/dabdecisions/index.html",
+            "description": "<p>Decisions issued by the Chair and Board Members of the Departmental Appeals Board concerning determinations in discretionary, project grant programs, including disallowances, terminations and denials of refunding, cost allocation plan disapprovals, and rate determinations; determinations in mandatory grant programs, including disallowances of state claims under titles I, IV-A (Temporary Assistance for Needy Families), IV-D (Child Support Enforcement), IV-E (Foster Care and Adoption Assistance), X, XIV, XVI, XIX (Medicaid), and XXI (State Children's Health Insurance Program) of the Social Security Act; and appellate review of decisions of DAB Civil Remedies Division ALJs, decisions of Food and Drug Administration ALJs regarding civil money penalties, and decisions of Department of the Interior ALJs in Indian Health Service contract/compact cases. .</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.hhs.gov/dab/decisions/index.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "3fa58f63-142f-4075-93f7-f58be8acb7f5",
             "issued": "2012-05-30",
-            "temporal": "1974-03-07T00:00:00-04:00/1974-03-07T00:00:00-04:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "abuse",
                 "acf",
@@ -32940,62 +32953,36 @@
                 "violation",
                 "withhold"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/departmental-appeals-board-decisions",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:024"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "3fa58f63-142f-4075-93f7-f58be8acb7f5",
-            "description": "<p>Decisions issued by the Chair and Board Members of the Departmental Appeals Board concerning determinations in discretionary, project grant programs, including disallowances, terminations and denials of refunding, cost allocation plan disapprovals, and rate determinations; determinations in mandatory grant programs, including disallowances of state claims under titles I, IV-A (Temporary Assistance for Needy Families), IV-D (Child Support Enforcement), IV-E (Foster Care and Adoption Assistance), X, XIV, XVI, XIX (Medicaid), and XXI (State Children's Health Insurance Program) of the Social Security Act; and appellate review of decisions of DAB Civil Remedies Division ALJs, decisions of Food and Drug Administration ALJs regarding civil money penalties, and decisions of Department of the Interior ALJs in Indian Health Service contract/compact cases. .</p>",
-            "title": "Departmental Appeals Board Decisions",
-            "programCode": [
-                "009:024"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.hhs.gov/dab/decisions/index.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://www.hhs.gov/dab/decisions/dabdecisions/index.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1974-03-07T00:00:00-04:00/1974-03-07T00:00:00-04:00",
             "theme": [
                 "Health",
                 "Medicare",
                 "Hospital"
-            ]
+            ],
+            "title": "Departmental Appeals Board Decisions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5b7j-usbu",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division, Pathology and Physiology Research Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5b7j-usbu",
             "description": "The process of stainless steel welding creates fumes rich in carcinogenic metals such as chromium (Cr). Welding consumables devoid of Cr are being produced in attempt to limit worker exposures to potentially toxic and carcinogenic metals. The study objective was to characterize a copper-nickel (Cu-Ni) fume generated using gas metal arc welding (GMAW) and determine the pulmonary deposition and toxicity of the fume in mice exposed by inhalation. Male A/J mice (6 \u2013 8 weeks of age) were exposed to air or Cu-Ni welding fumes for 2 (low deposition) or 4 (high deposition) hours/day for 10 days. Mice were sacrificed and bronchoalveolar lavage (BAL), macrophage function, and histopathological analysis were performed at various timepoints post-exposure to evaluate resolution. Characterization of the fume indicated that most of the particles were between 0.1 and 1 \u00b5m in diameter, with a mass median aerodynamic diameter of 0.43 \u00b5m. Metal content of the fume was primarily Cu (~76%) and Ni (~12%). After exposure, BAL macrophages had a reduced ability to phagocytose E. coli at 1 and 7 days and lung cytotoxicity was evident and significant (>12-19% fold change). Loss of body weight was also significant at these two early timepoints. Lung inflammation, the predominant lesion identified by histopathology, was observed as a subacute response early that progressively resolved by 28 days with only macrophage aggregates remaining late (84 days). Future studies are planned to investigate the tumorigenic potential of Cu-Ni fume in A/J mice.",
-            "title": "Lung Toxicity Profile of Inhaled Copper-Nickel Welding Fume in A/J Mice",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33003,45 +32990,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5b7j-usbu",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/5b7j-usbu",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Lung Toxicity Profile of Inhaled Copper-Nickel Welding Fume in A/J Mice"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/r5u4-fzxi",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "arboviral diseases",
-                "babesiosis",
-                "nedss",
-                "netss",
-                "nndss",
-                "west nile virus disease",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/r5u4-fzxi",
             "description": "NNDSS - Table 1D. Arboviral diseases, neuroinvasive and non-neuroinvasive, West Nile virus disease to Babesiosis - 2019.In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1D. Arboviral diseases, West Nile virus to Babesiosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33064,43 +33041,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/r5u4-fzxi",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "arboviral diseases",
+                "babesiosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "west nile virus disease",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/r5u4-fzxi",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1D. Arboviral diseases, West Nile virus to Babesiosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/8j7j-5y74",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2017-11-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-11",
-            "keyword": [
-                "cms-64",
-                "enrollment",
-                "expansion population",
-                "medicaid",
-                "new adult group",
-                "viii group"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "6c114b2c-cb83-559b-832f-4d8b06d6c1b9",
             "description": "Total Medicaid Enrollees - VIII Group Break Out Report Reported on the CMS-64\r\n\r\nThe enrollment information is a state-reported count of unduplicated individuals enrolled in the state\u2019s Medicaid program at any time during each month in the quarterly reporting period. The enrollment data identifies the total number of Medicaid enrollees and, for states that have expanded Medicaid, provides specific counts for the number of individuals enrolled in the new adult eligibility group, also referred to as the \u201cVIII Group\u201d. The VIII Group is only applicable for states that have expanded their Medicaid programs by adopting the VIII Group. This data includes state-by-state data for this population as well as a count of individuals whom the state has determined are newly eligible for Medicaid. All 50 states, the District of Columbia and the US territories are represented in these data.\r\n\r\nNotes:\r\n1. \u201cVIII GROUP\u201d is also known as the \u201cNew Adult Group.\u201d\r\n2. The VIII Group is only applicable for states that have expanded their Medicaid programs by adopting the VIII Group. VIII Group enrollment information for the states that have not expanded their Medicaid program is noted as \u201cN/A.\u201d",
-            "title": "Medicaid Enrollment - New Adult Group",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33109,48 +33089,43 @@
                     "title": "Medicaid Enrollment - New Adult Group"
                 }
             ],
+            "identifier": "6c114b2c-cb83-559b-832f-4d8b06d6c1b9",
+            "issued": "2017-11-10",
+            "keyword": [
+                "cms-64",
+                "enrollment",
+                "expansion population",
+                "medicaid",
+                "new adult group",
+                "viii group"
+            ],
+            "landingPage": "https://healthdata.gov/d/8j7j-5y74",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-12-11",
+            "programCode": [
+                "009:076"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Enrollment"
-            ]
+            ],
+            "title": "Medicaid Enrollment - New Adult Group"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/u7e4-s8zi",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "age <5 years serotype b",
-                "all ages all serotypes",
-                "gonorrhea",
-                "haemophilus influenzae",
-                "invasive disease",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/u7e4-s8zi",
             "description": "NNDSS - TABLE 1M.  Gonorrhea to Haemophilus influenzae, invasive disease, Age <5 years, Serotype b - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease, Age <5 years, Serotype b",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33173,54 +33148,49 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/u7e4-s8zi",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "age <5 years serotype b",
+                "all ages all serotypes",
+                "gonorrhea",
+                "haemophilus influenzae",
+                "invasive disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/u7e4-s8zi",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2021-01-07",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease, Age <5 years, Serotype b"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rhwp-grxi",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "N/A",
-            "issued": "2024-12-19",
-            "@type": "dcat:Dataset",
-            "temporal": "N/A",
-            "modified": "2025-01-24",
-            "references": [
-                "NHSN Hospital Respiratory Data (HRD) Reporting: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html  NHSN Hospital Respiratory Data (HRD) Dashboard: https://wwwdev.cdc.gov/nhsn/psc/hospital-respiratory-dashboard.html#anchor_83745  Centers for Medicare and Medicaid Services (CMS) requirements: Updates to the Condition of Participation (CoP) Requirements for Hospitals and Critical Access Hospitals (CAHs) To Report Acute Respiratory Illnesses."
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
-                "inpatient beds",
-                "respiratory",
-                "respiratory syncytial virus",
-                "rsv"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DHQP",
                 "hasEmail": "mailto:nhsn@cdc.gov (subject line: Hospital Respiratory Data)"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rhwp-grxi",
+            "describedBy": "N/A",
             "description": "This dataset represents weekly hospital respiratory data and metrics aggregated to national and state/territory levels reported to CDC\u2019s National Health Safety Network (NHSN) beginning November 2024. Data and metrics included in this dataset are NOT updated or adjusted week-over-week after initial publication, and therefore represent data received at the time of publication for a given reporting week. All data included in this dataset represent aggregated counts, and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and new hospital admissions with corresponding metrics indicating reporting coverage for a given reporting week. NHSN monitors national and local trends in healthcare system stress and capacity for all acute care and critical access hospitals in the United States. \n \nFor more information on the reporting mandate per the Centers for Medicare and Medicaid Services (CMS) requirements, visit: , visit: <a href=\"https://www.cms.gov/medicare/health-safety-standards/quality-safety-oversight-general-information/policy-memos-states/updates-condition-participation-cop-requirements-hospitals-and-critical-access-hospitals-cahs-report\">. \n \nFor more information regarding NHSN\u2019s collection of these data, including full reporting guidance, visit: <a href=\"https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html\">NHSN Hospital Respiratory Data.</a>\n\n<b>Source: CDC National Healthcare Safety Network (NHSN).</b>\n<ul><li><b>Data source description</b> \u202f(updated November 15, 2024): As of October 9, 2024, Hospital Respiratory Data (HRD; formerly Respiratory Pathogen, Hospital Capacity, and Supply data or 'COVID-19 hospital data') are reported to HHS through CDC's National Healthcare Safety Network (NHSN) based on updated requirements from the Centers for Medicare and Medicaid Services (CMS). These data were voluntarily reported to NHSN May 1, 2024 until November 1, 2024, at which time CMS began requiring acute care and critical access hospitals to electronically report information via NHSN about COVID-19, influenza, and RSV, hospital bed census and capacity. Hospital bed capacity and occupancy data for all patients and for patients with COVID-19 or influenza for collection dates prior to May 1, 2024, represent data reported during a previously mandated reporting period as specified by the HHS Secretary, and data for collection dates May 1, 2024 \u2013 October 31, 2024 represent data reported voluntarily to NHSN. All RSV data through October 31, 2024 represent voluntarily reported data; as such, all voluntarily reported data included in this dataset represent reporting hospitals only for a given week and might not be complete or representative of all hospitals during the specified reporting periods.</li><li>NHSN monitors national and local trends in healthcare system stress and capacity for all acute care and critical access hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Find more information about reporting to NHSN:\u202fhttps://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html. </li><li><b>Data quality:</b> While CDC reviews reported data for completeness and errors and corrects those found, some reporting errors might still exist within the data. CDC and partners work with reporters to correct these errors and update the data in subsequent weeks. Data reported as of December 1, 2020 are subject to thorough, routine data quality review procedures, including identifying and excluding invalid values from metric calculations and application of error correction methodology; data prior to this date may have anomalies that are not yet resolved. Data prior to August 1, 2020, are unavailable.\u202fData and metrics included in this dataset are NOT updated or adjusted week-over-week after initial publication, and therefore represent da",
-            "title": "Weekly Hospital Respiratory Data (HRD) Metrics by Jurisdiction, National Healthcare Safety Network (NHSN) (Historical)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33243,49 +33213,58 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
-            "describedBy": "N/A",
+            "identifier": "https://data.cdc.gov/api/views/rhwp-grxi",
+            "issued": "2024-12-19",
+            "keyword": [
+                "admissions",
+                "coronavirus",
+                "covid-19",
+                "hospital capacity",
+                "hospitalizations",
+                "hospital occupancy",
+                "icu beds",
+                "influenza",
+                "inpatient beds",
+                "respiratory",
+                "respiratory syncytial virus",
+                "rsv"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rhwp-grxi",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-24",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "NHSN Hospital Respiratory Data (HRD) Reporting: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html  NHSN Hospital Respiratory Data (HRD) Dashboard: https://wwwdev.cdc.gov/nhsn/psc/hospital-respiratory-dashboard.html#anchor_83745  Centers for Medicare and Medicaid Services (CMS) requirements: Updates to the Condition of Participation (CoP) Requirements for Hospitals and Critical Access Hospitals (CAHs) To Report Acute Respiratory Illnesses."
+            ],
+            "rights": "N/A",
+            "spatial": "US",
+            "temporal": "N/A",
             "theme": [
                 "Public Health Surveillance"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Hospital Respiratory Data (HRD) Metrics by Jurisdiction, National Healthcare Safety Network (NHSN) (Historical)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225435.htm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2010-10-01",
-            "keyword": [
-                "health",
-                "market",
-                "notifications",
-                "pet food",
-                "recalls",
-                "safety"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FDA Enterprise Data Inventory",
                 "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "6e4c0c94-6b71-49f8-b551-c70a9070867e",
             "description": "Contains data for FDA pet food recalls since January 1, 2006.",
-            "title": "FDA Pet Health and Safety Widget",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33293,54 +33272,49 @@
                     "mediaType": "application/unknown"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "6e4c0c94-6b71-49f8-b551-c70a9070867e",
+            "issued": "2021-02-25",
+            "keyword": [
+                "health",
+                "market",
+                "notifications",
+                "pet food",
+                "recalls",
+                "safety"
+            ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225435.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2010-10-01",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "FDA Pet Health and Safety Widget"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-opioid-prescribing-rates/medicare-part-d-opioid-prescribing-rates-by-geography",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2022-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-15",
-            "references": [
-                "https://data.cms.gov/resources/medicare-part-d-opioid-prescribing-rates-by-geography-methodology-0"
-            ],
-            "keyword": [
-                "counties",
-                "drugs",
-                "health equity",
-                "medicare",
-                "medicare prescription drug",
-                "national",
-                "physicians & practitioners",
-                "rural-urban",
-                "states & territories",
-                "zip code"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicare Provider Data - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/94d00f36-73ce-4520-9b3f-83cd3cded25c/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-part-d-opioid-prescribing-rates-by-geography-data-dictionary",
             "description": "The Medicare Part D Opioid Prescribing Rates by Geography dataset provides information on geographic comparisons of the number and percentage of Medicare Part D opioid prescriptions at the state, county, and ZIP code levels.",
-            "title": "Medicare Part D Opioid Prescribing Rates - by Geography",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/94d00f36-73ce-4520-9b3f-83cd3cded25c/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/94d00f36-73ce-4520-9b3f-83cd3cded25c/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Part D Opioid Prescribing Rates - by Geography : 2022-12-01"
                 },
                 {
@@ -33356,26 +33330,65 @@
                     "title": "Medicare Part D Opioid Prescribing Rates - by Geography : 2022-12-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-part-d-opioid-prescribing-rates-by-geography-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/94d00f36-73ce-4520-9b3f-83cd3cded25c/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "counties",
+                "drugs",
+                "health equity",
+                "medicare",
+                "medicare prescription drug",
+                "national",
+                "physicians & practitioners",
+                "rural-urban",
+                "states & territories",
+                "zip code"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-opioid-prescribing-rates/medicare-part-d-opioid-prescribing-rates-by-geography",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-part-d-opioid-prescribing-rates-by-geography-methodology-0"
+            ],
+            "temporal": "2022-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Part D Opioid Prescribing Rates - by Geography"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/california-drug-and-alcohol-treatment-assessment-caldata-1991-1993",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The California Drug and Alcohol Treatment Assessment<br />\n(CALDATA) was designed to study the costs, benefits, and effectiveness<br />\nof the state's alcohol and drug treatment infrastructure (recovery<br />\nservices) and specifically to assess (1) the effects of treatment on<br />\nparticipant behavior, (2) the costs of treatment, and (3) the economic<br />\nvalue of treatment to society. Data were collected on participants<br />\n(clients) across four types of treatment programs, or modalities:<br />\nresidential, residential \"social model,\" nonmethadone outpatient, and<br />\noutpatient methadone (detoxification and maintenance). Data were<br />\ncollected in two phases. In Phase 1, treatment records were abstracted<br />\nfor clients who received treatment or were discharged between October<br />\n1, 1991, and September 30, 1992. In Phase 2, these clients were<br />\nlocated and recruited for a follow-up interview. The CALDATA design<br />\nand procedures included elements from several national treatment<br />\noutcome studies including the Drug Services Research Survey, Services Research Outcomes Study, National<br />\nTreatment Improvement Evaluation Study, and Drug Abuse<br />\nTreatment Outcome Study. The record abstract was designed<br />\nto collect identifying and locating information for interview<br />\nreference during the personal interviewing phase. The abstract also<br />\ncollected demographic, drug, or alcohol use, and treatment and service<br />\ninformation. The follow-up questionnaire covered time periods before,<br />\nduring, and after treatment and focused on topics such as ethnic and<br />\neducational background, drug and alcohol use, mental and physical<br />\nhealth, HIV and AIDS status, drug testing, illegal activities and<br />\ncriminal status, living arrangements and family issues, employment and<br />\nincome, and treatment for drug, alcohol, and mental health<br />\nproblems. Drugs included alcohol, barbiturates, benzodiazepines,<br />\ncocaine powder, crack, downers, hallucinogens, heroin, illegal<br />\nmethadone, inhalants, LSD, marijuana/hashish/THC, methamphetamines and<br />\nother stimulants, narcotics, over-the-counter drugs, PCP, ritalin or<br />\npreludin, and sedatives/hypnotics. CALDATA was originally known as the<br />\nCalifornia Outcomes Study (COS).This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "California Drug and Alcohol Treatment Assessment (CALDATA-1991-1993) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/california-drug-and-alcohol-treatment-assessment-caldata-1991-1993-nid13527",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/california-drug-and-alcohol-treatment-assessment-caldata-1991-1993-nid13527"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/california-drug-and-alcohol-treatment-assessment-caldata-1991-1993-nid13527",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol",
                 "cocaine",
@@ -33400,41 +33413,41 @@
                 "treatment costs",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/california-drug-and-alcohol-treatment-assessment-caldata-1991-1993",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/california-drug-and-alcohol-treatment-assessment-caldata-1991-1993-nid13527",
-            "description": "<p>The California Drug and Alcohol Treatment Assessment<br />\n(CALDATA) was designed to study the costs, benefits, and effectiveness<br />\nof the state's alcohol and drug treatment infrastructure (recovery<br />\nservices) and specifically to assess (1) the effects of treatment on<br />\nparticipant behavior, (2) the costs of treatment, and (3) the economic<br />\nvalue of treatment to society. Data were collected on participants<br />\n(clients) across four types of treatment programs, or modalities:<br />\nresidential, residential \"social model,\" nonmethadone outpatient, and<br />\noutpatient methadone (detoxification and maintenance). Data were<br />\ncollected in two phases. In Phase 1, treatment records were abstracted<br />\nfor clients who received treatment or were discharged between October<br />\n1, 1991, and September 30, 1992. In Phase 2, these clients were<br />\nlocated and recruited for a follow-up interview. The CALDATA design<br />\nand procedures included elements from several national treatment<br />\noutcome studies including the Drug Services Research Survey, Services Research Outcomes Study, National<br />\nTreatment Improvement Evaluation Study, and Drug Abuse<br />\nTreatment Outcome Study. The record abstract was designed<br />\nto collect identifying and locating information for interview<br />\nreference during the personal interviewing phase. The abstract also<br />\ncollected demographic, drug, or alcohol use, and treatment and service<br />\ninformation. The follow-up questionnaire covered time periods before,<br />\nduring, and after treatment and focused on topics such as ethnic and<br />\neducational background, drug and alcohol use, mental and physical<br />\nhealth, HIV and AIDS status, drug testing, illegal activities and<br />\ncriminal status, living arrangements and family issues, employment and<br />\nincome, and treatment for drug, alcohol, and mental health<br />\nproblems. Drugs included alcohol, barbiturates, benzodiazepines,<br />\ncocaine powder, crack, downers, hallucinogens, heroin, illegal<br />\nmethadone, inhalants, LSD, marijuana/hashish/THC, methamphetamines and<br />\nother stimulants, narcotics, over-the-counter drugs, PCP, ritalin or<br />\npreludin, and sedatives/hypnotics. CALDATA was originally known as the<br />\nCalifornia Outcomes Study (COS).This study has 1 Data Set.</p>",
-            "title": "California Drug and Alcohol Treatment Assessment (CALDATA-1991-1993)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/california-drug-and-alcohol-treatment-assessment-caldata-1991-1993-nid13527",
-                    "description": "California Drug and Alcohol Treatment Assessment (CALDATA-1991-1993) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/california-drug-and-alcohol-treatment-assessment-caldata-1991-1993-nid13527"
-                }
-            ]
+            "title": "California Drug and Alcohol Treatment Assessment (CALDATA-1991-1993)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-mortality-infant-deaths",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/lbd.html",
+            "description": "<p>The Mortality - Infant Deaths (from Linked Birth / Infant Death Records) online databases on CDC WONDER provide counts and rates for deaths of children under 1 year of age, occuring within the United States to U.S. residents. Information from death certificates has been linked to corresponding birth certificates. Data are available by county of mother's residence, child's age, underlying cause of death, gender, birth weight, birth plurality, birth order, gestational age at birth, period of prenatal care, maternal race and ethnicity, maternal age, maternal education and marital status. Data are available since 1995. The data are produced by the National Center for Health Statistics.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/lbd.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "5f2e0ec4-4aa6-4b00-bc1a-9fa72bbff80c",
             "issued": "2012-05-30",
-            "temporal": "1995-01-01T00:00:00-05:00/2005-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "age",
                 "birthplace",
@@ -33460,64 +33473,37 @@
                 "sex",
                 "state"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-mortality-infant-deaths",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:015"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "5f2e0ec4-4aa6-4b00-bc1a-9fa72bbff80c",
-            "description": "<p>The Mortality - Infant Deaths (from Linked Birth / Infant Death Records) online databases on CDC WONDER provide counts and rates for deaths of children under 1 year of age, occuring within the United States to U.S. residents. Information from death certificates has been linked to corresponding birth certificates. Data are available by county of mother's residence, child's age, underlying cause of death, gender, birth weight, birth plurality, birth order, gestational age at birth, period of prenatal care, maternal race and ethnicity, maternal age, maternal education and marital status. Data are available since 1995. The data are produced by the National Center for Health Statistics.</p>",
-            "title": "CDC WONDER: Mortality - Infant Deaths",
-            "programCode": [
-                "009:015"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://wonder.cdc.gov/lbd.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/lbd.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1995-01-01T00:00:00-05:00/2005-12-31T00:00:00-05:00",
             "theme": [
                 "Health",
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Mortality - Infant Deaths"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135821.htm",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "cder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FDA Enterprise Data Inventory",
                 "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "f22c9b6a-e68a-445a-ae44-1441b2f698ab",
+            "describedBy": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm079750.htm",
             "description": "Information about FDA-approved brand name and generic prescription and over-the-counter human drugs and biological therapeutic products. Drugs@FDA includes most of the drug products approved since 1939. The majority of patient information, labels, approval letters, reviews, and other information are available for drug products approved since 1998.",
-            "title": "Drugs@FDA Database",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33525,38 +33511,35 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm079750.htm",
+            "identifier": "f22c9b6a-e68a-445a-ae44-1441b2f698ab",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cder"
+            ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135821.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1D"
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Drugs@FDA Database"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -33579,44 +33562,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/x9gq-59r3",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/x9gq-59r3",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-09-14",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://www.cdc.gov/art/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "art",
-                "assisted reproductive technology",
-                "clinic",
-                "fertility",
-                "infertility",
-                "services",
-                "success rates"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ARTINFO",
                 "hasEmail": "mailto:ARTINFO@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ey8b-ejrf",
+            "describedBy": "https://data.cdc.gov/dataset/2021-Final-Assisted-Reproductive-Technology-ART-Su/ey8b-ejrf/revisions/0",
             "description": "Data were updated on September 11, 2024.\n\nART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Success Rates dataset contains success rates for ART cycles started during the year indicated. Since ART success depends on whether patients are using their own eggs or donor eggs, success rates are included separately for these two groups. Success rates for patients using their own eggs are shown per intended retrieval, per actual retrieval, and per transfer. These success rates are reported as cumulative success rates, which take into account transfers that occur within 1 year after an egg retrieval. Since ART success depends on whether patients are using ART for the first time or had prior ART cycles, users can examine success rates for all \u201cPatients using their own eggs\u201d or for \u201cPatients with no prior ART using their own eggs.\u201d For new patients using ART for the first time, the success rates are also shown after 1, 2, or all intended egg retrievals during the reporting year. In addition, the average number of transfers per intended retrieval and the average number of intended retrievals per live-birth delivery are shown. Success rates for ART cycles that involve the transfer of embryos created from donor eggs or donated embryos are shown and are not cumulative. They are based on donor cycles started in the year indicated that had embryo transfers, regardless of when the donor eggs were retrieved. Success rates in this section are not presented by patient age group because previous data show that an intended parent\u2019s age does not substantially affect success when using donor eggs or donated embryos. The success rates are presented by types of embryos and eggs used in the transfer. This dataset excludes cycles that were considered research\u2014that is, cycles performed to evaluate new procedures.",
-            "title": "2021 Final Assisted Reproductive Technology (ART) Success Rates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33639,49 +33618,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/dataset/2021-Final-Assisted-Reproductive-Technology-ART-Su/ey8b-ejrf/revisions/0",
+            "identifier": "https://data.cdc.gov/api/views/ey8b-ejrf",
+            "issued": "2023-01-01",
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
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
+            "title": "2021 Final Assisted Reproductive Technology (ART) Success Rates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fyv2-xffj",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "acute)",
-                "confirmed",
-                "hepatitis b",
-                "hepatitis c (viral",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/fyv2-xffj",
             "description": "NNDSS - TABLE 1Q.  Hepatitis B, perinatal infection to Hepatitis C (viral, acute), Probable - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n * Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 For acute Hepatitis C, only confirmed cases were verified.",
-            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C (viral, acute), Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33704,46 +33678,49 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fyv2-xffj",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "acute)",
+                "confirmed",
+                "hepatitis b",
+                "hepatitis c (viral",
+                "nedss",
+                "netss",
+                "nndss",
+                "perinatal infection",
+                "probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fyv2-xffj",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C (viral, acute), Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-09",
-            "references": [
-                "https://www.cdc.gov/nccdphp/dnpao/index.html"
-            ],
-            "keyword": [
-                "breastfeeding",
-                "dnpao",
-                "fruit",
-                "nutrition",
-                "physical activity",
-                "vegetable"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DNPAO Public Inquiries",
                 "hasEmail": "mailto:dnpaoinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/k8w5-7ju6",
+            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Policy-and/k8w5-7ju6",
             "description": "This dataset includes data on policy and environmental supports for physical activity, diet, and breastfeeding. This data is used for DNPAO's Data, Trends, and Maps database, which provides national and state specific data on obesity, nutrition, physical activity, and breastfeeding.",
-            "title": "Nutrition, Physical Activity, and Obesity - Policy and Environmental Data",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33766,47 +33743,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Policy-and/k8w5-7ju6",
+            "identifier": "https://data.cdc.gov/api/views/k8w5-7ju6",
+            "issued": "2023-07-18",
+            "keyword": [
+                "breastfeeding",
+                "dnpao",
+                "fruit",
+                "nutrition",
+                "physical activity",
+                "vegetable"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-11-09",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/nccdphp/dnpao/index.html"
+            ],
             "theme": [
                 "Nutrition",
                 "Physical Activity",
                 "and Obesity"
-            ]
+            ],
+            "title": "Nutrition, Physical Activity, and Obesity - Policy and Environmental Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/art/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "art",
-                "assisted reproductive technology",
-                "clinic",
-                "fertility",
-                "infertility",
-                "services",
-                "success rates"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ARTINFO",
                 "hasEmail": "mailto:ARTINFO@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9tjt-seye",
+            "describedBy": "https://data.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Su/9tjt-seye",
             "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Summary dataset provides a full snapshot of clinic services and profile, patient characteristics, and ART success rates. It is worth noting that patient medical characteristics, such as age, diagnosis, and ovarian reserve, affect ART treatment\u2019s success. Comparison of success rates across clinics may not be meaningful because of differences in patient populations and ART treatment methods. The success rates displayed in this dataset do not reflect any one patient\u2019s chance of success. Patients should consult with a doctor to understand their chance of success based on their own characteristics.",
-            "title": "2022 Final Assisted Reproductive Technology (ART) Summary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33829,21 +33808,55 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Su/9tjt-seye",
+            "identifier": "https://data.cdc.gov/api/views/9tjt-seye",
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
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
+            "title": "2022 Final Assisted Reproductive Technology (ART) Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2009-0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2009 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, Adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. In the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2009) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2009-nid13531",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2009-nid13531"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2009-nid13531",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -33884,62 +33897,30 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2009-0",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2009-nid13531",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2009 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, Adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. In the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health (NSDUH-2009)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2009-nid13531",
-                    "description": "National Survey on Drug Use and Health (NSDUH-2009) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2009-nid13531"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health (NSDUH-2009)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xwa7-cukt",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-09-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "healthcare personnel",
-                "healthcare worker"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC-INFO",
                 "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xwa7-cukt",
             "description": "COVID-19 Deaths Among Healthcare Personnel, by week",
-            "title": "COVID-19 Deaths Among Healthcare Personnel, by week - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33962,51 +33943,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/xwa7-cukt",
+            "issued": "2023-09-18",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "healthcare personnel",
+                "healthcare worker"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xwa7-cukt",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "No longer updated (dataset archived)",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
             "theme": [
                 "Case Surveillance"
-            ]
+            ],
+            "title": "COVID-19 Deaths Among Healthcare Personnel, by week - ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-skilled-nursing-facility",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2013-01-01/2021-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-06",
-            "references": [
-                "https://data.cms.gov/resources/medicare-service-type-reports-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
-                "hospitals & facilities",
-                "medicare",
-                "national",
-                "original medicare",
-                "skilled nursing",
-                "states & territories"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CMS Program Statistics - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/c05cf65a-c13b-473c-8994-070f60f245b1/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics -\u00a0Medicare Skilled Nursing Facility tables provide use and payment data for skilled nursing facilities.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR SNF 1. \u00a0Medicare Skilled Nursing Facilities: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR SNF 2. \u00a0Medicare Skilled Nursing Facilities: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR SNF 3. \u00a0Medicare Skilled Nursing Facilities: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Area of Residence\n\tMDCR SNF 4. \u00a0Medicare Skilled Nursing Facilities: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Entitlement and Covered Days of Care\n\tMDCR SNF 5. \u00a0Medicare Skilled Nursing Facilities: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Facility and Bedsize\n\tMDCR SNF 6. \u00a0Medicare Skilled Nursing Facilities: \u00a0Distribution of Medicare Covered Skilled Nursing Facility Days, by State of Provider and Major Resource Utilization Groups (RUG)-III (versions 2013-2018 only)",
-            "title": "CMS Program Statistics - Medicare Skilled Nursing Facility",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34063,46 +34039,52 @@
                     "title": "CMS Program Statistics - Medicare Skilled Nursing Facility : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/c05cf65a-c13b-473c-8994-070f60f245b1/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "hospitals & facilities",
+                "medicare",
+                "national",
+                "original medicare",
+                "skilled nursing",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-skilled-nursing-facility",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-03-06",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-service-type-reports-methodology"
+            ],
+            "temporal": "2013-01-01/2021-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS Program Statistics - Medicare Skilled Nursing Facility"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://open.fda.gov/data.json",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "temporal": "1900-01-01/2013-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2013-12-20",
-            "keyword": [
-                "data-json",
-                "inventory"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "38fda70b-9734-4df0-ada6-897455bb7f7b",
             "description": "An inventory of all FDA Datasets",
-            "title": "FDA Data Inventory",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34110,40 +34092,37 @@
                     "mediaType": "application/json"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "38fda70b-9734-4df0-ada6-897455bb7f7b",
+            "issued": "2021-02-25",
+            "keyword": [
+                "data-json",
+                "inventory"
+            ],
+            "landingPage": "http://open.fda.gov/data.json",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-12-20",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "temporal": "1900-01-01/2013-12-31",
+            "title": "FDA Data Inventory"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/dhdsp/maps/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-02-08",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-24",
-            "keyword": [
-                "cardiovascular",
-                "cardiovascular disease",
-                "counties",
-                "county",
-                "heart",
-                "heart disease"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DHDSP Requests",
                 "hasEmail": "mailto:dhdsprequests@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/uc9k-vc2j",
             "description": "This dataset documents rates and trends in local hypertension-related cardiovascular disease (CVD) death rates. Specifically, this report presents county (or county equivalent) estimates of hypertension-related CVD death rates in 2000-2019 and trends during two intervals (2000-2010, 2010-2019) by age group (ages 35\u201364 years, ages 65 years and older), race/ethnicity (non-Hispanic American Indian/Alaska Native, non-Hispanic Asian/Pacific Islander, non-Hispanic Black, Hispanic, non-Hispanic White), and sex (female, male). The rates and trends were estimated using a Bayesian spatiotemporal model and a smoothed over space, time, and demographic group. Rates are age-standardized in 10-year age groups using the 2010 US population. Data source: National Vital Statistics System.",
-            "title": "Rates and Trends in Hypertension-related Cardiovascular Disease Mortality Among US Adults (35+) by County, Age Group, Race/Ethnicity, and Sex \u2013 2000-2019",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34166,86 +34145,90 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/uc9k-vc2j",
+            "issued": "2022-02-08",
+            "keyword": [
+                "cardiovascular",
+                "cardiovascular disease",
+                "counties",
+                "county",
+                "heart",
+                "heart disease"
+            ],
+            "landingPage": "https://www.cdc.gov/dhdsp/maps/index.htm",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-08-24",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Heart Disease & Stroke Prevention"
-            ]
+            ],
+            "title": "Rates and Trends in Hypertension-related Cardiovascular Disease Mortality Among US Adults (35+) by County, Age Group, Race/Ethnicity, and Sex \u2013 2000-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/8shu-9int",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-06",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "e707d154-79f4-5aea-a692-1a51a540007f",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt state v2.10.14 (coreset-dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.14/20241029/state.csv",
-                    "description": "CoreSEt state v2.10.14 (coreset-dev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt state v2.10.14 (coreset-dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.14/20241029/state.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt state v2.10.14 (coreset-dev)"
                 }
             ],
+            "identifier": "e707d154-79f4-5aea-a692-1a51a540007f",
+            "issued": "2024-11-06",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/8shu-9int",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-11-06",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSEt state v2.10.14 (coreset-dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/8t3i-7tqn",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-09-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-11",
-            "keyword": [
-                "core sets",
-                "performance rates",
-                "quality measures"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "dfd13757-d763-4f7a-9641-3f06ce21b4c6",
             "description": "Performance rates on frequently reported health care quality measures in the CMS Medicaid/CHIP Child and Adult Core Sets, for FFY 2022 reporting.\r\n\r\nSource: Mathematica analysis of MACPro and Form CMS-416 reports for the FFY 2022 reporting cycle. Dataset revised September 2023. For more information, see the Children's Health Care Quality Measures and Adult Health Care Quality Measures webpages.",
-            "title": "2022 Child and Adult Health Care Quality Measures Quality",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34253,47 +34236,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "dfd13757-d763-4f7a-9641-3f06ce21b4c6",
+            "issued": "2023-09-13",
+            "keyword": [
+                "core sets",
+                "performance rates",
+                "quality measures"
+            ],
+            "landingPage": "https://healthdata.gov/d/8t3i-7tqn",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-09-11",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Quality"
-            ]
+            ],
+            "title": "2022 Child and Adult Health Care Quality Measures Quality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/3qs9-qnbs",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-30",
-            "keyword": [
-                "covid-19",
-                "executive order",
-                "gathering bans",
-                "government order",
-                "legal epidemiology",
-                "mitigation",
-                "proclamation",
-                "public health order",
-                "social distancing"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "T.J. Pierce",
                 "hasEmail": "mailto:pwc2@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/3qs9-qnbs",
             "description": "State and territorial executive orders, administrative orders, resolutions, proclamations, and other official publicly available government communications are collected from government websites and cataloged and coded using Microsoft Excel by one or more coders with one or more additional coders conducting quality assurance.\n\nData were collected to determine when individuals in states and territories were subject to executive orders, administrative orders, resolutions, proclamations, and other official publicly available government communications related to  COVID-19 banning gatherings of various sizes either (1) generally, or specified that the gathering limit applied only when social distancing was not possible, or (2) even if participants practiced social distancing.\n\nThese data are derived from on the publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly ban gatherings found by the CDC, COVID-19 Community Intervention and Critical Populations Task Force, Monitoring and Evaluation Team & CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 11, 2020 through May 31, 2021. These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded, as well as official government communications such as announcements that counties have progressed through new phases of reopening pursuant to an executive order, directive, or other executive branch action, and posted to government websites; news media reports on restrictions were excluded. Recommendations and guidance documents not included or adopted by reference in an order are not included in these data. These data do not include mandatory business closures, curfews, or requirements/recommendations for people to stay in their homes. Due to limitations of the National Environmental Public Health Tracking Network Data Explorer, these data do not include tribes or cities, nor was a distinction made between county orders that applied county-wide versus those that were limited to unincorporated areas of the county. Effective and expiration dates were coded using only the date provided; no distinction was made based on the specific time of the day the order became effective or expired. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
-            "title": "U.S. State and Territorial Gathering Bans: March 11, 2020-May 31, 2021 by County by Day",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34316,48 +34292,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/3qs9-qnbs",
+            "issued": "2021-12-10",
+            "keyword": [
+                "covid-19",
+                "executive order",
+                "gathering bans",
+                "government order",
+                "legal epidemiology",
+                "mitigation",
+                "proclamation",
+                "public health order",
+                "social distancing"
+            ],
+            "landingPage": "https://data.cdc.gov/d/3qs9-qnbs",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-09-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Policy Surveillance"
-            ]
+            ],
+            "title": "U.S. State and Territorial Gathering Bans: March 11, 2020-May 31, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-10-06",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-28",
-            "keyword": [
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
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/dnhi-s2bf",
             "description": "Provisional counts of deaths involving coronavirus disease 2019 (COVID-19) by quarter and county of residence, in the United States, 2020-2021.",
-            "title": "AH Provisional COVID-19 Death Counts by Quarter and County",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34380,41 +34355,50 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/dnhi-s2bf",
+            "issued": "2021-10-06",
+            "keyword": [
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
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2022-03-28",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Death Counts by Quarter and County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-daily-fine-particulate-matter-0",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-08-03",
-            "temporal": "2003-01-01T00:00:00-05:00/2008-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "air temperature air quality air pollution fine particulate matter climate state county day month yea",
-                "other"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "admin",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
-            },
-            "identifier": "947d9832-ac25-45e6-800f-96fc9e4751a5",
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/PM.html",
             "description": "<p>The Daily Fine Particulate Matter data available on CDC WONDER are geographically aggregated daily measures of fine particulate matter in the outdoor air, spanning the years 2003-2008. PM2.5 particles are air pollutants with an aerodynamic diameter less than 2.5 micrometers. Reported measures are the daily measure of fine particulate matter in micrograms per cubic meter (PM2.5) (''\u00c2\u00b5g/m''\u00c2\u00b3), the number of observations, minimum and maximum range value, and standard deviation. Data are available by place (combined 48 contiguous states plus the District of Columbia, region, division, state, county), time (year, month, day) and specified fine particulate matter (''\u00c2\u00b5g/m''\u00c2\u00b3)value. County-level and higher data are aggregated from 10 kilometer square spatial resolution grids. In a study funded by the NASA Applied Sciences Program / Public Health Program, scientists at NASA Marshall Space Flight Center / Universities Space Research Association modified the regional surfacing algorithm of Al-Hamdan et al. (2009) and used it to generate continuous spatial surfaces (grids) of daily PM2.5 for the whole conterminous U.S. for 2003-2008. Two sources of environmental data were used as input to the surfacing algorithm, US Environmental Protection Agency (EPA) Air Quality System (AQS) PM2.5 in-situ data and National Aeronautics and Space Administration (NASA) Moderate Resolution Imaging Spectroradiometer (MODIS) aerosol optical depth remotely sensed data. They also identified in a Geographic Information System (GIS) the associated geographic locations of the centroids of the gridded PM2.5 dataset in terms of the counties and states they fall into to enable aggregation to different geographic levels in CDC WONDER.</p>",
-            "title": "CDC WONDER: Daily Fine Particulate Matter",
-            "programCode": [
-                "009:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34423,57 +34407,50 @@
                     "title": "Text "
                 }
             ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/PM.html",
-            "dataQuality": true,
+            "identifier": "947d9832-ac25-45e6-800f-96fc9e4751a5",
+            "issued": "2012-08-03",
+            "keyword": [
+                "air temperature air quality air pollution fine particulate matter climate state county day month yea",
+                "other"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-daily-fine-particulate-matter-0",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:031"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "temporal": "2003-01-01T00:00:00-05:00/2008-12-31T00:00:00-05:00",
             "theme": [
                 "Quality",
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Daily Fine Particulate Matter"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/performance-year-financial-and-quality-results",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2013-01-01/2023-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-29",
-            "references": [
-                "https://data.cms.gov/resources/performance-year-financial-and-quality-results-methodology-0"
-            ],
-            "keyword": [
-                "accountable care organizations",
-                "coordinated care",
-                "financials",
-                "medicare",
-                "original medicare",
-                "payment models",
-                "value-based care"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Shared Savings Program - CM",
                 "hasEmail": "mailto:SharedSavingsProgram@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/73b2ce14-351d-40ac-90ba-ec9e1f5ba80c/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/performance-year-financial-and-quality-results-data-dictionary",
             "description": "The Shared Savings Program Performance Year Financial and Quality Results data provides Medicare Shared Savings Program (Shared Savings Program) ACO-specific quality, expenditure, benchmark, and shared savings/loss metrics, as well as summarized beneficiary and provider information for each performance year of the Shared Savings Program. \u00a0\n\n\u00a0\n\nDISCLAIMER: This information is current as of the last update. Changes to Shared Savings Program ACO information occur periodically. Each Shared Savings Program ACO has the most up-to-date information about their organization. Consider contacting the Shared Savings Program ACO for the latest information. Contact information is available in the ACO Public Use File (PUF) and the ACO Participants PUF.",
-            "title": "Performance Year Financial and Quality Results",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/73b2ce14-351d-40ac-90ba-ec9e1f5ba80c/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/73b2ce14-351d-40ac-90ba-ec9e1f5ba80c/data",
+                    "mediaType": "text/html",
                     "title": "Performance Year Financial and Quality Results : 2023-10-01"
                 },
                 {
@@ -34621,66 +34598,52 @@
                     "title": "Performance Year Financial and Quality Results : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/performance-year-financial-and-quality-results-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/73b2ce14-351d-40ac-90ba-ec9e1f5ba80c/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "financials",
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/performance-year-financial-and-quality-results",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-29",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/performance-year-financial-and-quality-results-methodology-0"
+            ],
+            "temporal": "2013-01-01/2023-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Performance Year Financial and Quality Results"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/prams/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-06",
-            "references": [
-                "https://www.cdc.gov/prams/index.htm",
-                "https://www.cdc.gov/prams/pramstat/index.html"
-            ],
-            "keyword": [
-                "abuse",
-                "alcohol use",
-                "breastfeeding",
-                "contraception",
-                "infant health",
-                "medicaid",
-                "mental health",
-                "morbidity",
-                "obesity",
-                "preconception health",
-                "pregnancy history",
-                "prenatal care",
-                "reproductive health",
-                "sleep behavior",
-                "smoke exposure",
-                "stress",
-                "tobacco use",
-                "unintended pregnancy",
-                "wic"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DRH Public Inquiries",
                 "hasEmail": "mailto:PRAMSProposals@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/3hwj-hqmh",
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2000/3hwj-hqmh",
             "description": "2000. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2000",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34703,49 +34666,61 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2000/3hwj-hqmh",
+            "identifier": "https://data.cdc.gov/api/views/3hwj-hqmh",
+            "issued": "2023-07-19",
+            "keyword": [
+                "abuse",
+                "alcohol use",
+                "breastfeeding",
+                "contraception",
+                "infant health",
+                "medicaid",
+                "mental health",
+                "morbidity",
+                "obesity",
+                "preconception health",
+                "pregnancy history",
+                "prenatal care",
+                "reproductive health",
+                "sleep behavior",
+                "smoke exposure",
+                "stress",
+                "tobacco use",
+                "unintended pregnancy",
+                "wic"
+            ],
+            "landingPage": "https://www.cdc.gov/prams/index.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-09-06",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/prams/index.htm",
+                "https://www.cdc.gov/prams/pramstat/index.html"
+            ],
             "theme": [
                 "Maternal & Child Health"
-            ]
+            ],
+            "title": "CDC PRAMStat Data for 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/infant-mortality.htm",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2016-11-21",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-01-01/2024-06-30",
-            "modified": "2024-11-27",
-            "keyword": [
-                "causes of death",
-                "deaths",
-                "infant mortality",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "quarterly",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/jqwm-z2g9",
             "description": "Provisional estimates of infant mortality (deaths of infants under 1 year per 1,000 live births), neonatal mortality (deaths of infants aged 0-27 days per 1,000 live births), postneonatal mortality (deaths of infants aged 28 days through 11 months per 1,000 live births), and death rates for the five leading causes of infant death.",
-            "title": "NCHS - VSRR Quarterly provisional estimates for infant mortality",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34768,40 +34743,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/jqwm-z2g9",
+            "issued": "2016-11-21",
+            "keyword": [
+                "causes of death",
+                "deaths",
+                "infant mortality",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "quarterly",
+                "united states",
+                "vsrr"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/infant-mortality.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-11-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2022-01-01/2024-06-30",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - VSRR Quarterly provisional estimates for infant mortality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/tap4-sm6y",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2023-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-06",
-            "keyword": [
-                "pubmed"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/tap4-sm6y",
             "description": "*A file containing all Misc Baseline Reports for 2018-2023 in their original format is available in the <b>Attachments</b> section below.* \n\nMEDLINE/PubMed annual statistical reports are based upon the data elements in the baseline versions of MEDLINE\u00ae/PubMed are available. For each year covered the reports include: total citations containing each element; total occurrences of each element; minimum/average/maximum occurrences of each element in a record; minimum/average/maximum length of a single element occurrence; average record size; and other statistical data describing the content and size of the elements.",
-            "title": "MEDLINE/PubMed Baseline Statistics: Misc Report",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34824,94 +34808,84 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/tap4-sm6y",
+            "issued": "2023-03-22",
+            "keyword": [
+                "pubmed"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/tap4-sm6y",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-09-06",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Literature"
-            ]
+            ],
+            "title": "MEDLINE/PubMed Baseline Statistics: Misc Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/8vhs-66ax",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-20",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-10",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "171902bb-0e4a-568c-8514-f8ce5ff299cd",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet state v2.10.64 (coreset-prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/state.csv",
-                    "description": "CoreSet state v2.10.64 (coreset-prod)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet state v2.10.64 (coreset-prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/state.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet state v2.10.64 (coreset-prod)"
                 }
             ],
+            "identifier": "171902bb-0e4a-568c-8514-f8ce5ff299cd",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/8vhs-66ax",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2025-01-10",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSet state v2.10.64 (coreset-prod)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/93k9-hy54",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "keyword": [
-                "2016",
-                "all serogroups",
-                "invasive",
-                "lyme disease",
-                "malaria",
-                "meningococcal disease",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/93k9-hy54",
             "description": "NNDSS - Table II. Lyme disease to Meningococcal - 2016. In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.  NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change.   For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions.\r\n\u00a7 Data for meningococcal disease, invasive caused by serogroups ACWY; serogroup B; other serogroup; and unknown serogroup are available in Table I.",
-            "title": "NNDSS - Table II. Lyme disease to Meningococcal",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34934,41 +34908,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/93k9-hy54",
+            "issued": "2017-01-05",
+            "keyword": [
+                "2016",
+                "all serogroups",
+                "invasive",
+                "lyme disease",
+                "malaria",
+                "meningococcal disease",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/93k9-hy54",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2017-01-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://data.cdc.gov/d/b4av-siev",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2014-04-02",
-            "@type": "dcat:Dataset",
-            "modified": "2017-10-25",
-            "keyword": [
-                "brain injury",
-                "head trauma",
-                "tbi",
-                "traumatic brain injury"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/b4av-siev",
             "description": "Overall rates of TBI climbed slowly from 2001 through 2007, then spiked sharply in 2008 and continued to climb through 2010.  The increase in TBI rates in 2008 was much sharper for men (nearly 40% increase) than for women (20% increase).  In 2007, overall rates of TBI were 26% higher in men compared to women.  In 2008, that gap began to widen, reaching 61% in 2009 before narrowing to 29% in 2010.  Rates of overall TBI are largely driven by rates of TBI-related ED visits.",
-            "title": "Rates of TBI-related Emergency Department Visits, Hospitalizations, and Deaths by Sex - United States, 2001 \u2013 2010",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34991,101 +34972,89 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/b4av-siev",
+            "issued": "2014-04-02",
+            "keyword": [
+                "brain injury",
+                "head trauma",
+                "tbi",
+                "traumatic brain injury"
+            ],
+            "landingPage": "https://data.cdc.gov/d/b4av-siev",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2017-10-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Traumatic Brain Injury"
-            ]
+            ],
+            "title": "Rates of TBI-related Emergency Department Visits, Hospitalizations, and Deaths by Sex - United States, 2001 \u2013 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/8xfp-pqfb",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_prodauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "b832f850-6913-54ba-85f9-97073e8a0193",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_measure_compare_download",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_compare_download.csv",
-                    "description": "{\"dataset\": \"measure_compare_download\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_compare_download\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_compare_download.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_compare_download csv file"
                 }
             ],
+            "identifier": "b832f850-6913-54ba-85f9-97073e8a0193",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/8xfp-pqfb",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2024-11-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "prodAuto_measure_compare_download"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/schoolvaxview/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-05-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
-            "keyword": [
-                "any exemption",
-                "dt",
-                "dtap",
-                "dtp",
-                "hepatitis b",
-                "immunization",
-                "medical exemption",
-                "mmr",
-                "non-medical exemption",
-                "polio",
-                "school exemption",
-                "school vaccination",
-                "vaccination",
-                "vaccination coverage",
-                "varicella",
-                "vaxviews"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCIRD",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ijqb-a7ye",
             "description": "Vaccination Coverage and Exemptions among Kindergartners\n\n\u2022 Data on school vaccination coverage and exemptions from the School Vaccination Assessment Program for kindergartners at the national and state levels.\n\n\u2022 Additional information available at https://www.cdc.gov/vaccines/imz-managers/coverage/schoolvaxview/index.html",
-            "title": "Vaccination Coverage and Exemptions among Kindergartners",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35108,42 +35077,54 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ijqb-a7ye",
+            "issued": "2021-05-13",
+            "keyword": [
+                "any exemption",
+                "dt",
+                "dtap",
+                "dtp",
+                "hepatitis b",
+                "immunization",
+                "medical exemption",
+                "mmr",
+                "non-medical exemption",
+                "polio",
+                "school exemption",
+                "school vaccination",
+                "vaccination",
+                "vaccination coverage",
+                "varicella",
+                "vaxviews"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/schoolvaxview/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "Vaccination Coverage and Exemptions among Kindergartners"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-01",
-            "@type": "dcat:Dataset",
-            "temporal": "Flu Seasons-2021-22, 2022-23, 2023-24",
-            "modified": "2024-09-03",
-            "keyword": [
-                "flu vaccination",
-                "iis",
-                "immunization information system",
-                "vaccination coverage"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/udwr-3en6",
             "description": "Monthly Cumulative Number and Percent of Persons Who Received \u22651 Influenza Vaccination Doses, by Flu Season, Age Group, and Jurisdiction\n\n\u2022 Influenza vaccination coverage for children and adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems (IIS) data, submitted from jurisdictions to CDC monthly in aggregate by age group. More information about the IIS can be found at https://www.cdc.gov/vaccines/programs/iis/about.html.\n\n\u2022 Influenza vaccination coverage estimate numerators include the number of people receiving at least one dose of influenza vaccine in a given flu season, based on information that state, territorial, and local public health agencies report to CDC. Some jurisdictions\u2019 data may include data submitted by tribes. Estimates include persons who are deceased but received a vaccination during the current season. People receiving doses are attributed to the jurisdiction in which the person resides unless noted otherwise. Quality and completeness of data may vary across jurisdictions. Influenza vaccination coverage denominators are obtained from 2020 U.S. Census Bureau population estimates.\n\n\u2022 Monthly estimates shown are cumulative, reflecting all persons vaccinated from July through a given month of that flu season. Cumulative estimates include any historical data reported since the previous submission. National estimates are not presented since not all U.S. jurisdictions are currently reporting their IIS data to CDC. Jurisdictions reporting data to CDC include U.S. states, some localities, and territories.\n\n\u2022 Because IIS data contain all vaccinations administered within a jurisdiction rather than a sample, standard errors were not calculated and statistical testing for differences in estimates across years were not performed.\n\n\u2022 Laws and policies regarding the submission of vaccination data to an IIS vary by state, which may impact the completeness of vaccination coverage reflected for a jurisdiction. More information on laws and policies are found at https://www.cdc.gov/vaccines/programs/iis/policy-legislation.html.\n\n\u2022 Coverage estimates based on IIS data are expected to differ from National Immunization Survey (NIS) estimates for children (https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-coverage-race.html)\nand adults (https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-adult-coverage.html) because NIS estimates are based on a sample that may not be representative after survey weighting and vaccination status is determined by survey respondent rather than vaccine records or administrations, and quality and completeness of IIS data may vary across jurisdictions. In general, NIS estimates tend to overestimate coverage due to overreporting and IIS estimates may underestimate coverage due to incompleteness of data in certain jurisdictions.",
-            "title": "Monthly Cumulative Number and Percent of Persons Who Received \u22651 Influenza Vaccination Doses, by Flu Season, Age Group, and Jurisdiction",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35166,49 +35147,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Jurisdictions - States, District of Columbia, Islands, and US cities",
+            "identifier": "https://data.cdc.gov/api/views/udwr-3en6",
+            "issued": "2024-02-01",
+            "keyword": [
+                "flu vaccination",
+                "iis",
+                "immunization information system",
+                "vaccination coverage"
+            ],
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2024-09-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "Jurisdictions - States, District of Columbia, Islands, and US cities",
+            "temporal": "Flu Seasons-2021-22, 2022-23, 2023-24",
             "theme": [
                 "Flu Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Monthly Cumulative Number and Percent of Persons Who Received \u22651 Influenza Vaccination Doses, by Flu Season, Age Group, and Jurisdiction"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/khjf-tq2k",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "cryptosporidiosis",
-                "cyclosporiasis",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/khjf-tq2k",
             "description": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1I. Cryptosporidiosis to Cyclosporiasis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35231,42 +35209,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/khjf-tq2k",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "cryptosporidiosis",
+                "cyclosporiasis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/khjf-tq2k",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1I. Cryptosporidiosis to Cyclosporiasis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://rxnav.nlm.nih.gov/RxNav-in-a-Box.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "drugs",
-                "health data standards",
-                "software",
-                "supplements",
-                "terminologies"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/pai2-u4yd",
             "description": "RxNav-in-a-Box provides users with a locally-installable RxNav (https://rxnav.nlm.nih.gov/RxNavDoc.html) and RESTful companion APIs, including RxNorm, RxTerms, RxClass, RxCUI history, and drug-drug interactions.",
-            "title": "RxNav-in-a-Box",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35275,35 +35255,42 @@
                     "title": "RxNav-in-a-Box - Download"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/pai2-u4yd",
+            "issued": "2021-06-30",
+            "keyword": [
+                "drugs",
+                "health data standards",
+                "software",
+                "supplements",
+                "terminologies"
+            ],
+            "landingPage": "https://rxnav.nlm.nih.gov/RxNav-in-a-Box.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Drugs and Chemicals"
-            ]
+            ],
+            "title": "RxNav-in-a-Box"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ha59-j5yk",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Division of Field Studies and Evaluation, Hazard Evaluation and Technical Assistance Branch",
                 "hasEmail": "mailto:HHERequestHelp@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ha59-j5yk",
             "description": "The April 20, 2010, explosion and collapse of the BP Deepwater Horizon oil platform in the Gulf of Mexico resulted in the release of millions of barrels of oil into Gulf waters. The response to this disaster involved the efforts of tens of thousands of workers in a variety of capacities across Louisiana, Mississippi, Alabama, Florida, Texas, and in the Gulf of Mexico itself. The diverse work included oil and tar ball removal from beaches, oil skimming and booming near shores, burning of surface oil near the source of the oil release, surface application of dispersant by vessels and aircraft, and containment and recovery work on vessels at the release site. The nature of these activities raised concerns about potential occupational exposures to chemical and physical hazards and mental stressors.\n\nNIOSH investigators conducted health hazard evaluations (HHEs) of Deepwater Horizon Response onshore and offshore workers. The goals of the NIOSH HHE assessments were to describe acute health effects, evaluate occupational exposures in qualitative or quantitative assessments, and generate hypotheses regarding symptoms potentially related to work activities. Environmental air samples were collected in support of the goals.\n\nNIOSH investigators conducted the following exposure evaluations:\n\n- We conducted evaluations on board vessels releasing dispersant. These vessels were deployed to perform small\u2010scale releases of dispersant in an area with surface oil contamination.\n- We assessed exposures during in\u2010situ (i.e., on site) burns of surface oil.\n- We assessed exposures on fishing and shrimping trawlers in the Vessels of Opportunity (VoO) program that were assigned to remove surface oil by booming and skimming.\n- We assessed exposures aboard vessels located at the Deepwater Horizon incident site.\n- We assessed exposures during boom and vessel decontamination operations.",
-            "title": "Deepwater Horizon Response Air Sampling Data",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35311,20 +35298,44 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ha59-j5yk",
+            "issued": "2024-11-13",
+            "landingPage": "https://data.cdc.gov/d/ha59-j5yk",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Deepwater Horizon Response Air Sampling Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/8yuv-updi",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "description": "This data set includes annual counts and percentages of Medicaid and Children\u2019s Health Insurance Program (CHIP) enrollees who received mental health (MH) or substance use disorder (SUD) services, overall and by six subpopulation topics: age group, sex or gender identity, race and ethnicity, urban or rural residence, eligibility category, and primary language.\r\nThese results were generated using Transformed Medicaid Statistical Information System (T-MSIS) Analytic Files (TAF) Release 1 data and the Race/Ethnicity Imputation Companion File. This data set includes Medicaid and CHIP enrollees in all 50 states, the District of Columbia, Puerto Rico, and the U.S. Virgin Islands, ages 12 to 64 at the end of the calendar year, who were not dually eligible for Medicare and were continuously enrolled with comprehensive benefits for 12 months, with no more than one gap in enrollment exceeding 45 days. Enrollees who received services for both an MH condition and SUD in the year are counted toward both condition categories. Enrollees in Guam, American Samoa, the Northern Mariana Islands, and select states with TAF data quality issues are not included. Results shown for the race and ethnicity subpopulation topic exclude enrollees in the U.S. Virgin Islands. Results shown for the primary language subpopulation topic exclude select states with data quality issues with the primary language variable in TAF. Some rows in the data set have a value of \"DS,\" which indicates that data were suppressed according to the Centers for Medicare & Medicaid Services\u2019 Cell Suppression Policy for values between 1 and 10.\r\nThis data set is based on the brief: \"Medicaid and CHIP enrollees who received mental health or SUD services in 2020.\" Enrollees are assigned to an age group subpopulation using age as of December 31st of the calendar year. Enrollees are assigned to a sex or gender identity subpopulation using their latest reported sex in the calendar year. Enrollees are assigned to a race and ethnicity subpopulation using the state-reported race and ethnicity information in TAF when it is available and of good quality; if it is missing or unreliable, race and ethnicity is indirectly estimated using an enhanced version of Bayesian Improved Surname Geocoding (BISG) (Race and ethnicity of the national Medicaid and CHIP population in 2020). Enrollees are assigned to an urban or rural subpopulation based on the 2010 Rural-Urban Commuting Area (RUCA) code associated with their home or mailing address ZIP code in TAF (Rural Medicaid and CHIP enrollees in 2020). Enrollees are assigned to an eligibility category subpopulation using their latest reported eligibility group code, CHIP code, and age in the calendar year. Enrollees are assigned to a primary language subpopulation based on their reported ISO language code in TAF (English/missing, Spanish, and all other language codes) (Primary Language). Please refer to the full brief for additional context about the methodology and detailed findings. Future updates to this data set will include more recent data years as the TAF data become available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mh-and-sud-services-2020-2022-01162025.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "8062e2f4-4c0a-41c9-8217-979468a80986",
             "issued": "2025-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
             "keyword": [
                 "behavioral health",
                 "chip",
@@ -35334,57 +35345,31 @@
                 "substance use disorder",
                 "t-msis analytic files"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Medicaid.gov",
-                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/d/8yuv-updi",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Medicare & Medicaid Services"
             },
-            "identifier": "8062e2f4-4c0a-41c9-8217-979468a80986",
-            "description": "This data set includes annual counts and percentages of Medicaid and Children\u2019s Health Insurance Program (CHIP) enrollees who received mental health (MH) or substance use disorder (SUD) services, overall and by six subpopulation topics: age group, sex or gender identity, race and ethnicity, urban or rural residence, eligibility category, and primary language.\r\nThese results were generated using Transformed Medicaid Statistical Information System (T-MSIS) Analytic Files (TAF) Release 1 data and the Race/Ethnicity Imputation Companion File. This data set includes Medicaid and CHIP enrollees in all 50 states, the District of Columbia, Puerto Rico, and the U.S. Virgin Islands, ages 12 to 64 at the end of the calendar year, who were not dually eligible for Medicare and were continuously enrolled with comprehensive benefits for 12 months, with no more than one gap in enrollment exceeding 45 days. Enrollees who received services for both an MH condition and SUD in the year are counted toward both condition categories. Enrollees in Guam, American Samoa, the Northern Mariana Islands, and select states with TAF data quality issues are not included. Results shown for the race and ethnicity subpopulation topic exclude enrollees in the U.S. Virgin Islands. Results shown for the primary language subpopulation topic exclude select states with data quality issues with the primary language variable in TAF. Some rows in the data set have a value of \"DS,\" which indicates that data were suppressed according to the Centers for Medicare & Medicaid Services\u2019 Cell Suppression Policy for values between 1 and 10.\r\nThis data set is based on the brief: \"Medicaid and CHIP enrollees who received mental health or SUD services in 2020.\" Enrollees are assigned to an age group subpopulation using age as of December 31st of the calendar year. Enrollees are assigned to a sex or gender identity subpopulation using their latest reported sex in the calendar year. Enrollees are assigned to a race and ethnicity subpopulation using the state-reported race and ethnicity information in TAF when it is available and of good quality; if it is missing or unreliable, race and ethnicity is indirectly estimated using an enhanced version of Bayesian Improved Surname Geocoding (BISG) (Race and ethnicity of the national Medicaid and CHIP population in 2020). Enrollees are assigned to an urban or rural subpopulation based on the 2010 Rural-Urban Commuting Area (RUCA) code associated with their home or mailing address ZIP code in TAF (Rural Medicaid and CHIP enrollees in 2020). Enrollees are assigned to an eligibility category subpopulation using their latest reported eligibility group code, CHIP code, and age in the calendar year. Enrollees are assigned to a primary language subpopulation based on their reported ISO language code in TAF (English/missing, Spanish, and all other language codes) (Primary Language). Please refer to the full brief for additional context about the methodology and detailed findings. Future updates to this data set will include more recent data years as the TAF data become available.",
-            "title": "Medicaid and CHIP enrollees who received mental health or SUD services",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://download.medicaid.gov/data/mh-and-sud-services-2020-2022-01162025.csv",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "Medicaid and CHIP enrollees who received mental health or SUD services"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/8yvk-aiuk",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-07-22",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-21",
-            "keyword": [
-                "medicaid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "7459d190-e592-42e0-9b66-6f4e7e05eb9b",
             "description": "Dataset.",
-            "title": "2021 Managed Care Programs By State",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35392,39 +35377,35 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "7459d190-e592-42e0-9b66-6f4e7e05eb9b",
+            "issued": "2023-07-22",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/8yvk-aiuk",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-07-21",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "2021 Managed Care Programs By State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/puzh-5wax",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-07-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-07-27",
-            "keyword": [
-                "county",
-                "division of parasitic diseases and malaria",
-                "malaria",
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kimberly E. Mace",
                 "hasEmail": "mailto:igd3@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/puzh-5wax",
             "description": "This dataset contains deidentified data from the National Malaria Surveillance System on the number of malaria cases reported in the United States in 2017, by county. Only counties reporting five or more cases are included in this dataset.",
-            "title": "Number of Reported Malaria Cases by County\u2014 United States, 2017",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35447,40 +35428,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/puzh-5wax",
+            "issued": "2020-07-27",
+            "keyword": [
+                "county",
+                "division of parasitic diseases and malaria",
+                "malaria",
+                "united states"
+            ],
+            "landingPage": "https://data.cdc.gov/d/puzh-5wax",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2020-07-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Global Health"
-            ]
+            ],
+            "title": "Number of Reported Malaria Cases by County\u2014 United States, 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/8zgh-isvf",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-03-16",
-            "@type": "dcat:Dataset",
-            "modified": "2017-08-03",
-            "keyword": [
-                "core sets",
-                "performance rates",
-                "quality measures"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:no-reply@data.medicaid.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "2b6a0ec0-efe6-5aec-9fe4-e168b8b6f553",
             "description": "Performance rates on frequently reported health care quality measures in the CMS Medicaid/CHIP Child and Adult Core Sets, for FFY 2014 reporting.  Dataset contains both child and adult measures. Source: Mathematica analysis of FFY 2014 Child and Adult CARTS reports as of May 8, 2015, as published in the 2015 Secretary's Reports on the Quality of Care in Medicaid/CHIP.",
-            "title": "2014 Child and Adult Health Care Quality Measures",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35489,42 +35472,41 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "2b6a0ec0-efe6-5aec-9fe4-e168b8b6f553",
+            "issued": "2016-03-16",
+            "keyword": [
+                "core sets",
+                "performance rates",
+                "quality measures"
+            ],
+            "landingPage": "https://healthdata.gov/d/8zgh-isvf",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2017-08-03",
+            "programCode": [
+                "009:076"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Quality"
-            ]
+            ],
+            "title": "2014 Child and Adult Health Care Quality Measures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/child-coverage-vaccination.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-10-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024 & 2024-2025",
-            "modified": "2025-01-29",
-            "keyword": [
-                "flu vaccination",
-                "nis-ccm",
-                "nis-flu"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/qr63-vqq5",
             "description": "\u2022 Weekly Cumulative Influenza Vaccination Coverage and Comparison Between 2023-24 and 2024-25 by Jurisdiction, Children 6 Months\u201317, United States.\n\n\u2022 Weekly Influenza vaccination coverage and parental intent for vaccination among children is calculated using data from the National Immunization Survey\u2013Flu (NIS\u2013Flu) (https://www.cdc.gov/nis/about/index.html). NIS\u2013Flu is a national random-digit-dialed cellular telephone survey of households with children ages 6 months\u201317 years conducted during October-June. The respondent to a NIS\u2013Flu survey is a parent or guardian who said they were knowledgeable about the child\u2019s vaccination history. All estimates are based upon parental report of receipt of vaccination and month of that vaccination.",
-            "title": "Weekly Cumulative Influenza Vaccination Coverage and Comparison Between 2023\u201324 and 2024\u201325\u00b1 by Jurisdiction, Children 6 Months\u201317 Years, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35547,44 +35529,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/qr63-vqq5",
+            "issued": "2024-10-23",
+            "keyword": [
+                "flu vaccination",
+                "nis-ccm",
+                "nis-flu"
+            ],
+            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/child-coverage-vaccination.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2023-2024 & 2024-2025",
             "theme": [
                 "Child Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Influenza Vaccination Coverage and Comparison Between 2023\u201324 and 2024\u201325\u00b1 by Jurisdiction, Children 6 Months\u201317 Years, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6tmq-h6uy",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6tmq-h6uy",
             "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2014 national data: National Occupant Protection Use Survey (NOPUS), 2014.  Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 state data: Seat Belt Use in 2014- Use Rates in the States and Territories",
-            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 1 - Boston",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35607,120 +35590,124 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6tmq-h6uy",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6tmq-h6uy",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-09-14",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Motor Vehicle"
-            ]
+            ],
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 1 - Boston"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/nlmcatalog",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/a392-5wn4",
             "description": "The NLM Catalog provides access to NLM bibliographic data for journals, books, audiovisuals, computer software, electronic resources and other materials. Links to the library's holdings in LocatorPlus, NLM's online public access catalog, are also provided.",
-            "title": "NLM Catalog",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/nlmcatalog",
-                    "description": "Search the NLM Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "Search the NLM Catalog",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/nlmcatalog",
+                    "mediaType": "text/html",
                     "title": "NLM Catalog - Query Interface"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/nlmcatalog/journals",
-                    "description": "NLM Catalog search of the subset of journals that are referenced in NCBI database records",
                     "@type": "dcat:Distribution",
+                    "description": "NLM Catalog search of the subset of journals that are referenced in NCBI database records",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/nlmcatalog/journals",
+                    "mediaType": "text/html",
                     "title": "Journals referenced in the NCBI Databases - Query Interface"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://journal-reports.nlm.nih.gov/broad-subjects/",
-                    "description": "Broad Subject Terms are assigned by NLM\u00ae to MEDLINE\u00ae journals to describe the journal's overall scope. All of these broad subject terms (about 120) are valid MeSH\u00ae headings.  The links on this page run a search in the NLM Catalog. ",
                     "@type": "dcat:Distribution",
+                    "description": "Broad Subject Terms are assigned by NLM\u00ae to MEDLINE\u00ae journals to describe the journal's overall scope. All of these broad subject terms (about 120) are valid MeSH\u00ae headings.  The links on this page run a search in the NLM Catalog. ",
+                    "downloadURL": "https://journal-reports.nlm.nih.gov/broad-subjects/",
+                    "mediaType": "text/html",
                     "title": "Broad Subject Terms for Indexed Journals - Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/a392-5wn4",
+            "issued": "2021-08-26",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/nlmcatalog",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Other"
-            ]
+            ],
+            "title": "NLM Catalog"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.physionet.org/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "national-institutes-of-health-nih"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RAVICHANDRAN, VEERASAMY\u00a0",
                 "hasEmail": "mailto:veerasamy.ravichandra@nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "2f84e873-8e3a-4cb7-b5a3-c26ccd91f080",
+            "dataQuality": true,
             "description": "<p>The PhysioNet Resource is intended to stimulate current research and new investigations in the study of complex biomedical and physiologic signals. It offers free web access to large collections of recorded physiologic signals (PhysioBank) and related open-source software (PhysioToolkit).</p>",
-            "title": "PhysioNet",
+            "identifier": "2f84e873-8e3a-4cb7-b5a3-c26ccd91f080",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.physionet.org/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
             "programCode": [
                 "009:048"
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "PhysioNet"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7ehz-refy",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-12-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Toxicology and Molecular Biology Branch, HELD",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7ehz-refy",
             "description": "Gulf War Illness (GWI) is a disorder experienced by one-third of the veterans of the 1990-91 Gulf War, with symptoms including fatigue, chronic pain, respiratory and memory problems. Exposure to toxic chemicals during the war, such as oil well fire smoke, pesticides, physiological stress, and nerve agents, is thought to have triggered abnormal neuroinflammatory responses that contribute to GWI. Previous studies using animal models have indicated that combined exposure to high physiological stress and GW-relevant organophosphates, such as sarin nerve agent and chlorpyrifos and dichlorvos, produces neuroinflammation and changes in diffusion magnetic resonance imaging (MRI) measures, suggesting a neuroimmune basis for GWI. In the current study, we examined brain structure and immune function of a chronic rat model of GWI and showed that a combination of long-term corticosterone treatment (CORT, to mimic high physiological stress) and diisopropyl fluorophosphate exposure (DFP, to mimic sarin exposure) resulted in elevations of multiple inflammatory cytokines, an increased activated microglial population, and disrupted brain microstructure in the hippocampal regions. Moreover, prior exposures to these agents modeling the \u201cin-theater,\u201d initiating exposure conditions experienced by veterans with GWI can induce long-term alterations in neuroimmune signaling, resulting in an exacerbated neuroinflammatory response to future immune challenges.  The goal of the study was to establish a long-term model of GWI in rats that would be more relevant to the current state of ill veterans.  As such, rats were initially exposed to the stress hormone corticosterone (CORT) for 1 week followed by a single exposure to the sarin surrogate diisopropyl fluorophosphate, to mimic \u201cin-theater\u201d conditions of high physiological stress and nerve agent exposure.  This initial exposure was followed up with 4 weeks of intermittent re-exposure to week-long bouts of CORT and a final exposure to the prototypical inflammagen, lipopolysaccharide (LPS) to mimic a systemic inflammatory challenge.",
-            "title": "Nerve agent exposure and physiological stress alter brain microstructure and immune profiles after inflammatory challenge in a long-term animal model of Gulf War Illness",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35728,35 +35715,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7ehz-refy",
+            "issued": "2024-12-18",
+            "landingPage": "https://data.cdc.gov/d/7ehz-refy",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Nerve agent exposure and physiological stress alter brain microstructure and immune profiles after inflammatory challenge in a long-term animal model of Gulf War Illness"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9ziv-gyv9",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chemical and Biological Monitoring Branch (CBMB), Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9ziv-gyv9",
             "description": "The application of sodium hypochlorite bleach to surfaces causes the release of chlorine (Cl2) and hypochlorous acid (HOCl) into the gas phase where reactions with organic compounds can occur. The purpose of the current study was to investigate the reaction products generated from gas-phase bleach oxidants and limonene, a fragrance compound commonly found in indoor air due to personal care products and cleaning products.  Gas-phase reactions were prepared in Teflon chambers housing HOCl, Cl2, and limonene.  The resulting chemical products were collected and analyzed using gas-phase preconcentration following by gas chromatography and high-resolution mass spectrometry.  Several chlorinated products were detected including a limonene chlorohydrin and limonene species containing one, two, and three chlorines.  Product concentration and yields were estimated for the most abundant products, and greater than 80% of the transformed limonene was represented in the detected products.  Temporal sampling of the reactions allowed time courses to be plotted for limonene transformation and chlorinated limonene product generation under different conditions including the treatments of HOCl/Cl2, Cl2 only, high vs. low relative humidity, and +/- ozone. These experiments provide additional insight into the chemical transformations initiated by sodium hypochlorite bleach oxidants in the gas phase which may be of interest to human health.",
-            "title": "Factors affecting chlorinated product formation from sodium hypochlorite bleach and limonene reactions in the gas phase",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35764,40 +35751,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9ziv-gyv9",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/9ziv-gyv9",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Factors affecting chlorinated product formation from sodium hypochlorite bleach and limonene reactions in the gas phase"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/b7pe-5nws",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-02-24",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-17",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "vaccination"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ASPA Media",
                 "hasEmail": "mailto:media@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/b7pe-5nws",
             "description": "New weekly allocations of doses are posted every Tuesday.  Beginning the following Thursday, states can begin ordering doses from that week\u2019s new allocation of 1st doses.  Beginning two weeks (Pfizer) or three weeks (Moderna) from the following Sunday, states can begin ordering doses from that week\u2019s new allocation of 2nd doses. After doses are ordered by states, shipments begin the following Monday. The entire order may not arrive in one shipment or on one day, but over the course of the week.\n\nSecond doses are opened up for orders on Sundays, at the appropriate interval two or three weeks later according to the manufacturer\u2019s label, with shipments occurring after jurisdictions place orders. \n\nShipments of an FDA-authorized safe and effective COVID-19 vaccine continue to arrive at sites across America. Vaccinations began on December 14, 2020. \n\nhttps://www.hhs.gov/coronavirus/covid-19-vaccines/index.html\n\nPfizer Vaccine Data - https://data.cdc.gov/Vaccinations/COVID-19-Vaccine-Initial-Allocations-Pfizer/saz5-9hgg\n\nJanssen Vaccine Data - https://data.cdc.gov/Vaccinations/COVID-19-Vaccine-Distribution-Allocations-by-Juris/w9zu-fywh",
-            "title": "COVID-19 Vaccine Distribution Allocations by Jurisdiction - Moderna",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35820,40 +35802,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/b7pe-5nws",
+            "issued": "2021-02-24",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/b7pe-5nws",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2021-06-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "COVID-19 Vaccine Distribution Allocations by Jurisdiction - Moderna"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/rands/work.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-09-14",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-06-09/2021-06-30",
-            "modified": "2023-04-24",
-            "keyword": [
-                "covid-19",
-                "rands"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/qgkx-mswu",
             "description": "The Research and Development Survey (RANDS) is a platform designed for conducting survey question evaluation and statistical research. RANDS is an ongoing series of surveys from probability-sampled commercial survey panels used for methodological research at the National Center for Health Statistics (NCHS). RANDS estimates are generated using an experimental approach that differs from the survey design approaches generally used by NCHS, including possible biases from different response patterns and sampling frames as well as increased variability from lower sample sizes. Use of the RANDS platform allows NCHS to produce more timely data than would be possible using traditional data collection methods. RANDS is not designed to replace NCHS\u2019 higher quality, core data collections. Below are experimental estimates of loss of work due to illness with coronavirus for three rounds of RANDS during COVID-19. Data collection for the three rounds of RANDS during COVID-19 occurred between June 9, 2020 and July 6, 2020, August 3, 2020 and August 20, 2020, and May 17, 2021 and June 30, 2021. Information needed to interpret these estimates can be found in the Technical Notes. RANDS during COVID-19 included a question about the inability to work due to being sick or having a family member sick with COVID-19. The National Health Interview Survey, conducted by NCHS, is the source for high-quality data to monitor work-loss days and work limitations in the United States. For example, in 2018, 42.7% of adults aged 18 and over missed at least 1 day of work in the previous year due to illness or injury and 9.3% of adults aged 18 to 69 were limited in their ability to work or unable to work due to physical, mental, or emotional problems. The experimental estimates on this page are derived from RANDS during COVID-19 and show the percentage of U.S. adults who did not work for pay at a job or business, at any point, in the previous week because either they or someone in their family was sick with COVID-19. Technical Notes: https://www.cdc.gov/nchs/covid19/rands/work.htm#limitations",
-            "title": "Loss of Work Due to Illness from COVID-19",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35876,51 +35859,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/qgkx-mswu",
+            "issued": "2020-09-14",
+            "keyword": [
+                "covid-19",
+                "rands"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/rands/work.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-04-24",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
+            "temporal": "2020-06-09/2021-06-30",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Loss of Work Due to Illness from COVID-19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/national-survey-family-growth",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-11-05",
-            "temporal": "1973-01-01T00:00:00-05:00/2010-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "children's health",
-                "families",
-                "fertility",
-                "health",
-                "other",
-                "population statistics",
-                "rape",
-                "sexual assault"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Survey of Family Growth",
                 "hasEmail": "mailto:nsfg@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
-            },
-            "identifier": "b7600411-7e43-4c17-91b8-4627322de255",
+            "dataQuality": true,
+            "describedBy": "http://www.cdc.gov/nchs/nsfg/nsfg_questionnaires.htm",
             "description": "<p>The National Survey of Family Growth (NSFG) gathers information on family life, marriage and divorce, pregnancy, infertility, use of contraception, and men's and women's health. The survey results are used by the U.S. Department of Health and Human Services and others to plan health services and health education programs, and to do statistical studies of families, fertility, and health.  Years included:  1973, 1976, 1982, 1988, 1995, 2002, 2006-2010;  Data use agreement at time of file download:</p>",
-            "title": "National Survey of Family Growth",
-            "programCode": [
-                "006:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35929,68 +35907,101 @@
                     "title": "CSV "
                 }
             ],
-            "describedBy": "http://www.cdc.gov/nchs/nsfg/nsfg_questionnaires.htm",
-            "dataQuality": true,
+            "identifier": "b7600411-7e43-4c17-91b8-4627322de255",
+            "issued": "2012-11-05",
+            "keyword": [
+                "children's health",
+                "families",
+                "fertility",
+                "health",
+                "other",
+                "population statistics",
+                "rape",
+                "sexual assault"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-family-growth",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "006:008"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "temporal": "1973-01-01T00:00:00-05:00/2010-12-31T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "National Survey of Family Growth"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/97m5-2uks",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-05",
-            "keyword": [
-                "chip",
-                "dq atlas",
-                "medicaid",
-                "program enrollment",
-                "t-msis analytic files"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "3da9f4e6-7976-43a8-8d1b-72f2c557a5ca",
             "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by program type (Medicaid or CHIP). \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topics Medicaid-only Enrollment and M-CHIP and S-CHIP Enrollment. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Program Information for Medicaid and CHIP Beneficiaries by Month",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/ProgramType-montly.csv",
-                    "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by program type (Medicaid or CHIP). \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topics Medicaid-only Enrollment and M-CHIP and S-CHIP Enrollment. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by program type (Medicaid or CHIP). \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topics Medicaid-only Enrollment and M-CHIP and S-CHIP Enrollment. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/ProgramType-montly.csv",
+                    "mediaType": "text/csv",
                     "title": "Program Information for Medicaid and CHIP Beneficiaries by Month"
                 }
             ],
+            "identifier": "3da9f4e6-7976-43a8-8d1b-72f2c557a5ca",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "medicaid",
+                "program enrollment",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/97m5-2uks",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-01-05",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Enrollment"
-            ]
+            ],
+            "title": "Program Information for Medicaid and CHIP Beneficiaries by Month"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://labels.fda.gov/",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "openFDA",
+                "hasEmail": "mailto:open@fda.hhs.gov"
+            },
+            "description": "The drug labels and other drug-specific information on this Web site represent the most recent drug listing information companies have submitted to the Food and Drug Administration (FDA). (See 21 CFR part 207.) The drug labeling and other information has been reformatted to make it easier to read but its content has neither been altered nor verified by FDA. The drug labeling on this Web site may not be the labeling on currently distributed products or identical to the labeling that is approved. Most OTC drugs are not reviewed and approved by FDA, however they may be marketed if they comply with applicable regulations and policies described in monographs. Drugs marked 'OTC monograph final' or OTC monograph not final' are not checked for conformance to the monograph. Drugs marked 'unapproved medical gas', 'unapproved homeopathic' or 'unapproved drug other' on this Web site have not been evaluated by FDA for safety and efficacy and their labeling has not been approved. In addition, FDA is not aware of scientific evidence to support homeopathy as effective.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm240580.htm",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "ff9c9ee2-8c73-4142-b21f-2b694db8f783",
             "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-26",
             "keyword": [
                 "community health",
                 "drug",
@@ -36000,107 +36011,77 @@
                 "label repository",
                 "labels fda gov"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "openFDA",
-                "hasEmail": "mailto:open@fda.hhs.gov"
-            },
+            "landingPage": "http://labels.fda.gov/",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-26",
+            "programCode": [
+                "009:002"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "ff9c9ee2-8c73-4142-b21f-2b694db8f783",
-            "description": "The drug labels and other drug-specific information on this Web site represent the most recent drug listing information companies have submitted to the Food and Drug Administration (FDA). (See 21 CFR part 207.) The drug labeling and other information has been reformatted to make it easier to read but its content has neither been altered nor verified by FDA. The drug labeling on this Web site may not be the labeling on currently distributed products or identical to the labeling that is approved. Most OTC drugs are not reviewed and approved by FDA, however they may be marketed if they comply with applicable regulations and policies described in monographs. Drugs marked 'OTC monograph final' or OTC monograph not final' are not checked for conformance to the monograph. Drugs marked 'unapproved medical gas', 'unapproved homeopathic' or 'unapproved drug other' on this Web site have not been evaluated by FDA for safety and efficacy and their labeling has not been approved. In addition, FDA is not aware of scientific evidence to support homeopathy as effective.",
-            "title": "FDA Online Label Repository",
-            "programCode": [
-                "009:002"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm240580.htm",
-                    "mediaType": "application/zip"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "FDA Online Label Repository"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/99j2-nua8",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-10",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "749f6075-a81d-5309-9b49-b213d4170882",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet state v2.10.64 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/state.csv",
-                    "description": "CoreSet state v2.10.64 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet state v2.10.64 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/state.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet state v2.10.64 (coreset-etl-test)"
                 }
             ],
+            "identifier": "749f6075-a81d-5309-9b49-b213d4170882",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/99j2-nua8",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2025-01-10",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSet state v2.10.64 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://accessgudid.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-07-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-08",
-            "keyword": [
-                "api",
-                "dataset",
-                "health data standards",
-                "medical devices",
-                "terminologies"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/eef4-55cr",
+            "dataQuality": true,
             "description": "The Global Unique Device Identification Database (GUDID) contains key device identification information submitted to the FDA about medical devices that have Unique Device Identifiers (UDI).",
-            "title": "AccessGUDID",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36121,97 +36102,90 @@
                     "title": "AccessGUDID API"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/eef4-55cr",
+            "issued": "2016-07-08",
+            "keyword": [
+                "api",
+                "dataset",
+                "health data standards",
+                "medical devices",
+                "terminologies"
+            ],
+            "landingPage": "https://accessgudid.nlm.nih.gov/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-08",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Consumer Health"
-            ]
+            ],
+            "title": "AccessGUDID"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/9ash-kwxc",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-04-21",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-08",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "a7145ad2-4779-506c-8823-7651a651e031",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard measure_value v2.11.16 (cmsdev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/measure_value.csv",
-                    "description": "Scorecard measure_value v2.11.16 (cmsdev)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard measure_value v2.11.16 (cmsdev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard measure_value v2.11.16 (cmsdev)"
                 }
             ],
+            "identifier": "a7145ad2-4779-506c-8823-7651a651e031",
+            "issued": "2023-04-21",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/9ash-kwxc",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2025-01-08",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Scorecard measure_value v2.11.16 (cmsdev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/medicare-restricted.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2023-12-08",
-            "@type": "dcat:Dataset",
-            "temporal": "1999/2013",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data-linkage/cms/nchs-cms_medicare_linked_data-list_of_variables.pdf"
-            ],
-            "keyword": [
-                "linked medicare data",
-                "nhcs",
-                "research-data-center",
-                "sdoh-access-to-health-care",
-                "sdoh-source-of-health-care",
-                "sdoh-use-of-health-care"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCHS Data Linkage Program",
                 "hasEmail": "mailto:DataLinkage@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9fpg-7hvw",
-            "description": "NCHS has linked data from various surveys with 1999-2013 Medicare program enrollment and health care utilization and expenditure data from the Centers for Medicare & Medicaid Services (CMS). Linkage of the NCHS survey participants with the CMS Medicare data provides the opportunity to study changes in health status, health care utilization and costs, and prescription drug use among Medicare enrollees. Medicare is the federal health insurance program for people who are 65 or older, certain younger people with disabilities, and people with End-Stage Renal Disease.",
-            "title": "NCHS Survey Data Linked to Centers for Medicare & Medicaid Services (CMS) 1999-2013 Medicare Data",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/nchs-cms_medicare_linked_data_match_rate_tables.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "NCHS has linked data from various surveys with 1999-2013 Medicare program enrollment and health care utilization and expenditure data from the Centers for Medicare & Medicaid Services (CMS). Linkage of the NCHS survey participants with the CMS Medicare data provides the opportunity to study changes in health status, health care utilization and costs, and prescription drug use among Medicare enrollees. Medicare is the federal health insurance program for people who are 65 or older, certain younger people with disabilities, and people with End-Stage Renal Disease.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36219,51 +36193,50 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/nchs-cms_medicare_linked_data_match_rate_tables.pdf",
+            "identifier": "https://data.cdc.gov/api/views/9fpg-7hvw",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2023-12-08",
+            "keyword": [
+                "linked medicare data",
+                "nhcs",
+                "research-data-center",
+                "sdoh-access-to-health-care",
+                "sdoh-source-of-health-care",
+                "sdoh-use-of-health-care"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/medicare-restricted.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/data-linkage/cms/nchs-cms_medicare_linked_data-list_of_variables.pdf"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "temporal": "1999/2013",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Survey Data Linked to Centers for Medicare & Medicaid Services (CMS) 1999-2013 Medicare Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/akn2-qxic",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "N/A",
-            "issued": "2023-05-25",
-            "@type": "dcat:Dataset",
-            "temporal": "5/11/2023 \u2013 5/3/2024",
-            "modified": "2025-01-17",
-            "references": [
-                "CDT county-level hospital data displays: https://covid.cdc.gov/covid-data-tracker/#cases_new-admissions-rate-county  NHSN Hospital Data Reporting: https://www.cdc.gov/nhsn/covid19/hospital-reporting.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fnhsn%2Fcovid19%2Ftransition.html  Full reporting guidance: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf"
-            ],
-            "keyword": [
-                "admissions",
-                "coronavirus",
-                "covid-19",
-                "hospital capacity",
-                "hospitalizations",
-                "hospital occupancy",
-                "icu beds",
-                "inpatient beds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC-INFO",
                 "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/akn2-qxic",
             "description": "<b>Note:</b> After May 3, 2024, this dataset will no longer be updated because hospitals are no longer required to report data on COVID-19 hospital admissions, hospital capacity, or occupancy data to HHS through CDC\u2019s National Healthcare Safety Network (NHSN). The related CDC COVID Data Tracker site was revised or retired on May 10, 2023.\n\n<b>Note:</b>\n<b>May 3,2024:</b> Due to incomplete or missing hospital data received for the April 21,2024 through April 27, 2024 reporting period, the COVID-19 Hospital Admissions Level could not be calculated for CNMI and will be reported as \u201cNA\u201d or \u201cNot Available\u201d in the COVID-19 Hospital Admissions Level data released on May 3, 2024.\n\nThis dataset represents COVID-19 hospitalization data and metrics aggregated to county or county-equivalent, for all counties or county-equivalents (including territories) in the United States. COVID-19 hospitalization data are reported to CDC\u2019s National Healthcare Safety Network, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN and included in this dataset represent aggregated counts and include metrics capturing information specific to COVID-19 hospital admissions, and inpatient and ICU bed capacity occupancy.\n\n<b>Reporting information:</b><ul><li>As of December 15, 2022, COVID-19 hospital data are required to be reported to  NHSN, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Prior to December 15, 2022, hospitals reported data directly to the U.S. Department of Health and Human Services (HHS) or via a state submission for collection in the HHS Unified Hospital Data Surveillance System (UHDSS). </li><li>While CDC reviews these data for errors and corrects those found, some reporting errors might still exist within the data. To minimize errors and inconsistencies in data reported, CDC removes outliers before calculating the metrics. CDC and partners work with reporters to correct these errors and update the data in subsequent weeks.</li><li>Many hospital subtypes, including acute care and critical access hospitals, as well as Veterans Administration, Defense Health Agency, and Indian Health Service hospitals, are included in the metric calculations provided in this report. Psychiatric, rehabilitation, and religious non-medical hospital types are excluded from calculations.  </li><li>Data are aggregated and displayed for hospitals with the same Centers for Medicare and Medicaid Services (CMS) Certification Number (CCN), which are assigned by CMS to counties based on the CMS Provider of Services files. </li> <li>Full details on COVID-19 hospital data reporting guidance can be found here: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf</li></ul>\n<b>Calculation of county-level hospital metrics:</b><ul><li>County-level hospital data are derived using calculations performed at the Health Service Area (HSA) level. An HSA is defined by CDC\u2019s National Center for Health Statistics as a geographic area containing at least one county which is self-contained with respect to the population\u2019s provision of routine hospital care. Every county in the United States is assigned to an HSA, and each HSA must contain at least one hospital. Therefore, use of HSAs in the calculation of local hospital metrics allows for more accurate characterization of the relationship between health care utilization and health status at the local level. </li><li>Data presented at the county-level represent admissions, hospital inpatient and ICU bed capacity and occupancy among hosp",
-            "title": "Weekly United States COVID-19 Hospitalization Metrics by County \u2013 ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36286,44 +36259,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/akn2-qxic",
+            "issued": "2023-05-25",
+            "keyword": [
+                "admissions",
+                "coronavirus",
+                "covid-19",
+                "hospital capacity",
+                "hospitalizations",
+                "hospital occupancy",
+                "icu beds",
+                "inpatient beds"
+            ],
+            "landingPage": "https://data.cdc.gov/d/akn2-qxic",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "No longer updated (dataset archived)",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "CDT county-level hospital data displays: https://covid.cdc.gov/covid-data-tracker/#cases_new-admissions-rate-county  NHSN Hospital Data Reporting: https://www.cdc.gov/nhsn/covid19/hospital-reporting.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fnhsn%2Fcovid19%2Ftransition.html  Full reporting guidance: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf"
+            ],
+            "rights": "N/A",
+            "spatial": "US",
+            "temporal": "5/11/2023 \u2013 5/3/2024",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Weekly United States COVID-19 Hospitalization Metrics by County \u2013 ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5hpj-p74g",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-03-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-26",
-            "keyword": [
-                "interferon gamma release assay (igra)",
-                "quantiferon (qft)",
-                "t-spot.tb (tspot)",
-                "tuberculin skin test (tst)",
-                "tuberculosis"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tuberculosis Epidemiologic Studies Consortium",
                 "hasEmail": "mailto:tbesc3@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5hpj-p74g",
             "description": "This was a head-to-head comparison of three FDA-approved tests for TB infection (Tuberculin Skin Test, QuantiFERON-TB Gold In-Tube, and T-SPOT.TB) in populations at high risk of latent TB infection and/or progression to TB disease.",
-            "title": "Tuberculosis Epidemiologic Studies Consortium (TBESC)-II Part A: Comparison of the Tuberculin Skin Test and Interferon-Gamma Release Assays in Diagnosing Infection with Mycobacterium tuberculosis and Prediction of Progression to Tuberculosis Disease",
-            "programCode": [
-                "009:027"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36331,53 +36311,46 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5hpj-p74g",
+            "issued": "2024-03-20",
+            "keyword": [
+                "interferon gamma release assay (igra)",
+                "quantiferon (qft)",
+                "t-spot.tb (tspot)",
+                "tuberculin skin test (tst)",
+                "tuberculosis"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5hpj-p74g",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-26",
+            "programCode": [
+                "009:027"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Center for HIV",
                 "Viral Hepatitis",
                 "STD",
                 "and TB Prevention"
-            ]
+            ],
+            "title": "Tuberculosis Epidemiologic Studies Consortium (TBESC)-II Part A: Comparison of the Tuberculin Skin Test and Interferon-Gamma Release Assays in Diagnosing Infection with Mycobacterium tuberculosis and Prediction of Progression to Tuberculosis Disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-30",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
-            "references": [
-                "https://www.cdc.gov/nccdphp/dnpao/index.html"
-            ],
-            "keyword": [
-                "adolescents",
-                "dnpao",
-                "fruit",
-                "obesity",
-                "overweight",
-                "physical activity",
-                "soda",
-                "tv",
-                "vegetables",
-                "yrbss"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DNPAO Public Inquiries",
                 "hasEmail": "mailto:dnpaoinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/vba9-s8jp",
+            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Youth-Risk/vba9-s8jp",
             "description": "This dataset includes data on adolescent's diet, physical activity, and weight status from Youth Risk Behavior Surveillance System (YRBSS). This data is used for DNPAO's Data, Trends, and Maps database, which provides national and state specific data on obesity, nutrition, physical activity, and breastfeeding. For more information about YRBSS visit https://www.cdc.gov/healthyyouth/data/yrbs/index.htm.",
-            "title": "Nutrition, Physical Activity, and Obesity - Youth Risk Behavior Surveillance System",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36400,58 +36373,53 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Youth-Risk/vba9-s8jp",
+            "identifier": "https://data.cdc.gov/api/views/vba9-s8jp",
+            "issued": "2025-01-30",
+            "keyword": [
+                "adolescents",
+                "dnpao",
+                "fruit",
+                "obesity",
+                "overweight",
+                "physical activity",
+                "soda",
+                "tv",
+                "vegetables",
+                "yrbss"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/nccdphp/dnpao/index.html"
+            ],
             "theme": [
                 "Nutrition",
                 "Physical Activity",
                 "and Obesity"
-            ]
+            ],
+            "title": "Nutrition, Physical Activity, and Obesity - Youth Risk Behavior Surveillance System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-05-08",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2023-07-29",
-            "modified": "2023-09-27",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "hispanic origin",
-                "influenza",
-                "mortality",
-                "nchs",
-                "nvss",
-                "pneumonia",
-                "provisional",
-                "puerto rico",
-                "race",
-                "state",
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ks3g-spdg",
             "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nDeaths involving COVID-19, pneumonia, and influenza reported to NCHS by race, age, and jurisdiction of occurrence.",
-            "title": "Provisional COVID-19 Deaths by Race and Hispanic Origin, and Age",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36474,49 +36442,57 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/ks3g-spdg",
+            "issued": "2020-05-08",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hispanic origin",
+                "influenza",
+                "mortality",
+                "nchs",
+                "nvss",
+                "pneumonia",
+                "provisional",
+                "puerto rico",
+                "race",
+                "state",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-09-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States, Puerto Rico",
+            "temporal": "2020-01-01/2023-07-29",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional COVID-19 Deaths by Race and Hispanic Origin, and Age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
-            "references": [
-                "https://academic.oup.com/aje/article/179/8/1025/109078",
-                "https://academic.oup.com/aje/article/182/2/127/93984",
-                "https://www.cdc.gov/pcd/issues/2017/pdf/17_0281.pdf",
-                "https://www.cdc.gov/pcd/issues/2018/18_0313.htm"
-            ],
-            "keyword": [
-                "500 cities",
-                "city",
-                "estimates",
-                "prevalence"
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
-            "identifier": "https://data.cdc.gov/api/views/k56w-7tny",
+            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-City-level-Data-GIS-Friendly-Format-201/k56w-7tny",
             "description": "2014, 2013. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project census city-level data in GIS-friendly format can be joined with city spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-City-Boundaries/n44h-hy2j) in a geographic information system (GIS) to produce maps of 27 measures at the city-level.",
-            "title": "500 Cities: City-level Data (GIS Friendly Format), 2016 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36539,42 +36515,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-City-level-Data-GIS-Friendly-Format-201/k56w-7tny",
+            "identifier": "https://data.cdc.gov/api/views/k56w-7tny",
+            "issued": "2023-07-18",
+            "keyword": [
+                "500 cities",
+                "city",
+                "estimates",
+                "prevalence"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://academic.oup.com/aje/article/179/8/1025/109078",
+                "https://academic.oup.com/aje/article/182/2/127/93984",
+                "https://www.cdc.gov/pcd/issues/2017/pdf/17_0281.pdf",
+                "https://www.cdc.gov/pcd/issues/2018/18_0313.htm"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "500 Cities: City-level Data (GIS Friendly Format), 2016 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/head-start-family-and-child-experiences-survey-faces-2000-cohort",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-06-19",
-            "temporal": "2000-01-01T00:00:00-05:00/2003-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "children's health",
-                "early care and education",
-                "head start"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "admin",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Health & Human Services"
-            },
-            "identifier": "b06bd10c-3fa1-4f8c-8d5f-e6716ec2c7d4",
+            "dataQuality": true,
+            "describedBy": "http://researchconnections.org/childcare/resources/5553?q=Family+and+Child+Experiences+Survey",
             "description": "<p>Descriptive, longitudinal study including direct assessments, classroom observation, parent and teacher interviews, for a nationally represenative sample of Head Start Children</p>",
-            "title": "Head Start Family and Child Experiences Survey (FACES) 2000 Cohort",
-            "programCode": [
-                "009:092"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36583,38 +36566,38 @@
                     "title": "API "
                 }
             ],
-            "describedBy": "http://researchconnections.org/childcare/resources/5553?q=Family+and+Child+Experiences+Survey",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "b06bd10c-3fa1-4f8c-8d5f-e6716ec2c7d4",
+            "issued": "2013-06-19",
+            "keyword": [
+                "children's health",
+                "early care and education",
+                "head start"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/head-start-family-and-child-experiences-survey-faces-2000-cohort",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:092"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
+            },
+            "temporal": "2000-01-01T00:00:00-05:00/2003-01-01T00:00:00-05:00",
+            "title": "Head Start Family and Child Experiences Survey (FACES) 2000 Cohort"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://lhncbc.nlm.nih.gov/ii/areas/structured-abstracts.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-03-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dataset",
-                "literature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/fcnn-6kw5",
             "description": "Information about abstracts with distinct, labeled sections (e.g., Introduction, Methods, Results, discussion) that appear in MEDLINE.",
-            "title": "Structured Abstracts",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36629,52 +36612,40 @@
                     "title": "Download Structured Abstracts data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/fcnn-6kw5",
+            "issued": "2022-03-02",
+            "keyword": [
+                "dataset",
+                "literature"
+            ],
+            "landingPage": "https://lhncbc.nlm.nih.gov/ii/areas/structured-abstracts.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Literature"
-            ]
+            ],
+            "title": "Structured Abstracts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7mra-9cq9",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-11-19/2024-02-03",
-            "modified": "2024-10-18",
-            "keyword": [
-                "coronavirus",
-                "covid19",
-                "ed",
-                "emergency-department",
-                "flu",
-                "influenza",
-                "national-syndromic-surveillance-program",
-                "ncird",
-                "nssp",
-                "ophdst",
-                "respiratory-syncytial-virus",
-                "respiratory-virus-response",
-                "rsv",
-                "rvr"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Syndromic Surveillance Program",
                 "hasEmail": "mailto:nssp@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7mra-9cq9",
             "description": "2023 Respiratory Viruses Response \u2013 National Syndromic Surveillance Program Emergency Department Visit Trajectories - COVID-19, Flu, RSV, Combined \u2013 by state. This dataset provides the percentage of emergency department patient visits for the specified pathogen of all ED patient visits for the specified geography that were observed for the given week from data submitted to the National Syndromic Surveillance Program (NSSP). In addition, the trend over time both as of the given row date and as of the most current data submitted is characterized as increasing, decreasing or stable to provide awareness of how the weekly trend is changing for the given geographic region.\n\nFor the emergency department time series, trajectory classifications reported on the opening page are based on rolling regression model assessments of the slope for each respiratory illness. Weeks with a significant time term (p <0.05) are classified as increasing when the slope is positive and decreasing when the slope is negative. Weeks with a non-significant time term (p \u2265 0.05) are classified as stable. A 3-week moving average is applied to the time series prior to the regression procedure in order to smooth week-to-week variation. \n<br>\nFor additional information, please see:<a href=\"https://www.cdc.gov/ncird/surveillance/respiratory-illnesses/index.html#companion-guide\"><b>Companion Guide: NSSP Emergency Department Data on Respiratory Illness</b></a>\n<br>\nUpdated once per week on Fridays.",
-            "title": "2023 Respiratory Virus Response - NSSP Emergency Department Visit Trajectories by State- COVID-19, Flu, RSV, Combined",
-            "programCode": [
-                "009:037"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36697,22 +36668,64 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/7mra-9cq9",
+            "issued": "2023-11-16",
+            "keyword": [
+                "coronavirus",
+                "covid19",
+                "ed",
+                "emergency-department",
+                "flu",
+                "influenza",
+                "national-syndromic-surveillance-program",
+                "ncird",
+                "nssp",
+                "ophdst",
+                "respiratory-syncytial-virus",
+                "respiratory-virus-response",
+                "rsv",
+                "rvr"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7mra-9cq9",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2024-10-18",
+            "programCode": [
+                "009:037"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "U.S.",
+            "temporal": "2022-11-19/2024-02-03",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "2023 Respiratory Virus Response - NSSP Emergency Department Visit Trajectories by State- COVID-19, Flu, RSV, Combined"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2007",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 16 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Drug Abuse Warning Network (DAWN-2007) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2007-nid13522",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2007-nid13522"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2007-nid13522",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol",
                 "demographic characteristics",
@@ -36725,58 +36738,30 @@
                 "substance abuse",
                 "suicide"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2007",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2007-nid13522",
-            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 16 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
-            "title": "Drug Abuse Warning Network (DAWN-2007)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2007-nid13522",
-                    "description": "Drug Abuse Warning Network (DAWN-2007) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2007-nid13522"
-                }
-            ]
+            "title": "Drug Abuse Warning Network (DAWN-2007)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/9hmq-6ddv",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-22",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "b51bbd15-c6c7-4158-9365-54fe40a7d351",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-15-to-2023-05-21",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36785,36 +36770,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-15-to-2023-05-21"
                 }
             ],
+            "identifier": "b51bbd15-c6c7-4158-9365-54fe40a7d351",
+            "issued": "2023-05-23",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/9hmq-6ddv",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-05-22",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-15-to-2023-05-21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/9hte-xnpg",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-12-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-12",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "509b91a3-0fb5-449a-bbf2-40e987e45ed3",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-12-04-to-2023-12-10",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36823,40 +36808,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-12-04-to-2023-12-10"
                 }
             ],
+            "identifier": "509b91a3-0fb5-449a-bbf2-40e987e45ed3",
+            "issued": "2023-12-13",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/9hte-xnpg",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-12-12",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-12-04-to-2023-12-10"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/respiratory-viruses/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-03",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-08-28",
-            "keyword": [
-                "adult",
-                "covid-19 vaccination",
-                "pregnancy",
-                "vsd"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/efqg-e273",
             "description": "Weekly COVID-19 Vaccination Coverage, Pregnant Persons 18-49 Years Old\n\n\u2022 COVID-19 vaccination coverage among pregnant persons is assessed through the Vaccine \n   Safety Datalink* \n\n\u2022 Data on updated 2023-24 COVID-19 vaccinations among pregnant persons was available starting September 23, 2023, and includes doses received starting September 14, 2023.",
-            "title": "Weekly COVID-19 Vaccination Coverage among Pregnant Persons by Race and Ethnicity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36879,40 +36860,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/efqg-e273",
+            "issued": "2023-11-03",
+            "keyword": [
+                "adult",
+                "covid-19 vaccination",
+                "pregnancy",
+                "vsd"
+            ],
+            "landingPage": "https://www.cdc.gov/respiratory-viruses/index.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2024-08-28",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2023-2024",
             "theme": [
                 "Pregnancy & Vaccination"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly COVID-19 Vaccination Coverage among Pregnant Persons by Race and Ethnicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/pgaa-i327",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/pgaa-i327",
             "description": "Per- and polyfluoroalkyl substances (PFAS) are a large group of stable man-mad surfactants that are incorporated into numerous products for their water and oil resistance and have been associated with adverse health effects.   The present study evaluated the systemic and immunotoxicity of sub-chronic 28- or 10-day dermal exposure of PFHxS (0.625-5% or 15.63-125 mg/kg/dose) in a murine model.  Elevated levels of PFHxS were detected in the serum and urine, suggesting that absorption is occurring through the dermal route.  Liver weight (% body) significantly increased and spleen weight (% body) significantly deceased with PFHxS exposure supported by histopathological changes. Additionally, PFHxS significantly reduced the humoral immune response and altered immune subsets in the spleen, suggesting immunosuppression.  Gene expression changes were observed in the liver, skin, and spleen with genes involved in fatty acid metabolism, necrosis, and inflammation.  Immune-cell phenotyping identified significant decreases in B-cells, NK cells, and CD11b+ cells in the spleen along with increases in CD4+ and CD8+ T-cells, NK cells, and neutrophils in the skin.  These findings support dermal PFHxS-induced liver damage and immune suppression.  These data support PFHxS absorption through the skin and demonstrate immunotoxicity via this exposure route, raising concern about prompting the need for further investigation.",
-            "title": "Systemic and immunotoxicity induced by topical application of perfluorohexane sulfonic acid (PFHxS) in a murine model",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36920,35 +36907,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/pgaa-i327",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/pgaa-i327",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Systemic and immunotoxicity induced by topical application of perfluorohexane sulfonic acid (PFHxS) in a murine model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ga52-qyaz",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ga52-qyaz",
             "description": "There is strong evidence associating the indoor environment with transmission of SARS-CoV-2, the virus that causes COVID-19. SARS-CoV-2 can spread by exposure to droplets and very fine aerosol particles from respiratory fluids that are released by infected persons. Layered mitigation strategies, including but not limited to maintaining physical distancing, adequate ventilation, universal masking, avoiding overcrowding, and vaccination, have shown to be effective in re-ducing the spread of SARS-CoV-2 within the indoor environment. Here, we examine the effect of mitigation strategies on reducing the risk of exposure to simulated respiratory aerosol particles within a classroom-style meeting room. To quantify exposure of uninfected individuals (Recip-ients), surrogate respiratory aerosol particles were generated by a breathing simulator with a headform (Source) that mimicked breath exhalations. Recipients, represented by three breathing simulators with manikin headforms, were placed in a meeting room and affixed with optical particle counters to measure 0.3\u20133 \u00b5m aerosol particles.",
-            "title": "Efficacy of ventilation, HEPA air cleaners, universal masking, and physical distancing for reducing exposure to simulated exhaled aerosols in a meeting room-Dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36956,66 +36943,90 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ga52-qyaz",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/ga52-qyaz",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Efficacy of ventilation, HEPA air cleaners, universal masking, and physical distancing for reducing exposure to simulated exhaled aerosols in a meeting room-Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/9iqx-4x65",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-08-10",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-08",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "f0729254-a759-531f-940e-5bb531ccd2cf",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard STATE v0.3.58-test (local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.58-test/20230728/STATE.csv",
-                    "description": "Scorecard STATE v0.3.58-test (local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard STATE v0.3.58-test (local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.58-test/20230728/STATE.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard STATE v0.3.58-test (local)"
                 }
             ],
+            "identifier": "f0729254-a759-531f-940e-5bb531ccd2cf",
+            "issued": "2023-08-10",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/9iqx-4x65",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-08-08",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Scorecard STATE v0.3.58-test (local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225438.htm",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "description": "Contains data for FDA pistachio product recalls since March 2009.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225438.htm",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "identifier": "64ae1af7-2b25-4d00-9dbf-244269123d2f",
             "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2010-10-01",
             "keyword": [
                 "food",
                 "health",
@@ -37025,58 +37036,31 @@
                 "recalls",
                 "safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FDA Enterprise Data Inventory",
-                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
-            },
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225438.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2010-10-01",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "64ae1af7-2b25-4d00-9dbf-244269123d2f",
-            "description": "Contains data for FDA pistachio product recalls since March 2009.",
-            "title": "FDA Pistachio Product Recalls Widget",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225438.htm",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "FDA Pistachio Product Recalls Widget"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/rsv/php/surveillance/rsv-net.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-07-23",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
-            "keyword": [
-                "rsv",
-                "surveillance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RESP-NET",
                 "hasEmail": "mailto:CovidRSV-Net@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/29hc-w46k",
             "description": "The Respiratory Syncytial Virus Hospitalization Surveillance Network (RSV-NET) is a network that conducts active, population-based surveillance for laboratory-confirmed RSV-associated hospitalizations in children younger than 18 years of age and adults. RSV-NET, along with the Coronavirus Disease 2019 (COVID-19) Hospitalization Surveillance Network (COVID-NET) an the Influenza Hospitalization Surveillance network (FluSuv-NET), comprise the Respiratory Virus Hospitalization Surveillance Network (RESP-NET).  The RESP-NET platforms have overlapping surveillance areas and use similar methods to collect data. Because the surveillance areas and age groups included in surveillance have changed over time, trends should be interpreted with caution. RSV-NET is CDC\u2019s source for important data on rates of hospitalizations associated with RSV. Hospitalization rates show how many people in the surveillance area are hospitalized with RSV, compared to the total number of people residing in that area. \n\nData are preliminary and subject to change as more data become available. Data will be updated weekly.",
-            "title": "Weekly Rates of Laboratory-Confirmed RSV Hospitalizations from the RSV-NET Surveillance System",
-            "programCode": [
-                "009:038"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37099,44 +37083,41 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "RSV-NET Sites",
+            "identifier": "https://data.cdc.gov/api/views/29hc-w46k",
+            "issued": "2024-07-23",
+            "keyword": [
+                "rsv",
+                "surveillance"
+            ],
+            "landingPage": "https://www.cdc.gov/rsv/php/surveillance/rsv-net.html",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-24",
+            "programCode": [
+                "009:038"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "RSV-NET Sites",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Weekly Rates of Laboratory-Confirmed RSV Hospitalizations from the RSV-NET Surveillance System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-01",
-            "@type": "dcat:Dataset",
-            "temporal": "Flu Seasons-2021-22, 2022-23, 2023-24",
-            "modified": "2024-09-03",
-            "keyword": [
-                "flu vaccination",
-                "iis",
-                "immunization information system",
-                "vaccination coverage"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/g2ck-geg5",
             "description": "Monthly Cumulative Number and Percent of Persons Who Receive \u22651 Influenza Vaccination Doses and Comparison Between 2023-2024 and Two Previous Seasons, by Jurisdiction, United States\n\n\u2022 Influenza vaccination coverage for children and adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems (IIS) data, submitted from jurisdictions to CDC monthly in aggregate by age group. More information about the IIS can be found at https://www.cdc.gov/vaccines/programs/iis/about.html. \n\n\u2022 Influenza vaccination coverage estimate numerators include the number of people receiving at least one dose of influenza vaccine in a given flu season, based on information that state, territorial, and local public health agencies report to CDC. Some jurisdictions\u2019 data may include data submitted by tribes. Estimates include persons who are deceased but received a vaccination during the current season. People receiving doses are attributed to the jurisdiction in which the person resides unless noted otherwise. Quality and completeness of data may vary across jurisdictions. Influenza vaccination coverage denominators are obtained from 2020 U.S. Census Bureau population estimates. \n\n\u2022 Monthly estimates shown are cumulative, reflecting all persons vaccinated from July through a given month of that flu season. Cumulative estimates include any historical data reported since the previous submission. National estimates are not presented since not all U.S. jurisdictions are currently reporting their IIS data to CDC. Jurisdictions reporting data to CDC include U.S. states, some localities, and territories. \n\n\u2022 Because IIS data contain all vaccinations administered within a jurisdiction rather than a sample, standard errors were not calculated and statistical testing for differences in estimates across years were not performed. \n\n\u2022 Laws and policies regarding the submission of vaccination data to an IIS vary by state, which may impact the completeness of vaccination coverage reflected for a jurisdiction. More information on laws and policies are found at https://www.cdc.gov/vaccines/programs/iis/policy-legislation.html. \n\n\u2022 Coverage estimates based on IIS data are expected to differ from National Immunization Survey (NIS) estimates for children (https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-coverage-race.html)                 \nand adults (https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-adult-coverage.html) because NIS estimates are based on a sample that may not be representative after survey weighting and vaccination status is determined by survey respondent rather than vaccine records or administrations, and quality and completeness of IIS data may vary across jurisdictions. In general, NIS estimates tend to overestimate coverage due to overreporting and IIS estimates may underestimate coverage due to incompleteness of data in certain jurisdictions.",
-            "title": "Monthly Cumulative Number and Percent of Persons Who Receive \u22651 Influenza Vaccination Doses and Comparison Between 2023-2024 and Two Previous Seasons, by Jurisdiction, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37159,26 +37140,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Jurisdictions - States, District of Columbia, Islands, and US cities",
+            "identifier": "https://data.cdc.gov/api/views/g2ck-geg5",
+            "issued": "2024-02-01",
+            "keyword": [
+                "flu vaccination",
+                "iis",
+                "immunization information system",
+                "vaccination coverage"
+            ],
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2024-09-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "Jurisdictions - States, District of Columbia, Islands, and US cities",
+            "temporal": "Flu Seasons-2021-22, 2022-23, 2023-24",
             "theme": [
                 "Flu Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Monthly Cumulative Number and Percent of Persons Who Receive \u22651 Influenza Vaccination Doses and Comparison Between 2023-2024 and Two Previous Seasons, by Jurisdiction, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/study-womens-health-across-nation-swan-data-investigator-access",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Alicia Colvin Greene",
+                "hasEmail": "mailto:swanaccess@edc.pitt.edu"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.edc.gsph.pitt.edu/Swan/Research/Documents/AnalysisAssistance/SWAN_DataDictionary_Simple_Thru_V10.xls",
+            "describedByType": "application/vnd.ms-excel",
+            "description": "<p>The SWAN Coordinating Center provides SWAN data access to SWAN Investigators through the study website.  The SWAN website provides access to longitudinal data describing the physical, biological, psychological, and social changes that occur during the menopausal transition. Data collected from 3,302 SWAN participants from Baseline through the 13th Follow-Up visit are currently available.</p>",
+            "identifier": "e3f94668-b605-4006-a781-cf1d5a41aa07",
             "issued": "2015-03-04",
-            "temporal": "1999-01-26T00:00:00-05:00/1999-01-26T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "bone loss",
                 "cardiovascular disease",
@@ -37196,111 +37202,82 @@
                 "vasomotor symptoms",
                 "women s health"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Alicia Colvin Greene",
-                "hasEmail": "mailto:swanaccess@edc.pitt.edu"
-            },
+            "landingPage": "https://healthdata.gov/dataset/study-womens-health-across-nation-swan-data-investigator-access",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:015"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "e3f94668-b605-4006-a781-cf1d5a41aa07",
-            "description": "<p>The SWAN Coordinating Center provides SWAN data access to SWAN Investigators through the study website.  The SWAN website provides access to longitudinal data describing the physical, biological, psychological, and social changes that occur during the menopausal transition. Data collected from 3,302 SWAN participants from Baseline through the 13th Follow-Up visit are currently available.</p>",
-            "title": "Study of Womens Health Across the Nation (SWAN) Data: Investigator Access",
-            "describedByType": "application/vnd.ms-excel",
-            "programCode": [
-                "009:015"
-            ],
-            "describedBy": "http://www.edc.gsph.pitt.edu/Swan/Research/Documents/AnalysisAssistance/SWAN_DataDictionary_Simple_Thru_V10.xls",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1999-01-26T00:00:00-05:00/1999-01-26T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "Study of Womens Health Across the Nation (SWAN) Data: Investigator Access"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/9m69-came",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_implauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "7a7af4ad-3403-5ad7-8983-b2db6c203a82",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_measure_allStates",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_allStates.csv",
-                    "description": "{\"dataset\": \"measure_allStates\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_allStates\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_allStates.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_allStates csv file"
                 }
             ],
+            "identifier": "7a7af4ad-3403-5ad7-8983-b2db6c203a82",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/9m69-came",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "implAuto_measure_allStates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/pxa6-asqb",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-01-15",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "2014",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "tb",
-                "tuberculosis",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/pxa6-asqb",
             "description": "NNDSS - Table IV. Tuberculosis - 2014.This Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States will exclude counts from US territories.  Footnote:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Min: Minimum.    Max: Maximum. * Case counts for reporting year 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf Updated reports to the National Center for HIV/AIDS, Viral Hepatitis, STD and TB Prevention. Data for TB are displayed quarterly.",
-            "title": "NNDSS - Table IV. Tuberculosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37323,40 +37300,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/pxa6-asqb",
+            "issued": "2015-01-15",
+            "keyword": [
+                "2014",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "tb",
+                "tuberculosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/pxa6-asqb",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2015-08-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table IV. Tuberculosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/Class/Structure/pssm/pssm_viewer.cgi",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-07-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "computational biology",
-                "protein",
-                "tools & utilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/rp33-dkz5",
             "description": "Users can display, sort, subset and download position-specific score matrices (PSSMs) either from CDD records or from Position Specific Iterated (PSI)-BLAST protein searches.",
-            "title": "PSSM Viewer",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37365,44 +37347,41 @@
                     "title": "PSSM Viewer"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/rp33-dkz5",
+            "issued": "2021-07-01",
+            "keyword": [
+                "computational biology",
+                "protein",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/Class/Structure/pssm/pssm_viewer.cgi",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Molecular biology/Genetics"
-            ]
+            ],
+            "title": "PSSM Viewer"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/art/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-30",
-            "keyword": [
-                "art",
-                "assisted reproductive technology",
-                "clinic",
-                "fertility",
-                "infertility",
-                "services",
-                "success rates"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ARTINFO",
                 "hasEmail": "mailto:ARTINFO@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/3x54-3thk",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Su/3x54-3thk",
             "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Success Rates dataset contains success rates for ART cycles started during the year indicated. Since ART success depends on whether patients are using their own eggs or donor eggs, success rates are included separately for these two groups. Success rates for patients using their own eggs are shown per intended retrieval, per actual retrieval, and per transfer. These success rates are reported as cumulative success rates, which take into account transfers that occur within 1 year after an egg retrieval. Since ART success depends on whether patients are using ART for the first time or had prior ART cycles, users can examine success rates for all \u201cPatients using their own eggs\u201d or for \u201cPatients with no prior ART using their own eggs.\u201d For new patients using ART for the first time, the success rates are also shown after 1, 2, or all intended egg retrievals during the reporting year. In addition, the average number of transfers per intended retrieval and the average number of intended retrievals per live-birth delivery are shown. Success rates for ART cycles that involve the transfer of embryos created from donor eggs or donated embryos are shown and are not cumulative. They are based on donor cycles started in the year indicated that had embryo transfers, regardless of when the donor eggs were retrieved. Success rates in this section are not presented by patient age group because previous data show that an intended parent\u2019s age does not substantially affect success when using donor eggs or donated embryos. The success rates are presented by types of embryos and eggs used in the transfer. This dataset excludes cycles that were considered research\u2014that is, cycles performed to evaluate new procedures.",
-            "title": "2020 Final Assisted Reproductive Technology (ART) Success Rates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37425,46 +37404,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Su/3x54-3thk",
+            "identifier": "https://data.cdc.gov/api/views/3x54-3thk",
+            "issued": "2023-07-19",
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-30",
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
+            "title": "2020 Final Assisted Reproductive Technology (ART) Success Rates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hs59-amfp",
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
-                "salmonella paratyphi infection",
-                "salmonella typhi infection",
-                "salmonellosis (excluding salmonella typhi infection and salmonella paratyphi infection)",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hs59-amfp",
             "description": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection) - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 In previous years, cases were reported as Salmonellosis. Beginning in January 2019, cases began to be reported as Salmonella Paratyphi infection.\r\n\u00b6 In previous years, cases were reported as typhoid fever. Beginning in January 2019, cases began to be reported as Salmonella Typhi infection.\r\n** In previous years, cases were reported as Salmonellosis (excluding paratyphoid fever and typhoid fever). Beginning in January 2019, cases began to be reported as Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection).",
-            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37487,41 +37464,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hs59-amfp",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "salmonella paratyphi infection",
+                "salmonella typhi infection",
+                "salmonellosis (excluding salmonella typhi infection and salmonella paratyphi infection)",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hs59-amfp",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/home/learn/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-03-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "computational biology",
-                "education",
-                "reference",
-                "training and instruction"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/kbgu-xbn7",
             "description": "NCBI creates a variety of educational products including courses, workshops, webinars, training materials and documentation. NCBI educational events are free and open to everyone. All NCBI educational materials are available for anyone to re-use and distribute",
-            "title": "NCBI Learn",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37530,40 +37511,42 @@
                     "title": "NCBI Learn"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/kbgu-xbn7",
+            "issued": "2022-03-01",
+            "keyword": [
+                "computational biology",
+                "education",
+                "reference",
+                "training and instruction"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/home/learn/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Other"
-            ]
+            ],
+            "title": "NCBI Learn"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/children-coverage-vaccination.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-11",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-08-28",
-            "keyword": [
-                "covid-19 vaccination",
-                "nis-ccm"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/qfiq-jir6",
             "description": "\u2022 Weekly COVID-19 vaccination coverage estimates among children 6 months to 17 years is assessed through the National Immunization Survey (https://www.cdc.gov/vaccines/imz-managers/nis/about.html). \n\n\u2022 Weekly estimates of COVID-19 vaccination coverage among children through December 31, 2023, were calculated using data from the National Immunization Survey-Child COVID Module (NIS-CCM) (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-ccm). Beginning January 2, 2024, the NIS-CCM was discontinued, and questions regarding receipt of COVID-19 vaccination among children were added to the NIS-Flu (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-cim). \n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19.",
-            "title": "Weekly Differences in Cumulative Percentage of Children Ages 6 Months -17 Years who are up to date with the updated 2023-24 COVID-19 Vaccine, by Selected Demographics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37586,40 +37569,42 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/qfiq-jir6",
+            "issued": "2023-12-11",
+            "keyword": [
+                "covid-19 vaccination",
+                "nis-ccm"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/children-coverage-vaccination.html",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2024-08-28",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2023-2024",
             "theme": [
                 "Child Vaccinations"
-            ]
+            ],
+            "title": "Weekly Differences in Cumulative Percentage of Children Ages 6 Months -17 Years who are up to date with the updated 2023-24 COVID-19 Vaccine, by Selected Demographics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/9rw5-f4vn",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-02-09",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-07",
-            "keyword": [
-                "drug rebate program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "8f4b03ea-7cbc-44ed-a8b3-9524bbc01491",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-12-26-to-2023-01-01",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37628,22 +37613,40 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-12-26-to-2023-01-01"
                 }
             ],
+            "identifier": "8f4b03ea-7cbc-44ed-a8b3-9524bbc01491",
+            "issued": "2023-02-09",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/9rw5-f4vn",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-02-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-12-26-to-2023-01-01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mbd7-r32t",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC-INFO",
+                "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
+            },
+            "describedBy": "https://data.cdc.gov/api/views/mbd7-r32t/files/4697b7f1-c0ea-403a-9583-6a02fd33a21c?download=true&filename=data_dictionary_covid_cases_restricted_detailed_updated.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "<b>Note:</b>\nReporting of new COVID-19 Case Surveillance data will be discontinued July 1, 2024, to align with the process of removing SARS-CoV-2 infections (COVID-19 cases) from the list of nationally notifiable diseases. Although these data will continue to be publicly available, the dataset will no longer be updated. \n\nAuthorizations to collect certain public health data expired at the end of the U.S. public health emergency declaration on May 11, 2023. The following jurisdictions discontinued COVID-19 case notifications to CDC: Iowa (11/8/21), Kansas (5/12/23), Kentucky (1/1/24), Louisiana (10/31/23), New Hampshire (5/23/23), and Oklahoma (5/2/23). Please note that these jurisdictions will not routinely send new case data after the dates indicated. As of 7/13/23, case notifications from Oregon will only include pediatric cases resulting in death.\n\n\nThis case surveillance publicly available dataset has 33 elements for all COVID-19 cases shared with CDC and includes demographics, geography (county and state of residence), any exposure history, disease severity indicators and outcomes, and presence of any underlying medical conditions and risk behaviors. This dataset requires a registration process and a data use agreement.\n\n<h4><b>CDC has three COVID-19 case surveillance datasets:</b></h4><ul><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4\">COVID-19 Case Surveillance Public Use Data with Geography</a>: Public use, patient-level dataset with clinical data (including symptoms), demographics, and county and state of residence. (19 data elements)</li><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf\">COVID-19 Case Surveillance Public Use Data</a>: Public use, patient-level dataset with clinical and symptom data and demographics, with no geographic data. (12 data elements)</li><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Restricted-Access-Detai/mbd7-r32t\">COVID-19 Case Surveillance Restricted Access Detailed Data</a>: Restricted access, patient-level dataset with clinical and symptom data, demographics, and state and county of residence. Access requires a registration process and a data use agreement. (33 data elements)</li></ul>\n\n<b>Requesting Access to the COVID-19 Case Surveillance Restricted Access Detailed Data</b>\nPlease review the following documents to determine your interest in accessing the COVID-19 Case Surveillance Restricted Access Detailed Data file:\n1) <a href=\"https://data.cdc.gov/api/views/mbd7-r32t/files/9aad836e-5aa5-4047-aa5c-15996becc87c?download=true&filename=summary_guidance_and_limitations_information_and_restricted_access_data_use_agreement_information_updated.pdf\"> CDC COVID-19 Case Surveillance Restricted Access Detailed Data: Summary, Guidance, Limitations Information, and Restricted Access Data Use Agreement Information</a>\n\n2) <a href=\"https://data.cdc.gov/api/views/mbd7-r32t/files/4697b7f1-c0ea-403a-9583-6a02fd33a21c?download=true&filename=data_dictionary_covid_cases_restricted_detailed_updated.xlsx\"> Data Dictionary for the COVID-19 Case Surveillance Restricted Access Detailed Data</a>\n\nThe next step is to complete the Registration Information and Data Use Restrictions Agreement (<a href=\"https://app.smartsheetgov.com/b/form/20e9cf9b42d04a92a67585043cf34fbe\">RIDURA</a>). Once complete, CDC will review your agreement. After access is granted, Ask SRRG (<a href=\"mailto:eocevent394@cdc.gov\">eocevent394@cdc.gov</a>) will email you information about how to access the data through GitHub. If you have questions about obtaining access, email <a href=\"mailto:eocevent394@cdc.gov\">eocevent394@cdc.gov</a>. \n\n<h4><b>Overview</b></h4>\n\nThe COVID-19 case surveillance database includes individual-level data reported to U.S. states and autonomous reporting entities, including New York City and the District of Columbia (D.C.), as well as U.S. territories and affili",
+            "identifier": "https://data.cdc.gov/api/views/mbd7-r32t",
             "issued": "2020-05-17",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2024-06-21",
-            "modified": "2025-01-13",
-            "references": [
-                "https://data.cdc.gov/api/views/mbd7-r32t/files/53195382-2916-4a7a-b97f-010111f3aaa1?download=true&filename=public%2033%20utility%20summary.pdf"
-            ],
             "keyword": [
                 "cases",
                 "coronavirus",
@@ -37653,59 +37656,38 @@
                 "restricted",
                 "surveillance"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CDC-INFO",
-                "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
-            },
+            "landingPage": "https://data.cdc.gov/d/mbd7-r32t",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/mbd7-r32t",
-            "description": "<b>Note:</b>\nReporting of new COVID-19 Case Surveillance data will be discontinued July 1, 2024, to align with the process of removing SARS-CoV-2 infections (COVID-19 cases) from the list of nationally notifiable diseases. Although these data will continue to be publicly available, the dataset will no longer be updated. \n\nAuthorizations to collect certain public health data expired at the end of the U.S. public health emergency declaration on May 11, 2023. The following jurisdictions discontinued COVID-19 case notifications to CDC: Iowa (11/8/21), Kansas (5/12/23), Kentucky (1/1/24), Louisiana (10/31/23), New Hampshire (5/23/23), and Oklahoma (5/2/23). Please note that these jurisdictions will not routinely send new case data after the dates indicated. As of 7/13/23, case notifications from Oregon will only include pediatric cases resulting in death.\n\n\nThis case surveillance publicly available dataset has 33 elements for all COVID-19 cases shared with CDC and includes demographics, geography (county and state of residence), any exposure history, disease severity indicators and outcomes, and presence of any underlying medical conditions and risk behaviors. This dataset requires a registration process and a data use agreement.\n\n<h4><b>CDC has three COVID-19 case surveillance datasets:</b></h4><ul><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4\">COVID-19 Case Surveillance Public Use Data with Geography</a>: Public use, patient-level dataset with clinical data (including symptoms), demographics, and county and state of residence. (19 data elements)</li><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf\">COVID-19 Case Surveillance Public Use Data</a>: Public use, patient-level dataset with clinical and symptom data and demographics, with no geographic data. (12 data elements)</li><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Restricted-Access-Detai/mbd7-r32t\">COVID-19 Case Surveillance Restricted Access Detailed Data</a>: Restricted access, patient-level dataset with clinical and symptom data, demographics, and state and county of residence. Access requires a registration process and a data use agreement. (33 data elements)</li></ul>\n\n<b>Requesting Access to the COVID-19 Case Surveillance Restricted Access Detailed Data</b>\nPlease review the following documents to determine your interest in accessing the COVID-19 Case Surveillance Restricted Access Detailed Data file:\n1) <a href=\"https://data.cdc.gov/api/views/mbd7-r32t/files/9aad836e-5aa5-4047-aa5c-15996becc87c?download=true&filename=summary_guidance_and_limitations_information_and_restricted_access_data_use_agreement_information_updated.pdf\"> CDC COVID-19 Case Surveillance Restricted Access Detailed Data: Summary, Guidance, Limitations Information, and Restricted Access Data Use Agreement Information</a>\n\n2) <a href=\"https://data.cdc.gov/api/views/mbd7-r32t/files/4697b7f1-c0ea-403a-9583-6a02fd33a21c?download=true&filename=data_dictionary_covid_cases_restricted_detailed_updated.xlsx\"> Data Dictionary for the COVID-19 Case Surveillance Restricted Access Detailed Data</a>\n\nThe next step is to complete the Registration Information and Data Use Restrictions Agreement (<a href=\"https://app.smartsheetgov.com/b/form/20e9cf9b42d04a92a67585043cf34fbe\">RIDURA</a>). Once complete, CDC will review your agreement. After access is granted, Ask SRRG (<a href=\"mailto:eocevent394@cdc.gov\">eocevent394@cdc.gov</a>) will email you information about how to access the data through GitHub. If you have questions about obtaining access, email <a href=\"mailto:eocevent394@cdc.gov\">eocevent394@cdc.gov</a>. \n\n<h4><b>Overview</b></h4>\n\nThe COVID-19 case surveillance database includes individual-level data reported to U.S. states and autonomous reporting entities, including New York City and the District of Columbia (D.C.), as well as U.S. territories and affili",
-            "title": "COVID-19 Case Surveillance Restricted Access Detailed Data",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "009:020"
+            "references": [
+                "https://data.cdc.gov/api/views/mbd7-r32t/files/53195382-2916-4a7a-b97f-010111f3aaa1?download=true&filename=public%2033%20utility%20summary.pdf"
             ],
             "spatial": "US",
-            "describedBy": "https://data.cdc.gov/api/views/mbd7-r32t/files/4697b7f1-c0ea-403a-9583-6a02fd33a21c?download=true&filename=data_dictionary_covid_cases_restricted_detailed_updated.xlsx",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "temporal": "2020-01-01/2024-06-21",
             "theme": [
                 "Case Surveillance"
-            ]
+            ],
+            "title": "COVID-19 Case Surveillance Restricted Access Detailed Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://clinicaltables.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-21",
-            "keyword": [
-                "api",
-                "health data standards",
-                "terminologies"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ak72-wey9",
             "description": "Clinical Table Search Service (formerly \"lforms-service\") is a web service which software programs can use for querying clinical data tables.",
-            "title": "Clinical Table Search Service",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37720,45 +37702,40 @@
                     "title": "Clinical Table Search Service API"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ak72-wey9",
+            "issued": "2021-06-17",
+            "keyword": [
+                "api",
+                "health data standards",
+                "terminologies"
+            ],
+            "landingPage": "https://clinicaltables.nlm.nih.gov/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-21",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Research"
-            ]
+            ],
+            "title": "Clinical Table Search Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rxmp-xjpc",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "nedss",
-                "netss",
-                "nndss",
-                "non-congenital",
-                "west nile virus disease",
-                "wonder",
-                "zika virus disease"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rxmp-xjpc",
             "description": "NNDSS - Table II. West Nile to Zika  - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.  \r\n\r\n\u2020 Not reportable in all jurisdictions. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.",
-            "title": "NNDSS - Table II. West Nile to Zika",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37781,46 +37758,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rxmp-xjpc",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-congenital",
+                "west nile virus disease",
+                "wonder",
+                "zika virus disease"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rxmp-xjpc",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-01-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. West Nile to Zika"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://healthdata.gov/dataset/medical-expenditure-panel-survey-meps-restricted-data-files",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-10-24",
-            "temporal": "1996-01-01T00:00:00-05:00/2012-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "agency for healthcare research and quality",
-                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
-                "ahrq",
-                "expenditure",
-                "expenses",
-                "healthcare",
-                "health care cost",
-                "meps"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MEPS Project Director",
                 "hasEmail": "mailto:mepsprojectdirector@ahrq.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
-            },
-            "identifier": "f55380d9-8356-4d7a-97b2-ce8764053f29",
+            "describedBy": "http://meps.ahrq.gov/mepsweb/data_stats/onsite_datacenter.jsp",
             "description": "<p>Restricted Data Files Available at the Data Centers<br />\nResearchers and users with approved research projects can access restricted data files that have not been publicly released for reasons of confidentiality at the AHRQ Data Center in Rockville, Maryland.<br />\nQualified researchers can also access restricted data files through the U.S. Census Research Data Center (RDC) network (<a href=\"http://www.census.gov/ces/dataproducts/index.html\">http://www.census.gov/ces/dataproducts/index.html</a> -- Scroll down the page and click on the Agency for Health Care Research and Quality (AHRQ) link.) For information on the RDC research proposal process and the data sets available, read AHRQ-Census Bureau agreement on access to restricted MEPS data.</p>",
-            "title": "Medical Expenditure Panel Survey (MEPS) Restricted Data Files",
-            "programCode": [
-                "009:073"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37829,98 +37807,90 @@
                     "title": "Query Tool "
                 }
             ],
-            "describedBy": "http://meps.ahrq.gov/mepsweb/data_stats/onsite_datacenter.jsp",
+            "identifier": "f55380d9-8356-4d7a-97b2-ce8764053f29",
+            "issued": "2012-10-24",
+            "keyword": [
+                "agency for healthcare research and quality",
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "ahrq",
+                "expenditure",
+                "expenses",
+                "healthcare",
+                "health care cost",
+                "meps"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/medical-expenditure-panel-survey-meps-restricted-data-files",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:073"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
+            },
+            "temporal": "1996-01-01T00:00:00-05:00/2012-12-31T00:00:00-05:00",
+            "title": "Medical Expenditure Panel Survey (MEPS) Restricted Data Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/9u4w-2s8b",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-08-10",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-08",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "7fe15297-18ce-5295-a9ba-9ab1f4eb8fb3",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard MEASURE v0.3.58-test (local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.58-test/20230728/MEASURE.csv",
-                    "description": "Scorecard MEASURE v0.3.58-test (local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard MEASURE v0.3.58-test (local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.58-test/20230728/MEASURE.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard MEASURE v0.3.58-test (local)"
                 }
             ],
+            "identifier": "7fe15297-18ce-5295-a9ba-9ab1f4eb8fb3",
+            "issued": "2023-08-10",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/9u4w-2s8b",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-08-08",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Scorecard MEASURE v0.3.58-test (local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-11-12",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-26",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "excess deaths",
-                "hispanic origin",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "race",
-                "sex",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/m74n-4hbs",
             "description": "Weekly data on the number of deaths from all causes by sex, age group, and race/Hispanic origin group for the United States. Counts of deaths in more recent weeks can be compared with counts from earlier years (2015-2019) to determine if the number is higher than expected.",
-            "title": "AH Excess Deaths by Sex, Age, and Race and Hispanic Origin",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37943,25 +37913,65 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/m74n-4hbs",
+            "issued": "2020-11-12",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "excess deaths",
+                "hispanic origin",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "race",
+                "sex",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-04-26",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Excess Deaths by Sex, Age, and Race and Hispanic Origin"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/onc-budget-performance-measure-data",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2015-09-01",
-            "references": [
-                "https://www.healthit.gov/data/apps/onc-budget-performance-measures"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/onc-budget-performance-measure-data",
+            "description": "The dataset contains all the current and historical performance measures submitted as part of ONC;s annual budget formulation process. These measures track agency priorities for electronic health record adoption, health information exchange, patient engagement, and privacy and security. Each measure contains the annual estimate and a measure target, if applicable, for all the years the measure was reported in the ONC Budget.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/performance-measures.csv",
+                    "mediaType": "text/csv",
+                    "title": "performance-measures.csv"
+                }
             ],
+            "identifier": "8a9m6fom-b3x8-fk2t-sho0-d9sqcf25xomk",
+            "issued": "2023-10-03",
             "keyword": [
                 "adoption",
                 "budget formulation",
@@ -37973,107 +37983,79 @@
                 "performance measure",
                 "view download transmit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/onc-budget-performance-measure-data",
+            "modified": "2015-09-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "8a9m6fom-b3x8-fk2t-sho0-d9sqcf25xomk",
-            "description": "The dataset contains all the current and historical performance measures submitted as part of ONC;s annual budget formulation process. These measures track agency priorities for electronic health record adoption, health information exchange, patient engagement, and privacy and security. Each measure contains the annual estimate and a measure target, if applicable, for all the years the measure was reported in the ONC Budget.",
-            "title": "ONC Budget Performance Measure Data",
-            "programCode": [
-                "009:110"
+            "references": [
+                "https://www.healthit.gov/data/apps/onc-budget-performance-measures"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/performance-measures.csv",
-                    "mediaType": "text/csv",
-                    "title": "performance-measures.csv"
-                }
-            ],
-            "describedBy": "https://www.healthit.gov/data/datasets/onc-budget-performance-measure-data"
-        },
+            "title": "ONC Budget Performance Measure Data"
+        },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://wwwdev.cdc.gov/nchs/rss/rapid-surveys-system.html",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "Rapid Surveys questionnaires are composed of questions sponsored by CDC programs and other partners to address time-sensitive data needs, public health attitudes or behaviors, and developmental work to improve concept measurement and inform future question design. It also includes standard variables used for sample weighting and calibration, as well as selected portions of existing content from NCHS surveys (such as the National Health Interview Survey) to compare panel estimates to these benchmarks, assess the fitness-for-use of the panel survey data, and for other methodological purposes. Each round of Rapid Surveys has at least 4,000 adult participants. Each file includes questionnaire data, limited paradata, some demographic and characteristic data, and sample weights. The datafiles include records on both survey responders, partial responders, and sampled non-responders.",
-            "issued": "2024-07-17",
-            "@type": "dcat:Dataset",
-            "temporal": "2023",
-            "modified": "2024-10-18",
-            "keyword": [
-                "dhis",
-                "nchs"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/h6vx-wafp",
             "description": "The NCHS Rapid Surveys System includes questions sponsored by CDC programs and other partners to address time-sensitive data needs, public health attitudes or behaviors, and developmental work to improve concept measurement and inform future question design. It also includes standard variables used for sample weighting and calibration, as well as selected portions of existing content from NCHS surveys (such as the National Health Interview Survey) to compare panel estimates to these benchmarks, assess the fitness-for-use of the panel survey data, and for other methodological purposes.",
-            "title": "NCHS Rapid Survey Systems Restricted Use File",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/rdc/b1datatype/rdcrss.htm",
-                    "description": "The NCHS Rapid Surveys System is a platform for CDC to provide reliable, actionable data of known quality to public health experts, government officials, and community leaders. The Rapid Surveys System includes probability-sampled commercial online surveys. Data are collected quarterly from a minimum of 4,000 adult participants from two commercial panels: AmeriSpeak (conducted by NORC at the University of Chicago) and KnowledgePanel (conducted by Ipsos). Results from commercial online surveys are available faster than from traditional population health surveys, thus enabling timelier access to relevant health-related data. Rapid Surveys questionnaires are composed of questions sponsored by CDC programs and other partners to address time-sensitive data needs, public health attitudes or behaviors, and developmental work to improve concept measurement and inform future question design. It also includes standard variables used for sample weighting and calibration, as well as selected portions of existing content from NCHS surveys (such as the National Health Interview Survey) to compare panel estimates to these benchmarks, assess the fitness-for-use of the panel survey data, and for other methodological purposes. Each round of Rapid Surveys has at least 4,000 adult participants. Each file includes questionnaire data, limited paradata, some demographic and characteristic data, and sample weights. The datafiles include records on both survey responders, partial responders, and sampled non-responders.",
                     "@type": "dcat:Distribution",
+                    "description": "The NCHS Rapid Surveys System is a platform for CDC to provide reliable, actionable data of known quality to public health experts, government officials, and community leaders. The Rapid Surveys System includes probability-sampled commercial online surveys. Data are collected quarterly from a minimum of 4,000 adult participants from two commercial panels: AmeriSpeak (conducted by NORC at the University of Chicago) and KnowledgePanel (conducted by Ipsos). Results from commercial online surveys are available faster than from traditional population health surveys, thus enabling timelier access to relevant health-related data. Rapid Surveys questionnaires are composed of questions sponsored by CDC programs and other partners to address time-sensitive data needs, public health attitudes or behaviors, and developmental work to improve concept measurement and inform future question design. It also includes standard variables used for sample weighting and calibration, as well as selected portions of existing content from NCHS surveys (such as the National Health Interview Survey) to compare panel estimates to these benchmarks, assess the fitness-for-use of the panel survey data, and for other methodological purposes. Each round of Rapid Surveys has at least 4,000 adult participants. Each file includes questionnaire data, limited paradata, some demographic and characteristic data, and sample weights. The datafiles include records on both survey responders, partial responders, and sampled non-responders.",
+                    "downloadURL": "https://www.cdc.gov/rdc/b1datatype/rdcrss.htm",
+                    "mediaType": "text/html",
                     "title": "NCHS Rapid Surveys System Restricted Use File"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/h6vx-wafp",
+            "issued": "2024-07-17",
+            "keyword": [
+                "dhis",
+                "nchs"
+            ],
+            "landingPage": "https://wwwdev.cdc.gov/nchs/rss/rapid-surveys-system.html",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-10-18",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "rights": "Rapid Surveys questionnaires are composed of questions sponsored by CDC programs and other partners to address time-sensitive data needs, public health attitudes or behaviors, and developmental work to improve concept measurement and inform future question design. It also includes standard variables used for sample weighting and calibration, as well as selected portions of existing content from NCHS surveys (such as the National Health Interview Survey) to compare panel estimates to these benchmarks, assess the fitness-for-use of the panel survey data, and for other methodological purposes. Each round of Rapid Surveys has at least 4,000 adult participants. Each file includes questionnaire data, limited paradata, some demographic and characteristic data, and sample weights. The datafiles include records on both survey responders, partial responders, and sampled non-responders.",
+            "spatial": "United States",
+            "temporal": "2023",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "NCHS Rapid Survey Systems Restricted Use File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/9v8q-thkj",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-03-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-22",
-            "keyword": [
-                "exchange puf",
-                "machine readable",
-                "marketplace puf",
-                "py2023"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Center for Consumer Information and Insurance Oversight",
                 "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Center for Consumer Information and Insurance Oversight"
-            },
-            "identifier": "a96baa25-9d80-49b3-9339-97e6726e9d81",
             "description": "The Machine Readable PUF (MR-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The MR-PUF contains issuer-level URL locations for machine-readable network provider and formulary information.",
-            "title": "Machine Readable PUF - PY2023",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38081,40 +38063,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "a96baa25-9d80-49b3-9339-97e6726e9d81",
+            "issued": "2023-03-17",
+            "keyword": [
+                "exchange puf",
+                "machine readable",
+                "marketplace puf",
+                "py2023"
+            ],
+            "landingPage": "https://healthdata.gov/d/9v8q-thkj",
+            "modified": "2023-03-22",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Machine Readable PUF - PY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-10-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-23, 2023-2024, & 2024-25",
-            "modified": "2025-01-29",
-            "keyword": [
-                "flu vaccination",
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "vsd"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ivdz-qhnr",
             "description": "\u2022\tMonthly Cumulative Percent of Persons Who Received \u22651 Influenza Vaccination Doses, by Influenza Season, Age Group and Jurisdiction.\n\n\u2022\tInfluenza (flu) vaccination coverage for children and adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems Resources (IIS) data, submitted from jurisdictions to CDC monthly, in aggregate, by age group (https://www.cdc.gov/iis/about/).",
-            "title": "Monthly Cumulative Number and Percent of Persons Children 6 Months\u201317 Years Who Received \u22651 Influenza Vaccination Doses, by Influenza Season, Age Group, and Jurisdiction, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38137,53 +38117,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/ivdz-qhnr",
+            "issued": "2024-10-16",
+            "keyword": [
+                "flu vaccination",
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "vsd"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2025-01-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National",
+            "temporal": "2022-23, 2023-2024, & 2024-25",
             "theme": [
                 "Flu Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Monthly Cumulative Number and Percent of Persons Children 6 Months\u201317 Years Who Received \u22651 Influenza Vaccination Doses, by Influenza Season, Age Group, and Jurisdiction, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
-            "modified": "2024-05-24",
-            "references": [
-                "NIS-Flu"
-            ],
-            "keyword": [
-                "children",
-                "flu",
-                "flu shot",
-                "influenza",
-                "nis",
-                "nis-flu",
-                "vaccine coverage"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vax Views",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/eudc-n39h",
             "description": "Weekly Cumulative Influenza Vaccination Coverage, Children 6 months through 17 years, United States\n\n\u2022 Archived data are available here:  https://data.cdc.gov/resource/vfj2-bfuw \n\u2022 Influenza vaccination coverage among children is assessed through the National Immunization Survey-Flu (NIS-Flu) annually, providing weekly influenza vaccination coverage estimates for children 6 months\u201317 years based upon parental report. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\no NIS-Flu is a national random-digit-dialed cellular telephone survey of households conducted during the flu season (October-June).\n\u2022 Final estimates for prior seasons and other flu vaccination data are available at CDC\u2019s FluVaxView:  https://www.cdc.gov/flu/fluvaxview/index.htm.",
-            "title": "Weekly Cumulative Influenza Vaccination Coverage, Children 6 months through 17 years, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38206,40 +38181,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/eudc-n39h",
+            "issued": "2023-12-01",
+            "keyword": [
+                "children",
+                "flu",
+                "flu shot",
+                "influenza",
+                "nis",
+                "nis-flu",
+                "vaccine coverage"
+            ],
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2024-05-24",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "NIS-Flu"
+            ],
+            "spatial": "United States",
+            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Influenza Vaccination Coverage, Children 6 months through 17 years, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/biid-68vb",
-            "issued": "2018-08-03",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-09",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jarvis Sims",
                 "hasEmail": "mailto:xma4@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/biid-68vb",
             "description": "CDC Science Clips is an online bibliographic digest featuring scientific articles and publications that are shared with the public health community each week, to enhance awareness of emerging scientific knowledge.",
-            "title": "Science Clips",
-            "programCode": [
-                "009:038"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38262,39 +38249,32 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/biid-68vb",
+            "issued": "2018-08-03",
+            "landingPage": "https://data.cdc.gov/d/biid-68vb",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-09",
+            "programCode": [
+                "009:038"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "Science Clips"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2018-03-07",
-            "@type": "dcat:Dataset",
-            "temporal": "1999/2016",
-            "modified": "2022-03-31",
-            "keyword": [
-                "injury",
-                "mortality",
-                "nchs",
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/vc9m-u7tv",
             "description": "This dataset describes injury mortality in the United States beginning in 1999. Two concepts are included in the circumstances of an injury death: intent of injury and mechanism of injury. Intent of injury describes whether the injury was inflicted purposefully (intentional injury) and, if purposeful, whether the injury was self-inflicted (suicide or self-harm) or inflicted by another person (homicide). Injuries that were not purposefully inflicted are considered unintentional (accidental) injuries. Mechanism of injury describes the source of the energy transfer that resulted in physical or physiological harm to the body.",
-            "title": "NCHS - Injury Mortality: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38317,56 +38297,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/vc9m-u7tv",
+            "issued": "2018-03-07",
+            "keyword": [
+                "injury",
+                "mortality",
+                "nchs",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-03-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "1999/2016",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - Injury Mortality: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-outpatient-hospitals/medicare-outpatient-hospitals-by-geography-and-service",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2015-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-04",
-            "references": [
-                "https://data.cms.gov/resources/medicare-outpatient-hospitals-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
-                "hospitals & facilities",
-                "medicare",
-                "national",
-                "original medicare",
-                "outpatient facilities",
-                "states & territories"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicare Provider Data - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/04baec39-4a54-400e-824d-8e75251ceda9/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-outpatient-hospitals-by-geography-and-service-data-dictionary",
             "description": "The Medicare Outpatient Hospitals by Geography and Service dataset provides information on services for Original Medicare Part B\u00a0beneficiaries by OPPS hospitals. These datasets contain information on the number of services, payments, and submitted charges organized by geography and comprehensive Ambulatory Payment Classification (APC).",
-            "title": "Medicare Outpatient Hospitals - by Geography and Service",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/04baec39-4a54-400e-824d-8e75251ceda9/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/04baec39-4a54-400e-824d-8e75251ceda9/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Outpatient Hospitals - by Geography and Service : 2022-12-01"
                 },
                 {
@@ -38466,53 +38442,52 @@
                     "title": "Medicare Outpatient Hospitals - by Geography and Service : 2015-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-outpatient-hospitals-by-geography-and-service-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/04baec39-4a54-400e-824d-8e75251ceda9/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "hospitals & facilities",
+                "medicare",
+                "national",
+                "original medicare",
+                "outpatient facilities",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-outpatient-hospitals/medicare-outpatient-hospitals-by-geography-and-service",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-04",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-outpatient-hospitals-methodology"
+            ],
+            "temporal": "2015-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Outpatient Hospitals - by Geography and Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9kjw-3miq",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2021-09-10",
-            "keyword": [
-                "business closure",
-                "business reopening",
-                "covid-19",
-                "executive order",
-                "government order",
-                "legal epidemiology",
-                "mitigation",
-                "proclamation",
-                "public health order",
-                "social distancing"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "T.J. Pierce",
                 "hasEmail": "mailto:pwc2@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9kjw-3miq",
             "description": "State and territorial executive orders, administrative orders, resolutions, and proclamations are collected from government websites and cataloged and coded using Microsoft Excel by one coder with one or more additional coders conducting quality assurance.\n\nData were collected to determine when bars in states and territories were subject to closing and reopening requirements through executive orders, administrative orders, resolutions, and proclamations for COVID-19. Data can be used to determine when bars in states and territories were subject to closing and reopening requirements through executive orders, administrative orders, resolutions, and proclamations for COVID-19. Data consists exclusively of state and territorial orders, many of which apply to specific counties within their respective state or territory; therefore, data is broken down to the county level.\n\nThese data are derived from publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly close or reopen bars found by the CDC, COVID-19 Community Intervention & Critical Populations Task Force, Monitoring & Evaluation Team, Mitigation Policy Analysis Unit, and the CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 11, 2020 through August 15, 2021.  These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded; news media reports on restrictions were excluded. Recommendations not included in an order are not included in these data. Effective and expiration dates were coded using only the date provided; no distinction was made based on the specific time of the day the order became effective or expired. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
-            "title": "U.S. State and Territorial Orders Closing and Reopening Bars Issued from March 11, 2020 through August 15, 2021 by County by Day",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38535,48 +38510,49 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9kjw-3miq",
+            "issued": "2021-09-10",
+            "keyword": [
+                "business closure",
+                "business reopening",
+                "covid-19",
+                "executive order",
+                "government order",
+                "legal epidemiology",
+                "mitigation",
+                "proclamation",
+                "public health order",
+                "social distancing"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9kjw-3miq",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2021-09-10",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Policy Surveillance"
-            ]
+            ],
+            "title": "U.S. State and Territorial Orders Closing and Reopening Bars Issued from March 11, 2020 through August 15, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
+            "accrualPeriodicity": "Annually. Dataset will no longer be updated after the 2022 release in summer 2024.",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
-            "issued": "2024-02-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2016-2021",
-            "modified": "2024-12-23",
-            "references": [
-                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHAMCS/"
-            ],
-            "keyword": [
-                "diagnosis",
-                "emergency department",
-                "patient characteristics",
-                "reason for visit",
-                "visit characteristics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:CDCINFO@CDC.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6vwk-ensg",
+            "describedBy": "ftp.cdc.gov - /pub/Health_Statistics/NCHS/Dataset_Documentation/NHAMCS/",
             "description": "List of footnotes, notes, and source information for The National Hospital Ambulatory Medical Care Survey (NHAMCS). Each row of this dataset contains the accompanying text for a footnote found in NHAMCS dataset. The footnote lookup can be merged onto any NHAMCS dataset using, DATASET_SHORT_NAME, FN_ID, FN_TYPE, and FN_TEXT.\n\n\nSOURCE: National Center for Health Statistics CDC, The National Hospital Ambulatory Medical Care Survey (NHAMCS)",
-            "title": "DQS Estimate of Emergency Department Visits in the United States Footnotes",
-            "isPartOf": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38599,46 +38575,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "ftp.cdc.gov - /pub/Health_Statistics/NCHS/Dataset_Documentation/NHAMCS/",
+            "identifier": "https://data.cdc.gov/api/views/6vwk-ensg",
+            "isPartOf": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
+            "issued": "2024-02-26",
+            "keyword": [
+                "diagnosis",
+                "emergency department",
+                "patient characteristics",
+                "reason for visit",
+                "visit characteristics"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annually. Dataset will no longer be updated after the 2022 release in summer 2024.",
+            "modified": "2024-12-23",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHAMCS/"
+            ],
+            "rights": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
+            "spatial": "United States",
+            "temporal": "2016-2021",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "DQS Estimate of Emergency Department Visits in the United States Footnotes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm142438.htm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-14",
-            "references": [
-                "http://www.accessdata.fda.gov/scripts/cder/ndc/default.cfm",
-                "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM257244.zip"
-            ],
-            "keyword": [
-                "cder",
-                "ndc"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "2b7ec03d-67dc-4544-b1d6-b9aa02f693c6",
+            "describedBy": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm254527.htm",
             "description": "The Drug Listing Act of 1972 requires registered drug establishments to provide the Food and Drug Administration (FDA) with a current list of all drugs manufactured, prepared, propagated, compounded, or processed by it for commercial distribution. (See Section 510 of the Federal Food, Drug, and Cosmetic Act (Act) (21 U.S.C. \ufffd 360)). Drug products are identified and reported using a unique, three-segment number, called the National Drug Code (NDC), which serves as a universal product identifier for drugs. FDA publishes the listed NDC numbers and the information submitted as part of the listing information in the NDC Directory which is updated daily.",
-            "title": "National Drug Code Directory",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38646,33 +38626,40 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm254527.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "2b7ec03d-67dc-4544-b1d6-b9aa02f693c6",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cder",
+                "ndc"
+            ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm142438.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-14",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.accessdata.fda.gov/scripts/cder/ndc/default.cfm",
+                "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM257244.zip"
+            ],
+            "title": "National Drug Code Directory"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/eur4-ng38",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division, Pathology and Physiology Research Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/eur4-ng38",
             "description": "Adipose tissue (AT), an endocrine organ, plays a central role in maintenance of whole-body energy homeostasis through its release of adipokines. Obesity, affecting over 40% of American adults, disrupts adipocyte metabolism leading to chronic systemic inflammation and metabolic dysfunction (MetDys). MetDys is associated with impaired lung function, pulmonary hypertension, and asthma. The aim of this study was to investigate the effects of high-fat Western diet (HFWD)-consumption on silica-induced pulmonary inflammation and fibrosis in the F344 rat.",
-            "title": "High-fat western diet consumption exacerbates silica-induced pulmonary inflammation and fibrosis",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38680,44 +38667,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/eur4-ng38",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/eur4-ng38",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "High-fat western diet consumption exacerbates silica-induced pulmonary inflammation and fibrosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/9xdh-kzb9",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-07-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-31",
-            "keyword": [
-                "applications",
-                "child enrollment",
-                "chip",
-                "eligibility determinations",
-                "enrollment",
-                "medicaid",
-                "program enrollment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "ebcfc16f-8291-4c61-82a4-055846d72f3a",
             "description": "State-reported data on Medicaid and CHIP eligibility renewals conducted during the reporting period and call center operations\r\n<br /><b>Sources:</b> <br />(1) March and April 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of June 13, 2023. Florida's March and April 2023 Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of June 05, 2023. May 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of July 12, 2023. Florida's May 2023 Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of July 03, 2023. June 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of August 16, 2023. Florida's June 2023 Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of July 31, 2023. July 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of September 12, 2023. August 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of October 23, 2023. September 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of November 07, 2023. Delaware\u2019s September state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of November 28, 2023. October 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of December 05, 2023. November 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of January 05, 2024. December 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of February 08, 2024. January 2024 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of March 05, 2024. February 2024 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of April 02, 2024. The total number of Medicaid and CHIP beneficiaries for whom a renewal was initiated in the reporting month (metric 4) for Idaho and Nebraska as of April 12, 2024. March 2024 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of May 07, 2024. April 2024 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of June 11, 2024. May 2024 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of July 02, 2024. June 2024 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of August 06, 2024. July 2024 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report as of September 09, 2024. (2) Call Center Data from the Medicaid and CHIP Eligibility and Enrollment Performance Indicator Data as of September 10, 2024.<br />\t\r\n<b>Notes:</b> For all states, data may be affected by mitigation strategies in place, such as those related to ex parte functionality. Georgia reported data for individuals who continue to be eligible following a change in circumstances and were granted a new 12-month eligibility period during the April - July 2024 reporting periods, along with data on individuals due for renewal in these months. South Dakota did not initiate or complete renewals in the March - July 2024 reporting period due to a mitigation strategy for ex parte functionality. South Dakota did not initiate renewals in the February 2024 reporting period due to a mitigation strategy for ex parte functionality. Due to temporary renewal process changes, most renewals due in Iowa, including ex parte renewals, were not completed by the end of the reporting month for the December 2023 - February 2024 reporting periods. Hawaii and Vermont experienced a natural disaster, and the number of renewals initiated and completed in the reporting period were impacted due to the disaster response efforts in the month of August 2023. South Carolina does not have renewal outcomes to report",
-            "title": "Medicaid and CHIP CAA Reporting Metrics",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38822,21 +38801,55 @@
                     "title": "March and April 2023 Medicaid and CHIP CAA Reporting Metrics"
                 }
             ],
+            "identifier": "ebcfc16f-8291-4c61-82a4-055846d72f3a",
+            "issued": "2023-07-28",
+            "keyword": [
+                "applications",
+                "child enrollment",
+                "chip",
+                "eligibility determinations",
+                "enrollment",
+                "medicaid",
+                "program enrollment"
+            ],
+            "landingPage": "https://healthdata.gov/d/9xdh-kzb9",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-10-31",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Unwinding"
-            ]
+            ],
+            "title": "Medicaid and CHIP CAA Reporting Metrics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2006",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), to analyze general treatment services trends, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment<br />\nFacility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment and pre-treatment, substance abuse therapy and counseling, pharmacotherapies, testing, transitional, ancillary), primary focus (substance abuse, mental health, both, general health, and other), hotline operation, Opioid Treatment Programs and medication dispensed/prescribed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2006) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2006-nid13583",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2006-nid13583"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2006-nid13583",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -38849,58 +38862,29 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2006",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2006-nid13583",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), to analyze general treatment services trends, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment<br />\nFacility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment and pre-treatment, substance abuse therapy and counseling, pharmacotherapies, testing, transitional, ancillary), primary focus (substance abuse, mental health, both, general health, and other), hotline operation, Opioid Treatment Programs and medication dispensed/prescribed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2006)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2006-nid13583",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2006) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2006-nid13583"
-                }
-            ]
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2006)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nlm.nih.gov/hmd/digicolls/henkel/index.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "history of medicine"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/kytw-zci7",
             "description": "XML-encoded transcriptions and images of 828 handwritten letters (1786-1907) from the History of Medicine's Henkel Family correspondence collection; comprised largely of letters to and from Caspar C. Henkel (1835-1908).",
-            "title": "Physician\u2019s Lives in the Shenandoah Valley",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38909,20 +38893,49 @@
                     "title": "Access Physician\u2019s Lives in the Shenandoah Valley"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/kytw-zci7",
+            "issued": "2021-06-30",
+            "keyword": [
+                "history of medicine"
+            ],
+            "landingPage": "https://www.nlm.nih.gov/hmd/digicolls/henkel/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Historical Curated Content"
-            ]
+            ],
+            "title": "Physician\u2019s Lives in the Shenandoah Valley"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1995",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, and tobacco among members of United<br />\nStates households aged 12 and older. Questions include age at first<br />\nuse as well as lifetime, annual, and past-month usage for the<br />\nfollowing drug classes: marijuana, cocaine (and crack), hallucinogens,<br />\nheroin, inhalants, alcohol, tobacco, anabolic steroids, nonmedical use<br />\nof prescription drugs including psychotherapeutics, and polysubstance<br />\nuse. Respondents were also asked about substance abuse treatment<br />\nhistory, illegal activities, problems resulting from use of drugs,<br />\nperceptions of the risks involved, personal and family income sources<br />\nand amounts, need for treatment for drug or alcohol use, criminal<br />\nrecord, and needle-sharing. Questions on mental health and access to<br />\ncare, which were introduced in the 1994-B questionnaire (see NATIONAL<br />\nHOUSEHOLD SURVEY ON DRUG ABUSE, 1994), were retained in<br />\nthis administration of the survey. Demographic data include gender,<br />\nrace, age, ethnicity, marital status, motor vehicle use, educational<br />\nlevel, job status, income level, veteran status, and past and current<br />\nhousehold composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1995) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1995-nid13539",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1995-nid13539"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1995-nid13539",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "alcohol consumption",
@@ -38956,59 +38969,29 @@
                 "treatment",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1995",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1995-nid13539",
-            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, and tobacco among members of United<br />\nStates households aged 12 and older. Questions include age at first<br />\nuse as well as lifetime, annual, and past-month usage for the<br />\nfollowing drug classes: marijuana, cocaine (and crack), hallucinogens,<br />\nheroin, inhalants, alcohol, tobacco, anabolic steroids, nonmedical use<br />\nof prescription drugs including psychotherapeutics, and polysubstance<br />\nuse. Respondents were also asked about substance abuse treatment<br />\nhistory, illegal activities, problems resulting from use of drugs,<br />\nperceptions of the risks involved, personal and family income sources<br />\nand amounts, need for treatment for drug or alcohol use, criminal<br />\nrecord, and needle-sharing. Questions on mental health and access to<br />\ncare, which were introduced in the 1994-B questionnaire (see NATIONAL<br />\nHOUSEHOLD SURVEY ON DRUG ABUSE, 1994), were retained in<br />\nthis administration of the survey. Demographic data include gender,<br />\nrace, age, ethnicity, marital status, motor vehicle use, educational<br />\nlevel, job status, income level, veteran status, and past and current<br />\nhousehold composition.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-1995)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1995-nid13539",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-1995) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1995-nid13539"
-                }
-            ]
+            "title": "National Household Survey on Drug Abuse (NHSDA-1995)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6i2x-3kw3",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6i2x-3kw3",
             "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 5 - Chicago",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39031,45 +39014,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6i2x-3kw3",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6i2x-3kw3",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-10-18",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Motor Vehicle"
-            ]
+            ],
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 5 - Chicago"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6rpz-c2y5",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "nedss",
-                "netss",
-                "nndss",
-                "salmonellosis (excluding typhoid fever and paratyphoid fever)",
-                "shiga toxin-producing escherichia coli",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6rpz-c2y5",
             "description": "NNDSS - Table II. Salmonellosis (excluding typhoid fever and paratyphoid fever) to Shigellosis - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. FoFor further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.  \r\n\r\n\u2020 Prior to 2018, cases of paratyphoid fever were included as salmonellosis, but beginning in 2018 they are being published as paratyphoid fever (see Table 1).",
-            "title": "NNDSS - Table II. Salmonellosis (excluding typhoid fever and paratyphoid fever) to Shigellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39092,41 +39069,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6rpz-c2y5",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "nedss",
+                "netss",
+                "nndss",
+                "salmonellosis (excluding typhoid fever and paratyphoid fever)",
+                "shiga toxin-producing escherichia coli",
+                "shigellosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6rpz-c2y5",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-01-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Salmonellosis (excluding typhoid fever and paratyphoid fever) to Shigellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/a22e-66mr",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-14",
-            "keyword": [
-                "exchange puf",
-                "marketplace puf",
-                "py2024",
-                "service area"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Center for Consumer Information and Insurance Oversight",
                 "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Center for Consumer Information and Insurance Oversight"
-            },
-            "identifier": "bbc5e308-377c-4a05-830e-0ef9b893dc01",
             "description": "The Service Area PUF (SA-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The SA-PUF contains issuer-level data on geographic service areas including state, county, and zip code.",
-            "title": "Service Area PUF - PY2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39134,40 +39116,38 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "bbc5e308-377c-4a05-830e-0ef9b893dc01",
+            "issued": "2024-08-06",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2024",
+                "service area"
+            ],
+            "landingPage": "https://healthdata.gov/d/a22e-66mr",
+            "modified": "2024-08-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Service Area PUF - PY2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-10-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024 & 2024-2025",
-            "modified": "2025-01-29",
-            "keyword": [
-                "covid-19 vaccination",
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "vsd"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/q84f-e68r",
             "description": "\u2022 Monthly Cumulative Percent of Persons Who Received 1+ 2024-25 COVID-19 Vaccination Doses and Comparison between 2024\u250025 and 2023\u250024 Seasons, by Age Group and Jurisdiction, by Age Group and Jurisdiction\n\n\u2022 COVID-19 vaccination coverage for children and adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems Resources (IIS) data, submitted from jurisdictions to CDC monthly in aggregate by age group (https://www.cdc.gov/iis/about/)",
-            "title": "Monthly Cumulative Number and Percent of Persons Who Received 1+ 2024-25 COVID-19 Vaccination Doses and Comparison between 2024-25 and 2023-24 Seasons, by Age Group and Jurisdiction, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39190,65 +39170,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/q84f-e68r",
+            "issued": "2024-10-16",
+            "keyword": [
+                "covid-19 vaccination",
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "vsd"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2025-01-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National",
+            "temporal": "2023-2024 & 2024-2025",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Monthly Cumulative Number and Percent of Persons Who Received 1+ 2024-25 COVID-19 Vaccination Doses and Comparison between 2024-25 and 2023-24 Seasons, by Age Group and Jurisdiction, United States"
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
-            ],
-            "keyword": [
-                "abuse",
-                "alcohol use",
-                "breastfeeding",
-                "contraception",
-                "infant health",
-                "medicaid",
-                "mental health",
-                "morbidity",
-                "obesity",
-                "preconception health",
-                "pregnancy history",
-                "prenatal care",
-                "reproductive health",
-                "sleep behavior",
-                "smoke exposure",
-                "stress",
-                "tobacco use",
-                "unintended pregnancy",
-                "wic"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DRH Public Inquiries",
                 "hasEmail": "mailto:PRAMSProposals@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xyxp-dxa9",
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2004/xyxp-dxa9",
             "description": "2004. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2004",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39271,41 +39234,61 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2004/xyxp-dxa9",
+            "identifier": "https://data.cdc.gov/api/views/xyxp-dxa9",
+            "issued": "2023-07-18",
+            "keyword": [
+                "abuse",
+                "alcohol use",
+                "breastfeeding",
+                "contraception",
+                "infant health",
+                "medicaid",
+                "mental health",
+                "morbidity",
+                "obesity",
+                "preconception health",
+                "pregnancy history",
+                "prenatal care",
+                "reproductive health",
+                "sleep behavior",
+                "smoke exposure",
+                "stress",
+                "tobacco use",
+                "unintended pregnancy",
+                "wic"
+            ],
+            "landingPage": "https://www.cdc.gov/prams/index.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-09-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/prams/index.htm",
+                "https://www.cdc.gov/prams/pramstat/index.html"
+            ],
             "theme": [
                 "Maternal & Child Health"
-            ]
+            ],
+            "title": "CDC PRAMStat Data for 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/a2rg-pq7e",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-06-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-11",
-            "keyword": [
-                "drug utilization",
-                "medicaid reimbursements",
-                "pharmacy"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "915e5174-0869-5c6d-a5bb-454cb31ef605",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2001",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39313,46 +39296,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "915e5174-0869-5c6d-a5bb-454cb31ef605",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/a2rg-pq7e",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-06-11",
+            "programCode": [
+                "009:076"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "State Drug Utilization"
-            ]
+            ],
+            "title": "State Drug Utilization Data 2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5wqm-pm27",
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
-                "severe acute respiratory syndrome-associated coronavirus disease",
-                "shiga toxin-producing escherichia coli",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5wqm-pm27",
             "description": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39375,38 +39352,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5wqm-pm27",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "severe acute respiratory syndrome-associated coronavirus disease",
+                "shiga toxin-producing escherichia coli",
+                "shigellosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5wqm-pm27",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://data.cdc.gov/d/6zuv-bn3z",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-10-17",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-27",
-            "keyword": [
-                "restaurant grading"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hao Tian",
                 "hasEmail": "mailto:ejq7@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6zuv-bn3z",
             "description": "",
-            "title": "Survey Data - Restaurant Grading",
-            "programCode": [
-                "009:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39429,40 +39413,43 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "systemOfRecords": "No",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "theme": [
-                "Environmental Health & Toxicology"
+            "identifier": "https://data.cdc.gov/api/views/6zuv-bn3z",
+            "issued": "2022-10-17",
+            "keyword": [
+                "restaurant grading"
             ],
+            "landingPage": "https://data.cdc.gov/d/6zuv-bn3z",
             "language": [
                 "English"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mpb9-a9up",
-            "bureauCode": [
-                "009:20"
             ],
-            "issued": "2024-11-15",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-10-27",
+            "programCode": [
+                "009:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "systemOfRecords": "No",
+            "theme": [
+                "Environmental Health & Toxicology"
+            ],
+            "title": "Survey Data - Restaurant Grading"
+        },
+        {
             "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division, Pathology and Physiology Research Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mpb9-a9up",
             "description": "This study investigated the inhalation toxicity of the emissions from 3-D printing with acrylonitrile butadiene styrene (ABS) filament using an air-liquid interface (ALI) in vitro model. Primary normal human-derived bronchial epithelial cells (NHBEs) were exposed to ABS filament emissions in an ALI for 4 h. The mean and mode diameters of ABS emitted particles in the medium were 175 \u00b1 24 nm and 153 \u00b1 15 nm, respectively. The average particle deposition per surface area of the epithelium was 2.29 \u00d7 107 \u00b1 1.47 \u00d7 107 particle/cm2, equivalent to an estimated average particle mass of 0.144 \u00b1 0.042 \u00b5g/cm2.",
-            "title": "Evaluation of pulmonary effects of 3-D printer emissions from acrylonitrile butadiene styrene using an air-liquid interface model of primary normal human-derived bronchial epithelial cells",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39470,40 +39457,37 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mpb9-a9up",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/mpb9-a9up",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "Evaluation of pulmonary effects of 3-D printer emissions from acrylonitrile butadiene styrene using an air-liquid interface model of primary normal human-derived bronchial epithelial cells"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-population-census-0",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-08-03",
-            "temporal": "1970-01-01T00:00:00-05:00/2030-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "age race sex year state county",
-                "population statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "admin",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
-            },
-            "identifier": "c0ad9152-c042-4054-a7d6-322405e2b878",
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/population.html",
             "description": "<p>The Population online databases contain data from the US Census Bureau. The Census Estimates online database contains county-level population counts for years 1970 - 2000. The data comprise the April 1st Census counts for years 1970, 1980, 1990 and 2000, the July 1st intercensal estimates for years 1971-1979 and 1981-1989, and the July 1st postcensal estimates for years 1991-1999. The Census Projections online database contains population projections for years 2004-2030 by year, state, age, race and sex, produced by the Census Bureau in 2005. The data are produced by the United States Department of Commerce, U.S. Census Bureau, Population Division.</p>",
-            "title": "CDC WONDER: Population (from Census)",
-            "programCode": [
-                "009:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39512,43 +39496,41 @@
                     "title": "API "
                 }
             ],
-            "describedBy": "http://wonder.cdc.gov/population.html",
-            "dataQuality": true,
+            "identifier": "c0ad9152-c042-4054-a7d6-322405e2b878",
+            "issued": "2012-08-03",
+            "keyword": [
+                "age race sex year state county",
+                "population statistics"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-population-census-0",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "temporal": "1970-01-01T00:00:00-05:00/2030-12-31T00:00:00-05:00",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Population (from Census)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/a5va-q4t9",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-08-10",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-17",
-            "keyword": [
-                "benefits and cost sharing",
-                "exchange puf",
-                "marketplace puf",
-                "py2022"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Center for Consumer Information and Insurance Oversight",
                 "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Center for Consumer Information and Insurance Oversight"
-            },
-            "identifier": "9dbef2bc-2fab-4700-8cf3-5501f63c58c3",
             "description": "The Benefits and Cost Sharing PUF (BenCS-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The BenCS-PUF contains plan variant-level data on essential health benefits, coverage limits, and cost sharing for each QHP and SADP.",
-            "title": "Benefits and Cost Sharing PUF - PY2022",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39556,37 +39538,39 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "9dbef2bc-2fab-4700-8cf3-5501f63c58c3",
+            "issued": "2022-08-10",
+            "keyword": [
+                "benefits and cost sharing",
+                "exchange puf",
+                "marketplace puf",
+                "py2022"
+            ],
+            "landingPage": "https://healthdata.gov/d/a5va-q4t9",
+            "modified": "2022-08-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Benefits and Cost Sharing PUF - PY2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/head-start-family-and-child-experiences-survey-faces-2003-cohort",
             "bureauCode": [
                 "009:70"
             ],
-            "issued": "2013-06-19",
-            "temporal": "2003-01-01T00:00:00-05:00/2006-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "children's health",
-                "department-of-health-human-services"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "admin",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Health & Human Services"
-            },
-            "identifier": "fc856fae-78e5-4638-ab20-9563a6ae8172",
+            "dataQuality": true,
+            "describedBy": "http://researchconnections.org/childcare/resources/14419?q=Family+and+Child+Experience+Survey",
             "description": "<p>Descriptive, longitudinal study including direct assessments, classroom observation, parent and teacher interviews, for a nationally represenative sample of Head Start Children</p>",
-            "title": "Head Start Family and Child Experiences Survey (FACES) 2003 Cohort",
-            "programCode": [
-                "009:092"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39595,41 +39579,38 @@
                     "title": "API "
                 }
             ],
-            "describedBy": "http://researchconnections.org/childcare/resources/14419?q=Family+and+Child+Experience+Survey",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "fc856fae-78e5-4638-ab20-9563a6ae8172",
+            "issued": "2013-06-19",
+            "keyword": [
+                "children's health",
+                "department-of-health-human-services"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/head-start-family-and-child-experiences-survey-faces-2003-cohort",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:092"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
+            },
+            "temporal": "2003-01-01T00:00:00-05:00/2006-01-01T00:00:00-05:00",
+            "title": "Head Start Family and Child Experiences Survey (FACES) 2003 Cohort"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/a69e-j7j4",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-14",
-            "keyword": [
-                "individual",
-                "individual market medical",
-                "py2024",
-                "qhp",
-                "qhp landscape instructions"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Center for Consumer Information and Insurance Oversight",
                 "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Center for Consumer Information and Insurance Oversight"
-            },
-            "identifier": "4d8a3f9d-ce6b-4e1c-a1a3-3903393d44ed",
             "description": "The Medical Individual Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to consumers in the individual market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2024 Individual Medical",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39637,77 +39618,69 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "4d8a3f9d-ce6b-4e1c-a1a3-3903393d44ed",
+            "issued": "2024-08-06",
+            "keyword": [
+                "individual",
+                "individual market medical",
+                "py2024",
+                "qhp",
+                "qhp landscape instructions"
+            ],
+            "landingPage": "https://healthdata.gov/d/a69e-j7j4",
+            "modified": "2024-08-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2024 Individual Medical"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.vectorbase.org/",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "national-institutes-of-health-nih"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Yao, Alison",
                 "hasEmail": "mailto:yaoal@niaid.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "568f2bc3-1825-413f-a9bc-ab4444511554",
+            "dataQuality": true,
             "description": "<p>VectorBase is a Bioinformatics Resource Center for invertebrate vectors. It is one of four Bioinformatics Resource Centers funded by NIAID to provide web-based resources to scientific community conducting basic and applied research on organisms considered potential agents of biowarfare or bioterrorism or causing emerging or re-emerging diseases.</p>",
-            "title": "VectorBase",
+            "identifier": "568f2bc3-1825-413f-a9bc-ab4444511554",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "https://www.vectorbase.org/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
             "programCode": [
                 "009:028"
             ],
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "dataQuality": true
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "title": "VectorBase"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-27",
-            "temporal": "1999/2021",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
-            "keyword": [
-                "american indian or alaska native",
-                "asian",
-                "black or african american",
-                "death rates",
-                "drug overdose",
-                "health us",
-                "hispanic or latino",
-                "men",
-                "native hawaiian or other pacific islander",
-                "opioid",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/dh32-cnpq",
             "description": "Data on drug overdose death rates in the United States, by age, sex, race, Hispanic origin, and drug type. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Vital Statistics System, Mortality File.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Drug overdose death rates, by drug type, sex, age, race, and Hispanic origin: United States from CDC WONDER",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39730,55 +39703,59 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/dh32-cnpq",
+            "issued": "2024-02-27",
+            "keyword": [
+                "american indian or alaska native",
+                "asian",
+                "black or african american",
+                "death rates",
+                "drug overdose",
+                "health us",
+                "hispanic or latino",
+                "men",
+                "native hawaiian or other pacific islander",
+                "opioid",
+                "white",
+                "women"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "modified": "2024-11-15",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "1999/2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS Drug overdose death rates, by drug type, sex, age, race, and Hispanic origin: United States from CDC WONDER"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/covid-19/medicare-covid-19-hospitalization-trends",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2022-01-01/2023-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-29",
-            "references": [
-                "https://data.cms.gov/resources/medicare-covid-19-hospitalization-trends-methodology-2023"
-            ],
-            "keyword": [
-                "health equity",
-                "hospitals & facilities",
-                "inpatient",
-                "medicare",
-                "medicare advantage",
-                "original medicare",
-                "states & territories"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CMS Program Statistics - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/2684c3e2-3598-4997-a598-0991bad6fbf2/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-covid-19-hospitalization-trends-data-dictionary",
             "description": "The Medicare COVID-19 Hospitalization Trends dataset contains aggregate information from Medicare Fee-for-Service claims, Medicare Advantage encounter, and Medicare enrollment data. It provides insight around the groups of beneficiaries that were hospitalized at different points during the pandemic.\n\n\u00a0\n\nCMS publicly released the first Preliminary Medicare COVID-19 Snapshot in June 2020 during the early stages of the Public Health Emergency for COVID-19. That report focused on COVID-19 cases and hospitalizations data for Medicare beneficiaries with a COVID-19 diagnosis. Throughout 2020 and 2021, that report was subsequently updated with refreshed data 13 times. Beginning in October 2021, CMS shifted its public COVID-19 reporting away from cumulative case and hospitalization rates to hospitalization trends over time with the release of this report, the Medicare COVID-19 Hospitalization Trends Report.\u00a0\n\n\u00a0\n\nAll prior releases of both the Preliminary Medicare COVID-19 Snapshot and the Medicare COVID-19 Hospitalization Trends Report are available for download in the Medicare COVID-19 Data - Prior Releases file.\u00a0",
-            "title": "Medicare COVID-19 Hospitalization Trends",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2684c3e2-3598-4997-a598-0991bad6fbf2/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2684c3e2-3598-4997-a598-0991bad6fbf2/data",
+                    "mediaType": "text/html",
                     "title": "Medicare COVID-19 Hospitalization Trends : 2023-12-31"
                 },
                 {
@@ -39806,47 +39783,51 @@
                     "title": "Medicare COVID-19 Hospitalization Trends : 2022-12-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-covid-19-hospitalization-trends-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/2684c3e2-3598-4997-a598-0991bad6fbf2/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health equity",
+                "hospitals & facilities",
+                "inpatient",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/covid-19/medicare-covid-19-hospitalization-trends",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-01-29",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-covid-19-hospitalization-trends-methodology-2023"
+            ],
+            "temporal": "2022-01-01/2023-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare COVID-19 Hospitalization Trends"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/muep-c3qd",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-09-03",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-20",
-            "keyword": [
-                "covid-19 vaccination",
-                "covid tracker",
-                "disability",
-                "hps"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Assessment Branch, Immunization Services Division, NCIRD, CDC",
                 "hasEmail": "mailto:VaxView@cdc.gov "
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/muep-c3qd",
             "description": "Household Pulse Survey (HPS): HPS is a rapid-response survey of adults ages \u226518 years led by the U.S. Census Bureau, in partnership with seven other federal statistical agencies, to measure household experiences during the COVID-19 pandemic. Detailed information on probability sampling using the U.S. Census Bureau\u2019s Master Address File, questionnaires, response rates, and bias assessment is available on the Census Bureau website (https://www.census.gov/data/experimental-data-products/household-pulse-survey.html).\n\nData from adults age \u226518 years are collected by 20-minute online survey from randomly sampled households stratified by state and the top 15 metropolitan statistical areas (MSAs). Data are weighted to represent total persons age 18 and older living within households and to mitigate possible bias that can result from non-responses and incomplete survey frame. Data from adults age \u226518 years are collected by 20-minute online survey from randomly sampled households stratified by state and the top 15 metropolitan statistical areas (MSAs). For more information on this survey, see https://www.census.gov/programs-surveys/household-pulse-survey.html.\n\nData are weighted to represent total persons age 18 and older living within households and to mitigate possible bias that can result from non-responses and incomplete survey frame. Responses in the Household Pulse Survey (https://www.census.gov/programs-surveys/household-pulse-survey.html) are self-reported.\u202fEstimates of vaccination coverage may differ from vaccine administration data reported at\u202fCOVID-19 Vaccinations in the United States (https://covid.cdc.gov/covid-data-tracker/#vaccinations).",
-            "title": "Household Pulse Survey (HPS): COVID-19 Vaccination among People with Disabilities",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39869,20 +39850,52 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/muep-c3qd",
+            "issued": "2021-09-03",
+            "keyword": [
+                "covid-19 vaccination",
+                "covid tracker",
+                "disability",
+                "hps"
+            ],
+            "landingPage": "https://data.cdc.gov/d/muep-c3qd",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-12-20",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "Household Pulse Survey (HPS): COVID-19 Vaccination among People with Disabilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2004",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2004) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2004-nid13579",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2004-nid13579"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2004-nid13579",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -39895,71 +39908,29 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2004",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2004-nid13579",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2004)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2004-nid13579",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2004) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2004-nid13579"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2004)"
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
-                "sex"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:healthus@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
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
@@ -39982,77 +39953,113 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://healthdata.gov/d/a97f-x9bx",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_featauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "e93bf3fa-e92e-5bfe-b8e8-552ca8f9d499",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_measure_allStates_downloadLink",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_allStates_downloadLink.csv",
-                    "description": "{\"dataset\": \"measure_allStates_downloadLink\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_allStates_downloadLink\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_allStates_downloadLink.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_allStates_downloadLink csv file"
                 }
             ],
+            "identifier": "e93bf3fa-e92e-5bfe-b8e8-552ca8f9d499",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/a97f-x9bx",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "featAuto_measure_allStates_downloadLink"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nhcs/index.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
-            "issued": "2018-06-14",
-            "@type": "dcat:Dataset",
-            "temporal": "2013-2016, 2019-2021",
-            "modified": "2024-03-05",
-            "references": [
-                "https://www.cdc.gov/rdc/data/b1/2013_NHCS.pdf",
-                "https://www.cdc.gov/rdc/data/b1/2015_NHCS_RDC_Data_Dictionary.pdf",
-                "https://www.cdc.gov/rdc/data/b1/2016_NHCS_DATA-DICTIONARY.pdf",
-                "https://www.cdc.gov/rdc/data/b1/NHCS-RDC-Data-Dictionary.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "NHCS collects data on patient care in hospital-based settings to describe patterns of health care delivery and utilization in the United States. Settings include inpatient, emergency (EDs), and outpatient departments (OPDs). The survey will provide hospital utilization statistics for the Nation.",
+            "description": "The National Hospital Care Survey (NHCS) is designed to provide accurate and reliable health care statistics that answer key questions of interest to health care and public health professionals, researchers, and health care policy makers. This includes tracking the latest trends affecting hospitals and health care organizations and factors that influence the use of health care resources, the quality of health care, and disparities in health care services provided to population subgroups in the United States.\nNHCS collects data on patient care in hospital-based settings to describe patterns of health care delivery and utilization in the United States. Settings include inpatient, emergency (EDs), and outpatient departments (OPDs). The survey will provide hospital utilization statistics for the Nation. In addition, NHCS will also be able to monitor national trends in substance use-related ED visits including opioid visits.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Standard application process link attached.",
+                    "downloadURL": "https://www.cdc.gov/rdc/b3prosal/pp300.htm",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ijr5-qdv2",
+            "isPartOf": "https://www.cdc.gov/nchs/nhds/nhds_questionnaires.htm",
+            "issued": "2018-06-14",
             "keyword": [
                 "emergency departments",
                 "healthcare",
@@ -40065,62 +40072,42 @@
                 "outpatient departments",
                 "research-data-center"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nhcs/index.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-03-05",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/ijr5-qdv2",
-            "description": "The National Hospital Care Survey (NHCS) is designed to provide accurate and reliable health care statistics that answer key questions of interest to health care and public health professionals, researchers, and health care policy makers. This includes tracking the latest trends affecting hospitals and health care organizations and factors that influence the use of health care resources, the quality of health care, and disparities in health care services provided to population subgroups in the United States.\nNHCS collects data on patient care in hospital-based settings to describe patterns of health care delivery and utilization in the United States. Settings include inpatient, emergency (EDs), and outpatient departments (OPDs). The survey will provide hospital utilization statistics for the Nation. In addition, NHCS will also be able to monitor national trends in substance use-related ED visits including opioid visits.",
-            "title": "National Hospital Care Survey 2013-2016, 2019-2021, restricted data",
-            "isPartOf": "https://www.cdc.gov/nchs/nhds/nhds_questionnaires.htm",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/b3prosal/pp300.htm",
-                    "mediaType": "text/html",
-                    "description": "Standard application process link attached."
-                }
+            "references": [
+                "https://www.cdc.gov/rdc/data/b1/2013_NHCS.pdf",
+                "https://www.cdc.gov/rdc/data/b1/2015_NHCS_RDC_Data_Dictionary.pdf",
+                "https://www.cdc.gov/rdc/data/b1/2016_NHCS_DATA-DICTIONARY.pdf",
+                "https://www.cdc.gov/rdc/data/b1/NHCS-RDC-Data-Dictionary.pdf"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "United States",
-            "describedBy": "NHCS collects data on patient care in hospital-based settings to describe patterns of health care delivery and utilization in the United States. Settings include inpatient, emergency (EDs), and outpatient departments (OPDs). The survey will provide hospital utilization statistics for the Nation.",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2013-2016, 2019-2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Hospital Care Survey 2013-2016, 2019-2021, restricted data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/87ea-ip25",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Division of Field Studies and Engineering, Hazard Evaluation and Technical Assistance Branch",
                 "hasEmail": "mailto:HHERequestHelp@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/87ea-ip25",
             "description": "This noise database was developed to provide researchers and other interested stakeholders with noise measurement results that the National Institute for Occupational Safety and Health (NIOSH) has collected during health hazard evaluation (HHE) surveys from 1996 through 2013. HHEs are requested by employees or their representatives, or employers, to help learn whether health hazards are present at their workplace. The scope of HHEs varies based on the requestors\u2019 concerns and the NIOSH project officers\u2019 professional judgment. Only noise measurement results are included in this database; however, many HHEs include evaluation of exposures other than noise. Individual HHE reports are published on the NIOSH website. When available, the database provides a direct link to the HHE report for each of the noise measurement results.\n\nThe noise database contains workplace noise measurement results from 77 HHE reports, including over 808 personal noise exposure measurements and 582 area noise measurements. It also includes the following information: U.S. state or territory; Occupational Safety and Health Administration (OSHA) region; National Occupational Research Agenda (NORA) sector; North American Industry Classification System (NAICS) code; facility description; type of dosimeter or sound level meter used; whether a hearing conservation program was in place; whether a hearing protection was used; whether octave band data was collected; job title; noise-generating activities; location of noise measurements; start and end date for site visit; type (full-shift, partial-shift, or task-based) and duration of noise measurement; type of noise (continuous, impulsive, or intermittent); exposure to ototoxic chemicals; and results in decibels A-weighted (dBA) and percent dose according to OSHA and NIOSH noise measurement criteria. This database is an ongoing project and will be updated at least yearly to add the most recent HHE noise measurement data.",
-            "title": "NIOSH Health Hazard Evaluation Program Noise Measurement Database",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40128,98 +40115,90 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/87ea-ip25",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/87ea-ip25",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Institute for Occupational Safety and Health"
-            ]
+            ],
+            "title": "NIOSH Health Hazard Evaluation Program Noise Measurement Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/a9qt-prxv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-20",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-10",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "34d677c8-e62a-589b-b48e-0b33bc126271",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet version v2.10.64 (coreset-prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/version.csv",
-                    "description": "CoreSet version v2.10.64 (coreset-prod)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet version v2.10.64 (coreset-prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/version.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet version v2.10.64 (coreset-prod)"
                 }
             ],
+            "identifier": "34d677c8-e62a-589b-b48e-0b33bc126271",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/a9qt-prxv",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2025-01-10",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSet version v2.10.64 (coreset-prod)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-provider",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2013-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-04",
-            "references": [
-                "https://data.cms.gov/resources/medicare-part-d-prescribers-methodology"
-            ],
-            "keyword": [
-                "drugs",
-                "health equity",
-                "medicare",
-                "medicare prescription drug",
-                "physicians & practitioners"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicare Provider Data - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/14d8e8a9-7e9b-4370-a044-bf97c46b4b44/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-part-d-prescribers-by-provider-data-dictionary",
             "description": "The Medicare Part D Prescribers by Provider dataset contains information on prescription drugs prescribed by individual physicians and other health care providers and paid for under the Medicare Part D Prescription Drug Program. The dataset identifies providers by their National Provider Identifier (NPI) and summarizes for each prescriber the total number of prescriptions that were dispensed, which include original prescriptions and any refills, and the total drug cost.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Medicare Part D Prescribers - by Provider",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/14d8e8a9-7e9b-4370-a044-bf97c46b4b44/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/14d8e8a9-7e9b-4370-a044-bf97c46b4b44/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Part D Prescribers - by Provider : 2022-12-30"
                 },
                 {
@@ -40343,51 +40322,49 @@
                     "title": "Medicare Part D Prescribers - by Provider : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-part-d-prescribers-by-provider-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/14d8e8a9-7e9b-4370-a044-bf97c46b4b44/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "drugs",
+                "health equity",
+                "medicare",
+                "medicare prescription drug",
+                "physicians & practitioners"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-provider",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-04",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-part-d-prescribers-methodology"
+            ],
+            "temporal": "2013-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Part D Prescribers - by Provider"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hkr7-mcee",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "arboviral diseases",
-                "babesiosis",
-                "nedss",
-                "netss",
-                "nndss",
-                "western equine encephalitis virus disease",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hkr7-mcee",
             "description": "NNDSS - Table 1D. Arboviral diseases, Western equine encephalitis virus disease to Babesiosis - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1D. Arboviral diseases, Western equine encephalitis virus disease to Babesiosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40410,90 +40387,93 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hkr7-mcee",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "arboviral diseases",
+                "babesiosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "western equine encephalitis virus disease",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hkr7-mcee",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table 1D. Arboviral diseases, Western equine encephalitis virus disease to Babesiosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/a9zs-s4k3",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_implauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "b07feac7-335b-5675-b4de-e483ad948e89",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_measure_backgroundAndMethods",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_backgroundAndMethods.csv",
-                    "description": "{\"dataset\": \"measure_backgroundAndMethods\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_backgroundAndMethods\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_backgroundAndMethods.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_backgroundAndMethods csv file"
                 }
             ],
+            "identifier": "b07feac7-335b-5675-b4de-e483ad948e89",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/a9zs-s4k3",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "implAuto_measure_backgroundAndMethods"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://profiles.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "history of medicine",
-                "images",
-                "physician",
-                "reference",
-                "scientist"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/sx5r-cjmt",
             "description": "This site celebrates twentieth-century leaders in biomedical research and public health. It makes the archival collections of prominent scientists, physicians, and others who have advanced the scientific enterprise available to the public through modern digital technology.",
-            "title": "Profiles in Science",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40502,46 +40482,42 @@
                     "title": "Search and Browse Profiles in Science"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/sx5r-cjmt",
+            "issued": "2016-08-04",
+            "keyword": [
+                "history of medicine",
+                "images",
+                "physician",
+                "reference",
+                "scientist"
+            ],
+            "landingPage": "https://profiles.nlm.nih.gov/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Historical Curated Content"
-            ]
+            ],
+            "title": "Profiles in Science"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/r8hr-3jkm",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/r8hr-3jkm",
             "description": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers'. NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
-            "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40564,93 +40540,94 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/r8hr-3jkm",
+            "issued": "2019-04-23",
+            "keyword": [
+                "2019",
+                "junin virus",
+                "lassa virus",
+                "lujo virus",
+                "nedss",
+                "netss",
+                "nndss",
+                "viral hemorrhagic fevers",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/r8hr-3jkm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2020-01-02",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://healthdata.gov/d/abdi-6q8y",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-07",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_prodauto",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DataConnect Support Team",
                 "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "fe0d958b-bf89-590c-bfcf-b3eb0175f4ff",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_files_allDownloads",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20230601_ETL_DEV/files_allDownloads.csv",
-                    "description": "{\"dataset\": \"files_allDownloads\", \"stage\": \"prodAuto\", \"update_id\": \"20230601_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"files_allDownloads\", \"stage\": \"prodAuto\", \"update_id\": \"20230601_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20230601_ETL_DEV/files_allDownloads.csv",
+                    "mediaType": "text/csv",
                     "title": "files_allDownloads csv file"
                 }
             ],
+            "identifier": "fe0d958b-bf89-590c-bfcf-b3eb0175f4ff",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/abdi-6q8y",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2023-06-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "prodAuto_files_allDownloads"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -40673,45 +40650,45 @@
                     "mediaType": "application/xml"
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-02-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://data.cdc.gov/d/29xv-7ajw",
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
-                "vancomycin-intermediate staphylococcus aureus",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/29xv-7ajw",
             "description": "NNDSS - TABLE 1KK. Vancomycin-intermediate Staphylococcus aureus to Varicella morbidity \u2013 2020.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1KK. Vancomycin-intermediate Staphylococcus aureus to Varicella morbidity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40734,21 +40711,49 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/29xv-7ajw",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "nedss",
+                "netss",
+                "nndss",
+                "vancomycin-intermediate staphylococcus aureus",
+                "vancomycin-resistant staphylococcus aureus",
+                "varicella morbidity",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/29xv-7ajw",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2021-01-07",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1KK. Vancomycin-intermediate Staphylococcus aureus to Varicella morbidity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.hrsa.gov/topics/health-workforce/nursing-workforce-survey-data",
             "bureauCode": [
                 "009:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michelle Washko",
+                "hasEmail": "mailto:mwashko@hrsa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://bhw.hrsa.gov/health-workforce-analysis/data",
+            "description": "<p>The National Sample Survey of Registered Nurses (NSSRN) Download makes data from the survey readily available to users in a one-stop download. The Survey has been conducted approximately every four years since 1977. For each survey year, HRSA has prepared two Public Use File databases in flat ASCII file format without delimiters. The 2008 data are also offerred in SAS and SPSS formats. Information likely to point to an individual in a sparsely-populated county has been withheld. General Public Use Files are State-based and provide information on nurses without identifying the County and Metropolitan Area in which they live or work.  County Public Use Files provide most, but not all, the same information on the nurse from the General Public Use File, and also identifies the County and Metropolitan Areas in which the nurses live or work. NSSRN data are to be used for research purposes only and may not be used in any manner to identify individual respondents.</p>",
+            "identifier": "a8f9b63d-e28e-4a36-8ec3-aeb0e7e1559d",
             "issued": "2012-05-30",
-            "temporal": "1978-01-01T00:00:00-05:00/2008-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "associate degree",
                 "bachelor s degree",
@@ -40776,63 +40781,35 @@
                 "nurses",
                 "racial background"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michelle Washko",
-                "hasEmail": "mailto:mwashko@hrsa.gov"
-            },
+            "landingPage": "https://data.hrsa.gov/topics/health-workforce/nursing-workforce-survey-data",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Health Resources and Services Administration"
             },
-            "identifier": "a8f9b63d-e28e-4a36-8ec3-aeb0e7e1559d",
-            "description": "<p>The National Sample Survey of Registered Nurses (NSSRN) Download makes data from the survey readily available to users in a one-stop download. The Survey has been conducted approximately every four years since 1977. For each survey year, HRSA has prepared two Public Use File databases in flat ASCII file format without delimiters. The 2008 data are also offerred in SAS and SPSS formats. Information likely to point to an individual in a sparsely-populated county has been withheld. General Public Use Files are State-based and provide information on nurses without identifying the County and Metropolitan Area in which they live or work.  County Public Use Files provide most, but not all, the same information on the nurse from the General Public Use File, and also identifies the County and Metropolitan Areas in which the nurses live or work. NSSRN data are to be used for research purposes only and may not be used in any manner to identify individual respondents.</p>",
-            "title": "Nursing Workforce Survey Data (National Sample Survey of Registered Nurses)",
-            "programCode": [
-                "009:014"
-            ],
-            "describedBy": "https://bhw.hrsa.gov/health-workforce-analysis/data",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1978-01-01T00:00:00-05:00/2008-12-31T00:00:00-05:00",
             "theme": [
                 "Community",
                 "Health"
-            ]
+            ],
+            "title": "Nursing Workforce Survey Data (National Sample Survey of Registered Nurses)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ei7y-3g6s",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-14",
-            "keyword": [
-                "2015",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "tb",
-                "tuberculosis",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ei7y-3g6s",
             "description": "NNDSS - Table IV. Tuberculosis - 2015.This Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States will exclude counts from US territories.  Footnote:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Min: Minimum.    Max: Maximum. * Case counts for reporting year 2014 and 2015 are provisional through the end of the quarter,  January 2, 2016. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf Data for TB are displayed quarterly.",
-            "title": "NNDSS - Table IV. Tuberculosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40855,20 +40832,56 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ei7y-3g6s",
+            "issued": "2016-01-14",
+            "keyword": [
+                "2015",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "tb",
+                "tuberculosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ei7y-3g6s",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-01-14",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table IV. Tuberculosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-us-dawn-ns-1994",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Drug Abuse Warning Network (DAWN) survey is designed to<br />\ncapture data on emergency department (ED) episodes that are induced by<br />\nor related to the use of an illicit, prescription, or over-the-counter<br />\ndrug. For purposes of this collection, a drug \"episode\" is an ED visit<br />\nthat was induced by or related to the use of an illegal drug or the<br />\nnonmedical use of a legal drug for patients aged six years and<br />\nolder. A drug \"mention\" refers to a substance that was mentioned<br />\nduring a drug-related ED episode. Because up to four drugs can be<br />\nreported for each drug abuse episode, there are more mentions than<br />\nepisodes in the data. Individual persons may also be included more<br />\nthan once in the data. Within each facility participating in DAWN, a<br />\ndesignated reporter, usually a member of the emergency department or<br />\nmedical records staff, was responsible for identifying drug-related<br />\nepisodes and recording and submitting data on each case. An episode<br />\nreport was submitted for each patient visiting a DAWN emergency<br />\ndepartment whose presenting problem(s) was/were related to their own<br />\ndrug use. DAWN produces estimates of drug-related emergency department<br />\nvisits for 50 specific drugs, drug categories, or combinations of<br />\ndrugs, including the following: acetaminophen, alcohol in combination<br />\nwith other drugs, alprazolam, amitriptyline, amphetamines, aspirin,<br />\ncocaine, codeine, diazepam, diphenhydramine, fluoxetine,<br />\nheroin/morphine, inhalants/solvents/aerosols, LSD, lorazepam,<br />\nmarijuana/hashish, methadone, methamphetamine, and PCP/PCP in<br />\ncombination with other drugs. The use of alcohol alone is not<br />\nreported. The route of administration and form of drug used (e.g.,<br />\npowder, tablet, liquid) are included for each drug. Data collected for<br />\nDAWN also include drug use motive and total drug mentions in the<br />\nepisode, as well as race, age, patient disposition, reason for ED<br />\nvisit, and day of the week, quarter, and year of episode.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Drug Abuse Warning Network US (DAWN-NS-1994) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-us-dawn-ns-1994-nid13570",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-us-dawn-ns-1994-nid13570"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-us-dawn-ns-1994-nid13570",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "demographic characteristics",
                 "drug abuse",
@@ -40881,66 +40894,29 @@
                 "hospitalization",
                 "substance abuse"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-us-dawn-ns-1994",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-us-dawn-ns-1994-nid13570",
-            "description": "<p>The Drug Abuse Warning Network (DAWN) survey is designed to<br />\ncapture data on emergency department (ED) episodes that are induced by<br />\nor related to the use of an illicit, prescription, or over-the-counter<br />\ndrug. For purposes of this collection, a drug \"episode\" is an ED visit<br />\nthat was induced by or related to the use of an illegal drug or the<br />\nnonmedical use of a legal drug for patients aged six years and<br />\nolder. A drug \"mention\" refers to a substance that was mentioned<br />\nduring a drug-related ED episode. Because up to four drugs can be<br />\nreported for each drug abuse episode, there are more mentions than<br />\nepisodes in the data. Individual persons may also be included more<br />\nthan once in the data. Within each facility participating in DAWN, a<br />\ndesignated reporter, usually a member of the emergency department or<br />\nmedical records staff, was responsible for identifying drug-related<br />\nepisodes and recording and submitting data on each case. An episode<br />\nreport was submitted for each patient visiting a DAWN emergency<br />\ndepartment whose presenting problem(s) was/were related to their own<br />\ndrug use. DAWN produces estimates of drug-related emergency department<br />\nvisits for 50 specific drugs, drug categories, or combinations of<br />\ndrugs, including the following: acetaminophen, alcohol in combination<br />\nwith other drugs, alprazolam, amitriptyline, amphetamines, aspirin,<br />\ncocaine, codeine, diazepam, diphenhydramine, fluoxetine,<br />\nheroin/morphine, inhalants/solvents/aerosols, LSD, lorazepam,<br />\nmarijuana/hashish, methadone, methamphetamine, and PCP/PCP in<br />\ncombination with other drugs. The use of alcohol alone is not<br />\nreported. The route of administration and form of drug used (e.g.,<br />\npowder, tablet, liquid) are included for each drug. Data collected for<br />\nDAWN also include drug use motive and total drug mentions in the<br />\nepisode, as well as race, age, patient disposition, reason for ED<br />\nvisit, and day of the week, quarter, and year of episode.This study has 1 Data Set.</p>",
-            "title": "Drug Abuse Warning Network US (DAWN-NS-1994)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-us-dawn-ns-1994-nid13570",
-                    "description": "Drug Abuse Warning Network US (DAWN-NS-1994) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-us-dawn-ns-1994-nid13570"
-                }
-            ]
+            "title": "Drug Abuse Warning Network US (DAWN-NS-1994)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -40963,54 +40939,47 @@
                     "mediaType": "application/xml"
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-02-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-05-20",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-08",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "excess deaths",
-                "hispanic origin",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "race",
-                "sex",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/jqg8-ycmh",
             "description": "Quarterly data on the number of deaths from all causes by state (of occurrence), sex, age group, and race/Hispanic origin group for the United States. Counts of deaths in more recent time periods can be compared with counts from earlier years (2015-2019) to determine if the number is higher than expected. Annual and cumulative counts (from Quarter 2, 2020 through the most recent quarter) are also shown.",
-            "title": "AH Quarterly Excess Deaths by State, Sex, Age, and Race",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41033,48 +41002,55 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/jqg8-ycmh",
+            "issued": "2021-05-20",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "excess deaths",
+                "hispanic origin",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "race",
+                "sex",
+                "state",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-09-08",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Quarterly Excess Deaths by State, Sex, Age, and Race"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/tj26-bdgd",
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
-                "tetanus",
-                "varicella",
-                "vibriosis",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/tj26-bdgd",
             "description": "NNDSS - Table II. Tetanus to Vibriosis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.  NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change.  For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.  Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table II to facilitate case count verification with reporting jurisdictions. \r\n\u00a7 Any species of the family Vibrionaceae, other than toxigenic Vibrio cholerae O1 or O139.",
-            "title": "NNDSS - Table II. Tetanus to Vibriosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41097,39 +41073,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/tj26-bdgd",
+            "issued": "2017-01-05",
+            "keyword": [
+                "2016",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "tetanus",
+                "varicella",
+                "vibriosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/tj26-bdgd",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2017-01-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Tetanus to Vibriosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/affy-6amt",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2017-07-28",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-03",
-            "keyword": [
-                "medicaid",
-                "utility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hiko Naito - TylerTech/Socrata employee",
                 "hasEmail": "mailto:no-reply@data.medicaid.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "0e203dba-396e-5f9f-a695-e702303dc713",
             "description": "Template Dataset: category_tiles",
-            "title": "category_tiles",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41138,36 +41122,36 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "0e203dba-396e-5f9f-a695-e702303dc713",
+            "issued": "2017-07-28",
+            "keyword": [
+                "medicaid",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/affy-6amt",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2018-10-03",
+            "programCode": [
+                "009:076"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "category_tiles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfIVD/Search.cfm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-01",
-            "keyword": [
-                "cdrh"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "abf2baea-8af9-4507-8d28-641ed80f2021",
             "description": "Searchable listing of Over-the-Counter tests (OTC) and collection kits that have been cleared or approved by the FDA",
-            "title": "IVD Home Use Lab Tests (Over The Counter) Tests",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41175,41 +41159,36 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "abf2baea-8af9-4507-8d28-641ed80f2021",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfIVD/Search.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-01",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "IVD Home Use Lab Tests (Over The Counter) Tests"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/fluvaxview/dashboard/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-09-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024, 2024-2025",
-            "modified": "2025-01-29",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rdng-ki53",
             "description": "\u2022 Weekly Influenza Vaccination Coverage and Comparison among adults 18 Years and Older by Jurisdiction\n\n \u2022 Weekly estimates of influenza vaccination coverage and intent for vaccination among adults are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/).",
-            "title": "Weekly Cumulative Influenza Vaccination Coverage and Comparison Between 2024\u201325 and 2023\u201324, Overall, by Jurisdiction, Among Adults 18 Years and Older",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41232,46 +41211,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/rdng-ki53",
+            "issued": "2024-09-26",
+            "keyword": [
+                "flu vaccination",
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "nis-flu",
+                "vsd"
+            ],
+            "landingPage": "https://www.cdc.gov/fluvaxview/dashboard/index.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2023-2024, 2024-2025",
             "theme": [
                 "Flu Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Influenza Vaccination Coverage and Comparison Between 2024\u201325 and 2023\u201324, Overall, by Jurisdiction, Among Adults 18 Years and Older"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/aftg-kade",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-14",
-            "keyword": [
-                "exchange puf",
-                "marketplace puf",
-                "plan attributes",
-                "py2024"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Center for Consumer Information and Insurance Oversight",
                 "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Center for Consumer Information and Insurance Oversight"
-            },
-            "identifier": "bf8da239-095e-4481-bf60-1f3a9615ce0e",
             "description": "The Plan Attributes PUF (Plan-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Plan-PUF contains plan variant-level data on maximum out of pocket payments, deductibles, health savings account (HSA) eligibility, and other plan attributes.",
-            "title": "Plan Attributes PUF - PY2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41279,52 +41261,50 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "bf8da239-095e-4481-bf60-1f3a9615ce0e",
+            "issued": "2024-08-06",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "plan attributes",
+                "py2024"
+            ],
+            "landingPage": "https://healthdata.gov/d/aftg-kade",
+            "modified": "2024-08-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Plan Attributes PUF - PY2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://medlineplus.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "consumer health",
-                "dataset",
-                "multilanguage",
-                "public health"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/nwss-k34b",
             "description": "MedlinePlus is the National Institutes of Health's Web site for patients and their families and friends. Produced by the National Library of Medicine, the world\u2019s largest medical library, it brings you information about diseases, conditions, and wellness issues in language you can understand. MedlinePlus offers reliable, up-to-date health information, anytime, anywhere, for free.",
-            "title": "MedlinePlus",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://medlineplus.gov/xml.html",
-                    "description": "MedlinePlus produces XML data sets that you are welcome to download and use.",
                     "@type": "dcat:Distribution",
+                    "description": "MedlinePlus produces XML data sets that you are welcome to download and use.",
+                    "downloadURL": "https://medlineplus.gov/xml.html",
+                    "mediaType": "text/html",
                     "title": "MedlinePlus XML Files"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://medlineplus.gov/connect/technical.html",
-                    "description": "MedlinePlus Connect helps patients and health care providers access consumer health information at the point of need in a health IT system. Patient portals, patient health record (PHR) systems, and electronic health record (EHR) systems can use MedlinePlus Connect to provide health information for patients, families, and healthcare providers using standard clinical vocabularies for diagnoses (problem codes), medications, and lab tests.",
                     "@type": "dcat:Distribution",
+                    "description": "MedlinePlus Connect helps patients and health care providers access consumer health information at the point of need in a health IT system. Patient portals, patient health record (PHR) systems, and electronic health record (EHR) systems can use MedlinePlus Connect to provide health information for patients, families, and healthcare providers using standard clinical vocabularies for diagnoses (problem codes), medications, and lab tests.",
+                    "downloadURL": "https://medlineplus.gov/connect/technical.html",
+                    "mediaType": "text/html",
                     "title": "MedlinePlus Connect API"
                 },
                 {
@@ -41334,69 +41314,63 @@
                     "title": "Search and Browse MedlinePlus"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://medlineplus.gov/about/developers/webservices/",
-                    "description": "MedlinePlus offers a search-based Web service that provides access to MedlinePlus health topic data in XML format. Using the Web service, software developers can build applications that utilize MedlinePlus health topic information. The service accepts keyword searches as requests and returns relevant health topics in ranked order. Keyword searches may be limited to specific fields. The service also returns health topic summaries, search result snippets, external links, and other associated data.",
                     "@type": "dcat:Distribution",
+                    "description": "MedlinePlus offers a search-based Web service that provides access to MedlinePlus health topic data in XML format. Using the Web service, software developers can build applications that utilize MedlinePlus health topic information. The service accepts keyword searches as requests and returns relevant health topics in ranked order. Keyword searches may be limited to specific fields. The service also returns health topic summaries, search result snippets, external links, and other associated data.",
+                    "downloadURL": "https://medlineplus.gov/about/developers/webservices/",
+                    "mediaType": "text/html",
                     "title": "API/Web Service"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://medlineplus.gov/about/developers/geneticsdatafilesapi/",
-                    "description": "MedlinePlus Genetics provides programmatic retrieval of selected data via API.",
                     "@type": "dcat:Distribution",
+                    "description": "MedlinePlus Genetics provides programmatic retrieval of selected data via API.",
+                    "downloadURL": "https://medlineplus.gov/about/developers/geneticsdatafilesapi/",
+                    "mediaType": "text/html",
                     "title": "MedlinePlus Genetics Data Files & API"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://medlineplus.gov/spanish/",
-                    "description": "MedlinePlus es un servicio informativo para pacientes, familiares y amigos.",
                     "@type": "dcat:Distribution",
+                    "description": "MedlinePlus es un servicio informativo para pacientes, familiares y amigos.",
+                    "downloadURL": "https://medlineplus.gov/spanish/",
+                    "mediaType": "text/html",
                     "title": "Medlineplus en Espa\u00f1ol"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/nwss-k34b",
+            "issued": "2016-08-04",
+            "keyword": [
+                "api",
+                "consumer health",
+                "dataset",
+                "multilanguage",
+                "public health"
+            ],
+            "landingPage": "https://medlineplus.gov/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Consumer Health"
-            ]
+            ],
+            "title": "MedlinePlus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/d2zt-4m8y",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-02-26",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-01",
-            "keyword": [
-                "2020",
-                "age <5 years",
-                "haemophilus influenzae",
-                "invasive disease",
-                "nedss",
-                "netss",
-                "nndss",
-                "non-b serotype",
-                "nontypeable",
-                "unknown serotype",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/d2zt-4m8y",
             "description": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, Age <5 years, Non-b serotype to Unknown serotype - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Notice: In Table 1n of the 2020 NNDSS weekly tables for weeks 1-53, data for Haemophilus influenzae in children < 5 years categorized as \"non-b serotype\" and \"unknown serotype\" were updated on 02/26/2021 to correct the data associated with these two serotype categories. The original version of the tables incorrectly displayed data for \"non-b serotype\" in the \"unknown serotype\" column and incorrectly displayed data for \"unknown serotype\" in the \"non-b serotype\" column. The data are corrected now.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, Age <5 years, Non-b serotype to Unknown serotype",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41419,53 +41393,61 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/d2zt-4m8y",
+            "issued": "2021-02-26",
+            "keyword": [
+                "2020",
+                "age <5 years",
+                "haemophilus influenzae",
+                "invasive disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-b serotype",
+                "nontypeable",
+                "unknown serotype",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/d2zt-4m8y",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2021-03-01",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, Age <5 years, Non-b serotype to Unknown serotype"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/pmc/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "dataset",
-                "literature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/wm3j-izuq",
             "description": "PubMed Central (PMC) is a free, digital archive of full text biomedical and life sciences journal literature.",
-            "title": "PubMed Central (PMC)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pmc/tools/oa-service/",
-                    "description": "The service allows users to discover downloadable resources from the PMC Open Access Subset by providing an API to allow discovery of resources related to articles.",
                     "@type": "dcat:Distribution",
+                    "description": "The service allows users to discover downloadable resources from the PMC Open Access Subset by providing an API to allow discovery of resources related to articles.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pmc/tools/oa-service/",
+                    "mediaType": "text/html",
                     "title": "PMC Open Access Web Service"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pmc/tools/oai/",
```

