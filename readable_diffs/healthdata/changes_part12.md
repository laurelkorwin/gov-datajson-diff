# Change History for healthdata.json (Part 12)

### Changes from 31606f9 to dd2190f (Part 11/11)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "landingPage": "https://healthdata.gov/d/x7rp-ggcs",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2023-03-20",
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
+            "title": "Managed Care Information for Medicaid and CHIP Beneficiaries by Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2012",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Behavioral Health Services (I-BHS), to analyze general treatment services trends, and to generate the online Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>, as well as the National Directory of Drug and Alcohol Abuse Treatment Programs.Data are collected on topics including facility operation, services offered (assessment, testing, transitional, ancillary, and pharmacotherapies), detoxification, primary focus (substance abuse, mental health, both, general health, and other), Opioid Treatment Programs and medications dispensed/prescribed, counseling and therapeutic approaches, standard operating procedures, special programs/groups offered, languages in which treatment is provided, type of treatment provided (hospital inpatient, residential, outpatient), number of clients (by service, total, and under age 18), number of beds, types of payment accepted, sliding fee scale, and facility accreditation and licensure/certification.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2012) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2012-nid13600",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2012-nid13600"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2012-nid13600",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -149483,80 +149496,30 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2012",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2012-nid13600",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Behavioral Health Services (I-BHS), to analyze general treatment services trends, and to generate the online Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>, as well as the National Directory of Drug and Alcohol Abuse Treatment Programs.Data are collected on topics including facility operation, services offered (assessment, testing, transitional, ancillary, and pharmacotherapies), detoxification, primary focus (substance abuse, mental health, both, general health, and other), Opioid Treatment Programs and medications dispensed/prescribed, counseling and therapeutic approaches, standard operating procedures, special programs/groups offered, languages in which treatment is provided, type of treatment provided (hospital inpatient, residential, outpatient), number of clients (by service, total, and under age 18), number of beds, types of payment accepted, sliding fee scale, and facility accreditation and licensure/certification.This study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2012)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2012-nid13600",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2012) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2012-nid13600"
-                }
-            ]
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2012)"
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
-            "identifier": "https://data.cdc.gov/api/views/pj7z-f3xf",
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2005/pj7z-f3xf",
             "description": "2005. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2005",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -149579,46 +149542,60 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2005/pj7z-f3xf",
+            "identifier": "https://data.cdc.gov/api/views/pj7z-f3xf",
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
+            "title": "CDC PRAMStat Data for 2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/efpc-rr7b",
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
-                "primary and secondary",
-                "spotted fever rickettsiosis",
-                "syphilis",
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
-            "identifier": "https://data.cdc.gov/api/views/efpc-rr7b",
             "description": "NNDSS - Table II. Spotted fever rickettsiosis to Syphilis, primary and secondary - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\r\n \r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum.\r\n \r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Spotted fever rickettsiosis to Syphilis, primary and secondary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -149641,69 +149618,75 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/efpc-rr7b",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "nedss",
+                "netss",
+                "nndss",
+                "primary and secondary",
+                "spotted fever rickettsiosis",
+                "syphilis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/efpc-rr7b",
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
+            "title": "NNDSS - Table II. Spotted fever rickettsiosis to Syphilis, primary and secondary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://eupathdb.org/eupathdb/",
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
-            "identifier": "ac3f7bb4-7d95-4da1-8b12-ccfb5f6b2da7",
+            "dataQuality": true,
             "description": "<p>EuPathDB Bioinformatics Resource Center for Biodefense and Emerging/Re-emerging Infectious Diseases is a portal for accessing genomic-scale datasets associated with the eukaryotic pathogens.</p>",
-            "title": "Eukaryotic Pathogen Database Resources (EuPathDB)",
+            "identifier": "ac3f7bb4-7d95-4da1-8b12-ccfb5f6b2da7",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://eupathdb.org/eupathdb/",
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
+            "title": "Eukaryotic Pathogen Database Resources (EuPathDB)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/i54f-wv8z",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-02-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-27",
-            "keyword": [
-                "glossary",
-                "methodology"
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
-            "identifier": "https://data.cdc.gov/api/views/i54f-wv8z",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "Youth Risk Behavior Surveillance System (YRBSS) Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -149711,35 +149694,39 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/i54f-wv8z",
+            "issued": "2015-02-05",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "https://data.cdc.gov/d/i54f-wv8z",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-07-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Survey Data"
-            ]
+            ],
+            "title": "Youth Risk Behavior Surveillance System (YRBSS) Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/chnh-3rdi",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-22",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Allergy and Clinical Immunology Branch (ACIB), Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/chnh-3rdi",
             "description": "Powered air purifying respirators (PAPRs) are a popular alternative to the use of filtering facepiece respirators by healthcare workers. Although PAPRs protect the wearer from aerosol particles, their ability to block infectious aerosol particles exhaled by the wearer from being released into the environment (called source control) is unclear.",
-            "title": "Efficacy of powered air-purifying respirators (PAPRs) for source control of simulated respiratory aerosols-dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -149747,35 +149734,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/chnh-3rdi",
+            "issued": "2024-11-22",
+            "landingPage": "https://data.cdc.gov/d/chnh-3rdi",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-22",
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
+            "title": "Efficacy of powered air-purifying respirators (PAPRs) for source control of simulated respiratory aerosols-dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4ems-va7k",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Personal Protective Technology Laboratory, Research Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4ems-va7k",
             "description": "Total inward leakage (TIL) is an estimate of the performance of a respirator, which is measured as the leakage of contaminants through the filter media and through the faceseal interface and exhalation valve of respiratory protective devices under laboratory conditions. Several test agents have been used to measure TIL in different countries. There is a lack of consensus on the most appropriate test method to measure TIL. The International Organization for Standardization (ISO) developed a standard (ISO, 2014) on the comparison of TIL measurement using sodium chloride (NaCl) and corn oil aerosols, and sulfur hexafluoride gas. A comparison of the TIL values between different methods will enable the selection of a relatively suitable method for measuring TIL. NIOSH\u2019s National Personal Protective Technology Laboratory (NPPTL) investigated the TIL values for respirators worn by test subjects exposed to NaCl and corn oil aerosols in two aerosol chambers side-by-side. Four air-purifying respirator categories, made",
-            "title": "Total Inward Leakage (TIL) for Respiratory Protective Devices",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -149783,38 +149770,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4ems-va7k",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/4ems-va7k",
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
+            "title": "Total Inward Leakage (TIL) for Respiratory Protective Devices"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Food/RecallsOutbreaksEmergencies/Recalls/default.htm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-06-06",
-            "keyword": [
-                "cfsan"
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
-            "identifier": "7268c3d7-607f-452c-a54c-2ac89d7b6b65",
             "description": "Food producers recall their products from the marketplace when the products are mislabeled or when the food may present a health hazard to consumers because the food is contaminated or has caused a foodborne illness outbreak.",
-            "title": "Recalls of Food and Dietary Supplements",
-            "programCode": [
-                "009:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -149822,44 +149806,38 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "7268c3d7-607f-452c-a54c-2ac89d7b6b65",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cfsan"
+            ],
+            "landingPage": "http://www.fda.gov/Food/RecallsOutbreaksEmergencies/Recalls/default.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-06-06",
+            "programCode": [
+                "009:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Recalls of Food and Dietary Supplements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-part-a-part-b-all-types-of-service",
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
-                "medicare",
-                "national",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/9400ca2c-b36a-4380-873d-380ea67a249d/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics -\u00a0Medicare Part A & Part B - All Types of Service tables provide use and payment data by type of coverage and type of service.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR SUMMARY AB 1. \u00a0Medicare Part A and Part B Summary: Utilization, Program Payments, and Cost Sharing for All Original Medicare Beneficiaries, by Type of Coverage and Type of Service, Yearly Trend\n\tMDCR SUMMARY AB 2. \u00a0Medicare Part A and Part B Summary: \u00a0Utilization, Program Payments, and Cost Sharing for Aged Original Medicare Beneficiaries, by Type of Coverage and Type of Service, Yearly Trend\n\tMDCR SUMMARY AB 3. \u00a0Medicare Part A and Part B Summary: \u00a0Utilization, Program Payments, and Cost Sharing for Disabled Original Medicare Beneficiaries by Type of Coverage and Type of Service, Yearly Trend\n\tMDCR SUMMARY AB 4. \u00a0Medicare Part A and Part B Summary: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Coverage, Demographic Characteristics, and Medicare-Medicaid Enrollment Status\n\tMDCR SUMMARY AB 5. \u00a0Medicare Part A and Part B Summary: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Coverage and by Area of Residence\n\tMDCR SUMMARY AB 6. \u00a0Medicare Part A and Part B Summary: \u00a0Utilization and Program Payments for Original Medicare Beneficiaries, by Type of Entitlement, Amount of Program Payments, Type of Coverage, and Type of Service",
-            "title": "CMS Program Statistics - Medicare Part A & Part B - All Types of Service",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -149916,65 +149894,92 @@
                     "title": "CMS Program Statistics - Medicare Part A & Part B - All Types of Service : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/9400ca2c-b36a-4380-873d-380ea67a249d/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "medicare",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-part-a-part-b-all-types-of-service",
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
+            "title": "CMS Program Statistics - Medicare Part A & Part B - All Types of Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datatools.ahrq.gov/hcup-fast-stats",
             "bureauCode": [
                 "009:33"
             ],
-            "issued": "2021-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
-                "fast stats"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HCUP Technical Support",
                 "hasEmail": "mailto:hcup@ahrq.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
-            },
-            "identifier": "2cb5e7e7-361b-45ef-b662-8938e421f3ef",
+            "describedBy": "https://datatools.ahrq.gov/hcup-fast-stats",
             "description": "Healthcare Cost and Utilization Project (HCUP) Fast Stats provides easy access to the latest HCUP-based statistics for health care information topics. HCUP Fast Stats uses visual statistical displays in stand-alone graphs, trend figures, or simple tables\nto convey complex information at a glance. Fast Stats is updated regularly for timely, topic-specific national and State-level statistics.\n\nFast Stats topics and graphics on hospital stays and emergency department visits, including information at the national, and state levels, trends over time, and selected priority topics such as:\n<li>State Trends in Hospital User by Payer\n<li>National Hospital Utilization and Costs\n<li>Hurricane Impact on Hospital Use\n<li>Opioids & Neonatal Abstinence Syndrome\n<li>Severe Maternal Morbidity",
-            "title": "HCUP Fast Stats",
-            "programCode": [
-                "009:074"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.hcup-us.ahrq.gov/faststats/landing.jsp",
-                    "description": "HCUP Fast Stats provides easy access to the latest HCUP-based statistics for health information topics. HCUP Fast Stats uses visual statistical displays in stand-alone graphs, trend figures, or simple tables to convey complex information at a glance. Information on the effect of Medicaid expansion on hospital use will be updated regularly (quarterly or annually, as newer data become available). \n",
                     "@type": "dcat:Distribution",
+                    "description": "HCUP Fast Stats provides easy access to the latest HCUP-based statistics for health information topics. HCUP Fast Stats uses visual statistical displays in stand-alone graphs, trend figures, or simple tables to convey complex information at a glance. Information on the effect of Medicaid expansion on hospital use will be updated regularly (quarterly or annually, as newer data become available). \n",
+                    "downloadURL": "http://www.hcup-us.ahrq.gov/faststats/landing.jsp",
+                    "mediaType": "text/html",
                     "title": "HCUP Fast Stats"
                 }
             ],
-            "describedBy": "https://datatools.ahrq.gov/hcup-fast-stats"
+            "identifier": "2cb5e7e7-361b-45ef-b662-8938e421f3ef",
+            "issued": "2021-02-13",
+            "keyword": [
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "fast stats"
+            ],
+            "landingPage": "https://datatools.ahrq.gov/hcup-fast-stats",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:074"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
+            },
+            "title": "HCUP Fast Stats"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.samhsa.gov/ebp-resource-center",
             "bureauCode": [
                 "009:30"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "SAMHSA Policy Lab",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Evidence-Based Practices Resource Center aims to provide communities, clinicians, policy-makers and others in the field with the information and tools they need to incorporate evidence-based practices into their communities or clinical settings. The Resource Center contains a collection of scientifically-based resources for a broad range of audiences, including Treatment Improvement Protocols, toolkits, resource guides, clinical practice guidelines, and other science-based resources.</p>",
+            "identifier": "74d54c36-1323-4969-b98a-a6a2974047e8",
             "issued": "2018-09-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "children",
                 "evidence",
@@ -149985,66 +149990,38 @@
                 "substance abuse",
                 "women"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "SAMHSA Policy Lab",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://www.samhsa.gov/ebp-resource-center",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:069"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "74d54c36-1323-4969-b98a-a6a2974047e8",
-            "description": "<p>The Evidence-Based Practices Resource Center aims to provide communities, clinicians, policy-makers and others in the field with the information and tools they need to incorporate evidence-based practices into their communities or clinical settings. The Resource Center contains a collection of scientifically-based resources for a broad range of audiences, including Treatment Improvement Protocols, toolkits, resource guides, clinical practice guidelines, and other science-based resources.</p>",
-            "title": "Evidence-Based Practices Resource Center",
-            "programCode": [
-                "009:069"
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "Community",
                 "Health"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Evidence-Based Practices Resource Center"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://www.cdc.gov/dhdsp/index.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
-            ],
-            "keyword": [
-                "cardiovascular disease",
-                "cerebrovascular disease",
-                "county",
-                "stroke"
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
-            "identifier": "https://data.cdc.gov/api/views/dhsy-4sea",
+            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Stroke-Mortality-Data-Among-US-Adults-35-by-State-/dhsy-4sea",
             "description": "2012 to 2014, 3-year average. Rates are age-standardized. County rates are spatially smoothed. The data can be viewed by gender and race/ethnicity. Data source: National Vital Statistics System. Additional data, maps, and methodology can be viewed on the Interactive Atlas of Heart Disease and Stroke http://www.cdc.gov/dhdsp/maps/atlas",
-            "title": "Stroke Mortality Data Among US Adults (35+) by State/Territory and County",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -150067,45 +150044,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Stroke-Mortality-Data-Among-US-Adults-35-by-State-/dhsy-4sea",
+            "identifier": "https://data.cdc.gov/api/views/dhsy-4sea",
+            "issued": "2023-07-18",
+            "keyword": [
+                "cardiovascular disease",
+                "cerebrovascular disease",
+                "county",
+                "stroke"
+            ],
+            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
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
+                "https://www.cdc.gov/dhdsp/index.htm",
+                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
+                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
+            ],
             "theme": [
                 "Heart Disease & Stroke Prevention"
-            ]
+            ],
+            "title": "Stroke Mortality Data Among US Adults (35+) by State/Territory and County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/m5zs-rf6r",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "west nile virus",
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
-            "identifier": "https://data.cdc.gov/api/views/m5zs-rf6r",
             "description": "NNDSS - Table II. West Nile virus disease - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.  The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Updated weekly from the Division of Vector-Borne Diseases, National Center for Emerging and Zoonotic Infectious Diseases (ArboNET Surveillance). Data for Jamestown Canyon virus, La Crosse virus, Chikungunya virus, Eastern equine encephalitis virus, Powassan virus, St. Louis virus, and Western equine encephalitis virus diseases are available in Table I. \r\n\r\n\u00b6 Not reportable in all states. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.",
-            "title": "NNDSS - Table II. West Nile virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -150128,51 +150106,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/m5zs-rf6r",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "west nile virus",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/m5zs-rf6r",
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
+            "title": "NNDSS - Table II. West Nile virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-10-11",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
-            "keyword": [
-                "behaviors",
-                "brfss",
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
-            "identifier": "https://data.cdc.gov/api/views/s85h-9xpy",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-ZCTA-Data-2020/qnzd-25i4",
             "description": "This dataset contains model-based ZIP Code Tabulation Area (ZCTA) level estimates for the PLACES 2021 release. PLACES is the expansion of the original 500 Cities Project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. The dataset includes estimates for 29 measures: 4 chronic disease-related health risk behaviors, 13 health outcomes, 3 health status, and 9 on using preventive services. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2010 population data, and American Community Survey (ACS) 2015\u20132019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS because the relevant questions are only asked every other year in the BRFSS. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, ZCTA Data 2021 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -150195,45 +150167,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-ZCTA-Data-2020/qnzd-25i4",
+            "identifier": "https://data.cdc.gov/api/views/s85h-9xpy",
+            "issued": "2022-10-11",
+            "keyword": [
+                "behaviors",
+                "brfss",
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
+            "title": "PLACES: Local Data for Better Health, ZCTA Data 2021 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/child-maltreatment-annual-reports",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-01-18",
-            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "child abuse",
-                "child maltreatment",
-                "children's health",
-                "child safety",
-                "population statistics",
-                "safety"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "admin",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Administration for Children and Families, Department of Health & Human Services"
-            },
-            "identifier": "eb78172c-71ad-465f-a941-5ec61cdd0e3d",
+            "dataQuality": true,
             "description": "<p>Child Maltreatment Reports contain data from the National Child Abuse and Neglect Data System that have been aggregated to the State level</p>",
-            "title": "Child Maltreatment Annual Reports",
-            "programCode": [
-                "184:016"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -150242,33 +150221,41 @@
                     "title": "HTML "
                 }
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "eb78172c-71ad-465f-a941-5ec61cdd0e3d",
+            "issued": "2013-01-18",
+            "keyword": [
+                "child abuse",
+                "child maltreatment",
+                "children's health",
+                "child safety",
+                "population statistics",
+                "safety"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/child-maltreatment-annual-reports",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "184:016"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families, Department of Health & Human Services"
+            },
+            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
+            "title": "Child Maltreatment Annual Reports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/r4kb-pc87",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-10",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-10",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Research Branch (RB), National Personal Protective Technology Laboratory (NPPTL)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/r4kb-pc87",
             "description": "Supplies of N95\u00ae filtering facepiece respirators (FFRs) can become depleted during widespread outbreaks of infectious respiratory illnesses. To supplement the national inventory of NIOSH Approved\u00ae N95 FFRs during times of extreme shortages, FFR reuse following decontamination is a possible strategy. Decontamination is a process to reduce the number of pathogens on used FFRs before reuse. An effective FFR decontamination technique should significantly reduce the pathogen burden, but not reduce a respirator\u2019s filtration performance or its ability to fit properly. Another consideration is that no hazardous chemical residue should be left on the FFR following the decontamination process.",
-            "title": "Assessment of Filtration Efficiency, Manikin Fit Performance, and Strap Performance for Decontaminated N95 Filtering Facepiece Respirators",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -150276,39 +150263,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/r4kb-pc87",
+            "issued": "2025-01-10",
+            "landingPage": "https://data.cdc.gov/d/r4kb-pc87",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-10",
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
+            "title": "Assessment of Filtration Efficiency, Manikin Fit Performance, and Strap Performance for Decontaminated N95 Filtering Facepiece Respirators"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/3bjr-fr6m",
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
-            "identifier": "https://data.cdc.gov/api/views/3bjr-fr6m",
             "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 8 - Denver",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -150331,46 +150314,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/3bjr-fr6m",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/3bjr-fr6m",
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
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 8 - Denver"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6jgb-zrsp",
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
-                "rmsf",
-                "spotted fever rickettsiosis",
-                "syphilis primary and secondary",
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
-            "identifier": "https://data.cdc.gov/api/views/6jgb-zrsp",
             "description": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.   NP:  Nationally notifiable but not published.  Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change.   For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.\r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table II to facilitate case count verification with reporting jurisdictions.\r\n\u00a7 Illnesses with similar clinical presentation that result from Spotted fever group rickettsia infections are reported as Spotted fever rickettsioses.   Rocky Mountain spotted fever (RMSF) caused by Rickettsia rickettsii, is the most common and well-known spotted fever.",
-            "title": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -150393,48 +150369,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6jgb-zrsp",
+            "issued": "2017-01-05",
+            "keyword": [
+                "2016",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "rmsf",
+                "spotted fever rickettsiosis",
+                "syphilis primary and secondary",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6jgb-zrsp",
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
+            "title": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/unsk-b7fc",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-02-24",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-12-13/2023-05-12",
-            "modified": "2023-05-12",
-            "references": [
-                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
-            ],
-            "keyword": [
-                "administration",
-                "age",
-                "coronavirus",
-                "covid-19",
-                "immunization",
-                "izdl",
-                "vaccination"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCIRD",
                 "hasEmail": "mailto:iisinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/unsk-b7fc",
             "description": "Overall US COVID-19 Vaccine\u00a0deliveries and\u00a0administration\u00a0data at national and jurisdiction level. Data represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.\u00a0",
-            "title": "COVID-19 Vaccinations in the United States,Jurisdiction",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -150457,57 +150432,59 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/unsk-b7fc",
+            "issued": "2023-02-24",
+            "keyword": [
+                "administration",
+                "age",
+                "coronavirus",
+                "covid-19",
+                "immunization",
+                "izdl",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/unsk-b7fc",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1D",
+            "modified": "2023-05-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
+            ],
+            "spatial": "US",
+            "temporal": "2020-12-13/2023-05-12",
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "COVID-19 Vaccinations in the United States,Jurisdiction"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/covid-19/covid-19-nursing-home-data",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2020-05-24/2025-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-16",
-            "references": [
-                "https://data.cms.gov/resources/covid-19-nursing-home-methodology"
-            ],
-            "keyword": [
-                "chronic conditions",
-                "co-morbidity",
-                "hospitals & facilities",
-                "medicaid",
-                "medicare",
-                "original medicare",
-                "skilled nursing"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "COVID-19 Nursing Home Data - CCSQ",
                 "hasEmail": "mailto:NH_COVID_Data@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/137f90cb-ac53-4b3d-8358-e65cf64e03d3/data-viewer",
-            "description": "Submitted data as of the week ending 01/05/2025.\n\nThe Nursing Home COVID-19 Public File includes data reported by nursing homes to the CDC\u2019s National Healthcare Safety Network (NHSN) Long Term Care Facility (LTCF) COVID-19 Module.\u00a0For resources and ways to explore and visualize the data, please see the links to the left, as well as the buttons at the top of the page.\n\nUp to Date with COVID-19 Vaccines\n\nOn January 1, 2024, the Centers for Disease Control (CDC) changed the way it collects data to calculate the percent of staff who are up to date with their COVID-19 vaccination. It may take facilities some time to adapt to the new methodology. As a result, the reported percent of staff who are up to date with their COVID-19 vaccination should be viewed with caution over the next few weeks. Contact facilities directly for more information on their vaccination levels.",
-            "title": "COVID-19 Nursing Home Data",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/COVID-19%20Nursing%20Home%20Data%20Dictionary_0.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "Submitted data as of the week ending 01/05/2025.\n\nThe Nursing Home COVID-19 Public File includes data reported by nursing homes to the CDC\u2019s National Healthcare Safety Network (NHSN) Long Term Care Facility (LTCF) COVID-19 Module.\u00a0For resources and ways to explore and visualize the data, please see the links to the left, as well as the buttons at the top of the page.\n\nUp to Date with COVID-19 Vaccines\n\nOn January 1, 2024, the Centers for Disease Control (CDC) changed the way it collects data to calculate the percent of staff who are up to date with their COVID-19 vaccination. It may take facilities some time to adapt to the new methodology. As a result, the reported percent of staff who are up to date with their COVID-19 vaccination should be viewed with caution over the next few weeks. Contact facilities directly for more information on their vaccination levels.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/137f90cb-ac53-4b3d-8358-e65cf64e03d3/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/137f90cb-ac53-4b3d-8358-e65cf64e03d3/data",
+                    "mediaType": "text/html",
                     "title": "COVID-19 Nursing Home Data : 2025-01-05"
                 },
                 {
@@ -151927,48 +151904,53 @@
                     "title": "COVID-19 Nursing Home Data : 2020-05-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/COVID-19%20Nursing%20Home%20Data%20Dictionary_0.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/137f90cb-ac53-4b3d-8358-e65cf64e03d3/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "chronic conditions",
+                "co-morbidity",
+                "hospitals & facilities",
+                "medicaid",
+                "medicare",
+                "original medicare",
+                "skilled nursing"
+            ],
+            "landingPage": "https://data.cms.gov/covid-19/covid-19-nursing-home-data",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://data.cms.gov/resources/covid-19-nursing-home-methodology"
+            ],
+            "temporal": "2020-05-24/2025-01-04",
             "theme": [
                 "Medicare",
                 "Medicaid"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "COVID-19 Nursing Home Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "references": [
-                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Standards/default.htm"
-            ],
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
-            "identifier": "4b318035-9f0e-4f7e-b4ff-c70fd57b4994",
             "description": "This database consists of those national and international standards recognized by FDA which manufacturers can declare conformity to and is part of the information the Center can use to make an appropriate decision regarding the clearance or approval of a submission. Information submitted on conformance with such standards will have a direct bearing on safety and effectiveness determinations made during the review of IDEs, HDEs, PMAs, and PDPs. Conformance with recognized consensus standards in and of itself, however, may not always be a sufficient basis for regulatory decisions.",
-            "title": "FDA Recognized Consensus Standards",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -151976,41 +151958,38 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "4b318035-9f0e-4f7e-b4ff-c70fd57b4994",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P3M"
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Standards/default.htm"
+            ],
+            "title": "FDA Recognized Consensus Standards"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/xf2e-rch5",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2025-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "keyword": [
-                "chip",
-                "maternal health",
-                "medicaid",
-                "preterm birth",
-                "severe maternal morbidity",
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
-            "identifier": "ee3b9534-0d19-4c1b-bf74-43f898d5de7c",
             "description": "This data set includes annual counts and rates of Medicaid- and Children\u2019s Health Insurance Program (CHIP)-covered live-birth deliveries that were preterm or with a severe maternal morbidity (SMM) condition within six weeks before or after delivery. Results are shown overall; by state; and by four subpopulation topics: age group, race and ethnicity, disability-related eligibility category, and type of SMM condition (SMM category only). \r\nThese results were generated using Transformed Medicaid Statistical Information System (T-MSIS) Analytic Files (TAF) Release 1 data and the Race/Ethnicity Imputation Companion File. This data set includes Medicaid and CHIP enrollees in all 50 states, the District of Columbia, Puerto Rico, and the U.S. Virgin Islands, who were ages 15 to 49 as of their delivery date, who were enrolled in Medicaid or CHIP at any point in the calendar year, and who had a live birth. Enrollees in Guam, American Samoa, the Northern Mariana Islands, and select states with TAF data quality issues are not included. Results shown for the race and ethnicity subpopulation topic exclude enrollees in the U.S. Virgin Islands. Results for SMM are calculated per 10,000 Medicaid- and CHIP-covered live births. Results for states with TAF data quality issues in the year have a value of \"Unusable data.\" Some rows in the data set have a value of \"DS,\" which indicates that data were suppressed according to the Centers for Medicare & Medicaid Services\u2019 Cell Suppression Policy for values between 1 and 10.\r\n\r\nThis data set is based on the brief: \"Prematurity and severe maternal morbidity among Medicaid- and CHIP-covered live births in 2021.\" Preterm birth is defined as a live birth that occurs before the 37th week of gestation. SMM deliveries are defined as live births with an SMM condition within six weeks before or after delivery (Identifying Severe Maternal Morbidity (SMM)). Enrollees are assigned to an age group subpopulation using age as of their delivery date. Enrollees are assigned to a race and ethnicity subpopulation using the state-reported race and ethnicity information in TAF when it is available and of good quality; if it is missing or unreliable, race and ethnicity is indirectly estimated using an enhanced version of Bayesian Improved Surname Geocoding (BISG) (Race and ethnicity of the national Medicaid and CHIP population in 2020). Enrollees are assigned to a disability category subpopulation using their latest reported eligibility group code and age in the year (Medicaid enrollees who qualify for benefits based on disability in 2020). Please refer to the full brief for additional context about the methodology and detailed findings. Future updates to this data set will include more recent data years as the TAF data become available.",
-            "title": "Prematurity and severe maternal morbidity among Medicaid- and CHIP-covered live births",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -152018,38 +151997,40 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "ee3b9534-0d19-4c1b-bf74-43f898d5de7c",
+            "issued": "2025-01-18",
+            "keyword": [
+                "chip",
+                "maternal health",
+                "medicaid",
+                "preterm birth",
+                "severe maternal morbidity",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/xf2e-rch5",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Prematurity and severe maternal morbidity among Medicaid- and CHIP-covered live births"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fdyw-m38t",
             "bureauCode": [
                 "009:032"
             ],
-            "issued": "2018-08-01",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-27",
-            "keyword": [
-                "environmental health",
-                "skin cancer",
-                "sunlight",
-                "total solar irradiance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Craig Kassinger",
                 "hasEmail": "mailto:nephtrackingsupport@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/fdyw-m38t",
             "description": "This dataset provides data at the county level for the contiguous United States. It includes daily Global Horizontal Irradiance (GHI) data from 1991-2012 provided by the Environmental Remote Sensing group at the Rollins School of Public Health at Emory University. Please refer to the metadata attachment for more information.\r\n\r\nThese data are used by the CDC's National Environmental Public Health Tracking Network to generate sunlight and ultraviolet (UV) measures. Learn more about sunlight and UV on the Tracking Network's website: https://ephtracking.cdc.gov/showUVLanding.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking. \r\n\r\nProblems or Questions? \r\nEmail trackingsupport@cdc.gov.",
-            "title": "Population-Weighted Global Horizontal Irradiance, 1991-2012",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -152072,38 +152053,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fdyw-m38t",
+            "issued": "2018-08-01",
+            "keyword": [
+                "environmental health",
+                "skin cancer",
+                "sunlight",
+                "total solar irradiance"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fdyw-m38t",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-11-27",
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
+            "title": "Population-Weighted Global Horizontal Irradiance, 1991-2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/xfrb-e2j6",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-25",
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
-            "identifier": "3a0999f8-2850-4fee-aefe-8ae6a22e56c0",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-17-to-2023-04-23",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -152112,50 +152097,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-17-to-2023-04-23"
                 }
             ],
+            "identifier": "3a0999f8-2850-4fee-aefe-8ae6a22e56c0",
+            "issued": "2023-04-26",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/xfrb-e2j6",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-04-25",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-17-to-2023-04-23"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual (R/P1Y)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-07-09",
-            "temporal": "1975/2020",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-16",
-            "keyword": [
-                "american hospital association",
-                "community hospitals",
-                "federal hospitals",
-                "health care use",
-                "health us",
-                "hospital",
-                "hospital admissions",
-                "hospital ownership",
-                "hospital size",
-                "length of hospital stay",
-                "outpatient surgery",
-                "outpatient visits",
-                "sdoh-access-to-health-care",
-                "sdoh-use-of-health-care"
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
-            "identifier": "https://data.cdc.gov/api/views/rear-2epk",
             "description": "Data on hospital admission, average length of stay, outpatient visits, and outpatient surgery in the United States, by type of ownership and size of hospital. Data are from Health, United States. SOURCE: American Hospital Association (AHA) Annual Survey of Hospitals, Hospital Statistics.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Hospital admission, average length of stay, outpatient visits, and outpatient surgery by type of ownership and size of hospital: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -152178,45 +152149,53 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rear-2epk",
+            "issued": "2024-07-09",
+            "keyword": [
+                "american hospital association",
+                "community hospitals",
+                "federal hospitals",
+                "health care use",
+                "health us",
+                "hospital",
+                "hospital admissions",
+                "hospital ownership",
+                "hospital size",
+                "length of hospital stay",
+                "outpatient surgery",
+                "outpatient visits",
+                "sdoh-access-to-health-care",
+                "sdoh-use-of-health-care"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual (R/P1Y)",
+            "modified": "2024-09-16",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "1975/2020",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "DQS Hospital admission, average length of stay, outpatient visits, and outpatient surgery by type of ownership and size of hospital: United States"
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
-            "identifier": "https://data.cdc.gov/api/views/ix4g-rt8v",
+            "describedBy": "https://data.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Se/ix4g-rt8v",
             "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Services and Profiles dataset provides an overview of clinic services, the clinic\u2019s contact information, location, the medical director\u2019s name, and summary statistics.",
-            "title": "2022 Final Assisted Reproductive Technology (ART) Services and Profiles",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -152239,101 +152218,109 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Se/ix4g-rt8v",
+            "identifier": "https://data.cdc.gov/api/views/ix4g-rt8v",
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
+            "title": "2022 Final Assisted Reproductive Technology (ART) Services and Profiles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/office-medicare-hearings-and-appeals-omha-receipts-fiscal-year",
             "bureauCode": [
                 "001:05"
             ],
-            "issued": "2014-02-04",
-            "temporal": "2005-01-01T00:00:00-05:00/2012-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "appeals",
-                "claims",
-                "medicare",
-                "omha",
-                "receipts"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kimberly Rubi",
                 "hasEmail": "mailto:kimberly.rubi@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Medicare Hearings and Appeals"
-            },
-            "identifier": "037bce72-0ee5-4ddc-9299-1cc37a6a847e",
+            "dataQuality": true,
             "description": "<p>This data set provides information about the appeals received by the Office of Medicare and Hearings for Fiscal Year 2005 - 2012.</p>",
-            "title": "Office of Medicare Hearings and Appeals (OMHA) - Receipts by Fiscal Year",
-            "programCode": [
-                "009:111"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "http://www.hhs.gov/omha/Data/Health%20Data%20Sets/receipts_2005_to_2006_csv.csv",
-                    "description": "This dataset is a compilation of appeals received in Fiscal Year 2005 and Fiscal Year 2006. \n",
                     "@type": "dcat:Distribution",
+                    "description": "This dataset is a compilation of appeals received in Fiscal Year 2005 and Fiscal Year 2006. \n",
+                    "downloadURL": "http://www.hhs.gov/omha/Data/Health%20Data%20Sets/receipts_2005_to_2006_csv.csv",
+                    "mediaType": "text/csv",
                     "title": "Office of Medicare Hearings and Appeals (OMHA) Receipts by Fiscal Year - 2005-2006"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "http://www.hhs.gov/omha/Data/Health%20Data%20Sets/receipts_2007_to_2008_csv.csv",
-                    "description": "This dataset is a compilation of appeals received in Fiscal Year 2007 and Fiscal Year 2008. \n",
                     "@type": "dcat:Distribution",
+                    "description": "This dataset is a compilation of appeals received in Fiscal Year 2007 and Fiscal Year 2008. \n",
+                    "downloadURL": "http://www.hhs.gov/omha/Data/Health%20Data%20Sets/receipts_2007_to_2008_csv.csv",
+                    "mediaType": "text/csv",
                     "title": "Office of Medicare Hearings and Appeals (OMHA) Receipts by Fiscal Year 2007-2008"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "http://www.hhs.gov/omha/Data/Health%20Data%20Sets/receipts_2009_to_2010_csv.csv",
-                    "description": "This dataset is a compilation of appeals received in Fiscal Year 2009 and Fiscal Year 2010. \n",
                     "@type": "dcat:Distribution",
+                    "description": "This dataset is a compilation of appeals received in Fiscal Year 2009 and Fiscal Year 2010. \n",
+                    "downloadURL": "http://www.hhs.gov/omha/Data/Health%20Data%20Sets/receipts_2009_to_2010_csv.csv",
+                    "mediaType": "text/csv",
                     "title": "Office of Medicare Hearings and Appeals (OMHA) Receipts by Fiscal Year 2009-2010"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "http://www.hhs.gov/omha/Data/Health%20Data%20Sets/receipts_2011_to_2012_csv.csv",
-                    "description": "This dataset is a compilation of appeals received in Fiscal Year 2011 and Fiscal Year 2012. \n",
                     "@type": "dcat:Distribution",
+                    "description": "This dataset is a compilation of appeals received in Fiscal Year 2011 and Fiscal Year 2012. \n",
+                    "downloadURL": "http://www.hhs.gov/omha/Data/Health%20Data%20Sets/receipts_2011_to_2012_csv.csv",
+                    "mediaType": "text/csv",
                     "title": "Office of Medicare Hearings and Appeals (OMHA) Receipts by Fiscal Year 2011-2012"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "037bce72-0ee5-4ddc-9299-1cc37a6a847e",
+            "issued": "2014-02-04",
+            "keyword": [
+                "appeals",
+                "claims",
+                "medicare",
+                "omha",
+                "receipts"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/office-medicare-hearings-and-appeals-omha-receipts-fiscal-year",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:111"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Medicare Hearings and Appeals"
+            },
+            "temporal": "2005-01-01T00:00:00-05:00/2012-01-01T00:00:00-05:00",
+            "title": "Office of Medicare Hearings and Appeals (OMHA) - Receipts by Fiscal Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/adnf-fpem",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/adnf-fpem",
             "description": "MicroRNAs are essential regulators of gene expression in humans and can control pathogenesis and host-virus interactions. Notably, the role of specific miRNAs during influenza virus infections are still ill-defined. The central goal of this study was to identify novel miRNAs and their target genes in response to influenza virus infections in airway epithelium. Human airway epithelial cells exposed to influenza virus induced several novel miRNAs that were identified using next generation sequencing (NGS) and their target genes by biochemical methods. NGS analysis predicted forty-two RNA sequences as possible miRNAs based on computational algorithms. Expression patterns of these putative miRNAs were further confirmed using RT-PCR in human bronchial epithelial cells (HBEpC) exposed to H1N1, H9N1(1P10) and H9N1 (1WF10) strains of influenza virus. A time course study showed significant downregulation of put-miR-34 in H1N1 and put-miR-35 in H9N1(1P10) infected cells, consistent with the NGS data. Additionally put-miR-34, and put-miR-35 showed a high fold enrichment in argonaute-immunoprecipitation compared to the controls, indicating their ability to form a complex with argonaute protein and RNA induced silencing complex (RISC), a typical mode of action found with miRNAs. Our earlier studies have shown that replication and survival of influenza virus is modulated by certain transcription factors, such as, NF-\u0138B. To identify the target(s) of these putative miRNAs, we screened 84 transcription factors that have a role in viral pathogenesis. Cells transfected with mimic of the put-miR-34 showed significant decrease in expression of Signal Transducers and Activators of Transcription 3 (STAT3), and the inhibitor of put-miR-34 showed significant increase in STAT3 expression and its phosphorylation. In addition, put-miR-34 had 76% homology to the untranslated region (UTR) of STAT3. NGS and PCR array data submitted to the Gene Ontology also predicted the role of transcription factors modulated by put-miR-34. Our data suggests that put-miR-34 could be a good target for the antiviral therapy as the hyperactivation or inactivation of STAT3 results in viral disease, as tightly regulated STAT3 function is central to health.",
-            "title": "Influenza virus induced novel miRNAs regulate the STAT pathway",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -152341,47 +152328,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/adnf-fpem",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/adnf-fpem",
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
+            "title": "Influenza virus induced novel miRNAs regulate the STAT pathway"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/provisional-drug-overdose.htm",
+            "accrualPeriodicity": "R/P6M",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-04-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-01-01/2024-06-30",
-            "modified": "2025-01-22",
-            "keyword": [
-                "deaths",
-                "drug overdose",
-                "hhs region",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
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
-            "identifier": "https://data.cdc.gov/api/views/8hzs-zshh",
             "description": "This data presents counts of provisional drug overdose deaths by selected drugs and U.S. Department of Health and Human Services (HHS) public health regions, based on provisional mortality data from the National Vital Statistics System. This data is limited to drug overdose deaths with an underlying cause of death assigned to International Statistical Classification of Diseases, 10th Revision (ICD-10) code numbers X40-X44 (unintentional), X60-X64 (suicide), X85 (homicide), or Y10-Y14 (undetermined intent). Specific drugs were identified using methods for searching literal text from death certificates. \n\nThe provisional data are based on a current flow of mortality data and include reported 12 month-ending provisional counts of drug overdose deaths by jurisdiction of occurrence and specified drug. Provisional drug overdose death counts presented on this page are for \u201c12-month ending periods,\u201d defined as the number of deaths occurring in the 12-month period ending in the month indicated. For example, the 12-month ending period in June 2022 would include deaths occurring from July 1, 2021, through June 30, 2022. Evaluation of trends over time should compare estimates from year to year (June 2021 and June 2022), rather than month to month, to avoid overlapping time periods. It is important to note that the data represent counts of deaths, and not mortality ratios or rates, which are the standard measure used to compare groups, and therefore should not be used to determine populations at disproportionate risk of drug overdose death.",
-            "title": "Provisional drug overdose death counts for specific drugs",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -152404,41 +152380,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/8hzs-zshh",
+            "issued": "2024-04-15",
+            "keyword": [
+                "deaths",
+                "drug overdose",
+                "hhs region",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "united states",
+                "vsrr"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/provisional-drug-overdose.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P6M",
+            "modified": "2025-01-22",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2019-01-01/2024-06-30",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional drug overdose death counts for specific drugs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-03-02",
-            "@type": "dcat:Dataset",
-            "temporal": "1999/2018",
-            "modified": "2023-09-08",
-            "keyword": [
-                "oral health"
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
-            "identifier": "https://data.cdc.gov/api/views/ggsw-596z",
             "description": "These data represent prevalence estimates of select oral health topics from the National Health and Nutrition Examination Survey (NHANES).",
-            "title": "NHANES Select Oral Health Prevalence Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -152461,47 +152445,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/ggsw-596z",
+            "issued": "2023-03-02",
+            "keyword": [
+                "oral health"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-09-08",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "U.S.",
+            "temporal": "1999/2018",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NHANES Select Oral Health Prevalence Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/xinu-a2t7",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-08-09",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-16",
-            "keyword": [
-                "py2023",
-                "qhp landscape instructions",
-                "sadp",
-                "shop",
-                "shop market dental"
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
-            "identifier": "253ecd82-4a43-4150-bd1e-3de6de1e2953",
             "description": "The Dental SHOP Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2023 Dental SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -152509,93 +152490,85 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "253ecd82-4a43-4150-bd1e-3de6de1e2953",
+            "issued": "2023-08-09",
+            "keyword": [
+                "py2023",
+                "qhp landscape instructions",
+                "sadp",
+                "shop",
+                "shop market dental"
+            ],
+            "landingPage": "https://healthdata.gov/d/xinu-a2t7",
+            "modified": "2023-08-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2023 Dental SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/xir8-6rfn",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-24",
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
-            "identifier": "142041ba-885c-517e-be08-53cc86a13f9a",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt version v2.10.6 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/version.csv",
-                    "description": "CoreSEt version v2.10.6 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt version v2.10.6 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/version.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt version v2.10.6 (coreset-etl-test)"
                 }
             ],
+            "identifier": "142041ba-885c-517e-be08-53cc86a13f9a",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/xir8-6rfn",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-24",
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
+            "title": "CoreSEt version v2.10.6 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-10-11",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
-            "keyword": [
-                "behaviors",
-                "brfss",
-                "census tract",
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
-            "identifier": "https://data.cdc.gov/api/views/373s-ayzu",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh",
             "description": "This dataset contains model-based census tract-level estimates for the PLACES 2021 release. PLACES is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. The dataset includes estimates for 29 measures: 4 chronic disease-related health risk behaviors, 13 health outcomes, 3 health status, and 9 on use of preventive services. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2010 population data, and American Community Survey (ACS) 2015\u2013019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS because the relevant questions are only asked every other year in the BRFSS. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, Census Tract Data 2021 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -152618,172 +152591,183 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh",
+            "identifier": "https://data.cdc.gov/api/views/373s-ayzu",
+            "issued": "2022-10-11",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "census tract",
+                "health",
+                "outcomes",
+                "places",
+                "prevalence",
+                "prevention",
+                "risk",
+                "status"
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
+            "title": "PLACES: Local Data for Better Health, Census Tract Data 2021 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/deaths.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-05-31",
-            "@type": "dcat:Dataset",
-            "temporal": "1950-2020",
-            "modified": "2023-03-27",
-            "references": [
-                "https://www.cdc.gov/nchs/nvss/deaths.htm"
-            ],
-            "keyword": [
-                "deaths",
-                "injury",
-                "mortality",
-                "research-data-center"
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
-            "identifier": "https://data.cdc.gov/api/views/kn6j-fsdu",
+            "describedBy": "All death certificate records issued by each state and independent jurisdiction each year",
             "description": "Data are based on information from all death certificates filed in the 50 states and the District of Columbia and processed by the National Center for Health Statistics (NCHS). Restricted data available through the Research Data Center include geographical indicators, exact date of birth and death of decedent, among others.",
-            "title": "Restricted mortality data from the National Vital Statistics System",
-            "isPartOf": "https://www.cdc.gov/nchs/nvss/deaths.htm",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "description": "Data are based on information from all death certificates filed in the 50 states and the District of Columbia and processed by the National Center for Health Statistics (NCHS). Restricted data available through the Research Data Center include geographical indicators, exact date of birth and death of decedent, among others.",
                     "@type": "dcat:Distribution",
+                    "description": "Data are based on information from all death certificates filed in the 50 states and the District of Columbia and processed by the National Center for Health Statistics (NCHS). Restricted data available through the Research Data Center include geographical indicators, exact date of birth and death of decedent, among others.",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
                     "title": "Restricted mortality data from the National Vital Statistics System"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "All death certificate records issued by each state and independent jurisdiction each year",
+            "identifier": "https://data.cdc.gov/api/views/kn6j-fsdu",
+            "isPartOf": "https://www.cdc.gov/nchs/nvss/deaths.htm",
+            "issued": "2022-05-31",
+            "keyword": [
+                "deaths",
+                "injury",
+                "mortality",
+                "research-data-center"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/deaths.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-03-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/nvss/deaths.htm"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "United States",
+            "temporal": "1950-2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Restricted mortality data from the National Vital Statistics System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/xj9d-qbai",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-07-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-11",
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
-            "identifier": "fb0920cb-7ed2-57ee-b138-1f7947ba6ac5",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard measure v2.11.9 (prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/measure.csv",
-                    "description": "Scorecard measure v2.11.9 (prod)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard measure v2.11.9 (prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard measure v2.11.9 (prod)"
                 }
             ],
+            "identifier": "fb0920cb-7ed2-57ee-b138-1f7947ba6ac5",
+            "issued": "2023-07-22",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/xj9d-qbai",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-12-11",
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
+            "title": "Scorecard measure v2.11.9 (prod)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.informatics.jax.org/expression.shtml",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "national-institutes-of-health-nih"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DI FRANCESCO, VALENTINA\u00a0",
                 "hasEmail": "mailto:valentina.difrancesco@nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "7d09c1b3-9752-44a4-bec2-42c273e927f9",
+            "dataQuality": true,
             "description": "<p>MGI is the international database resource for the laboratory mouse, providing integrated genetic, genomic, and biological data to facilitate the study of human health and disease.</p>",
-            "title": "Mouse Genome Informatics (MGI)",
+            "identifier": "7d09c1b3-9752-44a4-bec2-42c273e927f9",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.informatics.jax.org/expression.shtml",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:045"
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
+            "title": "Mouse Genome Informatics (MGI)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/xkj2-kr3z",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-09-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-27",
-            "keyword": [
-                "marketplace",
-                "transitions in coverage"
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
-            "identifier": "5636a78c-fe18-4229-aee1-e40fa910a8a0",
             "description": "Metrics from individual Marketplaces during the current reporting period. The report includes data for the states using HealthCare.gov.<br />\r\n<b>Sources:</b> HealthCare.gov application and policy data through October 6, 2024, HealthCare.gov inbound account transfer data through November 7, 2024, and T-MSIS Analytic Files (TAF) through July 2024 (TAF version 7.1). The table includes states that use HealthCare.gov.<br />\r\n<b>Notes: </b>\r\n<ol>\r\n<li>This table includes Marketplace consumers who submitted a HealthCare.gov application from March 6, 2023 - October 6, 2024 or who had an inbound account transfer from April 3, 2023 - November 7, 2024, who can be linked to an enrollment record in TAF that shows a last day of Medicaid or CHIP enrollment from March 31, 2023 - July 31, 2024. Beneficiaries with a leaving event may have continuous coverage through another coverage source, including Medicaid or CHIP coverage in another state. However, a beneficiary that lost Medicaid or CHIP coverage and regained coverage in the same state must have a gap of at least 31 days or a full calendar month.</li>\r\n<li>This table includes Medicaid or CHIP beneficiaries with full benefits in the month they left Medicaid or CHIP coverage.</li>\r\n<li>\u2018Account Transfer Consumers Whose Medicaid or CHIP Coverage was Terminated\u2019 are consumers 1) whose full benefit Medicaid or CHIP coverage was terminated and 2) were sent by a state Medicaid or CHIP agency via secure electronic file to the HealthCare.gov Marketplace in a process referred to as an inbound account transfer either 2 months before or 4 months after they left Medicaid or CHIP.  'Marketplace Consumers Not on Account Transfer Whose Medicaid or CHIP Coverage was Terminated' are consumers 1) who applied at the HealthCare.gov Marketplace and 2) were not sent by a state Medicaid or CHIP agency via an inbound account transfer either 2 months before or 4 months after they left Medicaid or CHIP.</li> \r\n<li>Marketplace consumers counts are based on the month Medicaid or CHIP coverage was terminated for a beneficiary. Counts include all recent Marketplace activity.</li>\r\n<li>HealthCare.gov data are organized by week. Reporting months start on the first Monday of the month and end on the first Sunday of the next month when the last day of the reporting month is not a Sunday. HealthCare.gov data are through Sunday, October 6.</li>\r\n<li>Data are preliminary and will be restated over time to reflect consumers most recent HealthCare.gov status. Data may change as states resubmit T-MSIS data or data quality issues are identified.</li>\r\n<li>See the data and methodology documentation for a full description of the data sources, measure definitions, and general data limitations.</li>\r\n</ol>\t\t\t\r\n<b>Data notes:</b> <ol>\r\n<li> The percentages for the 'Marketplace Consumers Not on Account Transfer whose Medicaid or CHIP Coverage was Terminated' data record group are marked as not available (NA) because the full population of consumers without an account transfer was not available for this report.</li>\r\n<li>Virginia operated a Federally Facilitated Exchange (FFE) on the HealthCare.gov platform during 2023.  In 2024, the state started operating a State Based Marketplace (SBM) platform. This table only includes data about 2023 applications and policies obtained through the HealthCare.gov Marketplace. Due to limited Marketplace activity on the HealthCare.gov platform in November 2023, data from November 2023 onward are excluded. The cumulative count and percentage for Virginia and the HealthCare.gov total reflect Virginia data from April 2023 through October 2023.</li>\t\r\n</ol>\t\t\t\t\r\nAPTC: Advance Premium Tax Credit; CHIP: Children's Health Insurance Program; QHP: Qualified Health Plan; NA: Not Available",
-            "title": "HealthCare.gov Transitions Marketplace Medicaid Unwinding Report",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -152796,88 +152780,87 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "5636a78c-fe18-4229-aee1-e40fa910a8a0",
+            "issued": "2023-09-29",
+            "keyword": [
+                "marketplace",
+                "transitions in coverage"
+            ],
+            "landingPage": "https://healthdata.gov/d/xkj2-kr3z",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-12-27",
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
+            "title": "HealthCare.gov Transitions Marketplace Medicaid Unwinding Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/xksj-pjwd",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-21",
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
-            "identifier": "3606023c-6e7f-53b5-b1ff-1757ca9da64e",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_files_stateSnapshot",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_stateSnapshot.csv",
-                    "description": "{\"dataset\": \"files_stateSnapshot\", \"stage\": \"featAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"files_stateSnapshot\", \"stage\": \"featAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_stateSnapshot.csv",
+                    "mediaType": "text/csv",
                     "title": "files_stateSnapshot csv file"
                 }
             ],
+            "identifier": "3606023c-6e7f-53b5-b1ff-1757ca9da64e",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/xksj-pjwd",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2022-09-21",
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
+            "title": "featAuto_files_stateSnapshot"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/books",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-02-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-08",
-            "keyword": [
-                "books",
-                "reference"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ken6-3jnj",
             "description": "A collection of online books and documents in life science and healthcare whose full text can be searched through the Entrez system. Bookshelf provides free online access to books and documents in life science and healthcare.",
-            "title": "Bookshelf",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -152886,47 +152869,40 @@
                     "title": "Bookshelf Homepage and Search"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ken6-3jnj",
+            "issued": "2022-02-08",
+            "keyword": [
+                "books",
+                "reference"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/books",
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
                 "Literature"
-            ]
+            ],
+            "title": "Bookshelf"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/dt66-w6m6",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-02-24",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-22/2023-05-10",
-            "modified": "2025-01-13",
-            "references": [
-                "https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn"
-            ],
-            "keyword": [
-                "case",
-                "community transmission",
-                "coronavirus",
-                "county",
-                "covid-19",
-                "laboratory"
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
-            "identifier": "https://data.cdc.gov/api/views/dt66-w6m6",
             "description": "Reporting of Aggregate Case and Death Count data was discontinued May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. Although these data will continue to be publicly available, this dataset will no longer be updated.\n\nWeekly COVID-19 Community Levels (CCLs) have been replaced with levels of COVID-19 hospital admission rates (low, medium, or high) which demonstrate <a href=\"https://www.cdc.gov/mmwr/volumes/72/wr/mm7219e1.htm\">>99% concordance</a> by county during February 2022\u2013March 2023. For more information on the latest COVID-19 status levels in your area and hospital admission rates, visit <a href=\"https://covid.cdc.gov/covid-data-tracker/#cases_new-admissions-rate-county\">United States COVID-19 Hospitalizations, Deaths, and Emergency Visits by Geographic Area.</a>\n\nThis archived public use dataset contains historical case and percent positivity data updated weekly for all available counties and jurisdictions. Each week, the dataset was refreshed to capture any historical updates. Please note, percent positivity data may be incomplete for the most recent time period.\n\nThis archived public use dataset contains weekly community transmission levels data for all available counties and jurisdictions since October 20, 2022. The dataset was appended to contain the most recent week's data as originally posted on COVID Data Tracker. Historical corrections are not made to these data if new case or testing information become available. A separate archived file is made available here (<a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn\">: Weekly COVID-19 County Level of Community Transmission Historical Changes</a>) if historically updated data are desired.\n\n<b>Related data</b> \nCDC provides the public with two active versions of COVID-19 county-level community transmission level data: this dataset with the levels as originally posted (<a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/dt66-w6m6\">Weekly Originally Posted dataset</a>), updated weekly with the most recent week\u2019s data since October 20, 2022, and a historical dataset with the county-level transmission data from January 22, 2020 (<a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn\">Weekly Historical Changes dataset</a>).  \n \n<b>Methods for calculating county level of community transmission indicator</b> \nThe County Level of Community Transmission indicator uses two metrics: (1) total new COVID-19 cases per 100,000 persons in the last 7 days and (2) percentage of positive SARS-CoV-2 diagnostic nucleic acid amplification tests (NAAT) in the last 7 days. For each of these metrics, CDC classifies transmission values as low, moderate, substantial, or high (below and\u202f<a href=\"https://www.cdc.gov/mmwr/volumes/70/wr/mm7030e2.htm?s_cid=mm7030e2_w#T1_down\">here</a>). If the values for each of these two metrics differ (e.g., one indicates moderate and the other low), then the higher of the two should be used for decision-making. \n \n<b>CDC core metrics of and thresholds for community transmission levels of SARS-CoV-2</b>\n<b>Total New Case Rate Metric:</b> \"New cases per 100,000 persons in the past 7 days\" is calculated by adding the number of new cases in the county (or other administrative level) in the last 7 days divided by the population in the county (or other administrative level) and multiplying by 100,000. \"New cases per 100,000 persons in the past 7 days\" is considered to have a transmission level of Low (0-9.99); Moderate (10.00-49.99); Substantial (50.00-99.99); and High (greater than or equal to 100.00). \n \n<b>Test Percent Positivity Metric:</b> \"Percentage of positive NAAT in the past 7 days\" is calculated by dividing the number of positive tests in the county (or other administrative level) during the last 7 days by the total number of tests conducted",
-            "title": "Weekly COVID-19 County Level of Community Transmission as Originally Posted - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -152949,23 +152925,73 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/dt66-w6m6",
+            "issued": "2023-02-24",
+            "keyword": [
+                "case",
+                "community transmission",
+                "coronavirus",
+                "county",
+                "covid-19",
+                "laboratory"
+            ],
+            "landingPage": "https://data.cdc.gov/d/dt66-w6m6",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "No longer updated (dataset archived)",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn"
+            ],
+            "spatial": "US",
+            "temporal": "2020-01-22/2023-05-10",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Weekly COVID-19 County Level of Community Transmission as Originally Posted - ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:healthus@cdc.gov"
+            },
+            "description": "Data on infant, neonatal, and postneonatal mortality rates in the United States, by detailed race and Hispanic origin of mother. Data are from Health, United States. Source: National Center for Health Statistics, National Vital Statistics System, Linked Birth/Infant Death Data Set.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/m7w3-utaq",
             "issued": "2024-08-05",
-            "temporal": "1983/2021",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-08",
             "keyword": [
                 "american indian and alaska native",
                 "asian",
@@ -152994,82 +153020,34 @@
                 "single race",
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
-            "identifier": "https://data.cdc.gov/api/views/m7w3-utaq",
-            "description": "Data on infant, neonatal, and postneonatal mortality rates in the United States, by detailed race and Hispanic origin of mother. Data are from Health, United States. Source: National Center for Health Statistics, National Vital Statistics System, Linked Birth/Infant Death Data Set.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Infant, neonatal, and postneonatal mortality rates, by detailed race and Hispanic origin of mother: United States",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-08",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "temporal": "1983/2021",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "DQS Infant, neonatal, and postneonatal mortality rates, by detailed race and Hispanic origin of mother: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/qsk4-8yy5",
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
-                "tularemia",
-                "vancomycin-intermediate staphylococcus aureus",
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
-            "identifier": "https://data.cdc.gov/api/views/qsk4-8yy5",
             "description": "NNDSS - TABLE 1JJ. Tularemia to  Vancomycin-intermediate Staphylococcus aureus - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1JJ. Tularemia to  Vancomycin-intermediate Staphylococcus aureus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153092,38 +153070,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qsk4-8yy5",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "tularemia",
+                "vancomycin-intermediate staphylococcus aureus",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/qsk4-8yy5",
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
+            "title": "NNDSS - TABLE 1JJ. Tularemia to  Vancomycin-intermediate Staphylococcus aureus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/g653-rqe2",
+            "accrualPeriodicity": "Daily",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-22",
-            "keyword": [
-                "wastewater"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Wastewater Surveillance System",
                 "hasEmail": "mailto:nwss@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/g653-rqe2",
             "description": "This dataset provides a complete time history of SARS-CoV-2 concentrations in wastewater for each sampling location.",
-            "title": "NWSS Public SARS-CoV-2 Concentration in Wastewater Data",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153146,76 +153131,74 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/g653-rqe2",
+            "issued": "2024-06-25",
+            "keyword": [
+                "wastewater"
+            ],
+            "landingPage": "https://data.cdc.gov/d/g653-rqe2",
+            "language": [
+                "English"
+            ],
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Daily",
+            "modified": "2025-01-22",
+            "programCode": [
+                "009:028"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Public Health Surveillance"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NWSS Public SARS-CoV-2 Concentration in Wastewater Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.niagads.org/",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-07-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "national-institutes-of-health-nih"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Miller, Marilyn",
                 "hasEmail": "mailto:millerm@nia.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "a08ab7e7-d870-4d8a-aaa1-7ebe7ca7a0ce",
+            "dataQuality": true,
             "description": "<p>The National Institute on Aging Genetics of Alzheimer's Disease Data Storage Site (NIAGADS) is a national genetics data repository facilitating access to genotypic and phenotypic data for Alzheimer's disease (AD). Data include GWAS, whole genome (WGS) and whole exome (WES), expression, RNA Seq, and CHIP Seq analyses. Data for the Alzheimer\u2019s Disease Sequencing Project (ADSP) are available through a partnership with dbGaP (ADSP at dbGaP). Results are integrated and annotated in the searchable genomics database that also provides access to a variety of software packages, analytic pipelines, online resources, and web-based tools to facilitate analysis and interpretation of large-scale genomic data. Data are available as defined by the NIA Genomics of Alzheimer\u2019s Disease Sharing Policy and the NIH Genomics Data Sharing Policy. Investigators return secondary analysis data to the database in keeping with the NIAGADS Data Distribution Agreement.</p>",
-            "title": "The National Institute on Aging Genetics of Alzheimer\u2019s Disease Data Storage Site (NIAGADS)\u00a0",
+            "identifier": "a08ab7e7-d870-4d8a-aaa1-7ebe7ca7a0ce",
+            "issued": "2016-07-15",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "https://www.niagads.org/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
             "programCode": [
                 "009:044"
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
+            "title": "The National Institute on Aging Genetics of Alzheimer\u2019s Disease Data Storage Site (NIAGADS)\u00a0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-04-01",
-            "keyword": [
-                "cdrh",
-                "regulations"
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
-            "identifier": "f1b5d989-b06e-46b6-a992-4b753912656b",
             "description": "This database contains the most recent revision from the Government Printing Office (GPO) of the Code of Federal Regulations (CFR) Title 21 - Food and Drugs.",
-            "title": "Code of Federal Regulations Title 21",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153223,36 +153206,37 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "f1b5d989-b06e-46b6-a992-4b753912656b",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh",
+                "regulations"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-04-01",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Code of Federal Regulations Title 21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-03-02",
-            "@type": "dcat:Dataset",
-            "temporal": "1999/2018",
-            "modified": "2023-09-08",
-            "keyword": [
-                "chronic conditions"
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
-            "identifier": "https://data.cdc.gov/api/views/i667-sjhg",
             "description": "These data represent prevalence estimates of select chronic conditions from the National Health and Nutrition Examination Survey (NHANES).",
-            "title": "NHANES Select Chronic Conditions Prevalence Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153275,40 +153259,43 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/i667-sjhg",
+            "issued": "2023-03-02",
+            "keyword": [
+                "chronic conditions"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-09-08",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "U.S.",
+            "temporal": "1999/2018",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NHANES Select Chronic Conditions Prevalence Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5y75-rs75",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Personal Protective Technology Laboratory, Research Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5y75-rs75",
             "description": "Filtering facepiece respirators (FFRs) and elastomeric half-mask respirators (EHRs) are commonly used by workers for protection against potentially hazardous particles, including engineered nanoparticles (i.e., particles measuring less than 100 nanometers (nm). The purpose of this study was to evaluate the performance of these types of respirators against 10-400 nm particles using human subjects exposed to NaCl aerosols under simulated workplace activities. Simulated workplace protection factors (SWPFs) were measured for eight combinations of respirator models (2 N95 FFRs, 2 P100 FFRs, 2 N95 EHRs, and 2 P100 EHRs) worn by 25 healthy test subjects (13 females and 12 males) with varying face sizes. Before beginning a SWPF test for a given respirator model, each subject had to pass a quantitative fit test. Each SWPF test was performed using a protocol of six exercises for three minutes each: (i) normal breathing, (ii) deep breathing, (iii) moving head side to side, (iv) moving head up and down, (v) bending at th",
-            "title": "Respirator Performance against Nanoparticles under Simulated Workplace Activities Data",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153316,41 +153303,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5y75-rs75",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/5y75-rs75",
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
+            "title": "Respirator Performance against Nanoparticles under Simulated Workplace Activities Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/mental-health.htm",
+            "accrualPeriodicity": "R/P2W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-05-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-08-19/2024-09-16",
-            "modified": "2024-10-04",
-            "keyword": [
-                "anxiety",
-                "covid-19",
-                "depression"
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
-            "identifier": "https://data.cdc.gov/api/views/8pt5-q6wp",
             "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, gender, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions,",
-            "title": "Indicators of Anxiety or Depression Based on Reported Frequency of Symptoms During Last 7 Days",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153373,44 +153355,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/8pt5-q6wp",
+            "issued": "2020-05-20",
+            "keyword": [
+                "anxiety",
+                "covid-19",
+                "depression"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/mental-health.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P2W",
+            "modified": "2024-10-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
+            "temporal": "2020-08-19/2024-09-16",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Indicators of Anxiety or Depression Based on Reported Frequency of Symptoms During Last 7 Days"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/national-foster-care-and-adoption-directory",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-05-30",
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
-            "identifier": "a2f65cfc-17bf-4314-85c4-883a53034b0d",
+            "dataQuality": true,
             "description": "<p>The National Foster Care &amp; Adoption Directory (formerly the National Adoption Directory) offers adoption and foster care resources by State.</p>",
-            "title": "National Foster Care and Adoption Directory",
-            "programCode": [
-                "009:103"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153419,37 +153403,36 @@
                     "title": "Query Tool "
                 }
             ],
+            "identifier": "a2f65cfc-17bf-4314-85c4-883a53034b0d",
+            "issued": "2012-05-30",
+            "keyword": [
+                "children's health",
+                "department-of-health-human-services"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-foster-care-and-adoption-directory",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "dataQuality": true
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:103"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
+            },
+            "title": "National Foster Care and Adoption Directory"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Drugs/DrugSafety/DrugShortages/ucm050794.htm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2025-01-29",
-            "@type": "dcat:Dataset",
-            "modified": "2013-09-26",
-            "keyword": [
-                "cder",
-                "discontinued drugs"
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
-            "identifier": "6e72c239-0510-49f4-8404-d3d7d50351ec",
             "description": "Companies are required under Section 506C of the Federal Food, Drug, and Cosmetic Act (FD&C Act) (as amended by the Food and Drug Administration Safety and Innovation Act) to notify FDA of a permanent discontinuance of certain drug products, six months in advance, or if that is not possible, as soon as practicable. These drugs include those that are life-supporting, life-sustaining or for use in the prevention or treatment of a debilitating disease or condition, including any such drug used in emergency medical care or during surgery). The discontinuations provided below reflect information received from manufacturers, and are for informational purposes only.",
-            "title": "Drugs to be Discontinued",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153457,123 +153440,123 @@
                     "mediaType": "application/unknown"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "6e72c239-0510-49f4-8404-d3d7d50351ec",
+            "issued": "2025-01-29",
+            "keyword": [
+                "cder",
+                "discontinued drugs"
+            ],
+            "landingPage": "http://www.fda.gov/Drugs/DrugSafety/DrugShortages/ucm050794.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-09-26",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Drugs to be Discontinued"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/xr2u-sbqf",
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
-            "identifier": "9701e19c-7e6f-51f4-95cd-4ce1d568e93f",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_measure_compare_download",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_compare_download.csv",
-                    "description": "{\"dataset\": \"measure_compare_download\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_compare_download\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_compare_download.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_compare_download csv file"
                 }
             ],
+            "identifier": "9701e19c-7e6f-51f4-95cd-4ce1d568e93f",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/xr2u-sbqf",
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
+            "title": "implAuto_measure_compare_download"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/xr6g-9z88",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2015-02-03",
-            "keyword": [
-                "constituents",
-                "harmful",
-                "hphc"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Danny Hsu",
                 "hasEmail": "mailto:danny.hsu@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "96E5B59F-286A-4127-A6E1-82EBA4981EFF",
             "description": "The FDA shall publish in a format that is understandable and not misleading to a lay person, and place on public display, a list of 93 harmful and potentially harmful constituents in each tobacco product and smoke established under section 904(e) of the TCA.  CTP has determined the best means to display the data is web-based on FDA.GOV.  The HPHC back-end database and template for industry will be created in a future release of eSubmissions.  The scope of this project is to: Phase 1 (Current POP): 1) build a website to support the display of the HPHC constituents, 2) allow the user to access educational information about the health effects of the chemicals; Phase 2 (next POP):  1) allow users of the website to perform a search by brand and sub-brand, 2) display a report on the HPHCs contained in that tobacco product, and 3) create an admin module to allow for an import of HPHC data via an Excel spreadsheet and to update the list of constituents.",
-            "title": "Harmful and Potentially Harmful Constituents",
-            "programCode": [
-                "009:007"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "description": "Website is still under development, not yet published to the public. Pre-Production L is: http://accessdata-preprod.fda.gov/scripts/hphc/",
                     "downloadURL": "http://www.fda.gov/TobaccoProducts/GuidanceComplianceRegulatoryInformation/ucm297786.htm",
-                    "mediaType": "text/html",
-                    "description": "Website is still under development, not yet published to the public. Pre-Production L is: http://accessdata-preprod.fda.gov/scripts/hphc/"
+                    "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "96E5B59F-286A-4127-A6E1-82EBA4981EFF",
+            "issued": "2021-02-25",
+            "keyword": [
+                "constituents",
+                "harmful",
+                "hphc"
+            ],
+            "landingPage": "https://healthdata.gov/d/xr6g-9z88",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2015-02-03",
+            "programCode": [
+                "009:007"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Harmful and Potentially Harmful Constituents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://ncbi.github.io/cxx-toolkit/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "computational biology",
-                "software"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/x3vz-qq3q",
             "description": "Provides an overview of the C++ language with a focus on its use in accessing resources of the National Center for Biotechnology Information at the National Library of Medicine, National Institutes of Health.",
-            "title": "NCBI C++ Toolkit Book",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153582,47 +153565,40 @@
                     "title": "The NCBI C++ Toolkit Book"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/x3vz-qq3q",
+            "issued": "2021-08-26",
+            "keyword": [
+                "computational biology",
+                "software"
+            ],
+            "landingPage": "https://ncbi.github.io/cxx-toolkit/",
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
+            "title": "NCBI C++ Toolkit Book"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-09",
-            "references": [
-                "https://www.cdc.gov/dhdsp/index.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
-            ],
-            "keyword": [
-                "cardiovascular disease",
-                "coronary heart disease",
-                "diseases of the heart",
-                "mortality",
-                "stroke"
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
-            "identifier": "https://data.cdc.gov/api/views/kztq-p2jf",
+            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/National-Vital-Statistics-System-NVSS-National-Car/kztq-p2jf",
             "description": "2000\u20132020. NVSS is a secure, web-based data management system that collects and disseminates the Nation's official vital statistics. Indicators from this data source have been computed by personnel in CDC's Division for Heart Disease and Stroke Prevention (DHDSP). This was one of the datasets provided by the National Cardiovascular Disease Surveillance System and presented on DHDSP\u2019s Data, Trends, and Maps online tool. This tool was retired in April of 2024 and this dataset will not be updated. Contact dhdsprequests@cdc.gov if you need assistance with data previously included in this dataset. The data are organized by location (national and state) and indicator; NVSS mortality data include CVDs (e.g., heart failure). The data can be viewed by temporal trends and stratified by age group, sex, and race/ethnicity.",
-            "title": "National Vital Statistics System (NVSS) - National Cardiovascular Disease Surveillance Data",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153645,43 +153621,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/National-Vital-Statistics-System-NVSS-National-Car/kztq-p2jf",
+            "identifier": "https://data.cdc.gov/api/views/kztq-p2jf",
+            "issued": "2023-07-18",
+            "keyword": [
+                "cardiovascular disease",
+                "coronary heart disease",
+                "diseases of the heart",
+                "mortality",
+                "stroke"
+            ],
+            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-04-09",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/dhdsp/index.htm",
+                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
+                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
+            ],
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "National Vital Statistics System (NVSS) - National Cardiovascular Disease Surveillance Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nlm.nih.gov/research/umls/Snomed/nursing_terminology_resources.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-03-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "health data standards",
-                "nursing",
-                "population groups",
-                "reference",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/3ymh-phhi",
             "description": "A nursing terminologies resource for systems development. Describes the role of SNOMED CT and Laboratory Observation Identifiers Names and Codes (LOINC) in implementing Meaningful Use in the U.S., specifically for the nursing and care domain.",
-            "title": "Nursing Resources for Standards and Interoperability",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153690,44 +153670,42 @@
                     "title": "Nursing Resources for Standards and Interoperability"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/3ymh-phhi",
+            "issued": "2022-03-01",
+            "keyword": [
+                "health data standards",
+                "nursing",
+                "population groups",
+                "reference",
+                "terminologies"
+            ],
+            "landingPage": "https://www.nlm.nih.gov/research/umls/Snomed/nursing_terminology_resources.html",
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
                 "Terminology"
-            ]
+            ],
+            "title": "Nursing Resources for Standards and Interoperability"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kxvg-q6s7",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/kxvg-q6s7",
             "description": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153750,49 +153728,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kxvg-q6s7",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "novel influenza a virus infections",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/kxvg-q6s7",
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
+            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -153815,40 +153789,51 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pmamemos.cfm",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
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
-            "identifier": "8dabbf7e-0e4a-4e1c-a0d2-982d97398a10",
             "description": "A 180-day supplement is a request for a significant change in components, materials, design, specification, software, color additive, and labeling to an approved premarket application or premarket report. As a pilot program under the CDRH Transparency Initiative, FDA has begun releasing some summary review memos for 180-day PMA supplements relating to design changes.",
-            "title": "Premarket Approval (PMA) Summary Review Memos for 180-Day Design Changes",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153856,39 +153841,36 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "8dabbf7e-0e4a-4e1c-a0d2-982d97398a10",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pmamemos.cfm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1W"
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Premarket Approval (PMA) Summary Review Memos for 180-Day Design Changes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/xu6x-dfcx",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-14",
-            "keyword": [
-                "business rules",
-                "exchange puf",
-                "marketplace puf",
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
-            "identifier": "0063b2e0-f674-4c04-91a4-380d71f613ee",
             "description": "The Business Rules PUF (BR-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The BR-PUF contains plan-level data on rating business rules, such as maximum age for a dependent and allowed dependent relationships.",
-            "title": "Business Rules PUF - PY2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153896,44 +153878,40 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "0063b2e0-f674-4c04-91a4-380d71f613ee",
+            "issued": "2024-08-06",
+            "keyword": [
+                "business rules",
+                "exchange puf",
+                "marketplace puf",
+                "py2024"
+            ],
+            "landingPage": "https://healthdata.gov/d/xu6x-dfcx",
+            "modified": "2024-08-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Business Rules PUF - PY2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-part-d",
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
-                "medicare",
-                "medicare prescription drug",
-                "national",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/f28a5c57-b4b2-4a3b-8c0e-18ab67c4d59b/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics -\u00a0Medicare Part D tables provide use and Part D drug costs by type of Part D plan (stand-alone prescription drug plan and Medicare Advantage prescription drug plan).\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR UTLZN D 1. \u00a0Medicare Part D Utilization: \u00a0Average Annual Prescription Drug Fills\u00a0by Type of Plan, Low Income Subsidy (LIS) Eligibility, and Generic Dispensing Rate,\u00a0Yearly Trend\n\tMDCR UTLZN D 2. \u00a0Medicare Part D Utilization: \u00a0Average Annual Gross Drug Costs Per Part D Enrollee, by Type of Plan, Low Income Subsidy (LIS) Eligibility, and Brand/Generic Drug Classification, Yearly Trend\n\tMDCR UTLZN D 3. \u00a0Medicare Part D Utilization: \u00a0Average Annual Gross Drug Costs Per Part D Enrollee, by Type of Plan, Low Income Subsidy (LIS) Eligibility, and Brand/Generic Drug Classification, Yearly Trend\n\tMDCR UTLZN D 4. \u00a0Medicare Part D Utilization: \u00a0Average Annual Prescription Drug Fills\u00a0and Average Annual Gross Drug Cost Per Part D Enrollee, by Type of Plan and Demographic Characteristics\n\tMDCR UTLZN D 5. \u00a0Medicare Part D Utilization: \u00a0Average Annual Prescription Drug Fills\u00a0and Average Annual Gross Drug Cost Per Part D Utilizer, by Type of Plan and Demographic Characteristics\n\tMDCR UTLZN D 6. \u00a0Medicare Part D Utilization: \u00a0Average Annual Prescription Drug Fills\u00a0and Average Annual Gross Drug Cost Per Part D Enrollee, by Type of Plan, by Area of Residence\n\tMDCR UTLZN D 7. \u00a0Medicare Part D Utilization: \u00a0Average Annual Prescription Drug Fills\u00a0and Average Annual Gross Drug Cost Per Part D Utilizer, by Type of Plan, by Area of Residence\n\tMDCR UTLZN D 8. \u00a0Medicare Part D Utilization: \u00a0Number of Part D Utilizers and Average Annual Prescription Drug Fills\u00a0by Type of Part D Plan, Low Income Subsidy (LIS) Eligibility, and Part D Coverage Phase, Yearly Trend\n\tMDCR UTLZN D 9. \u00a0Medicare Part D Utilization:\u00a0\u00a0Number of Part D Utilizers and Drug Costs by Type of Part D Plan, Low Income Subsidy (LIS) Eligibility, and Part D Coverage Phase, Yearly Trend\n\tMDCR UTLZN D 10. \u00a0Medicare Part D Utilization: \u00a0Number of Part D Utilizers, Average Annual Prescription Drug Events (Fills)\u00a0and Average Annual Gross Drug Cost Per Part D Utilizer, by Part D Coverage Phase and Demographic Characteristics\n\tMDCR UTLZN D 11. \u00a0Medicare Part D Utilization: \u00a0Number of Part D Utilizers, Average Annual Prescription Drug Fills\u00a0and Average Annual Gross Drug Cost Per Part D Utilizer, by Part D Coverage Phase and Area of Residence",
-            "title": "CMS Program Statistics - Medicare Part D",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153990,48 +153968,50 @@
                     "title": "CMS Program Statistics - Medicare Part D : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/f28a5c57-b4b2-4a3b-8c0e-18ab67c4d59b/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "medicare",
+                "medicare prescription drug",
+                "national",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-part-d",
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
+            "title": "CMS Program Statistics - Medicare Part D"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/89qs-mr7i",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-21",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "demographics",
-                "mortality"
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
-            "identifier": "https://data.cdc.gov/api/views/89qs-mr7i",
             "description": "Monthly COVID-19 death rates per 100,000 population stratified by age group, race/ethnicity, sex, and region",
-            "title": "Monthly COVID-19 Death Rates per 100,000 Population by Age Group, Race and Ethnicity, Sex, and Region",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154054,53 +154034,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/89qs-mr7i",
+            "issued": "2023-11-21",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "demographics",
+                "mortality"
+            ],
+            "landingPage": "https://data.cdc.gov/d/89qs-mr7i",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Monthly COVID-19 Death Rates per 100,000 Population by Age Group, Race and Ethnicity, Sex, and Region"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/jk8p-fqhn",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-02-17",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-12-13/2023-05-12",
-            "modified": "2023-05-12",
-            "references": [
-                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
-            ],
-            "keyword": [
-                "administration",
-                "age",
-                "coronavirus",
-                "covid-19",
-                "demographics",
-                "ethnicity",
-                "immunization",
-                "izdl",
-                "race",
-                "sex",
-                "vaccination"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCIRD",
                 "hasEmail": "mailto:iisinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/jk8p-fqhn",
             "description": "<p style=\"margin:0in;vertical-align:baseline;\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>This site provides historical data related to COVID-19 booster dose eligibility presented on two CDC COVID Data Tracker sites:&nbsp;</span><a href=\"https://covid.cdc.gov/covid-data-tracker/#vaccinations\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Vaccinations in the US</span></a><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>&nbsp;and&nbsp;</span><a href=\"https://covid.cdc.gov/covid-data-tracker/#vaccination-equity\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Vaccination Equity</span></a><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>.&nbsp;</span><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>&nbsp;</span><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Data are updated weekly on Thursdays.</span></p><p style=\"margin:0in;vertical-align:baseline;\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Some COVID-19 vaccine recipients are&nbsp;</span><a href=\"https://www.cdc.gov/coronavirus/2019-ncov/vaccines/booster-shot.html\" target=\"_blank\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>eligible to receive booster doses</span></a><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>,&nbsp;</span><span style=\"font-size:11px;\">&nbsp;</span><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>and criteria for booster eligibility may change over time. Data and footnotes will be updated to align with the current recommendations.&nbsp;</span><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>&nbsp;</span></p><p style=\"margin:0in;vertical-align:baseline;\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>CDC counts people as having &ldquo;received a booster dose&rdquo; if they are fully vaccinated and received another dose of any COVID-19 vaccine on or after August 13, 2021. This does not distinguish whether the recipient is&nbsp;</span><a href=\"https://www.cdc.gov/coronavirus/2019-ncov/vaccines/recommendations/immuno.html\" target=\"_blank\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>immunocompromised and received an additional dose</span></a></p><p style=\"margin:0in;vertical-align:baseline;\"><strong><em><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Data Limitations:</span></em></strong><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>&nbsp;</span></p><ul style=\"list-style-type: undefined;margin-left:0in;\"><li><span style='font-family:\"Calibri\",sans-serif;color:black;font-size:11.0pt;color:black;'>The booster eligibility metric excludes fully vaccinated recipients who have an &ldquo;Other&rdquo; primary series vaccine type.\u202f</span><span style='font-family:\"Calibri\",sans-serif;font-size:11.0pt;color:black;'>&nbsp;</span></li><li><span style='font-family:\"Calibri\",sans-serif;color:black;font-size:11.0pt;color:black;'>Booster eligibility counts and percentages exclude vaccine administrations reported by Texas as the primary series cannot be linked to booster dose in the aggregate data submitted by Texas.</span><span style='font-family:\"Calibri\",sans-serif;font-size:11.0pt;color:black;'>&nbsp;</span></li></ul><p style=\"margin:0in;vertical-align:baseline;\"><strong><em><span style='font-size:15px;font-family:\"Calibri\",sans-serif;'>Footnotes:</span></em></strong></p><p style=\"margin:0in;vertical-align:baseline;\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;'>CDC counts people as being &ldquo;</span><a href=\"https://www.cdc.gov/coronavirus/2019-ncov/vaccines/booster-shot.html\" target=\"_blank\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:windowtext;'>eligible to get a booster dose</span></a><",
-            "title": "COVID-19 Booster Dose Eligibility in the United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154123,41 +154094,53 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/jk8p-fqhn",
+            "issued": "2022-02-17",
+            "keyword": [
+                "administration",
+                "age",
+                "coronavirus",
+                "covid-19",
+                "demographics",
+                "ethnicity",
+                "immunization",
+                "izdl",
+                "race",
+                "sex",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/jk8p-fqhn",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1D",
+            "modified": "2023-05-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
+            ],
+            "spatial": "US",
+            "temporal": "2020-12-13/2023-05-12",
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "COVID-19 Booster Dose Eligibility in the United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/pp7x-dyj2",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2016-10-13",
-            "@type": "dcat:Dataset",
-            "modified": "2019-04-05",
-            "keyword": [
-                "mortality",
-                "nchs"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Krista Kniss",
                 "hasEmail": "mailto:krk9@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/pp7x-dyj2",
             "description": "",
-            "title": "Deaths from Pneumonia and Influenza (P&I) and all deaths, by state and region, National Center For Health Statistics Mortality Surveillance System",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154180,35 +154163,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/pp7x-dyj2",
+            "issued": "2016-10-13",
+            "keyword": [
+                "mortality",
+                "nchs"
+            ],
+            "landingPage": "https://data.cdc.gov/d/pp7x-dyj2",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-04-05",
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
+            "title": "Deaths from Pneumonia and Influenza (P&I) and all deaths, by state and region, National Center For Health Statistics Mortality Surveillance System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/3crz-97tw",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-09-26",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-09",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DCPC Communications (CDC)",
                 "hasEmail": "mailto:dcpccommunications@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/3crz-97tw",
             "description": "This database of cancer-related citations for publications authored by CDC\u2019s Division of Cancer Prevention and Control (DCPC) staff, fosters collaboration among scientists throughout the world. Allows for searching for links to scientific articles authored or co-authored by researchers from DCPC since 2000.",
-            "title": "Cancer Research Citation Search",
-            "programCode": [
-                "009:029"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154231,85 +154218,81 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/3crz-97tw",
+            "issued": "2024-09-26",
+            "landingPage": "https://data.cdc.gov/d/3crz-97tw",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-09",
+            "programCode": [
+                "009:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Cancer Research Citation Search"
-            ]
+            ],
+            "title": "Cancer Research Citation Search"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/xvzi-6ads",
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
-            "identifier": "1109e8a3-8da6-581a-9241-52938b196807",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet measure v2.10.64 (coreset-impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure.csv",
-                    "description": "CoreSet measure v2.10.64 (coreset-impl)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet measure v2.10.64 (coreset-impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet measure v2.10.64 (coreset-impl)"
                 }
             ],
+            "identifier": "1109e8a3-8da6-581a-9241-52938b196807",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/xvzi-6ads",
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
+            "title": "CoreSet measure v2.10.64 (coreset-impl)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fip8-rcng",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-02-02",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-27",
-            "keyword": [
-                "glossary",
-                "methodology"
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
-            "identifier": "https://data.cdc.gov/api/views/fip8-rcng",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "The Tax Burden on Tobacco Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154317,46 +154300,39 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fip8-rcng",
+            "issued": "2015-02-02",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fip8-rcng",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
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
+            "title": "The Tax Burden on Tobacco Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hbbg-vj7f",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "all serogroups",
-                "meningococcal disease",
-                "nedss",
-                "netss",
-                "nndss",
-                "serogroup b",
-                "serogroups acwy",
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
-            "identifier": "https://data.cdc.gov/api/views/hbbg-vj7f",
             "description": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154379,35 +154355,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hbbg-vj7f",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "all serogroups",
+                "meningococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "serogroup b",
+                "serogroups acwy",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hbbg-vj7f",
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
+            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/c75w-3h6e",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-12-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-02",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/c75w-3h6e",
             "description": "Trace measurement of aerosol chemical composition in workplace atmospheres requires the development of high-throughput aerosol collectors that are compact, hand-portable, and can be operated using personal pumps. We describe the design and characterization of a compact, high flow, Turbulent-mixing Condensation Aerosol-in-Liquid Concentrator (TCALC) that allows direct collection of aerosols as liquid suspensions, for off-line chemical, biological, or microscopy analysis. The TCALC unit, measuring approximately 12 \u00d7 16 \u00d7 18 cm, operates at an aerosol sample flowrate of up to 10 L min-1, using rapid mixing of a hot flow saturated with water vapor and a cold aerosol sample flow, thereby promoting condensational growth of aerosol particles. We investigated the effect of operating parameters such as vapor temperature, growth tube wall temperature, and aerosol sample flowrate, along with the effect of particle diameter, inlet humidity, aerosol concentration, and operation time on TCALC performance. Nanoparticles with an initial aerodynamic diameter \u2265 25 nm could grow to droplet diameters > 1400 nm with an efficiency \u2265 80%. Good droplet growth efficiency was achieved for sampled aerosol relative humidity \u2265 9%. We measured complete aerosol collection for concentrations of \u2264 3\u00d7105 cm-3. The results showed good agreement between the particulate mass collected through the liquid collector and direct filter collection. The TCALC eliminates the need for sample preparation and filter digestion during chemical analysis, thereby increasing sample recovery and substantially improving the limit of detection and sensitivity of off-line trace analysis of collected liquid samples.",
-            "title": "A High-throughput, Turbulent-mixing, Condensation Aerosol Concentrator for Direct Aerosol Collection as a Liquid Suspension",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154415,39 +154402,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/c75w-3h6e",
+            "issued": "2024-12-02",
+            "landingPage": "https://data.cdc.gov/d/c75w-3h6e",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-02",
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
+            "title": "A High-throughput, Turbulent-mixing, Condensation Aerosol Concentrator for Direct Aerosol Collection as a Liquid Suspension"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/xz2b-xd8b",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2025-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-28",
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
-            "identifier": "f38d0706-1239-442c-a3cc-40ef1b686ac0",
             "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
-            "title": "NADAC (National Average Drug Acquisition Cost) 2025",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154455,51 +154438,49 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "f38d0706-1239-442c-a3cc-40ef1b686ac0",
+            "issued": "2025-01-01",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "landingPage": "https://healthdata.gov/d/xz2b-xd8b",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-28",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Drug Pricing and Payment",
                 "National Average Drug Acquisition Cost"
-            ]
+            ],
+            "title": "NADAC (National Average Drug Acquisition Cost) 2025"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-price-transparency-enforcement-activities-and-outcomes",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-03-05",
-            "temporal": "2023-10-01/2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
-            "references": [
-                "https://data.cms.gov/resources/hospital-price-transparency-enforcement-activities-and-outcomes-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "hospitals & facilities",
-                "medicare"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Price Transparency - CM",
                 "hasEmail": "mailto:Pricetransparencyhospitalcharges@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/6a3aa708-3c9d-411a-a1a4-e046d3ade7ef/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/hospital-price-transparency-enforcement-activities-and-outcomes-data-dictionary",
             "description": "The Hospital Price Transparency Enforcement Activities and Outcomes dataset contains information related to enforcement actions taken by CMS following a compliance review of a hospital's obligation to establish, update and make public a list of the hospital\u2019s standard charges for items and services provided by the hospital, in accordance with regulation (45 CFR 180). This data set includes the name of each hospital or hospital location, the hospital or hospital location address, the outcome or action following a CMS compliance review and the date of the outcome or action taken.",
-            "title": "Hospital Price Transparency Enforcement Activities and Outcomes",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6a3aa708-3c9d-411a-a1a4-e046d3ade7ef/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6a3aa708-3c9d-411a-a1a4-e046d3ade7ef/data",
+                    "mediaType": "text/html",
                     "title": "Hospital Price Transparency Enforcement Activities and Outcomes : 2024-09-01"
                 },
                 {
@@ -154539,26 +154520,58 @@
                     "title": "Hospital Price Transparency Enforcement Activities and Outcomes : 2023-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/hospital-price-transparency-enforcement-activities-and-outcomes-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/6a3aa708-3c9d-411a-a1a4-e046d3ade7ef/data-viewer",
+            "issued": "2024-03-05",
+            "keyword": [
+                "health care use & payments",
+                "hospitals & facilities",
+                "medicare"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-price-transparency-enforcement-activities-and-outcomes",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-10-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/hospital-price-transparency-enforcement-activities-and-outcomes-methodology"
+            ],
+            "temporal": "2023-10-01/2024-09-30",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Hospital Price Transparency Enforcement Activities and Outcomes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2002",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), analyze general treatment services trends, and generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment, substance abuse therapy and counseling, pharmacotherapies, testing, transitional, ancillary), primary focus (substance abuse, mental health, both, general health, other), hotline operation, Opioid Treatment Programs and medication dispensed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2002) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2002-nid13585",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2002-nid13585"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2002-nid13585",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -154571,69 +154584,30 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2002",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2002-nid13585",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), analyze general treatment services trends, and generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment, substance abuse therapy and counseling, pharmacotherapies, testing, transitional, ancillary), primary focus (substance abuse, mental health, both, general health, other), hotline operation, Opioid Treatment Programs and medication dispensed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2002)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2002-nid13585",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2002) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2002-nid13585"
-                }
-            ]
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2002)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -154656,26 +154630,65 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-aids-public-use-data",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/aids.html",
+            "description": "<p>The AIDS Public Information Data Set (APIDS) for years 1981-2002 on CDC WONDER online database contains counts of AIDS (Acquired Immune Deficiency Syndrome) cases reported by state and local health departments, by demographics; location (region and selected metropolitan areas); case-definition; month/year and quarter-year of diagnosis, report, and death (if applicable); and HIV exposure group (risk factors for AIDS).  Data are produced by the US Department of Health and Human Services (US DHHS), Public Health Service (PHS), Centers for Disease Control and Prevention (CDC), National Center for HIV, STD and TB Prevention (NCHSTP), Division of HIV/AIDS Prevention (DHP).</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/AIDSPublic.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "8208b2a4-58bb-460e-b6fc-56ae6e6cd5e2",
             "issued": "2012-05-30",
-            "temporal": "1981-01-01T00:00:00-05:00/2002-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "age",
                 "aids",
@@ -154700,60 +154713,32 @@
                 "sexual orientation",
                 "vital status"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-aids-public-use-data",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "8208b2a4-58bb-460e-b6fc-56ae6e6cd5e2",
-            "description": "<p>The AIDS Public Information Data Set (APIDS) for years 1981-2002 on CDC WONDER online database contains counts of AIDS (Acquired Immune Deficiency Syndrome) cases reported by state and local health departments, by demographics; location (region and selected metropolitan areas); case-definition; month/year and quarter-year of diagnosis, report, and death (if applicable); and HIV exposure group (risk factors for AIDS).  Data are produced by the US Department of Health and Human Services (US DHHS), Public Health Service (PHS), Centers for Disease Control and Prevention (CDC), National Center for HIV, STD and TB Prevention (NCHSTP), Division of HIV/AIDS Prevention (DHP).</p>",
-            "title": "CDC WONDER: AIDS Public Use Data",
-            "programCode": [
-                "009:027"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://wonder.cdc.gov/AIDSPublic.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/aids.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "temporal": "1981-01-01T00:00:00-05:00/2002-12-31T00:00:00-05:00",
+            "title": "CDC WONDER: AIDS Public Use Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/y3kz-zbmh",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-02-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-13",
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
-            "identifier": "dfaabae9-21bd-4f77-84f6-3bda5806c6f7",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-06-to-2023-02-12",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154762,42 +154747,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-06-to-2023-02-12"
                 }
             ],
+            "identifier": "dfaabae9-21bd-4f77-84f6-3bda5806c6f7",
+            "issued": "2023-02-15",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/y3kz-zbmh",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-02-13",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-06-to-2023-02-12"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nehrs/about.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm\u201d",
-            "issued": "2023-09-27",
-            "@type": "dcat:Dataset",
-            "temporal": "2008-2011",
-            "modified": "2023-09-27",
-            "keyword": [
-                "electronic health records",
-                "health us",
-                "nchs",
-                "nehrs",
-                "research-data-center"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:nhcs@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/53z7-6asy",
+            "describedBy": "The sampling frame was composed of Master files for all American physicians who met the following criteria: Office-based; Principally engaged in patient care activities; Non-federally employed; Not in specialties of anesthesiology, pathology, or radiology; and Younger than 85 years of age at the time of the survey.",
             "description": "The National Electronic Health Records Survey (NEHRS) is an annual survey of non-federally employed, office-based physicians practicing in the United States (excluding those in the specialties of anesthesiology, radiology, and pathology). NEHRS began in 2008 and was originally designed as an annual mail supplement to the National Ambulatory Medical Care Survey (NAMCS). Prior to 2012, NEHRS was a supplement to the NAMCS, referred to as the NAMCS Electronic Medical Records Supplement. The annual data collected was similar to NEHRS and may be analyzed as a distinct dataset.\nData from the supplement can be used to produce state and national estimates of EHR adoption and capabilities, burden associated with EHRs, and progress physicians have made towards meeting the policy goals of the HITECH Act. \nPlease refer to the following link for the 2008\u20142011 NAMCS Electronic Medical Records Supplemental questionnaire and data dictionary: https://www.cdc.gov/nchs/nehrs/questionnaires.htm.",
-            "title": "National Ambulatory Medical Care Survey: Electronic Medical Records Supplement, 2008-2011, Restricted",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154805,37 +154784,45 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "The sampling frame was composed of Master files for all American physicians who met the following criteria: Office-based; Principally engaged in patient care activities; Non-federally employed; Not in specialties of anesthesiology, pathology, or radiology; and Younger than 85 years of age at the time of the survey.",
+            "identifier": "https://data.cdc.gov/api/views/53z7-6asy",
+            "issued": "2023-09-27",
+            "keyword": [
+                "electronic health records",
+                "health us",
+                "nchs",
+                "nehrs",
+                "research-data-center"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nehrs/about.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-09-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm\u201d",
+            "spatial": "United States",
+            "temporal": "2008-2011",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Ambulatory Medical Care Survey: Electronic Medical Records Supplement, 2008-2011, Restricted"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/8ve6-tiah",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Research Branch (RB), National Personal Protective Technology Laboratory (NPPTL)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/8ve6-tiah",
             "description": "In response to the shortage of N95\u00ae filtering facepiece respirators (FFRs) for healthcare workers during the COVID-19 pandemic, the Centers for Disease Control and Prevention (CDC) issued strategies for extended use and limited reuse of N95 FFRs to conserve supply. Previously worn N95 FFRs can serve as a source of pathogens, which can be transferred to the wearer while doffing and donning a respirator when practicing reuse. To reduce the risk of self-contamination when donning and doffing reused FFRs, the CDC suggested storing FFRs for five days between uses to allow for the decay of viable pathogens including SARS-CoV-2. This study assessed the persistence of the SARS-CoV-2 strain USA-WA1/2020 on N95 FFRs under controlled storage conditions for up to five days to inform the CDC guidance.",
-            "title": "Persistence of SARS-CoV-2 on N95 filtering facepiece respirators: implications for reuse",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154843,43 +154830,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8ve6-tiah",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/8ve6-tiah",
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
+            "title": "Persistence of SARS-CoV-2 on N95 filtering facepiece respirators: implications for reuse"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/nis/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-09-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-28",
-            "keyword": [
-                "adults",
-                "coverage",
-                "flu vaccination",
-                "influenza",
-                "vaccination",
-                "vaccine coverage"
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
-            "identifier": "https://data.cdc.gov/api/views/8dyx-9z99",
             "description": "Cumulative Influenza Vaccination Coverage Age Group, Race/Ethnicity, and Jurisdiction, Adults 18 Years and Older, United States, National Immunization Survey Adult COVID Module.\n\nThe National Immunization Survey-Adult COVID Module (NIS-ACM) was launched in April 2021 among adults 18 years and older. The survey was used to monitor COVID-19 vaccination uptake and confidence in vaccination among adults and included questions about influenza vaccination.",
-            "title": "Cumulative Influenza Vaccination Coverage by Race/Ethnicity and Age Group, NIS-ACM (Archived)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154902,24 +154881,58 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, District of Columbia, US Virgin Islands, and Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/8dyx-9z99",
+            "issued": "2022-09-28",
+            "keyword": [
+                "adults",
+                "coverage",
+                "flu vaccination",
+                "influenza",
+                "vaccination",
+                "vaccine coverage"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/nis/",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-03-28",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States, District of Columbia, US Virgin Islands, and Puerto Rico",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Cumulative Influenza Vaccination Coverage by Race/Ethnicity and Age Group, NIS-ACM (Archived)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2008-0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. Detailed NSDUH 2008 documentation <a href=\"http://www.samhsa.gov/data/2k12/NSDUH2008MRB/Index.aspx\">http://www.samhsa.gov/data/2k12/NSDUH2008MRB/Index.aspx</a> is available from SAMHSA. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2008 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For this 2008 survey, Adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. A split-sample design also was included to administer separate sets of questions to assess impairment due to mental health problems. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2008) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2008-nid13602",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2008-nid13602"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2008-nid13602",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -154960,108 +154973,77 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2008-0",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2008-nid13602",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. Detailed NSDUH 2008 documentation <a href=\"http://www.samhsa.gov/data/2k12/NSDUH2008MRB/Index.aspx\">http://www.samhsa.gov/data/2k12/NSDUH2008MRB/Index.aspx</a> is available from SAMHSA. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2008 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For this 2008 survey, Adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. A split-sample design also was included to administer separate sets of questions to assess impairment due to mental health problems. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health (NSDUH-2008)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2008-nid13602",
-                    "description": "National Survey on Drug Use and Health (NSDUH-2008) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2008-nid13602"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health (NSDUH-2008)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/y53x-tedw",
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
-            "identifier": "9a44a67b-4623-5bf5-941e-2d28a9874023",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_fileType_measureDisplayGroups",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/fileType_measureDisplayGroups.csv",
-                    "description": "{\"dataset\": \"fileType_measureDisplayGroups\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"fileType_measureDisplayGroups\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/fileType_measureDisplayGroups.csv",
+                    "mediaType": "text/csv",
                     "title": "fileType_measureDisplayGroups csv file"
                 }
             ],
+            "identifier": "9a44a67b-4623-5bf5-941e-2d28a9874023",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/y53x-tedw",
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
+            "title": "prodAuto_fileType_measureDisplayGroups"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#vaccine-confidence",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-06-22",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-03",
-            "keyword": [
-                "covid-19 vaccination",
-                "covid tracker",
-                "nis-acm"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James Singleton",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/iwxc-qftf",
             "description": "National Immunization Survey Adult COVID Module (NIS-ACM): CDC is providing information on COVID-19 vaccine confidence to supplement vaccine administration data. These data represent trends in vaccination status and intent by demographics. \n\nFollowing collection of August 2021 survey data, an error in data processing led to incorrect categorization of some survey respondents; some respondents who should have been categorized as MSA: Principal City instead were categorized as MSA: Non-Principal City. Data downloaded during the period September 12, 2021 through September 30, 2021 may have incorrect estimates by MSA status, SVI of county of residence, and political leaning of county of residence.",
-            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): Vaccination Status and Intent by Demographics",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -155084,39 +155066,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/iwxc-qftf",
+            "issued": "2022-06-22",
+            "keyword": [
+                "covid-19 vaccination",
+                "covid tracker",
+                "nis-acm"
+            ],
+            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#vaccine-confidence",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-03",
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
+            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): Vaccination Status and Intent by Demographics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/68ej-h5ze",
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
-            "identifier": "https://data.cdc.gov/api/views/68ej-h5ze",
             "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 5 - Chicago",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -155139,38 +155122,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/68ej-h5ze",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/68ej-h5ze",
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
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 5 - Chicago"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/y5r7-kn8s",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-22",
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
-            "identifier": "1e1fd4d7-e872-4613-b40a-268815c7dabe",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-02-14 to 2022-02-20",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -155178,38 +155163,35 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "1e1fd4d7-e872-4613-b40a-268815c7dabe",
+            "issued": "2022-02-23",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/y5r7-kn8s",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2022-02-22",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-02-14 to 2022-02-20"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/gr26-95h2",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-06-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-03",
-            "keyword": [
-                "covid-19 vaccination",
-                "covid tracker",
-                "nis-ccm"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James Singleton",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/gr26-95h2",
             "description": "National Immunization Survey Child COVID Module (NIS-CCM): CDC is providing information on COVID-19 vaccine confidence to supplement vaccine administration data. These data represent trends in vaccination status and intent, and other behavioral indicators, by demographics and other characteristics.",
-            "title": "National Immunization Survey Child COVID Module (NIS-CCM): Vaccination Status and Intent by Demographics | Data | Centers for Disease Control and Prevention (cdc.gov)",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -155232,100 +155214,88 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/gr26-95h2",
+            "issued": "2022-06-21",
+            "keyword": [
+                "covid-19 vaccination",
+                "covid tracker",
+                "nis-ccm"
+            ],
+            "landingPage": "https://data.cdc.gov/d/gr26-95h2",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-03",
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
+            "title": "National Immunization Survey Child COVID Module (NIS-CCM): Vaccination Status and Intent by Demographics | Data | Centers for Disease Control and Prevention (cdc.gov)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/y759-qbzb",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "dqatlas",
-                "dqatlas_devauto",
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
-            "identifier": "5937b2be-32a4-5dc9-b9dc-b1f97e38e935",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_brief",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/brief.csv",
-                    "description": "{\"dataset\": \"brief\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"brief\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/brief.csv",
+                    "mediaType": "text/csv",
                     "title": "brief csv file"
                 }
             ],
+            "identifier": "5937b2be-32a4-5dc9-b9dc-b1f97e38e935",
+            "issued": "2024-07-17",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/y759-qbzb",
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
+            "title": "devAuto_brief"
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
-                "city",
-                "disability",
-                "gis",
-                "health",
-                "outcomes",
-                "place",
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
-            "identifier": "https://data.cdc.gov/api/views/vgc8-iyc4",
             "description": "This dataset contains model-based place (incorporated and census designated places) estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia \u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2022 or 2021 data, Census Bureau 2020 population estimates, and American Community Survey (ACS) 2018\u20132022 estimates. The 2024 release uses 2022 BRFSS data for 36 measures and 2021 BRFSS data for 4 measures (high blood pressure, high cholesterol, cholesterol screening, and taking medicine for high blood pressure control among those with high blood pressure) that the survey collects data on every other year. These data can be joined with the 2020 Census place boundary file in a GIS system to produce maps for 40 measures at the place level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software. https://cdcarcgis.maps.arcgis.com/home/item.html?id=3b7221d4e47740cab9235b839fa55cd7",
-            "title": "PLACES: Place Data (GIS Friendly Format), 2024 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -155348,41 +155318,52 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vgc8-iyc4",
+            "issued": "2024-08-23",
+            "keyword": [
+                "behaviors",
+                "city",
+                "disability",
+                "gis",
+                "health",
+                "outcomes",
+                "place",
+                "places",
+                "prevalence",
+                "prevention",
+                "risk",
+                "status"
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
+            "title": "PLACES: Place Data (GIS Friendly Format), 2024 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/3kjq-j5dm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-06-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-27",
-            "keyword": [
-                "glossary",
-                "methodology",
-                "sae",
-                "sammec"
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
-            "identifier": "https://data.cdc.gov/api/views/3kjq-j5dm",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "Smoking-Attributable Mortality, Morbidity, and Economic Costs (SAMMEC) - Smoking-Attributable Expenditures (SAE) Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -155390,54 +155371,51 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/3kjq-j5dm",
+            "issued": "2015-06-17",
+            "keyword": [
+                "glossary",
+                "methodology",
+                "sae",
+                "sammec"
+            ],
+            "landingPage": "https://data.cdc.gov/d/3kjq-j5dm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-07-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Health Consequences and Costs"
-            ]
+            ],
+            "title": "Smoking-Attributable Mortality, Morbidity, and Economic Costs (SAMMEC) - Smoking-Attributable Expenditures (SAE) Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/home-health-agency-enrollments",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-04-20",
-            "temporal": "2023-04-01/2025-03-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-10/HHA_Data_Guidance.pdf"
-            ],
-            "keyword": [
-                "home health",
-                "hospitals & facilities",
-                "medicare",
-                "medicare advantage",
-                "original medicare",
-                "provider enrollment"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/15f64ab4-3172-4a27-b589-ebd67a6d28aa/data-viewer",
-            "description": "The Home Health Agency (HHA) Enrollments dataset provides enrollment information on all HHAs currently enrolled in Medicare. This data includes information on the HHA's legal business name, doing business as name, organization type and address.\u00a0",
-            "title": "Home Health Agency Enrollments",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/HHA_Enrollments_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Home Health Agency (HHA) Enrollments dataset provides enrollment information on all HHAs currently enrolled in Medicare. This data includes information on the HHA's legal business name, doing business as name, organization type and address.\u00a0",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/15f64ab4-3172-4a27-b589-ebd67a6d28aa/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/15f64ab4-3172-4a27-b589-ebd67a6d28aa/data",
+                    "mediaType": "text/html",
                     "title": "Home Health Agency Enrollments : 2025-01-01"
                 },
                 {
@@ -155537,26 +155515,61 @@
                     "title": "Home Health Agency Enrollments : 2023-04-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/HHA_Enrollments_Data_Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/15f64ab4-3172-4a27-b589-ebd67a6d28aa/data-viewer",
+            "issued": "2023-04-20",
+            "keyword": [
+                "home health",
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/home-health-agency-enrollments",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-10/HHA_Data_Guidance.pdf"
+            ],
+            "temporal": "2023-04-01/2025-03-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Home Health Agency Enrollments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2007",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2007) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2007-nid13535",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2007-nid13535"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2007-nid13535",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -155569,68 +155582,30 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2007",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2007-nid13535",
-            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2007)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2007-nid13535",
-                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2007) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2007-nid13535"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2007)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/egm8-9wq7",
+            "accrualPeriodicity": "Archived",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-10-06",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-12-13 to 2021-09-30",
-            "modified": "2022-09-28",
-            "references": [
-                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
-            ],
-            "keyword": [
-                "administration",
-                "coronavirus",
-                "covid-19",
-                "immunization",
-                "izdl",
-                "report date",
-                "vaccination"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCIRD",
                 "hasEmail": "mailto:iisinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/egm8-9wq7",
             "description": "The Federal Pharmacy Partnership for Long-Term Care (LTC) Program was a partnership between CDC and CVS, Walgreens, and Managed Health Care Associates, Inc. The program offered on-site COVID-19 vaccination services for residents of nursing homes and assisted living facilities. The Federal Pharmacy Partnership for LTC Program was in effect after vaccines became available to April 23, 2021. This is the historical archived data related to the LTC Program and represents data that was shown on COVID Data Tracker through September 30, 2021. Twelve variables that provided data on residents and staff vaccinated through the program were removed from\u00a0the\u00a0COVID-19 Vaccinations in the United States,Jurisdiction dataset. LTC was removed as an option from the location variable in the following datasets: COVID-19 Vaccinations in the United States,Jurisdiction and COVID-19 Vaccination Trends in the United States,National and Jurisdictional.",
-            "title": "Archive: COVID-19 LTC Program Vaccinations and Trends in the United States, Jurisdiction",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -155653,47 +155628,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/egm8-9wq7",
+            "issued": "2021-10-06",
+            "keyword": [
+                "administration",
+                "coronavirus",
+                "covid-19",
+                "immunization",
+                "izdl",
+                "report date",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/egm8-9wq7",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Archived",
+            "modified": "2022-09-28",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
+            ],
+            "spatial": "US",
+            "temporal": "2020-12-13 to 2021-09-30",
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "Archive: COVID-19 LTC Program Vaccinations and Trends in the United States, Jurisdiction"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hwyy-s2tt",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "carbapenemase-producing carbapenem-resistant enterobacteriaceae",
-                "chancroid",
-                "chlamydia trachomatis infection",
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
-            "identifier": "https://data.cdc.gov/api/views/hwyy-s2tt",
             "description": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Reporting jurisdictions were informed CDC could receive data for this condition in August 2019. Please note there will be a delay in reporting of case notifications for this condition to CDC.",
-            "title": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -155716,47 +155693,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hwyy-s2tt",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "carbapenemase-producing carbapenem-resistant enterobacteriaceae",
+                "chancroid",
+                "chlamydia trachomatis infection",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hwyy-s2tt",
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
+            "title": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/m6gf-vfkz",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "all serotypes)",
-                "giardiasis",
-                "gonorrhea",
-                "haemophilus influenza",
-                "invasive disease (all ages",
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
-            "identifier": "https://data.cdc.gov/api/views/m6gf-vfkz",
             "description": "NNDSS - Table II. Giardiasis to Haemophilus influenza - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\r\n \r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -155779,39 +155754,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/m6gf-vfkz",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "all serotypes)",
+                "giardiasis",
+                "gonorrhea",
+                "haemophilus influenza",
+                "invasive disease (all ages",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/m6gf-vfkz",
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
+            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.ncbi.nlm.nih.gov/biosample",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-08",
-            "keyword": [
-                "biological assay",
-                "computational biology"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/w5ku-k2ma",
             "description": "The BioSample database contains descriptions of biological source materials used in experimental assays.",
-            "title": "BioSample",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -155826,44 +155809,39 @@
                     "title": "BioSample API via Entrez Programming Utilities"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/w5ku-k2ma",
+            "issued": "2016-08-08",
+            "keyword": [
+                "biological assay",
+                "computational biology"
+            ],
+            "landingPage": "http://www.ncbi.nlm.nih.gov/biosample",
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
                 "Molecular biology/Genetics"
-            ]
+            ],
+            "title": "BioSample"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5egk-p6rd",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "chlamydia trachomatis infection",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5egk-p6rd",
             "description": "NNDSS - Table II. Chlamydia trachomatis infection to Coccidioidomycosis - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Chlamydia trachomatis infection to Coccidioidomycosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -155886,85 +155864,91 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5egk-p6rd",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "chlamydia trachomatis infection",
+                "coccidioidomycosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5egk-p6rd",
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
+            "title": "NNDSS - Table II. Chlamydia trachomatis infection to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ycku-mvk7",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-13",
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
-            "identifier": "fe676dcf-c49f-592c-a11c-2c0f3e9ab684",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet filters v2.10.64 (coreset-cmsdev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/filters.csv",
-                    "description": "CoreSet filters v2.10.64 (coreset-cmsdev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet filters v2.10.64 (coreset-cmsdev)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet filters v2.10.64 (coreset-cmsdev)"
                 }
             ],
+            "identifier": "fe676dcf-c49f-592c-a11c-2c0f3e9ab684",
+            "issued": "2024-11-13",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/ycku-mvk7",
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
+            "title": "CoreSet filters v2.10.64 (coreset-cmsdev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ycqg-qrdk",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2016-09-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-09",
-            "keyword": [
-                "amp",
-                "average manufacturer price"
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
-            "identifier": "80956a7d-e343-54f3-94a7-45d41b34fc0b",
             "description": "Drugs that have been reported under the Medicaid Drug Rebate Program along with an indication of whether or not the required Average Manufacturer Price (AMP) was reported for each drug. All drugs are identified in the file by the 11-digit National Drug Code, product name, labeler name, and reported (R) or not reported (NR).",
-            "title": "Drug AMP Reporting - Quarterly",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -155972,53 +155956,39 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "80956a7d-e343-54f3-94a7-45d41b34fc0b",
+            "issued": "2016-09-26",
+            "keyword": [
+                "amp",
+                "average manufacturer price"
+            ],
+            "landingPage": "https://healthdata.gov/d/ycqg-qrdk",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-11-09",
+            "programCode": [
+                "009:076"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "Drug AMP Reporting - Quarterly"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2018-12-04",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://academic.oup.com/aje/article/179/8/1025/109078",
-                "https://academic.oup.com/aje/article/182/2/127/93984",
-                "https://www.cdc.gov/pcd/issues/2017/17_0281.htm",
-                "https://www.cdc.gov/pcd/issues/2018/18_0313.htm"
-            ],
-            "keyword": [
-                "500cities",
-                "behaviors",
-                "census",
-                "cities",
-                "outcomes",
-                "prevalence",
-                "prevention",
-                "tracts",
-                "unhealthy"
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
-            "identifier": "https://data.cdc.gov/api/views/vurf-k5wr",
             "description": "This is the complete dataset for the 500 Cities project 2017 release. This dataset includes 2015, 2014 model-based small area estimates for 27 measures of chronic disease related to unhealthy behaviors (5), health outcomes (13), and use of preventive services (9). Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. It represents a first-of-its kind effort to release information on a large scale for cities and for small areas within those cities. It includes estimates for the 500 largest US cities and approximately 28,000 census tracts within these cities. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these measures include Behavioral Risk Factor Surveillance System (BRFSS) data (2015, 2014), Census Bureau 2010 census population data, and American Community Survey (ACS) 2011-2015, 2010-2014 estimates. Because some questions are only asked every other year in the BRFSS, there are 7 measures from the 2014 BRFSS that are the same in the 2017 release as the previous 2016 release. More information about the methodology can be found at www.cdc.gov/500cities.",
-            "title": "500 Cities: Local Data for Better Health, 2017 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -156041,41 +156011,53 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vurf-k5wr",
+            "issued": "2018-12-04",
+            "keyword": [
+                "500cities",
+                "behaviors",
+                "census",
+                "cities",
+                "outcomes",
+                "prevalence",
+                "prevention",
+                "tracts",
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
+                "https://academic.oup.com/aje/article/179/8/1025/109078",
+                "https://academic.oup.com/aje/article/182/2/127/93984",
+                "https://www.cdc.gov/pcd/issues/2017/17_0281.htm",
+                "https://www.cdc.gov/pcd/issues/2018/18_0313.htm"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "500 Cities: Local Data for Better Health, 2017 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ydu5-gw79",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-08-09",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-16",
-            "keyword": [
-                "exchange puf",
-                "marketplace puf",
-                "py2023",
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
-            "identifier": "8c491ff0-8e6e-4988-b02a-e4736783aed3",
             "description": "The Service Area PUF (SA-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The SA-PUF contains issuer-level data on geographic service areas including state, county, and zip code.",
-            "title": "Service Area PUF \u2013 PY2023",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -156083,46 +156065,37 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "8c491ff0-8e6e-4988-b02a-e4736783aed3",
+            "issued": "2023-08-09",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2023",
+                "service area"
+            ],
+            "landingPage": "https://healthdata.gov/d/ydu5-gw79",
+            "modified": "2023-08-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Service Area PUF \u2013 PY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/vx8v-gfyf",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "age <5 years",
-                "all ages",
-                "all serotypes",
-                "gonorrhea",
-                "haemophilus influenzae",
-                "invasive disease",
-                "nedss",
-                "netss",
-                "nndss",
-                "serotype b",
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
-            "identifier": "https://data.cdc.gov/api/views/vx8v-gfyf",
             "description": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease (age <5 years), Serotype b - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease (age <5 years), Serotype b",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -156145,43 +156118,50 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vx8v-gfyf",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "age <5 years",
+                "all ages",
+                "all serotypes",
+                "gonorrhea",
+                "haemophilus influenzae",
+                "invasive disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "serotype b",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/vx8v-gfyf",
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
+            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease (age <5 years), Serotype b"
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
-            "keyword": [
-                "e-cigarette",
-                "legislation",
-                "osh",
-                "policy",
-                "state system",
-                "tax"
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
-            "identifier": "https://data.cdc.gov/api/views/kwbr-syv2",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Tax/kwbr-syv2",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  E-Cigarette Legislation\u2014Tax. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include state excise taxes on e-cigarettes and tax stamps.",
-            "title": "CDC STATE System E-Cigarette Legislation - Tax",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -156204,22 +156184,68 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Tax/kwbr-syv2",
+            "identifier": "https://data.cdc.gov/api/views/kwbr-syv2",
+            "issued": "2023-07-18",
+            "keyword": [
+                "e-cigarette",
+                "legislation",
+                "osh",
+                "policy",
+                "state system",
+                "tax"
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
             "theme": [
                 "Legislation"
-            ]
+            ],
+            "title": "CDC STATE System E-Cigarette Legislation - Tax"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nProvisional counts of deaths by the month the death occurred and by select causes of death for 2020-2023.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/9dzk-mvmi",
             "issued": "2021-02-03",
-            "temporal": "2020/2023",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-27",
             "keyword": [
                 "all causes",
                 "alzheimer disease",
@@ -156250,139 +156276,91 @@
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
-            "identifier": "https://data.cdc.gov/api/views/9dzk-mvmi",
-            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nProvisional counts of deaths by the month the death occurred and by select causes of death for 2020-2023.",
-            "title": "Monthly Provisional Counts of Deaths by Select Causes, 2020-2023",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-09-27",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2020/2023",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Monthly Provisional Counts of Deaths by Select Causes, 2020-2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/yf25-8bdz",
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
-            "identifier": "e6bda299-3940-5edc-8ef9-7af3d675d14e",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_states_measures",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/states_measures.csv",
-                    "description": "{\"dataset\": \"states_measures\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"states_measures\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/states_measures.csv",
+                    "mediaType": "text/csv",
                     "title": "states_measures csv file"
                 }
             ],
+            "identifier": "e6bda299-3940-5edc-8ef9-7af3d675d14e",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/yf25-8bdz",
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
+            "title": "prodAuto_states_measures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/pioneer-aco-model/pioneer-aco-model",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-05-26",
-            "temporal": "2012-01-01/2016-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-25",
-            "references": [
-                "https://data.cms.gov/resources/pioneer-aco-model-methodology"
-            ],
-            "keyword": [
-                "accountable care organizations",
-                "coordinated care",
-                "medicare",
-                "original medicare",
-                "payment models",
-                "value-based care"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ACO REACH - CMMI",
                 "hasEmail": "mailto:ACOREACH@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/bb2a336c-0710-4de9-80ad-6a2a5cbdbdeb/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/pioneer-aco-model-performance-year-2015-2016-data-dictionary",
             "description": "The Pioneer Accountable Care Organization (ACO) Model Public Use File (PUF) provides information on ACOs participating in the model. This dataset includes information on each ACO regarding beneficiaries, financial and quality results.",
-            "title": "Pioneer ACO Model",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bb2a336c-0710-4de9-80ad-6a2a5cbdbdeb/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bb2a336c-0710-4de9-80ad-6a2a5cbdbdeb/data",
+                    "mediaType": "text/html",
                     "title": "Pioneer ACO Model : 2016-12-01"
                 },
                 {
@@ -156446,26 +156424,59 @@
                     "title": "Pioneer ACO Model : 2012-05-11"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/pioneer-aco-model-performance-year-2015-2016-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/bb2a336c-0710-4de9-80ad-6a2a5cbdbdeb/data-viewer",
+            "issued": "2023-05-26",
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/pioneer-aco-model/pioneer-aco-model",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-05-25",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/pioneer-aco-model-methodology"
+            ],
+            "temporal": "2012-01-01/2016-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Pioneer ACO Model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Consumers/rss.xml",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "description": "This feed provides new health and safety updates related to FDA approved products",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Consumers/rss.xml",
+                    "mediaType": "application/rss+xml"
+                }
+            ],
+            "identifier": "82319f7a-9d6e-4b9e-b67f-cf8ff1a4980e",
             "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2012-05-30",
             "keyword": [
                 "approved",
                 "community health",
@@ -156477,40 +156488,41 @@
                 "safety",
                 "updates"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FDA Enterprise Data Inventory",
-                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
-            },
+            "landingPage": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Consumers/rss.xml",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2012-05-30",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "82319f7a-9d6e-4b9e-b67f-cf8ff1a4980e",
-            "description": "This feed provides new health and safety updates related to FDA approved products",
-            "title": "Health Information Updates",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Consumers/rss.xml",
-                    "mediaType": "application/rss+xml"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "Health Information Updates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cooperative-research-and-development-agreement-crada-opportunities-nih",
             "bureauCode": [
                 "001:05"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This RSS Feed represents all Collaborative Research and Development (CRADA) opportunities available from the National Institutes of Health (NIH).The intent of Congress in establishing CRADAs was to promote national technological competitiveness and the rapid transfer of the fruits of innovation to the marketplace. CRADA research and development at the NIH should be directed to the development of biological and behavioral technology, products, and processes by transferring relevant knowledge acquired from NIH research efforts to state and local governments, universities, and the private sector.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ott.nih.gov/rss/CRADARSS.XML",
+                    "mediaType": "text/html",
+                    "title": "Feed "
+                }
+            ],
+            "identifier": "8bbc3620-957c-44b4-aadc-e9c818de609c",
             "issued": "2012-05-30",
-            "temporal": "1981-01-01T00:00:00-05:00/1981-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "administrative",
                 "biomedical",
@@ -156527,115 +156539,84 @@
                 "reasearch",
                 "technology"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cooperative-research-and-development-agreement-crada-opportunities-nih",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Institutes of Health (NIH), Department of Health & Human Services"
             },
-            "identifier": "8bbc3620-957c-44b4-aadc-e9c818de609c",
-            "description": "<p>This RSS Feed represents all Collaborative Research and Development (CRADA) opportunities available from the National Institutes of Health (NIH).The intent of Congress in establishing CRADAs was to promote national technological competitiveness and the rapid transfer of the fruits of innovation to the marketplace. CRADA research and development at the NIH should be directed to the development of biological and behavioral technology, products, and processes by transferring relevant knowledge acquired from NIH research efforts to state and local governments, universities, and the private sector.</p>",
-            "title": "National Institues of Health: Outreach",
-            "programCode": [
-                "009:048"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ott.nih.gov/rss/CRADARSS.XML",
-                    "mediaType": "text/html",
-                    "title": "Feed "
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1981-01-01T00:00:00-05:00/1981-01-01T00:00:00-05:00",
             "theme": [
                 "Community",
                 "Health"
-            ]
+            ],
+            "title": "National Institues of Health: Outreach"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/yhga-m8m2",
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
-            "identifier": "2e201fad-8bc8-51b2-b810-e14bb45dd65c",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_concernLevel",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/concernLevel.csv",
-                    "description": "{\"dataset\": \"concernLevel\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"concernLevel\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/concernLevel.csv",
+                    "mediaType": "text/csv",
                     "title": "concernLevel csv file"
                 }
             ],
+            "identifier": "2e201fad-8bc8-51b2-b810-e14bb45dd65c",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/yhga-m8m2",
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
+            "title": "implAuto_concernLevel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/yi85-3s6j",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-08-09",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-16",
-            "keyword": [
-                "py2023",
-                "qhp landscape",
-                "sadp",
-                "shop",
-                "shop market dental"
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
-            "identifier": "5eb5f179-5e8c-433e-85a3-2a38d2c75ba2",
             "description": "The Dental SHOP Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2023 Dental SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -156643,19 +156624,51 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "5eb5f179-5e8c-433e-85a3-2a38d2c75ba2",
+            "issued": "2023-08-09",
+            "keyword": [
+                "py2023",
+                "qhp landscape",
+                "sadp",
+                "shop",
+                "shop market dental"
+            ],
+            "landingPage": "https://healthdata.gov/d/yi85-3s6j",
+            "modified": "2023-08-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2023 Dental SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/rdc/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information. Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement. If approved, data access would occur at a NCHS or Federal Statistical Research Data Center. For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:births@cdc.gov"
+            },
+            "describedBy": "All registered fetal deaths occurring to residents of the United States for a given year",
+            "description": "This dataset includes all fetal deaths for a given year and includes all items released in the public-use file. Additional information in this file includes state and county of residence (cities with a population of 250,000 or greater) and exact date of delivery (which includes day of month, month, and year).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This dataset includes all fetal deaths for a given year and includes all items released in the public-use file. Additional information in this file includes state and county of residence (cities with a population of 250,000 or greater) and exact date of delivery (which includes day of month, month, and year).",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "NCHS - All-County Fetal Death File with Exact Date of Delivery"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/mny7-y385",
+            "isPartOf": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "issued": "2022-12-22",
-            "@type": "dcat:Dataset",
-            "temporal": "1982/2020",
-            "modified": "2023-04-14",
             "keyword": [
                 "county",
                 "date of delivery",
@@ -156664,115 +156677,84 @@
                 "research-data-center",
                 "united states"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:births@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/rdc/index.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-04-14",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/mny7-y385",
-            "description": "This dataset includes all fetal deaths for a given year and includes all items released in the public-use file. Additional information in this file includes state and county of residence (cities with a population of 250,000 or greater) and exact date of delivery (which includes day of month, month, and year).",
-            "title": "NCHS - All-County Fetal Death File with Exact Date of Delivery",
-            "isPartOf": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "description": "This dataset includes all fetal deaths for a given year and includes all items released in the public-use file. Additional information in this file includes state and county of residence (cities with a population of 250,000 or greater) and exact date of delivery (which includes day of month, month, and year).",
-                    "@type": "dcat:Distribution",
-                    "title": "NCHS - All-County Fetal Death File with Exact Date of Delivery"
-                }
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information. Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement. If approved, data access would occur at a NCHS or Federal Statistical Research Data Center. For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "50 states and District of Columbia, all counties and cities with a population of 100,000 or greater",
-            "describedBy": "All registered fetal deaths occurring to residents of the United States for a given year",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "1982/2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - All-County Fetal Death File with Exact Date of Delivery"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/yix6-vnec",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-07-25",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
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
-            "identifier": "f2872f69-7ad7-5863-a87d-f95199d333be",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_briefType",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250127_ETL_DEV/briefType.csv",
-                    "description": "{\"dataset\": \"briefType\", \"stage\": \"featAuto\", \"update_id\": \"20250127_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"briefType\", \"stage\": \"featAuto\", \"update_id\": \"20250127_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250127_ETL_DEV/briefType.csv",
+                    "mediaType": "text/csv",
                     "title": "briefType csv file"
                 }
             ],
+            "identifier": "f2872f69-7ad7-5863-a87d-f95199d333be",
+            "issued": "2024-07-25",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/yix6-vnec",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2025-01-30",
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
+            "title": "featAuto_briefType"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://oculus.nlm.nih.gov/cgi/t/text/text-idx?page=browsecolls",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-03-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dataset",
-                "history of medicine",
-                "reference"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ebin-whwr",
             "description": "NLM History of Medicine Division's XML-encoded online oral histories provide access to a wealth of digitized transcripts, and audio when available.",
-            "title": "Online Oral Histories",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -156781,39 +156763,40 @@
                     "title": "Online Oral Histories"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ebin-whwr",
+            "issued": "2022-03-01",
+            "keyword": [
+                "dataset",
+                "history of medicine",
+                "reference"
+            ],
+            "landingPage": "https://oculus.nlm.nih.gov/cgi/t/text/text-idx?page=browsecolls",
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
+            "title": "Online Oral Histories"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "computational biology",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/f52g-xt9u",
             "description": "Sequence databases in FASTA format for use with the stand-alone BLAST programs. These databases must be formatted using formatdb before they can be used with BLAST.",
-            "title": "FASTA BLAST Databases",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -156822,38 +156805,39 @@
                     "title": "Download FASTA BLAST Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/f52g-xt9u",
+            "issued": "2021-06-30",
+            "keyword": [
+                "computational biology",
+                "dataset"
+            ],
+            "landingPage": "ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA",
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
+            "title": "FASTA BLAST Databases"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfCLIA/clia.cfm",
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
-            "identifier": "c13343cf-eda1-425d-b346-6186c92e3992",
             "description": "This database contains the commercially marketed in vitro test systems categorized by the FDA since January 31, 2000, and tests categorized by the Centers for Disease Control and Prevention (CDC) prior to that date.",
-            "title": "Clinical Laboratory Improvement Amendments",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -156861,43 +156845,35 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "c13343cf-eda1-425d-b346-6186c92e3992",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfCLIA/clia.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-01",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Clinical Laboratory Improvement Amendments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/vmgc-uspy",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "all serogroups",
-                "meningococcal disease",
-                "nedss",
-                "netss",
-                "nndss",
-                "serogroup b",
-                "serogroups acwy",
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
-            "identifier": "https://data.cdc.gov/api/views/vmgc-uspy",
             "description": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -156920,43 +156896,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vmgc-uspy",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "all serogroups",
+                "meningococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "serogroup b",
+                "serogroups acwy",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/vmgc-uspy",
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
+            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ymbn-wcu8",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2017-09-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "keyword": [
-                "applications",
-                "child enrollment",
-                "chip",
-                "eligibility determinations",
-                "enrollment",
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
-            "identifier": "6165f45b-ca93-5bb5-9d06-db29c692a360",
             "description": "All states (including the District of Columbia) are required to provide data to The Centers for Medicare & Medicaid Services (CMS) on a range of Medicaid and Children\u2019s Health Insurance Program (CHIP) indicators related to key application, eligibility, enrollment and call center processes. These data reflect enrollment activity for all populations receiving comprehensive Medicaid and CHIP benefits in all states, as well as state program performance.<br/>\r\nStates submit this data via the Performance Indicator dataset. Further information about this dataset is available at:  <a href=\"https://www.medicaid.gov/medicaid/national-medicaid-chip-program-information/medicaid-chip-enrollment-data/performance-indicator-technical-assistance/index.html\">https://www.medicaid.gov/medicaid/national-medicaid-chip-program-information/medicaid-chip-enrollment-data/performance-indicator-technical-assistance/index.html</a>.",
-            "title": "State Medicaid and CHIP Applications, Eligibility Determinations, and Enrollment Data",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -156964,40 +156944,43 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "6165f45b-ca93-5bb5-9d06-db29c692a360",
+            "issued": "2017-09-08",
+            "keyword": [
+                "applications",
+                "child enrollment",
+                "chip",
+                "eligibility determinations",
+                "enrollment",
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/ymbn-wcu8",
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
             "theme": [
                 "Enrollment"
-            ]
+            ],
+            "title": "State Medicaid and CHIP Applications, Eligibility Determinations, and Enrollment Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bptw-uw4i",
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
-            "identifier": "https://data.cdc.gov/api/views/bptw-uw4i",
             "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 2 - New York",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157020,42 +157003,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bptw-uw4i",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bptw-uw4i",
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
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 2 - New York"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ypj4-jmx6",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-08-10",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-17",
-            "keyword": [
-                "individual",
-                "individual market dental",
-                "py2022",
-                "qhp landscape instructions",
-                "sadp"
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
-            "identifier": "5fce65a2-11d2-493d-9c68-f576d09d0ce1",
             "description": "The Dental Individual Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to consumers in the individual market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2022 Individual Dental",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157063,37 +157044,38 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "5fce65a2-11d2-493d-9c68-f576d09d0ce1",
+            "issued": "2022-08-10",
+            "keyword": [
+                "individual",
+                "individual market dental",
+                "py2022",
+                "qhp landscape instructions",
+                "sadp"
+            ],
+            "landingPage": "https://healthdata.gov/d/ypj4-jmx6",
+            "modified": "2022-08-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2022 Individual Dental"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/geo/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "dataset",
-                "genomics",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/6m2g-frjb",
             "description": "GEO (Gene Expression Omnibus) is a public functional genomics data repository supporting MIAME-compliant data submissions. There are also tools provided to help users query and download experiments and curated gene expression profiles.",
-            "title": "GEO (Gene Expression Omnibus)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157108,42 +157090,41 @@
                     "title": "Download GEO (Gene Expression Omnibus) Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/6m2g-frjb",
+            "issued": "2021-06-30",
+            "keyword": [
+                "dataset",
+                "genomics",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/geo/",
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
+            "title": "GEO (Gene Expression Omnibus)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/275g-9x8h",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-02-08",
-            "@type": "dcat:Dataset",
-            "temporal": "2021-10-01/2023-11-10",
-            "modified": "2025-01-14",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "otc",
-                "self-tests"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jasmine Chaitram",
                 "hasEmail": "mailto:zoa6@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/275g-9x8h",
             "description": "This dataset includes COVID-19 self-test result data voluntarily reported by users of tests through manufacturer websites and mobile companion applications. At this time, the dataset does not include data reported through the MakeMyTestCount website. All fields are self-reported by the user voluntarily reporting the test result. This dataset will be updated monthly.\n\nPlease note that there are limitations with these data, including:\n1.\tData are not comprehensive of all self-tests performed. Data represent results voluntarily reported by an individual via manufacturer-provided website or companion mobile applications. Not all self-test manufacturers are currently capturing and sending data to CDC. Similarly, these data do not include self-test results that were reported to state and local health departments if they were not also reported through the manufacturer-provided website or companion mobile applications. The true denominator (number of tests completed) cannot be ascertained, but based on manufacturer production numbers, this dataset reflects a small fraction of the number of self-tests used.   \n\n2.\tData are not verified. The quality of specimen, appropriate execution of self-test, result produced, and person tested are unverified; therefore, reported interpretation of results cannot be confirmed. All results and accompanying demographic information are also self-reported and cannot be verified. \n\n3.\tData reports are not complete. Manufacturer-provided websites and companion mobile applications vary widely in terms of the data elements collected. Not all data elements are required, and many results are missing demographic information. \n\n4.\tData are not representative. Based on the limited number of self-reported test results, this dataset is not representative of the use of self-testing by demographic, nor is the dataset inclusive of all self-testing completed within each jurisdiction. This dataset represents a small proportion of overall COVID-19 testing conducted in each jurisdiction and reported volumes are much lower than testing conducted in point of care and laboratory settings.  \n\n5.\tData represent individual test results, not persons tested. Data in this dataset are not linkable and do not allow for analyses around serial testing. Data also cannot be disaggregated to identify multiple reports by the same individual. \n\nAll analyses should be completed with these limitations in mind.\n\nFor more information about the challenges and opportunities around self-test data, please refer to the following article: Ritchey MD, Rosenblum HG, Del Guercio K, et al. COVID-19 Self-Test Data: Challenges and Opportunities \u2014 United States, October 31, 2021\u2013June 11, 2022. MMWR Morb Mortal Wkly Rep 2022;71:1005\u20131010. DOI: http://dx.doi.org/10.15585/mmwr.mm7132a1",
-            "title": "U.S. COVID-19 Self-Test Data",
-            "programCode": [
-                "009:038"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157166,54 +157147,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/275g-9x8h",
+            "issued": "2023-02-08",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "otc",
+                "self-tests"
+            ],
+            "landingPage": "https://data.cdc.gov/d/275g-9x8h",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2025-01-14",
+            "programCode": [
+                "009:038"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
+            "temporal": "2021-10-01/2023-11-10",
             "theme": [
                 "Public Health Surveillance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "U.S. COVID-19 Self-Test Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-05-25",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-12-29/2023-07-29",
-            "modified": "2023-09-27",
-            "keyword": [
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "social vulnerability index",
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
-            "identifier": "https://data.cdc.gov/api/views/9hdi-ekmb",
             "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nDeaths involving COVID-19 reported to NCHS by week and county Social Vulnerability Index (SVI) in the United States. SVI scores are from CDC/ASTDR's Geospatial Research, Analysis & Service Program 2018 database. These scores range from 0 to 1, and categorized as low (0-0.333), moderate (0.334-0.666) or high (0.667-1).\n\nMore information on SVI can be found here: https://www.atsdr.cdc.gov/placeandhealth/svi/index.html",
-            "title": "Provisional COVID-19 Deaths by Week and County Social Vulnerability Index",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157236,46 +157210,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/9hdi-ekmb",
+            "issued": "2021-05-25",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "social vulnerability index",
+                "united states",
+                "weekly"
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
+            "spatial": "United States",
+            "temporal": "2019-12-29/2023-07-29",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional COVID-19 Deaths by Week and County Social Vulnerability Index"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/i4eq-dgfc",
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
-                "vibriosis confirmed",
-                "vibriosis probable",
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
-            "identifier": "https://data.cdc.gov/api/views/i4eq-dgfc",
             "description": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157298,43 +157276,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/i4eq-dgfc",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "vibriosis confirmed",
+                "vibriosis probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/i4eq-dgfc",
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
+            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/healthyyouth/about/index.htm",
             "bureauCode": [
                 "009:20"
             ],
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
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DASH Publc Inquiries",
                 "hasEmail": "mailto:nccdDashInfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/pxpe-pgrg",
+            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Global-School-based-Student-Health-Survey-GSH/pxpe-pgrg",
             "description": "2003-2015. Global School dataset.  The Global School-based Student Health Survey (GSHS) was developed by the World Health Organization (WHO) in collaboration with the United Nations' UNICEF, UNESCO, and UNAIDS; and with technical assistance from CDC.  The GSHS is a school-based survey conducted primarily among students aged 13-17 years in countries around the world.  It uses core questionnaire modules that address the leading causes of morbidity and mortality among children and adults worldwide: 1) Alcohol use, 2) dietary behaviors, 3) drug use, 4) hygiene, 5) mental health, 6) physical activity, 7) protective factors, 8) sexual behaviors that contribute to HIV infection, other sexually-transmitted infections, and unintended pregnancy, 9) tobacco use, and 10) violence and unintentional injury.  This dataset contains global data from 2003 \u2013 2015.  Additional information about the GSHS can be found at https://www.cdc.gov/gshs/index.htm.",
-            "title": "DASH - Global School-based Student Health Survey (GSHS)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157357,47 +157337,43 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Global-School-based-Student-Health-Survey-GSH/pxpe-pgrg",
+            "identifier": "https://data.cdc.gov/api/views/pxpe-pgrg",
+            "issued": "2023-07-18",
+            "keyword": [
+                "global",
+                "gshs",
+                "risk behavior",
+                "student health",
+                "survey",
+                "youth online"
+            ],
+            "landingPage": "https://www.cdc.gov/healthyyouth/about/index.htm",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-08-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Youth Risk Behaviors"
-            ]
+            ],
+            "title": "DASH - Global School-based Student Health Survey (GSHS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ppmd-3u54",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-            "identifier": "https://data.cdc.gov/api/views/ppmd-3u54",
             "description": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers\". NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
-            "title": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157420,38 +157396,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ppmd-3u54",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "crimean-congo hemorrhagic fever virus",
+                "ebola virus",
+                "guanarito virus",
+                "nedss",
+                "netss",
+                "nndss",
+                "viral hemorrhagic fevers",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ppmd-3u54",
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
+            "title": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/yt5k-6i8y",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-02-22",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-21",
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
-            "identifier": "17022a65-b21b-45ae-8224-3cee48c42ef3",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-13-to-2023-02-19",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157460,40 +157445,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-13-to-2023-02-19"
                 }
             ],
+            "identifier": "17022a65-b21b-45ae-8224-3cee48c42ef3",
+            "issued": "2023-02-22",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/yt5k-6i8y",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-02-21",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-13-to-2023-02-19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-visualization/potentially-excess-deaths/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2017-01-19",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-30",
-            "keyword": [
-                "cancer",
-                "chronic lower respiratory disease",
-                "heart disease",
-                "stroke",
-                "unintentional injury"
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
-            "identifier": "https://data.cdc.gov/api/views/vdpk-qzpr",
             "description": "MMWR Surveillance Summary 66 (No. SS-1):1-8 found that nonmetropolitan areas have significant numbers of potentially excess deaths from the five leading causes of death. These figures accompany this report by presenting information on potentially excess deaths in nonmetropolitan and metropolitan areas at the state level. They also add additional years of data and options for selecting different age ranges and benchmarks.\r\n\r\nPotentially excess deaths are defined in MMWR Surveillance Summary 66(No. SS-1):1-8 as deaths that exceed the numbers that would be expected if the death rates of states with the lowest rates (benchmarks) occurred across all states. They are calculated by subtracting expected deaths for specific benchmarks from observed deaths.\r\n\r\nNot all potentially excess deaths can be prevented; some areas might have characteristics that predispose them to higher rates of death. However, many potentially excess deaths might represent deaths that could be prevented through improved public health programs that support healthier behaviors and neighborhoods or better access to health care services.\r\n\r\nMortality data for U.S. residents come from the National Vital Statistics System. Estimates based on fewer than 10 observed deaths are not shown and shaded yellow on the map.\r\n\r\nUnderlying cause of death is based on the International Classification of Diseases, 10th Revision (ICD-10)\r\n\r\nHeart disease (I00-I09, I11, I13, and I20\u2013I51)\r\nCancer (C00\u2013C97)\r\nUnintentional injury (V01\u2013X59 and Y85\u2013Y86)\r\nChronic lower respiratory disease (J40\u2013J47)\r\nStroke (I60\u2013I69)\r\nLocality (nonmetropolitan vs. metropolitan) is based on the Office of Management and Budget\u2019s 2013 county-based classification scheme.\r\n\r\nBenchmarks are based on the three states with the lowest age and cause-specific mortality rates.\r\n\r\nPotentially excess deaths for each state are calculated by subtracting deaths at the benchmark rates (expected deaths) from observed deaths.\r\n\r\nUsers can explore three benchmarks:\r\n\r\n\u201c2010 Fixed\u201d is a fixed benchmark based on the best performing States in 2010.\r\n\u201c2005 Fixed\u201d is a fixed benchmark based on the best performing States in 2005.\r\n\u201cFloating\u201d is based on the best performing States in each year so change from year to year.\r\n \r\nSOURCES\r\n\r\nCDC/NCHS, National Vital Statistics System, mortality data (see http://www.cdc.gov/nchs/deaths.htm); and CDC WONDER (see http://wonder.cdc.gov).\r\n\r\nREFERENCES \r\n\r\n1. Moy E, Garcia MC, Bastian B, Rossen LM, Ingram DD, Faul M, Massetti GM, Thomas CC, Hong Y, Yoon PW, Iademarco MF. Leading Causes of Death in Nonmetropolitan and Metropolitan Areas \u2013 United States, 1999-2014. MMWR Surveillance Summary 2017; 66(No. SS-1):1-8.\r\n\r\n2. Garcia MC, Faul M, Massetti G, Thomas CC, Hong Y, Bauer UE, Iademarco MF. Reducing Potentially Excess Deaths from the Five Leading Causes of Death in the Rural United States. MMWR Surveillance Summary 2017; 66(No. SS-2):1\u20137.",
-            "title": "NCHS - Potentially Excess Deaths from the Five Leading Causes of Death",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157516,35 +157496,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vdpk-qzpr",
+            "issued": "2017-01-19",
+            "keyword": [
+                "cancer",
+                "chronic lower respiratory disease",
+                "heart disease",
+                "stroke",
+                "unintentional injury"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/potentially-excess-deaths/",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-03-30",
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
+            "title": "NCHS - Potentially Excess Deaths from the Five Leading Causes of Death"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/3h4m-i8xf",
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
-            "identifier": "https://data.cdc.gov/api/views/3h4m-i8xf",
             "description": "Occupational exposure to 4,4\u2019-methylene diphenyl diisocyanate (MDI), the most widely used monomeric diisocyanate (dNCO), is associated with occupational asthma (OA) development. Recruitment of immune cells to the lung microenvironment via secreted chemokines by alveolar macrophages may plays important roles during asthma pathogenesis. Our prior studies identified MDI/MDI-GSH-exposure downregulates endogenous human/murine(hsa/mmu)-microRNA(miR)-206-3p, resulting in the activation of mmu/hsa-miR-206-3p-regulated signaling including KLF4-mediated signaling in M\u00d8s. The hsa-miR-206-3p-regulated signaling activation leading to induction of chemokines and chemotaxis activities of immune cells. However, the underlying molecular mechanism(s) by which MDI/ MDI in the form of MDI-GSH conjugate exposure downregulated endogenous hsa-miR-206-3p expression is unclear. Circular RNAs (circRNAs) play important roles in many different biological processes by targeting endogenous miRs, affecting protein translation and gene transcription in different cell types. The circRNA expression can be regulated via outside stimuli exposures; however, whether MDI-exposure influence circRNAs expression is unknown. Several circRNAs have been identified to regulate hsa-miR-206-3p levels through miR binding/targeting. We hypothesize that MDI-exposure induces endogenous circRNA(s) to regulate hsa-miR-206-3p in M\u00d8s. The first aim of this study was to identified candidate hsa-miR-206-3p-binding circRNA(s) that can be regulated by MDI/MDI-GSH regulated. The second aim of this study was to examine whether MDI/MDI-GSH regulated hsa-miR-206-3p-binding circRNA(s) can indeed regulate the endogenous hsa-miR-206-3p in M\u00d8s. After identified the roles of endogenous circRNA(s) in regulation of endogenous hsa-miR-206-3p after MDI/MDI-GSH-exposure, we investigated the roles of circRNAs in regulation of hsa-miR-206-3p-mediated M2 macrophage-associated markers and chemokines\u2019 expressions in relation to the exposure to MDI.",
-            "title": "Circular RNA hsa_circ_0008726 Targets the hsa-miR-206-3p/KLF4 Axis to Modulate 4,4\u2019-Methylene Diphenyl Diisocyanate-Glutathione Conjugate-Induced Chemokine Transcription in Macrophages",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157552,21 +157539,45 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/3h4m-i8xf",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/3h4m-i8xf",
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
+            "title": "Circular RNA hsa_circ_0008726 Targets the hsa-miR-206-3p/KLF4 Axis to Modulate 4,4\u2019-Methylene Diphenyl Diisocyanate-Glutathione Conjugate-Induced Chemokine Transcription in Macrophages"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "description": "This list is intended to alert consumers about Web sites that are or were illegally marketing unapproved, uncleared, or unauthorized products in relation to the 2009 H1N1 Flu Virus (sometimes referred to as the 'swine flu' virus).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/h1n1flu/FraudulentH1N1ProductsList2009.xml",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "8b366073-48df-4c87-9120-9878f4875373",
             "issued": "2021-02-25",
-            "temporal": "2009-01-01/2009-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "1900-01-01",
             "keyword": [
                 "community health",
                 "h1n1",
@@ -157578,64 +157589,32 @@
                 "recalls",
                 "safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FDA Enterprise Data Inventory",
-                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
-            },
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "1900-01-01",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "8b366073-48df-4c87-9120-9878f4875373",
-            "description": "This list is intended to alert consumers about Web sites that are or were illegally marketing unapproved, uncleared, or unauthorized products in relation to the 2009 H1N1 Flu Virus (sometimes referred to as the 'swine flu' virus).",
-            "title": "Fraudulent 2009 H1N1 Influenza Products",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/h1n1flu/FraudulentH1N1ProductsList2009.xml",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "irregular"
+            "temporal": "2009-01-01/2009-12-31",
+            "title": "Fraudulent 2009 H1N1 Influenza Products"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/adult-vaccination-coverage.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-09-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024, 2024-25",
-            "modified": "2025-01-29",
-            "keyword": [
-                "covid-19 vaccination",
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
-            "identifier": "https://data.cdc.gov/api/views/8yup-c35n",
             "description": "\u2022 Weekly COVID-19 Vaccination Coverage and Comparison among adults 18 Years and Older by Jurisdiction\n\n \u2022 Weekly estimates of COVID-19 vaccination coverage and intent for vaccination among adults are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/index.html).\n\n \u2022 Weekly comparisons to previous season should take into account differences between seasons in vaccine availability dates. 2023\u201324 COVID-19 vaccines were first available mid-September 2023, and 2024\u201325 COVID-19 vaccines were first available at the end of August 2024.\u202f",
-            "title": "Weekly Differences in Cumulative COVID-19 Vaccination Coverage and Comparison Between 2024\u201325 and 2023\u201324 Among Adults 18 Years, Overall, by Selected Demographics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157658,25 +157637,57 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/8yup-c35n",
+            "issued": "2024-09-26",
+            "keyword": [
+                "covid-19 vaccination",
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "nis-flu",
+                "vsd"
+            ],
+            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/adult-vaccination-coverage.html",
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
+            "temporal": "2023-2024, 2024-25",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Differences in Cumulative COVID-19 Vaccination Coverage and Comparison Between 2024\u201325 and 2023\u201324 Among Adults 18 Years, Overall, by Selected Demographics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225439.htm",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "description": "Contains data for FDA peanut product recalls since January 2009.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xls",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "identifier": "1fce6941-625f-4dac-ae3b-6664fcfeea6d",
             "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2010-10-01",
             "keyword": [
                 "community health",
                 "food",
@@ -157687,100 +157698,76 @@
                 "recalls",
                 "safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FDA Enterprise Data Inventory",
-                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
-            },
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225439.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2010-10-01",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "1fce6941-625f-4dac-ae3b-6664fcfeea6d",
-            "description": "Contains data for FDA peanut product recalls since January 2009.",
-            "title": "FDA Peanut Product Recalls",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xls",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "FDA Peanut Product Recalls"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/yunm-3wmu",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-06-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-11",
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
-            "identifier": "c3d4ec55-f9ea-5b76-9eba-93cc3664c1f1",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard measure_value v2.11.9 (impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/measure_value.csv",
-                    "description": "Scorecard measure_value v2.11.9 (impl)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard measure_value v2.11.9 (impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard measure_value v2.11.9 (impl)"
                 }
             ],
+            "identifier": "c3d4ec55-f9ea-5b76-9eba-93cc3664c1f1",
+            "issued": "2023-06-29",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/yunm-3wmu",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-11-11",
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
+            "title": "Scorecard measure_value v2.11.9 (impl)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xm7q-e7uu",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -157788,20 +157775,59 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xm7q-e7uu",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/xm7q-e7uu",
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
+            "title": "Applied force alters sensorineural and peripheral vascular function in an animal model of hand-arm vibration syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/pb4z-432k",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "NNDSS - Table I. infrequently reported notifiable diseases - 2015.  In this Table, provisional cases of selected infrequently reported notifiable diseases (<1,000 cases reported during the preceding year) are displayed.  Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in these tables are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnote:-: No reported cases    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year  2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. \ufffd\ufffd Calculated by summing the incidence counts for the current week, the 2 weeks preceding the current week, and the 2 weeks following the current week, for a total of 5 preceding years. The total sum of incident cases is then divided by 25 weeks. Additional information is available at http://wwwn.cdc.gov/nndss/document/5yearweeklyaverage.pdf. \ufffd\ufffd Data for the Arboviral disease, Chikungunya, and Hantavirus infection disease, non-Hantavirus Pulmonary Syndrome (HPS), will be displayed in this table after the CDC obtains Office of Management and Budget Paperwork Reduction Act approval to receive data for these conditions. ** Includes both neuroinvasive and nonneuroinvasive. Updated weekly from reports to the Division of Vector-Borne Infectious Diseases, National Center for Zoonotic, Vector-Borne, and Enteric Diseases (ArboNET Surveillance). Data for West Nile virus are available in Table II. \ufffd\ufffd\u0289\ufffd\ufffd Not reportable in all states. Data from states where the condition is not reportable are excluded from this table except starting in 2007 for the arboviral diseases, STD data, TB data, and influenza-associated pediatric mortality, and in 2003 for SARS-CoV. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.  \ufffd\ufffd\ufffd\ufffd Data for H. influenzae (all ages, all serotypes) are available in Table II. \ufffd\ufffd\ufffd\ufffd Updated weekly from reports to the Influenza Division, National Center for Immunization and Respiratory Diseases. Please refer to the MMWR publication for weekly updates to the footnote for this condition. *** Please refer to the MMWR publication for weekly updates to the footnote for this condition. \ufffd\ufffd\u0289\ufffd\u0289\ufffd\ufffd Data for meningococcal disease (all serogroups) are available in Table II. \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd Please refer to the MMWR publication for weekly updates to the footnote for this condition. \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd Updated weekly from reports to the Division of STD Prevention, National Center for HIV/AIDS, Viral Hepatitis, STD, and TB Prevention. **** Please refer to the MMWR publication for weekly updates to the footnote for this condition. See Table II for Dengue Hemorrhagic Fever.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pb4z-432k/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pb4z-432k/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pb4z-432k/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pb4z-432k/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/pb4z-432k",
             "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
             "keyword": [
                 "2015",
                 "anthrax",
@@ -157864,81 +157890,34 @@
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
-            "identifier": "https://data.cdc.gov/api/views/pb4z-432k",
-            "description": "NNDSS - Table I. infrequently reported notifiable diseases - 2015.  In this Table, provisional cases of selected infrequently reported notifiable diseases (<1,000 cases reported during the preceding year) are displayed.  Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in these tables are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnote:-: No reported cases    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year  2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. \ufffd\ufffd Calculated by summing the incidence counts for the current week, the 2 weeks preceding the current week, and the 2 weeks following the current week, for a total of 5 preceding years. The total sum of incident cases is then divided by 25 weeks. Additional information is available at http://wwwn.cdc.gov/nndss/document/5yearweeklyaverage.pdf. \ufffd\ufffd Data for the Arboviral disease, Chikungunya, and Hantavirus infection disease, non-Hantavirus Pulmonary Syndrome (HPS), will be displayed in this table after the CDC obtains Office of Management and Budget Paperwork Reduction Act approval to receive data for these conditions. ** Includes both neuroinvasive and nonneuroinvasive. Updated weekly from reports to the Division of Vector-Borne Infectious Diseases, National Center for Zoonotic, Vector-Borne, and Enteric Diseases (ArboNET Surveillance). Data for West Nile virus are available in Table II. \ufffd\ufffd\u0289\ufffd\ufffd Not reportable in all states. Data from states where the condition is not reportable are excluded from this table except starting in 2007 for the arboviral diseases, STD data, TB data, and influenza-associated pediatric mortality, and in 2003 for SARS-CoV. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.  \ufffd\ufffd\ufffd\ufffd Data for H. influenzae (all ages, all serotypes) are available in Table II. \ufffd\ufffd\ufffd\ufffd Updated weekly from reports to the Influenza Division, National Center for Immunization and Respiratory Diseases. Please refer to the MMWR publication for weekly updates to the footnote for this condition. *** Please refer to the MMWR publication for weekly updates to the footnote for this condition. \ufffd\ufffd\u0289\ufffd\u0289\ufffd\ufffd Data for meningococcal disease (all serogroups) are available in Table II. \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd Please refer to the MMWR publication for weekly updates to the footnote for this condition. \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd Updated weekly from reports to the Division of STD Prevention, National Center for HIV/AIDS, Viral Hepatitis, STD, and TB Prevention. **** Please refer to the MMWR publication for weekly updates to the footnote for this condition. See Table II for Dengue Hemorrhagic Fever.",
-            "title": "NNDSS - Table I. infrequently reported notifiable diseases",
+            "landingPage": "https://data.cdc.gov/d/pb4z-432k",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-01-07",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pb4z-432k/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pb4z-432k/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pb4z-432k/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pb4z-432k/rows.xml?accessType=DOWNLOAD",
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
-            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "public",
-            "issued": "2015-12-02",
-            "@type": "dcat:Dataset",
-            "temporal": "1990/2010",
-            "modified": "2022-03-29",
-            "keyword": [
-                "hispanic women",
-                "nchs",
-                "pregnancy rate",
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:births@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hdy7-e2a3",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "https://www.cdc.gov/nchs/data-visualization/natality-trends/index.htm",
-            "title": "NCHS - Pregnancy Rates, by Age for Hispanic Women: United States, 1990-2010",
-            "isPartOf": "NCHS - Pregnancy Rates, by Age for Hispanic Women: United States, 1990-2010",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157961,44 +157940,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/hdy7-e2a3",
+            "isPartOf": "NCHS - Pregnancy Rates, by Age for Hispanic Women: United States, 1990-2010",
+            "issued": "2015-12-02",
+            "keyword": [
+                "hispanic women",
+                "nchs",
+                "pregnancy rate",
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
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "rights": "public",
+            "spatial": "50 states and District of Columbia",
+            "temporal": "1990/2010",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - Pregnancy Rates, by Age for Hispanic Women: United States, 1990-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/9jbh-ypax",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-09-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "health services research",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/9jbh-ypax",
             "description": "Health Services Research Information Central (HSRIC) is a web portal and current awareness service of information on health services research. Alerts the communities to meetings, webinars, new web-born reports (analyses, statistics), datasets, and general news. Currently contains over 3,000 items.\n\nThis resource was retired on September 14, 2021 and is no longer updated.",
-            "title": "Health Services Research Information Central (HSRIC)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -158021,35 +158004,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/9jbh-ypax",
+            "issued": "2021-09-15",
+            "keyword": [
+                "health services research",
+                "public health"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/9jbh-ypax",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-05",
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
+            "title": "Health Services Research Information Central (HSRIC)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/aian-amjw",
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
-            "identifier": "https://data.cdc.gov/api/views/aian-amjw",
             "description": "Workers involved in oil exploration and production in the upstream petroleum industry are exposed to crude oil vapor (COV).  COV levels in the proximity of workers during production tank gauging and opening of thief hatches can exceed regulatory standards, and several deaths have occurred after opening thief hatches.  There is a paucity of information regarding the effects of COV inhalation in the lung.  To address these knowledge gaps, the present hazard identification study was one of six undertaken to investigate the effects of inhaled COV in a rat animal model.",
-            "title": "Biological effects of inhaled crude oil vapor. III. Pulmonary effects",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -158057,10 +158044,23 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/aian-amjw",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/aian-amjw",
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
+            "title": "Biological effects of inhaled crude oil vapor. III. Pulmonary effects"
         }
-    ]
+    ],
+    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
 }
```

### Changes from 9cd27cf to 31606f9
**Author:** Automated

**Date:** 2025-02-01 14:34:19+00:00

**Message:** Updated data: Sat Feb  1 14:34:19 UTC 2025

```diff
diff --git a/healthdata.json b/healthdata.json
index e749fd6..b017330 100644
--- a/healthdata.json
+++ b/healthdata.json
@@ -14822,9 +14822,9 @@
                 "age",
                 "cessation",
                 "cigar",
-                "cigar use",
                 "cigarette",
                 "cigarette use",
+                "cigar use",
                 "consumption",
                 "current",
                 "demographics",
@@ -21228,7 +21228,7 @@
             ],
             "issued": "2024-07-25",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
+            "modified": "2025-01-30",
             "references": [
                 "https://www.medicaid.gov/dq-atlas/welcome",
                 "https://www.mathematica.org/"
@@ -21256,8 +21256,8 @@
             "distribution": [
                 {
                     "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/brief.csv",
-                    "description": "{\"dataset\": \"brief\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250127_ETL_DEV/brief.csv",
+                    "description": "{\"dataset\": \"brief\", \"stage\": \"featAuto\", \"update_id\": \"20250127_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
                     "title": "brief csv file"
                 }
@@ -31916,8 +31916,8 @@
                 "cigarette",
                 "current",
                 "demographics",
-                "e-cigarette",
                 "ecigarette",
+                "e-cigarette",
                 "education",
                 "ethnicity",
                 "gender",
@@ -92319,7 +92319,7 @@
             ],
             "issued": "2022-06-29",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
+            "modified": "2025-01-31",
             "keyword": [
                 "education",
                 "training and instruction",
@@ -96096,7 +96096,7 @@
             "issued": "2021-12-22",
             "temporal": "2011-10-01/2024-12-31",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-16",
+            "modified": "2025-01-31",
             "references": [
                 "https://data.cms.gov/resources/provider-of-services-file-methodology"
             ],
@@ -96126,24 +96126,11 @@
                 "009:000"
             ],
             "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8ba0f9b4-9493-4aa0-9f82-44ea9468d1b5/data",
-                    "description": "latest",
-                    "@type": "dcat:Distribution",
-                    "title": "Provider of Services File - Hospital & Non-Hospital Facilities : 2024-12-01"
-                },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/6340dd38-9a31-40e8-867a-e1df02fc8890/other_data_Q4%202024.csv",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/b5fb8b31-8e6e-41d0-8d73-8da1e2185ee2/PQWB.POSQ.OTHER.DATA.DEC24.csv",
                     "mediaType": "text/csv",
-                    "title": "Provider of Services File - Hospital & Non-Hospital Facilities : 2024-12-01"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/40145204-c219-4a0e-8c9e-5fda313386e8/data",
-                    "mediaType": "text/html",
-                    "title": "Provider of Services File - Hospital & Non-Hospital Facilities : 2024-12-01"
+                    "title": "Provider of Services File - Hospital & Non-Hospital Facilities : 2024-12-02"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -121133,9 +121120,9 @@
             "keyword": [
                 "coronavirus",
                 "covid",
+                "covid-19",
                 "covid cases",
                 "covid deaths",
-                "covid-19",
                 "dialysis",
                 "hemodialysis",
                 "sars-cov-2"
@@ -153601,7 +153588,7 @@
             ]
         },
         {
-            "accessLevel": "public",
+            "accessLevel": "non-public",
             "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
             "bureauCode": [
                 "009:20"
@@ -153661,7 +153648,7 @@
             "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/National-Vital-Statistics-System-NVSS-National-Car/kztq-p2jf",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
             "theme": [
-                "Heart Disease & Stroke Prevention"
+                "Health"
             ]
         },
         {
@@ -156717,7 +156704,7 @@
             ],
             "issued": "2024-07-25",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
+            "modified": "2025-01-30",
             "references": [
                 "https://www.medicaid.gov/dq-atlas/welcome",
                 "https://www.mathematica.org/"
@@ -156745,8 +156732,8 @@
             "distribution": [
                 {
                     "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/briefType.csv",
-                    "description": "{\"dataset\": \"briefType\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250127_ETL_DEV/briefType.csv",
+                    "description": "{\"dataset\": \"briefType\", \"stage\": \"featAuto\", \"update_id\": \"20250127_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
                     "title": "briefType csv file"
                 }
```

### Changes from 29aa757 to 9cd27cf
**Author:** Automated

**Date:** 2025-01-31 22:10:57+00:00

**Message:** Updated data: Fri Jan 31 22:10:57 UTC 2025

```diff
diff --git a/healthdata.json b/healthdata.json
index 38008bd..e749fd6 100644
--- a/healthdata.json
+++ b/healthdata.json
@@ -130036,8 +130036,8 @@
             "@type": "dcat:Dataset",
             "modified": "2025-01-31",
             "keyword": [
-                "vital statistics  us births and deaths",
-                "population statistics"
+                "population statistics",
+                "vital statistics  us births and deaths"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
```

### Changes from acf49f0 to 29aa757
**Author:** Automated

**Date:** 2025-01-31 20:10:42+00:00

**Message:** Updated data: Fri Jan 31 20:10:42 UTC 2025

```diff
diff --git a/healthdata.json b/healthdata.json
index 15eb41d..38008bd 100644
--- a/healthdata.json
+++ b/healthdata.json
@@ -130027,17 +130027,17 @@
         },
         {
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/national-death-index",
+            "landingPage": "https://www.cdc.gov/nchs/ndi/index.html",
             "bureauCode": [
                 "009:20"
             ],
             "issued": "2015-02-22",
             "temporal": "1979-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
             "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
+            "modified": "2025-01-31",
             "keyword": [
-                "population statistics",
-                "vital statistics  us births and deaths"
+                "vital statistics  us births and deaths",
+                "population statistics"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
```

### Changes from 761a84b to acf49f0 (Part 1/12)
**Author:** Automated

**Date:** 2025-01-31 15:36:25+00:00

**Message:** Updated data: Fri Jan 31 15:36:25 UTC 2025

```diff
diff --git a/healthdata.json b/healthdata.json
index e2ed06c..15eb41d 100644
--- a/healthdata.json
+++ b/healthdata.json
@@ -5,5 +5,158075 @@
     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
     "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
     "dataset": [
```

