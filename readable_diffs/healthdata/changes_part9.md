# Change History for healthdata.json (Part 9)

### Changes from 31606f9 to dd2190f (Part 8/11)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "landingPage": "https://healthdata.gov/d/n6ia-x2vv",
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
                 "Uncategorized"
-            ]
+            ],
+            "title": "Number and rate of SMM among Medicaid- and CHIP-covered deliveries, 2017 - 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/8396-v7yb",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-09-21",
-            "@type": "dcat:Dataset",
-            "temporal": "2021-08-16/2022-10-19",
-            "modified": "2025-01-13",
-            "references": [
-                "https://data.cdc.gov/Public-Health-Surveillance/United-States-County-Level-of-Community-Transmissi/nra9-vzzn"
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
-            "identifier": "https://data.cdc.gov/api/views/8396-v7yb",
             "description": "On October 20, 2022, CDC began retrieving aggregate case and death data from jurisdictional and state partners weekly instead of daily. This dataset contains archived community transmission and related data elements by county as originally displayed on the COVID Data Tracker. Although these data will continue to be publicly available, this dataset has not been updated since October 20, 2022. An archived dataset containing weekly community transmission data by county as originally posted can also be found here: <a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/dt66-w6m6\">Weekly COVID-19 County Level of Community Transmission as Originally Posted | Data | Centers for Disease Control and Prevention (cdc.gov)</a>. \n\n<b>Related data</b>\nCDC has been providing the public with two versions of COVID-19 county-level community transmission level data: this dataset with the daily values as originally posted on the COVID Data Tracker, and an historical dataset with daily data as well as the updates and corrections from state and local health departments. Similar to this dataset, the <a href=\"https://data.cdc.gov/Public-Health-Surveillance/United-States-COVID-19-County-Level-of-Community-T/nra9-vzzn\">original historical dataset</a> is archived on 10/20/2022. It will continue to be publicly available but will no longer be updated. A new dataset containing historical community transmission data by county is now published weekly and can be found at: <a href=\"https://data.cdc.gov/dataset/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn\">Weekly COVID-19 County Level of Community Transmission Historical Changes | Data | Centers for Disease Control and Prevention (cdc.gov)</a>.\n\nThis public use dataset has 7 data elements reflecting community transmission levels for all available counties and jurisdictions. It contains reported daily transmission levels at the county level with the same values used to display transmission maps on the COVID Data Tracker. Each day, the dataset is appended to contain the most recent day's data. Transmission level is set to low, moderate, substantial, or high using the calculation rules below.\n\n<b>Methods for calculating county level of community transmission indicator</b>\nThe County Level of Community Transmission indicator uses two metrics: (1) total new COVID-19 cases per 100,000 persons in the last 7 days and (2) percentage of positive SARS-CoV-2 diagnostic nucleic acid amplification tests (NAAT) in the last 7 days. For each of these metrics, CDC classifies transmission values as low, moderate, substantial, or high (below and <a href=\"https://www.cdc.gov/mmwr/volumes/70/wr/mm7030e2.htm?s_cid=mm7030e2_w#T1_down\">here</a>). If the values for each of these two metrics differ (e.g., one indicates moderate and the other low), then the higher of the two should be used for decision-making.\n\n<b>CDC core metrics of and thresholds for community transmission levels of SARS-CoV-2</b>\n\n<b>Total New Case Rate Metric:</b> \"New cases per 100,000 persons in the past 7 days\" is calculated by adding the number of new cases in the county (or other administrative level) in the last 7 days divided by the population in the county (or other administrative level) and multiplying by 100,000. \"New cases per 100,000 persons in the past 7 days\" is considered to have a transmission level of Low (0-9.99); Moderate (10.00-49.99); Substantial (50.00-99.99); and High (greater than or equal to 100.00).\n\n<b>Test Percent Positivity Metric:</b> \"Percentage of positive NAAT in the past 7 days\" is calculated by dividing the number of positive tests in the county (or other administrative level) during the last 7 days by the total number of tests conducted over the last 7 days. \"Percentage of positive NAAT in the past 7 days\" is considered to have a transmission level of Low (less than 5.00); Moderate (5.00-7.99); Substantial (8.00-9.99); and High (greater than or equal to 10.00).\n\nIf",
-            "title": "United States COVID-19 County Level of Community Transmission as Originally Posted - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106823,77 +106799,77 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/8396-v7yb",
+            "issued": "2021-09-21",
+            "keyword": [
+                "case",
+                "community transmission",
+                "coronavirus",
+                "county",
+                "covid-19",
+                "laboratory"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8396-v7yb",
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
+                "https://data.cdc.gov/Public-Health-Surveillance/United-States-County-Level-of-Community-Transmissi/nra9-vzzn"
+            ],
+            "spatial": "US",
+            "temporal": "2021-08-16/2022-10-19",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "United States COVID-19 County Level of Community Transmission as Originally Posted - ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:25"
             ],
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/hw99-m8wb",
-            "issued": "2024-03-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-14",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/hw99-m8wb",
             "description": "This portal systematically collects information about planned strategies and activities, monitors beta testing progress, and reports and communicates the expected outcomes to stakeholders.",
-            "title": "Dataset Catalog Performance and Evaluation Portal",
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/hw99-m8wb",
+            "issued": "2024-03-18",
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/hw99-m8wb",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-14",
             "programCode": [
                 "009:041"
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
             "theme": [
                 "Research"
-            ]
+            ],
+            "title": "Dataset Catalog Performance and Evaluation Portal"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9qys-crt2",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "all serogroups",
-                "meningococcal disease",
-                "mumps",
-                "nedss",
-                "netss",
-                "nndss",
-                "pertussis",
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
-            "identifier": "https://data.cdc.gov/api/views/9qys-crt2",
             "description": "NNDSS - Table II. Meningococcal disease to Pertussis - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\r\n \r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Meningococcal disease to Pertussis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106916,48 +106892,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9qys-crt2",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "all serogroups",
+                "meningococcal disease",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "pertussis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9qys-crt2",
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
+            "title": "NNDSS - Table II. Meningococcal disease to Pertussis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/provisional-drug-overdose.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-08-10",
-            "@type": "dcat:Dataset",
-            "temporal": "2018-12-01/2020-12-31",
-            "modified": "2023-04-03",
-            "keyword": [
-                "all causes",
-                "deaths",
-                "drug overdose",
-                "monthly",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "united states",
-                "urbanicity"
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
-            "identifier": "https://data.cdc.gov/api/views/dtm2-meqi",
             "description": "National provisional drug overdose deaths by month and 2013 NCHS Urban\u2013Rural Classification Scheme for Counties. Drug overdose deaths are identified using underlying cause-of-death codes from the Tenth Revision of ICD (ICD\u201310): X40\u2013X44 (unintentional), X60\u2013X64 (suicide), X85 (homicide), and Y10\u2013Y14 (undetermined). Deaths are based on the county of residence in the United States. Death counts provided are for \u201c12-month ending periods,\u201d defined as the number of deaths occurring in the 12-month period ending in the month indicated. Estimates for 2020 are based on provisional data. Estimates for 2018 and 2019 are based on final data.\n\nFor more information on NCHS urban-rural classification, see: https://www.cdc.gov/nchs/data/series/sr_02/sr02_166.pdf",
-            "title": "Provisional Drug Overdose Deaths by Urban/Rural Classification Scheme for 12 month-ending December 2018-December 2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106980,48 +106955,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/dtm2-meqi",
+            "issued": "2021-08-10",
+            "keyword": [
+                "all causes",
+                "deaths",
+                "drug overdose",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "united states",
+                "urbanicity"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/provisional-drug-overdose.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-04-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2018-12-01/2020-12-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional Drug Overdose Deaths by Urban/Rural Classification Scheme for 12 month-ending December 2018-December 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/3bix-jq57",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-            "identifier": "https://data.cdc.gov/api/views/3bix-jq57",
             "description": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers'. NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
-            "title": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107044,20 +107020,57 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/3bix-jq57",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/3bix-jq57",
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
+            "title": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus"
         },
         {
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:30"
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), analyze general treatment services trends, and generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment, substance abuse therapy and counseling, testing, transitional, and ancillary), primary focus (substance abuse, mental health, both, general health, other), hotline operation, Opioid Treatment Programs and medication dispensed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2000) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2000-nid13616",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2000-nid13616"
+                }
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2000",
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2000-nid13616",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -107070,98 +107083,66 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2000",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2000-nid13616",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), analyze general treatment services trends, and generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment, substance abuse therapy and counseling, testing, transitional, and ancillary), primary focus (substance abuse, mental health, both, general health, other), hotline operation, Opioid Treatment Programs and medication dispensed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2000)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2000-nid13616",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2000) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2000-nid13616"
-                }
-            ]
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2000)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nimhgenetics.org/",
             "bureauCode": [
                 "009:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Senthil, Geetha",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The NIMH Repository and Genomics Resource (RGR) stores biosamples, genetic, pedigree and clinical data collected in designated NIMH-funded human subject studies. The RGR database likewise links to other repositories holding data from the same subjects, including dbGAP, GEO and NDAR. The NIMH RGR allows the broader research community to access these data and biospecimens (e.g., lymphoblastoid cell lines, induced pluripotent cell lines, fibroblasts) and further expand the genetic and molecular characterization of patient populations with severe mental illness.</p>",
+            "identifier": "40058e12-63d7-4c6c-94e0-732304267311",
             "issued": "2016-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "mental health",
                 "mental illness",
                 "severe mental illness",
                 "smi"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Senthil, Geetha",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://www.nimhgenetics.org/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:060"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Institutes of Health (NIH)"
             },
-            "identifier": "40058e12-63d7-4c6c-94e0-732304267311",
-            "description": "<p>The NIMH Repository and Genomics Resource (RGR) stores biosamples, genetic, pedigree and clinical data collected in designated NIMH-funded human subject studies. The RGR database likewise links to other repositories holding data from the same subjects, including dbGAP, GEO and NDAR. The NIMH RGR allows the broader research community to access these data and biospecimens (e.g., lymphoblastoid cell lines, induced pluripotent cell lines, fibroblasts) and further expand the genetic and molecular characterization of patient populations with severe mental illness.</p>",
-            "title": "NIMH Repository and Genomics Resources (RGR)",
-            "programCode": [
-                "009:060"
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "NIMH Repository and Genomics Resources (RGR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/nb74-cu37",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "py2025",
-                "qhp",
-                "qhp landscape",
-                "shop",
-                "shop market medical"
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
-            "identifier": "2ffb5a20-8b08-48cb-b0ba-115de4381ca1",
             "description": "The Medical SHOP Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2025 Medical SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107169,32 +107150,38 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "2ffb5a20-8b08-48cb-b0ba-115de4381ca1",
+            "issued": "2024-12-10",
+            "keyword": [
+                "py2025",
+                "qhp",
+                "qhp landscape",
+                "shop",
+                "shop market medical"
+            ],
+            "landingPage": "https://healthdata.gov/d/nb74-cu37",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2025 Medical SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/yp23-fq9k",
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
-            "identifier": "https://data.cdc.gov/api/views/yp23-fq9k",
             "description": "SARS-CoV-2 spreads by infectious aerosols and droplets expelled from the respiratory tract. Masks and respirators can reduce the transmission of infectious respiratory diseases like SARS-CoV-2 by blocking these aerosols and droplets at the source. The ability of source control devices to block aerosols can be tested by expelling an aerosol through a headform wearing the device. These tests may be performed using constant airflows, which are simpler, or cyclic airflows, which are more realistic but require more complex methods. The purpose of these experiments was to compare the results found using constant vs. cyclic airflows.\n\nA source control measurement system was used to measure the efficacy of two cloth face masks, two medical masks with and without an elastic mask brace, a neck gaiter, and an N95 respirator as source control devices for simulated respiratory aerosols. With this system, the aerosol flows from the inside of the mask toward the outside; that is, the aerosol flows in the same direction as it would flow during an exhalation by a person wearing the source control device. The experiments were conducted under four airflow conditions: cyclic breathing at 15 liters/minute (L/min), cyclic breathing at 85 L/min, constant outward airflow at 15 L/min, and constant outward airflow at 85 L/min. Each experiment began by placing the source control device on the headform and performing a fit test. The measurement system collection chamber was then sealed, and the cyclic or constant airflow and the aerosol generation were initiated. The aerosol concentration in the collection chamber was measured using an optical particle spectrometer (OPS). The source control collection efficiency was determined by comparing the steady-state concentration of aerosol particles in the collection chamber when the source control device was worn with the concentration when no source control device was used.",
-            "title": "Constant vs. cyclic flow when testing face masks and respirators as source control devices for simulated respiratory aerosols",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107202,40 +107189,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/yp23-fq9k",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/yp23-fq9k",
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
+            "title": "Constant vs. cyclic flow when testing face masks and respirators as source control devices for simulated respiratory aerosols"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/proteinclusters",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-03-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/qmpj-ixje",
             "description": "A collection of Reference Sequence (RefSeq) proteins, from the complete genomes of prokaryotes, plasmids, and organelles, that have been grouped and annotated based on sequence similarity and protein function.",
-            "title": "Protein Clusters",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107244,114 +107226,119 @@
                     "title": "Protein Clusters"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/qmpj-ixje",
+            "issued": "2022-03-01",
+            "keyword": [
+                "dataset",
+                "protein",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/proteinclusters",
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
+            "title": "Protein Clusters"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/nd4h-apu9",
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
-            "identifier": "a462b2cc-d767-5975-8c8d-9e7493c3112d",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt pillar v2.10.6 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/pillar.csv",
-                    "description": "CoreSEt pillar v2.10.6 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt pillar v2.10.6 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt pillar v2.10.6 (coreset-etl-test)"
                 }
             ],
+            "identifier": "a462b2cc-d767-5975-8c8d-9e7493c3112d",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/nd4h-apu9",
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
+            "title": "CoreSEt pillar v2.10.6 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.peptideatlas.org/",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-07-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "national-institutes-of-health-nih"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "COULOMBE, JAMES N",
                 "hasEmail": "mailto:coulombej@mail.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "a6efb56e-35c5-4db5-9158-3f50f3b9fb9f",
+            "dataQuality": true,
             "description": "<p>PeptideAtlas is a multi-organism, publicly accessible compendium of peptides identified in a large set of tandem mass spectrometry proteomics experiments. Mass spectrometer output files are collected for human, mouse, yeast, and several other organisms, and searched using the latest search engines and protein sequences.</p>",
-            "title": "PeptideAtlas",
+            "identifier": "a6efb56e-35c5-4db5-9158-3f50f3b9fb9f",
+            "issued": "2016-07-15",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.peptideatlas.org/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:003"
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
+            "title": "PeptideAtlas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/gkpu-vawv",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division, Physical Effects Research Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/gkpu-vawv",
             "description": "According to the North American Industry Classification System, workers employed in the oil and gas extraction industry are working in one of three areas; 1) extraction, 2) drilling, or 3) processing and refinement (Bureau of Labor Statistics, April 15, 2014).  Both workers and people living in communities that are in close proximity to areas where gas and oil extraction and refinement occur have a higher incidence of respiratory, cardiovascular, digestive, reproductive and nervous system disorders,\n\nThe goal of these studies was to identify mechanisms underlying the development of cardiovascular disease after inhalation of crude oil vapors (COV). The oil used for this study was a surrogate of the crude oil that leaked into the Gulf of Mexico after the Deepwater Horizon oil spill (McKinney et al., 2021). We tested the hypothesis that changes in cardiovascular function after inhalation of COV are manifested as changes in the responsiveness of the heart and peripheral vascular system to vasoconstricting and vasodilating agonists.  Based on previous studies, we also predicted that inhalation of COV would affect the expression of biomarkers of cardiac and kidney function that are associated with blood pressure regulation and disease.",
-            "title": "Biological effects of crude oil vapor. IV. Cardiovascular effects-Dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107359,40 +107346,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/gkpu-vawv",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/gkpu-vawv",
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
+            "title": "Biological effects of crude oil vapor. IV. Cardiovascular effects-Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/nedq-yymp",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-09-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-25",
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
-            "identifier": "e85033c7-367e-467e-9e81-8e85048102b8",
             "description": "Performance rates on frequently reported health care quality measures in the CMS Medicaid/CHIP Child and Adult Core Sets, for FFY 2023 reporting.\r\n\r\nSource: Mathematica analysis of MACPro and Form CMS-416 reports for the FFY 2023 reporting cycle. Dataset revised September 2024. For more information, see the Children's Health Care Quality Measures and Adult Health Care Quality Measures webpages.",
-            "title": "2023 Child and Adult Health Care Quality Measures Quality",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107400,20 +107382,49 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "e85033c7-367e-467e-9e81-8e85048102b8",
+            "issued": "2024-09-26",
+            "keyword": [
+                "core sets",
+                "performance rates",
+                "quality measures"
+            ],
+            "landingPage": "https://healthdata.gov/d/nedq-yymp",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-09-25",
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
+            "title": "2023 Child and Adult Health Care Quality Measures Quality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/vtwh-8kxg",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "description": "Download the latest version of the Glossary and Methodology File",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/vtwh-8kxg/application/vnd.ms-excel",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/vtwh-8kxg",
             "issued": "2017-04-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-27",
             "keyword": [
                 "cigar",
                 "cigarette",
@@ -107426,67 +107437,33 @@
                 "smokeless",
                 "tobacco consumption"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "OSHData Support",
-                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/vtwh-8kxg",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-07-27",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/vtwh-8kxg",
-            "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "Adult Tobacco Consumption In The U. S. Glossary And Methodology",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/download/vtwh-8kxg/application/vnd.ms-excel",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
             "theme": [
                 "Policy"
-            ]
+            ],
+            "title": "Adult Tobacco Consumption In The U. S. Glossary And Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9g7x-sfq4",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-26",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-26",
-            "keyword": [
-                "2017",
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
-            "identifier": "https://data.cdc.gov/api/views/9g7x-sfq4",
             "description": "NNDSS - Table III. Tuberculosis - 2017.This Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States will exclude counts from US territories.  Footnote: C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Min: Minimum.    Max: Maximum. * Case counts for reporting year 2016 and 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf Data for TB are displayed quarterly.",
-            "title": "NNDSS - Table III. Tuberculosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107509,46 +107486,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9g7x-sfq4",
+            "issued": "2018-01-26",
+            "keyword": [
+                "2017",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "tb",
+                "tuberculosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9g7x-sfq4",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-01-26",
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
+            "title": "NNDSS - Table III. Tuberculosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/brfss/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-14",
-            "references": [
-                "https://www.cdc.gov/brfss/"
-            ],
-            "keyword": [
-                "behavioral",
-                "brfss",
-                "mmsa",
-                "risk",
-                "smart",
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
-            "identifier": "https://data.cdc.gov/api/views/j32a-sa6u",
+            "describedBy": "https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factors-Selected-Metropolitan-Area/j32a-sa6u",
             "description": "2011 to present. BRFSS SMART MMSA Prevalence combined land line and cell phone data. The Selected Metropolitan Area Risk Trends (SMART) project uses the Behavioral Risk Factor Surveillance System (BRFSS) to analyze the data of selected metropolitan statistical areas (MMSAs) with 500 or more respondents. BRFSS data can be used to identify emerging health problems, establish and track health objectives, and develop and evaluate public health policies and programs. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Data will be updated annually as it becomes available. Detailed information on sampling methodology and quality assurance can be found on the BRFSS website (http://www.cdc.gov/brfss). Methodology: http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf Glossary: https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct",
-            "title": "Behavioral Risk Factors: Selected Metropolitan Area Risk Trends (SMART) MMSA Prevalence Data (2011 to Present)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107571,22 +107548,58 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factors-Selected-Metropolitan-Area/j32a-sa6u",
+            "identifier": "https://data.cdc.gov/api/views/j32a-sa6u",
+            "issued": "2023-07-18",
+            "keyword": [
+                "behavioral",
+                "brfss",
+                "mmsa",
+                "risk",
+                "smart",
+                "survey"
+            ],
+            "landingPage": "https://www.cdc.gov/brfss/",
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
+                "https://www.cdc.gov/brfss/"
+            ],
             "theme": [
                 "Behavioral Risk Factors"
-            ]
+            ],
+            "title": "Behavioral Risk Factors: Selected Metropolitan Area Risk Trends (SMART) MMSA Prevalence Data (2011 to Present)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/aid-families-dependent-children-quality-control-review-panel-decisions",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.hhs.gov/dab/decisions/afdcquality/index.html",
+            "description": "<p>Decisions issued by the Aid to Families with Dependent Children (AFDC) Quality Control Review Panel of the Departmental Appeals Board concerning the AFDC program (predecessor of Temporary Aid for Needy Families) established by title IV-A of the Social Security Act.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.hhs.gov/dab/decisions/index.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "250fd232-5e43-4eef-a64a-3f05fa629921",
             "issued": "2012-05-30",
-            "temporal": "1991-08-09T00:00:00-04:00/1996-09-16T00:00:00-04:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "acf",
                 "administrative",
@@ -107664,72 +107677,35 @@
                 "welfare",
                 "withhold"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/aid-families-dependent-children-quality-control-review-panel-decisions",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:102"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "250fd232-5e43-4eef-a64a-3f05fa629921",
-            "description": "<p>Decisions issued by the Aid to Families with Dependent Children (AFDC) Quality Control Review Panel of the Departmental Appeals Board concerning the AFDC program (predecessor of Temporary Aid for Needy Families) established by title IV-A of the Social Security Act.</p>",
-            "title": "Aid to Families with Dependent Children Quality Control Review Panel Decisions",
-            "programCode": [
-                "009:102"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.hhs.gov/dab/decisions/index.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://www.hhs.gov/dab/decisions/afdcquality/index.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1991-08-09T00:00:00-04:00/1996-09-16T00:00:00-04:00",
             "theme": [
                 "Health",
                 "Quality"
-            ]
+            ],
+            "title": "Aid to Families with Dependent Children Quality Control Review Panel Decisions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7gnu-j6js",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "confirmed",
-                "leptospirosis",
-                "listeriosis",
-                "nedss",
-                "netss",
-                "nndss",
-                "probable",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.go"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7gnu-j6js",
             "description": "NNDSS - TABLE 1U. Leptospirosis to Listeriosis, Probable - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Beginning in 2020, confirmed and probable cases are published separately. Prior years included confirmed cases only.",
-            "title": "NNDSS - TABLE 1U. Leptospirosis to Listeriosis, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107752,44 +107728,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7gnu-j6js",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "confirmed",
+                "leptospirosis",
+                "listeriosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7gnu-j6js",
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
+            "title": "NNDSS - TABLE 1U. Leptospirosis to Listeriosis, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/u3yt-gdfa",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-18",
-            "keyword": [
-                "2018",
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
-            "identifier": "https://data.cdc.gov/api/views/u3yt-gdfa",
             "description": "NNDSS - Table III. Tuberculosis - 2018.This Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying WONDER data.  Data on United States will exclude counts from US territories. \r\n \r\nFootnote: C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Min: Minimum.    Max: Maximum. \r\n\r\n* Case counts for reporting year 2017 and 2018 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf \r\n\r\n\u2020 Data for TB are displayed quarterly.",
-            "title": "NNDSS - Table III. Tuberculosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107812,54 +107790,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/u3yt-gdfa",
+            "issued": "2019-01-18",
+            "keyword": [
+                "2018",
+                "nedss",
+                "netss",
+                "nndss",
+                "tb",
+                "tuberculosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/u3yt-gdfa",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-01-18",
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
+            "title": "NNDSS - Table III. Tuberculosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/oralhealth",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-26",
-            "references": [
-                "https://www.cdc.gov/oralhealthdata/"
-            ],
-            "keyword": [
-                "astdd",
-                "basic screening survey",
-                "bss",
-                "caries",
-                "caries experience",
-                "child",
-                "children",
-                "dental sealants",
-                "division of oral health",
-                "nohss",
-                "oral health",
-                "prevalence",
-                "tooth decay",
-                "untreated tooth decay"
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
-            "identifier": "https://data.cdc.gov/api/views/qcai-zfj9",
+            "describedBy": "https://chronicdata.cdc.gov/Oral-Health/NOHSS-Child-Indicators/qcai-zfj9",
             "description": "Data for School year-end 1994 through year-end 2020.  State oral health surveys are the data sources for these indicators. States periodically conduct independent screening surveys of a probability sample designed to be representative of all third-grade students in the state. Some states also conduct surveys of students in other grades in school, or of Head Start program enrollees. This surveillance activity is voluntary. States submit their data to the Association of State and Territorial Dental Directors (ASTDD), where the survey design and data collected are reviewed for quality and against the criteria for inclusion in NOHSS, before being sent to CDC for inclusion in Oral Health Data. For more information, see: http://www.cdc.gov/oralhealthdata/overview/childIndicators/",
-            "title": "NOHSS Child Indicators",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107882,47 +107851,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Oral-Health/NOHSS-Child-Indicators/qcai-zfj9",
+            "identifier": "https://data.cdc.gov/api/views/qcai-zfj9",
+            "issued": "2023-07-19",
+            "keyword": [
+                "astdd",
+                "basic screening survey",
+                "bss",
+                "caries",
+                "caries experience",
+                "child",
+                "children",
+                "dental sealants",
+                "division of oral health",
+                "nohss",
+                "oral health",
+                "prevalence",
+                "tooth decay",
+                "untreated tooth decay"
+            ],
+            "landingPage": "http://www.cdc.gov/oralhealth",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-09-26",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/oralhealthdata/"
+            ],
             "theme": [
                 "Oral Health"
-            ]
+            ],
+            "title": "NOHSS Child Indicators"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/cqcc-kwwr",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "nedss",
-                "netss",
-                "nndss",
-                "paralytic",
-                "pertussis",
-                "plague",
-                "poliomyelitis",
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
-            "identifier": "https://data.cdc.gov/api/views/cqcc-kwwr",
             "description": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107945,38 +107921,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cqcc-kwwr",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "paralytic",
+                "pertussis",
+                "plague",
+                "poliomyelitis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/cqcc-kwwr",
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
+            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/nhby-kr4i",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2020-06-12",
-            "@type": "dcat:Dataset",
-            "modified": "2021-10-29",
-            "keyword": [
-                "medicaid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Vaughn",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "b7cf4576-a930-59b4-86c8-c8685aaa5c2c",
             "description": "Dataset.",
-            "title": "2018 Managed Care Programs By State",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107985,37 +107970,35 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "b7cf4576-a930-59b4-86c8-c8685aaa5c2c",
+            "issued": "2020-06-12",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/nhby-kr4i",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2021-10-29",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "2018 Managed Care Programs By State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/26a7-nc4u",
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
-            "identifier": "https://data.cdc.gov/api/views/26a7-nc4u",
             "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2014 national data: National Occupant Protection Use Survey (NOPUS), 2014.  Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 state data: Seat Belt Use in 2014- Use Rates in the States and Territories",
-            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 5 - Chicago",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -108038,20 +108021,50 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/26a7-nc4u",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/26a7-nc4u",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 5 - Chicago"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1997",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1997) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1997-nid13526",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1997-nid13526"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1997-nid13526",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -108064,66 +108077,29 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1997",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1997-nid13526",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1997)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1997-nid13526",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1997) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1997-nid13526"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1997)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/axsa-zcg5",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/axsa-zcg5",
             "description": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus \u2013 2020.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers\". NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
-            "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -108146,46 +108122,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/axsa-zcg5",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "junin virus",
+                "lassa virus",
+                "lujo virus",
+                "nedss",
+                "netss",
+                "nndss",
+                "viral hemorrhagic fevers",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/axsa-zcg5",
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
+            "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ngaa-n8ir",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "botulism",
-                "foodborne",
-                "infant",
-                "nedss",
-                "netss",
-                "nndss",
-                "other (wound & unspecified)",
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
-            "identifier": "https://data.cdc.gov/api/views/ngaa-n8ir",
             "description": "NNDSS - Table 1E. Botulism, Foodborne to Botulism, Other (wound & unspecified) - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1E. Botulism, Foodborne to Botulism, Other (wound & unspecified)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -108208,144 +108184,147 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ngaa-n8ir",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "botulism",
+                "foodborne",
+                "infant",
+                "nedss",
+                "netss",
+                "nndss",
+                "other (wound & unspecified)",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ngaa-n8ir",
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
+            "title": "NNDSS - Table 1E. Botulism, Foodborne to Botulism, Other (wound & unspecified)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/nk45-zjqy",
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
-            "identifier": "cfc2c875-2278-5ef4-b7f3-75099ce8add9",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard state v2.11.9 (impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/state.csv",
-                    "description": "Scorecard state v2.11.9 (impl)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard state v2.11.9 (impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/state.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard state v2.11.9 (impl)"
                 }
             ],
+            "identifier": "cfc2c875-2278-5ef4-b7f3-75099ce8add9",
+            "issued": "2023-06-29",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/nk45-zjqy",
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
+            "title": "Scorecard state v2.11.9 (impl)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/nkkg-un7u",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-04-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-22",
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
-            "identifier": "1e34c475-7147-5318-838f-a31ed3fcff9b",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard TAG v0.2.4-1 (dev0)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.2.4-1/TAG.csv",
-                    "description": "Scorecard TAG v0.2.4-1 (dev0)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard TAG v0.2.4-1 (dev0)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.2.4-1/TAG.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard TAG v0.2.4-1 (dev0)"
                 }
             ],
+            "identifier": "1e34c475-7147-5318-838f-a31ed3fcff9b",
+            "issued": "2023-04-21",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/nkkg-un7u",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-05-22",
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
+            "title": "Scorecard TAG v0.2.4-1 (dev0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/quality-of-care/payroll-based-journal-daily-nurse-staffing",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2017-01-01/2024-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-31",
-            "references": [
-                "https://data.cms.gov/resources/payroll-based-journal-methodology-0"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "hospitals & facilities",
-                "medicare",
-                "original medicare",
-                "skilled nursing"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nursing Home Staffing - CCSQ (PBJ Reports)",
                 "hasEmail": "mailto:nhstaffing@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/7e0d53ba-8f02-4c66-98a5-14a1c997c50d/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/payroll-based-journal-daily-nurse-staffing-data-dictionary",
             "description": "The Payroll Based Journal (PBJ) Nurse Staffing and Non-Nurse Staffing datasets provide information submitted by nursing homes including rehabilitation services on a quarterly basis. The View Data link above includes the hours staff are paid to work each day, for each facility, aggregated by staff reporting category. \u00a0Examples of reporting categories include Director of Nursing, Administrative Registered Nurses, Registered Nursing, Administrative Licensed Practice Nurses, Licensed Practice Nurses, Certified Nurse Aides, Certified Medication Aides, and Nurse Aides in Training. There are also other non-nurse staff categories provided in the data such as Respiratory Therapist, Occupational Therapist, and Social Worker. The datasets also include a facility\u2019s daily census calculated using the Minimum Data Set (MDS) submission.\n\nThe Payroll Based Journal (PBJ) Employee Detail Nursing Home Staffing datasets and technical information have been moved to a new location.\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Payroll Based Journal Daily Nurse Staffing",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7e0d53ba-8f02-4c66-98a5-14a1c997c50d/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7e0d53ba-8f02-4c66-98a5-14a1c997c50d/data",
+                    "mediaType": "text/html",
                     "title": "Payroll Based Journal Daily Nurse Staffing : 2024-04-01"
                 },
                 {
@@ -108709,46 +108688,50 @@
                     "title": "Payroll Based Journal Daily Nurse Staffing : 2017-03-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/payroll-based-journal-daily-nurse-staffing-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/7e0d53ba-8f02-4c66-98a5-14a1c997c50d/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "hospitals & facilities",
+                "medicare",
+                "original medicare",
+                "skilled nursing"
+            ],
+            "landingPage": "https://data.cms.gov/quality-of-care/payroll-based-journal-daily-nurse-staffing",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-10-31",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/payroll-based-journal-methodology-0"
+            ],
+            "temporal": "2017-01-01/2024-06-30",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Payroll Based Journal Daily Nurse Staffing"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/nkx4-nm48",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2018-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-05",
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
-            "identifier": "c1028fdf-2e43-5d5e-990b-51ed03428625",
             "description": "Performance rates on frequently reported health care quality measures in the CMS Medicaid/CHIP Child and Adult Core Sets, for FFY 2017 reporting.  Source: Mathematica analysis of MACPro and Form CMS-416 reports for the FFY 2017 reporting cycle. For more information, see the <a href=\"https://www.medicaid.gov/medicaid/quality-of-care/performance-measurement/child-core-set/index.html\">Children's Health Care Quality Measures</a> and <a href=\"https://www.medicaid.gov/medicaid/quality-of-care/performance-measurement/adult-core-set/index.html\">Adult Health Care Quality Measures</a> webpages.",
-            "title": "2017 Child and Adult Health Care Quality Measures",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -108757,61 +108740,41 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "c1028fdf-2e43-5d5e-990b-51ed03428625",
+            "issued": "2018-08-08",
+            "keyword": [
+                "core sets",
+                "performance rates",
+                "quality measures"
+            ],
+            "landingPage": "https://healthdata.gov/d/nkx4-nm48",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2019-08-05",
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
+            "title": "2017 Child and Adult Health Care Quality Measures"
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
-            "identifier": "https://data.cdc.gov/api/views/vr6p-ert2",
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2007/vr6p-ert2",
             "description": "2007. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2007",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -108834,88 +108797,103 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2007/vr6p-ert2",
+            "identifier": "https://data.cdc.gov/api/views/vr6p-ert2",
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
+            "title": "CDC PRAMStat Data for 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/nmv8-h7tv",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-10-14",
-            "@type": "dcat:Dataset",
-            "modified": "2021-10-13",
-            "keyword": [
-                "drug products",
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
-            "identifier": "6b53cee3-300d-4779-b882-556d43ffe45b",
             "description": "The Table below, updated weekly, contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database. Each file on this table represents a snapshot of data in the system and is not updated by subsequent changes. Once the covered outpatient drugs in each of these files appear in the quarterly MDRP database, the file will be removed from this table. States can utilize these files to identify newly reported covered outpatient drugs.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "description": "https://data.medicaid.gov/sites/default/files/uploaded_resources/newly-reported-drugs-october-files.csv",
                     "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/newly-reported-drugs-october-files.csv",
-                    "mediaType": "text/csv",
-                    "description": "https://data.medicaid.gov/sites/default/files/uploaded_resources/newly-reported-drugs-october-files.csv"
+                    "mediaType": "text/csv"
                 }
             ],
+            "identifier": "6b53cee3-300d-4779-b882-556d43ffe45b",
+            "issued": "2021-10-14",
+            "keyword": [
+                "drug products",
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/nmv8-h7tv",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2021-10-13",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/3nnm-4jni",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-08-11",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-02-24 - 2023-05-10",
-            "modified": "2025-01-13",
-            "keyword": [
-                "cases",
-                "community levels",
-                "coronavirus",
-                "county",
-                "covid-19",
-                "hospital",
-                "united states"
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
-            "identifier": "https://data.cdc.gov/api/views/3nnm-4jni",
             "description": "Reporting of Aggregate Case and Death Count data was discontinued May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. Although these data will continue to be publicly available, this dataset will no longer be updated.\n\nThis archived public use dataset has 11 data elements reflecting United States COVID-19 community levels for all available counties. \n\nThe COVID-19 community levels were developed using a combination of three metrics \u2014 new COVID-19 admissions per 100,000 population in the past 7 days, the percent of staffed inpatient beds occupied by COVID-19 patients, and total new COVID-19 cases per 100,000 population in the past 7 days. The COVID-19 community level was determined by the higher of the new admissions and inpatient beds metrics, based on the current level of new cases per 100,000 population in the past 7 days. New COVID-19 admissions and the percent of staffed inpatient beds occupied represent the current potential for strain on the health system. Data on new cases acts as an early warning indicator of potential increases in health system strain in the event of a COVID-19 surge.\n\nUsing these data, the COVID-19 community level was classified as low, medium, or high.\n\nCOVID-19 Community Levels were used to help communities and individuals make decisions based on their local context and their unique needs. Community vaccination coverage and other local information, like early alerts from surveillance, such as through wastewater or the number of emergency department visits for COVID-19, when available, can also inform decision making for health officials and individuals.\n\nFor the most accurate and up-to-date data for any county or state, visit the relevant health department website. COVID Data Tracker may display data that differ from state and local websites. This can be due to differences in how data were collected, how metrics were calculated, or the timing of web updates.\n\n<b>Archived Data Notes:</b>\n\nThis dataset was renamed from \"United States COVID-19 Community Levels by County as Originally Posted\" to \"United States COVID-19 Community Levels by County\" on March 31, 2022. \n\n<b>March 31, 2022:</b> Column name for county population was changed to \u201ccounty_population\u201d. No change was made to the data points previous released.\n\n<b>March 31, 2022:</b> New column, \u201chealth_service_area_population\u201d, was added to the dataset to denote the total population in the designated Health Service Area based on 2019 Census estimate. \n\n<b>March 31, 2022:</b> FIPS codes for territories American Samoa, Guam, Commonwealth of the Northern Mariana Islands, and United States Virgin Islands were re-formatted to 5-digit numeric for records released on 3/3/2022 to be consistent with other records in the dataset.\n\n<b>March 31, 2022:</b> Changes were made to the text fields in variables \u201ccounty\u201d, \u201cstate\u201d, and \u201chealth_service_area\u201d so the formats are consistent across releases.\n\n<b>March 31, 2022:</b> The \u201c%\u201d sign was removed from the text field in column \u201ccovid_inpatient_bed_utilization\u201d. No change was made to the data. As indicated in the column description, values in this column represent the percentage of staffed inpatient beds occupied by COVID-19 patients (7-day average).  \n\n<b>March 31, 2022:</b> Data values for columns, \u201ccounty_population\u201d, \u201chealth_service_area_number\u201d, and \u201chealth_service_area\u201d were backfilled for records released on 2/24/2022. These columns were added since the week of 3/3/2022, thus the values were previously missing for records released the week prior.\n\n<b>April 7, 2022:</b> Updates made to data released on 3/24/2022 for Guam, Commonwealth of the Northern Mariana Islands, and United States Virgin Islands to correct a data mapping error.\n\n<b>April 21, 2022:</b> COVID-19 Community Level (CCL) data released for counties in Nebraska for the week of April 21, 2022 have 3 counties identified in the high category and 37 in the medium category. CDC has been working with state officials t",
-            "title": "United States COVID-19 Community Levels by County",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -108938,47 +108916,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/3nnm-4jni",
+            "issued": "2022-08-11",
+            "keyword": [
+                "cases",
+                "community levels",
+                "coronavirus",
+                "county",
+                "covid-19",
+                "hospital",
+                "united states"
+            ],
+            "landingPage": "https://data.cdc.gov/d/3nnm-4jni",
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
+            "spatial": "US",
+            "temporal": "2022-02-24 - 2023-05-10",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "United States COVID-19 Community Levels by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7mbm-jety",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "chlamydia trachomatis infection",
-                "coccidioidomycosis",
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
-            "identifier": "https://data.cdc.gov/api/views/7mbm-jety",
             "description": "NNDSS - Table II. Chlamydia to Coccidioidomycosis - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Chlamydia to Coccidioidomycosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109001,35 +108978,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7mbm-jety",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "chlamydia trachomatis infection",
+                "coccidioidomycosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7mbm-jety",
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
+            "title": "NNDSS - Table II. Chlamydia to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/9xt5-u42s",
-            "issued": "2024-02-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-23",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:healthus@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9xt5-u42s",
             "description": "List of footnotes, notes, and source information for Health, United States datasets. Each row of this dataset contains the accompanying text for a footnote found in a Health, United \nStates dataset. The footnote lookup can be merged onto any Health, United States dataset using FN_YEAR, HUS_SHORT_NAME, and FN_ID.\n\nSOURCE: CDC, National Center for Health Statistics, Health, United States",
-            "title": "DQS Health, United States Dataset Footnote Lookup",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109052,38 +109039,33 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/9xt5-u42s",
+            "issued": "2024-02-16",
+            "landingPage": "https://data.cdc.gov/d/9xt5-u42s",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-23",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "DQS Health, United States Dataset Footnote Lookup"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adult-coverage-vaccination.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-11",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-08-28",
-            "keyword": [
-                "adults",
-                "covid-19 vaccination",
-                "nis-acm"
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
-            "identifier": "https://data.cdc.gov/api/views/sjpm-fk4b",
             "description": "Weekly COVID-19 Vaccination Coverage of Adults 18 Years and Older by Jurisdiction\n\n\u2022 COVID-19 vaccination coverage among adults 18 years and older is assessed through the National Immunization Survey-Adult COVID Module, providing weekly COVID-19 vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine for adults ages 18 years and older.",
-            "title": "Weekly Cumulative Percentage of Adults 18 Years and Older Vaccinated with the Updated 2023-24 COVID-19 Vaccine by Jurisdiction",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109106,43 +109088,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/sjpm-fk4b",
+            "issued": "2023-12-11",
+            "keyword": [
+                "adults",
+                "covid-19 vaccination",
+                "nis-acm"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adult-coverage-vaccination.html",
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
+            "spatial": "United States- National, Region, State",
+            "temporal": "2023-2024",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Percentage of Adults 18 Years and Older Vaccinated with the Updated 2023-24 COVID-19 Vaccine by Jurisdiction"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfClia/analyteswaived.cfm",
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
-            "identifier": "3f3f0bb7-1c03-415a-90ca-400bfc08f096",
             "description": "This database contains the commercially marketed in vitro test systems categorized as CLIA waived by the FDA since January 31, 2000, and by the Centers for Disease Control and Prevention (CDC) prior to that date. CLIA waived test systems are waived from certain CLIA laboratory requirements (42 CFR Part 493).",
-            "title": "CLIA Currently Waived Analytes",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109150,82 +109134,81 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "3f3f0bb7-1c03-415a-90ca-400bfc08f096",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfClia/analyteswaived.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-01",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "CLIA Currently Waived Analytes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/nqqs-g5sn",
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
-            "identifier": "f93854eb-8150-515f-a05f-c318ed49af66",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt filters v2.10.6 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/filters.csv",
-                    "description": "CoreSEt filters v2.10.6 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt filters v2.10.6 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt filters v2.10.6 (coreset-etl-test)"
                 }
             ],
+            "identifier": "f93854eb-8150-515f-a05f-c318ed49af66",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/nqqs-g5sn",
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
+            "title": "CoreSEt filters v2.10.6 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/iz46-hpaa",
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
-            "identifier": "https://data.cdc.gov/api/views/iz46-hpaa",
             "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2014 national data: National Occupant Protection Use Survey (NOPUS), 2014.  Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 state data: Seat Belt Use in 2014- Use Rates in the States and Territories",
-            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 8 - Denver",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109248,53 +109231,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/iz46-hpaa",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/iz46-hpaa",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 8 - Denver"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-04-02",
-            "@type": "dcat:Dataset",
-            "temporal": "2019/2020",
-            "modified": "2022-04-01",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "influenza",
-                "mortality",
-                "nchs",
-                "pneumonia",
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
-            "identifier": "https://data.cdc.gov/api/views/hc4f-j6nb",
             "description": "This dataset is no longer updated.  Please see the following datasets for recent data:\n\nProvisional COVID-19 Deaths by Week (https://data.cdc.gov/dataset/Provisional-COVID-19-Death-Counts-by-Week-Ending-D/r8kw-7aab/)\n\nProvisional COVID-19 Deaths by Sex, Age, and State (https://data.cdc.gov/NCHS/Provisional-COVID-19-Death-Counts-by-Sex-Age-and-S/9bhg-hcku)",
-            "title": "Provisional Death Counts for Coronavirus Disease (COVID-19)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109317,43 +109287,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/hc4f-j6nb",
+            "issued": "2020-04-02",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "influenza",
+                "mortality",
+                "nchs",
+                "pneumonia",
+                "provisional",
+                "puerto rico",
+                "state",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
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
+            "spatial": "United States, Puerto Rico",
+            "temporal": "2019/2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional Death Counts for Coronavirus Disease (COVID-19)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/sutils/splign/splign.cgi",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/qj9j-7v27",
             "description": "Compute cDNA-to-Genomic sequence alignments.",
-            "title": "Splign",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109362,43 +109343,41 @@
                     "title": "Splign - Download"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/qj9j-7v27",
+            "issued": "2021-06-30",
+            "keyword": [
+                "computational biology",
+                "genomics",
+                "software",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/sutils/splign/splign.cgi",
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
+            "title": "Splign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://lhncbc.nlm.nih.gov/project/rxterms",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2012-08-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "dataset",
-                "drugs",
-                "drug terminology",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/k3pf-fv24",
             "description": "RxTerms is a drug interface terminology derived from RxNorm for prescription writing or medication history recording (e.g. in e-prescribing systems, PHRs). RxTerms is derived only from the non-proprietary content of RxNorm, which is developed and maintained by the U.S. National Library of Medicine. No fee or license is required to use the RxTerms data.  Technical documentation at https://wwwcf.nlm.nih.gov/umlslicense/rxtermApp/rxTermFileStructure.cfm",
-            "title": "RxTerms",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109413,45 +109392,43 @@
                     "title": "Download RxTerms Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/k3pf-fv24",
+            "issued": "2012-08-22",
+            "keyword": [
+                "api",
+                "dataset",
+                "drugs",
+                "drug terminology",
+                "health data standards",
+                "terminologies"
+            ],
+            "landingPage": "https://lhncbc.nlm.nih.gov/project/rxterms",
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
+            "title": "RxTerms"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hjax-h34q",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "malaria",
-                "measles imported",
-                "measles indigenous",
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
-            "identifier": "https://data.cdc.gov/api/views/hjax-h34q",
             "description": "NNDSS - TABLE 1V. Malaria to Measles, Imported - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1V. Malaria to Measles, Imported",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109474,44 +109451,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hjax-h34q",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "malaria",
+                "measles imported",
+                "measles indigenous",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hjax-h34q",
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
+            "title": "NNDSS - TABLE 1V. Malaria to Measles, Imported"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/efb8-zbb7",
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
-                "tuberculosis",
-                "tularemia",
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
-            "identifier": "https://data.cdc.gov/api/views/efb8-zbb7",
             "description": "NNDSS - TABLE 1JJ. Tuberculosis to Tularemia \u2013 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Tuberculosis data for weeks 4-31 are incorrect for New York City; the Middle Atlantic region total; U.S. Residents, excluding U.S. Territories total; and the grand total, due to data processing issues. \nNotice: Tuberculosis data for weeks 32-33 are incorrect for the U.S. Residents, excluding U.S. Territories total and the grand total, due to data processing issues. \n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1JJ. Tuberculosis to Tularemia",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109534,35 +109512,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/efb8-zbb7",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "nedss",
+                "netss",
+                "nndss",
+                "tuberculosis",
+                "tularemia",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/efb8-zbb7",
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
+            "title": "NNDSS - TABLE 1JJ. Tuberculosis to Tularemia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/2tj4-nah7",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/2tj4-nah7",
             "description": "Deaths or serious injuries among emergency medical technicians (EMTs) and other ambulance occupants occur at a high rate during transport. According to a study by the National Institute for Occupational Safety and Health (NIOSH), EMTs and paramedics have higher fatality rates when compared to all workers, with forty-five percent of EMT deaths resulting from highway incidents, primarily due to vehicle collisions.1 Data from the National Highway and Traffic Safety Administration showed that among the persons killed in crashes involving an ambulance between 1992 and 2011, twenty one percent were EMTs and patients, while four percent were ambulance drivers.2 To reduce injury potential to the EMTs and other ambulance occupants, NIOSH, the Department of Homeland Security, the U.S. General Services Administration, and the National Institute of Standards and Technology, along with private industry partners, have committed to improving the workspace design of ambulance patient compartments for safe and effective perfo",
-            "title": "Anthropometric Database for the EMTs in the United States",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109570,43 +109557,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/2tj4-nah7",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/2tj4-nah7",
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
+            "title": "Anthropometric Database for the EMTs in the United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-20",
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
-            "identifier": "https://data.cdc.gov/api/views/4bdk-kyzv",
             "description": "Monthly Cumulative Percent of Children <8 Months Who Received Nirsevimab by Jurisdiction, United States. \nNirsevimab coverage for children 0 to 7 months is assessed through U.S. jurisdictions\u2019 Immunization Information Systems Resources (IIS) data, submitted from jurisdictions to CDC monthly in aggregate by age group (https://www.cdc.gov/iis/about/).",
-            "title": "Monthly Cumulative Number and Percent of Children <8 Months Who Received Nirsevimab by Jurisdiction, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109629,54 +109609,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/4bdk-kyzv",
+            "issued": "2024-11-20",
+            "keyword": [
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "rsv vaccination",
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
+            "temporal": "2024-2025",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Monthly Cumulative Number and Percent of Children <8 Months Who Received Nirsevimab by Jurisdiction, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/medicare-current-beneficiary-survey-mcbs/medicare-current-beneficiary-survey-survey-file",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2013-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-31",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-10/SFPUF2022_DUG.pdf"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/cab71ec9-221c-4969-93dc-196d9f824689/data-viewer",
-            "description": "The Medicare Current Beneficiary Survey (MCBS) - Survey File Microdata Public Use File (PUF) dataset provides information on topics such as Medicare beneficiaries' access to care, health status, other information regarding beneficiaries\u2019 knowledge of, attitudes toward, and satisfaction with their health care, as well as demographic data and information on all types of health insurance coverage.",
-            "title": "Medicare Current Beneficiary Survey - Survey File",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/SFPUF2022_Codebooks.zip",
             "describedByType": "application/zip",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Medicare Current Beneficiary Survey (MCBS) - Survey File Microdata Public Use File (PUF) dataset provides information on topics such as Medicare beneficiaries' access to care, health status, other information regarding beneficiaries\u2019 knowledge of, attitudes toward, and satisfaction with their health care, as well as demographic data and information on all types of health insurance coverage.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109733,52 +109710,51 @@
                     "title": "Medicare Current Beneficiary Survey - Survey File : 2013-12-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/SFPUF2022_Codebooks.zip",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/cab71ec9-221c-4969-93dc-196d9f824689/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health equity",
+                "medicare",
+                "medicare advantage",
+                "medicare prescription drug",
+                "national",
+                "original medicare",
+                "patient experience"
+            ],
+            "landingPage": "https://data.cms.gov/medicare-current-beneficiary-survey-mcbs/medicare-current-beneficiary-survey-survey-file",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-31",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-10/SFPUF2022_DUG.pdf"
+            ],
+            "temporal": "2013-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Current Beneficiary Survey - Survey File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/g3g2-srtq",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "machupo virus",
-                "marburg virus",
-                "nedss",
-                "netss",
-                "nndss",
-                "sabia virus",
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
-            "identifier": "https://data.cdc.gov/api/views/g3g2-srtq",
             "description": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Machupo virus to Viral hemorrhagic fevers, Sabia virus \u2013 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\n\u00a7 Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers\". NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
-            "title": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Machupo virus to Viral hemorrhagic fevers, Sabia virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109801,41 +109777,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/g3g2-srtq",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "machupo virus",
+                "marburg virus",
+                "nedss",
+                "netss",
+                "nndss",
+                "sabia virus",
+                "viral hemorrhagic fevers",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/g3g2-srtq",
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
+            "title": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Machupo virus to Viral hemorrhagic fevers, Sabia virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/num2-ab96",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-27",
-            "keyword": [
-                "exchange puf",
-                "machine readable",
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
-            "identifier": "79409395-1868-4895-8601-e39a6a9266fe",
             "description": "The Machine Readable PUF (MR-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The MR-PUF contains issuer-level URL locations for machine-readable network provider and formulary information.",
-            "title": "Machine Readable PUF - PY2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109843,17 +109825,46 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "79409395-1868-4895-8601-e39a6a9266fe",
+            "issued": "2024-08-26",
+            "keyword": [
+                "exchange puf",
+                "machine readable",
+                "marketplace puf",
+                "py2024"
+            ],
+            "landingPage": "https://healthdata.gov/d/num2-ab96",
+            "modified": "2024-08-27",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Machine Readable PUF - PY2024"
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
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/pistachiorecall/Pistachio2009.xls",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "identifier": "a501b289-fe9f-4c20-980f-f95f34c81f30",
             "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2010-10-01",
             "keyword": [
                 "community health",
                 "food",
@@ -109864,60 +109875,31 @@
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
-            "identifier": "a501b289-fe9f-4c20-980f-f95f34c81f30",
-            "description": "Contains data for FDA pistachio product recalls since March 2009.",
-            "title": "FDA Pistachio Product Recalls",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/pistachiorecall/Pistachio2009.xls",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "FDA Pistachio Product Recalls"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/nvu8-jgnr",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-05-25",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-20",
-            "references": [
-                "https://download.medicaid.gov/data/Spreadsheet_Footnotes.pdf"
-            ],
-            "keyword": [
-                "drug products"
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
-            "identifier": "52d7cf12-5c8d-450c-884d-7dca2632142a",
             "description": "The Reference Document link for the downable Blood Disorder Treatment Spreadsheet can be accessed below under the Additional Information table under Related Documents.",
-            "title": "Pricing Comparison for Blood Disorder Treatments (Pricing as of 12/1/2021)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -109925,61 +109907,43 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "52d7cf12-5c8d-450c-884d-7dca2632142a",
+            "issued": "2022-05-25",
+            "keyword": [
+                "drug products"
+            ],
+            "landingPage": "https://healthdata.gov/d/nvu8-jgnr",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2022-12-20",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://download.medicaid.gov/data/Spreadsheet_Footnotes.pdf"
+            ],
             "theme": [
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "Pricing Comparison for Blood Disorder Treatments (Pricing as of 12/1/2021)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://github.com/cmheilig/harvest-cdc-journals",
+            "accrualPeriodicity": "Irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-03-19",
-            "temporal": "1982 - 2023",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-22",
-            "references": [
-                "\"https://github.com/cmheilig/harvest-cdc-journals?tab=readme-ov-file\"",
-                "\"https://www.cdc.gov/mmwr/\"",
-                "\"https://wwwnc.cdc.gov/eid\"",
-                "\"https://www.cdc.gov/pcd/\""
-            ],
-            "keyword": [
-                "corpora",
-                "corpus",
-                "data science",
-                "eid",
-                "harvest-cdc-journals",
-                "informatics",
-                "language",
-                "machine learning",
-                "ml",
-                "mmwr",
-                "ncstltphiw",
-                "pcd",
-                "phic",
-                "smokefree indoor air",
-                "text analysis"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCSTLTPHIW(PHIC) Associate Director of Informatics and Data Science",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7rih-tqi5",
+            "describedBy": "https://github.com/cmheilig/harvest-cdc-journals?tab=readme-ov-file#cdc-text-corpora-for-learners",
             "description": "This landing page is part of the <a href=\"https://github.com/cmheilig/harvest-cdc-journals\">CDC Text Corpora for Learners</a> program; this includes the compiled 33,576 CDC Text for Learners <a href=\"https://data.cdc.gov/National-Center-for-State-Tribal-Local-and-Territo/CDC-Text-Corpora-for-Learners-HTML-Mirrors-of-MMWR/ut5n-bmc3/about_data\">HTML mirrors</a> of the MMWR <a href=\"https://www.cdc.gov/mmwr/\">Morbidity and Mortality Weekly Report</a> including its series: <i>Weekly Reports</i>, <i>Recommendations and Reports</i>, <i>Surveillance Summaries</i>, <i>Supplements</i>, and <i>Notifiable Diseases</i>, a subset of <i>Weekly Reports</i>, constructed ad hoc; EID <a href=\"https://www.cdc.gov/eid/\">Emerging Infectious Diseases</a>; and PCD <a href=\"https://www.cdc.gov/pcd/\">Preventing Chronic Disease</a>\n\nThe data represented here is the tabulated <a href=\"https://github.com/cmheilig/harvest-cdc-journals/blob/main/README.md#metadata-fields\">metadata</a> of the combined 33,567 articles of the  <a href=\"https://github.com/cmheilig/harvest-cdc-journals?tab=readme-ov-file#collections\">MMWR, EID, and PCD collections</a> whose contents are organized into three ZIP archived JSON files per collection. The JSON value output formats include UTF-8 HTML, UTF-8 markdown, and ASCII plain text.\n\nThe <a href=\"https://github.com/cmheilig/harvest-cdc-journals?tab=readme-ov-file#collections\">JSON files</a> are located in the <a href=\"https://github.com/cmheilig/harvest-cdc-journals\">program's repository.</a> This version was constructed on 2024-03-01 using source content retrieved on 2024-01-09.",
-            "title": "CDC Text Corpora for Learners: MMWR, EID, and PCD Article Metadata",
-            "isPartOf": "CDC Text Corpora for Learners",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -110002,60 +109966,72 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://github.com/cmheilig/harvest-cdc-journals?tab=readme-ov-file#cdc-text-corpora-for-learners",
+            "identifier": "https://data.cdc.gov/api/views/7rih-tqi5",
+            "isPartOf": "CDC Text Corpora for Learners",
+            "issued": "2024-03-19",
+            "keyword": [
+                "corpora",
+                "corpus",
+                "data science",
+                "eid",
+                "harvest-cdc-journals",
+                "informatics",
+                "language",
+                "machine learning",
+                "ml",
+                "mmwr",
+                "ncstltphiw",
+                "pcd",
+                "phic",
+                "smokefree indoor air",
+                "text analysis"
+            ],
+            "landingPage": "https://github.com/cmheilig/harvest-cdc-journals",
             "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "accrualPeriodicity": "Irregular",
+            "modified": "2024-03-22",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "\"https://github.com/cmheilig/harvest-cdc-journals?tab=readme-ov-file\"",
+                "\"https://www.cdc.gov/mmwr/\"",
+                "\"https://wwwnc.cdc.gov/eid\"",
+                "\"https://www.cdc.gov/pcd/\""
+            ],
+            "temporal": "1982 - 2023",
             "theme": [
                 "National Center for State",
                 "Tribal",
                 "Local",
                 "and Territorial Public Health Infrastructure and Workforce"
-            ]
+            ],
+            "title": "CDC Text Corpora for Learners: MMWR, EID, and PCD Article Metadata"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/county-level-aggregate-expenditure-and-risk-score-data-on-assignable-beneficiaries",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2016-01-01/2023-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "references": [
-                "https://data.cms.gov/resources/county-level-aggregate-expenditure-and-risk-score-data-on-assignable-beneficiaries-methodology"
-            ],
-            "keyword": [
-                "accountable care organizations",
-                "coordinated care",
-                "counties",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/5f9f1216-6fd9-455d-bfbc-0efade687a4e/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/county-level-aggregate-expenditure-and-risk-score-data-on-assignable-beneficiaries-data-dictionary-0",
             "description": "The Shared Savings Program County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries Public Use File (PUF) for the Medicare Shared Savings Program (Shared Savings Program) provides aggregate data consisting of per capita Parts A and B FFS expenditures, average CMS-HCC prospective risk scores,\u00a0average demographic risk scores and total person-years for Shared Savings Program assignable beneficiaries by Medicare enrollment type (End Stage Renal Disease (ESRD), disabled, aged/dual eligible, aged/non-dual eligible).\n\n\u00a0\n\nDISCLAIMER: This information is current as of the last update. Changes to Shared Savings Program Accountable Care Organization (ACO) information occur periodically. Each Shared Savings Program ACO has the most up-to-date information about their organization. Consider contacting the Shared Savings Program ACO for the latest information. Contact information is available in the ACO PUF and the ACO Participants PUF.",
-            "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5f9f1216-6fd9-455d-bfbc-0efade687a4e/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5f9f1216-6fd9-455d-bfbc-0efade687a4e/data",
+                    "mediaType": "text/html",
                     "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-03oc2"
                 },
                 {
@@ -110227,49 +110203,52 @@
                     "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2016-01-15"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/county-level-aggregate-expenditure-and-risk-score-data-on-assignable-beneficiaries-data-dictionary-0",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/5f9f1216-6fd9-455d-bfbc-0efade687a4e/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "counties",
+                "financials",
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/county-level-aggregate-expenditure-and-risk-score-data-on-assignable-beneficiaries",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-12-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/county-level-aggregate-expenditure-and-risk-score-data-on-assignable-beneficiaries-methodology"
+            ],
+            "temporal": "2016-01-01/2023-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-visualization/mortality-leading-causes/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-12-02",
-            "@type": "dcat:Dataset",
-            "temporal": "1999/2017",
-            "modified": "2022-03-30",
-            "keyword": [
-                "leading causes of death",
-                "mortality",
-                "nchs",
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
-            "identifier": "https://data.cdc.gov/api/views/bi63-dtpu",
             "description": "This dataset presents the age-adjusted death rates for the 10 leading causes of death in the United States beginning in 1999.\r\n\r\nData are based on information from all resident death certificates filed in the 50 states and the District of Columbia using demographic and medical characteristics. Age-adjusted death rates (per 100,000 population) are based on the 2000 U.S. standard population. Populations used for computing death rates after 2010 are postcensal estimates based on the 2010 census, estimated as of July 1, 2010. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for non-census years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published.\r\n\r\nCauses of death classified by the International Classification of Diseases, Tenth Revision (ICD\u201310) are ranked according to the number of deaths assigned to rankable causes. Cause of death statistics are based on the underlying cause of death.\r\n\r\nSOURCES\r\nCDC/NCHS, National Vital Statistics System, mortality data (see http://www.cdc.gov/nchs/deaths.htm); and CDC WONDER (see http://wonder.cdc.gov).\r\n\r\nREFERENCES\r\n\r\n1. National Center for Health Statistics. Vital statistics data available. Mortality multiple cause files. Hyattsville, MD: National Center for Health Statistics. Available from: https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm.\r\n\r\n2. Murphy SL, Xu JQ, Kochanek KD, Curtin SC, and Arias E. Deaths: Final data for 2015. National vital statistics reports; vol 66. no. 6. Hyattsville, MD: National Center for Health Statistics. 2017. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_06.pdf.",
-            "title": "NCHS - Leading Causes of Death: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -110292,47 +110271,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/bi63-dtpu",
+            "issued": "2015-12-02",
+            "keyword": [
+                "leading causes of death",
+                "mortality",
+                "nchs",
+                "state",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/mortality-leading-causes/index.htm",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-03-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "1999/2017",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - Leading Causes of Death: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9k8a-cbgx",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "imported",
-                "indigenous",
-                "malaria",
-                "measles",
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
-            "identifier": "https://data.cdc.gov/api/views/9k8a-cbgx",
             "description": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Measles is considered imported if the disease was acquired outside of the United States and is considered indigenous if the disease was acquired anywhere within the United States or it is not known where the disease was acquired.",
-            "title": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -110355,44 +110331,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9k8a-cbgx",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "imported",
+                "indigenous",
+                "malaria",
+                "measles",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9k8a-cbgx",
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
+            "title": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/acdz-tk8j",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "legionellosis",
-                "malaria",
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
-            "identifier": "https://data.cdc.gov/api/views/acdz-tk8j",
             "description": "NNDSS - Table II. Legionellosis to Malaria - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\r\n \r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum.\r\n \r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Legionellosis to Malaria",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -110415,46 +110393,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/acdz-tk8j",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "legionellosis",
+                "malaria",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/acdz-tk8j",
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
+            "title": "NNDSS - Table II. Legionellosis to Malaria"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/aspp-bzzu",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "confirmed",
-                "leptospirosis",
-                "listeriosis",
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
-            "identifier": "https://data.cdc.gov/api/views/aspp-bzzu",
             "description": "NNDSS - TABLE 1U. Leptospirosis to Listeriosis, Probable - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1U. Leptospirosis to Listeriosis, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -110477,44 +110453,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/aspp-bzzu",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "confirmed",
+                "leptospirosis",
+                "listeriosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/aspp-bzzu",
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
+            "title": "NNDSS - TABLE 1U. Leptospirosis to Listeriosis, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/82nv-dn3y",
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
-                "syphilis congenital",
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
-            "identifier": "https://data.cdc.gov/api/views/82nv-dn3y",
             "description": "NNDSS - TABLE 1HH. Syphilis, Congenital to Syphilis, Primary and Secondary \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1HH. Syphilis, Congenital to Syphilis, Primary and Secondary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -110537,46 +110515,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/82nv-dn3y",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "syphilis congenital",
+                "syphilis primary and secondary",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/82nv-dn3y",
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
+            "title": "NNDSS - TABLE 1HH. Syphilis, Congenital to Syphilis, Primary and Secondary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/drfe-vxdh",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
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
-            "identifier": "https://data.cdc.gov/api/views/drfe-vxdh",
             "description": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease.",
-            "title": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -110599,38 +110575,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/drfe-vxdh",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "all ages",
+                "confirmed",
+                "invasive pneumococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/drfe-vxdh",
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
+            "title": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/p2eg-a93h",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-10-14",
-            "@type": "dcat:Dataset",
-            "modified": "2021-10-13",
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
-            "identifier": "4928c3c9-0a03-459f-b1ce-ca692b22e2bd",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210927 to 20211003",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -110638,38 +110623,35 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "identifier": "4928c3c9-0a03-459f-b1ce-ca692b22e2bd",
+            "issued": "2021-10-14",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/p2eg-a93h",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-10-13",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210927 to 20211003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/sesw-5ehn",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-08-15",
-            "@type": "dcat:Dataset",
-            "modified": "2017-09-07",
-            "keyword": [
-                "electronic health information",
-                "law",
-                "public health law program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rachel Hulkower",
                 "hasEmail": "mailto:hzo2@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/sesw-5ehn",
             "description": "Authors: Cason Schmit, JD, Gregory Sunshine, JD, Dawn Pepin, JD, MPH, Tara Ramanathan, JD, MPH, Akshara Menon, JD, MPH, Matthew Penn, JD, MLIS\r\nThe Health Information Technology for Economic and Clinical Health Act, adopted in 2009, accelerated adoption of electronic health record systems among health care providers. Many state statutes and regulations authorize and define the use of electronic health information (EHI). Practitioners often criticize these laws as complex and contradictory and point to them as barriers to using EHI. Attorney researchers used WestlawNext to search for EHI-related statutes and regulations of the US states, US\r\nterritories, and the District of Columbia in effect as of January 2014. The researchers independently catalogued provisions by the EHI use described in the law. This research protocol accompanies the data set, Electronic Health Information Legal Epidemiology Data Set 2014.",
-            "title": "Electronic Health Information Legal Epidemiology Protocol 2014",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -110677,42 +110659,37 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/sesw-5ehn",
+            "issued": "2017-08-15",
+            "keyword": [
+                "electronic health information",
+                "law",
+                "public health law program"
+            ],
+            "landingPage": "https://data.cdc.gov/d/sesw-5ehn",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2017-09-07",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "Electronic Health Information Legal Epidemiology Protocol 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/q9sm-44y3",
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
-                "nonparalytic",
-                "poliovirus infection",
-                "psittacosis",
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
-            "identifier": "https://data.cdc.gov/api/views/q9sm-44y3",
             "description": "NNDSS - TABLE 1AA.  Poliovirus infection, nonparalytic to Psittacosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1AA.  Poliovirus infection, nonparalytic to Psittacosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -110735,40 +110712,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/q9sm-44y3",
+            "issued": "2019-04-23",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "nonparalytic",
+                "poliovirus infection",
+                "psittacosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/q9sm-44y3",
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
+            "title": "NNDSS - TABLE 1AA.  Poliovirus infection, nonparalytic to Psittacosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/genomes/GenomesHome.cgi?",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dataset",
-                "genomics",
-                "virus"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/569f-vvac",
             "description": "This resource provides viral genome sequence data and related information.",
-            "title": "Viral Genomes",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -110801,41 +110783,40 @@
                     "title": "View all RefSeq and Neighbor nucleotide records"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/569f-vvac",
+            "issued": "2021-06-30",
+            "keyword": [
+                "dataset",
+                "genomics",
+                "virus"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/genomes/GenomesHome.cgi?",
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
+            "title": "Viral Genomes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7njk-uncd",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-08-10",
-            "@type": "dcat:Dataset",
-            "modified": "2018-02-21",
-            "keyword": [
-                "americas",
-                "chikungunya",
-                "predictions",
-                "travelers"
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
-            "identifier": "https://data.cdc.gov/api/views/7njk-uncd",
             "description": "Interactive visualization: http://www.cdc.gov/chikungunya/modeling/index.html. This dataset contains monthly predictions for the spread of chikungunya virus transmission. A full description of the methods is available at: http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0104915.",
-            "title": "Nowcast Predictions for Local Transmission of Chikungunya Virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -110858,32 +110839,38 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/7njk-uncd",
+            "issued": "2015-08-10",
+            "keyword": [
+                "americas",
+                "chikungunya",
+                "predictions",
+                "travelers"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7njk-uncd",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-02-21",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "Nowcast Predictions for Local Transmission of Chikungunya Virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/q8qz-3pb6",
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
-            "identifier": "https://data.cdc.gov/api/views/q8qz-3pb6",
             "description": "Masks block aerosols produced during coughs and exhalations (\u201csource control\u201d). Masks also slow and deflect cough and exhalation airflows, which changes the dispersion of aerosols. Factors such as the directions in which people are facing (orientation) and separation distance also affect aerosol dispersion. However, it is not clear how masking, orientation, and distance interact. We placed a respiratory aerosol simulator (\u201csource\u201d) and a breathing simulator (\u201crecipient\u201d) in a chamber and measured aerosol concentrations for different combinations of masking, orientation, and separation distance. When the simulators were front-to-front during coughing, masks reduced the 15-minute mean aerosol concentration at the recipient by 92% (p < 0.0001) at 0.9 and 1.8 m separation. When the simulators were side-by-side, masks reduced the concentration by 81% at 0.9 m and 78% at 1.8 m (p < 0.0001 for both). During breathing, masks reduced the aerosol concentration by 66% when front-to-front (p = 0.0056) and 76% when side-by-side (p < 0.0001) at 0.9 m. Similar results were seen at 1.8 m. When the simulators were unmasked, changing the orientations from front-to-front to side-by-side reduced the cough aerosol concentration by 59% at 0.9 m and 60% at 1.8 m (p < 0.0001 for both). When both simulators were masked, changing the orientations did not significantly change the concentration at either distance during coughing or breathing. Increasing the distance between the simulators from 0.9 m to 1.8 m during coughing reduced the aerosol concentration by 25% when no masks were worn (p < 0.0001) but had little effect when both simulators were masked (4% decrease, p = 0.7090). During breathing, when neither simulator was masked, increasing the separation reduced the concentration by 13%, which approached significance (p = 0.0737), while the change was not significant when both source and recipient were masked (8% decrease, p = 0.3235). Our results suggest that universal masking reduces exposure to respiratory aerosol particles regardless of the orientation and separation distance between the source and recipient.",
-            "title": "Efficacy of universal masking for source control and personal protection from simulated respiratory aerosols in a room",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -110891,20 +110878,47 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/q8qz-3pb6",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/q8qz-3pb6",
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
+            "title": "Efficacy of universal masking for source control and personal protection from simulated respiratory aerosols in a room"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/p54m-tycn",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of behavioral health services, including emergency department services, inpatient services, intensive outpatient/partial hospitalizations, outpatient services, or services delivered through telehealth, provided to Medicaid and CHIP beneficiaries, by state. Users can filter by either mental health disorder or substance use disorder. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating behavioral health services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Diagnosis Code - IP, Diagnosis Code - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of behavioral health services, including emergency department services, inpatient services, intensive outpatient/partial hospitalizations, outpatient services, or services delivered through telehealth, provided to Medicaid and CHIP beneficiaries, by state. Users can filter by either mental health disorder or substance use disorder. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating behavioral health services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Diagnosis Code - IP, Diagnosis Code - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/Blood-Lead-Screening-Services-Provided-to-MedicaidCHIP-Beneficiaries-Ages-1-2.csv",
+                    "mediaType": "text/csv",
+                    "title": "Blood Lead Screening Services Provided to Medicaid and CHIP Beneficiaries Ages 1-2"
+                }
+            ],
+            "identifier": "34fc0456-e28c-4762-91e1-49cd88462e7a",
             "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-05",
             "keyword": [
                 "behavioral health",
                 "chip",
@@ -110915,79 +110929,42 @@
                 "substance use disorder",
                 "t-msis analytic files"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Medicaid.gov",
-                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/d/p54m-tycn",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-01-05",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Medicare & Medicaid Services"
             },
-            "identifier": "34fc0456-e28c-4762-91e1-49cd88462e7a",
-            "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of behavioral health services, including emergency department services, inpatient services, intensive outpatient/partial hospitalizations, outpatient services, or services delivered through telehealth, provided to Medicaid and CHIP beneficiaries, by state. Users can filter by either mental health disorder or substance use disorder. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating behavioral health services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Diagnosis Code - IP, Diagnosis Code - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Blood Lead Screening Services Provided to Medicaid and CHIP Beneficiaries Ages 1-2",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/Blood-Lead-Screening-Services-Provided-to-MedicaidCHIP-Beneficiaries-Ages-1-2.csv",
-                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of behavioral health services, including emergency department services, inpatient services, intensive outpatient/partial hospitalizations, outpatient services, or services delivered through telehealth, provided to Medicaid and CHIP beneficiaries, by state. Users can filter by either mental health disorder or substance use disorder. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating behavioral health services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Diagnosis Code - IP, Diagnosis Code - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-                    "@type": "dcat:Distribution",
-                    "title": "Blood Lead Screening Services Provided to Medicaid and CHIP Beneficiaries Ages 1-2"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Blood Lead Screening Services Provided to Medicaid and CHIP Beneficiaries Ages 1-2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-geography-and-drug",
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
-                "national",
-                "physicians & practitioners",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/c8ea3f8e-3a09-4fea-86f2-8902fb4b0920/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-part-d-prescribers-by-geography-and-drug-data-dictionary",
             "description": "The Medicare Part D Prescribers by Geography and Drug dataset contains information on prescription drugs prescribed by individual physicians and other health care providers and paid for under the Medicare Part D Prescription Drug Program. For each drug, the dataset includes the total number of prescriptions that were dispensed, which include original prescriptions and any refills, and the total drug cost. The total drug cost includes the ingredient cost of the medication, dispensing fees, sales tax, and any applicable administration fees and is based on the amount paid by the Part D plan, Medicare beneficiary, government subsidies, and any other third-party payers.",
-            "title": "Medicare Part D Prescribers - by Geography and Drug",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c8ea3f8e-3a09-4fea-86f2-8902fb4b0920/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c8ea3f8e-3a09-4fea-86f2-8902fb4b0920/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Part D Prescribers - by Geography and Drug : 2022-12-30"
                 },
                 {
@@ -111111,59 +111088,61 @@
                     "title": "Medicare Part D Prescribers - by Geography and Drug : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-part-d-prescribers-by-geography-and-drug-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/c8ea3f8e-3a09-4fea-86f2-8902fb4b0920/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "drugs",
+                "health equity",
+                "medicare",
+                "medicare prescription drug",
+                "national",
+                "physicians & practitioners",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-geography-and-drug",
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
+            "title": "Medicare Part D Prescribers - by Geography and Drug"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/federally-qualified-health-center-enrollments",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-12-08",
-            "temporal": "2023-10-01/2025-03-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2023-09/FQHC_Data_Guidance.pdf"
-            ],
-            "keyword": [
-                "federally qualified health centers",
-                "hospitals & facilities",
-                "medicare",
-                "outpatient facilities",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/4bcae866-3411-439a-b762-90a6187c194b/data-viewer",
-            "description": "The Federally Qualified Health Center (FQHC) Enrollments dataset provides enrollment information on all FQHCs currently enrolled in Medicare. This data includes information on the FQHC's legal business name, doing business as name, organization type, and address.",
-            "title": "Federally Qualified Health Center Enrollments",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-09/FQHC_Enrollments_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Federally Qualified Health Center (FQHC) Enrollments dataset provides enrollment information on all FQHCs currently enrolled in Medicare. This data includes information on the FQHC's legal business name, doing business as name, organization type, and address.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4bcae866-3411-439a-b762-90a6187c194b/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4bcae866-3411-439a-b762-90a6187c194b/data",
+                    "mediaType": "text/html",
                     "title": "Federally Qualified Health Center Enrollments : 2025-01-01"
                 },
                 {
@@ -111239,102 +111218,96 @@
                     "title": "Federally Qualified Health Center Enrollments : 2023-10-28"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2023-09/FQHC_Enrollments_Data_Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/4bcae866-3411-439a-b762-90a6187c194b/data-viewer",
+            "issued": "2023-12-08",
+            "keyword": [
+                "federally qualified health centers",
+                "hospitals & facilities",
+                "medicare",
+                "outpatient facilities",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/federally-qualified-health-center-enrollments",
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
+                "https://data.cms.gov/sites/default/files/2023-09/FQHC_Data_Guidance.pdf"
+            ],
+            "temporal": "2023-10-01/2025-03-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Federally Qualified Health Center Enrollments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/p7bq-srdf",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-03-28",
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
-            "identifier": "6ac0cd59-34dd-5a2b-aca9-6f9322fbf7be",
             "description": "This is a dataset created for use by the Scorecard website, and is not intended for use outside that application.",
-            "title": "Scorecard measure",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/measure.csv",
-                    "description": "Scorecard measure",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard measure",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard measure"
                 }
             ],
+            "identifier": "6ac0cd59-34dd-5a2b-aca9-6f9322fbf7be",
+            "issued": "2023-03-28",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/p7bq-srdf",
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
-            "landingPage": "https://healthdata.gov/dataset/mental-health-treatement-facilities-locator",
             "bureauCode": [
                 "009:30"
             ],
-            "issued": "2012-12-14",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "health care providers",
-                "help",
-                "locator",
-                "mental health treatment facilities",
-                "provider",
-                "psychatrist",
-                "psychologist",
-                "safety",
-                "sexual assault",
-                "substance abuse. buprenorphine",
-                "suicide prevention",
-                "therapy",
-                "treatments"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Find Treatment",
                 "hasEmail": "mailto:findtreatment@samhsa.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Substance Abuse & Mental Health Services Administration, Department of Health & Human Services"
-            },
-            "identifier": "08d3f21c-6ab7-4f78-9590-54eb07ee6670",
+            "dataQuality": true,
             "description": "<p>An online resource for locating mental health treatment facilities and programs supported by the Substance Abuse and Mental Health Services Administration (SAMHSA). The Mental Health Treatment Locator section of the Behavioral Health Treatment Services Locator lists facilities providing mental health services to persons with mental illness. It includes:<br />\nPublic mental health facilities that are funded by their State mental health agency (SMHA) or other State agency or department<br />\nMental health treatment facilities administered by the Department of Veterans Affairs, Private for-profit and non-profit mental health facilities that are licensed by the State or accredited by a national accreditation organization.</p>\n<p>NOTE: The Mental Health Treatment Locator does not include facilities whose primary or only focus is the provision of services to persons with Mental Retardation (MR), Developmental Disability (DD), and Traumatic Brain Injuries (TBI). Facilities that provide treatment exclusively to persons with mental illness who are incarcerated. Mental health professionals in private practice (individual) or in a small group practice not licensed or certified as a mental health clinic or (community) mental health center.</p>\n<p>SAMHSA endeavors to keep the Locator current. All information in the Locator is updated annually based on facility responses to SAMHSA's National Mental Health Services Survey (N-MHSS). The most recent complete update includes data collected as of April 30, 2010 in the N-MHSS. New facilities are added monthly. Updates to facility names, addresses, telephone numbers and services are made weekly, if facilities inform SAMHSA of changes.</p>\n<p>For additional advice, you may call the Referral Helpline operated by SAMHSA's Center for Substance Abuse Treatment:</p>\n<p><code>1-800-662-HELP (English &amp; Espa\u00f1ol)</p>\n<p>1-800-487-4889 (TTY)<br />\n</code></p>",
-            "title": "Mental Health Treatement Facilities Locator",
-            "programCode": [
-                "009:068"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -111355,72 +111328,84 @@
                     "title": "Map "
                 }
             ],
-            "dataQuality": true,
+            "identifier": "08d3f21c-6ab7-4f78-9590-54eb07ee6670",
+            "issued": "2012-12-14",
+            "keyword": [
+                "health care providers",
+                "help",
+                "locator",
+                "mental health treatment facilities",
+                "provider",
+                "psychatrist",
+                "psychologist",
+                "safety",
+                "sexual assault",
+                "substance abuse. buprenorphine",
+                "suicide prevention",
+                "therapy",
+                "treatments"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/mental-health-treatement-facilities-locator",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:068"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration, Department of Health & Human Services"
+            },
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "Mental Health Treatement Facilities Locator"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.ncbi.nlm.nih.gov/snp",
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
                 "fn": "Phan, Lon",
                 "hasEmail": "mailto:lonphan@ncbi.nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "d6fe10ae-1cf5-4466-bf9e-f9e5ab267fa0",
+            "dataQuality": true,
             "description": "<p>dbSNP is a database of single nucleotide polymorphisms (SNPs) and multiple small-scale variations that include insertions/deletions, microsatellites, and non-polymorphic variants.</p>",
-            "title": "dbSNP",
+            "identifier": "d6fe10ae-1cf5-4466-bf9e-f9e5ab267fa0",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.ncbi.nlm.nih.gov/snp",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
             "programCode": [
                 "009:041"
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
+            "title": "dbSNP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/p82x-rydy",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-07",
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
-            "identifier": "c85171aa-68dc-42eb-85c6-4a24fc3185a7",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-31-to-2023-08-06",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -111429,33 +111414,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-31-to-2023-08-06"
                 }
             ],
+            "identifier": "c85171aa-68dc-42eb-85c6-4a24fc3185a7",
+            "issued": "2023-08-08",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/p82x-rydy",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-08-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-31-to-2023-08-06"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ef89-9ik2",
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
-            "identifier": "https://data.cdc.gov/api/views/ef89-9ik2",
             "description": "Interleukin (IL)-11, a pleiotropic, cationic cytokine, contributes to numerous biological processes, including adipogenesis, hematopoiesis, and inflammation.  Asthma, a chronic respiratory disease, is notably characterized by reversible airway obstruction, persistent lung inflammation, and airway hyperresponsiveness (AHR).  Nasal insufflation of IL-11 causes AHR in wild-type mice while lung inflammation induced by antigen sensitization and challenge, which mimics features of atopic asthma in humans, is attenuated in mice genetically deficient in IL-11 receptor subunit alpha-1 (IL-11R\u03b11-deficient mice), a transmembrane receptor that is required along with glycoprotein 130 to transduce IL-11 intracellular signaling.  Nevertheless, the contribution of IL-11R\u03b11 to the manifestation of phenotypic features of non-atopic asthma are not presently known. Thus, based on the aforementioned observations, we hypothesized that genetic deficiency of IL-11R\u03b11 would attenuate lung inflammation and increases in airway responsiveness following acute inhalation exposure to ozone, a criteria pollutant and non-atopic asthma stimulus.",
-            "title": "Interleukin-11 Receptor Subunit Alpha-1 is Required for Maximal Airway Responsiveness to Methacholine After Acute Exposure to Ozone",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -111463,90 +111450,84 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ef89-9ik2",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/ef89-9ik2",
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
+            "title": "Interleukin-11 Receptor Subunit Alpha-1 is Required for Maximal Airway Responsiveness to Methacholine After Acute Exposure to Ozone"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/p8hn-wtmc",
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
-            "identifier": "9e407144-9ed9-5cee-937a-17d65b07a9a7",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_map",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/map.csv",
-                    "description": "{\"dataset\": \"map\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"map\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/map.csv",
+                    "mediaType": "text/csv",
                     "title": "map csv file"
                 }
             ],
+            "identifier": "9e407144-9ed9-5cee-937a-17d65b07a9a7",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/p8hn-wtmc",
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
+            "title": "featAuto_map"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/p8w9-uqca",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-08-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-28",
-            "keyword": [
-                "individual",
-                "individual market medical",
-                "py2023",
-                "qhp",
-                "qhp landscape"
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
-            "identifier": "cfbbddd9-b405-4c4a-b679-fd2986945b88",
             "description": "The Medical Individual Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to consumers in the individual market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2023 Individual Medical",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -111554,37 +111535,39 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "cfbbddd9-b405-4c4a-b679-fd2986945b88",
+            "issued": "2023-08-23",
+            "keyword": [
+                "individual",
+                "individual market medical",
+                "py2023",
+                "qhp",
+                "qhp landscape"
+            ],
+            "landingPage": "https://healthdata.gov/d/p8w9-uqca",
+            "modified": "2023-08-28",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2023 Individual Medical"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/p988-gfex",
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
-            "identifier": "17c4bf03-ba38-5c0a-9f08-96e9ed812bdf",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 1995",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -111592,49 +111575,41 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "17c4bf03-ba38-5c0a-9f08-96e9ed812bdf",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/p988-gfex",
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
+            "title": "State Drug Utilization Data 1995"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5dqz-y4ea",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-12-06",
-            "temporal": "2024-10-04/present",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-06",
-            "keyword": [
-                "cfa",
-                "coronavirus",
-                "covid-19",
-                "epidemic trend",
-                "flu",
-                "influenza",
-                "modeling",
-                "respiratory virus response",
-                "rt",
-                "rvr"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Center for Forecasting and Outbreak Analytics",
                 "hasEmail": "mailto:cfa@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5dqz-y4ea",
             "description": "An archive of estimated trend categories, probabilities of epidemic growth, and Rt, updated weekly for COVID-19 and flu. Estimates are based on emergency department visits reported to the National Syndromic Surveillance Program (NSSP), and generated using a model that includes nowcasting to adjust for incomplete reports on the most recent dates. See the visuals supported by these data, and more information about the data, models and methods at https://www.cdc.gov/cfa-modeling-and-forecasting/rt-estimates/index.html, and https://www.cdc.gov/respiratory-viruses/data/activity-levels.html.\n\nFor a semi-technical overview of the modeling methods used to generate these estimates see https://www.cdc.gov/cfa-behind-the-model/php/data-research/rt-estimates/index.html.\n\nFor the code used to run the models, see https://github.com/CDCgov/cfa-epinow2-pipeline.",
-            "title": "CDC Epidemic Trends and Rt",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -111657,90 +111632,97 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5dqz-y4ea",
+            "issued": "2024-12-06",
+            "keyword": [
+                "cfa",
+                "coronavirus",
+                "covid-19",
+                "epidemic trend",
+                "flu",
+                "influenza",
+                "modeling",
+                "respiratory virus response",
+                "rt",
+                "rvr"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5dqz-y4ea",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2024-12-06",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2024-10-04/present",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "CDC Epidemic Trends and Rt"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/p9hc-avk4",
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
-            "identifier": "842c5980-37e0-5a3f-989d-a54b60436d34",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_tafVersion",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/tafVersion.csv",
-                    "description": "{\"dataset\": \"tafVersion\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"tafVersion\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/tafVersion.csv",
+                    "mediaType": "text/csv",
                     "title": "tafVersion csv file"
                 }
             ],
+            "identifier": "842c5980-37e0-5a3f-989d-a54b60436d34",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/p9hc-avk4",
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
+            "title": "implAuto_tafVersion"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/p9qu-rfuq",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-05",
-            "keyword": [
-                "chip",
-                "maternal health",
-                "medicaid",
-                "pregnancy"
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
-            "identifier": "a4035a82-7433-4efb-985d-32a9ab8e5341",
             "description": "This table presents the number of pregnant and postpartum Medicaid and CHIP beneficiaries, 2017-2021. It includes (1) the number and percentage of beneficiaries ever pregnant in the year; (2) the number and percentage of live births in the year; (3) the number and percentage of miscarriages, stillbirths, or terminations in the year; and (4) the number and percentage of births with an unknown delivery outcome in the year.\r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues, making the data unusable for identifying this population. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nData from Maryland, Tennessee, and Utah are omitted from the tables due to data quality concerns. Maryland was excluded in 2017 due to unusable diagnosis codes in the IP file and the OT file. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2020. In addition, states with a high data quality concern on one or more measures are noted in the table in the \"Data Quality\" column. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Number of pregnant and postpartum Medicaid and CHIP beneficiaries, 2017-2021",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -111749,89 +111731,91 @@
                     "title": "Number of pregnant and postpartum Medicaid and CHIP beneficiaries, 2017-2021"
                 }
             ],
+            "identifier": "a4035a82-7433-4efb-985d-32a9ab8e5341",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "maternal health",
+                "medicaid",
+                "pregnancy"
+            ],
+            "landingPage": "https://healthdata.gov/d/p9qu-rfuq",
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
                 "Uncategorized"
-            ]
+            ],
+            "title": "Number of pregnant and postpartum Medicaid and CHIP beneficiaries, 2017-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/p9sp-5gqf",
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
-            "identifier": "a49b8d56-2f5a-5990-a1a3-bc154ca04570",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_concernLevel",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/concernLevel.csv",
-                    "description": "{\"dataset\": \"concernLevel\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"concernLevel\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/concernLevel.csv",
+                    "mediaType": "text/csv",
                     "title": "concernLevel csv file"
                 }
             ],
+            "identifier": "a49b8d56-2f5a-5990-a1a3-bc154ca04570",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/p9sp-5gqf",
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
+            "title": "featAuto_concernLevel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/vital-stats-vital-statistics-tables-and-files-births-infant-deaths-fetal-deaths",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-11-05",
-            "temporal": "1990-01-01T00:00:00-05:00/2011-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "births perinatal mortality  population statistics",
-                "population statistics"
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
-            "identifier": "f954e1b2-d513-4b70-b892-f1bebbed46bb",
+            "dataQuality": true,
+            "describedBy": "http://www.cdc.gov/nchs/VitalStats.htm",
             "description": "<p>VitalStats:  A collection of vital statistics products including tables, data files, and reports that allow users to access and examine vital statistics and population data interactively.</p>\n<p>VitalStats includes pre-built tables and reports for quick access to statistics;  or the user can create tables--choosing from over 100 variables.  Tables can be customized to create charts, graphs, and maps.  Data can be exported.</p>",
-            "title": "Vital Stats (Vital Statistics Tables and files- Births, Infant Deaths, Fetal Deaths)",
-            "programCode": [
-                "009:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -111840,41 +111824,38 @@
                     "title": "HTML "
                 }
             ],
-            "describedBy": "http://www.cdc.gov/nchs/VitalStats.htm",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "f954e1b2-d513-4b70-b892-f1bebbed46bb",
+            "issued": "2012-11-05",
+            "keyword": [
+                "births perinatal mortality  population statistics",
+                "population statistics"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/vital-stats-vital-statistics-tables-and-files-births-infant-deaths-fetal-deaths",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
+            },
+            "temporal": "1990-01-01T00:00:00-05:00/2011-12-31T00:00:00-05:00",
+            "title": "Vital Stats (Vital Statistics Tables and files- Births, Infant Deaths, Fetal Deaths)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/index.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-12-16",
-            "temporal": "1999/2018",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-08",
-            "keyword": [
-                "high cholesterol",
-                "hypertension",
-                "nhanes",
-                "obesity"
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
-            "identifier": "https://data.cdc.gov/api/views/28df-2bwy",
             "description": "This data represents the age-adjusted prevalence of high total cholesterol, hypertension, and obesity among US adults aged 20 and over between 1999-2000 to 2017-2018.\n\n\nNotes:\n\n* All estimates are age adjusted by the direct method to the U.S. Census 2000 population using age groups 20\u201339, 40\u201359, and 60 and over.\n\n\nDefinitions\n\nHypertension: Systolic blood pressure greater than or equal to 130 mmHg or diastolic blood pressure greater than or equal to 80 mmHg, or currently taking medication to lower high blood pressure\n\nHigh total cholesterol: Serum total cholesterol greater than or equal to 240 mg/dL.\n\nObesity: Body mass index (BMI, weight in kilograms divided by height in meters squared) greater than or equal to 30.\n\n\nData Source and Methods\n\nData from the National Health and Nutrition Examination Surveys (NHANES) for the years 1999\u20132000, 2001\u20132002, 2003\u20132004, 2005\u20132006, 2007\u20132008, 2009\u20132010, 2011\u20132012, 2013\u20132014, 2015\u20132016, and 2017\u20132018 were used for these analyses.\n\nNHANES is a cross-sectional survey designed to monitor the health and nutritional status of the civilian noninstitutionalized U.S. population. The survey consists of interviews conducted in participants\u2019 homes and standardized physical examinations, including a blood draw, conducted in mobile examination centers.",
-            "title": "Prevalence of Selected Measures Among Adults Aged 20 and Over: United States, 1999-2000 through 2017-2018",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -111897,21 +111878,54 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/28df-2bwy",
+            "issued": "2020-12-16",
+            "keyword": [
+                "high cholesterol",
+                "hypertension",
+                "nhanes",
+                "obesity"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/index.htm",
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
+            "temporal": "1999/2018",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Prevalence of Selected Measures Among Adults Aged 20 and Over: United States, 1999-2000 through 2017-2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus/index.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "Health, United States  is the report on the health status of the country. Every year, the report presents an overview of national health trends organized around four subject areas: health status and determinants, utilization of health resources, health care resources, and health care expenditures and payers.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The Data Finder gives you Health, United States trend tables and figures on a subject and/or population subgroup of interest. ",
+                    "downloadURL": "https://www.cdc.gov/nchs/hus/data-finder.htm",
+                    "mediaType": "text/html",
+                    "title": "Data Finder"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/v5gm-kvkn",
             "issued": "2020-11-10",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-13",
             "keyword": [
                 "adults",
                 "children",
@@ -111927,67 +111941,37 @@
                 "resources",
                 "substance use"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/hus/index.htm",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-09-13",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/v5gm-kvkn",
-            "description": "Health, United States  is the report on the health status of the country. Every year, the report presents an overview of national health trends organized around four subject areas: health status and determinants, utilization of health resources, health care resources, and health care expenditures and payers.",
-            "title": "Health, United States",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/nchs/hus/data-finder.htm",
-                    "description": "The Data Finder gives you Health, United States trend tables and figures on a subject and/or population subgroup of interest. ",
-                    "@type": "dcat:Distribution",
-                    "title": "Data Finder"
-                }
-            ],
             "spatial": "US",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Health, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/pbyt-qpdj",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-11-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
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
-            "identifier": "3e3820b8-e89f-42a5-9e53-7557f98d7a7f",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 11-11-2024-to-11-17-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -111995,36 +111979,35 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "3e3820b8-e89f-42a5-9e53-7557f98d7a7f",
+            "issued": "2024-11-20",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/pbyt-qpdj",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 11-11-2024-to-11-17-2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/crzr-uvwg",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2019-06-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-03",
-            "keyword": [
-                "drug label",
-                "medication"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/crzr-uvwg",
             "description": "This resource was retired on January 28, 2021 and is no longer updated.  These data remain available to support research and development efforts.  Pillbox's final image library is available at https://ftp.nlm.nih.gov/projects/pillbox/pillbox_production_images_full_202008.zip.  For more information on Pillbox's retirement visit https://www.nlm.nih.gov/pubs/techbull/ja20/ja20_pillbox_discontinue.html.\n\nPillbox contains metadata for oral solid dosage form medications, derived from FDA drug labeling, including physical characteristics, active and inactive ingredients, National Drug Codes, information about firms marketing those products, selected information from RxNorm, and links to images provided by the National Library of Medicine.",
-            "title": "Pillbox (retired January 28, 2021)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112047,39 +112030,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/crzr-uvwg",
+            "issued": "2019-06-27",
+            "keyword": [
+                "drug label",
+                "medication"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/crzr-uvwg",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-09-03",
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
+            "title": "Pillbox (retired January 28, 2021)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/p8tr-pquj",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-01-23",
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
-            "identifier": "https://data.cdc.gov/api/views/p8tr-pquj",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "SAMHSA Synar Reports: Youth Tobacco Sales Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112087,39 +112070,39 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/p8tr-pquj",
+            "issued": "2015-01-23",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "https://data.cdc.gov/d/p8tr-pquj",
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
+            "title": "SAMHSA Synar Reports: Youth Tobacco Sales Glossary and Methodology"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -112142,100 +112125,86 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xbk2-5i4e",
+            "issued": "2018-07-26",
+            "keyword": [
+                "drought",
+                "environmental health"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xbk2-5i4e",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-11-27",
+            "programCode": [
+                "009:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Environmental Health & Toxicology"
-            ]
+            ],
+            "title": "Standardized Precipitation Index, 1895-2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/pep3-wh6f",
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
-            "identifier": "942d804c-6c1d-5912-a61f-08d42927ee9b",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard state v2.11.16 (cmsdev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/state.csv",
-                    "description": "Scorecard state v2.11.16 (cmsdev)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard state v2.11.16 (cmsdev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/state.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard state v2.11.16 (cmsdev)"
                 }
             ],
+            "identifier": "942d804c-6c1d-5912-a61f-08d42927ee9b",
+            "issued": "2023-04-21",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/pep3-wh6f",
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
+            "title": "Scorecard state v2.11.16 (cmsdev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
-            "keyword": [
-                "covid",
-                "covid19",
-                "covid-19",
-                "covidnet",
-                "covid-net",
-                "epi curve",
-                "hospitalizations",
-                "icu",
-                "in-hospital death",
-                "percent icu",
-                "percent in-hospital death",
-                "percent mechanically ventilated",
-                "respiratory illness",
-                "respiratory virus response",
-                "respnet",
-                "resp-net",
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
-            "identifier": "https://data.cdc.gov/api/views/bigw-pgk2",
             "description": "The Coronavirus Disease 2019 (COVID-19) Hospitalization Surveillance Network (COVID-NET) a network that conducts active, population-based surveillance for laboratory-confirmed COVID-19-associated hospitalizations among children and adults. COVID-NET, along with the Respiratory Syncytial Virus Hospitalization Surveillance Network (RSV-NET) and the Influenza Hospitalization Surveillance Network (FluSurv-NET), comprise the Respiratory Virus Hospitalization Surveillance Network (RESP-NET). The RESP-NET platforms have overlapping surveillance areas and use similar methods to collect data. COVID-NET is CDC\u2019s source for important data on rates of hospitalizations associated with COVID-19. Hospitalization rates show how many people in the surveillance area are hospitalized with COVID-19, compared to the total number of people residing in that area.\n\nData are preliminary and subject to change as more data become available. Data will be updated weekly.",
-            "title": "Patient Characteristics of Laboratory-Confirmed COVID-19 Hospitalizations from the COVID-NET Surveillance System",
-            "programCode": [
-                "009:038"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112258,47 +112227,55 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "COVID-NET Sites",
+            "identifier": "https://data.cdc.gov/api/views/bigw-pgk2",
+            "issued": "2023-09-22",
+            "keyword": [
+                "covid",
+                "covid19",
+                "covid-19",
+                "covidnet",
+                "covid-net",
+                "epi curve",
+                "hospitalizations",
+                "icu",
+                "in-hospital death",
+                "percent icu",
+                "percent in-hospital death",
+                "percent mechanically ventilated",
+                "respiratory illness",
+                "respiratory virus response",
+                "respnet",
+                "resp-net",
+                "surveillance"
+            ],
+            "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
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
+            "spatial": "COVID-NET Sites",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Patient Characteristics of Laboratory-Confirmed COVID-19 Hospitalizations from the COVID-NET Surveillance System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/97tt-n3j3",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
-            "keyword": [
-                "2015",
-                "chlamydia trachomatis infection",
-                "coccidioidomycosis",
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
-            "identifier": "https://data.cdc.gov/api/views/97tt-n3j3",
             "description": "NNDSS - Table II. Chlamydia to Coccidioidomycosis - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Chlamydia to Coccidioidomycosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112321,41 +112298,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/97tt-n3j3",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
+                "chlamydia trachomatis infection",
+                "coccidioidomycosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/97tt-n3j3",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-01-07",
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
+            "title": "NNDSS - Table II. Chlamydia to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/pfpx-3ynm",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-08-10",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-17",
-            "keyword": [
-                "business rules",
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
-            "identifier": "e614aeb8-580e-4aae-9140-cf55b4a22180",
             "description": "The Business Rules PUF (BR-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The BR-PUF contains plan-level data on rating business rules, such as maximum age for a dependent and allowed dependent relationships.",
-            "title": "Business Rules PUF - PY2022",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112363,37 +112345,37 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "e614aeb8-580e-4aae-9140-cf55b4a22180",
+            "issued": "2022-08-10",
+            "keyword": [
+                "business rules",
+                "exchange puf",
+                "marketplace puf",
+                "py2022"
+            ],
+            "landingPage": "https://healthdata.gov/d/pfpx-3ynm",
+            "modified": "2022-08-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Business Rules PUF - PY2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/sra",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "genetics",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jp6k-328y",
             "description": "The Sequence Read Archive (SRA) stores sequencing data from the next generation of sequencing platforms including Roche 454 GS System\u00ae, Illumina Genome Analyzer\u00ae, Life Technologies AB SOLiD System\u00ae, Helicos Biosciences Heliscope\u00ae, Complete Genomics\u00ae, and Pacific Biosciences SMRT\u00ae.",
-            "title": "Sequence Read Archive (SRA)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112402,69 +112384,68 @@
                     "title": "Sequence Read Archive (SRA) - Toolkit"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&BLAST_PROGRAMS=megaBlast&PAGE_TYPE=BlastSearch&BLAST_SPEC=SRA&SHOW_DEFAULTS=on",
-                    "description": "BLASTN programs search SRA databases using a nucleotide query. ",
                     "@type": "dcat:Distribution",
+                    "description": "BLASTN programs search SRA databases using a nucleotide query. ",
+                    "downloadURL": "https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&BLAST_PROGRAMS=megaBlast&PAGE_TYPE=BlastSearch&BLAST_SPEC=SRA&SHOW_DEFAULTS=on",
+                    "mediaType": "text/html",
                     "title": "Sequence Read Archive Nucleotide BLAST - Query Interface"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=run_browser",
-                    "description": "Search and browse data for a single RUN",
                     "@type": "dcat:Distribution",
+                    "description": "Search and browse data for a single RUN",
+                    "downloadURL": "https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=run_browser",
+                    "mediaType": "text/html",
                     "title": "SRA Run Browser - Query Interface"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Traces/study/",
-                    "description": "The Run Selector can select runs from one or more studies to download or analyze with the SRA Toolkit. To retrieve data from SRA, you must download the SRA Toolkit.",
                     "@type": "dcat:Distribution",
+                    "description": "The Run Selector can select runs from one or more studies to download or analyze with the SRA Toolkit. To retrieve data from SRA, you must download the SRA Toolkit.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Traces/study/",
+                    "mediaType": "text/html",
                     "title": "SRA Run Selector - Query Interface"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://submit.ncbi.nlm.nih.gov/subs/sra/",
-                    "description": "The SRA accepts genetic data and the associated quality scores produced by next generation sequencing technologies. Before submitting, read the SRA Submission Wizard Help. https://www.ncbi.nlm.nih.gov/sra/docs/submitportal/",
                     "@type": "dcat:Distribution",
+                    "description": "The SRA accepts genetic data and the associated quality scores produced by next generation sequencing technologies. Before submitting, read the SRA Submission Wizard Help. https://www.ncbi.nlm.nih.gov/sra/docs/submitportal/",
+                    "downloadURL": "https://submit.ncbi.nlm.nih.gov/subs/sra/",
+                    "mediaType": "text/html",
                     "title": "Sequence Read Archive (SRA) Submission Portal"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jp6k-328y",
+            "issued": "2021-06-30",
+            "keyword": [
+                "genetics",
+                "genomics",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/sra",
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
+            "title": "Sequence Read Archive (SRA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/ckve-znde",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2023-12-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-03",
-            "keyword": [
-                "api",
-                "mesh",
-                "mesh 2023 update",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ckve-znde",
             "description": "<b>(Includes MeSH 2023 changes)</b>  The MeSH 2024 Update - Split Report lists terms that are replaced by a set of terms, either descriptors or SCRs, instead of a single term.  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
-            "title": "MeSH 2024 Update - Split Report",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112487,52 +112468,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ckve-znde",
+            "issued": "2023-12-14",
+            "keyword": [
+                "api",
+                "mesh",
+                "mesh 2023 update",
+                "terminologies"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/ckve-znde",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-09-03",
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
+            "title": "MeSH 2024 Update - Split Report"
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
-            "modified": "2023-08-25",
-            "references": [
-                "https://chronicdata.cdc.gov/d/h6kq-aiu7"
-            ],
-            "keyword": [
-                "callers",
-                "cessation",
-                "intervention",
-                "national quitline data warehouse",
-                "nqdw",
-                "office on smoking and health",
-                "osh",
-                "quit",
-                "quitline",
-                "quit-now",
-                "services",
-                "state system"
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
-            "identifier": "https://data.cdc.gov/api/views/tbyb-bvjd",
+            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Services-Available-Medications-2010-To-Pr/tbyb-bvjd",
             "description": "2010-2020.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
-            "title": "Quitline \u2013 Services Available \u2013 Medications - 2010 To Present",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112555,63 +112526,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Services-Available-Medications-2010-To-Pr/tbyb-bvjd",
+            "identifier": "https://data.cdc.gov/api/views/tbyb-bvjd",
+            "issued": "2023-07-18",
+            "keyword": [
+                "callers",
+                "cessation",
+                "intervention",
+                "national quitline data warehouse",
+                "nqdw",
+                "office on smoking and health",
+                "osh",
+                "quit",
+                "quitline",
+                "quit-now",
+                "services",
+                "state system"
+            ],
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-08-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://chronicdata.cdc.gov/d/h6kq-aiu7"
+            ],
             "theme": [
                 "Quitline"
-            ]
+            ],
+            "title": "Quitline \u2013 Services Available \u2013 Medications - 2010 To Present"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://github.com/cmheilig/harvest-cdc-journals",
+            "accrualPeriodicity": "Irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-03-19",
-            "temporal": "1982 - 2023",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-22",
-            "references": [
-                "\"https://github.com/cmheilig/harvest-cdc-journals?tab=readme-ov-file\"",
-                "\"https://www.cdc.gov/mmwr/\"",
-                "\"https://wwwnc.cdc.gov/eid\"",
-                "\"https://www.cdc.gov/pcd/\""
-            ],
-            "keyword": [
-                "ai",
-                "corpora",
-                "corpus",
-                "data science",
-                "eid",
-                "harvest-cdc-journals",
-                "informatics",
-                "language",
-                "llm",
-                "machine learning",
-                "ml",
-                "mmwr",
-                "ncstltphiw",
-                "nlp",
-                "pcd",
-                "phic",
-                "text analysis"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCSTLTPHIW(PHIC) Associate Director of Informatics and Data Science",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ut5n-bmc3",
+            "describedBy": "https://github.com/cmheilig/harvest-cdc-journals?tab=readme-ov-file#cdc-text-corpora-for-learners",
             "description": "The attached ZIP archives are part of the <a href=\"https://github.com/cmheilig/harvest-cdc-journals\">CDC Text Corpora for Learners</a> program. This version, comprised of 33,567 articles, was constructed on 2024-03-01 using source content retrieved on 2024-01-09. \n\nThe attached three ZIP archives contain the 33,567  articles in 33,576 compiled HTML mirrors of the MMWR <a href=\"https://www.cdc.gov/mmwr/\">Morbidity and Mortality Weekly Report</a> including its series: <i>Weekly Reports</i>, <i>Recommendations and Reports</i>, <i>Surveillance Summaries</i>, <i>Supplements</i>, and <i>Notifiable Diseases</i>, a subset of <i>Weekly Reports</i>, constructed ad hoc; EID <a href=\"https://www.cdc.gov/eid/\">Emerging Infectious Diseases</a>; and PCD <a href=\"https://www.cdc.gov/pcd/\">Preventing Chronic Disease</a>.There is one archive per series. The archive attachments are located in the <i>About this Dataset</i> section of this landing page. In that section when you click Show More, the attachments are located in the section <i>Attachments</i>.\n\nThe retrieval and organization of the files included making as few changes to raw sources as possible, to support as many downstream uses as possible.",
-            "title": "CDC Text Corpora for Learners: HTML Mirrors of MMWR, EID, and PCD",
-            "isPartOf": "CDC Text Corpora for Learners",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112634,46 +112596,65 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://github.com/cmheilig/harvest-cdc-journals?tab=readme-ov-file#cdc-text-corpora-for-learners",
+            "identifier": "https://data.cdc.gov/api/views/ut5n-bmc3",
+            "isPartOf": "CDC Text Corpora for Learners",
+            "issued": "2024-03-19",
+            "keyword": [
+                "ai",
+                "corpora",
+                "corpus",
+                "data science",
+                "eid",
+                "harvest-cdc-journals",
+                "informatics",
+                "language",
+                "llm",
+                "machine learning",
+                "ml",
+                "mmwr",
+                "ncstltphiw",
+                "nlp",
+                "pcd",
+                "phic",
+                "text analysis"
+            ],
+            "landingPage": "https://github.com/cmheilig/harvest-cdc-journals",
             "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "accrualPeriodicity": "Irregular",
+            "modified": "2024-03-22",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "\"https://github.com/cmheilig/harvest-cdc-journals?tab=readme-ov-file\"",
+                "\"https://www.cdc.gov/mmwr/\"",
+                "\"https://wwwnc.cdc.gov/eid\"",
+                "\"https://www.cdc.gov/pcd/\""
+            ],
+            "temporal": "1982 - 2023",
             "theme": [
                 "National Center for State",
                 "Tribal",
                 "Local",
                 "and Territorial Public Health Infrastructure and Workforce"
-            ]
+            ],
+            "title": "CDC Text Corpora for Learners: HTML Mirrors of MMWR, EID, and PCD"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/datasets/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-02-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "dataset",
-                "genes",
-                "genomics",
-                "protein"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/3br9-y2tm",
             "description": "NCBI Datasets is one-stop shop for finding, browsing, and downloading genomic data. Find and download taxonomy, genome, gene, transcript, protein data, including installation of NCBI Datasets command-line tools.",
-            "title": "NCBI Datasets",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112682,36 +112663,42 @@
                     "title": "NCBI Datasets (BETA) Homepage, Search, and Utilities"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/3br9-y2tm",
+            "issued": "2022-02-09",
+            "keyword": [
+                "dataset",
+                "genes",
+                "genomics",
+                "protein"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/datasets/",
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
+            "title": "NCBI Datasets"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/d6p8-wqjm",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-03-22",
-            "temporal": "September 19, 2021-September 24, 2022",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-09",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vaccine Breakthrough Unit, Surveillance and Analytics Team",
                 "hasEmail": "mailto:vbtsurveillance@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/d6p8-wqjm",
             "description": "Data for CDC\u2019s COVID Data Tracker site on Rates of COVID-19 Cases and Deaths by Vaccination Status.\nClick 'More' for important dataset description and footnotes\n\nDataset and data visualization details:\nThese data were posted on October 21, 2022, archived on November 18, 2022, and revised on February 22, 2023. These data reflect cases among persons with a positive specimen collection date through September 24, 2022, and deaths among persons with a positive specimen collection date through September 3, 2022. \n\nVaccination status: A person vaccinated with a primary series had SARS-CoV-2 RNA or antigen detected on a respiratory specimen collected \u226514 days after verifiably completing the primary series of an FDA-authorized or approved COVID-19 vaccine. An unvaccinated person had SARS-CoV-2 RNA or antigen detected on a respiratory specimen and has not been verified to have received COVID-19 vaccine. Excluded were partially vaccinated people who received at least one FDA-authorized vaccine dose but did not complete a primary series \u226514 days before collection of a specimen where SARS-CoV-2 RNA or antigen was detected.\nAdditional or booster dose: A person vaccinated with a primary series and an additional or booster dose had SARS-CoV-2 RNA or antigen detected on a respiratory specimen collected \u226514 days after receipt of an additional or booster dose of any COVID-19 vaccine on or after August 13, 2021. For people ages 18 years and older, data are graphed starting the week including September 24, 2021, when a COVID-19 booster dose was first recommended by CDC for adults 65+ years old and people in certain populations and high risk occupational and institutional settings. For people ages 12-17 years, data are graphed starting the week of December 26, 2021, 2 weeks after the first recommendation for a booster dose for adolescents ages 16-17 years. For people ages 5-11 years, data are included starting the week of June 5, 2022, 2 weeks after the first recommendation for a booster dose for children aged 5-11 years. For people ages 50 years and older, data on second booster doses are graphed starting the week including March 29, 2022, when the recommendation was made for second boosters. Vertical lines represent dates when changes occurred in U.S. policy for COVID-19 vaccination (details provided above). Reporting is by primary series vaccine type rather than additional or booster dose vaccine type. The booster dose vaccine type may be different than the primary series vaccine type.\n** Because data on the immune status of cases and associated deaths are unavailable, an additional dose in an immunocompromised person cannot be distinguished from a booster dose. This is a relevant consideration because vaccines can be less effective in this group.\nDeaths: A COVID-19\u2013associated death occurred in a person with a documented COVID-19 diagnosis who died; health department staff reviewed to make a determination using vital records, public health investigation, or other data sources. Rates of COVID-19 deaths by vaccination status are reported based on when the patient was tested for COVID-19, not the date they died. Deaths usually occur up to 30 days after COVID-19 diagnosis.\nParticipating jurisdictions: Currently, these 31 health departments that regularly link their case surveillance to immunization information system data are included in these incidence rate estimates: Alabama, Arizona, Arkansas, California, Colorado, Connecticut, District of Columbia, Florida, Georgia, Idaho, Indiana, Kansas, Kentucky, Louisiana, Massachusetts, Michigan, Minnesota, Nebraska, New Jersey, New Mexico, New York, New York City (New York), North Carolina, Philadelphia (Pennsylvania), Rhode Island, South Dakota, Tennessee, Texas, Utah, Washington, and West Virginia; 30 jurisdictions also report deaths among vaccinated and unvaccinated people. These jurisdictions represent 72% of the total U.S. population and all ten of the Health and Human Services Regions. Data on cases",
-            "title": "Rates of COVID-19 Cases or Deaths by Age Group and Vaccination Status and Booster Dose",
-            "programCode": [
-                "009:038"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112734,46 +112721,41 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Select US Jurisdictions",
+            "identifier": "https://data.cdc.gov/api/views/d6p8-wqjm",
+            "issued": "2022-03-22",
+            "landingPage": "https://data.cdc.gov/d/d6p8-wqjm",
+            "language": [
+                "English"
+            ],
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2023-06-09",
+            "programCode": [
+                "009:038"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "Select US Jurisdictions",
+            "temporal": "September 19, 2021-September 24, 2022",
             "theme": [
                 "Public Health Surveillance"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Rates of COVID-19 Cases or Deaths by Age Group and Vaccination Status and Booster Dose"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-18",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-09-11",
-            "keyword": [
-                "adults",
-                "iqvia",
-                "rsv vaccination"
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
-            "identifier": "https://data.cdc.gov/api/views/a3gi-4phs",
             "description": "Weekly Cumulative Estimated Number of RSV Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 60 Years and Older, United States\n\n\u2022 Estimated Number of RSV vaccinations among adults 60 years and older is assessed through IQVIA (https://www.iqvia.com/) as a source of information on vaccinations administered in retail pharmacies (include chain, mass merchandise, food stores, and independent pharmacies) and physician medical offices.\n\n\u2022 Starting in September 2023, the CDC recommended the RSV vaccine for adults 60 years and older.",
-            "title": "Weekly Cumulative Estimated Number of RSV Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 60 years and older, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112796,43 +112778,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/a3gi-4phs",
+            "issued": "2023-12-18",
+            "keyword": [
+                "adults",
+                "iqvia",
+                "rsv vaccination"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2024-09-11",
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
+            "title": "Weekly Cumulative Estimated Number of RSV Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 60 years and older, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/tiss/index.cfm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2008-04-10",
-            "keyword": [
-                "cber"
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
-            "identifier": "dc73689d-c8cc-4c9f-b3ee-c293483dbdb7",
             "description": "This application provides Human Cell and Tissue registration information for registered, inactive, and pre-registered firms. Query options are by Establishment Name, Establishment Function, Product, Establishment Status, State, Zip Code, and Country.",
-            "title": "Human Cell and Tissue Establishment Registration Public Query",
-            "programCode": [
-                "009:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112840,35 +112824,36 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "dc73689d-c8cc-4c9f-b3ee-c293483dbdb7",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cber"
+            ],
+            "landingPage": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/tiss/index.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2008-04-10",
+            "programCode": [
+                "009:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Human Cell and Tissue Establishment Registration Public Query"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/pjzq-t23s",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-10-14",
-            "@type": "dcat:Dataset",
-            "modified": "2021-10-13",
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
-            "identifier": "1fee67f0-ee42-4cf5-b764-4bf7e2610fe0",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210802 to 20210808",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112876,44 +112861,35 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "1fee67f0-ee42-4cf5-b764-4bf7e2610fe0",
+            "issued": "2021-10-14",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/pjzq-t23s",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2021-10-13",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210802 to 20210808"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kpbd-vsd5",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "imported",
-                "indigenous",
-                "malaria",
-                "measles",
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
-            "identifier": "https://data.cdc.gov/api/views/kpbd-vsd5",
             "description": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112936,35 +112912,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kpbd-vsd5",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "imported",
+                "indigenous",
+                "malaria",
+                "measles",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/kpbd-vsd5",
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
+            "title": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/76u3-26ik",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division, Physical Effects Research Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/76u3-26ik",
             "description": "To protect residential roofing construction workers from both fatal and musculoskeletal injuries, it is necessary to assess the musculoskeletal and biomechanical risks in residential roofing tasks. This undertaking requires accurate information of workers\u2019 3D body positions to analyze kinematics and kinetics of the human body. In this study, we proposed a novel 2- stage motion estimation approach based on a convolution neural network to estimate residential roofer\u2019s body positions using three-view video data. Instead of pursuing end-to- end training, our approach includes two stages: (1) use a multi-view model to estimate the 3D pose in a single frame; (2) use a multi-frame model to apply temporal convolutions to refine the multi-view outputs. The performance of the approach was evaluated by comparing our estimation with the gold-standard marker-based 3D human pose estimation (\u201cground truth\u201d). The evaluation results show that our marker-free video-based approach can accurately capture the 3D posture of workers during the common roofing task and the proposed multi-frame model can effectively improve the precision of the coordinate sequence. The values of mean per joint position error of estimated human position before and after processing by the multi-frame model are 27.93 and 24.81 mm, respectively. These results prove that the proposed marker-free motion capture estimation approach can efficiently and accurately locate 3D body joints and pave the way for future onsite musculoskeletal motion analysis during roofing activities.",
-            "title": "Video-Based 3D pose estimation for residential roofing-dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -112972,81 +112959,81 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/76u3-26ik",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/76u3-26ik",
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
+            "title": "Video-Based 3D pose estimation for residential roofing-dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/pn26-36bb",
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
-            "identifier": "92926a98-0f8c-5a43-9e83-d9239fb485a3",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard filters v2.11.9 (prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/filters.csv",
-                    "description": "Scorecard filters v2.11.9 (prod)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard filters v2.11.9 (prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard filters v2.11.9 (prod)"
                 }
             ],
+            "identifier": "92926a98-0f8c-5a43-9e83-d9239fb485a3",
+            "issued": "2023-07-22",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/pn26-36bb",
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
+            "title": "Scorecard filters v2.11.9 (prod)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/wtvk-6zfr",
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
-            "identifier": "https://data.cdc.gov/api/views/wtvk-6zfr",
             "description": "SARS-CoV-2 can be spread by droplets and aerosols expelled by infected people when they cough, talk, sing, or exhale. To reduce exposure to these droplets and aerosols while indoors, CDC recommends measures including physical distancing, universal mask wearing, and room ventilation. Ventilation systems can be supplemented with portable air cleaners to remove infectious material from the air more quickly and provide greater protection. We conducted a case study using respiratory simulators to examine the efficacy of portable High Efficiency Particulate Air (HEPA) air cleaners and universal masking at reducing exposure to simulated exhaled aerosol particles from an infected meeting participant in a conference room. We found that, in a room with good air mixing, the use of two HEPA air cleaners meeting the EPA recommended Clean Air Delivery Rate (CADR) reduced the overall exposure by up to 65%, and that the combination of the HEPA air cleaners and universal masking reduced exposure by up to 90%. The air cleaners were most effective when they were close to the aerosol source. Our results demonstrate that portable HEPA cleaners can be an effective method to reduce exposure to airborne particles while meeting indoors, especially in combination with universal masking.",
-            "title": "Efficacy of Portable Air Cleaners and Masking for Reducing Indoor Exposure to Simulated Exhaled SARS-CoV-2 Aerosols \u2014 United States, 2021",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -113054,24 +113041,46 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wtvk-6zfr",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/wtvk-6zfr",
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
+            "title": "Efficacy of Portable Air Cleaners and Masking for Reducing Indoor Exposure to Simulated Exhaled SARS-CoV-2 Aerosols \u2014 United States, 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-state",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2015-06-01",
-            "references": [
-                "https://www.healthit.gov/data/quickstats/percent-rec-enrolled-critical-access-and-rural-hospitals-state-demonstrating",
-                "https://www.healthit.gov/data/quickstats/percent-rec-enrolled-priority-primary-care-providers-ppcps-state-demonstrating"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-state",
+            "description": "The ONC Regional Extension Centers (REC) Program provides assistance to health care providers to adopt and meaningfully use certified EHR technology. The program, funded through the American Recovery and Reinvestment Act (ARRA) or The Recovery Act, provides grants to organizations, Regional Extension Centers, that assist providers directly in the organization's region. There are 62 unique RECs across the United States. This data set provides county-level health care professional participation in the REC Program. You can track metrics on the total primary care and non-primary care providers that signed up for REC assistance, gone live with an EHR, and demonstrated meaningful use of certified EHR technology. See ONC's REC data by state to track these metrics at the state level.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/REC_KPI_State.csv",
+                    "mediaType": "text/csv",
+                    "title": "REC_KPI_State.csv"
+                }
             ],
+            "identifier": "zyaifc3t-i181-2wnr-j3fu-j6qo40bbttxx",
+            "issued": "2023-10-03",
             "keyword": [
                 "health information technology",
                 "health it",
@@ -113081,103 +113090,81 @@
                 "regional extension centers",
                 "state"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-state",
+            "modified": "2015-06-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "zyaifc3t-i181-2wnr-j3fu-j6qo40bbttxx",
-            "description": "The ONC Regional Extension Centers (REC) Program provides assistance to health care providers to adopt and meaningfully use certified EHR technology. The program, funded through the American Recovery and Reinvestment Act (ARRA) or The Recovery Act, provides grants to organizations, Regional Extension Centers, that assist providers directly in the organization's region. There are 62 unique RECs across the United States. This data set provides county-level health care professional participation in the REC Program. You can track metrics on the total primary care and non-primary care providers that signed up for REC assistance, gone live with an EHR, and demonstrated meaningful use of certified EHR technology. See ONC's REC data by state to track these metrics at the state level.",
-            "title": "ONC Regional Extension Centers (REC) Key Performance Indicators (KPIs) by State",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/REC_KPI_State.csv",
-                    "mediaType": "text/csv",
-                    "title": "REC_KPI_State.csv"
-                }
+            "references": [
+                "https://www.healthit.gov/data/quickstats/percent-rec-enrolled-critical-access-and-rural-hospitals-state-demonstrating",
+                "https://www.healthit.gov/data/quickstats/percent-rec-enrolled-priority-primary-care-providers-ppcps-state-demonstrating"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-state"
+            "title": "ONC Regional Extension Centers (REC) Key Performance Indicators (KPIs) by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/pnsv-sqfk",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-08-27",
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
-            "identifier": "103806a7-aed4-5f01-ad27-c3fccbe2694a",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_brief",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/brief.csv",
-                    "description": "{\"dataset\": \"brief\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"brief\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/brief.csv",
+                    "mediaType": "text/csv",
                     "title": "brief csv file"
                 }
             ],
+            "identifier": "103806a7-aed4-5f01-ad27-c3fccbe2694a",
+            "issued": "2024-08-27",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/pnsv-sqfk",
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
+            "title": "prodAuto_brief"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/eddk-effy",
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
-            "identifier": "https://data.cdc.gov/api/views/eddk-effy",
             "description": "Growing evidence suggests that Gulf War Illness (GWI) is the result of underlying neuroimmune dysfunction.  For example, previously we found that several Gulf War-relevant organophosphate, acetylcholinesterase inhibitors produce heightened neuroinflammatory responses following a sub chronic stressor exposure.  The goal of the study was to evaluate the potential for the \u03b2-adrenergic receptor inhibitor and anti-inflammatory drug, propranolol, to treat neuroinflammation in a novel long-term mouse model of GWI. We established that our long-term GWI model produces enhanced and prolonged neuroinflammation that is dependent upon Gulf War-relevant organophosphate exposure. Propranolol treatment abrogated the neuroinflammation instigated in our model specifically, having no treatment effects in non-DFP exposed groups. Our results indicate that propranolol may be a promising therapy for GWI by treating the underlying neuroinflammation associated with Gulf War-relevant physiological stress and organophosphate exposures.",
-            "title": "The \u03b2-adrenergic receptor blocker and anti-inflammatory drug propranolol mitigates brain cytokine expression in a long-term model of Gulf War Illness",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -113185,48 +113172,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/eddk-effy",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/eddk-effy",
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
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-02-23",
-            "temporal": "2000/2016",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-18",
-            "keyword": [
-                "american indian or alaska native",
-                "asian or pacific islander",
-                "births",
-                "black or african american",
-                "child and adolescent",
-                "health risk factors",
-                "health us",
-                "hispanic or latino",
-                "state",
-                "white"
+            ],
+            "title": "The \u03b2-adrenergic receptor blocker and anti-inflammatory drug propranolol mitigates brain cytokine expression in a long-term model of Gulf War Illness"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "Annual",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:healthus@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/dj4t-wmry",
             "description": "Data on Low birthweight live births, by race and Hispanic origin of mother, state, and territory in the United States and U.S. dependent areas. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Vital Statistics System, Birth File.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Low birthweight live births, by race and Hispanic origin of mother, state, and territory: United States and U.S. dependent areas",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -113249,22 +113224,65 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/dj4t-wmry",
+            "issued": "2024-02-23",
+            "keyword": [
+                "american indian or alaska native",
+                "asian or pacific islander",
+                "births",
+                "black or african american",
+                "child and adolescent",
+                "health risk factors",
+                "health us",
+                "hispanic or latino",
+                "state",
+                "white"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "modified": "2024-09-18",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2000/2016",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS Low birthweight live births, by race and Hispanic origin of mother, state, and territory: United States and U.S. dependent areas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/panel-study-income-dynamics-psid",
             "bureauCode": [
                 "001:05"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Panel Study of Income Dynamics Help",
+                "hasEmail": "mailto:psidhelp@umich.edu"
+            },
+            "dataQuality": true,
+            "description": "<p>The Panel Study of Income Dynamics (PSID) began in 1968 with a nationally representative sample of over 18,000 individuals living in 5,000 families in the United States. Information on these individuals and their descendants has been collected continuously, including data covering employment, income, wealth, expenditures, health, marriage, childbearing, child development, philanthropy, education, and numerous other topics.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://psidonline.isr.umich.edu/Studies.aspx",
+                    "mediaType": "text/html",
+                    "title": "Text "
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://simba.isr.umich.edu/default.aspx",
+                    "mediaType": "text/html",
+                    "title": "Text "
+                }
+            ],
+            "identifier": "b2a0bdee-117e-48e5-ad0c-f9982e05281a",
             "issued": "2014-04-08",
-            "temporal": "1968-01-01T00:00:00-05:00/1968-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "adulthood",
                 "aging",
@@ -113285,76 +113303,40 @@
                 "transitions",
                 "wealth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Panel Study of Income Dynamics Help",
-                "hasEmail": "mailto:psidhelp@umich.edu"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
-            },
-            "identifier": "b2a0bdee-117e-48e5-ad0c-f9982e05281a",
-            "description": "<p>The Panel Study of Income Dynamics (PSID) began in 1968 with a nationally representative sample of over 18,000 individuals living in 5,000 families in the United States. Information on these individuals and their descendants has been collected continuously, including data covering employment, income, wealth, expenditures, health, marriage, childbearing, child development, philanthropy, education, and numerous other topics.</p>",
-            "title": "The Panel Study of Income Dynamics (PSID)",
+            "landingPage": "https://healthdata.gov/dataset/panel-study-income-dynamics-psid",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:048"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://psidonline.isr.umich.edu/Studies.aspx",
-                    "mediaType": "text/html",
-                    "title": "Text "
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://simba.isr.umich.edu/default.aspx",
-                    "mediaType": "text/html",
-                    "title": "Text "
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1968-01-01T00:00:00-05:00/1968-01-01T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "The Panel Study of Income Dynamics (PSID)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/47ru-cshp",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-09-21",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "chemicals",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/47ru-cshp",
             "description": "ChemIDplus, the Chemical Identification Plus Database, is no longer updated. These are the final files from February 22, 2023. All ChemIDplus data have been incorporated into PubChem.\n\nChemIDplus was a dictionary of over 400,000 chemicals (names, synonyms, and structures). ChemIDplus includes links to NLM and other databases and resources, including links to federal, state and international agencies.  NLM makes a subset of ChemIDplus data available for download. The ChemIDplus Subset does not include the structure or the toxicity data available from the NLM web versions of the database. The ChemIDplus Subset is updated monthly.",
-            "title": "ChemIDplus",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/chemidlease/",
-                    "description": "ChemIDplus is no longer updated. These are the final files from February 22, 2023. All ChemIDplus data have been incorporated into PubChem. ",
                     "@type": "dcat:Distribution",
+                    "description": "ChemIDplus is no longer updated. These are the final files from February 22, 2023. All ChemIDplus data have been incorporated into PubChem. ",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/chemidlease/",
+                    "mediaType": "text/html",
                     "title": "Download ChemIDplus Subset Data"
                 },
                 {
@@ -113364,40 +113346,40 @@
                     "title": "Download ChemIDplus Sample Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/47ru-cshp",
+            "issued": "2020-09-21",
+            "keyword": [
+                "chemicals",
+                "chemistry",
+                "dataset"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/47ru-cshp",
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
                 "Drugs and Chemicals"
-            ]
+            ],
+            "title": "ChemIDplus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/e9r5-5hjr",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-08-10",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "americas",
-                "chikungunya",
-                "paho"
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
-            "identifier": "https://data.cdc.gov/api/views/e9r5-5hjr",
             "description": "Derived from Pan American Health Organization reports: http://www.paho.org/hq/index.php?option=com_topics&view=article&id=343&Itemid=40931",
-            "title": "New Chikungunya Cases Reported in the Americas",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -113420,132 +113402,135 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/e9r5-5hjr",
+            "issued": "2015-08-10",
+            "keyword": [
+                "americas",
+                "chikungunya",
+                "paho"
+            ],
+            "landingPage": "https://data.cdc.gov/d/e9r5-5hjr",
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
+            "title": "New Chikungunya Cases Reported in the Americas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/pqz3-as22",
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
-            "identifier": "be70cb98-52f4-5254-8fe9-f8dcb34f5f45",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt filters v2.10.23 (coreset-prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.23/20241029/filters.csv",
-                    "description": "CoreSEt filters v2.10.23 (coreset-prod)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt filters v2.10.23 (coreset-prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.23/20241029/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt filters v2.10.23 (coreset-prod)"
                 }
             ],
+            "identifier": "be70cb98-52f4-5254-8fe9-f8dcb34f5f45",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/pqz3-as22",
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
+            "title": "CoreSEt filters v2.10.23 (coreset-prod)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/psa5-qby7",
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
-            "identifier": "fe72018c-0f13-5f58-b58b-20bf988645bc",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_concernLevel",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/concernLevel.csv",
-                    "description": "{\"dataset\": \"concernLevel\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"concernLevel\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/concernLevel.csv",
+                    "mediaType": "text/csv",
                     "title": "concernLevel csv file"
                 }
             ],
+            "identifier": "fe72018c-0f13-5f58-b58b-20bf988645bc",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/psa5-qby7",
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
+            "title": "devAuto_concernLevel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/psgy-3uyv",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-06",
-            "keyword": [
-                "medicaid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Vaughn",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "1b03ec9b-07dd-4547-99a5-aacf206162d5",
             "description": "Notes:\r\n1. CAA 2023 provides a temporary 5.0 percentage point FMAP increase to each qualifying state and territory's FMAP under section 1905(b) of the Act, beginning April 1, 2023 through June 30, 2023.\t\t\t\t\t\t\t\r\n2. CAA 2023 provides a temporary 2.5 percentage point FMAP increase to each qualifying state and territory's FMAP under section 1905(b) of the Act, beginning July 1, 2023 through September 30, 2023.\t\t\t\t\t\t\t\r\n3. CAA 2023 provides a temporary 1.5 percentage point FMAP increase to each qualifying state and territory's FMAP under section 1905(b) of the Act, beginning October 1, 2023 through December 31, 2023.\t\t\t\t\t\t\t\r\n4. States that have reported \u201c0\u201d either have no expenditures for that reporting category or have not yet reported expenditures for that category. \t\t\t\t\t\t\t\r\n5. This report is a cumulative summary report that includes current and prior period adjustment expenditures that apply to this quarter and does not include Collections or Overpayment Recoveries.",
-            "title": "Medicaid CMS-64 CAA 2023 Increased FMAP Expenditure Data Collected through MBES/CBES",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -113554,39 +113539,36 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "1b03ec9b-07dd-4547-99a5-aacf206162d5",
+            "issued": "2024-03-27",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/psgy-3uyv",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2025-01-06",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Medicaid CMS-64 CAA 2023 Increased FMAP Expenditure Data Collected through MBES/CBES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/psqj-8ru8",
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
-                "rate"
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
-            "identifier": "e6deb20e-dd27-495b-8eb1-c67db7bbd788",
             "description": "The Rate PUF (Rate-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Rate-PUF contains plan-level data on rates based on an eligible subscriber\u2019s age, tobacco use, and geographic location; and family-tier rates.",
-            "title": "Rate PUF \u2013 PY2023",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -113594,32 +113576,37 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "e6deb20e-dd27-495b-8eb1-c67db7bbd788",
+            "issued": "2023-08-09",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2023",
+                "rate"
+            ],
+            "landingPage": "https://healthdata.gov/d/psqj-8ru8",
+            "modified": "2023-08-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Rate PUF \u2013 PY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.datasetcatalog.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2024-11-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Library of Medicine",
                 "hasEmail": "mailto:custserv@nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Library of Medicine"
-            },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/k6qs-qncs",
             "description": "The Dataset Catalog (beta)is a catalog of biomedical datasets from various repositories for users to search, discover, retrieve, and connect with datasets to accelerate scientific research. This beta version aims to collect user feedback to inform future product development.",
-            "title": "Dataset Catalog (beta)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -113628,40 +113615,36 @@
                     "title": "Dataset Catalog (beta) Homepage and Search"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/k6qs-qncs",
+            "issued": "2024-11-04",
+            "landingPage": "https://www.datasetcatalog.nlm.nih.gov/",
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
                 "Research"
-            ]
+            ],
+            "title": "Dataset Catalog (beta)"
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
-            "identifier": "https://data.cdc.gov/api/views/ithv-4e9m",
             "description": "\u2022 COVID-19 vaccination coverage and parental intent among children 6 months to 17 years is assessed through the National Immunization Survey providing weekly COVID-19 vaccination coverage estimates (https://www.cdc.gov/vaccines/imz-managers/nis/about.html). \n\n\u2022 Weekly estimates of COVID-19 vaccination coverage and parental intent for vaccination among children through December 31, 2023, were calculated using data from the National Immunization Survey-Child COVID Module (NIS-CCM). Beginning January 2, 2024, the NIS-CCM was discontinued, and questions regarding receipt of COVID-19 vaccination among children were added to the NIS-Flu (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-cim). \n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19.",
-            "title": "Weekly Parental Intent for Vaccination and Cumulative Percentage of Children 6 Months-17 Years who are up to date with the updated 2023-24 COVID-19 Vaccine",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -113684,45 +113667,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/ithv-4e9m",
+            "issued": "2023-11-07",
+            "keyword": [
+                "covid-19 vaccination",
+                "nis-ccm"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/children-coverage-vaccination.html",
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
+            "spatial": "United States- National, Region, State",
+            "temporal": "2023-2024",
             "theme": [
                 "Child Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Parental Intent for Vaccination and Cumulative Percentage of Children 6 Months-17 Years who are up to date with the updated 2023-24 COVID-19 Vaccine"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://aspe.hhs.gov/pdf-report/vaccine-hesitancy",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-05-17",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-17",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "vaccine hesitancy"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HHS",
                 "hasEmail": "mailto:joel.ruhter@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/q9mh-h2tw",
             "description": "Due to the change in the survey instrument regarding intention to vaccinate, our estimates for \u201chesitant or unsure\u201d or \u201chesitant\u201d derived from April 14-26, 2021, are not directly comparable with prior Household Pulse Survey data and should not be used to examine trends in hesitancy.\n\nTo support state and local communication and outreach efforts, ASPE developed state, county, and sub-state level predictions of hesitancy rates (https://aspe.hhs.gov/pdf-report/vaccine-hesitancy) using the most recently available federal survey data.\n\nWe estimate hesitancy rates at the state level using the U.S. Census Bureau\u2019s Household Pulse Survey (HPS) (https://www.census.gov/programs-surveys/household-pulse-survey.html) data and utilize the estimated values to predict hesitancy rates at the Public Use Microdata Areas (PUMA) level using the Census Bureau\u2019s 2019 American Community Survey (ACS) 1-year Public Use Microdata Sample (PUMS)(https://www.census.gov/programs-surveys/acs/microdata.html). To create county-level estimates, we used a PUMA-to-county crosswalk from the Missouri Census Data Center(https://mcdc.missouri.edu/applications/geocorr2014.html). PUMAs spanning multiple counties had their estimates apportioned across those counties based on overall 2010 Census populations.\n\nThe HPS is nationally representative and includes information on U.S. residents\u2019 intentions to receive the COVID-19 vaccine when available, as well as other sociodemographic and geographic (state, region and metropolitan statistical areas) information. The ACS is a nationally representative survey, and it provides key sociodemographic and geographic (state, region, PUMAs, county) information. We utilized data for the survey collection period May 26, 2021 \u2013 June 7, 2021, which the HPS refers to as Week 31..\n\nPUMA COVID-19 Hesitancy Data - https://data.cdc.gov/Vaccinations/Vaccine-Hesitancy-for-COVID-19-Public-Use-Microdat/djj9-kh3p",
-            "title": "Vaccine Hesitancy for COVID-19: County and local estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -113745,53 +113727,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/q9mh-h2tw",
+            "issued": "2021-05-17",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "vaccine hesitancy"
+            ],
+            "landingPage": "https://aspe.hhs.gov/pdf-report/vaccine-hesitancy",
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
+            "title": "Vaccine Hesitancy for COVID-19: County and local estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2019-12-05",
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
-                "gis",
-                "outcomes",
-                "prevalence",
-                "prevention",
-                "tract",
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
-            "identifier": "https://data.cdc.gov/api/views/pf7q-w24q",
             "description": "2016, 2015. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project city-level data in GIS-friendly format can be joined with city spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-City-Boundaries/n44h-hy2j) in a geographic information system (GIS) to produce maps of 27 measures at the city-level. There are 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, cholesterol screening) in this 2018 release from the 2015 BRFSS that were the same as the 2017 release.",
-            "title": "500 Cities: City-level Data (GIS Friendly Format), 2018 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -113814,41 +113783,54 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/pf7q-w24q",
+            "issued": "2019-12-05",
+            "keyword": [
+                "500cities",
+                "behaviors",
+                "census",
+                "cities",
+                "gis",
+                "outcomes",
+                "prevalence",
+                "prevention",
+                "tract",
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
+            "title": "500 Cities: City-level Data (GIS Friendly Format), 2018 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/pvu5-a2vy",
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
-                "network",
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
-            "identifier": "e164fcba-c5fb-4d81-97a9-882e98a69325",
             "description": "The Network PUF (Ntwrk-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Ntwrk-PUF contains issuer-level data identifying provider network URLs.",
-            "title": "Network PUF - PY2023",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -113856,18 +113838,40 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "e164fcba-c5fb-4d81-97a9-882e98a69325",
+            "issued": "2023-08-09",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "network",
+                "py2023"
+            ],
+            "landingPage": "https://healthdata.gov/d/pvu5-a2vy",
+            "modified": "2023-08-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Network PUF - PY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/custodial-parents-living-poverty",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dennis Putze",
+                "hasEmail": "mailto:dennis.putze@acf.hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Office of Child Support Enforecment (OCSE) Story Behind the Numbers - Child Support Fact Sheet #3.  This fact sheet focuses on data reported in a recent U.S. Census Bureau report, Custodial Mothers and Fathers and Their Child Support: 2011. The data reported are estimated based on a biennial survey of custodial parents, the Child Support Supplement to the Current Population Survey, March/April 2012, co-sponsored by the Office of Child Support Enforcement.  The proportion of custodial parents living below poverty line continues to increase in 2011. The report found that 4.2 million custodial parents lived in poverty in 2011, representing 29 percent of all custodial parents, about twice the poverty rate for the total population. These statistics reinforce the essential role that child support services can play in helping low-income families, especially during an economic downturn.</p>",
+            "identifier": "65f41ddb-094b-4181-a85a-ce55a945312e",
             "issued": "2014-02-10",
-            "temporal": "2011-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "administrative",
                 "arrears management",
@@ -113884,54 +113888,35 @@
                 "story behind the numbers",
                 "us census bureau"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dennis Putze",
-                "hasEmail": "mailto:dennis.putze@acf.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/custodial-parents-living-poverty",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:103"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Administration for Children and Families, Department of Health & Human Services"
             },
-            "identifier": "65f41ddb-094b-4181-a85a-ce55a945312e",
-            "description": "<p>Office of Child Support Enforecment (OCSE) Story Behind the Numbers - Child Support Fact Sheet #3.  This fact sheet focuses on data reported in a recent U.S. Census Bureau report, Custodial Mothers and Fathers and Their Child Support: 2011. The data reported are estimated based on a biennial survey of custodial parents, the Child Support Supplement to the Current Population Survey, March/April 2012, co-sponsored by the Office of Child Support Enforcement.  The proportion of custodial parents living below poverty line continues to increase in 2011. The report found that 4.2 million custodial parents lived in poverty in 2011, representing 29 percent of all custodial parents, about twice the poverty rate for the total population. These statistics reinforce the essential role that child support services can play in helping low-income families, especially during an economic downturn.</p>",
-            "title": "Custodial Parents Living in Poverty",
-            "programCode": [
-                "009:103"
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "2011-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "Custodial Parents Living in Poverty"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/px3f-paf3",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-06-06",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-05",
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
-            "identifier": "4fca2c9b-d0d2-4016-8e60-644f6d552a81",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-29-to-2023-06-04",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -113940,39 +113925,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-29-to-2023-06-04"
                 }
             ],
+            "identifier": "4fca2c9b-d0d2-4016-8e60-644f6d552a81",
+            "issued": "2023-06-06",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/px3f-paf3",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-06-05",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-29-to-2023-06-04"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/projects/genotyping/formpage.cgi",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-07-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dataset",
-                "genomics",
-                "tools & utilities",
-                "virus"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ftac-bfk9",
             "description": "This tool helps identify the genotype of a viral sequence.",
-            "title": "Viral Genotyping Tool",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -113981,40 +113962,42 @@
                     "title": "Viral Genotyping Tool - Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ftac-bfk9",
+            "issued": "2021-07-01",
+            "keyword": [
+                "dataset",
+                "genomics",
+                "tools & utilities",
+                "virus"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/projects/genotyping/formpage.cgi",
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
+            "title": "Viral Genotyping Tool"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/py3k-6dws",
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
-            "identifier": "602e7c79-774d-529a-a377-75faa749e878",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 1994",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -114022,46 +114005,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "602e7c79-774d-529a-a377-75faa749e878",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/py3k-6dws",
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
+            "title": "State Drug Utilization Data 1994"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rihk-iawc",
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
-                "smallpox",
-                "spotted fever rickettsiosis confirmed",
-                "spotted fever rickettsiosis probable",
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
-            "identifier": "https://data.cdc.gov/api/views/rihk-iawc",
             "description": "NNDSS - TABLE 1GG.  Spotted fever rickettsiosis, Confirmed to Smallpox - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1GG. Spotted fever rickettsiosis, Confirmed to Smallpox",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -114084,43 +114061,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rihk-iawc",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "smallpox",
+                "spotted fever rickettsiosis confirmed",
+                "spotted fever rickettsiosis probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rihk-iawc",
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
+            "title": "NNDSS - TABLE 1GG. Spotted fever rickettsiosis, Confirmed to Smallpox"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/pwgb-7r9t",
+            "accrualPeriodicity": "n/a",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "Public access to full dataset except age.  For age, reach out to point of contact",
-            "issued": "2019-03-14",
-            "@type": "dcat:Dataset",
-            "temporal": "N/A",
-            "modified": "2019-03-14",
-            "keyword": [
-                "antibody",
-                "chlamydia trachomatis",
-                "division of parasitic diseases and malaria",
-                "latent class"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ryan E. Wiegand",
                 "hasEmail": "mailto: fwk2@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/pwgb-7r9t",
+            "describedBy": "https://www.nature.com/articles/s41598-018-22708-9",
             "description": "This set includes data used in a latent class model to compare testing platforms for detection of antibodies against the Chlamydia trachomatis antigen Pgp3.  The analysis was published as: Latent class modeling to compare testing platforms for detection of antibodies against the Chlamydia trachomatis antigen Pgp3. Wiegand RE, Cooley G, Goodhew B, Banniettis N, Kohlhoff S, Gwyn S, Martin DL. Sci Rep. 2018 Mar 9;8(1):4232. doi: 10.1038/s41598-018-22708-9. PMID: 29523810",
-            "title": "Tests for antibodies to trachoma PGP3 antigen",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -114143,52 +114124,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "samples from patients from Africa and New York",
-            "describedBy": "https://www.nature.com/articles/s41598-018-22708-9",
+            "identifier": "https://data.cdc.gov/api/views/pwgb-7r9t",
+            "issued": "2019-03-14",
+            "keyword": [
+                "antibody",
+                "chlamydia trachomatis",
+                "division of parasitic diseases and malaria",
+                "latent class"
+            ],
+            "landingPage": "https://data.cdc.gov/d/pwgb-7r9t",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "n/a",
+            "modified": "2019-03-14",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "rights": "Public access to full dataset except age.  For age, reach out to point of contact",
+            "spatial": "samples from patients from Africa and New York",
+            "temporal": "N/A",
             "theme": [
                 "Global Health"
-            ]
+            ],
+            "title": "Tests for antibodies to trachoma PGP3 antigen"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
             "bureauCode": [
                 "009:20"
             ],
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
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DDT Public Inquiries",
                 "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/bwx3-gx66",
+            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Private-Medicaid-Claims-MAX-Vision-and-Eye-Health-/bwx3-gx66",
             "description": "2016-2019. This dataset is a de-identified summary table of prevalence rates for vision and eye health data indicators from the Medicaid Analytic eXtract (MAX) data. Medicaid MAX are a set of de-identified person-level data files with information on Medicaid eligibility, service utilization, diagnoses, and payments. The MAX data contain a convenience sample of claims processed by Medicaid and Children\u2019s Health Insurance Program (CHIP) fee for service and managed care plans.  Not all states are included in MAX in all years, and as of November 2019, 2014 data is the latest available.  Prevalence estimates are stratified by all available combinations of age group, gender, and state.  Detailed information on VEHSS Medicare analyses can be found on the VEHSS Medicaid MAX webpage (cdc.gov/visionhealth/vehss/data/claims/medicaid.html). Information on available Medicare claims data can be found on the ResDac website (www.resdac.org). The VEHSS Medicaid MAX dataset was last updated May 2023.",
-            "title": "Medicaid Claims (MAX) - Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -114211,49 +114185,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Private-Medicaid-Claims-MAX-Vision-and-Eye-Health-/bwx3-gx66",
+            "identifier": "https://data.cdc.gov/api/views/bwx3-gx66",
+            "issued": "2023-09-21",
+            "keyword": [
+                "claims",
+                "diagnosed prevalence",
+                "eye exams",
+                "max",
+                "medicaid",
+                "medical diagnoses",
+                "screening",
+                "service utilization"
+            ],
+            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-09-21",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://wwwdev.cdc.gov/visionhealth/vehss/data/claims/medicaid.html",
+                "https://www.medicaid.gov/medicaid/index.html"
+            ],
             "theme": [
                 "Vision & Eye Health"
-            ]
+            ],
+            "title": "Medicaid Claims (MAX) - Vision and Eye Health Surveillance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7vnz-2mjz",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "keyword": [
-                "2016",
-                "hepatitis",
-                "hepatitis (viral acute)",
-                "hepatitis (viral acute) type a",
-                "hepatitis (viral acute) type b",
-                "hepatitis (viral acute) type c",
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
-            "identifier": "https://data.cdc.gov/api/views/7vnz-2mjz",
             "description": "NNDSS - Table II. Hepatitis (viral, acute) - 2016. In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.  The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.  NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n * Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n \u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions.",
-            "title": "NNDSS - Table II. Hepatitis (viral, acute)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -114276,92 +114250,96 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7vnz-2mjz",
+            "issued": "2017-01-05",
+            "keyword": [
+                "2016",
+                "hepatitis",
+                "hepatitis (viral acute)",
+                "hepatitis (viral acute) type a",
+                "hepatitis (viral acute) type b",
+                "hepatitis (viral acute) type c",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7vnz-2mjz",
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
+            "title": "NNDSS - Table II. Hepatitis (viral, acute)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/pywq-su29",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-24",
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
-            "identifier": "26a6154a-3e36-58bd-aef3-6bcc465687c0",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_files_allDownloads",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_allDownloads.csv",
-                    "description": "{\"dataset\": \"files_allDownloads\", \"stage\": \"devAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"files_allDownloads\", \"stage\": \"devAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_allDownloads.csv",
+                    "mediaType": "text/csv",
                     "title": "files_allDownloads csv file"
                 }
             ],
+            "identifier": "26a6154a-3e36-58bd-aef3-6bcc465687c0",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/pywq-su29",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2023-08-24",
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
+            "title": "devAuto_files_allDownloads"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/68sm-zh95",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/68sm-zh95",
             "description": "NNDSS - Table 1H. Cholera to Coccidioidomycosis - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1H. Cholera to Coccidioidomycosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -114384,55 +114362,53 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/68sm-zh95",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "cholera",
+                "coccidioidomycosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/68sm-zh95",
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
+            "title": "NNDSS - Table 1H. Cholera to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-geography-and-service",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2013-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-04",
-            "references": [
-                "https://data.cms.gov/resources/medicare-inpatient-hospitals-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
-                "hospitals & facilities",
-                "inpatient",
-                "medicare",
-                "national",
-                "original medicare",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/2941ab09-8cee-49d8-9703-f3c5b854e388/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-inpatient-hospitals-by-geography-and-service-data-dictionary-0",
             "description": "The Medicare Inpatient Hospitals by Geography and Service dataset provides information on hospital discharges for Original Medicare Part A beneficiaries by IPPS\u00a0hospitals. This dataset\u00a0contains information on the number of discharges, payments, and submitted charges organized by geography and Medicare Severity Diagnosis Related Group (DRG).",
-            "title": "Medicare Inpatient Hospitals - by Geography and Service",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2941ab09-8cee-49d8-9703-f3c5b854e388/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2941ab09-8cee-49d8-9703-f3c5b854e388/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Inpatient Hospitals - by Geography and Service : 2022-12-01"
                 },
                 {
@@ -114556,91 +114532,98 @@
                     "title": "Medicare Inpatient Hospitals - by Geography and Service : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-inpatient-hospitals-by-geography-and-service-data-dictionary-0",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/2941ab09-8cee-49d8-9703-f3c5b854e388/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "hospitals & facilities",
+                "inpatient",
+                "medicare",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-geography-and-service",
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
+                "https://data.cms.gov/resources/medicare-inpatient-hospitals-methodology"
+            ],
+            "temporal": "2013-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Inpatient Hospitals - by Geography and Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/q2v4-vdvf",
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
-            "identifier": "d605e8ea-553c-50b2-83ac-238f1734c257",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt version v2.10.14 (coreset-dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.14/20241029/version.csv",
-                    "description": "CoreSEt version v2.10.14 (coreset-dev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt version v2.10.14 (coreset-dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.14/20241029/version.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt version v2.10.14 (coreset-dev)"
                 }
             ],
+            "identifier": "d605e8ea-553c-50b2-83ac-238f1734c257",
+            "issued": "2024-11-06",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/q2v4-vdvf",
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
+            "title": "CoreSEt version v2.10.14 (coreset-dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/tobacco/stateandcommunity/best_practices/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-01-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-30",
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
-            "identifier": "https://data.cdc.gov/api/views/f8gx-sdye",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "CDC Best Practices for Comprehensive Tobacco Control Programs - 2007 Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -114648,35 +114631,39 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/f8gx-sdye",
+            "issued": "2015-01-28",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "http://www.cdc.gov/tobacco/stateandcommunity/best_practices/",
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
                 "Funding"
-            ]
+            ],
+            "title": "CDC Best Practices for Comprehensive Tobacco Control Programs - 2007 Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/gt5d-asw4",
-            "issued": "2023-09-01",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-01",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Test",
                 "hasEmail": "mailto:Test"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/gt5d-asw4",
             "description": "",
-            "title": "SocrataDataRefresh_Test",
-            "programCode": [
-                "009:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -114699,18 +114686,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/gt5d-asw4",
+            "issued": "2023-09-01",
+            "landingPage": "https://data.cdc.gov/d/gt5d-asw4",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-09-01",
+            "programCode": [
+                "009:036"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "SocrataDataRefresh_Test"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-sexually-transmitted-disease-std-morbidity",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/std.html",
+            "description": "<p>The Sexually Transmitted Disease (STD) Morbidity online databases on CDC WONDER contain case reports reported from the 50 United States and D.C., Puerto Rico, Virgin Islands and Guam.   The online databases report  the number of cases and disease incidence rates by year, state, disease, age, gender of patient, type of STD, and area of report.  Data are produced by the U.S. Department of Health and Human Services, Public Health Service, Centers for Disease Control and Prevention (CDC), National Center for HIV/AIDS, viral Hepatitis, STD and TB Prevention (NCHHSTP).</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/std.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "134d23cb-d5d0-45d0-8fa4-4313efb14183",
             "issued": "2012-05-30",
-            "temporal": "1984-01-01T00:00:00-05:00/2008-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "age",
                 "case",
@@ -114727,63 +114740,35 @@
                 "virgin islands",
                 "year"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-sexually-transmitted-disease-std-morbidity",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "134d23cb-d5d0-45d0-8fa4-4313efb14183",
-            "description": "<p>The Sexually Transmitted Disease (STD) Morbidity online databases on CDC WONDER contain case reports reported from the 50 United States and D.C., Puerto Rico, Virgin Islands and Guam.   The online databases report  the number of cases and disease incidence rates by year, state, disease, age, gender of patient, type of STD, and area of report.  Data are produced by the U.S. Department of Health and Human Services, Public Health Service, Centers for Disease Control and Prevention (CDC), National Center for HIV/AIDS, viral Hepatitis, STD and TB Prevention (NCHHSTP).</p>",
-            "title": "CDC WONDER: Sexually Transmitted Disease (STD) Morbidity",
-            "programCode": [
-                "009:027"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://wonder.cdc.gov/std.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://wonder.cdc.gov/std.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1984-01-01T00:00:00-05:00/2008-12-31T00:00:00-05:00",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Sexually Transmitted Disease (STD) Morbidity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/q433-kijn",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-04-07",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-05",
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
-            "identifier": "c5bd69ae-7c98-4787-beb6-cb347ebf329f",
             "description": "test",
-            "title": "NADAC",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -114791,19 +114776,38 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "c5bd69ae-7c98-4787-beb6-cb347ebf329f",
+            "issued": "2022-04-07",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/q433-kijn",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2022-04-05",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "NADAC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.hcup-us.ahrq.gov/db/nation/neds/nedsdbdocumentation.jsp",
             "bureauCode": [
                 "009:33"
             ],
-            "rights": "N/A",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HCUP Technical Support",
+                "hasEmail": "mailto:hcup@ahrq.gov"
+            },
+            "describedBy": "https://www.hcup-us.ahrq.gov/db/nation/neds/nedsdbdocumentation.jsp",
+            "description": "The Healthcare Cost and Utilization Project (HCUP) Nationwide Emergency Department Sample (NEDS) is the largest all-payer emergency department (ED) database in the United States. yielding national estimates of hospital-owned ED visits. Unweighted, it contains data from over 30 million ED visits each year. Weighted, it estimates roughly 145 million ED visits nationally.  Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality, HCUP data inform decision making at the national, State, and community levels.\n\nSampled from the HCUP State Inpatient Databases (SID) and State Emergency Department Databases (SEDD), the HCUP NEDS can be used to create national and regional estimates of ED care. The SID contain information on patients initially seen in the ED and subsequently admitted to the same hospital. The SEDD capture information on ED visits that do not result in an admission (i.e., treat-and-release visits and transfers to another hospital). Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality, HCUP data inform decision making at the national, State, and community levels. \n\nThe NEDS contain information about geographic characteristics, hospital characteristics, patient characteristics, and the nature of visits (e.g., common reasons for ED visits, including injuries). The NEDS contains clinical and resource use information included in a typical discharge abstract, with safeguards to protect the privacy of individual patients, physicians, and hospitals (as required by data sources). It includes ED charge information for over 85% of patients, regardless of expected payer, including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge\u2019. The NEDS excludes data elements that could directly or indirectly identify individuals, hospitals, or states.Restricted access data files are available with a data use agreement and brief online security training.",
+            "identifier": "26887d97-e5da-4b40-893d-0cb9bebf1948",
             "issued": "2021-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "claims",
                 "diagnoses",
@@ -114820,54 +114824,33 @@
                 "sexual assault",
                 "utilization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HCUP Technical Support",
-                "hasEmail": "mailto:hcup@ahrq.gov"
-            },
+            "landingPage": "https://www.hcup-us.ahrq.gov/db/nation/neds/nedsdbdocumentation.jsp",
+            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.asp",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:037"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
             },
-            "identifier": "26887d97-e5da-4b40-893d-0cb9bebf1948",
-            "description": "The Healthcare Cost and Utilization Project (HCUP) Nationwide Emergency Department Sample (NEDS) is the largest all-payer emergency department (ED) database in the United States. yielding national estimates of hospital-owned ED visits. Unweighted, it contains data from over 30 million ED visits each year. Weighted, it estimates roughly 145 million ED visits nationally.  Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality, HCUP data inform decision making at the national, State, and community levels.\n\nSampled from the HCUP State Inpatient Databases (SID) and State Emergency Department Databases (SEDD), the HCUP NEDS can be used to create national and regional estimates of ED care. The SID contain information on patients initially seen in the ED and subsequently admitted to the same hospital. The SEDD capture information on ED visits that do not result in an admission (i.e., treat-and-release visits and transfers to another hospital). Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality, HCUP data inform decision making at the national, State, and community levels. \n\nThe NEDS contain information about geographic characteristics, hospital characteristics, patient characteristics, and the nature of visits (e.g., common reasons for ED visits, including injuries). The NEDS contains clinical and resource use information included in a typical discharge abstract, with safeguards to protect the privacy of individual patients, physicians, and hospitals (as required by data sources). It includes ED charge information for over 85% of patients, regardless of expected payer, including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge\u2019. The NEDS excludes data elements that could directly or indirectly identify individuals, hospitals, or states.Restricted access data files are available with a data use agreement and brief online security training.",
-            "title": "HCUP Nationwide Emergency Department Database (NEDS) Restricted Access File",
-            "programCode": [
-                "009:037"
-            ],
-            "describedBy": "https://www.hcup-us.ahrq.gov/db/nation/neds/nedsdbdocumentation.jsp",
-            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.asp"
+            "rights": "N/A",
+            "title": "HCUP Nationwide Emergency Department Database (NEDS) Restricted Access File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/occ-administrative-data",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-08-01",
-            "temporal": "2009-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "administrative",
-                "children families child care",
-                "other"
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
-            "identifier": "803d680c-e91c-4347-b91b-c24051b8a7c5",
+            "dataQuality": true,
+            "describedBy": "http://www.acf.hhs.gov/programs/occ/resource/current-technical-bulletins",
             "description": "<p>Characteristics of families and children served by Child Care and Development Fund (CCDF)</p>",
-            "title": "OCC Administrative Data",
-            "programCode": [
-                "009:015"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -114876,45 +114859,38 @@
                     "title": "XLS "
                 }
             ],
-            "describedBy": "http://www.acf.hhs.gov/programs/occ/resource/current-technical-bulletins",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "803d680c-e91c-4347-b91b-c24051b8a7c5",
+            "issued": "2012-08-01",
+            "keyword": [
+                "administrative",
+                "children families child care",
+                "other"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/occ-administrative-data",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:015"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families, Department of Health & Human Services"
+            },
+            "temporal": "2009-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
+            "title": "OCC Administrative Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mpdg-hf57",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
-            "keyword": [
-                "2015",
-                "giardiasis",
-                "gonorrhea",
-                "haemophilus influenzae",
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
-            "identifier": "https://data.cdc.gov/api/views/mpdg-hf57",
             "description": "NNDSS - Table II. Giardiasis to Haemophilus influenza - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Data for H. influenzae (age <5 years for serotype b, nonserotype b, and unknown serotype) are available in Table I.",
-            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -114937,42 +114913,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mpdg-hf57",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
+                "giardiasis",
+                "gonorrhea",
+                "haemophilus influenzae",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mpdg-hf57",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-01-07",
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
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/adults-60-coverage-intent.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
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
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/gzbv-dn9g",
             "description": "Weekly Intent for Vaccination and Cumulative Percentage of Adults 60 Years and Older Vaccinated with RSV Vaccine.\n\n \u2022 RSV vaccination coverage among adults ages 60 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly RSV vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n \u2022 The CDC recommended the RSV vaccine for adults ages 60 years and older in July 2023. (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)",
-            "title": "Weekly Intent for Vaccination and Cumulative Percentage of Adults 60 Years and Older Vaccinated with RSV Vaccine",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -114995,58 +114976,56 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/gzbv-dn9g",
+            "issued": "2023-11-07",
+            "keyword": [
+                "nis-acm",
+                "older adults",
+                "rsv",
+                "vaccination"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/adults-60-coverage-intent.html",
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
+            "spatial": "United States- National, Region, State",
+            "temporal": "2023-2024",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Intent for Vaccination and Cumulative Percentage of Adults 60 Years and Older Vaccinated with RSV Vaccine"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/rural-health-clinic-enrollments",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-12-08",
-            "temporal": "2023-10-01/2025-03-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-10/RHC_Data_Guidance.pdf"
-            ],
-            "keyword": [
-                "hospitals & facilities",
-                "medicare",
-                "outpatient facilities",
-                "provider enrollment",
-                "rural health clinics"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/3b7e7659-067e-41ea-8e36-f9ee2036e1f6/data-viewer",
-            "description": "The Rural Health Clinic (RHC) Enrollments dataset provides enrollment information on all RHCs currently enrolled in Medicare. This data includes information on the RHC's legal business name, doing business as name, organization type and address.",
-            "title": "Rural Health Clinic Enrollments",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-09/RHC_Enrollments_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Rural Health Clinic (RHC) Enrollments dataset provides enrollment information on all RHCs currently enrolled in Medicare. This data includes information on the RHC's legal business name, doing business as name, organization type and address.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3b7e7659-067e-41ea-8e36-f9ee2036e1f6/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3b7e7659-067e-41ea-8e36-f9ee2036e1f6/data",
+                    "mediaType": "text/html",
                     "title": "Rural Health Clinic Enrollments : 2025-01-01"
                 },
                 {
@@ -115122,52 +115101,49 @@
                     "title": "Rural Health Clinic Enrollments : 2023-10-29"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2023-09/RHC_Enrollments_Data_Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/3b7e7659-067e-41ea-8e36-f9ee2036e1f6/data-viewer",
+            "issued": "2023-12-08",
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "outpatient facilities",
+                "provider enrollment",
+                "rural health clinics"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/rural-health-clinic-enrollments",
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
+                "https://data.cms.gov/sites/default/files/2024-10/RHC_Data_Guidance.pdf"
+            ],
+            "temporal": "2023-10-01/2025-03-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Rural Health Clinic Enrollments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9gny-cbhc",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "arboviral diseases",
-                "jamestown canyon virus disease",
-                "la crosse virus disease",
-                "nedss",
-                "netss",
-                "nndss",
-                "powassan virus disease",
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
-            "identifier": "https://data.cdc.gov/api/views/9gny-cbhc",
             "description": "NNDSS - Table 1B. Arboviral diseases, neuroinvasive and non-neuroinvasive, Jamestown Canyon virus disease to Powassan virus disease - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1B. Arboviral diseases, neuroinvasive and non-neuroinvasive, Jamestown Canyon virus disease to Powassan virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -115190,43 +115166,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9gny-cbhc",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "arboviral diseases",
+                "jamestown canyon virus disease",
+                "la crosse virus disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "powassan virus disease",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9gny-cbhc",
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
+            "title": "NNDSS - Table 1B. Arboviral diseases, neuroinvasive and non-neuroinvasive, Jamestown Canyon virus disease to Powassan virus disease"
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
@@ -115234,39 +115213,44 @@
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
+            "title": "Going Smokefree Matters - Casinos Infographic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/progress-tables.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-22",
-            "@type": "dcat:Dataset",
-            "temporal": "1988-01-01/2019-12-31",
-            "modified": "2023-08-23",
-            "keyword": [
-                "healthy people 2020"
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
-            "identifier": "https://data.cdc.gov/api/views/x749-vh2i",
             "description": "[1] Status is determined using the baseline, final, and target value. The statuses used in Healthy People 2020 were: \n\n1 - Target met or exceeded\u2014One of the following applies: (i) At baseline, the target was not met or exceeded, and the most recent value was equal to or exceeded the target. (The percentage of targeted change achieved was equal to or greater than 100%.); (ii) The baseline and most recent values were equal to or exceeded the target. (The percentage of targeted change achieved was not assessed.) \n\n2 - Improved\u2014One of the following applies: (i) Movement was toward the target, standard errors were available, and the percentage of targeted change achieved was statistically significant; (ii) Movement was toward the target, standard errors were not available, and the objective had achieved 10% or more of the targeted change.\n\n3 - Little or no detectable change\u2014One of the following applies: (i) Movement was toward the target, standard errors were available, and the percentage of targeted change achieved was not statistically significant; (ii) Movement was toward the target, standard errors were not available, and the objective had achieved less than 10% of the targeted change; (iii) Movement was away from the baseline and target, standard errors were available, and the percent change relative to the baseline was not statistically significant; (iv) Movement was away from the baseline and target, standard errors were not available, and the objective had moved less than 10% relative to the baseline; (v) No change was observed between the baseline and the final data point.\n\n4 - Got worse\u2014One of the following applies: (i) Movement was away from the baseline and target, standard errors were available, and the percent change relative to the baseline was statistically significant; (ii) Movement was away from the baseline and target, standard errors were not available, and the objective had moved 10% or more relative to the baseline.\n\n5 - Baseline only\u2014The objective only had one data point, so progress toward target attainment could not be assessed. Note that if additional data points did not meet the criteria for statistical reliability, data quality, or confidentiality, the objective was categorized as baseline only. \n\n6 - Informational\u2014A target was not set for this objective, so progress toward target attainment could not be assessed.\n\n\n[2] The final value is generally based on data available on the Healthy People 2020 website as of January 2020. For objectives that are continuing into Healthy People 2030, more recent data are available on the Healthy People 2030 website: https://health.gov/healthypeople. \n\n\n[3] For objectives that moved toward their targets, movement toward the target was measured as the percentage of targeted change achieved (unless the target was already met or exceeded at baseline): \n\nPercentage of targeted change achieved = (Final value - Baseline value) / (HP2020 target - Baseline value) * 100\n\n\n[4] For objectives that were not improving, did not meet or exceed their targets, and did not move towards their targets, movement away from the baseline was measured as the magnitude of the percent change from baseline: \n\nMagnitude of percent change from baseline = |Final value - Baseline value| / Baseline value * 100\n\n\n[5] Statistical significance was tested when the objective had a target, at least two data points (of unequal value), and available standard errors of the data. A normal distribution was assumed. All available digits were used to test statistical significance. Statistical significance of the percentage of targeted change achieved or the magnitude of the percentage change from baseline was assessed at the 0.05 level using a normal one-sided test. \n\n\n[6] For more information on the Healthy People 2020 methodology for measuring progress toward target attainment and the elimination of health disparities, see: Healthy People Statistical Notes, no 27; available from: https://www.cdc.gov/nchs/data/sta",
-            "title": "Healthy People 2020 Final Progress Table",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -115289,50 +115273,43 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/x749-vh2i",
+            "issued": "2022-01-22",
+            "keyword": [
+                "healthy people 2020"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/progress-tables.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-08-23",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
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
-            "landingPage": "https://data.cdc.gov/d/fuzh-wm4c",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
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
-            "identifier": "https://data.cdc.gov/api/views/fuzh-wm4c",
             "description": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection) - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 In previous years, cases were reported as Salmonellosis. Beginning in January 2019, cases began to be reported as Salmonella Paratyphi infection.\r\n\u00b6 In previous years, cases were reported as typhoid fever. Beginning in January 2019, cases began to be reported as Salmonella Typhi infection.\r\n** In previous years, cases were reported as Salmonellosis (excluding paratyphoid fever and typhoid fever). Beginning in January 2019, cases began to be reported as Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection).",
-            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -115355,28 +115332,56 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fuzh-wm4c",
+            "issued": "2019-04-24",
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
+            "landingPage": "https://data.cdc.gov/d/fuzh-wm4c",
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
+            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nhis/index.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "The NHIS website features downloadable annual data and documentation, information about any modifications or updates to the data or documentation, and published reports (https://www.cdc.gov/nchs/nhis/index.htm). NHIS is protected by Federal confidentiality laws that state the data collected by NCHS may be used only for statistical reporting and analysis. Some NHIS survey measures have been suppressed or edited in the downloadable public use files to protect confidentiality. Analysts interested in working with data that were suppressed or edited may apply to access selected unmodified data through the NCHS Research Data Center at https://www.cdc.gov/rdc/. For information about variables that are available in the public use files, see the annual Codebook. For information about restricted variables available through the RDC, see the Codebook for Restricted-use variables. In addition, the appendix of the annual Survey Description Document (SDD) includes a list of questionnaire variables that were recoded, suppressed, or are not available.",
-            "issued": "2023-06-28",
-            "@type": "dcat:Dataset",
-            "temporal": "2019\u20132023",
-            "modified": "2024-08-06",
-            "references": [
-                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2019/srvydesc-508.pdf",
-                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2020/srvydesc-508.pdf",
-                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2021/srvydesc-508.pdf",
-                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2022/srvydesc-508.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:nhislist@cdc.gov"
+            },
+            "description": "2019\u2013present. The National Health Interview Survey (NHIS) is a nationally representative household health survey of the U.S. civilian noninstitutionalized population. The NHIS data are used to monitor trends in illness and disability, track progress toward achieving national health objectives, for epidemiologic and policy analysis of various health problems, determining barriers to accessing and using appropriate health care, and evaluating Federal health programs. NHIS is conducted continuously throughout the year by the National Center for Health Statistics (NCHS). Public-use data files on adults and children with corresponding imputed income data files, and survey paradata are released annually. The NHIS data website (https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm) features the most up-to-date public-use data files and documentation for downloading including questionnaire, codebooks, CSV and ASCII data files, programs and sample code, and in-depth survey description. Most of the NHIS data are included in the public use files. NHIS is protected by Federal confidentiality laws that state the data collected by NCHS may be used only for statistical reporting and analysis. Some NHIS variables have been suppressed or edited in the public use files to protect confidentiality. Analysts interested in using data that has been suppressed or edited may apply for access through the NCHS Research Data Center at https://www.cdc.gov/rdc/. In 2019, NHIS launched a redesigned content and structure that differs from its previous questionnaire designs. NHIS has been conducted continuously since 1957.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+                    "mediaType": "text/html",
+                    "title": "National Health Interview Survey"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8zhx-mf8r",
+            "issued": "2023-06-28",
             "keyword": [
                 "access-to-health-care",
                 "civic-participation",
@@ -115405,74 +115410,45 @@
                 "use-of-health-care",
                 "workplace"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:nhislist@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nhis/index.htm",
+            "language": [
+                "English"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-06",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/8zhx-mf8r",
-            "description": "2019\u2013present. The National Health Interview Survey (NHIS) is a nationally representative household health survey of the U.S. civilian noninstitutionalized population. The NHIS data are used to monitor trends in illness and disability, track progress toward achieving national health objectives, for epidemiologic and policy analysis of various health problems, determining barriers to accessing and using appropriate health care, and evaluating Federal health programs. NHIS is conducted continuously throughout the year by the National Center for Health Statistics (NCHS). Public-use data files on adults and children with corresponding imputed income data files, and survey paradata are released annually. The NHIS data website (https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm) features the most up-to-date public-use data files and documentation for downloading including questionnaire, codebooks, CSV and ASCII data files, programs and sample code, and in-depth survey description. Most of the NHIS data are included in the public use files. NHIS is protected by Federal confidentiality laws that state the data collected by NCHS may be used only for statistical reporting and analysis. Some NHIS variables have been suppressed or edited in the public use files to protect confidentiality. Analysts interested in using data that has been suppressed or edited may apply for access through the NCHS Research Data Center at https://www.cdc.gov/rdc/. In 2019, NHIS launched a redesigned content and structure that differs from its previous questionnaire designs. NHIS has been conducted continuously since 1957.",
-            "title": "National Health Interview Survey",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
-                    "mediaType": "text/html",
-                    "title": "National Health Interview Survey"
-                }
+            "references": [
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2019/srvydesc-508.pdf",
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2020/srvydesc-508.pdf",
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2021/srvydesc-508.pdf",
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2022/srvydesc-508.pdf"
             ],
+            "rights": "The NHIS website features downloadable annual data and documentation, information about any modifications or updates to the data or documentation, and published reports (https://www.cdc.gov/nchs/nhis/index.htm). NHIS is protected by Federal confidentiality laws that state the data collected by NCHS may be used only for statistical reporting and analysis. Some NHIS survey measures have been suppressed or edited in the downloadable public use files to protect confidentiality. Analysts interested in working with data that were suppressed or edited may apply to access selected unmodified data through the NCHS Research Data Center at https://www.cdc.gov/rdc/. For information about variables that are available in the public use files, see the annual Codebook. For information about restricted variables available through the RDC, see the Codebook for Restricted-use variables. In addition, the appendix of the annual Survey Description Document (SDD) includes a list of questionnaire variables that were recoded, suppressed, or are not available.",
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2019\u20132023",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "National Health Interview Survey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/w7ew-4aqz",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
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
-            "identifier": "https://data.cdc.gov/api/views/w7ew-4aqz",
             "description": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Includes data for dengue and dengue-like illness.",
-            "title": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -115495,42 +115471,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/w7ew-4aqz",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "dengue",
+                "dengue-like illness",
+                "dengue virus infections",
+                "nedss",
+                "netss",
+                "nndss",
+                "severe dengue",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/w7ew-4aqz",
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
+            "title": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/q7jh-763c",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-14",
-            "keyword": [
-                "py2024",
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
-            "identifier": "bcaea23a-7ece-4c8c-8e53-c1f10231eb95",
             "description": "The Dental SHOP Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2024 Dental SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -115538,42 +115519,38 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "bcaea23a-7ece-4c8c-8e53-c1f10231eb95",
+            "issued": "2024-08-06",
+            "keyword": [
+                "py2024",
+                "qhp landscape instructions",
+                "sadp",
+                "shop",
+                "shop market dental"
+            ],
+            "landingPage": "https://healthdata.gov/d/q7jh-763c",
+            "modified": "2024-08-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2024 Dental SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6dep-qtzm",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "anaplasma phagocytophilum infection",
-                "ehrlichia chaffeensis infection",
-                "ehrlichiosis and anaplasmosis",
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
-            "identifier": "https://data.cdc.gov/api/views/6dep-qtzm",
             "description": "NNDSS - Table 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -115596,39 +115573,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6dep-qtzm",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "anaplasma phagocytophilum infection",
+                "ehrlichia chaffeensis infection",
+                "ehrlichiosis and anaplasmosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6dep-qtzm",
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
+            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5p6r-d32s",
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
-            "identifier": "https://data.cdc.gov/api/views/5p6r-d32s",
             "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012, 2014.",
-            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 5 - Chicago",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -115651,47 +115634,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5p6r-d32s",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5p6r-d32s",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 5 - Chicago"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mtc3-kq6r",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-10-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-07-01/2021-12-14",
-            "modified": "2025-01-13",
-            "keyword": [
-                "coronavirus",
-                "covid",
-                "covid19",
-                "covid-19",
-                "laboratory",
-                "prevalence",
-                "sars-cov",
-                "seroprevalence",
-                "serosurveys"
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
-            "identifier": "https://data.cdc.gov/api/views/mtc3-kq6r",
             "description": "CDC is collaborating with the National Institutes of Health (NIH), the Food and Drug Administration (FDA), Vitalant Research Institute (VRI), Westat Inc., and numerous blood collection organizations across the United States to conduct a nationwide COVID-19 seroprevalence survey of blood donors. This is the largest nationwide COVID-19 seroprevalence survey to date. De-identified blood samples are tested for antibodies to SARS-CoV-2 to better understand the percentage of people in the United States who have antibodies against SARS-CoV-2 (the virus that causes COVID-19) and to track how this percentage changes over time. Both SARS-CoV-2 infection and COVID-19 vaccines currently used in the United States result in production of anti-spike (anti-S) antibodies but only infection results in production of anti-nucleocapsid (anti-N) antibodies. Infection-induced seroprevalence estimates the proportion of the population with evidence of previous SARS-CoV-2 infection and refers to the prevalence of the population with both anti-S and anti-N antibodies.\n\nThis link connects to a webpage that displays the data from the Nationwide Blood Donor Seroprevalence Survey. It offers an interactive visualization available at https://covid.cdc.gov/covid-data-tracker/#nationwide-blood-donor-seroprevalence\n\nAdditional information is available at: https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/blood-bank-serosurvey.html",
-            "title": "2020-2021 Nationwide Blood Donor Seroprevalence Survey Infection-Induced Seroprevalence Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -115714,44 +115690,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/mtc3-kq6r",
+            "issued": "2021-10-01",
+            "keyword": [
+                "coronavirus",
+                "covid",
+                "covid19",
+                "covid-19",
+                "laboratory",
+                "prevalence",
+                "sars-cov",
+                "seroprevalence",
+                "serosurveys"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mtc3-kq6r",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
+            "temporal": "2020-07-01/2021-12-14",
             "theme": [
                 "Laboratory Surveillance"
-            ]
+            ],
+            "title": "2020-2021 Nationwide Blood Donor Seroprevalence Survey Infection-Induced Seroprevalence Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/q9ee-jubp",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-14",
-            "keyword": [
-                "py2024",
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
-            "identifier": "0e706798-a495-4121-b1b6-feb319e39726",
             "description": "The Dental SHOP Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2024 Dental SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -115759,42 +115740,38 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "0e706798-a495-4121-b1b6-feb319e39726",
+            "issued": "2024-08-06",
+            "keyword": [
+                "py2024",
+                "qhp landscape",
+                "sadp",
+                "shop",
+                "shop market dental"
+            ],
+            "landingPage": "https://healthdata.gov/d/q9ee-jubp",
+            "modified": "2024-08-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2024 Dental SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/vq7a-fvin",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "confirmed",
-                "nedss",
-                "netss",
-                "nndss",
-                "probable",
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
-            "identifier": "https://data.cdc.gov/api/views/vq7a-fvin",
             "description": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data",
-            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -115817,47 +115794,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vq7a-fvin",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "confirmed",
+                "nedss",
+                "netss",
+                "nndss",
+                "probable",
+                "vibriosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/vq7a-fvin",
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
+            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/gn5f-ec35",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-06-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2015",
-            "modified": "2023-04-20",
-            "keyword": [
-                "chronic conditions",
-                "food security",
-                "health behaviors",
-                "health insurance",
-                "o\tanxiety",
-                "physical activity",
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
-            "identifier": "https://data.cdc.gov/api/views/gn5f-ec35",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional \nsurveys from probability-sampled commercial survey panels which began in 2015. \nRANDS 1 was administered by Gallup using the Gallup Panel in the fall of 2015 \nand contains existing questions from the National Health Interview Survey (NHIS).",
-            "title": "NCHS Research and Development Survey (RANDS) Round 1 Restricted File",
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS1_technical_documentation.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional \nsurveys from probability-sampled commercial survey panels which began in 2015. \nRANDS 1 was administered by Gallup using the Gallup Panel in the fall of 2015 \nand contains existing questions from the National Health Interview Survey (NHIS).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -115865,53 +115842,47 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/gn5f-ec35",
+            "issued": "2022-06-15",
+            "keyword": [
+                "chronic conditions",
+                "food security",
+                "health behaviors",
+                "health insurance",
+                "o\tanxiety",
+                "physical activity",
+                "research-data-center"
+            ],
+            "landingPage": "https://data.cdc.gov/d/gn5f-ec35",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-04-20",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS1_technical_documentation.pdf",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "2015",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 1 Restricted File"
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
-                "city",
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
-            "identifier": "https://data.cdc.gov/api/views/cj8b-94cj",
             "description": "This dataset contains model-based place (incorporated and census designated places) level estimates for the PLACES 2021 release in GIS-friendly format. PLACES is the expansion of the original 500 Cities Project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the 2019 Census TIGER/Line place boundary file in a GIS system to produce maps for 29 measures at the place level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software. https://cdcarcgis.maps.arcgis.com/home/item.html?id=024cf3f6f59e49fe8c70e0e5410fe3cf",
-            "title": "PLACES: Place Data (GIS Friendly Format), 2021 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -115934,51 +115905,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "theme": [
-                "500 Cities & Places"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-08-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-23",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/cj8b-94cj",
+            "issued": "2022-10-11",
             "keyword": [
                 "behaviors",
-                "brfss",
-                "county",
-                "disability",
+                "city",
+                "gis",
                 "health",
                 "outcomes",
+                "place",
                 "places",
                 "prevalence",
                 "prevention",
                 "risk",
                 "status"
             ],
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
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
+            "theme": [
+                "500 Cities & Places"
+            ],
+            "title": "PLACES: Place Data (GIS Friendly Format), 2021 release"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PLACES Public Inquiries",
                 "hasEmail": "mailto:places@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/swc5-untb",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
             "description": "This dataset contains model-based county estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. This dataset includes estimates for 40 measures: 12 for health outcomes, 7 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, 3 for health status, and 7 for health-related social needs. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2022 or 2021 data, Census Bureau 2022 county population estimate data, and American Community Survey 2018\u20132022 estimates. The 2024 release uses 2022 BRFSS data for 36 measures and 2021 BRFSS data for 4 measures (high blood pressure, high cholesterol, cholesterol screening, and taking medicine for high blood pressure control among those with high blood pressure) that the survey collects data on every other year. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, County Data 2024 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -116001,47 +115973,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
+            "identifier": "https://data.cdc.gov/api/views/swc5-untb",
+            "issued": "2024-08-23",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "county",
+                "disability",
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
+            "modified": "2024-12-23",
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
+            "title": "PLACES: Local Data for Better Health, County Data 2024 release"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -116064,46 +116040,48 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/g76d-z8vy",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-06-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2020",
-            "modified": "2023-04-24",
-            "keyword": [
-                "anxiety",
-                "covid-19",
-                "depression",
-                "missed healthcare",
-                "research-data-center",
-                "telemedicine"
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
-            "identifier": "https://data.cdc.gov/api/views/g76d-z8vy",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 2 is the second round of a three-round survey. The probability sample of RANDS during COVID-19 Round 2 was recruited using NORC at the University of Chicago (NORC)'s AmeriSpeak Panel, and the survey was administered by NORC from August 3, 2020 to August 20, 2020.  The RANDS during COVID-19 Round 2 Probability Sample has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates",
-            "title": "NCHS Research and Development Survey (RANDS) Round 2 during COVID-19 probability sampled Restricted File",
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_2_technical_documentation.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 2 is the second round of a three-round survey. The probability sample of RANDS during COVID-19 Round 2 was recruited using NORC at the University of Chicago (NORC)'s AmeriSpeak Panel, and the survey was administered by NORC from August 3, 2020 to August 20, 2020.  The RANDS during COVID-19 Round 2 Probability Sample has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -116111,40 +116089,47 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_2_technical_documentation.pdf",
+            "identifier": "https://data.cdc.gov/api/views/g76d-z8vy",
+            "issued": "2022-06-15",
+            "keyword": [
+                "anxiety",
+                "covid-19",
+                "depression",
+                "missed healthcare",
+                "research-data-center",
+                "telemedicine"
+            ],
+            "landingPage": "https://data.cdc.gov/d/g76d-z8vy",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-04-24",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "50 states and District of Columbia",
+            "temporal": "2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 2 during COVID-19 probability sampled Restricted File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qbqi-u7ub",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-08-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-22",
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
-            "identifier": "52b6029b-6833-45d0-b3bf-aa5b8bf7fd92",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-14-to-2023-08-20",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -116153,45 +116138,38 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-14-to-2023-08-20"
                 }
             ],
+            "identifier": "52b6029b-6833-45d0-b3bf-aa5b8bf7fd92",
+            "issued": "2023-08-23",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/qbqi-u7ub",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-08-22",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-14-to-2023-08-20"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-medicare-advantage-other-health-plan-enrollment",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2013-01-01/2021-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-06",
-            "references": [
-                "https://data.cms.gov/resources/medicare-and-medicaid-reports-methodology"
-            ],
-            "keyword": [
-                "beneficiary enrollment",
-                "health equity",
-                "medicare",
-                "medicare advantage",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/24fe2a9a-4144-46b2-bf1a-07aa86fb65ae/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
             "description": "The CMS Program Statistics -\u00a0Medicare Advantage & Other Health Plan Enrollment tables provide data on characteristics of the population covered by Medicare Advantage & other health plans.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR ENROLL AB 15. \u00a0Medicare Advantage and Other Health Plan Enrollment: \u00a0Part A and/or Part B Total, Aged, and Disabled Enrollees, Yearly Trend\n\tMDCR ENROLL AB 16. \u00a0Medicare Advantage and Other Health Plan Enrollment: Part A and/or Part B Enrollees, by Age Group, Yearly Trend\n\tMDCR ENROLL AB 17. \u00a0Medicare Advantage and Other Health Plan Enrollment: \u00a0Part A and/or Part B Enrollees, by Demographic Characteristics\n\tMDCR ENROLL AB 18. \u00a0Medicare Advantage and Other Health Plan Enrollment: \u00a0Part A and/or Part B Enrollees, by Type of Entitlement and Demographic Characteristics\n\tMDCR ENROLL AB 19. \u00a0Medicare Advantage and Other Health Plan Enrollment: \u00a0Part A and/or Part B Total, Aged, and Disabled Enrollees, by Area of Residence\n\tMDCR ENROLL AB 20. \u00a0Medicare Advantage and Other Health Plan Enrollment: \u00a0Part A and/or Part B Enrollees, by Type of Entitlement and Area of Residence",
-            "title": "CMS Program Statistics - Medicare Advantage & Other Health Plan Enrollment",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -116248,59 +116226,60 @@
                     "title": "CMS Program Statistics - Medicare Advantage & Other Health Plan Enrollment : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/24fe2a9a-4144-46b2-bf1a-07aa86fb65ae/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "beneficiary enrollment",
+                "health equity",
+                "medicare",
+                "medicare advantage",
+                "national",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-medicare-advantage-other-health-plan-enrollment",
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
+                "https://data.cms.gov/resources/medicare-and-medicaid-reports-methodology"
+            ],
+            "temporal": "2013-01-01/2021-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS Program Statistics - Medicare Advantage & Other Health Plan Enrollment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-enrollments",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-12-21",
-            "temporal": "2022-11-01/2025-01-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-10/Hospital_Data_Guidance.pdf"
-            ],
-            "keyword": [
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/f6f6505c-e8b0-4d57-b258-e2b94133aaf2/data-viewer",
-            "description": "The Hospital Enrollments dataset provides enrollment information of all Hospitals currently enrolled in Medicare. This data includes information on the Hospital's sub-group type, legal business name, doing business as name, organization type and address.\u00a0",
-            "title": "Hospital Enrollments",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-07/Hospital_Enrollments_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Hospital Enrollments dataset provides enrollment information of all Hospitals currently enrolled in Medicare. This data includes information on the Hospital's sub-group type, legal business name, doing business as name, organization type and address.\u00a0",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f6f6505c-e8b0-4d57-b258-e2b94133aaf2/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f6f6505c-e8b0-4d57-b258-e2b94133aaf2/data",
+                    "mediaType": "text/html",
                     "title": "Hospital Enrollments : 2025-01-01"
                 },
                 {
@@ -116616,55 +116595,50 @@
                     "title": "Hospital Enrollments : 2022-11-21"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2023-07/Hospital_Enrollments_Data_Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/f6f6505c-e8b0-4d57-b258-e2b94133aaf2/data-viewer",
+            "issued": "2022-12-21",
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-enrollments",
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
+                "https://data.cms.gov/sites/default/files/2024-10/Hospital_Data_Guidance.pdf"
+            ],
+            "temporal": "2022-11-01/2025-01-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Hospital Enrollments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-10-02",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
-            "keyword": [
-                "age",
-                "age group",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "mortality",
-                "nchs",
-                "nvss",
-                "place of death",
-                "provisional",
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
-            "identifier": "https://data.cdc.gov/api/views/g7hk-rc8d",
             "description": "Provisional death counts of COVID-19 deaths by place of death, week, and age.\n\nData source: National Center for Health Statistics National Vital Statistics System. Provisional data for 2020-2021.",
-            "title": "AH Provisional COVID-19 Deaths by Week, Place of Death, and Age",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -116687,42 +116661,50 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/g7hk-rc8d",
+            "issued": "2020-10-02",
+            "keyword": [
+                "age",
+                "age group",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "place of death",
+                "provisional",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
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
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by Week, Place of Death, and Age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/respiratory-viruses/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-11",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-04-17",
-            "keyword": [
-                "pregnancy",
-                "rsv",
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
-            "identifier": "https://data.cdc.gov/api/views/g4jn-64pd",
             "description": "Weekly RSV Vaccination Coverage, Pregnant Persons 18-49 Years Old\n\n\u2022 RSV vaccination coverage among pregnant persons is assessed through the Vaccine Safety Datalink*\n\n\u2022 Data on RSV vaccinations among pregnant persons was available starting September 22, 2023, and includes doses received starting September 24, 2023.",
-            "title": "Weekly Respiratory Syncytial Virus (RSV) Vaccination Coverage among Pregnant Persons by Race and Ethnicity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -116745,45 +116727,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/g4jn-64pd",
+            "issued": "2023-12-11",
+            "keyword": [
+                "pregnancy",
+                "rsv",
+                "vsd"
+            ],
+            "landingPage": "https://www.cdc.gov/respiratory-viruses/index.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2024-04-17",
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
+            "title": "Weekly Respiratory Syncytial Virus (RSV) Vaccination Coverage among Pregnant Persons by Race and Ethnicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qeuw-ymq9",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-05",
-            "keyword": [
-                "chip",
-                "medicaid",
-                "neonatal abstinence syndrome"
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
-            "identifier": "9c9ad0d1-c59b-4a25-9314-8e7e44e7f281",
             "description": "This table presents the number of beneficiaries with NAS and the rate of neonatal abstinence syndrome per 1,000 newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2021.\r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues, making the data unusable for identifying this population. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nData from Maryland, Tennessee, and Utah are omitted due to data quality concerns. Maryland was excluded in 2017 due to unusable diagnosis codes in the IP file and the OT file. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2020. In addition, states with a high data quality concern on one or more measures are noted in the table in the \"Data Quality\" column. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Number and rate of NAS per 1,000 births in newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2021",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -116792,41 +116775,40 @@
                     "title": "Number and rate of NAS per 1,000 births in newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2021"
                 }
             ],
+            "identifier": "9c9ad0d1-c59b-4a25-9314-8e7e44e7f281",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "medicaid",
+                "neonatal abstinence syndrome"
+            ],
+            "landingPage": "https://healthdata.gov/d/qeuw-ymq9",
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
                 "Uncategorized"
-            ]
+            ],
+            "title": "Number and rate of NAS per 1,000 births in newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/wngq-sdai",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-09-07",
-            "@type": "dcat:Dataset",
-            "modified": "2017-09-07",
-            "keyword": [
-                "electronic health information",
-                "law",
-                "public health law program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rachel Hulkower",
                 "hasEmail": "mailto:hzo2@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/wngq-sdai",
             "description": "Authors: Cason Schmit, JD, Gregory Sunshine, JD, Dawn Pepin, JD, MPH, Tara Ramanathan, JD, MPH, Akshara Menon, JD, MPH, Matthew Penn, JD, MLIS\r\nThis legal data set consists of state statutes and regulations in effect as of January 1, 2014, related to electronic health information (EHI). Jurisdictions were limited to US states, territories, and the District of Columbia that had statutes and regulations in the Westlaw legal database that expressly referenced EHI. This data set includes 2,364 EHI-related laws representing 49 EHI uses in 54 jurisdictions. For information about research methods, please reference the Electronic Health Information Legal Epidemiology Protocol 2014.",
-            "title": "Electronic Health Information Legal Epidemiology Data Set 2014",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -116849,43 +116831,37 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/wngq-sdai",
+            "issued": "2017-09-07",
+            "keyword": [
+                "electronic health information",
+                "law",
+                "public health law program"
+            ],
+            "landingPage": "https://data.cdc.gov/d/wngq-sdai",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2017-09-07",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "Electronic Health Information Legal Epidemiology Data Set 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/qpq4-k3td",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "ehrlichia ewingii infection",
-                "ehrlichiosis and anaplasmosis",
-                "giardiasis",
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
-            "identifier": "https://data.cdc.gov/api/views/qpq4-k3td",
             "description": "NNDSS - Table 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -116908,23 +116884,57 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qpq4-k3td",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "ehrlichia ewingii infection",
+                "ehrlichiosis and anaplasmosis",
+                "giardiasis",
+                "nedss",
+                "netss",
+                "nndss",
+                "undetermined",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/qpq4-k3td",
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
+            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/hospital-public-health-reporting",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-01",
-            "references": [
-                "https://www.healthit.gov/data/quickstats/hospital-selection-public-health-measures-state"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/hospital-public-health-reporting",
+            "description": "The Centers for Medicare &amp; Medicaid Services (CMS) EHR Incentive Program provides incentive payments for eligible hospitals to adopt and meaningfully use certified health IT. Among the requirements to receive an incentive payment, participating hospitals must report on public health measures. These measures include the electronic reporting of data regarding: immunizations, emergency department visits (syndromic surveillance), reportable infectious disease laboratory results, and electronic patient data to specialized registries, like cancert. As of 2015, stage 2 of the EHR Incentive Program requires hospitals to report on three public health measures, when applicable, and modified stage 2 of the program requires hospitals to report on two of the three measures. This dataset includes the percentage of hospitals who reported on these measures in program years, 2013, 2014 and 2015.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/hospital-mu-public-health-measures.csv",
+                    "mediaType": "text/csv",
+                    "title": "hospital-mu-public-health-measures.csv"
+                }
             ],
+            "identifier": "vzcc5ta0-36kx-g2f7-uzay-ps4jb0jt6xdw",
+            "issued": "2023-10-03",
             "keyword": [
                 "cms ehr incentive program",
                 "emergency department visits",
@@ -116934,71 +116944,33 @@
                 "public health measures",
                 "public health measures reporting"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/hospital-public-health-reporting",
+            "modified": "2017-01-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "vzcc5ta0-36kx-g2f7-uzay-ps4jb0jt6xdw",
-            "description": "The Centers for Medicare &amp; Medicaid Services (CMS) EHR Incentive Program provides incentive payments for eligible hospitals to adopt and meaningfully use certified health IT. Among the requirements to receive an incentive payment, participating hospitals must report on public health measures. These measures include the electronic reporting of data regarding: immunizations, emergency department visits (syndromic surveillance), reportable infectious disease laboratory results, and electronic patient data to specialized registries, like cancert. As of 2015, stage 2 of the EHR Incentive Program requires hospitals to report on three public health measures, when applicable, and modified stage 2 of the program requires hospitals to report on two of the three measures. This dataset includes the percentage of hospitals who reported on these measures in program years, 2013, 2014 and 2015.",
-            "title": "Hospital Public Health Reporting",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/hospital-mu-public-health-measures.csv",
-                    "mediaType": "text/csv",
-                    "title": "hospital-mu-public-health-measures.csv"
-                }
+            "references": [
+                "https://www.healthit.gov/data/quickstats/hospital-selection-public-health-measures-state"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/hospital-public-health-reporting"
+            "title": "Hospital Public Health Reporting"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-07-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
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
-            "identifier": "https://data.cdc.gov/api/views/hky2-3tpn",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
             "description": "This dataset contains model-based census tract level estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. These data can be joined with the census tract 2015 boundary file in a GIS system to produce maps for 36 measures at the census tract level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=2c3deb0c05a748b391ea8c9cf9903588",
-            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2023 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -117021,41 +116993,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
+            "identifier": "https://data.cdc.gov/api/views/hky2-3tpn",
+            "issued": "2024-07-15",
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-08-26",
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
+            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2023 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qgsr-s7bf",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-08-01",
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
-            "identifier": "53cf9f05-97e3-5bd6-a237-bc971e3642d9",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2016",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -117063,36 +117046,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "53cf9f05-97e3-5bd6-a237-bc971e3642d9",
+            "issued": "2016-08-01",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/qgsr-s7bf",
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
+            "title": "State Drug Utilization Data 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/re9g-kq7w",
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
-            "identifier": "https://data.cdc.gov/api/views/re9g-kq7w",
             "description": "Thermal spray coating is an industrial process where molten metal is sprayed onto a surface as a protective coat at high velocity. Using acellular, in vitro, and in vivo models, the toxicity of these aerosols was evaluated. An automated electric arc wire thermal spray coating aerosol generator and inhalation exposure system were developed to simulate an occupational exposure in an experimental model. Using the inhalation system, male Sprague-Dawley rats were exposed to stainless steel PMET720 aerosols at 25 mg/m3 x 4 hr/d x 9 d. Lung injury, inflammation, and cytokine alteration were determined. Resolution of the response was assessed by evaluating these parameters at 1, 7, 14 and 28 days after exposure. The aerosols generated were also collected and characterized. Macrophages were exposed to 0 \u2013 200 \u00b5g/ml of the collected particles to determine cytotoxicity and screened for known mechanisms of toxicity. Other metal particles similar in composition and morphology, gas metal arc (GMA-SS) and manual metal arc (MMA-SS) stainless steel, were used as particle controls. The influence of pressure used during the process on the toxicity profile of the generated aerosols also was assessed and found to be minimal. The PMET720 thermal spray coating particles exhibited in vitro cytotoxicity and membrane damage only at the highest dose tested. Electron paramagnetic resonance spectroscopy (EPR) showed the PMET720 particles to have oxidative stress potential and caused a dose-dependent increase in intracellular oxidative stress. There also was a dose-dependent increase in NF-kB/AP-1 activity. Treatment with uptake inhibitors showed that the PMET720 particles were internalized via clathrin- and caveolar-mediated endocytosis as wells as actin-dependent pinocytosis/phagocytosis. In most of the cell assays, the two welding fume control particles generated a greater response compared to the PMET720 particles. In vivo, lung damage, inflammation and alteration in cytokines were observed 1 day after inhalation exposure, and this response returned to air control exposure levels by day 7. Alveolar macrophages retained the particulate even after 28 days after exposure. The results suggest that compared to stainless steel welding fumes, the PMET 720 aerosols were less potent, and the animals recovered from the acute pulmonary toxicity induced after 7 days.",
-            "title": "In vivo and in vitro toxicity of a stainless-steel aerosol generated during thermal spray coating",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -117100,20 +117087,46 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/re9g-kq7w",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/re9g-kq7w",
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
+            "title": "In vivo and in vitro toxicity of a stainless-steel aerosol generated during thermal spray coating"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/intergovernmental-reference-guide-irg-policy-profies-and-contacts",
             "bureauCode": [
                 "009:70"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dennis Putze",
+                "hasEmail": "mailto:dennis.putze@acf.hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Child support program, policy, and local conatct information.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.acf.hhs.gov/programs/css/irg-state-map",
+                    "mediaType": "text/html",
+                    "title": "Map"
+                }
+            ],
+            "identifier": "d7cd8d21-678c-4565-8ffa-886189db7f86",
             "issued": "2014-02-07",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "administrative",
                 "age of majority",
@@ -117141,154 +117154,118 @@
                 "uniform interstate family support act",
                 "usa states"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dennis Putze",
-                "hasEmail": "mailto:dennis.putze@acf.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/intergovernmental-reference-guide-irg-policy-profies-and-contacts",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:084"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Administration for Children and Families, Department of Health & Human Services"
             },
-            "identifier": "d7cd8d21-678c-4565-8ffa-886189db7f86",
-            "description": "<p>Child support program, policy, and local conatct information.</p>",
-            "title": "Intergovernmental Reference Guide (IRG); Policy Profies and Contacts",
-            "programCode": [
-                "009:084"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.acf.hhs.gov/programs/css/irg-state-map",
-                    "mediaType": "text/html",
-                    "title": "Map"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "Intergovernmental Reference Guide (IRG); Policy Profies and Contacts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pdbp.ninds.nih.gov/",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "parkinsons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SUTHERLAND, MARGARET L",
                 "hasEmail": "mailto:sutherlandm@ninds.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "9047712c-cc5b-4a53-8cb0-a09d769af693",
+            "dataQuality": true,
             "description": "<p>The NINDS Parkinson\u2019s Disease (PD) Biomarkers Program Data Management Resource enables web-based data entry for clinical studies supporting PD biomarker development, as well as broad data sharing (imaging, clinical, genetic, and biospecimen analysis) across the entire PD research community. The PDBP DMR coordinates information and access to PD biospecimens distributed through the NINDS Human Genetics, DNA, iPSC , Cell Line and Biospecimen Repository and the Harvard Neurodiscovery Initiative.</p>",
-            "title": "Parkinson\u2019s Disease Biomarkers Program Data Management Resource (PDBP DMR)",
+            "identifier": "9047712c-cc5b-4a53-8cb0-a09d769af693",
+            "issued": "2016-07-17",
+            "keyword": [
+                "parkinsons"
+            ],
+            "landingPage": "https://pdbp.ninds.nih.gov/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:041"
             ],
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "dataQuality": true
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "title": "Parkinson\u2019s Disease Biomarkers Program Data Management Resource (PDBP DMR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qhz2-qcgn",
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
-            "identifier": "7ef3fd19-f2a2-5fbe-93c3-c9efd7247872",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt measure_value v2.10.22 (coreset-impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/measure_value.csv",
-                    "description": "CoreSEt measure_value v2.10.22 (coreset-impl)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt measure_value v2.10.22 (coreset-impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt measure_value v2.10.22 (coreset-impl)"
                 }
             ],
+            "identifier": "7ef3fd19-f2a2-5fbe-93c3-c9efd7247872",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/qhz2-qcgn",
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
+            "title": "CoreSEt measure_value v2.10.22 (coreset-impl)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies/medicare-durable-medical-equipment-devices-supplies-by-geography-and-service",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2014-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-04",
-            "references": [
-                "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
-                "medicare",
-                "national",
-                "original medicare",
-                "physicians & practitioners",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/27c150fd-8578-43b1-bba5-6388987e32af/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-by-geography-and-service-data-dictionary-2022",
             "description": "The Medicare Durable Medical Equipment, Devices & Supplies by Geography and Service dataset contains information on usage, payments, and submitted charges organized by geography, Healthcare Common Procedure Coding System (HCPCS) code, and supplier rental indicator.",
-            "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/27c150fd-8578-43b1-bba5-6388987e32af/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/27c150fd-8578-43b1-bba5-6388987e32af/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2022-12-30"
                 },
                 {
@@ -117400,53 +117377,51 @@
                     "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2014-12-16"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-by-geography-and-service-data-dictionary-2022",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/27c150fd-8578-43b1-bba5-6388987e32af/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "medicare",
+                "national",
+                "original medicare",
+                "physicians & practitioners",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies/medicare-durable-medical-equipment-devices-supplies-by-geography-and-service",
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
+                "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-methodology"
+            ],
+            "temporal": "2014-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ttjk-6u2v",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "anthrax",
-                "arboviral diseases",
-                "chikungunya virus disease",
-                "eastern equine encephalitis virus disease",
-                "nedss",
-                "netss",
-                "neuroinvasive and non-neuroinvasive",
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
-            "identifier": "https://data.cdc.gov/api/views/ttjk-6u2v",
             "description": "NNDSS - Table 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -117469,48 +117444,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ttjk-6u2v",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "anthrax",
+                "arboviral diseases",
+                "chikungunya virus disease",
+                "eastern equine encephalitis virus disease",
+                "nedss",
+                "netss",
+                "neuroinvasive and non-neuroinvasive",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ttjk-6u2v",
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
+            "title": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease"
         },
         {
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
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DDT Public Inquiries",
                 "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/a35h-9yn4",
+            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Shell-Commercial-Medical-Insurance-MSCANCC-Vision-/a35h-9yn4",
             "description": "2016. This dataset is a de-identified summary table of prevalence rates for vision and eye health data indicators from the 2016 MarketScan\u00ae Commercial Claims and Encounters Data (CCAE) is produced by Truven Health Analytics, a division of IBM Watson Health.  The CCEA data contain a convenience sample of insurance claims information from person with employer-sponsored insurance and their dependents, including 43.6 million person years of data. Prevalence estimates are stratified by all available combinations of age group, gender, and state.  Detailed information on VEHSS MarketScan analyses can be found on the VEHSS MarketScan webpage (cdc.gov/visionhealth/vehss/data/claims/marketscan.html). Information on available Medicare claims data can be found on the IBM MarketScan website (https://marketscan.truvenhealth.com). The VEHSS MarketScan summary dataset was last updated November 2019.",
-            "title": "Commercial Medical Insurance (MSCANCC) - Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -117533,21 +117508,59 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Shell-Commercial-Medical-Insurance-MSCANCC-Vision-/a35h-9yn4",
+            "identifier": "https://data.cdc.gov/api/views/a35h-9yn4",
+            "issued": "2024-12-20",
+            "keyword": [
+                "claims",
+                "diagnosed prevalence",
+                "eye exams",
+                "marketscan",
+                "medical diagnoses",
+                "service utilization",
+                "truven"
+            ],
+            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2024-12-20",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://wwwdev.cdc.gov/visionhealth/vehss/data/claims/marketscan.html",
+                "https://marketscan.truvenhealth.com/marketscanportal/"
+            ],
             "theme": [
                 "Vision & Eye Health"
-            ]
+            ],
+            "title": "Commercial Medical Insurance (MSCANCC) - Vision and Eye Health Surveillance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2006-2011",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and<br />\nhashish, heroin, nonprescription methadone, other opiates and<br />\nsynthetics, PCP, other hallucinogens, methamphetamine, other amphetamines,<br />\nother stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates,<br />\nother non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications,<br />\nand other substances.<br />\nCreated variables include total number<br />\nof substances reported, intravenous drug use (IDU), and flags for any<br />\nmention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2006-2011) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-2011-nid13578",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-2011-nid13578"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-2011-nid13578",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -117560,158 +117573,120 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2006-2011",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-2011-nid13578",
-            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and<br />\nhashish, heroin, nonprescription methadone, other opiates and<br />\nsynthetics, PCP, other hallucinogens, methamphetamine, other amphetamines,<br />\nother stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates,<br />\nother non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications,<br />\nand other substances.<br />\nCreated variables include total number<br />\nof substances reported, intravenous drug use (IDU), and flags for any<br />\nmention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2006-2011)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-2011-nid13578",
-                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2006-2011) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-2011-nid13578"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2006-2011)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qjb4-un5j",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-05",
-            "keyword": [
-                "chip",
-                "contraceptives",
-                "dq atlas",
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
-            "identifier": "eb88943c-309d-440f-a2d5-ef93e066d83c",
             "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of contraceptives, including any contraceptives and long-acting reversible contraceptives, provided to female Medicaid and CHIP beneficiaries ages 15 to 44 (as of the first day of the month), by state. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating contraceptive care services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Contraceptive Care Services Provided to Medicaid and CHIP Beneficiaries ages 15 to 44",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/Contraceptive-Care-Services-Provided-to-MedicaidCHIP-Beneficiaries-ages-15-to-44.csv",
-                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of contraceptives, including any contraceptives and long-acting reversible contraceptives, provided to female Medicaid and CHIP beneficiaries ages 15 to 44 (as of the first day of the month), by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating contraceptive care services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of contraceptives, including any contraceptives and long-acting reversible contraceptives, provided to female Medicaid and CHIP beneficiaries ages 15 to 44 (as of the first day of the month), by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating contraceptive care services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/Contraceptive-Care-Services-Provided-to-MedicaidCHIP-Beneficiaries-ages-15-to-44.csv",
+                    "mediaType": "text/csv",
                     "title": "Contraceptive Care Services Provided to Medicaid and CHIP Beneficiaries ages 15 to 44"
                 }
             ],
+            "identifier": "eb88943c-309d-440f-a2d5-ef93e066d83c",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "contraceptives",
+                "dq atlas",
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/qjb4-un5j",
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
                 "Uncategorized"
-            ]
+            ],
+            "title": "Contraceptive Care Services Provided to Medicaid and CHIP Beneficiaries ages 15 to 44"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qjcp-amex",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-16",
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
-            "identifier": "047d3943-6ed3-532e-8eb4-eb67e9b6afc3",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard TAG v0.2.4-1 (dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.2.4-1/TAG.csv",
-                    "description": "Scorecard TAG v0.2.4-1 (dev)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard TAG v0.2.4-1 (dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.2.4-1/TAG.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard TAG v0.2.4-1 (dev)"
                 }
             ],
+            "identifier": "047d3943-6ed3-532e-8eb4-eb67e9b6afc3",
+            "issued": "2023-03-28",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/qjcp-amex",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-05-16",
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
+            "title": "Scorecard TAG v0.2.4-1 (dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/dp9i-idru",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-            "identifier": "https://data.cdc.gov/api/views/dp9i-idru",
             "description": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease, Age <5 years, Serotype b - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease, Age <5 years, Serotype b",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -117734,40 +117709,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/dp9i-idru",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
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
+            "landingPage": "https://data.cdc.gov/d/dp9i-idru",
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
+            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease, Age <5 years, Serotype b"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/crtu-weni",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-08-05",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "adults",
-                "diabetes",
-                "hus"
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
-            "identifier": "https://data.cdc.gov/api/views/crtu-weni",
             "description": "Health, United States is an annual report on trends in health statistics, find more information at http://www.cdc.gov/nchs/hus.htm.",
-            "title": "Selected Trend Table from Health, United States, 2011. Diabetes prevalence and glycemic control among adults 20 years of age and over, by sex, age, and race and Hispanic origin: United States, selected years 1988 - 1994 through 2003 - 2006",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -117790,86 +117772,89 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/crtu-weni",
+            "issued": "2013-08-05",
+            "keyword": [
+                "adults",
+                "diabetes",
+                "hus"
+            ],
+            "landingPage": "https://data.cdc.gov/d/crtu-weni",
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
+            "title": "Selected Trend Table from Health, United States, 2011. Diabetes prevalence and glycemic control among adults 20 years of age and over, by sex, age, and race and Hispanic origin: United States, selected years 1988 - 1994 through 2003 - 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qkzp-9x7x",
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
-            "identifier": "78430aaa-df0a-5343-92a5-395dcf7c5e33",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_measure_concernLevel",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_concernLevel.csv",
-                    "description": "{\"dataset\": \"measure_concernLevel\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_concernLevel\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_concernLevel.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_concernLevel csv file"
                 }
             ],
+            "identifier": "78430aaa-df0a-5343-92a5-395dcf7c5e33",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/qkzp-9x7x",
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
+            "title": "featAuto_measure_concernLevel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qm9a-s4n5",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-07-20",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-18",
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
-            "identifier": "55978f20-d0db-49a0-a304-1c4471367a95",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-10-to-2023-07-16",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -117878,51 +117863,45 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-10-to-2023-07-16"
                 }
             ],
+            "identifier": "55978f20-d0db-49a0-a304-1c4471367a95",
+            "issued": "2023-07-20",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/qm9a-s4n5",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-07-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-10-to-2023-07-16"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-change-of-ownership",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-04-21",
-            "temporal": "2022-01-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-10/Hospital_CHOW_Data_Guidance.pdf"
-            ],
-            "keyword": [
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/c04031db-54ce-461c-85d1-d2613d71f167/data-viewer",
-            "description": "The Hospital Change of Ownership (CHOW) dataset provides information on the hospital ownership changes that occurred on or after January 1, 2016. This data includes information on the buyer and seller organization\u2019s legal business name, provider type, change of ownership type (CHOW, Acquisition/Merger, or Consolidation) and the effective date of the change.",
-            "title": "Hospital Change of Ownership",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-01/Hospital_CHOW_Data_Dictionary_2022.12.30.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Hospital Change of Ownership (CHOW) dataset provides information on the hospital ownership changes that occurred on or after January 1, 2016. This data includes information on the buyer and seller organization\u2019s legal business name, provider type, change of ownership type (CHOW, Acquisition/Merger, or Consolidation) and the effective date of the change.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c04031db-54ce-461c-85d1-d2613d71f167/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c04031db-54ce-461c-85d1-d2613d71f167/data",
+                    "mediaType": "text/html",
                     "title": "Hospital Change of Ownership : 2024-12-01"
                 },
                 {
@@ -118070,50 +118049,50 @@
                     "title": "Hospital Change of Ownership : 2022-03-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2023-01/Hospital_CHOW_Data_Dictionary_2022.12.30.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/c04031db-54ce-461c-85d1-d2613d71f167/data-viewer",
+            "issued": "2022-04-21",
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-change-of-ownership",
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
+                "https://data.cms.gov/sites/default/files/2024-10/Hospital_CHOW_Data_Guidance.pdf"
+            ],
+            "temporal": "2022-01-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Hospital Change of Ownership"
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
-            "temporal": "2024-2025",
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
-            "identifier": "https://data.cdc.gov/api/views/ksfb-ug5d",
             "description": "Weekly COVID-19 Vaccination Coverage and intent among adults 18 Years and Older by Demographic Characteristics and Jurisdiction \u2022 Weekly estimates of COVID-19 vaccination coverage and intent among adults 18 years and older are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/). \n\nWeekly comparisons to previous season should take into account differences between seasons in vaccine availability dates. 2023\u201324 COVID-19 vaccines were first available mid-September 2023, and 2024\u201325 COVID-19 vaccines were first available at the end of August 2024.",
-            "title": "Weekly Cumulative COVID-19 Vaccination Coverage and Intent, Overall, by Selected Demographics and Jurisdiction, Among Adults 18 Years and Older",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -118136,53 +118115,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/ksfb-ug5d",
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
+            "temporal": "2024-2025",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative COVID-19 Vaccination Coverage and Intent, Overall, by Selected Demographics and Jurisdiction, Among Adults 18 Years and Older"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7pb7-w9us",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
-            "keyword": [
-                "2015",
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
-            "identifier": "https://data.cdc.gov/api/views/7pb7-w9us",
             "description": "NNDSS - Table II. Lyme disease to Meningococcal - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Data for meningococcal disease, invasive caused by serogroups ACWY; serogroup B; other serogroup; and unknown serogroup are available in Table I.",
-            "title": "NNDSS - Table II. Lyme disease to Meningococcal",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -118205,118 +118179,156 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7pb7-w9us",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
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
+            "landingPage": "https://data.cdc.gov/d/7pb7-w9us",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-01-07",
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
-            "landingPage": "https://healthdata.gov/d/qngr-rkng",
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
-            "identifier": "cb8d7614-bf80-5ffd-a166-4f3903f1ddd4",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_measure_compare",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_compare.csv",
-                    "description": "{\"dataset\": \"measure_compare\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_compare\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_compare.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_compare csv file"
                 }
             ],
+            "identifier": "cb8d7614-bf80-5ffd-a166-4f3903f1ddd4",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/qngr-rkng",
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
+            "title": "devAuto_measure_compare"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qp4n-462d",
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
-            "identifier": "cf8cfb80-9c92-5582-adbc-11c22f5ed9bc",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_topicArea_measureDisplayGroups",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/topicArea_measureDisplayGroups.csv",
-                    "description": "{\"dataset\": \"topicArea_measureDisplayGroups\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"topicArea_measureDisplayGroups\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/topicArea_measureDisplayGroups.csv",
+                    "mediaType": "text/csv",
                     "title": "topicArea_measureDisplayGroups csv file"
                 }
             ],
+            "identifier": "cf8cfb80-9c92-5582-adbc-11c22f5ed9bc",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/qp4n-462d",
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
+            "title": "devAuto_topicArea_measureDisplayGroups"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "NHDS - National Hospital Discharge Survey Homepage (cdc.gov)",
+            "accrualPeriodicity": "Database will not be updated again.",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "Restricted data files can be requested through the Research Data Center. Restricted files contain sensitive protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:nhcs@cdc.gov"
+            },
+            "description": "The National Hospital Discharge Survey (NHDS), conducted from 1965 to 2010, was a national probability survey designed to meet the need for information on characteristics of inpatients discharged from non-Federal short-stay hospitals in the United States. From 1988-2007 the NHDS collected data from a sample of approximately 270,000 inpatient records acquired from a national sample of about 500 hospitals. From 2008 to 2010 the sample size was reduced to 239. Only hospitals with an average length of stay of fewer than 30 days for all patients, general hospitals, or children\u2019s general hospitals are included in the survey. Federal, military, and Department of Veterans Affairs hospitals, as well as hospital units of institutions (such as prison hospitals), and hospitals with fewer than six beds staffed for patient use, are excluded.\nBeginning in 1988, two data collection procedures have been used in the survey. The medical abstract form and the automated data tapes contain items that relate to the personal characteristics of the patient. These items include age, sex, race, ethnicity, marital status, and expected sources of payment. Administrative items such as admission and discharge dates (which allow calculation of length of stay), as well as discharge status are also included. Medical information about patients includes diagnoses and procedures coded to the International Classification of Diseases, 9th Revision, Clinical Modification (ICD-9-CM).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Links to downloadable data files and data documentation included.",
+                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHDS/",
+                    "mediaType": "text/html",
+                    "title": "NHDS 1970-2010"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/9f67-8jse",
             "issued": "2010-05-19",
-            "@type": "dcat:Dataset",
-            "temporal": "1970\u20142010",
-            "modified": "2024-02-20",
             "keyword": [
                 "discharge",
                 "hospital",
@@ -118325,99 +118337,69 @@
                 "sdoh-use-of-health-care",
                 "short-stay-hospitals"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:nhcs@cdc.gov"
-            },
+            "landingPage": "NHDS - National Hospital Discharge Survey Homepage (cdc.gov)",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-02-20",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/9f67-8jse",
-            "description": "The National Hospital Discharge Survey (NHDS), conducted from 1965 to 2010, was a national probability survey designed to meet the need for information on characteristics of inpatients discharged from non-Federal short-stay hospitals in the United States. From 1988-2007 the NHDS collected data from a sample of approximately 270,000 inpatient records acquired from a national sample of about 500 hospitals. From 2008 to 2010 the sample size was reduced to 239. Only hospitals with an average length of stay of fewer than 30 days for all patients, general hospitals, or children\u2019s general hospitals are included in the survey. Federal, military, and Department of Veterans Affairs hospitals, as well as hospital units of institutions (such as prison hospitals), and hospitals with fewer than six beds staffed for patient use, are excluded.\nBeginning in 1988, two data collection procedures have been used in the survey. The medical abstract form and the automated data tapes contain items that relate to the personal characteristics of the patient. These items include age, sex, race, ethnicity, marital status, and expected sources of payment. Administrative items such as admission and discharge dates (which allow calculation of length of stay), as well as discharge status are also included. Medical information about patients includes diagnoses and procedures coded to the International Classification of Diseases, 9th Revision, Clinical Modification (ICD-9-CM).",
-            "title": "National Hospital Discharge Survey (NHDS) 1970-2010",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHDS/",
-                    "description": "Links to downloadable data files and data documentation included.",
-                    "@type": "dcat:Distribution",
-                    "title": "NHDS 1970-2010"
-                }
-            ],
+            "rights": "Restricted data files can be requested through the Research Data Center. Restricted files contain sensitive protected health information.",
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Database will not be updated again.",
+            "temporal": "1970\u20142010",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Hospital Discharge Survey (NHDS) 1970-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nursa.org/index.cfm",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "national-institutes-of-health-nih"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HYDE, JAMES F\u00a0",
                 "hasEmail": "mailto:hydej@niddk.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "ff71e3cf-f17b-463c-97ef-c0b61c2bb9c0",
+            "dataQuality": true,
             "description": "<p>The Nuclear Receptor Signaling Atlas (NURSA) is designed to foster the development of a comprehensive understanding of the structure, function, and role in disease of nuclear receptors (NRs) and coregulators. NURSA seeks to elucidate the roles played by NRs and coregulators in metabolism and the development of metabolic disorders (including type 2 diabetes, obesity, osteoporosis, and lipid dysregulation), as well as in cardiovascular disease, oncology, regenerative medicine and the effects of environmental agents on their actions.</p>",
-            "title": "Nuclear Receptor Signaling Atlas (NURSA)",
+            "identifier": "ff71e3cf-f17b-463c-97ef-c0b61c2bb9c0",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.nursa.org/index.cfm",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
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
+            "title": "Nuclear Receptor Signaling Atlas (NURSA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://classification.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "classification",
-                "dataset",
-                "library services"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/a7sv-mxd2",
             "description": "A product of the National Library of Medicine for the arrangement of library materials in the field of medicine and related sciences used internationally.  The NLM Classification is updated twice a year with the winter edition published in January and the summer edition published in August. Publication of printed editions ceased with the 5th revised edition, 1999. Beginning with the 2006 edition, the NLM Classification is also available in PDF (Portable Document Format) at https://www.nlm.nih.gov/class/terms_cond.html",
-            "title": "NLM Classification",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -118438,10 +118420,10 @@
                     "title": "Class Numbers Added (Cumulative List)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://classification.nlm.nih.gov/cumulative_class_numbers_canceled",
-                    "description": "The National Library of Medicine cancels classification numbers from its schedules for a variety of reasons - most often classification numbers are realigned to better reflect their domain and improve collocation of materials on related concepts.",
                     "@type": "dcat:Distribution",
+                    "description": "The National Library of Medicine cancels classification numbers from its schedules for a variety of reasons - most often classification numbers are realigned to better reflect their domain and improve collocation of materials on related concepts.",
+                    "downloadURL": "https://classification.nlm.nih.gov/cumulative_class_numbers_canceled",
+                    "mediaType": "text/html",
                     "title": "Canceled Class Numbers (Cumulative List)"
                 },
                 {
@@ -118451,52 +118433,54 @@
                     "title": "Outline of the NLM Classification"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://classification.nlm.nih.gov/tableg",
-                    "description": "Table G is a cutter system of notations that provides geographical or jurisdictional arrangement of materials under specific class numbers in the NLM Classification. The use of Table G permits a shelving order which is controlled geographically and alphabetically.",
                     "@type": "dcat:Distribution",
+                    "description": "Table G is a cutter system of notations that provides geographical or jurisdictional arrangement of materials under specific class numbers in the NLM Classification. The use of Table G permits a shelving order which is controlled geographically and alphabetically.",
+                    "downloadURL": "https://classification.nlm.nih.gov/tableg",
+                    "mediaType": "text/html",
                     "title": "Table G (Geographic Notation)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://classification.nlm.nih.gov/19century_schedule",
-                    "description": "Classify here works and reprints of works published between 1801-1913. Classify here translations of works originally published from 1801-1913 only if the translation itself is published from 1801-1913.",
                     "@type": "dcat:Distribution",
+                    "description": "Classify here works and reprints of works published between 1801-1913. Classify here translations of works originally published from 1801-1913 only if the translation itself is published from 1801-1913.",
+                    "downloadURL": "https://classification.nlm.nih.gov/19century_schedule",
+                    "mediaType": "text/html",
                     "title": "19th Century Schedule"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/a7sv-mxd2",
+            "issued": "2021-08-26",
+            "keyword": [
+                "classification",
+                "dataset",
+                "library services"
+            ],
+            "landingPage": "https://classification.nlm.nih.gov/",
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
+            "title": "NLM Classification"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qrfh-d6pe",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-11-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-25",
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
-            "identifier": "ea9cd328-bfc4-4444-b02a-0411d93e419a",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 11-18-2024-to-11-24-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -118504,42 +118488,35 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "ea9cd328-bfc4-4444-b02a-0411d93e419a",
+            "issued": "2024-11-27",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/qrfh-d6pe",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-25",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 11-18-2024-to-11-24-2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/759d-qk63",
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
-            "identifier": "https://data.cdc.gov/api/views/759d-qk63",
             "description": "NNDSS - TABLE 1KK. Vancomycin-intermediate Staphylococcus aureus to Varicella morbidity \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1KK. Vancomycin-intermediate Staphylococcus aureus to Varicella morbidity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -118562,38 +118539,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/759d-qk63",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "vancomycin-intermediate staphylococcus aureus",
+                "vancomycin-resistant staphylococcus aureus",
+                "varicella morbidity",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/759d-qk63",
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
+            "title": "NNDSS - TABLE 1KK. Vancomycin-intermediate Staphylococcus aureus to Varicella morbidity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qshf-g2pe",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-03-30",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-29",
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
-            "identifier": "f7e2cee0-4e65-4c44-8a28-4dab252a8e5b",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-03-21 to 2022-03-27",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -118601,20 +118586,46 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "f7e2cee0-4e65-4c44-8a28-4dab252a8e5b",
+            "issued": "2022-03-30",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/qshf-g2pe",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2022-03-29",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-03-21 to 2022-03-27"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/airz-k28h",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS5-technical-documentation.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The fifth round of RANDS (RANDS 5) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from January 1, 2022 to March 9, 2022. RANDS 5 contained the embedded probe questions and experiments as in previous rounds of RANDS. It also examined responses to gender identity questions as well as different survey administrations of questions appearing in CDC\u2019s National Intimate Partner and Sexual Violence Survey (NISVS). RANDS 5 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/airz-k28h",
             "issued": "2023-02-22",
-            "@type": "dcat:Dataset",
-            "temporal": "2022",
-            "modified": "2023-04-20",
             "keyword": [
                 "gender identity",
                 "intimate partner violence",
@@ -118624,78 +118635,45 @@
                 "sexual violence",
                 "stalking"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/airz-k28h",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-04-20",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/airz-k28h",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The fifth round of RANDS (RANDS 5) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from January 1, 2022 to March 9, 2022. RANDS 5 contained the embedded probe questions and experiments as in previous rounds of RANDS. It also examined responses to gender identity questions as well as different survey administrations of questions appearing in CDC\u2019s National Intimate Partner and Sexual Violence Survey (NISVS). RANDS 5 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
-            "title": "NCHS Research and Development Survey (RANDS) Round 5 Restricted File",
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
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS5-technical-documentation.pdf",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "2022",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 5 Restricted File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies/medicare-durable-medical-equipment-devices-supplies-by-referring-provider-and-service",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2014-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-04",
-            "references": [
-                "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
-                "medical suppliers & equipment",
-                "medicare",
-                "original medicare",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/86b4807a-d63a-44be-bfdf-ffd398d5e623/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-by-referring-provider-and-service-data-dictionary",
             "description": "The Medicare Durable Medical Equipment, Devices & Supplies by Referring Provider and Service dataset contains information on usage, payments and submitted charges organized by National Provider Identifier (NPI), Healthcare Common Procedure Coding System (HCPCS) code, and supplier rental indicator.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/86b4807a-d63a-44be-bfdf-ffd398d5e623/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/86b4807a-d63a-44be-bfdf-ffd398d5e623/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2022-12-30"
                 },
                 {
@@ -118807,90 +118785,83 @@
                     "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2014-12-30"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-by-referring-provider-and-service-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/86b4807a-d63a-44be-bfdf-ffd398d5e623/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "medical suppliers & equipment",
+                "medicare",
+                "original medicare",
+                "physicians & practitioners"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies/medicare-durable-medical-equipment-devices-supplies-by-referring-provider-and-service",
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
+                "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-methodology"
+            ],
+            "temporal": "2014-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/adoption-and-foster-care-analysis-and-reporting-system-trends-chart-and-table",
             "bureauCode": [
                 "009:70"
             ],
-            "issued": "2013-01-18",
-            "temporal": "2010-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "adoption and foster care",
-                "children's health"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "admin",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Administration for Children and Families"
-            },
-            "identifier": "186960c3-830b-4181-9c12-b965b051047f",
+            "dataQuality": true,
             "description": "<p>The AFCARS Trends Chart tracks children in Foster Care from FY 2002 through the most recent year.  A table of data and a graphic depiction of trends are shown for children in care on the first day of the year, entries to foster care, exits, children waiting to be adopted,  children adopted, children with terminations of parental rights, and total children served in foster care.</p>",
-            "title": "Adoption and Foster Care Analysis and Reporting System Trends Chart and Table",
+            "identifier": "186960c3-830b-4181-9c12-b965b051047f",
+            "issued": "2013-01-18",
+            "keyword": [
+                "adoption and foster care",
+                "children's health"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/adoption-and-foster-care-analysis-and-reporting-system-trends-chart-and-table",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:101"
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families"
             },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2021-02-01",
-            "temporal": "2020-03-01/2020-07-31",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "hispanic origin",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "race",
-                "sex",
-                "united states"
+            "temporal": "2010-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
+            "title": "Adoption and Foster Care Analysis and Reporting System Trends Chart and Table"
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/s9qn-46pq",
             "description": "Provisional counts of deaths in the United States by age group, sex, and race/ethnicity, from March-July 2020. The dataset includes cumulative provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
-            "title": "AH Provisional COVID-19 Deaths By Race, Age, and Sex from 3/1/2020 to 7/31/2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -118913,52 +118884,61 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/s9qn-46pq",
+            "issued": "2021-02-01",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hispanic origin",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "race",
+                "sex",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
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
+            "temporal": "2020-03-01/2020-07-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths By Race, Age, and Sex from 3/1/2020 to 7/31/2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/revalidation-due-date-list",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2022-02-01/2025-01-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-02",
-            "references": [
-                "https://data.cms.gov/resources/additional-information-on-revalidation"
-            ],
-            "keyword": [
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/3746498e-874d-45d8-9c69-68603cafea60/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/revalidation-due-date-list-data-dictionary",
             "description": "The Revalidation Due Date List dataset contains revalidation due dates for Medicare providers who are due to revalidate in the following six months. If a provider's due date does not fall within the ensuing six months, the due date is marked 'TBD'. In addition the dataset also includes subfiles with reassignment information for a given provider as well as due date listings for clinics and group practices and their providers.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Revalidation Due Date List",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3746498e-874d-45d8-9c69-68603cafea60/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3746498e-874d-45d8-9c69-68603cafea60/data",
+                    "mediaType": "text/html",
                     "title": "Revalidation Due Date List : 2025-01-01"
                 },
                 {
@@ -119262,55 +119242,49 @@
                     "title": "Revalidation Due Date List : 2022-02-28"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/revalidation-due-date-list-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/3746498e-874d-45d8-9c69-68603cafea60/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/revalidation-due-date-list",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2025-01-02",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/additional-information-on-revalidation"
+            ],
+            "temporal": "2022-02-01/2025-01-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Revalidation Due Date List"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-06-24",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-27",
-            "keyword": [
-                "all causes",
-                "coronavirus",
-                "county",
-                "covid-19",
-                "deaths",
-                "hispanic origin",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "race",
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
-            "identifier": "https://data.cdc.gov/api/views/k8wy-p9cg",
             "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nCounty data on race and Hispanic origin is available for counties with more than 100 COVID-19 deaths.\u00a0Deaths are cumulative from the week ending January 4, 2020 to the most recent reporting week, and based on county of occurrence. Data is provisional. \n\nUrban-rural classification is based on the 2013 National Center for Health Statistics Urban-Rural Classification Scheme for Counties (https://www.cdc.gov/nchs/data_access/urban_rural.htm).",
-            "title": "Provisional COVID-19 Deaths by County, and Race and Hispanic Origin",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -119333,58 +119307,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/k8wy-p9cg",
+            "issued": "2020-06-24",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "county",
+                "covid-19",
+                "deaths",
+                "hispanic origin",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "race",
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
+            "spatial": "United States",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional COVID-19 Deaths by County, and Race and Hispanic Origin"
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
-            "temporal": "1960/2018",
-            "modified": "2022-03-28",
-            "references": [
-                "https://www.cdc.gov/nchs/data/vsus/vsus_1950_1.pdf",
-                "https://www.cdc.gov/nchs/data/misc/usvss.pdf",
-                "https://www.cdc.gov/nchs/data/vsus/nat67_1.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
-                "https://www.cdc.gov/nvsr/nvsr67/nvsr67_01.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13.pdf"
-            ],
-            "keyword": [
-                "birth rates",
-                "births",
-                "ethnicity",
-                "fertility rates",
-                "hispanic origin",
-                "nchs",
-                "race",
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
-            "identifier": "https://data.cdc.gov/api/views/89yk-m38d",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "This dataset includes live births, birth rates, and fertility rates by race of mother in the United States since 1960. \n\nData availability varies by race and ethnicity groups. All birth data by race before 1980 are based on race of the child. Since 1980, birth data by race are based on race of the mother. For race, data are available for Black and White births since 1960, and for American Indians/Alaska Native and Asian/Pacific Islander births since 1980. Data on Hispanic origin are available since 1989. Teen birth rates for specific racial and ethnic categories are also available since 1989. From 2003 through 2015, the birth data by race were based on the \u201cbridged\u201d race categories (5). Starting in 2016, the race categories for reporting birth data changed; the new race and Hispanic origin categories are: Non-Hispanic, Single Race White; Non-Hispanic, Single Race Black; Non-Hispanic, Single Race American Indian/Alaska Native; Non-Hispanic, Single Race Asian; and, Non-Hispanic, Single Race Native Hawaiian/Pacific Islander (5,6). Birth data by the prior, \u201cbridged\u201d race (and Hispanic origin) categories are included through 2018 for comparison.\n\nSOURCES\n\nNCHS, National Vital Statistics System, birth data (see https://www.cdc.gov/nchs/births.htm); public-use data files (see https://www.cdc.gov/nchs/data_access/VitalStatsOnline.htm); and CDC WONDER (see http://wonder.cdc.gov/).\n\nREFERENCES\n\n1. National Office of Vital Statistics. Vital Statistics of the United States, 1950, Volume I. 1954. Available from: https://www.cdc.gov/nchs/data/vsus/vsus_1950_1.pdf.\n\n2. Hetzel AM. U.S. vital statistics system: major activities and developments, 1950-95. National Center for Health Statistics. 1997. Available from: https://www.cdc.gov/nchs/data/misc/usvss.pdf.\n\n3. National Center for Health Statistics. Vital Statistics of the United States, 1967, Volume I\u2013Natality. 1969. Available from: https://www.cdc.gov/nchs/data/vsus/nat67_1.pdf.\n\n4. Martin JA, Hamilton BE, Osterman MJK, et al. Births: Final data for 2015. National vital statistics reports; vol 66 no 1. Hyattsville, MD: National Center for Health Statistics. 2017. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf.\n\n5. Martin JA, Hamilton BE, Osterman MJK, Driscoll AK, Drake P. Births: Final data for 2016. National Vital Statistics Reports; vol 67 no 1. Hyattsville, MD: National Center for Health Statistics. 2018. Available from: https://www.cdc.gov/nvsr/nvsr67/nvsr67_01.pdf.\n\n6. Martin JA, Hamilton BE, Osterman MJK, Driscoll AK, Births: Final data for 2018. National vital statistics reports; vol 68 no 13. Hyattsville, MD: National Center for Health Statistics. 2019. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13.pdf.",
-            "title": "NCHS - Natality Measures for Females by Race and Hispanic Origin: United States",
-            "isPartOf": "NCHS - Natality Measures for Females by Race and Hispanic Origin: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -119407,57 +119374,61 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
-            "license": "https://www.usa.gov/government-works",
-            "theme": [
-                "NCHS"
+            "identifier": "https://data.cdc.gov/api/views/89yk-m38d",
+            "isPartOf": "NCHS - Natality Measures for Females by Race and Hispanic Origin: United States",
+            "issued": "2015-12-02",
+            "keyword": [
+                "birth rates",
+                "births",
+                "ethnicity",
+                "fertility rates",
+                "hispanic origin",
+                "nchs",
+                "race",
+                "united states"
             ],
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "language": [
                 "English"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
-            "bureauCode": [
-                "009:20"
             ],
-            "rights": "public",
-            "issued": "2015-12-02",
-            "@type": "dcat:Dataset",
-            "temporal": "1989/2018",
-            "modified": "2022-03-29",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-03-28",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "references": [
+                "https://www.cdc.gov/nchs/data/vsus/vsus_1950_1.pdf",
+                "https://www.cdc.gov/nchs/data/misc/usvss.pdf",
+                "https://www.cdc.gov/nchs/data/vsus/nat67_1.pdf",
                 "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
                 "https://www.cdc.gov/nvsr/nvsr67/nvsr67_01.pdf",
                 "https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13.pdf"
             ],
-            "keyword": [
-                "birth",
-                "birth rate",
-                "ethnicity",
-                "fertility rate",
-                "hispanic origin",
-                "nchs",
-                "united states"
+            "rights": "public",
+            "spatial": "50 states and District of Columbia",
+            "temporal": "1960/2018",
+            "theme": [
+                "NCHS"
+            ],
+            "title": "NCHS - Natality Measures for Females by Race and Hispanic Origin: United States"
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
                 "hasEmail": "mailto:births@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/s54h-bixi",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "This dataset includes live births, birth rates, and fertility rates by Hispanic origin of mother in the United States since 1989. \n\nNational data on births by Hispanic origin exclude data for Louisiana, New Hampshire, and Oklahoma in 1989; New Hampshire and Oklahoma in 1990; and New Hampshire in 1991 and 1992. Birth and fertility rates for the Central and South American population includes other and unknown Hispanic. Information on reporting Hispanic origin is detailed in the Technical Appendix for the 1999 public-use natality data file (see ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/Nat1999doc.pdf).",
-            "title": "NCHS - Natality Measures for Females by Hispanic Origin Subgroup: United States",
-            "isPartOf": "NCHS - Natality Measures for Females by Hispanic Origin Subgroup: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -119480,53 +119451,57 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/s54h-bixi",
+            "isPartOf": "NCHS - Natality Measures for Females by Hispanic Origin Subgroup: United States",
+            "issued": "2015-12-02",
+            "keyword": [
+                "birth",
+                "birth rate",
+                "ethnicity",
+                "fertility rate",
+                "hispanic origin",
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
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
+                "https://www.cdc.gov/nvsr/nvsr67/nvsr67_01.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13.pdf"
+            ],
+            "rights": "public",
+            "spatial": "50 states and District of Columbia",
+            "temporal": "1989/2018",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - Natality Measures for Females by Hispanic Origin Subgroup: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5c6r-xi2t",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-09",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024 respiratory virus season",
-            "modified": "2025-01-24",
-            "keyword": [
-                "coronavirus",
-                "covid19",
-                "immunization",
-                "ncird",
-                "nis-acm",
-                "nis-ccm",
-                "respiratory-virus-response",
-                "rsv",
-                "vaccination",
-                "vaccination-coverage"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James Singleton",
                 "hasEmail": "mailto:vaxview@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5c6r-xi2t",
             "description": "The weekly respiratory virus vaccination data come from the National Immunization Survey-Adult COVID Module (NIS-ACM), National Immunization Survey-Child COVID Module (NIS-CCM), and the National Immunization Survey-Flu (NIS-Flu). The NIS-ACM provides data on Influenza (flu), COVID-19, and RSV vaccination for adults aged \u226518 years in the United States. The NIS-CCM provides data on COVID-19 vaccination for children aged 6 months-17 years in the United States. The NIS-Flu provides data on Influenza vaccination for children aged 6 months-17 years in the United States National Immunization Survey data are collected by telephone interview using a random-digit-dialed sample of cellular telephone numbers stratified by state, the District of Columbia, five local jurisdictions (Bexar County TX, Chicago IL, Houston TX, New York City NY, and Philadelphia County PA), and Guam, Puerto Rico, and the United States Virgin Islands. Data are weighted to represent the non-institutionalized United States population and mitigate possible bias that can result from incomplete sample frame (exclusion of households with no phone service or only landline telephones) or non-response. All responses are self-reported, or reported by a parent for children 6 months-17 years. For more information about the surveys, see\u202fhttps://www.cdc.gov/vaccines/imz-managers/nis/about.html#current-surveys. Estimates should be interpreted with caution when there is a small sample size or wide confidence interval.\u202f",
-            "title": "Weekly Respiratory Virus Vaccination Data, Children 6 Months-17 Years and Adults 18 Years and Older, National Immunization Survey",
-            "programCode": [
-                "009:037"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -119549,43 +119524,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/5c6r-xi2t",
+            "issued": "2023-11-09",
+            "keyword": [
+                "coronavirus",
+                "covid19",
+                "immunization",
+                "ncird",
+                "nis-acm",
+                "nis-ccm",
+                "respiratory-virus-response",
+                "rsv",
+                "vaccination",
+                "vaccination-coverage"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5c6r-xi2t",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-24",
+            "programCode": [
+                "009:037"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "U.S.",
+            "temporal": "2023-2024 respiratory virus season",
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "Weekly Respiratory Virus Vaccination Data, Children 6 Months-17 Years and Adults 18 Years and Older, National Immunization Survey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/t984-9cdv",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-08-13",
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
-            "identifier": "https://data.cdc.gov/api/views/t984-9cdv",
             "description": "Percentages are weighted to population characteristics. Data are not available if it did not meet BRFSS stability requirements. For more information on these requirements, as well as risk factors and calculated variables, see the Technical Documents and Survey Data for a specific year - http://www.cdc.gov/brfss/annual_data/annual_data.htm. Recommended citation: Centers for Disease Control and Prevention (CDC). Behavioral Risk Factor Surveillance System. Atlanta, Georgia: U.S. Department of Health and Human Services, Centers for Disease Control and Prevention, [appropriate year].",
-            "title": "BRFSS Prevalence And Trends Data: Health Care Access/Coverage for 1995-2010",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -119608,89 +119589,90 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/t984-9cdv",
+            "issued": "2013-08-13",
+            "keyword": [
+                "adults",
+                "brfss",
+                "health care coverage",
+                "heath care access"
+            ],
+            "landingPage": "https://data.cdc.gov/d/t984-9cdv",
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
+            "title": "BRFSS Prevalence And Trends Data: Health Care Access/Coverage for 1995-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qvpz-fkkp",
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
-            "identifier": "d2469e00-b3f0-568b-8f66-658ee6e67c86",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_states_measures_download",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states_measures_download.csv",
-                    "description": "{\"dataset\": \"states_measures_download\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"states_measures_download\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states_measures_download.csv",
+                    "mediaType": "text/csv",
                     "title": "states_measures_download csv file"
                 }
             ],
+            "identifier": "d2469e00-b3f0-568b-8f66-658ee6e67c86",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/qvpz-fkkp",
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
+            "title": "implAuto_states_measures_download"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/techlab/ipg/",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-03",
-            "keyword": [
-                "data standards",
-                "health care",
-                "health it",
-                "interoperability"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ONC Request",
                 "hasEmail": "mailto:onc.request@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the National Coordinator for Health Information Technology"
-            },
-            "identifier": "obq8zsu3-97j2-kg6f-m27a-jblq9u0jqg4s",
+            "describedBy": "https://www.healthit.gov/techlab/ipg/",
             "description": "The Interoperability Proving Ground (IPG) is an open, community platform where you can share, learn, and be inspired by interoperability projects occurring in the United States (and around the world).",
-            "title": "Interoperability Proving Ground",
-            "programCode": [
-                "009:110"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -119699,87 +119681,83 @@
                     "title": "Interoperability_Proving_Ground.csv"
                 }
             ],
-            "describedBy": "https://www.healthit.gov/techlab/ipg/"
+            "identifier": "obq8zsu3-97j2-kg6f-m27a-jblq9u0jqg4s",
+            "issued": "2023-10-03",
+            "keyword": [
+                "data standards",
+                "health care",
+                "health it",
+                "interoperability"
+            ],
+            "landingPage": "https://www.healthit.gov/techlab/ipg/",
+            "modified": "2023-10-03",
+            "programCode": [
+                "009:110"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the National Coordinator for Health Information Technology"
+            },
+            "title": "Interoperability Proving Ground"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qw6v-hk93",
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
-            "identifier": "7973548e-1362-5969-8ee7-8e9ea0cda0fe",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt filters v2.10.22 (coreset-impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/filters.csv",
-                    "description": "CoreSEt filters v2.10.22 (coreset-impl)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt filters v2.10.22 (coreset-impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt filters v2.10.22 (coreset-impl)"
                 }
             ],
+            "identifier": "7973548e-1362-5969-8ee7-8e9ea0cda0fe",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/qw6v-hk93",
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
+            "title": "CoreSEt filters v2.10.22 (coreset-impl)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/r7hc-32zu",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
-            "keyword": [
-                "2015",
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
-            "identifier": "https://data.cdc.gov/api/views/r7hc-32zu",
             "description": "NNDSS - Table II. West Nile virus disease - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Updated weekly from reports to the Division of Vector-Borne Diseases, National Center for Emerging and Zoonotic Infectious Diseases (ArboNET Surveillance). Data for California serogroup, Chikungunya virus, eastern equine, Powassan, St. Louis, and western equine diseases are available in Table I. \ufffd\ufffd Not reportable in all states. Data from states where the condition is not reportable are excluded from this table, except starting in 2007 for the domestic arboviral diseases, influenza-associated pediatric mortality, and in 2003 for SARS-CoV. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.",
-            "title": "NNDSS - Table II. West Nile virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -119802,135 +119780,139 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/r7hc-32zu",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "west nile virus",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/r7hc-32zu",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-01-07",
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
-            "landingPage": "https://healthdata.gov/d/qw9z-s3b4",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-08-27",
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
-            "identifier": "c9de5ddc-5651-5e76-83e1-e132e0826839",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_briefType",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/briefType.csv",
-                    "description": "{\"dataset\": \"briefType\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"briefType\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/briefType.csv",
+                    "mediaType": "text/csv",
                     "title": "briefType csv file"
                 }
             ],
+            "identifier": "c9de5ddc-5651-5e76-83e1-e132e0826839",
+            "issued": "2024-08-27",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/qw9z-s3b4",
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
+            "title": "prodAuto_briefType"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qwzd-jxqv",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-05",
-            "keyword": [
-                "chip",
-                "covid-19",
-                "dq atlas",
-                "medicaid",
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
-            "identifier": "ed35fa7f-279b-4d68-b624-b6ff32e956df",
             "description": "This data set includes monthly counts and percentages of Medicaid and CHIP beneficiaries, by state, who received at least one service for each of the following conditions: acute bronchitis, acute respiratory distress, bronchitis not other specified (NOS), COVID-19 (based on the presence of diagnosis code U07.1), influenza, lower or acute respiratory infection, pneumonia, respiratory infection NOS, and suspected COVID-19 (based on the presence of diagnosis code B97.29).\r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating COVID-related conditions measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Respiratory Conditions in the Medicaid and CHIP Population",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/Respiratory-Conditions-in-the-MedicaidCHIP-Population.csv",
-                    "description": "This data set includes monthly counts and percentages of Medicaid and CHIP beneficiaries, by state, who received at least one service for each of the following conditions: acute bronchitis, acute respiratory distress, bronchitis not other specified (NOS), COVID-19 (based on the presence of diagnosis code U07.1), influenza, lower or acute respiratory infection, pneumonia, respiratory infection NOS, and suspected COVID-19 (based on the presence of diagnosis code B97.29).\n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating COVID-related conditions measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly counts and percentages of Medicaid and CHIP beneficiaries, by state, who received at least one service for each of the following conditions: acute bronchitis, acute respiratory distress, bronchitis not other specified (NOS), COVID-19 (based on the presence of diagnosis code U07.1), influenza, lower or acute respiratory infection, pneumonia, respiratory infection NOS, and suspected COVID-19 (based on the presence of diagnosis code B97.29).\n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating COVID-related conditions measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/Respiratory-Conditions-in-the-MedicaidCHIP-Population.csv",
+                    "mediaType": "text/csv",
                     "title": "Respiratory Conditions in the Medicaid and CHIP Population"
                 }
             ],
+            "identifier": "ed35fa7f-279b-4d68-b624-b6ff32e956df",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "covid-19",
+                "dq atlas",
+                "medicaid",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/qwzd-jxqv",
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
                 "Uncategorized"
-            ]
+            ],
+            "title": "Respiratory Conditions in the Medicaid and CHIP Population"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nors/",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-07-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-30",
-            "keyword": [
-                "foodborne",
-                "gastroenteritis",
-                "outbreak",
-                "waterborne"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NORS Team",
                 "hasEmail": "mailto:NORSDashboard@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5xkq-dg7x",
             "description": "The National Outbreak Reporting System (NORS) is a web-based platform designed to support reporting to CDC by local, state, and territorial health departments in the United States of all waterborne disease outbreaks and enteric disease outbreaks transmitted by food, contact with environmental sources, infected persons or animals, or unknown modes of transmission.",
-            "title": "NORS",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -119953,41 +119935,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5xkq-dg7x",
+            "issued": "2024-07-29",
+            "keyword": [
+                "foodborne",
+                "gastroenteritis",
+                "outbreak",
+                "waterborne"
+            ],
+            "landingPage": "https://www.cdc.gov/nors/",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "modified": "2024-12-30",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Foodborne",
                 "Waterborne",
                 "and Related Diseases"
-            ]
+            ],
+            "title": "NORS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xml",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "1900-01-01",
-            "keyword": [
-                "recalls"
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
-            "identifier": "cbb45912-ca03-4398-8d6d-607e335a8ed9",
             "description": "This list includes products subject to recall since September 2010 related to infant formula distributed by Abbott. This list will be updated with publicly available information as received. The information is current as of the date indicated. If we learn that any information is not accurate, we will revise the list as soon as possible. When available, this database also includes photos of recalled products that have been voluntarily submitted by recalling firms to the FDA to assist the public in identifying those products that are subject to recall.",
-            "title": "Abbott Infant Formula Recall",
-            "programCode": [
-                "009:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -119995,45 +119980,36 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "cbb45912-ca03-4398-8d6d-607e335a8ed9",
+            "issued": "2021-02-25",
+            "keyword": [
+                "recalls"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xml",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "irregular"
+            "modified": "1900-01-01",
+            "programCode": [
+                "009:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Abbott Infant Formula Recall"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/nhcs.htm",
+            "accrualPeriodicity": "R/P2M",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-12-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-03-18/2023-12-26",
-            "modified": "2024-07-29",
-            "keyword": [
-                "covid-19",
-                "emergency department",
-                "hospital encounters",
-                "inpatient",
-                "intubation",
-                "mortality",
-                "respiratory illness",
-                "screenings",
-                "ventilator use"
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
-            "identifier": "https://data.cdc.gov/api/views/q3t8-zr7t",
             "description": "The National Hospital Care Survey (NHCS) collects data on patient care in hospital-based settings to describe patterns of health care delivery and utilization in the United States. Settings currently include inpatient and emergency departments (ED). Additionally, the NHCS contributes data that may inform public health emergencies as the survey is designed to capture emerging diseases and viruses that require hospitalizations, including COVID-19 encounters. The 2020 - 2023 NHCS are not yet fully operational so it is important to note that these data are not nationally representative.\n\nThe data are from 26 hospitals submitting inpatient and 26 hospitals submitting ED Uniform Bill (UB)-04 administrative claims from March 18, 2020-December 26, 2023.  Even though the data are not nationally representative, they can provide insight on the impact of COVID-19 on various types of hospitals throughout the country. This information is not available in other hospital reporting systems. The NHCS data from these hospitals can show results by a combination of indicators related to COVID-19, such as length of inpatient stay, in-hospital mortality, comorbidities, and intubation or ventilator use. NHCS data allow for reporting on patient conditions and treatments within the hospital over time.",
-            "title": "COVID-19 Hospital Data from the National Hospital Care Survey",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -120056,46 +120032,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/q3t8-zr7t",
+            "issued": "2020-12-15",
+            "keyword": [
+                "covid-19",
+                "emergency department",
+                "hospital encounters",
+                "inpatient",
+                "intubation",
+                "mortality",
+                "respiratory illness",
+                "screenings",
+                "ventilator use"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/nhcs.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P2M",
+            "modified": "2024-07-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2020-03-18/2023-12-26",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "COVID-19 Hospital Data from the National Hospital Care Survey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://mor.nlm.nih.gov/RxMix/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "drugs",
-                "supplements",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jqkg-525p",
             "description": "An interface for building applications that allows users to combine functions of various NLM drug APIs, including the RxNorm, RxClass, RxTerms, and NDF-RT APIs. Sequences of functions can be executed interactively or in batch mode.",
-            "title": "RxMix",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -120104,45 +120085,41 @@
                     "title": "Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jqkg-525p",
+            "issued": "2021-06-30",
+            "keyword": [
+                "api",
+                "drugs",
+                "supplements",
+                "tools & utilities"
+            ],
+            "landingPage": "https://mor.nlm.nih.gov/RxMix/",
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
+            "title": "RxMix"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hyak-nxqs",
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
-                "tetanus",
-                "toxic shock syndrome (other than streptococcal)",
-                "trichinellosis",
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
-            "identifier": "https://data.cdc.gov/api/views/hyak-nxqs",
             "description": "NNDSS - TABLE 1II. Tetanus to Trichinellosis \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -120165,46 +120142,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hyak-nxqs",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "tetanus",
+                "toxic shock syndrome (other than streptococcal)",
+                "trichinellosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hyak-nxqs",
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
+            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7jik-jwvu",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/7jik-jwvu",
             "description": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -120227,94 +120203,94 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7jik-jwvu",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "dengue",
+                "dengue-like illness",
+                "dengue virus infections",
+                "nedss",
+                "netss",
+                "nndss",
+                "severe dengue",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7jik-jwvu",
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
+            "title": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/qzza-zykr",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-04-27",
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
-            "identifier": "095672d6-0a1f-520c-a59a-a87227801cf4",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_footnotes",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/footnotes.csv",
-                    "description": "{\"dataset\": \"footnotes\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"footnotes\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/footnotes.csv",
+                    "mediaType": "text/csv",
                     "title": "footnotes csv file"
                 }
             ],
+            "identifier": "095672d6-0a1f-520c-a59a-a87227801cf4",
+            "issued": "2023-04-27",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/qzza-zykr",
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
+            "title": "devAuto_footnotes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4bft-6yws",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-17",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "botulism",
-                "foodborne",
-                "infant",
-                "nedss",
-                "netss",
-                "nndss",
-                "other (wound & unspecified)",
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
-            "identifier": "https://data.cdc.gov/api/views/4bft-6yws",
             "description": "NNDSS - Table 1E. Botulism, Foodborne to Botulism, Other (wound & unspecified) - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1E. Botulism, Foodborne to Botulism, Other (wound & unspecified)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -120337,46 +120313,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4bft-6yws",
+            "issued": "2020-01-17",
+            "keyword": [
+                "2020",
+                "botulism",
+                "foodborne",
+                "infant",
+                "nedss",
+                "netss",
+                "nndss",
+                "other (wound & unspecified)",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/4bft-6yws",
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
+            "title": "NNDSS - Table 1E. Botulism, Foodborne to Botulism, Other (wound & unspecified)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nnhs/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
-            "issued": "2007-04-13",
-            "@type": "dcat:Dataset",
-            "temporal": "2004-08-01/2004-12-31",
-            "modified": "2024-03-25",
-            "keyword": [
-                "icd-9-cm",
-                "long-term care",
-                "medications",
-                "national nursing home survey",
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
-            "identifier": "https://data.cdc.gov/api/views/tks5-umwc",
-            "description": "The 2004 National Nursing Home Survey (NNHS), conducted between August and December of 2004, was reintroduced into the field after a five-year break, during which time the survey was redesigned and expanded to collect many new data items. All nursing homes that participated in the NNHS had at least three beds and were either certified (by Medicare or Medicaid) or had a state license to operate as a nursing home. The redesigned survey was administered using a computer-assisted personal interviewing (CAPI) system. The National Nursing Home Survey provides information on nursing homes from two perspectives-that of the provider of services and that of the recipient of care. Data about the facilities include characteristics such as size, ownership, Medicare/Medicaid certification, services provided and specialty programs offered, and charges. For recipients, data were obtained on demographic characteristics, health status and medications taken, services received, and sources of payment.\n\nData for the survey were obtained through personal interviews with facility administrators and designated staff who used administrative records to answer questions about the facilities, staff, services and programs, and medical records to answer questions about the residents.\n\nThe total number of nursing home facilities that participated in NNHS is 1,174.",
-            "title": "2004 National Nursing Home Survey - Restricted Resident Medications Dataset",
-            "isPartOf": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NNHS/nnhs04/SAS_Data/",
+            "describedBy": "https://www.cdc.gov/nchs/data/nnhsd/2004NNHS_DesignCollectionEstimates_072706tags.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The 2004 National Nursing Home Survey (NNHS), conducted between August and December of 2004, was reintroduced into the field after a five-year break, during which time the survey was redesigned and expanded to collect many new data items. All nursing homes that participated in the NNHS had at least three beds and were either certified (by Medicare or Medicaid) or had a state license to operate as a nursing home. The redesigned survey was administered using a computer-assisted personal interviewing (CAPI) system. The National Nursing Home Survey provides information on nursing homes from two perspectives-that of the provider of services and that of the recipient of care. Data about the facilities include characteristics such as size, ownership, Medicare/Medicaid certification, services provided and specialty programs offered, and charges. For recipients, data were obtained on demographic characteristics, health status and medications taken, services received, and sources of payment.\n\nData for the survey were obtained through personal interviews with facility administrators and designated staff who used administrative records to answer questions about the facilities, staff, services and programs, and medical records to answer questions about the residents.\n\nThe total number of nursing home facilities that participated in NNHS is 1,174.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -120385,51 +120363,50 @@
                     "title": "2004 National Nursing Home Survey - Restricted Resident Medications Dataset"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data/nnhsd/2004NNHS_DesignCollectionEstimates_072706tags.pdf",
+            "identifier": "https://data.cdc.gov/api/views/tks5-umwc",
+            "isPartOf": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NNHS/nnhs04/SAS_Data/",
+            "issued": "2007-04-13",
+            "keyword": [
+                "icd-9-cm",
+                "long-term care",
+                "medications",
+                "national nursing home survey",
+                "research-data-center"
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
+            "title": "2004 National Nursing Home Survey - Restricted Resident Medications Dataset"
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
@@ -120452,42 +120429,46 @@
                     "mediaType": "application/xml"
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
-            "landingPage": "https://data.cdc.gov/d/x7zy-2xmx",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2016-11-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
-            "keyword": [
-                "500 cities",
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
@@ -120495,40 +120476,41 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/x7zy-2xmx",
+            "issued": "2016-11-08",
+            "keyword": [
+                "500 cities",
+                "boundaries",
+                "census tract",
+                "shapefile"
+            ],
+            "landingPage": "https://data.cdc.gov/d/x7zy-2xmx",
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
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "500 Cities: Census Tract Boundaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/g3k9-gyw7",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-04-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-04-10",
-            "keyword": [
-                "artesunate",
-                "division of parasitic diseases and malaria",
-                "malaria"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Francisca Abanyie, MD, MPH",
                 "hasEmail": "mailto:why6@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/g3k9-gyw7",
             "description": "This dataset includes deidentified data on patients receiving artesunate through the National Artesunate for Severe Malaria Program from April- December 2019. \n\nThis dataset contains the data from the case report form only.\nPlease see the links below for the other datasets and the attached document 'Guide to NASMP Datasets':\nData from Case Report Form- https://data.cdc.gov/Global-Health/National-Artesunate-for-Severe-Malaria-Program-Cas/igaz-icki\nData on Artesunate Dosing- https://data.cdc.gov/dataset/National-Artesunate-for-Severe-Malaria-Program-Art/qan4-gt4k\nData on Microscopy (Parasitemia values)- https://data.cdc.gov/Global-Health/National-Artesunate-for-Severe-Malaria-Program-Mic/v2k9-ctv4\n\nAll data can be easily linked using the ParticipantID field, a unique ID number assigned to each participant.",
-            "title": "National Artesunate for Severe Malaria Program Follow-On Antimalarial Dosing Data- April to December 2019",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -120551,52 +120533,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/g3k9-gyw7",
+            "issued": "2020-04-10",
+            "keyword": [
+                "artesunate",
+                "division of parasitic diseases and malaria",
+                "malaria"
+            ],
+            "landingPage": "https://data.cdc.gov/d/g3k9-gyw7",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2020-04-10",
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
+            "title": "National Artesunate for Severe Malaria Program Follow-On Antimalarial Dosing Data- April to December 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/3pbe-qh9z",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-07-25",
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
-            "identifier": "https://data.cdc.gov/api/views/3pbe-qh9z",
             "description": "This site provides historical data beginning June 22, 2022, for the visualization presented on <a href=\"https://covid.cdc.gov/covid-data-tracker/#vaccinations\" target=\"_blank\">COVID-19 Data Tracker\u2019s \u201cVaccinations in the United States\u201d</a> site titled \u201cPrimary Series Completion, Booster Dose Eligibility, and Booster Dose Receipt by Age, United States\u201d.\n\n<b >Fully Vaccinated / Completed Primary Series:</b> <ul><li> For surveillance purposes, COVID Data Tracker counts people as being \"fully vaccinated\" or as having \"completed a primary series\" if they received two doses on different days (regardless of time interval) of the two-dose mRNA series or received one dose of a single-dose vaccine. When the vaccine manufacturer is not reported, the recipient is considered fully vaccinated with two doses.</li></ul><b>First Booster Dose:\u202f </b><ul><li>For surveillance purposes, the count and percentage of people who received a first booster dose includes anyone who is fully vaccinated and has received another dose of COVID-19 vaccine since August 13, 2021. This includes people who received a first booster dose and people who received an additional primary series dose as this metric does not distinguish if the recipient is <b><a href='https://www.cdc.gov/coronavirus/2019-ncov/vaccines/recommendations/immuno.html' target=\"_blank\">\u202fimmunocompromised and received an additional dose</a></b>.</li><li><b>   First booster dose eligibility: </b><ul><li>CDC counts people as being <b>\"\u202f<a href=\"https://www.cdc.gov/coronavirus/2019-ncov/vaccines/booster-shot.html\" target=\"_blank\">eligible for a first booster dose</a>\"</b> if it has been at least 5 months since completion of a Pfizer-BioNTech or Moderna primary series or at least 2 months since receipt of a Janssen (Johnson & Johnson) singe-dose vaccine. </li></ul></li></ul>\n<b>Second Booster Dose:</b><ul><li>For surveillance purposes, the count and percentage of people who received a second booster dose includes anyone who is fully vaccinated and has received two subsequent doses of COVID-19 vaccine since August 13, 2021. This includes people who received two booster doses and people who received one additional dose and one booster dose.\u202f </li><li>The count of people who received a second booster dose and the percentage of people with a first booster who received a second booster dose does not account for whether a person is <b><a href='https://www.cdc.gov/coronavirus/2019-ncov/vaccines/recommendations/immuno.html'  target=\"_blank\">immunocompromised or time interval since first booster dose</a></b>. </li><li><b>Second booster dose eligibility: </b><ul><li>CDC counts people as being\u202f <b>\"<a href=\"https://www.cdc.gov/coronavirus/2019-ncov/vaccines/booster-shot.html\" target=\"_blank\"><b>eligible for a second booster dose</b></a>\"\u202f</b> if it has been at least 4 months since receiving a first booster dose. </ul></li></li><li><b>Limitations to counting people with a second booster dose: </b>\n<ul><li>Due to the aggregate vaccination record reporting method used by Idaho for its residents under the age of 18 years and by Texas for all its residents, CDC counts all 4th doses received by these populations as a second booster dose. This includes immunocompromised individuals who received a three-dose primary series and only one booster dose. This limitation may lead to an undercount of people who received the single-dose J&J/Janssen vaccine as their primary series and two booster doses.</li></ul>\n</li></ul>Data represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.",
-            "title": "COVID-19 Primary Series Completion, Booster Dose Eligibility, and Booster Dose Receipt by Age, United States\u00a0",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -120619,66 +120590,82 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/3pbe-qh9z",
+            "issued": "2022-07-25",
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
+            "landingPage": "https://data.cdc.gov/d/3pbe-qh9z",
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
+            "title": "COVID-19 Primary Series Completion, Booster Dose Eligibility, and Booster Dose Receipt by Age, United States\u00a0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:10"
             ],
-            "landingPage": "https://healthdata.gov/d/r4a9-ub25",
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2014-12-01",
-            "keyword": [
-                "information center; foods help desk"
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
-            "identifier": "A6EEDE4E-01A2-4167-A196-87066F135C34",
             "description": "This system supports the Information Center's Help Desk capabilities, and reports can be exported.",
-            "title": "CFSAN Knowledge Management System",
+            "identifier": "A6EEDE4E-01A2-4167-A196-87066F135C34",
+            "issued": "2021-02-25",
+            "keyword": [
+                "information center; foods help desk"
+            ],
+            "landingPage": "https://healthdata.gov/d/r4a9-ub25",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2014-12-01",
             "programCode": [
                 "009:001"
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "CFSAN Knowledge Management System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9kpc-xntn",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chemical and Biochemical Monitoring Branch (CBMB), Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9kpc-xntn",
             "description": "The goal of the experimental design and research presented herein was to produce peracetic acid (PAA) atmospheres suitable for evaluating PAA sampling methods in a controlled environment. To achieve this, generated test atmospheres must: enable simultaneous exposure of multiple samplers to equivalent atmospheres; maintain a continuous stable atmosphere for a duration to exceed experimental time frames; and produce a range of analyte concentrations, air velocities, temperatures and humidities. The American Conference of Governmental Industrial Hygienists (AGCIH) Threshold Limit Value (TLV) for PAA is 0.4 ppm. The goal was to generate PAA atmospheres with concentrations from one tenth of the TLV up to 100 times the TLV.\n\nPAA is a reactive chemical, which presents some inherent challenges to generation of standard reference materials and atmospheres. PAA is a strong oxidant. PAA solutions are labile, thus it is difficult to keep reference standards or atmospheres. In solution, PAA and water are in equilibrium with acetic acid (AA) and hydrogen peroxide (HP). The equilibrium shifts as solutions of PAA evolve oxygen gas through the degradation of HP. Dynamic PAA atmospheres which are flowing and continuously refreshed are the preferred method for exposing samplers to equivalent atmospheres. Generation of static atmospheres by evaporating PAA solution into a closed container cannot be maintained for very long before needing to be refreshed. Dynamically generated atmospheres are created by a continuously renewed flow of air as a carrier and a source of PAA vapors, which are necessary for evaluating sensor performance over time frames relevant to occupational safety.\n\nGeneration of PAA vapors can be accomplished from assisted vaporization, including applying heat and/or aerosolization with a nebulizer to accelerate evaporation. Glass reacts with PAA to hydroxylate the silica. used a glass syringe to deliver PAA solution to a nebulizer; however, gas bubbles formed in the syringe leading to uncontrollable ejection of the PAA solution from the syringe. To mitigate this, used acid washed syringes. They generated atmospheres of up to 2 ppm with a reported 95% recovery of theoretical delivered PAA. Dilute solutions of PAA can help to mitigate gas evolution but require more energy to evaporate and introduce additional humidity.\n\nFor these experiments, PAA vapors were swept directly from the headspace above a PAA solution into our generation system. The flow rate of the air sweeping the headspace was varied to achieve the desired concentration after dilution into the carrier gas stream. When evaporating diluted PAA solutions using a nebulizer, the minimum humidity range is limited due to the water content in the dilute PAA solution. Thus, a wider humidity range on the low end is available when sweeping the headspace. The ability to maintain the concentration of PAA in the headspace above the solution is limited by the kinetics at the PAA solution-air interface. A practical solution was achieved using a PAA delivery system where air was passed through the headspace above a PAA solution in a vial. An impinger with a N,N-diethyl-p-phenylenediamine (DPD) analysis was used as the reference measurement for the PAA concentrations in the generated atmospheres.",
-            "title": "Controlled Generation of Peracetic Acid Atmospheres for the Evaluation of Chemical Samplers",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -120686,44 +120673,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9kpc-xntn",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/9kpc-xntn",
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
+            "title": "Controlled Generation of Peracetic Acid Atmospheres for the Evaluation of Chemical Samplers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/p8ia-4jqj",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
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
-            "identifier": "https://data.cdc.gov/api/views/p8ia-4jqj",
             "description": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1I. Cryptosporidiosis to Cyclosporiasis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -120746,47 +120724,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/p8ia-4jqj",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "cryptosporidiosis",
+                "cyclosporiasis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/p8ia-4jqj",
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
+            "title": "NNDSS - TABLE 1I. Cryptosporidiosis to Cyclosporiasis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/nhcs-hud.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-06-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2013/2017",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data/datalinkage/NHCS-Linked-HUD-Program-Participation-Any.pdf"
-            ],
-            "keyword": [
-                "linked hud data",
-                "nhcs",
-                "research-data-center"
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
-            "identifier": "https://data.cdc.gov/api/views/qfu5-aeqe",
-            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the 2014 and 2016\u00a0National Hospital Care Surveys (NHCS)\u00a0by linking patient records with up to three years of administrative housing data from the U.S. Department of Housing and Urban Development\u2019s (HUD) largest housing assistance programs: the Housing Choice Voucher (HCV) program, Public Housing (PH) , and privately owned, subsidized Multifamily housing (MF). These innovative linked data will support a wide array of patient outcomes studies, including the opportunity to study complex relationships between housing and health.",
-            "title": "National Hospital Care Survey (NHCS) linked to Department of Housing and Urban Development (HUD) Administrative Housing Data",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 11) here: https://www.cdc.gov/nchs/data/datalinkage/NHCS-HUD-Linkage-Methods-and-Analytic-Considerations.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the 2014 and 2016\u00a0National Hospital Care Surveys (NHCS)\u00a0by linking patient records with up to three years of administrative housing data from the U.S. Department of Housing and Urban Development\u2019s (HUD) largest housing assistance programs: the Housing Choice Voucher (HCV) program, Public Housing (PH) , and privately owned, subsidized Multifamily housing (MF). These innovative linked data will support a wide array of patient outcomes studies, including the opportunity to study complex relationships between housing and health.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -120794,40 +120771,48 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 11) here: https://www.cdc.gov/nchs/data/datalinkage/NHCS-HUD-Linkage-Methods-and-Analytic-Considerations.pdf",
+            "identifier": "https://data.cdc.gov/api/views/qfu5-aeqe",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-06-23",
+            "keyword": [
+                "linked hud data",
+                "nhcs",
+                "research-data-center"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/nhcs-hud.htm",
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
+                "https://www.cdc.gov/nchs/data/datalinkage/NHCS-Linked-HUD-Program-Participation-Any.pdf"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "United States",
+            "temporal": "2013/2017",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Hospital Care Survey (NHCS) linked to Department of Housing and Urban Development (HUD) Administrative Housing Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/DataSets/Recalls/Food/Food.xml",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "recalls"
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
-            "identifier": "cdaa413b-325f-4f81-a78e-f8e55ac77098",
             "description": "Press Releases of food recalls from industry",
-            "title": "Food Recalls",
-            "programCode": [
-                "009:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -120835,51 +120820,77 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "cdaa413b-325f-4f81-a78e-f8e55ac77098",
+            "issued": "2021-02-25",
+            "keyword": [
+                "recalls"
+            ],
+            "landingPage": "http://www.fda.gov/DataSets/Recalls/Food/Food.xml",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S"
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Food Recalls"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.neuromorpho.org/",
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
                 "fn": "GNADT, JAMES W\u00a0",
                 "hasEmail": "mailto:gnadtjw@ninds.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "95a4d2ef-29d6-4c6d-9a32-339fe4d9771f",
+            "dataQuality": true,
             "description": "<p>NeuroMorpho.Org is a centrally curated inventory of digitally reconstructed neurons associated with peer-reviewed publications. It contains contributions from over 80 laboratories worldwide and is continuously updated as new morphological reconstructions are collected, published, and shared.</p>",
-            "title": "NeuroMorpho",
+            "identifier": "95a4d2ef-29d6-4c6d-9a32-339fe4d9771f",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.neuromorpho.org/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
             "programCode": [
                 "009:054"
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
+            "title": "NeuroMorpho"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/r6pz-e6cq",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "description": "This data set includes annual counts and percentages of Medicaid and Children\u2019s Health Insurance Program (CHIP) enrollees by urban or rural residence. Results are shown overall; by state; and by four subpopulation topics: scope of Medicaid and CHIP benefits, race and ethnicity, disability-related eligibility category, and managed care participation.\r\nThese results were generated using Transformed Medicaid Statistical Information System (T-MSIS) Analytic Files (TAF) Release 1 data and the Race/Ethnicity Imputation Companion File. This data set includes Medicaid and CHIP enrollees in all 50 states, the District of Columbia, Puerto Rico, and the U.S. Virgin Islands who were enrolled for at least one day in the calendar year, except where otherwise noted. Enrollees in Guam, American Samoa, and the Northern Mariana Islands are not included. Results shown overall (where subpopulation topic is \"Total enrollees\") and for the race and ethnicity subpopulation topic exclude enrollees in the U.S. Virgin Islands. Results shown for the race and ethnicity, disability category, and managed care participation subpopulation topics only include Medicaid and CHIP enrollees with comprehensive benefits. Results shown for the disability category subpopulation topic only include working-age adults (ages 19 to 64). Results for states with TAF data quality issues in the year have a value of \"Unusable data.\" Some rows in the data set have a value of \"DS,\" which indicates that data were suppressed according to the Centers for Medicare & Medicaid Services\u2019 Cell Suppression Policy for values between 1 and 10.\r\nThis data set is based on the brief: \"Rural Medicaid and CHIP enrollees in 2020.\" Enrollees are assigned to an urban or rural category based on the 2010 Rural-Urban Commuting Area (RUCA) code associated with their home or mailing address ZIP code in TAF. Enrollees are assigned to the comprehensive benefits or limited benefits subpopulation according to the criteria in the \"Identifying Beneficiaries with Full-Scope, Comprehensive, and Limited Benefits in the TAF\" DQ Atlas brief. Enrollees are assigned to a race and ethnicity subpopulation using the state-reported race and ethnicity information in TAF when it is available and of good quality; if it is missing or unreliable, race and ethnicity is indirectly estimated using an enhanced version of Bayesian Improved Surname Geocoding (BISG) (Race and ethnicity of the national Medicaid and CHIP population in 2020). Enrollees are assigned to a disability category subpopulation using their latest reported eligibility group code and age in the year (Medicaid enrollees who qualify for benefits based on disability in 2020). Enrollees are assigned to a managed care participation subpopulation based on the managed care plan type code that applies to the majority of their enrolled-months during the year (Enrollment in CMC Plans). Please refer to the full brief for additional context about the methodology and detailed findings. Future updates to this data set will include more recent data years as the TAF data become available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/rural-residence-2020-2022-01162025.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "73fdbf7c-569e-427b-9bff-eeed34a51dcb",
             "issued": "2025-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
             "keyword": [
                 "chip",
                 "demographics",
@@ -120889,60 +120900,31 @@
                 "t-msis analytic files",
                 "urban"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Medicaid.gov",
-                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/d/r6pz-e6cq",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Medicare & Medicaid Services"
             },
-            "identifier": "73fdbf7c-569e-427b-9bff-eeed34a51dcb",
-            "description": "This data set includes annual counts and percentages of Medicaid and Children\u2019s Health Insurance Program (CHIP) enrollees by urban or rural residence. Results are shown overall; by state; and by four subpopulation topics: scope of Medicaid and CHIP benefits, race and ethnicity, disability-related eligibility category, and managed care participation.\r\nThese results were generated using Transformed Medicaid Statistical Information System (T-MSIS) Analytic Files (TAF) Release 1 data and the Race/Ethnicity Imputation Companion File. This data set includes Medicaid and CHIP enrollees in all 50 states, the District of Columbia, Puerto Rico, and the U.S. Virgin Islands who were enrolled for at least one day in the calendar year, except where otherwise noted. Enrollees in Guam, American Samoa, and the Northern Mariana Islands are not included. Results shown overall (where subpopulation topic is \"Total enrollees\") and for the race and ethnicity subpopulation topic exclude enrollees in the U.S. Virgin Islands. Results shown for the race and ethnicity, disability category, and managed care participation subpopulation topics only include Medicaid and CHIP enrollees with comprehensive benefits. Results shown for the disability category subpopulation topic only include working-age adults (ages 19 to 64). Results for states with TAF data quality issues in the year have a value of \"Unusable data.\" Some rows in the data set have a value of \"DS,\" which indicates that data were suppressed according to the Centers for Medicare & Medicaid Services\u2019 Cell Suppression Policy for values between 1 and 10.\r\nThis data set is based on the brief: \"Rural Medicaid and CHIP enrollees in 2020.\" Enrollees are assigned to an urban or rural category based on the 2010 Rural-Urban Commuting Area (RUCA) code associated with their home or mailing address ZIP code in TAF. Enrollees are assigned to the comprehensive benefits or limited benefits subpopulation according to the criteria in the \"Identifying Beneficiaries with Full-Scope, Comprehensive, and Limited Benefits in the TAF\" DQ Atlas brief. Enrollees are assigned to a race and ethnicity subpopulation using the state-reported race and ethnicity information in TAF when it is available and of good quality; if it is missing or unreliable, race and ethnicity is indirectly estimated using an enhanced version of Bayesian Improved Surname Geocoding (BISG) (Race and ethnicity of the national Medicaid and CHIP population in 2020). Enrollees are assigned to a disability category subpopulation using their latest reported eligibility group code and age in the year (Medicaid enrollees who qualify for benefits based on disability in 2020). Enrollees are assigned to a managed care participation subpopulation based on the managed care plan type code that applies to the majority of their enrolled-months during the year (Enrollment in CMC Plans). Please refer to the full brief for additional context about the methodology and detailed findings. Future updates to this data set will include more recent data years as the TAF data become available.",
-            "title": "Rural Medicaid and CHIP enrollees",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://download.medicaid.gov/data/rural-residence-2020-2022-01162025.csv",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "title": "Rural Medicaid and CHIP enrollees"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/r6ud-pman",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "benefits and cost sharing",
-                "exchange puf",
-                "marketplace puf",
-                "py2025"
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
-            "identifier": "8060e816-b052-42b3-ad60-9eac699d7c8b",
             "description": "The Benefits and Cost Sharing PUF (BenCS-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The BenCS-PUF contains plan variant-level data on essential health benefits, coverage limits, and cost sharing for each QHP and SADP.",
-            "title": "Benefits and Cost Sharing PUF - PY2025",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -120950,35 +120932,38 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "8060e816-b052-42b3-ad60-9eac699d7c8b",
+            "issued": "2024-12-10",
+            "keyword": [
+                "benefits and cost sharing",
+                "exchange puf",
+                "marketplace puf",
+                "py2025"
+            ],
+            "landingPage": "https://healthdata.gov/d/r6ud-pman",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Benefits and Cost Sharing PUF - PY2025"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/r74b-4d67",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2022-06-13",
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
-            "identifier": "72135da5-f8b4-475b-b602-91621f4205d9",
             "description": "Dataset.",
-            "title": "2019 Managed Care Programs By State",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -120986,45 +120971,35 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "72135da5-f8b4-475b-b602-91621f4205d9",
+            "issued": "2021-10-30",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/r74b-4d67",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2022-06-13",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "2019 Managed Care Programs By State"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -121047,40 +121022,47 @@
                     "mediaType": "application/xml"
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
+            "title": "U.S. State and Territorial Stay-At-Home Orders: March 15, 2020 \u2013 August 15, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/genbank/TPA.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-03-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "computational biology",
-                "dataset",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/eg2g-944h",
             "description": "A database that contains sequences built from the existing primary sequence data in GenBank. The sequences and corresponding annotations are experimentally supported and have been published in a peer-reviewed scientific journal.",
-            "title": "Third Party Annotation (TPA) Database",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -121089,59 +121071,54 @@
                     "title": "About Third Party Annotation (TPA) Database"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genbank/TPA-Exp",
-                    "description": "Annotation of sequence data is supported by peer-reviewed wet-lab experimental evidence.",
                     "@type": "dcat:Distribution",
+                    "description": "Annotation of sequence data is supported by peer-reviewed wet-lab experimental evidence.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genbank/TPA-Exp",
+                    "mediaType": "text/html",
                     "title": "Third Party Annotation (TPA) Database: Experimental"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genbank/TPA-Inf",
-                    "description": "Annotation of sequence data by inference (where the source molecule or its product(s) have not been the subject of direct experimentation)",
                     "@type": "dcat:Distribution",
+                    "description": "Annotation of sequence data by inference (where the source molecule or its product(s) have not been the subject of direct experimentation)",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genbank/TPA-Inf",
+                    "mediaType": "text/html",
                     "title": "Third Party Annotation (TPA) Database: Inferential"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/eg2g-944h",
+            "issued": "2022-03-02",
+            "keyword": [
+                "computational biology",
+                "dataset",
+                "genomics"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/genbank/TPA.html",
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
+            "title": "Third Party Annotation (TPA) Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/n5qs-vw3x",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "coronavirus",
-                "covid",
-                "covid-19",
-                "covid cases",
-                "covid deaths",
-                "dialysis",
-                "hemodialysis",
-                "sars-cov-2"
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
-            "identifier": "https://data.cdc.gov/api/views/n5qs-vw3x",
             "description": "Mandated reporting of Weekly Aggregate Case and Death Count data among dialysis patients and dialysis facility staff (healthcare personnel or HCP) in the United States was discontinued May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. This dataset will contain weekly aggregate data from January 1, 2021, through May 10, 2023, and will remain publicly available.\n\nThis archived public use dataset contains reported COVID-19 case and death data per week for all states and territories, along with weekly totals for the entire United States, throughout the given timeframe.",
-            "title": "Weekly United States COVID-19 Cases and Deaths among Dialysis Patients - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -121164,42 +121141,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/n5qs-vw3x",
+            "issued": "2023-10-03",
+            "keyword": [
+                "coronavirus",
+                "covid",
+                "covid-19",
+                "covid cases",
+                "covid deaths",
+                "dialysis",
+                "hemodialysis",
+                "sars-cov-2"
+            ],
+            "landingPage": "https://data.cdc.gov/d/n5qs-vw3x",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
             "theme": [
                 "Case Surveillance"
-            ]
+            ],
+            "title": "Weekly United States COVID-19 Cases and Deaths among Dialysis Patients - ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nlm.nih.gov/research/umls/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-30",
-            "keyword": [
-                "api",
-                "dataset",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/9t6e-u9qh",
             "description": "The UMLS integrates and distributes key terminology, classification and coding standards, and associated resources to promote creation of more effective and interoperable biomedical information systems and services, including electronic health records.",
-            "title": "Unified Medical Language System (UMLS)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -121208,10 +121189,10 @@
                     "title": "Download UMLS Data - Knowledge Sources"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://documentation.uts.nlm.nih.gov/",
-                    "description": "The UTS API is intended for application developers to perform Web service calls and retrieve UMLS data within their own applications. The UTS API provides the ability to search, retrieve, and filter terms, concepts, attributes, relations, metadata and more from over 160 vocabularies of the UMLS Metathesaurus, as well as the Semantic Network. Paging, sorting and filtering (PSF) capabilities allows users to customize results of Web service calls in many ways: choose to include or exclude specific criteria, sort results by fields, or specify results displayed per page. The documentation provides a suite of Web Services Description Language (WSDL) files, API installation instructions, and sample code.",
                     "@type": "dcat:Distribution",
+                    "description": "The UTS API is intended for application developers to perform Web service calls and retrieve UMLS data within their own applications. The UTS API provides the ability to search, retrieve, and filter terms, concepts, attributes, relations, metadata and more from over 160 vocabularies of the UMLS Metathesaurus, as well as the Semantic Network. Paging, sorting and filtering (PSF) capabilities allows users to customize results of Web service calls in many ways: choose to include or exclude specific criteria, sort results by fields, or specify results displayed per page. The documentation provides a suite of Web Services Description Language (WSDL) files, API installation instructions, and sample code.",
+                    "downloadURL": "https://documentation.uts.nlm.nih.gov/",
+                    "mediaType": "text/html",
                     "title": "API"
                 },
                 {
@@ -121227,45 +121208,41 @@
                     "title": "Download UMLS Data - Vocabulary Standards and Mappings"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/9t6e-u9qh",
+            "issued": "2016-08-04",
+            "keyword": [
+                "api",
+                "dataset",
+                "health data standards",
+                "terminologies"
+            ],
+            "landingPage": "https://www.nlm.nih.gov/research/umls/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-09-30",
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
+            "title": "Unified Medical Language System (UMLS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rcdh-n3ej",
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
-            "identifier": "https://data.cdc.gov/api/views/rcdh-n3ej",
             "description": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection) \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -121288,35 +121265,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rcdh-n3ej",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "salmonella paratyphi infection",
+                "salmonella typhi infection",
+                "salmonellosis (excluding salmonella typhi infection and salmonella paratyphi infection)",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rcdh-n3ej",
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
+            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/vagq-bwyc",
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
-            "identifier": "https://data.cdc.gov/api/views/vagq-bwyc",
             "description": "Loading-induced hypertrophy with transcriptional upregulation has been observed concomitant with nuclei accretion in various studies regarding both humans and rodents.   Bruusgaard et al. in 2010 pioneered work utilizing a model of synergist ablation to cause hypertrophy followed by denervation-induced atrophy to demonstrate that load-induced gains in myonuclei could be long-lasting after the termination of such exposure.  This finding was consistent with the idea of enduring myonuclear accretion as a form of \u201cmuscle memory\u201d allowing enhanced muscle adaptation following a period of detraining.  Subsequent research groups further investigated this possibility in the context of exercise utilizing rodents and various loaded exercise paradigms such as weighted wheel running and ladder climbing.  This research yielded a spectrum of results.  While these studies were instrumental in highlighting the variation in outcomes possible following load-induced hypertrophy in general, they were limited in their direct relatedness to resistance training \u2013 the predominate form of exposure utilized to induce hypertrophy.  Our research group has established and repeatedly validated a rat research model to investigate resistance-type training.   The model is based on using a dynamometer to precisely expose dorsiflexor muscles of rats to 8 sets of 10 repetitions (per set) of stretch-shortening contractions (SSCs) \u2013 a consecutive sequence of isometric, lengthening, and shortening contractions.  Training with this exposure 3 sessions per week for one month results in increases in muscle mass and performance.  This is accompanied by an increase in muscle fiber area accompanied by a proportional increase in myonuclei number and a rise in overall transcriptional output as measured by total RNA levels.  The purpose of the present study was to determine to what extent alterations in performance, muscle mass, nuclei number, and transcriptional output persist several months following the termination of this relevant and valid model of resistance-type training.",
-            "title": "Elevated muscle mass accompanied by transcriptional and nuclear alterations several months following cessation of resistance-type training in rats",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -121324,49 +121311,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vagq-bwyc",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/vagq-bwyc",
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
+            "title": "Elevated muscle mass accompanied by transcriptional and nuclear alterations several months following cessation of resistance-type training in rats"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-05-12",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-01-04/2021-07-03",
-            "modified": "2023-11-16",
-            "keyword": [
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "hospital referral region",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
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
-            "identifier": "https://data.cdc.gov/api/views/mqmc-4b9n",
             "description": "Provisional count of deaths involving coronavirus disease 2019 (COVID-19) in the United States by week of death and by hospital referral region (HRR). HRR is determined by county of occurrence. Weekly weighted counts of deaths from all causes and due to COVID-19 are provided by HRR overall and for decedents 65 years and older. The weighted counts by HRRs are based on published methods for aggregating county-level data to HRRs. More detail about aggregating to HRRs from counties can be found in the following: https://github.com/Dartmouth-DAC/covid-19-hrr-mapping\nhttps://dartmouthatlas.org/covid-19/hrr-mapping/",
-            "title": "AH Provisional COVID-19 Deaths by Hospital Referral Region",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -121389,22 +121363,75 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/mqmc-4b9n",
+            "issued": "2021-05-12",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hospital referral region",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-11-16",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2015-01-04/2021-07-03",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by Hospital Referral Region"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nThis visualization provides weekly data on the number of deaths by jurisdiction of occurrence and cause of death. Counts of deaths in more recent weeks can be compared with counts from earlier years to determine if the number is higher than expected. Selected causes of death are shown, based on analyses of the most prevalent comorbid conditions reported on death certificates where COVID-19 was listed as a cause of death (see https://www.cdc.gov/nchs/nvss/vsrr/covid_weekly/index.htm#Comorbidities). Cause of death counts are based on the underlying cause of death, and presented for Respiratory diseases, Circulatory diseases, Malignant neoplasms, and Alzheimer disease and dementia. Estimated numbers of deaths due to these other causes of death could represent misclassified COVID-19 deaths, or potentially could be indirectly related to COVID-19 (e.g., deaths from other causes occurring in the context of health care shortages or overburdened health care systems). Deaths with an underlying cause of death of COVID-19 are not included in these estimates of deaths due to other causes. Deaths due to external causes (i.e. injuries) or unknown causes are excluded. For more detail, see the Technical Notes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u6jv-9ijr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u6jv-9ijr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u6jv-9ijr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u6jv-9ijr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/u6jv-9ijr",
             "issued": "2020-05-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-27",
             "keyword": [
                 "alzheimer disease",
                 "cancer",
@@ -121432,90 +121459,34 @@
                 "united states",
                 "weekly"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
```

