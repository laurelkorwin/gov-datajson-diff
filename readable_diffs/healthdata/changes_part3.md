# Change History for healthdata.json (Part 3)

### Changes from 31606f9 to dd2190f (Part 2/11)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
             "description": "Thermal spray coating is a process in which molten metal is sprayed onto a surface. Little is known about the health effects associated with these aerosols. Sprague-Dawley rats were exposed to aerosols (25 mg/m3 x 4 hr/d x 4 d) generated during thermal spray coating using different consumables [i.e., stainless-steel wire (PMET731), Ni-based wire (PMET885), Zn-based wire (PMET540)]. Control animals received air. Bronchoalveolar lavage was performed at 4 and 30 d post-exposure to assess lung toxicity. The particles were chain-like agglomerates and similar in size (310\u2013378 nm). Inhalation of PMET885 aerosol caused a significant increase in lung injury and inflammation at both time points. Inhalation of PMET540 aerosol caused a slight but significant increase in lung toxicity at 4 but not 30 d. Exposure to PMET731 aerosol had no effect on lung toxicity. Overall, the lung responses were in the order: PMET885>>PMET540>PMT731. Following a shorter exposure (25 mg/m3 x 4 h/d x 1d), lung burdens of metals from the different aerosols were determined by ICP-AES at 0, 1, 4 and 30 d post-exposure. Zn was cleared from the lungs at the fastest rate with complete clearance by 4 d post-exposure. Ni, Cr, and Mn had similar rates of clearance as nearly half of the deposited metal was cleared by 4 d. A small but significant percentage of each of these metals persisted in the lungs at 30 d. The pulmonary clearance of Fe was difficult to assess because of inherently high levels of Fe in control lungs.",
-            "title": "Lung toxicity, deposition, and clearance of thermal spray coating particles with different metal profiles after inhalation in rats",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13842,93 +13829,81 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/2se8-zi9r",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/2se8-zi9r",
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
+            "title": "Lung toxicity, deposition, and clearance of thermal spray coating particles with different metal profiles after inhalation in rats"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/4zqx-8w9w",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-03-28",
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
-            "identifier": "59144314-e1b2-5e50-9a00-a17b0eec7d0b",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard measure_value v2.11.16 (dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/measure_value.csv",
-                    "description": "Scorecard measure_value v2.11.16 (dev)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard measure_value v2.11.16 (dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard measure_value v2.11.16 (dev)"
                 }
             ],
+            "identifier": "59144314-e1b2-5e50-9a00-a17b0eec7d0b",
+            "issued": "2023-03-28",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/4zqx-8w9w",
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
+            "title": "Scorecard measure_value v2.11.16 (dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/647a-wjd2",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-20",
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
-            "identifier": "https://data.cdc.gov/api/views/647a-wjd2",
             "description": "State and territorial executive orders, administrative orders, resolutions, and proclamations are collected from government websites and cataloged and coded using Microsoft Excel by one coder with one or more additional coders conducting quality assurance.\n\nData were collected to determine when restaurants in states and territories were subject to closing and reopening requirements through executive orders, administrative orders, resolutions, and proclamations for COVID-19. Data can be used to determine when restaurants in states and territories were subject to closing and reopening requirements through executive orders, administrative orders, resolutions, and proclamations for COVID-19. Data consists exclusively of state and territorial orders, many of which apply to specific counties within their respective state or territory; therefore, data is broken down to the county level.\n\nThese data are derived from publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly close or reopen restaurants found by the CDC, COVID-19 Community Intervention & Critical Populations Task Force, Monitoring & Evaluation Team, Mitigation Policy Analysis Unit, and the CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 11, 2020 through May 31, 2021.  These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded; news media reports on restrictions were excluded. Recommendations not included in an order are not included in these data. Effective and expiration dates were coded using only the date provided; no distinction was made based on the specific time of the day the order became effective or expired. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
-            "title": "U.S. State and Territorial Orders Closing and Reopening Restaurants Issued from March 11, 2020 through May 31, 2021 by County by Day",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13951,49 +13926,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/647a-wjd2",
+            "issued": "2021-12-10",
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
+            "landingPage": "https://data.cdc.gov/d/647a-wjd2",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-09-20",
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
+            "title": "U.S. State and Territorial Orders Closing and Reopening Restaurants Issued from March 11, 2020 through May 31, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6p3a-6xr9",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-11-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2021-2022",
-            "modified": "2023-03-31",
-            "keyword": [
-                "adults",
-                "age",
-                "age group",
-                "covid-19",
-                "covid-19 vaccination",
-                "ethnicity",
-                "flu",
-                "influenza",
-                "race",
-                "vaccination",
-                "vaccination coverage"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Immunization and Respiratory Diseases (NCIRD)",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6p3a-6xr9",
             "description": "National Center for Immunization and Respiratory Diseases, US Centers for Disease Control and Prevention. Cumulative Influenza Vaccination Coverage and Intent for Vaccination Among Adults 18 Years and Older by Age, Race/Ethnicity, and COVID-19 Vaccination and Intent, United States; IPSOS Knowledge Panel and NORC AmeriSpeak Omnibus Surveys.",
-            "title": "Cumulative Influenza Vaccination Coverage and Intent for Vaccination Among Adults 18 Years and Older by Age, Race/Ethnicity, and COVID-19 Vaccination and Intent, United States; IPSOS Knowledge Panel and NORC AmeriSpeak Omnibus Surveys.",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14016,25 +13990,64 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "National",
+            "identifier": "https://data.cdc.gov/api/views/6p3a-6xr9",
+            "issued": "2021-11-16",
+            "keyword": [
+                "adults",
+                "age",
+                "age group",
+                "covid-19",
+                "covid-19 vaccination",
+                "ethnicity",
+                "flu",
+                "influenza",
+                "race",
+                "vaccination",
+                "vaccination coverage"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6p3a-6xr9",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2023-03-31",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "National",
+            "temporal": "2021-2022",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Cumulative Influenza Vaccination Coverage and Intent for Vaccination Among Adults 18 Years and Older by Age, Race/Ethnicity, and COVID-19 Vaccination and Intent, United States; IPSOS Knowledge Panel and NORC AmeriSpeak Omnibus Surveys."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-youth-survey-us-wave-iv-nys-1979",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>Youth data for the fourth wave of the National Youth Survey<br />\nare contained in this data collection. The first wave of this survey<br />\nwas conducted in 1976, the second wave in 1977, and the third wave in 1978. Data are available in<br />\nthis wave on the demographic and socioeconomic status of respondents,<br />\ndisruptive events in the home, youth aspirations and expectations,<br />\nsocial isolation, normlessness, perceived disapproval by parents and<br />\npeers, attitudes toward deviance, exposure and commitment to delinquent<br />\npeers, sex roles, interpersonal violence, pressure for substance abuse<br />\nby peers, self-reported delinquency, drug and alcohol use, and<br />\nvictimization.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Youth Survey US:  Wave IV (NYS-1979) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iv-nys-1979-nid13607",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iv-nys-1979-nid13607"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iv-nys-1979-nid13607",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "aspirations",
                 "behavior problems",
@@ -14066,66 +14079,29 @@
                 "young adults",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-youth-survey-us-wave-iv-nys-1979",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iv-nys-1979-nid13607",
-            "description": "<p>Youth data for the fourth wave of the National Youth Survey<br />\nare contained in this data collection. The first wave of this survey<br />\nwas conducted in 1976, the second wave in 1977, and the third wave in 1978. Data are available in<br />\nthis wave on the demographic and socioeconomic status of respondents,<br />\ndisruptive events in the home, youth aspirations and expectations,<br />\nsocial isolation, normlessness, perceived disapproval by parents and<br />\npeers, attitudes toward deviance, exposure and commitment to delinquent<br />\npeers, sex roles, interpersonal violence, pressure for substance abuse<br />\nby peers, self-reported delinquency, drug and alcohol use, and<br />\nvictimization.This study has 1 Data Set.</p>",
-            "title": "National Youth Survey US:  Wave IV (NYS-1979)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iv-nys-1979-nid13607",
-                    "description": "National Youth Survey US:  Wave IV (NYS-1979) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-iv-nys-1979-nid13607"
-                }
-            ]
+            "title": "National Youth Survey US:  Wave IV (NYS-1979)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mrip-2k2a",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-            "identifier": "https://data.cdc.gov/api/views/mrip-2k2a",
             "description": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease.",
-            "title": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14148,44 +14124,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mrip-2k2a",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "all ages",
+                "confirmed",
+                "invasive pneumococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mrip-2k2a",
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
+            "title": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bqmb-vyka",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/bqmb-vyka",
             "description": "NNDSS - Table 1H.  Cholera to Coccidioidomycosis - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1H.  Cholera to Coccidioidomycosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14208,38 +14186,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bqmb-vyka",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "cholera",
+                "coccidioidomycosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bqmb-vyka",
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
+            "title": "NNDSS - Table 1H.  Cholera to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/558z-cyuf",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-06-14",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-13",
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
-            "identifier": "f929e8d0-863b-4310-b4ce-1c8e28e6813c",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-06-05-to-2023-06-11",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14248,42 +14233,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-06-05-to-2023-06-11"
                 }
             ],
+            "identifier": "f929e8d0-863b-4310-b4ce-1c8e28e6813c",
+            "issued": "2023-06-14",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/558z-cyuf",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-06-13",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-06-05-to-2023-06-11"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/iu3b-5ngj",
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
-            "identifier": "https://data.cdc.gov/api/views/iu3b-5ngj",
             "description": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14306,41 +14284,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/iu3b-5ngj",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "nedss",
+                "netss",
+                "nndss",
+                "rubella",
+                "rubella congenital syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/iu3b-5ngj",
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
+            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-13",
-            "references": [
-                "http://www.fda.gov/MedicalDevices/Safety/ListofRecalls/ucm329946.htm"
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
-            "identifier": "c2420fb3-2c71-4a09-80a9-5fc2f3a459f5",
             "description": "This database contains a list of classified medical device recalls since November 1, 2002",
-            "title": "Medical and Radiation Emitting Device Recalls",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14348,66 +14329,70 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "c2420fb3-2c71-4a09-80a9-5fc2f3a459f5",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-13",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.fda.gov/MedicalDevices/Safety/ListofRecalls/ucm329946.htm"
+            ],
+            "title": "Medical and Radiation Emitting Device Recalls"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/nih-data-sharing-repositories",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2013-09-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "biomedical research",
-                "national-institutes-of-health-nih-department-of-health-human-services"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "admin",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
-            },
-            "identifier": "d98d5757-b20c-48b7-9f84-bfdc720c1d6f",
+            "dataQuality": true,
             "description": "<p>A list of NIH-supported repositories that accept submissions of appropriate scientific research data from biomedical researchers. It includes resources that aggregate information about biomedical data and information sharing systems. Links are provided to information about submitting data to and accessing data from the listed repositories. Additional information about the repositories and points-of contact for further information or inquiries can be found on the websites of the individual repositories.</p>",
-            "title": "NIH Data Sharing Repositories",
+            "identifier": "d98d5757-b20c-48b7-9f84-bfdc720c1d6f",
+            "issued": "2013-09-23",
+            "keyword": [
+                "biomedical research",
+                "national-institutes-of-health-nih-department-of-health-human-services"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/nih-data-sharing-repositories",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:046"
             ],
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "dataQuality": true
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
+            },
+            "title": "NIH Data Sharing Repositories"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/56kw-ijxb",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-09-06",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-05",
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
-            "identifier": "4df924c1-c00a-4387-bed6-3994a6aec8fe",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-28-to-2023-09-03",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14416,39 +14401,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-28-to-2023-09-03"
                 }
             ],
+            "identifier": "4df924c1-c00a-4387-bed6-3994a6aec8fe",
+            "issued": "2023-09-06",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/56kw-ijxb",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-09-05",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-28-to-2023-09-03"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD/PCDSimpleSearch.cfm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "references": [
-                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Overview/ClassifyYourDevice/ucm051668.htm"
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
-            "identifier": "3286eac6-86ad-4236-9281-8d09ad04e816",
+            "describedBy": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Overview/ClassifyYourDevice/ucm2005371.htm",
             "description": "This database contains medical device names and associated information developed by the Center. It includes a three letter device product code and a Device Class that refers to the level of CDRH regulation of a given device.",
-            "title": "Product Classification",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14456,42 +14438,39 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Overview/ClassifyYourDevice/ucm2005371.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "3286eac6-86ad-4236-9281-8d09ad04e816",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD/PCDSimpleSearch.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Overview/ClassifyYourDevice/ucm051668.htm"
+            ],
+            "title": "Product Classification"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-17",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-05-24",
-            "keyword": [
-                "adult",
-                "flu",
-                "flu shot",
-                "influenza",
-                "nis-acm",
-                "vaccine coverage"
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
-            "identifier": "https://data.cdc.gov/api/views/2v3t-r3np",
             "description": "Weekly Cumulative Influenza Vaccination Coverage, Adults 18 and Older, United States\n\n\u2022 Influenza vaccination coverage among adults is assessed through the National Immunization Survey-Adult COVID Module providing weekly influenza vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\u2022 NIS-ACM was started in April 2021 to survey adults 18 years and older COVID-19 vaccination uptake and vaccine confidence. \n\u2022 Final estimates for prior seasons and other flu vaccination data are available at CDC\u2019s FluVaxView: https://www.cdc.gov/flu/fluvaxview/index.htm.",
-            "title": "Weekly Cumulative Influenza Vaccination Coverage, Adults 18 and Older, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14514,119 +14493,153 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/2v3t-r3np",
+            "issued": "2023-11-17",
+            "keyword": [
+                "adult",
+                "flu",
+                "flu shot",
+                "influenza",
+                "nis-acm",
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
+            "spatial": "United States",
+            "temporal": "2023-2024",
             "theme": [
                 "Flu Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Influenza Vaccination Coverage, Adults 18 and Older, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/57r9-eggd",
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
-            "identifier": "f13ada0f-65b7-5d55-b4bd-2f9ff0855201",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_states_measures_download",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states_measures_download.csv",
-                    "description": "{\"dataset\": \"states_measures_download\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"states_measures_download\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states_measures_download.csv",
+                    "mediaType": "text/csv",
                     "title": "states_measures_download csv file"
                 }
             ],
+            "identifier": "f13ada0f-65b7-5d55-b4bd-2f9ff0855201",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/57r9-eggd",
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
+            "title": "featAuto_states_measures_download"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/57u7-zbua",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-05-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
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
-            "identifier": "f489a2dd-aef4-5fc8-b0ea-95d0308e3ee3",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard PILLAR vCORESET.1.1-test (coreset-local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/CORESET.1.1-test/20240430/PILLAR.csv",
-                    "description": "Scorecard PILLAR vCORESET.1.1-test (coreset-local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard PILLAR vCORESET.1.1-test (coreset-local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/CORESET.1.1-test/20240430/PILLAR.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard PILLAR vCORESET.1.1-test (coreset-local)"
                 }
             ],
+            "identifier": "f489a2dd-aef4-5fc8-b0ea-95d0308e3ee3",
+            "issued": "2024-05-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/57u7-zbua",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-05-07",
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
+            "title": "Scorecard PILLAR vCORESET.1.1-test (coreset-local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1991",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, anabolic steroids, and tobacco<br />\namong members of United States households aged 12 and older. Data are<br />\nalso provided on treatment for drug use and on illegal activities<br />\nrelated to drug use. Questions include age at first use, as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, inhalants, cocaine, hallucinogens, heroin, alcohol, tobacco,<br />\nand nonmedical use of psychotherapeutics. Respondents were also asked<br />\nabout problems resulting from their use of drugs, alcohol, and<br />\ntobacco, their perceptions of the risks involved, insurance coverage,<br />\nand personal and family income sources and amounts. Demographic data<br />\ninclude gender, race, ethnicity, educational level, job status, income<br />\nlevel, household composition, and population density.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1991) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1991-nid13584",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1991-nid13584"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1991-nid13584",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "alcohol consumption",
@@ -14654,144 +14667,111 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1991",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1991-nid13584",
-            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, anabolic steroids, and tobacco<br />\namong members of United States households aged 12 and older. Data are<br />\nalso provided on treatment for drug use and on illegal activities<br />\nrelated to drug use. Questions include age at first use, as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, inhalants, cocaine, hallucinogens, heroin, alcohol, tobacco,<br />\nand nonmedical use of psychotherapeutics. Respondents were also asked<br />\nabout problems resulting from their use of drugs, alcohol, and<br />\ntobacco, their perceptions of the risks involved, insurance coverage,<br />\nand personal and family income sources and amounts. Demographic data<br />\ninclude gender, race, ethnicity, educational level, job status, income<br />\nlevel, household composition, and population density.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-1991)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1991-nid13584",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-1991) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1991-nid13584"
-                }
-            ]
+            "title": "National Household Survey on Drug Abuse (NHSDA-1991)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/58rv-egst",
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
-            "identifier": "96856bde-4550-55cd-b032-8eda102fa32a",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_states",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/states.csv",
-                    "description": "{\"dataset\": \"states\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"states\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/states.csv",
+                    "mediaType": "text/csv",
                     "title": "states csv file"
                 }
             ],
+            "identifier": "96856bde-4550-55cd-b032-8eda102fa32a",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/58rv-egst",
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
+            "title": "devAuto_states"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://flybase.org/",
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
                 "fn": "GOOD, PETER J.",
                 "hasEmail": "mailto:goodp@mail.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "faf46179-3fce-451f-83b6-017f27f2e8b8",
+            "dataQuality": true,
             "description": "<p>Drosophila Genomic and Genetic database that includes proteomics data, microarrays and Tiling BAC's.</p>",
-            "title": "FlyBase: A Drosophila Genomic and Genetic Database",
+            "identifier": "faf46179-3fce-451f-83b6-017f27f2e8b8",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://flybase.org/",
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
+            "title": "FlyBase: A Drosophila Genomic and Genetic Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/59da-c8bi",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-27",
-            "keyword": [
-                "applications",
-                "child enrollment",
-                "chip",
-                "eligibility determinations",
-                "enrollment",
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
-            "identifier": "4723da0d-4d04-46ce-8163-e4b58c8fe728",
             "description": "This dataset includes total enrollment in separate CHIP (S-CHIP) programs by month and state from April 2023 forward.\r\n<p><b>Sources:</b> T-MSIS Analytic Files (TAF) and state-submitted enrollment totals. The data notes indicate when a state\u2019s monthly total was a state-submitted value, rather than from T-MSIS.<br/>\r\n<b>Methods:</b> Enrollment includes individuals enrolled in S-CHIP at any point during the coverage month, excluding those enrolled in dental-only coverage. The S-CHIP enrollment in this report also excludes enrollees covered by Medicaid expansion CHIP, a program in which a state receives federal funding to expand Medicaid eligibility to optional targeted low-income children that meets the requirements of section 2103 of the Social Security Act.  If an individual is enrolled in both Medicaid or Medicaid-expansion CHIP and S-CHIP in a given month, TAF picks the program in which they were last enrolled.<br/>\r\nUnless S-CHIP enrollment counts are replaced with a state-submitted value, each state's monthly S-CHIP enrollment is equal to the number of unique people in TAF with a CHIP_CODE = 3 (S-CHIP) and ELGBLTY_GRP_CD not equal to \u201866\u2019 (Children Eligible for Dental Only Supplemental Coverage). More information about TAF is available at <a href=\"https://www.medicaid.gov/medicaid/data-systems/macbis/medicaid-chip-research-files/transformed-medicaid-statistical-information-system-t-msis-analytic-files-taf/index.html\">https://www.medicaid.gov/medicaid/data-systems/macbis/medicaid-chip-research-files/transformed-medicaid-statistical-information-system-t-msis-analytic-files-taf/index.html</a>. </p>\t\r\n<b>Note:</b> A historic dataset with S-CHIP enrollment by month and state from April 2023 to June 2024 is also available at: <a href=\"https://data.medicaid.gov/dataset/d30cfc7c-4b32-4df1-b2bf-e0a850befd77\">https://data.medicaid.gov/dataset/d30cfc7c-4b32-4df1-b2bf-e0a850befd77</a>. This historic dataset was created to fulfill reporting requirements under section 1902(tt)(1) of the Social Security Act, which was added by section 5131(b) of subtitle D of title V of division FF of the Consolidated Appropriations Act, 2023 (P.L. 117-328) (CAA, 2023). Please note that the methods used to count S-CHIP enrollees differ slightly between the two datasets; as a result, data users should exercise caution if comparing S-CHIP enrollment across the two datasets.<br/>\r\n<b>State notes:</b>\r\n    Alaska, District of Columbia, Hawaii, New Hampshire, New Mexico, North Carolina, North Dakota, Ohio, South Carolina, Vermont, and Wyoming do not have S-CHIP programs.<br/>\r\n    Maryland has an S-CHIP program for the from conception to end of pregnancy group that began in July 2023; April 2023 - June 2023 data for Maryland represents retroactive coverage.<br/>\r\n   Oregon moved all its S-CHIP enrollees, other than those in the from conception to the end of pregnancy group, to a Medicaid-expansion CHIP program effective January 1, 2024.<br/>\r\nCHIP: Children's Health Insurance Program",
-            "title": "Separate CHIP Enrollment by Month and State",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14799,78 +14779,44 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "4723da0d-4d04-46ce-8163-e4b58c8fe728",
+            "issued": "2024-12-27",
+            "keyword": [
+                "applications",
+                "child enrollment",
+                "chip",
+                "eligibility determinations",
+                "enrollment",
+                "program enrollment"
+            ],
+            "landingPage": "https://healthdata.gov/d/59da-c8bi",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-12-27",
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
+            "title": "Separate CHIP Enrollment by Month and State"
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
-                "https://chronicdata.cdc.gov/d/idgn-d2g2"
-            ],
-            "keyword": [
-                "adult",
-                "age",
-                "cessation",
-                "cigar",
-                "cigarette",
-                "cigarette use",
-                "cigar use",
-                "consumption",
-                "current",
-                "demographics",
-                "education",
-                "ethnicity",
-                "ever",
-                "every day",
-                "former",
-                "frequency",
-                "gender",
-                "homes",
-                "never",
-                "office on smoking and health",
-                "osh",
-                "pipe",
-                "prevalence",
-                "quit",
-                "race",
-                "rules",
-                "smokefree",
-                "smokeless tobacco products",
-                "smoker",
-                "smoking",
-                "smoking status",
-                "some days",
-                "state system",
-                "survey",
-                "tobacco",
-                "tobacco use",
-                "worksites"
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
-            "identifier": "https://data.cdc.gov/api/views/4y6p-yphk",
+            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/Tobacco-Use-Supplement-to-the-Current-Population-S/4y6p-yphk",
             "description": "1992-1993, 1995-1996, 1998-1999, 2001-2002, 2003, 2006-2007, 2010-2011, 2014-2015.   Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  TUS-CPS Survey Data.  The Current Population Survey is a monthly survey of about 50,000 households conducted by the Bureau of the Census for the Bureau of Labor Statistics. The survey has been conducted for more than 50 years. Estimates obtained from the CPS include employment, unemployment, earnings, hours of work, and other indicators. Supplemental surveys include questions about a variety of topics, including an annual social and economic supplement, school enrollment, work schedules, voting and registration, job tenure and occupational mobility, food security, and tobacco use.\r\n\r\nThe data for the STATE System were obtained through the Tobacco Use Supplement to the Current Population Survey (TUS-CPS).  Tobacco topics included are cigarette smoking status, cigarette smoking prevalence by demographics, cigarette smoking frequency, cigarette consumption, quit attempts, cigar use, pipe use, smokeless tobacco use, and smokefree rules/policies in homes and worksites.",
-            "title": "Tobacco Use Supplement to the Current Population Survey (TUS-CPS) Data",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14893,42 +14839,78 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/Tobacco-Use-Supplement-to-the-Current-Population-S/4y6p-yphk",
+            "identifier": "https://data.cdc.gov/api/views/4y6p-yphk",
+            "issued": "2025-01-31",
+            "keyword": [
+                "adult",
+                "age",
+                "cessation",
+                "cigar",
+                "cigarette",
+                "cigarette use",
+                "cigar use",
+                "consumption",
+                "current",
+                "demographics",
+                "education",
+                "ethnicity",
+                "ever",
+                "every day",
+                "former",
+                "frequency",
+                "gender",
+                "homes",
+                "never",
+                "office on smoking and health",
+                "osh",
+                "pipe",
+                "prevalence",
+                "quit",
+                "race",
+                "rules",
+                "smokefree",
+                "smokeless tobacco products",
+                "smoker",
+                "smoking",
+                "smoking status",
+                "some days",
+                "state system",
+                "survey",
+                "tobacco",
+                "tobacco use",
+                "worksites"
+            ],
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
+                "https://chronicdata.cdc.gov/d/idgn-d2g2"
+            ],
             "theme": [
                 "Survey Data"
-            ]
+            ],
+            "title": "Tobacco Use Supplement to the Current Population Survey (TUS-CPS) Data"
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
-                "unmet need"
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
-            "identifier": "https://data.cdc.gov/api/views/xb3p-q62w",
             "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, gender, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
-            "title": "Indicators of Reduced Access to Care Due to the Coronavirus Pandemic During Last 4 Weeks",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14951,25 +14933,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/xb3p-q62w",
+            "issued": "2020-05-20",
+            "keyword": [
+                "covid-19",
+                "delayed care",
+                "unmet need"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/reduced-access-to-care.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-04-14",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://findahealthcenter.hrsa.gov/",
             "bureauCode": [
                 "009:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HRSA Bureau of Primary Care",
+                "hasEmail": "mailto:comments@hrsa.gov"
+            },
+            "description": "<p>HRSA Health Centers care for you, even if you have no health insurance \u2013 you pay what you can afford based on your income. Health centers provide services that include checkups when you are well, treatment when you are sick, complete care when you are pregnant, and immunizations and checkups for your children. Some health centers also provide mental health, substance abuse, oral health, and/or vision services. Contact the health center organization directly to confirm the availability of specific services and to make an appointment.</p>",
+            "identifier": "27b4e77a-5adc-4b6a-bc26-6bbe7beac8b2",
             "issued": "2017-07-14",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "clinic locations",
                 "community health",
@@ -14982,62 +14986,37 @@
                 "primary care",
                 "sliding scale"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HRSA Bureau of Primary Care",
-                "hasEmail": "mailto:comments@hrsa.gov"
-            },
+            "landingPage": "https://findahealthcenter.hrsa.gov/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Health Resources and Services Administration"
             },
-            "identifier": "27b4e77a-5adc-4b6a-bc26-6bbe7beac8b2",
-            "description": "<p>HRSA Health Centers care for you, even if you have no health insurance \u2013 you pay what you can afford based on your income. Health centers provide services that include checkups when you are well, treatment when you are sick, complete care when you are pregnant, and immunizations and checkups for your children. Some health centers also provide mental health, substance abuse, oral health, and/or vision services. Contact the health center organization directly to confirm the availability of specific services and to make an appointment.</p>",
-            "title": "Find a Health Center",
-            "programCode": [
-                "009:013"
-            ],
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "Community",
                 "Health",
                 "National",
                 "State"
-            ]
+            ],
+            "title": "Find a Health Center"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5cf3-8irw",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-04-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-01",
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
-            "identifier": "e6205a51-e6d7-4849-9882-4483b8a28c41",
             "description": "State-reported data on Medicaid and CHIP eligibility renewals that reflect the outcomes of previously pending renewals three months after the renewal was due and also any corrections to the original renewal data submitted to CMS. <a href=\"https://data.medicaid.gov/dataset/ebcfc16f-8291-4c61-82a4-055846d72f3a/data?conditions%5B0%5D%5Bproperty%5D=reporting_period&amp;conditions%5B0%5D%5Bvalue%5D=202312&amp;conditions%5B0%5D%5Boperator%5D=%3D\">See here</a> for original renewal data.<br />\r\nCMS <a href=\"https://www.medicaid.gov/resources-for-states/coronavirus-disease-2019-covid-19/unwinding-and-returning-regular-operations-after-covid-19/data-reporting/data-reporting-tools/index.html\">renewal data specifications</a> require states to update and submit to CMS their monthly renewal outcome metrics - metric 5 data and its submetrics (monthly metrics 5a, 5a(1), 5a(2), 5b, 5c, and 5d) - after the original monthly report submission. The \u201cupdated\u201d renewal data reflect the outcomes of renewals previously reported as pending (monthly metric 5d of the original monthly report) as of three months after the renewal was due. For more information about this data set and considerations for users when reviewing, please see the Medicaid and CHIP Unwinding: Data Sources and Metrics Definitions Overview <a href=\"https://www.medicaid.gov/media/160271\">found here</a>.\r\n<br /><b>Sources:</b> <br />(1) March 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report pulled on March 05, 2024, representing the updated disposition of renewals due in March 2023 as of June 2023. April 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report pulled on March 05, 2024, representing the updated disposition of renewals due in April 2023 as of July 2023. May 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report pulled on March 05, 2024, representing the updated disposition of renewals due in May 2023 as of August 2023. June 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report pulled on March 05, 2024, representing the updated disposition of renewals due in June 2023 as of September 2023. July 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report pulled on March 05, 2024, representing the updated disposition of renewals due in July 2023 as of October 2023. August 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report pulled on March 05, 2024, representing the updated disposition of renewals due in August 2023 as of November 2023. September 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report pulled on April 02, 2024, representing the updated disposition of renewals due in September 2023 as of December 2023. October 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report pulled on April 02, 2024, representing the updated disposition of renewals due in October 2023 as of January 2024. November 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report pulled on May 07, 2024, representing the updated disposition of renewals due in November 2023 as of February 2024. December 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report pulled on June 11, 2024, representing the updated disposition of renewals due in December 2023 as of March 2024. New Hampshire\u2019s December 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report pulled on April 09, 2024, representing the updated disposition of renewals due in December 2023 as of March 2024. New York\u2019s December 2023 state Medicaid and CHIP Renewal and Termination Data for the Unwinding Data Report pulled on April 22, 2024, representing the updated disposition of renewals due in December 2023 as of March 2024. January 2024 state Medicaid and CHIP Renewal and Termination Data for t",
-            "title": "Medicaid and CHIP Updated Renewal Outcomes",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15123,21 +15102,55 @@
                     "title": "March 2023 Updated Medicaid and CHIP Renewal Outcomes"
                 }
             ],
+            "identifier": "e6205a51-e6d7-4849-9882-4483b8a28c41",
+            "issued": "2024-04-30",
+            "keyword": [
+                "applications",
+                "child enrollment",
+                "chip",
+                "eligibility determinations",
+                "enrollment",
+                "medicaid",
+                "program enrollment"
+            ],
+            "landingPage": "https://healthdata.gov/d/5cf3-8irw",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-11-01",
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
+            "title": "Medicaid and CHIP Updated Renewal Outcomes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2006",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 16 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Drug Abuse Warning Network (DAWN-2006) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2006-nid13603",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2006-nid13603"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2006-nid13603",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol",
                 "demographic characteristics",
@@ -15150,62 +15163,30 @@
                 "substance abuse",
                 "suicide"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2006",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2006-nid13603",
-            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 16 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
-            "title": "Drug Abuse Warning Network (DAWN-2006)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2006-nid13603",
-                    "description": "Drug Abuse Warning Network (DAWN-2006) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2006-nid13603"
-                }
-            ]
+            "title": "Drug Abuse Warning Network (DAWN-2006)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5cim-jmbs",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-08-09",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-16",
-            "keyword": [
-                "individual",
-                "individual market dental",
-                "py2023",
-                "qhp landscape",
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
-            "identifier": "e023a113-2c4a-4e4f-b177-0544e2dccccd",
             "description": "The Dental Individual Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to consumers in the individual market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2023 Individual Dental",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15213,36 +15194,38 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "e023a113-2c4a-4e4f-b177-0544e2dccccd",
+            "issued": "2023-08-09",
+            "keyword": [
+                "individual",
+                "individual market dental",
+                "py2023",
+                "qhp landscape",
+                "sadp"
+            ],
+            "landingPage": "https://healthdata.gov/d/5cim-jmbs",
+            "modified": "2023-08-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2023 Individual Dental"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/s9bp-7k3m",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-09-26",
-            "@type": "dcat:Dataset",
-            "modified": "2016-09-26",
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
-            "identifier": "https://data.cdc.gov/api/views/s9bp-7k3m",
             "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012 & 2014.",
-            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), All States, 2012 & 2014",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15265,49 +15248,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/s9bp-7k3m",
+            "issued": "2016-09-26",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/s9bp-7k3m",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-09-26",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), All States, 2012 & 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/npals/webtables/overview.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-05-11",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-11-01/2021-07-31",
-            "modified": "2024-10-24",
-            "keyword": [
-                "activities of daily living",
-                "adult day services centers",
-                "diagnoses",
-                "healthcare",
-                "long-term care",
-                "medicaid",
-                "nurse staffing",
-                "post-acute care",
-                "residential care communities",
-                "sdoh-access-to-health-care",
-                "sdoh-use-of-health-care"
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
-            "identifier": "https://data.cdc.gov/api/views/wibz-pb5q",
             "description": "The NCHS National Post-acute and Long-term Care Study (NPALS) collects data on post-acute and long-term care providers every two years. The goal is to monitor post-acute and long-term care settings with reliable, accurate, relevant, and timely statistical information to support and inform policy, research, and practice. These data tables provide an overview of the geographic, organizational, staffing, service provision, and user characteristics of paid, regulated long-term and post-acute care providers in the United States. The settings include adult day services centers, home health agencies, hospices, inpatient rehabilitation facilities, long-term care hospitals, and nursing homes.",
-            "title": "Biennial Overview of Post-acute and Long-term Care in the United States: Data from the 2020 National Post-acute and Long-term Care Study",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15330,85 +15304,98 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/wibz-pb5q",
+            "issued": "2023-05-11",
+            "keyword": [
+                "activities of daily living",
+                "adult day services centers",
+                "diagnoses",
+                "healthcare",
+                "long-term care",
+                "medicaid",
+                "nurse staffing",
+                "post-acute care",
+                "residential care communities",
+                "sdoh-access-to-health-care",
+                "sdoh-use-of-health-care"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/npals/webtables/overview.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2024-10-24",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2020-11-01/2021-07-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Biennial Overview of Post-acute and Long-term Care in the United States: Data from the 2020 National Post-acute and Long-term Care Study"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5drk-e3yq",
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
-            "identifier": "935a5667-0da1-56a5-8a7a-e5e4135abd06",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_measure_compare",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_compare.csv",
-                    "description": "{\"dataset\": \"measure_compare\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_compare\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_compare.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_compare csv file"
                 }
             ],
+            "identifier": "935a5667-0da1-56a5-8a7a-e5e4135abd06",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/5drk-e3yq",
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
+            "title": "featAuto_measure_compare"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/g5ts-294x",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Pathology and Physiology Branch, HELD",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/g5ts-294x",
             "description": "Silicosis is an irreversible occupational lung disease resulting from crystalline silica exposure. Previously, we discovered that Western diet (HFWD)-consumption increases susceptibility to silica-induced pulmonary inflammation and fibrosis. This study investigates the potential of HFWD to alter silica-induced effects on airway epithelial ion transport and smooth muscle reactivity.",
-            "title": "High-Fat Western Diet Alters Silica-induced airway epithelium ion exchange but not airway smooth muscle reactivity",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15416,44 +15403,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/g5ts-294x",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/g5ts-294x",
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
+            "title": "High-Fat Western Diet Alters Silica-induced airway epithelium ion exchange but not airway smooth muscle reactivity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/niosh-certified-equipment-list-cel",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-05-30",
-            "temporal": "1972-01-01T00:00:00-05:00/1972-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "certification",
-                "equipment",
-                "occupational health",
-                "personal protective",
-                "respirator",
-                "safety"
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
-            "identifier": "63a7cbf3-3b97-407d-a7b7-c55431fc9829",
+            "dataQuality": true,
             "description": "<p>The National Institute for Occupational Safety and Health (NIOSH), under the authorization of the Federal Mine Safety and Health Act of 1977 and the Occupational Safety and Health Act of 1970, provides a testing approval and certification program assuring commercial availability of safe personal protective devices. NIOSH develops improved performance regulations, tests and certifies (or approves) devices, and purchases approved and certified products on the open market to verify quality of manufacture</p>",
-            "title": "NIOSH Certified Equipment List (CEL)",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15462,41 +15441,45 @@
                     "title": "Query Tool "
                 }
             ],
-            "dataQuality": true,
+            "identifier": "63a7cbf3-3b97-407d-a7b7-c55431fc9829",
+            "issued": "2012-05-30",
+            "keyword": [
+                "certification",
+                "equipment",
+                "occupational health",
+                "personal protective",
+                "respirator",
+                "safety"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/niosh-certified-equipment-list-cel",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "temporal": "1972-01-01T00:00:00-05:00/1972-01-01T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "NIOSH Certified Equipment List (CEL)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5fhv-8y53",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2020-07-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-21",
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
-            "identifier": "cc318bfb-a9b2-55f3-a924-d47376b32ea3",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2020",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15504,51 +15487,41 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "cc318bfb-a9b2-55f3-a924-d47376b32ea3",
+            "issued": "2020-07-30",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/5fhv-8y53",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-10-21",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "State Drug Utilization"
-            ]
+            ],
+            "title": "State Drug Utilization Data 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-06-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
-            "keyword": [
-                "behaviors",
-                "census tract",
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
-            "identifier": "https://data.cdc.gov/api/views/shc3-fzig",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
             "description": "This dataset contains model-based census tract level estimates for the PLACES 2022 release in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. These data can be joined with the census tract 2015 boundary file in a GIS system to produce maps for 29 measures at the census tract level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=3b7221d4e47740cab9235b839fa55cd7",
-            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2022 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15571,36 +15544,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
+            "identifier": "https://data.cdc.gov/api/views/shc3-fzig",
+            "issued": "2023-06-15",
+            "keyword": [
+                "behaviors",
+                "census tract",
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
+            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2022 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/8nyy-xsq7",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCIRD",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/8nyy-xsq7",
             "description": "Weekly Cumulative Influenza Vaccination Coverage Comparison between Current and Previous Season, Children 6 Months through 17 Years, United States \n\n\u2022 Influenza vaccination coverage among children is assessed through the National Immunization Survey-Flu (NIS-Flu) annually, providing weekly influenza vaccination coverage estimates for children 6 months\u201317 years based upon parental report. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html) \n\no NIS-Flu is a national random-digit-dialed cellular telephone survey of households conducted during the flu season (October-June). \n\n\u2022 Additional information about NIS-Flu methods and estimates from the 2019-2020 season are available at: https://www.cdc.gov/flu/fluvaxview/coverage-1920estimates.htm. Final estimates for prior seasons and other flu vaccination data are available at CDC\u2019s FluVaxView.:  https://www.cdc.gov/flu/fluvaxview/index.htm.",
-            "title": "Weekly Cumulative Influenza Vaccination Coverage Comparison between Current and Previous Season, Children 6 Months through 17 Years, United States",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15623,40 +15611,39 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, States, and Local Jurisdictions",
+            "identifier": "https://data.cdc.gov/api/views/8nyy-xsq7",
+            "issued": "2023-12-01",
+            "landingPage": "https://data.cdc.gov/d/8nyy-xsq7",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2024-05-24",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States, States, and Local Jurisdictions",
             "theme": [
                 "Child Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Influenza Vaccination Coverage Comparison between Current and Previous Season, Children 6 Months through 17 Years, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mhj9-4wi2",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2016-11-30",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-27",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OSHData Support",
                 "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mhj9-4wi2",
             "description": "2010-2018; 2019. US Census Annual Estimates of the Resident Population for Selected Age Groups by Sex for the United States. The estimates for the 2010-2018 dataset are based on the 2010 Census and reflect changes to the April 1, 2010 population due to the Count Question Resolution program and geographic program revisions. Median age is calculated based on single year of age. The estimates for 2019 are based on a one-year dataset that was published on the US Census website in 2021. For population estimates methodology statements, see http://www.census.gov/popest/methodology/index.html.",
-            "title": "US Census Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15664,39 +15651,35 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mhj9-4wi2",
+            "issued": "2016-11-30",
+            "landingPage": "https://data.cdc.gov/d/mhj9-4wi2",
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
                 "Funding"
-            ]
+            ],
+            "title": "US Census Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/msjj-a7q2",
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
-            "identifier": "https://data.cdc.gov/api/views/msjj-a7q2",
             "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2014 national data: National Occupant Protection Use Survey (NOPUS), 2014.  Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 state data: Seat Belt Use in 2014- Use Rates in the States and Territories",
-            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 10 - Seattle",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15719,38 +15702,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/msjj-a7q2",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/msjj-a7q2",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 10 - Seattle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/eds5-ig9r",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-02-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-03",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/eds5-ig9r",
             "description": "Yearly citation totals from each year of the MEDLINE/PubMed Baseline referencing citations back to year 1781.  These totals may increase over time for a particular year as new citations are added.  For example, 25 citations were listed for the year 1800 in the 2018 MEDLINE/PubMed Baseline, while the 2019 Baseline includes 387 citations for that year.",
-            "title": "PubMed total records by publication year",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15773,45 +15757,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/eds5-ig9r",
+            "issued": "2022-02-10",
+            "keyword": [
+                "pubmed"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/eds5-ig9r",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-03",
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
+            "title": "PubMed total records by publication year"
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
-                "county",
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
-            "identifier": "https://data.cdc.gov/api/views/i2vk-mgdh",
+            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Heart-Disease-Mortality-Data-Among-US-Adults-35-by/i2vk-mgdh",
             "description": "2013 to 2015, 3-year average. Rates are age-standardized. County rates are spatially smoothed. The data can be viewed by gender and race/ethnicity. Data source: National Vital Statistics System. Additional data, maps, and methodology can be viewed on the Interactive Atlas of Heart Disease and Stroke http://www.cdc.gov/dhdsp/maps/atlas",
-            "title": "Heart Disease Mortality Data Among US Adults (35+) by State/Territory and County",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15834,42 +15812,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Heart-Disease-Mortality-Data-Among-US-Adults-35-by/i2vk-mgdh",
+            "identifier": "https://data.cdc.gov/api/views/i2vk-mgdh",
+            "issued": "2023-07-18",
+            "keyword": [
+                "cardiovascular disease",
+                "county",
+                "heart disease"
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
+            "title": "Heart Disease Mortality Data Among US Adults (35+) by State/Territory and County"
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
-            "identifier": "https://data.cdc.gov/api/views/amjr-ph5r",
             "description": "\u2022 Weekly Differences in Cumulative Influenza Vaccination Coverage by Selected Demographics and by Season, 2024-25 and 2024-25 Compared with 2023-24, Children 6 Months\u201317 Years, United States.\n\n\u2022 Weekly Influenza vaccination coverage and parental intent for vaccination among children is calculated using data from the National Immunization Survey\u2013Flu (NIS\u2013Flu) (https://www.cdc.gov/nis/about/index.html). NIS\u2013Flu is a national random-digit-dialed cellular telephone survey of households with children ages 6 months\u201317 years conducted during October-June. The respondent to a NIS\u2013Flu survey is a parent or guardian who said they were knowledgeable about the child\u2019s vaccination history. All estimates are based upon parental report of receipt of vaccination and month of that vaccination.",
-            "title": "Weekly Differences in Cumulative Influenza Vaccination Coverage by Selected Demographics and by Season, 2024-25 and 2024-25 Compared with 2023-24, Children 6 Months -17 Years, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15892,45 +15874,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/amjr-ph5r",
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
+            "title": "Weekly Differences in Cumulative Influenza Vaccination Coverage by Selected Demographics and by Season, 2024-25 and 2024-25 Compared with 2023-24, Children 6 Months -17 Years, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://ftp.ncbi.nih.gov/repository/UniGene/",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ixcy-uq3c",
             "description": "An automated analytical system for producing organized views of the transcriptome from a growing number of organisms. UniGene was retired in July 2019; however, you will continue to be able to access archived data.",
-            "title": "UniGene archived data (RETIRED)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15939,41 +15921,41 @@
                     "title": "Download UniGene (Archived Data)"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ixcy-uq3c",
+            "issued": "2022-03-02",
+            "keyword": [
+                "computational biology",
+                "dataset",
+                "genomics"
+            ],
+            "landingPage": "https://ftp.ncbi.nih.gov/repository/UniGene/",
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
+            "title": "UniGene archived data (RETIRED)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5ifr-n23x",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-03-02",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-30",
-            "keyword": [
-                "exchange puf",
-                "marketplace puf",
-                "py2022",
-                "transparency in coverage"
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
-            "identifier": "e5af98d2-deda-48c2-a6e3-4be667f938d3",
             "description": "The Transparency in Coverage PUF (TC-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The PUF contains data on issuer and plan-level claims, appeals, and active URL data. The PY2022 PUF contains data from PY2020 for issuers participating in the Exchange in PY2020.",
-            "title": "Transparency in Coverage PUF - PY2022",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15981,43 +15963,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "e5af98d2-deda-48c2-a6e3-4be667f938d3",
+            "issued": "2022-03-02",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2022",
+                "transparency in coverage"
+            ],
+            "landingPage": "https://healthdata.gov/d/5ifr-n23x",
+            "modified": "2022-03-30",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Transparency in Coverage PUF - PY2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/d69q-iyrb",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
-            "keyword": [
-                "2015",
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
-            "identifier": "https://data.cdc.gov/api/views/d69q-iyrb",
             "description": "NNDSS - Table II. Mumps to Rabies, animal - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Mumps to Rabies, animal",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16040,41 +16016,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/d69q-iyrb",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
+                "mmwr",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "pertussis",
+                "rabies animal",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/d69q-iyrb",
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
+            "title": "NNDSS - Table II. Mumps to Rabies, animal"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5jn7-f3kn",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-07-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-28",
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
-            "identifier": "d32dc095-de60-45f0-9e58-852257970244",
             "description": "The Reference Document link for the downable Blood Disorder Treatment Spreadsheet can be accessed below under the Additional Information table under Related Documents.",
-            "title": "Pricing Comparison for Blood Disorder Treatments (Pricing as of 06/1/2024)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16082,48 +16064,41 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "d32dc095-de60-45f0-9e58-852257970244",
+            "issued": "2024-07-01",
+            "keyword": [
+                "drug products"
+            ],
+            "landingPage": "https://healthdata.gov/d/5jn7-f3kn",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-06-28",
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
+            "title": "Pricing Comparison for Blood Disorder Treatments (Pricing as of 06/1/2024)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/j9id-xrm6",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
-            "keyword": [
-                "2015",
-                "anaplasma phagocytophilum",
-                "ehrlichia chaffeensis",
-                "ehrlichiosis/anaplasmosis",
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
-            "identifier": "https://data.cdc.gov/api/views/j9id-xrm6",
             "description": "NNDSS - Table II. Ehrlichiosis/Anaplasmosis - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.   NP:  Nationally notifiable but not published.   Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Cumulative total E. ewingii cases reported for year 2015 = 0, and 14 cases reported for 2014.",
-            "title": "NNDSS - Table II. Ehrlichiosis/Anaplasmosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16146,45 +16121,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/j9id-xrm6",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
+                "anaplasma phagocytophilum",
+                "ehrlichia chaffeensis",
+                "ehrlichiosis/anaplasmosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "undetermined",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/j9id-xrm6",
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
+            "title": "NNDSS - Table II. Ehrlichiosis/Anaplasmosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/psx4-wq38",
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
-            "identifier": "https://data.cdc.gov/api/views/psx4-wq38",
             "description": "This file contains death counts and death rates for drug overdose, suicide, homicide and firearm injuries by county of residence (additional datasets exist for other levels of geography). The data is grouped by 2 different time periods including yearly and trailing twelve months. Please see data dictionary for intents and mechanisms included in each measure. \n\n \n\nWhen there are 1-9 deaths in an area, CDC uses a Bayesian model to calculate rates. A Bayesian model is a type of statistical model often used in geographic analysis. This model can improve stability of the rates in lower population areas and protects privacy by taking into account information from neighboring areas.",
-            "title": "Mapping Injury, Overdose, and Violence - County",
-            "programCode": [
-                "009:033"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16207,40 +16185,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/psx4-wq38",
+            "issued": "2025-01-13",
+            "keyword": [
+                "deaths",
+                "drug overdose",
+                "firearm injury",
+                "homicide",
+                "mortality",
+                "nchs",
+                "suicide"
+            ],
+            "landingPage": "https://data.cdc.gov/d/psx4-wq38",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:033"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2019-01-01/Present",
             "theme": [
                 "Injury & Violence"
-            ]
+            ],
+            "title": "Mapping Injury, Overdose, and Violence - County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/uxwq-vny5",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-06-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-03",
-            "keyword": [
-                "abcs",
-                "bactfacts"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Active Bacterial Core surveillance",
                 "hasEmail": "mailto:abcs@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/uxwq-vny5",
             "description": "ABCs is an ongoing surveillance program that began in 1997. <a href=\"https://www.cdc.gov/abcs/reports-findings/surv-reports.html\">ABCs reports</a> describe the ABCs case definition and the specific methodology used to calculate rates and estimated numbers in the United States for each bacterium by year.  The methods, <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">surveillance areas</a>, and <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">laboratory isolate collection areas</a> have changed over time.\n                Additionally, the way missing data are taken into account changed in 2010.  It went from distributing unknown values based on known values of cases by site to use of multiple imputation using a sequential regression imputation method.\n                Given these changes over time, trends should be interpreted with caution.\n<ul> <li> <a href=\"http://www.cdc.gov/abcs/methodology/index.html\">Methodology</a>\nFind details about surveillance population, case determination, surveillance evaluation, and more. </li>                    <li> <a href=\"http://www.cdc.gov/abcs/reports-findings/index.html\">Reports and Findings</a>\nGet official interpretations from reports and publications created from ABCs data. </li>\n  </ul>",
-            "title": "Active Bacterial Core surveillance (ABCs) Haemophilus influenzae",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16263,40 +16246,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/uxwq-vny5",
+            "issued": "2021-06-23",
+            "keyword": [
+                "abcs",
+                "bactfacts"
+            ],
+            "landingPage": "https://data.cdc.gov/d/uxwq-vny5",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-09-03",
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
+            "title": "Active Bacterial Core surveillance (ABCs) Haemophilus influenzae"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5m3m-f68d",
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
-            "identifier": "138872f1-b1ba-5e05-be13-8be200306a58",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2011",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16304,24 +16287,51 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "138872f1-b1ba-5e05-be13-8be200306a58",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/5m3m-f68d",
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
+            "title": "State Drug Utilization Data 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/onc-community-college-consortia-educate-health-it-professionals-program-key",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2014-06-01",
-            "references": [
-                "http://www.healthit.gov/facas/sites/faca/files/Workforce%20Evaluation%20Briefing%20for%20FACA%20Committee%2009%2010.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/onc-community-college-consortia-educate-health-it-professionals-program-key",
+            "description": "The Office of the National Coordinator for Health Information Technology (ONC) created the Community College Consortia to Educate Health IT Professionals in Health Care Program to increase the workforce of skilled health IT specialists that can help transition health care providers to electronic health records (EHRs). The Community College Consortia Program includes 82 member community colleges representing all 50 states. The member community colleges received funding to rapidly create health IT academic programs, or expand existing health IT training programs that can be completed in six months or less. This data provides key performance indicators by U.S. state. The data is provided beginning in September, 2010 and through September, 2013: the duration of the program. This data is an artifact of ONC's performance measurement for the Recovery and HITECH acts.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/Comm_College_Consortia_KPI.csv",
+                    "mediaType": "text/csv",
+                    "title": "Comm_College_Consortia_KPI.csv"
+                }
             ],
+            "identifier": "51r770k2-dmbo-1kp5-9582-4gn8mameur80",
+            "issued": "2023-10-03",
             "keyword": [
                 "grants",
                 "health data",
@@ -16333,61 +16343,32 @@
                 "trainee",
                 "training"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/onc-community-college-consortia-educate-health-it-professionals-program-key",
+            "modified": "2014-06-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "51r770k2-dmbo-1kp5-9582-4gn8mameur80",
-            "description": "The Office of the National Coordinator for Health Information Technology (ONC) created the Community College Consortia to Educate Health IT Professionals in Health Care Program to increase the workforce of skilled health IT specialists that can help transition health care providers to electronic health records (EHRs). The Community College Consortia Program includes 82 member community colleges representing all 50 states. The member community colleges received funding to rapidly create health IT academic programs, or expand existing health IT training programs that can be completed in six months or less. This data provides key performance indicators by U.S. state. The data is provided beginning in September, 2010 and through September, 2013: the duration of the program. This data is an artifact of ONC's performance measurement for the Recovery and HITECH acts.",
-            "title": "ONC Community College Consortia to Educate Health IT Professionals Program Key Performance Indicators (KPIs)",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/Comm_College_Consortia_KPI.csv",
-                    "mediaType": "text/csv",
-                    "title": "Comm_College_Consortia_KPI.csv"
-                }
+            "references": [
+                "http://www.healthit.gov/facas/sites/faca/files/Workforce%20Evaluation%20Briefing%20for%20FACA%20Committee%2009%2010.pdf"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/onc-community-college-consortia-educate-health-it-professionals-program-key"
+            "title": "ONC Community College Consortia to Educate Health IT Professionals Program Key Performance Indicators (KPIs)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/5bhp-bdab",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2023-12-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/5bhp-bdab",
             "description": "<b>(Includes MeSH 2023 and 2024 changes) NOTE - There are no Merges for 2025 MeSH.</b>  The MeSH 2025 Update - Merge Report describes cases where two or more terms have merged into a single term. The term(s) being merged into another term become(s) an Entry Term.  Merges can be between Descriptors and Supplementary Concept Records (SCRs), between Descriptors, or between SCRs.  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
-            "title": "MeSH 2025 Update - Merge Report",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16410,46 +16391,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/5bhp-bdab",
+            "issued": "2023-12-14",
+            "keyword": [
+                "api",
+                "mesh",
+                "mesh 2023 update",
+                "terminologies"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/5bhp-bdab",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-16",
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
+            "title": "MeSH 2025 Update - Merge Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4jje-6vv6",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/4jje-6vv6",
             "description": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16472,42 +16448,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4jje-6vv6",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "all serogroups",
+                "meningococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "serogroup b",
+                "serogroups acwy",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/4jje-6vv6",
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
+            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fpqb-s69d",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2018-07-16",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-27",
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
                 "hasEmail": "mailto:nephtrackingsupport@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/fpqb-s69d",
             "description": "This dataset provides modeled predictions of PM2.5 levels from the EPA's Downscaler model. Data are at the census tract level for 2006-2010. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\r\n\r\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2006-2010",
-            "programCode": [
-                "009:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16530,40 +16510,43 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fpqb-s69d",
+            "issued": "2018-07-16",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "particulate matter",
+                "pm2.5"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fpqb-s69d",
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
+            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2006-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5np2-bsac",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2016-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-26",
-            "keyword": [
-                "amp",
-                "federal upper limits",
-                "ful"
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
-            "identifier": "ce4cf49b-a21b-5a53-bbc3-509414940847",
             "description": "Affordable Care Act Federal Upper Limits (FUL) based on the weighted average of the most recently reported monthly average manufacturer price (AMP) for pharmaceutically and therapeutically equivalent multiple source drug products that are available for purchase by retail community pharmacies on a nationwide basis.",
-            "title": "ACA Federal Upper Limits",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16571,90 +16554,87 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "ce4cf49b-a21b-5a53-bbc3-509414940847",
+            "issued": "2016-10-31",
+            "keyword": [
+                "amp",
+                "federal upper limits",
+                "ful"
+            ],
+            "landingPage": "https://healthdata.gov/d/5np2-bsac",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-12-26",
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
+            "title": "ACA Federal Upper Limits"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5npy-pruv",
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
-                "dual enrollment",
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
-            "identifier": "36ed6909-ab49-4ca5-a38e-6790138cd613",
             "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by dual eligibility status for Medicaid and Medicare (full dual eligibility, partial dual eligibility, or not dually eligible).\r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Dually Enrolled in Medicare. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.\r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Dual Status Information for Medicaid and CHIP Beneficiaries by Month",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/DualStatus-montly.csv",
-                    "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by dual eligibility status for Medicaid and Medicare (full dual eligibility, partial dual eligibility, or not dually eligible).\n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Dually Enrolled in Medicare. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.\n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by dual eligibility status for Medicaid and Medicare (full dual eligibility, partial dual eligibility, or not dually eligible).\n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Dually Enrolled in Medicare. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.\n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/DualStatus-montly.csv",
+                    "mediaType": "text/csv",
                     "title": "Dual Status Information for Medicaid and CHIP Beneficiaries by Month"
                 }
             ],
+            "identifier": "36ed6909-ab49-4ca5-a38e-6790138cd613",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "dual enrollment",
+                "medicaid",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/5npy-pruv",
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
+            "title": "Dual Status Information for Medicaid and CHIP Beneficiaries by Month"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-29",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-24 & 2024-2025",
-            "modified": "2025-01-29",
-            "keyword": [
-                "covid-19 vaccination",
-                "iis",
-                "iqvia",
-                "nis",
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
-            "identifier": "https://data.cdc.gov/api/views/jjpx-mxt8",
             "description": "\u2022 Weekly Cumulative COVID-19 Vaccination Coverage, by Season and Race and Ethnicity, Medicare Fee-For-Service Beneficiaries, Adults aged 65 years and Older\n\n\u2022 COVID-19 vaccination coverage among Medicare fee-for-service beneficiaries aged 65 years and older is assessed using data files from the Medicare Fee-For-Service (FFS) administrative claims data managed by the Centers for Medicare & Medicaid Services (CMS).",
-            "title": "Weekly Cumulative COVID-19 Vaccination Coverage, by Season and Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16677,87 +16657,81 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/jjpx-mxt8",
+            "issued": "2025-01-29",
+            "keyword": [
+                "covid-19 vaccination",
+                "iis",
+                "iqvia",
+                "nis",
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
+            "temporal": "2023-24 & 2024-2025",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative COVID-19 Vaccination Coverage, by Season and Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://thebiogrid.org/",
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
                 "fn": "WATSON, HAROLD L.",
                 "hasEmail": "mailto:watsonh@mail.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "27788c47-c2ce-4f76-8462-573f505a557e",
+            "dataQuality": true,
             "description": "<p>BioGRID is an online interaction repository with data on raw protein and genetic interactions from major model organism species. All interaction data are freely provided through our search index and available via download in a wide variety of standardized formats.</p>",
-            "title": "Biological General Repository for Interaction Datasets (BioGRID)",
+            "identifier": "27788c47-c2ce-4f76-8462-573f505a557e",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://thebiogrid.org/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:046"
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
+            "title": "Biological General Repository for Interaction Datasets (BioGRID)"
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
-            "modified": "2024-04-09",
-            "references": [
-                "https://www.cdc.gov/dhdsp/index.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
-            ],
-            "keyword": [
-                "blood pressure",
-                "cardiovascular disease",
-                "cardiovascular health",
-                "cholesterol",
-                "cvd risk factors",
-                "hypertension",
-                "sodium"
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
-            "identifier": "https://data.cdc.gov/api/views/5svk-8bnq",
+            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/National-Health-and-Nutrition-Examination-Survey-N/5svk-8bnq",
             "description": "1999\u20132000 to 2017\u20132018. The National Health and Nutrition Examination Survey (NHANES) is a program of studies designed to assess the health and nutritional status of adults and children in the United States. The survey is unique in that it combines interviews and physical examinations. Indicators from this data source have been computed by personnel in CDC's Division for Heart Disease and Stroke Prevention (DHDSP). This was one of the datasets provided by the National Cardiovascular Disease Surveillance System and presented on DHDSP\u2019s Data, Trends, and Maps online tool. This tool was retired in April of 2024 and this dataset will not be updated. Contact dhdsprequests@cdc.gov if you need assistance with data previously included in this dataset. The data can be plotted as trends and stratified by age group, sex, and race/ethnicity.",
-            "title": "National Health and Nutrition Examination Survey (NHANES) - National Cardiovascular Disease Surveillance System",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16780,43 +16754,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/National-Health-and-Nutrition-Examination-Survey-N/5svk-8bnq",
+            "identifier": "https://data.cdc.gov/api/views/5svk-8bnq",
+            "issued": "2023-07-18",
+            "keyword": [
+                "blood pressure",
+                "cardiovascular disease",
+                "cardiovascular health",
+                "cholesterol",
+                "cvd risk factors",
+                "hypertension",
+                "sodium"
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
                 "Heart Disease & Stroke Prevention"
-            ]
+            ],
+            "title": "National Health and Nutrition Examination Survey (NHANES) - National Cardiovascular Disease Surveillance System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/adults-60-coverage-intent.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-08",
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
-            "identifier": "https://data.cdc.gov/api/views/qve4-fp9c",
             "description": "Weekly RSV Vaccination Coverage of Adults 60 Years and Older by Jurisdiction \n\n\u2022 RSV vaccination coverage among adults 60 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly RSV vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html) \n\n\u2022 The CDC recommended the RSV vaccine for adults 60 years and older in July 2023. (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)",
-            "title": "Weekly Cumulative Percentage of Adults 60 Years and Older Vaccinated with Respiratory Syncytial Virus (RSV) Vaccine by Jurisdiction",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16839,52 +16820,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/qve4-fp9c",
+            "issued": "2023-12-08",
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
+            "title": "Weekly Cumulative Percentage of Adults 60 Years and Older Vaccinated with Respiratory Syncytial Virus (RSV) Vaccine by Jurisdiction"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/97bc-2r74",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/97bc-2r74",
             "description": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease, Age <5 years, Serotype b - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease, Age <5 years, Serotype b",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16907,46 +16882,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/97bc-2r74",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
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
+            "landingPage": "https://data.cdc.gov/d/97bc-2r74",
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
+            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease, Age <5 years, Serotype b"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/snev-n7vb",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-            "identifier": "https://data.cdc.gov/api/views/snev-n7vb",
             "description": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Machupo virus to Viral hemorrhagic fevers, Sabia virus \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers\". NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
-            "title": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Machupo virus to Viral hemorrhagic fevers, Sabia virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16969,114 +16945,151 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/snev-n7vb",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "machupo virus",
+                "marburg virus",
+                "nedss",
+                "netss",
+                "nndss",
+                "sabia virus",
+                "viral hemorrhagic fevers",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/snev-n7vb",
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
+            "title": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Machupo virus to Viral hemorrhagic fevers, Sabia virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5t3b-dvvn",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-12-22",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-20",
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
-            "identifier": "d9fb4ebc-7ff5-5376-ae96-f7d08c294929",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard SELECTIONS v0.drew.2-test (local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.drew.2-test/20231116/SELECTIONS.csv",
-                    "description": "Scorecard SELECTIONS v0.drew.2-test (local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard SELECTIONS v0.drew.2-test (local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.drew.2-test/20231116/SELECTIONS.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard SELECTIONS v0.drew.2-test (local)"
                 }
             ],
+            "identifier": "d9fb4ebc-7ff5-5376-ae96-f7d08c294929",
+            "issued": "2023-12-22",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/5t3b-dvvn",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-12-20",
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
+            "title": "Scorecard SELECTIONS v0.drew.2-test (local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5t96-jsaw",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-03-29",
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
-            "identifier": "3f3a2024-8f74-5d4f-80d8-3ce4c1b72dce",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_footnotes",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/footnotes.csv",
-                    "description": "{\"dataset\": \"footnotes\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"footnotes\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/footnotes.csv",
+                    "mediaType": "text/csv",
                     "title": "footnotes csv file"
                 }
             ],
+            "identifier": "3f3a2024-8f74-5d4f-80d8-3ce4c1b72dce",
+            "issued": "2023-03-29",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/5t96-jsaw",
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
+            "title": "featAuto_footnotes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2011",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), to analyze general treatment services trends, and to generate the online Substance Abuse Treatment<br />\nFacility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>, as well as the National Directory of Drug and Alcohol Abuse Treatment Programs.Data are collected on topics including facility operation, services offered (assessment, testing, transitional, ancillary, and pharmacotherapies), detoxification, primary focus (substance abuse, mental health, both, general health, and other), Opioid Treatment Programs and medications dispensed/prescribed, counseling and therapeutic approaches, standard operating procedures, special programs/groups offered, languages in which treatment is provided, type of treatment provided (hospital inpatient, residential, outpatient), number of clients (by service, total, and under age 18), number of beds, types of payment accepted, sliding fee scale, and facility accreditation and licensure/certification.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2011) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2011-nid13565",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2011-nid13565"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2011-nid13565",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -17089,58 +17102,30 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2011",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2011-nid13565",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), to analyze general treatment services trends, and to generate the online Substance Abuse Treatment<br />\nFacility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>, as well as the National Directory of Drug and Alcohol Abuse Treatment Programs.Data are collected on topics including facility operation, services offered (assessment, testing, transitional, ancillary, and pharmacotherapies), detoxification, primary focus (substance abuse, mental health, both, general health, and other), Opioid Treatment Programs and medications dispensed/prescribed, counseling and therapeutic approaches, standard operating procedures, special programs/groups offered, languages in which treatment is provided, type of treatment provided (hospital inpatient, residential, outpatient), number of clients (by service, total, and under age 18), number of beds, types of payment accepted, sliding fee scale, and facility accreditation and licensure/certification.This study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2011)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2011-nid13565",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2011) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2011-nid13565"
-                }
-            ]
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2011)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5tbn-ibkm",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-10-07",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
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
-            "identifier": "a54d7605-b780-4cf0-b53d-50313798f528",
             "description": "Exclusively Pediatric (EP) designation allows for a minimum rebate percentage of 17.1 percent of Average Manufacturer Price (AMP) for single source and innovator multiple source drugs.",
-            "title": "Exclusive Pediatric Drugs",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17148,44 +17133,35 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "a54d7605-b780-4cf0-b53d-50313798f528",
+            "issued": "2022-10-07",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/5tbn-ibkm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Exclusive Pediatric Drugs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/d6kj-devz",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
-            "keyword": [
-                "2015",
-                "congenital syndrome",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "rubella",
-                "salmonellosis",
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
-            "identifier": "https://data.cdc.gov/api/views/d6kj-devz",
             "description": "NNDSS - Table II. Rubella to Salmonellosis - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Rubella to Salmonellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17208,43 +17184,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/d6kj-devz",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
+                "congenital syndrome",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "rubella",
+                "salmonellosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/d6kj-devz",
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
+            "title": "NNDSS - Table II. Rubella to Salmonellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-29",
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
-            "identifier": "https://data.cdc.gov/api/views/3bmy-cyyd",
             "description": "\u2022 Monthly Cumulative Percent of Persons Who Received 1+ 2024-25 COVID-19 Vaccination Doses, by Age Group and Jurisdiction \n\n\u2022 COVID-19 vaccination coverage for children and adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems Resources (IIS) data, submitted from jurisdictions to CDC monthly in aggregate by age group (https://www.cdc.gov/iis/about/).",
-            "title": "Monthly Cumulative Number and Percent of Persons Who Received 1+ 2024-25 COVID-19 Vaccination Doses, by Age Group, and Jurisdiction, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17267,50 +17247,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/3bmy-cyyd",
+            "issued": "2025-01-29",
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
+            "title": "Monthly Cumulative Number and Percent of Persons Who Received 1+ 2024-25 COVID-19 Vaccination Doses, by Age Group, and Jurisdiction, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/nis/",
+            "accrualPeriodicity": "Approximately Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-17",
-            "@type": "dcat:Dataset",
-            "temporal": "Monthly",
-            "modified": "2024-05-24",
-            "keyword": [
-                "adults",
-                "ethnicity",
-                "flu",
-                "flu vaccination",
-                "race",
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
-            "identifier": "https://data.cdc.gov/api/views/v22g-tzpk",
             "description": "Differences in Cumulative Influenza Vaccination Coverage by Selected Demographics, Adults 18 Year and Older, NIS Adult COVID Module\n\n\u2022 The National Immunization Survey-Adult COVID Module (NIS-ACM) was launched in April 2021 among adults 18 years and older. The survey was used to monitor COVID-19 vaccination uptake and confidence in vaccination among adults and included questions about influenza vaccination.",
-            "title": "Differences in Cumulative Influenza Vaccination Coverage by Selected Demographics, Adults 18 Year and Older, NIS Adult COVID Module",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17333,29 +17311,60 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, District of Columbia, US Virgin Islands, and Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/v22g-tzpk",
+            "issued": "2023-11-17",
+            "keyword": [
+                "adults",
+                "ethnicity",
+                "flu",
+                "flu vaccination",
+                "race",
+                "vaccination",
+                "vaccine coverage"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/nis/",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Approximately Monthly",
+            "modified": "2024-05-24",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States, District of Columbia, US Virgin Islands, and Puerto Rico",
+            "temporal": "Monthly",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Differences in Cumulative Influenza Vaccination Coverage by Selected Demographics, Adults 18 Year and Older, NIS Adult COVID Module"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.hcup-us.ahrq.gov/db/state/siddbdocumentation.jsp",
             "bureauCode": [
                 "009:33"
             ],
-            "rights": "N/A",
-            "issued": "2021-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "references": [
-                "https://www.hcup-us.ahrq.gov/db/state/siddbdocumentation.jsp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HCUP Technical Support",
+                "hasEmail": "mailto:hcup@ahrq.gov"
+            },
+            "describedBy": "https://www.hcup-us.ahrq.gov/db/state/siddist/siddist_ddeavailbyyear.jsp",
+            "description": "The Healthcare Cost and Utilization Project (HCUP) State Inpatient Databases (SID) are a set of hospital databases that contain the universe of hospital inpatient discharge abstracts from data organizations in participating States. The data are translated into a uniform format to facilitate multi-State comparisons and analyses. The SID are based on data from short term, acute care, nonfederal hospitals. Some States include discharges from specialty facilities, such as acute psychiatric hospitals. The SID include all patients, regardless of payer and contain clinical and resource use information included in a typical discharge abstract, with safeguards to protect the privacy of individual patients, physicians, and hospitals (as required by data sources). Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality (AHRQ), HCUP data inform decision making at the national, State, and community levels.\n\nThe SID contain clinical and resource-use information that is included in a typical discharge abstract, with safeguards to protect the privacy of individual patients, physicians, and hospitals (as required by data sources). Data elements include but are not limited to: diagnoses, procedures, admission and discharge status, patient demographics (e.g., gender, age), total charges, length of stay, and expected payment source, including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge\u2019. In addition to the core set of uniform data elements common to all SID, some include State-specific data elements. The SID exclude data elements that could directly or indirectly identify individuals. For some States, hospital and county identifiers are included that permit linkage to the American Hospital Association Annual Survey File and county-level data from the Bureau of Health Professions' Area Resource File except in States that do not allow the release of hospital identifiers.\n\nRestricted access data files are available with a data use agreement and brief online security training.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.hcup-us.ahrq.gov/db/state/siddbdocumentation.jsp",
+                    "mediaType": "text/html",
+                    "title": "HCUP State Inpatient Databases (SID)"
+                }
             ],
+            "identifier": "6ae52fd4-6ac1-4c36-938c-9f57a36ed812",
+            "issued": "2021-02-13",
             "keyword": [
                 "claims",
                 "community health",
@@ -17371,74 +17380,38 @@
                 "procedures",
                 "utilization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HCUP Technical Support",
-                "hasEmail": "mailto:hcup@ahrq.gov"
-            },
+            "landingPage": "https://www.hcup-us.ahrq.gov/db/state/siddbdocumentation.jsp",
+            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
             },
-            "identifier": "6ae52fd4-6ac1-4c36-938c-9f57a36ed812",
-            "description": "The Healthcare Cost and Utilization Project (HCUP) State Inpatient Databases (SID) are a set of hospital databases that contain the universe of hospital inpatient discharge abstracts from data organizations in participating States. The data are translated into a uniform format to facilitate multi-State comparisons and analyses. The SID are based on data from short term, acute care, nonfederal hospitals. Some States include discharges from specialty facilities, such as acute psychiatric hospitals. The SID include all patients, regardless of payer and contain clinical and resource use information included in a typical discharge abstract, with safeguards to protect the privacy of individual patients, physicians, and hospitals (as required by data sources). Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality (AHRQ), HCUP data inform decision making at the national, State, and community levels.\n\nThe SID contain clinical and resource-use information that is included in a typical discharge abstract, with safeguards to protect the privacy of individual patients, physicians, and hospitals (as required by data sources). Data elements include but are not limited to: diagnoses, procedures, admission and discharge status, patient demographics (e.g., gender, age), total charges, length of stay, and expected payment source, including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge\u2019. In addition to the core set of uniform data elements common to all SID, some include State-specific data elements. The SID exclude data elements that could directly or indirectly identify individuals. For some States, hospital and county identifiers are included that permit linkage to the American Hospital Association Annual Survey File and county-level data from the Bureau of Health Professions' Area Resource File except in States that do not allow the release of hospital identifiers.\n\nRestricted access data files are available with a data use agreement and brief online security training.",
-            "title": "HCUP State Inpatient Databases (SID) - Restricted Access File",
-            "programCode": [
-                "009:072"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.hcup-us.ahrq.gov/db/state/siddbdocumentation.jsp",
-                    "mediaType": "text/html",
-                    "title": "HCUP State Inpatient Databases (SID)"
-                }
+            "references": [
+                "https://www.hcup-us.ahrq.gov/db/state/siddbdocumentation.jsp"
             ],
-            "describedBy": "https://www.hcup-us.ahrq.gov/db/state/siddist/siddist_ddeavailbyyear.jsp",
-            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx",
+            "rights": "N/A",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "HCUP State Inpatient Databases (SID) - Restricted Access File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ch5i-63ve",
+            "accrualPeriodicity": "Never",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-12-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-23 and 2023-24 respiratory illness seasons (2 October 2022 through 31 August 2024; data from last 5 weeks of 2023-24 season not available)",
-            "modified": "2024-12-26",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "emergency department",
-                "flu",
-                "influenza",
-                "ncird",
-                "ncird-corvd",
-                "ncird-id",
-                "respiratory disease",
-                "respiratory syncytial virus",
-                "rsv",
-                "sars-cov-2"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RESP-LENS",
                 "hasEmail": "mailto:bkw7@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ch5i-63ve",
             "description": "During the 2022-23 and 2023-24 respiratory illness seasons, the Respiratory Virus Laboratory Emergency Department Network Surveillance (RESP-LENS) system gathered electronic health record (EHR) data from nearly 100 hospitals associated with 24 participating sites located in 20 states and the District of Columbia. There was at least one site in each of the 10 Health and Human Services (HHS) regions. RESP-LENS collected reports of emergency department (ED) visits for acute respiratory illness (ARI) and corresponding viral testing results for SARS-CoV-2 (the virus that causes COVID-19), influenza (flu), and respiratory syncytial virus (RSV).  Sites reported data for an average of approximately 77,000 ED visits weekly, of which 11,000 were associated with ARI and 4,000 of those were in children younger than 18 years.  Between May 2023 and August 2024, these data were posted to CDC's RESP-LENS public dashboard, showing number tested, number positive, and percent positive for each of the three viruses mentioned, by virus, region, and age group.  Due to budget constraints, RESP-LENS was not funded beyond the end of the 2024 fiscal year.  RESP-LENS served as a valuable tool for public health and health care professionals and allowed users to visualize and understand trends in virus circulation, estimate disease burden, respond to outbreaks, and inform decisions and strategies for protecting public health.",
-            "title": "RESP-LENS",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17461,44 +17434,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "24 sites/health systems with a total of >100 participating hospitals located in 20 states and the District of Columbia",
+            "identifier": "https://data.cdc.gov/api/views/ch5i-63ve",
+            "issued": "2024-12-23",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "emergency department",
+                "flu",
+                "influenza",
+                "ncird",
+                "ncird-corvd",
+                "ncird-id",
+                "respiratory disease",
+                "respiratory syncytial virus",
+                "rsv",
+                "sars-cov-2"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ch5i-63ve",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Never",
+            "modified": "2024-12-26",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "24 sites/health systems with a total of >100 participating hospitals located in 20 states and the District of Columbia",
+            "temporal": "2022-23 and 2023-24 respiratory illness seasons (2 October 2022 through 31 August 2024; data from last 5 weeks of 2023-24 season not available)",
             "theme": [
                 "National Center for Immunization and Respiratory Diseases"
-            ]
+            ],
+            "title": "RESP-LENS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5ubv-4ab6",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-08-10",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-17",
-            "keyword": [
-                "py2022",
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
-            "identifier": "66b55b41-152e-44c2-9727-158401c2e526",
             "description": "The Dental SHOP Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2022 Dental SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17506,46 +17487,47 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "66b55b41-152e-44c2-9727-158401c2e526",
+            "issued": "2022-08-10",
+            "keyword": [
+                "py2022",
+                "qhp landscape instructions",
+                "sadp",
+                "shop",
+                "shop market dental"
+            ],
+            "landingPage": "https://healthdata.gov/d/5ubv-4ab6",
+            "modified": "2022-08-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2022 Dental SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/quality-of-care/minimum-data-set-frequency",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-08-22",
-            "temporal": "2020-01-01/2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-09",
-            "references": [
-                "https://data.cms.gov/resources/minimum-data-set-frequency-methodology"
-            ],
-            "keyword": [
-                "medicaid",
-                "medicare"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Minimum Data Set Frequency - CCSQ",
                 "hasEmail": "mailto:iqies@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/4b50bbe6-a496-4eda-b03b-5f835937f81b/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/minimum-data-set-frequency-data-dictionary",
             "description": "The Minimum Data Set (MDS) Frequency data summarizes health status indicators for active residents currently in nursing homes. The MDS is part of the Federally-mandated process for clinical assessment of all residents in Medicare and Medicaid certified nursing homes. This process provides a comprehensive assessment of each resident's functional capabilities and helps nursing home staff identify health problems. Care Area Assessments (CAAs) are part of this process, and provide the foundation upon which a resident's individual care plan is formulated. MDS assessments are completed for all residents in certified nursing homes, regardless of source of payment for the individual resident. MDS assessments are required for residents on admission to the nursing facility, periodically, and on discharge. All assessments are completed within specific guidelines and time frames. In most cases, participants in the assessment process are licensed health care professionals employed by the nursing home. MDS information is transmitted electronically by nursing homes to the national MDS database at CMS.\n\n\u00a0\n\nWhen reviewing the MDS 3.0 Frequency files, some common software programs e.g., \u2018Microsoft Excel\u2019 might inaccurately strip leading zeros from designated code values (i.e., \"01\" becomes \"1\") or misinterpret code ranges as dates (i.e., O0600 ranges such as 02-04 are misread as 04-Feb). As each piece of software is unique, if you encounter an issue when reading the CSV file of Frequency data, please open the file in a plain text editor such as \u2018Notepad\u2019 or \u2018TextPad\u2019 to review the underlying data, before reaching out to CMS for assistance.",
-            "title": "Minimum Data Set Frequency",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4b50bbe6-a496-4eda-b03b-5f835937f81b/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4b50bbe6-a496-4eda-b03b-5f835937f81b/data",
+                    "mediaType": "text/html",
                     "title": "Minimum Data Set Frequency : 2024-09-01"
                 },
                 {
@@ -17777,42 +17759,47 @@
                     "title": "Minimum Data Set Frequency : 2020-01-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/minimum-data-set-frequency-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/4b50bbe6-a496-4eda-b03b-5f835937f81b/data-viewer",
+            "issued": "2023-08-22",
+            "keyword": [
+                "medicaid",
+                "medicare"
+            ],
+            "landingPage": "https://data.cms.gov/quality-of-care/minimum-data-set-frequency",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-10-09",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/minimum-data-set-frequency-methodology"
+            ],
+            "temporal": "2020-01-01/2024-09-30",
             "theme": [
                 "Medicare",
                 "Medicaid"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Minimum Data Set Frequency"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/w6be-99qd",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-02-01",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-23",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Surveillance and Epidemiology Branch, Immunization Services Division, NCIRD, CDC",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/w6be-99qd",
             "description": "These weekly COVID-19 vaccination coverage estimates are for pregnant persons who are fully vaccinated before and during pregnancy based on data  from the Vaccine Safety Datalink*.",
-            "title": "Weekly Data: COVID-19 vaccination among pregnant people ages 18-49 years before and during pregnancy overall, by race/ethnicity, and week ending date - Vaccine Safety Datalink,* United States",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17835,54 +17822,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/w6be-99qd",
+            "issued": "2022-02-01",
+            "landingPage": "https://data.cdc.gov/d/w6be-99qd",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-06-23",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Pregnancy & Vaccination"
-            ]
+            ],
+            "title": "Weekly Data: COVID-19 vaccination among pregnant people ages 18-49 years before and during pregnancy overall, by race/ethnicity, and week ending date - Vaccine Safety Datalink,* United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/5jdf-gdqh",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "data distribution",
-                "dataset",
-                "drugs",
-                "images"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/5jdf-gdqh",
             "description": "The Computational Photography Project for Pill Identification (C3PI) was sunset in 2018. No new images will be added to the collection. Identifiers for pills will not be updated.  Images and metadata are for research and development purposes only.\n\nThe Computational Photography Project for Pill Identification (C3PI) created the RxIMAGE database of freely available high-quality digital images of prescription pills and associated data for use in conducting computer vision research in text- and image-based search and retrieval. Photographs of pills for the RxIMAGE database were taken under laboratory lighting conditions, from a camera directly above the front and the back faces of the pill, at high resolution, and using specialized digital macro-photography techniques. Image segmentation algorithms were then applied to create the JPEG images in the database.\n\nHistorical information about the project is available in the NLM archive at https://wayback.archive-it.org/7867/20190423182937/https:/lhncbc.nlm.nih.gov/project/c3pi-computational-photography-project-pill-identification.",
-            "title": "Computational Photography Project for Pill Identification (C3PI)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Pills/rximage.zip",
-                    "description": "4,000 reference pill images taken under controlled light conditions",
                     "@type": "dcat:Distribution",
+                    "description": "4,000 reference pill images taken under controlled light conditions",
+                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Pills/rximage.zip",
+                    "mediaType": "text/html",
                     "title": "Download C3PI Reference Images (6.8GB zip file)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Pills/index.html",
-                    "description": "133,000 consumer-grade pill images for training pill image recognition algorithms as well as additional project support files",
                     "@type": "dcat:Distribution",
+                    "description": "133,000 consumer-grade pill images for training pill image recognition algorithms as well as additional project support files",
+                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Pills/index.html",
+                    "mediaType": "text/html",
                     "title": "Download C3PI Training Images"
                 },
                 {
@@ -17892,38 +17873,42 @@
                     "title": "Download C3PI Sample Data (493MB zip file)"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/5jdf-gdqh",
+            "issued": "2020-08-06",
+            "keyword": [
+                "data distribution",
+                "dataset",
+                "drugs",
+                "images"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/5jdf-gdqh",
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
+            "title": "Computational Photography Project for Pill Identification (C3PI)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5vjr-nzpw",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2017-12-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-16",
-            "keyword": [
-                "medicaid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeff Chamblee",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "5394bcab-c748-5e4b-af07-b5bf77ed3aa3",
             "description": "1. Enrollment includes both Medicaid-only and Medicare-Medicaid (\u201cdual\u201d) enrollees. For both types of enrollees, Medicaid covers LTSS. For dual enrollees, Medicaid may also cover Medicare cost-sharing for acute, primary care, and specialty services covered by Medicare, and other non-LTSS services that are not covered by Medicare.\t\t\t\t\t\r\n2. Some comprehensive managed care programs enroll beneficiaries who may be at risk of needing LTSS but do not receive any LTSS. These counts only include individuals that receive LTSS. Moreover, states differ in their ability to report individuals who use MLTSS versus those who are enrolled (and may or may not be using LTSS). This table reports MLTSS users unless otherwise noted. \t\t\t\t\t\r\n3. Comprehensive Managed Care Including LTSS does not include PACE programs.\t\t\t\t\t\r\n4. MLTSS Only programs cover LTSS under capitation; acute, primary, and specialty care services for these enrollees may be covered by another Medicaid MCO, Medicaid FFS, or by Medicare for dual enrollees. These data include states that provide MLTSS plus other benefits in a package that does not include inpatient medical care.\t\t\t\t\t\r\n5. The indicated territory was not able to supply data for this report. The Northern Mariana Islands reported that they have no Medicaid managed care enrollment, but they did not report total Medicaid enrollees.\r\n6. Enrollment and user counts include both Medicaid-only enrollees and dually eligible individuals. For both types of enrollees, Medicaid covers LTSS. For dually eligible individuals, Medicaid may also cover Medicare cost-sharing for acute, primary care, and specialty services covered by Medicare, and other non-LTSS services that are not covered by Medicare.\r\n7. The \u201cComprehensive Managed Care Including LTSS\u201d column does not include PACE programs.\r\n8. Columns indicating the \"Number of enrollees using LTSS\" reflect what states reported. In addition to the three states that reported LTSS users (Arizona, New York and Wisconsin), California and Delaware also offer LTSS services in a stand-alone program.\r\n9. Note: \"n/a\" indicates that a state or territory was not able to report data or does not have a managed care program. \"--\" indicates that a state or territory does not operate programs of the type listed in the column heading. Enrollment and user counts include both Medicaid-only and dually eligible individuals. For both types of enrollees, Medicaid covers LTSS. For dually eligible individuals, Medicaid may also cover Medicare cost-sharing for acute, primary care, and specialty services covered by Medicare and other non-LTSS services that are not covered by Medicare.\r\n10. Columns indicating the \"Number of enrollees using LTSS\" reflect what states reported. In addition to the three states that reported LTSS users (Arizona, New York and Wisconsin), California and Delaware also offer LTSS services in a stand-alone program.",
-            "title": "Managed Long Term Services and Supports (MLTSS) Enrollees",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17932,87 +17917,84 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "5394bcab-c748-5e4b-af07-b5bf77ed3aa3",
+            "issued": "2017-12-09",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/5vjr-nzpw",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-10-16",
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
+            "title": "Managed Long Term Services and Supports (MLTSS) Enrollees"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5vvw-rrpa",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-05-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
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
-            "identifier": "c4bfc9fa-9248-5500-bcd6-07a471c8e959",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard MEASURE vCORESET.1.1-test (coreset-local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/CORESET.1.1-test/20240430/MEASURE.csv",
-                    "description": "Scorecard MEASURE vCORESET.1.1-test (coreset-local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard MEASURE vCORESET.1.1-test (coreset-local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/CORESET.1.1-test/20240430/MEASURE.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard MEASURE vCORESET.1.1-test (coreset-local)"
                 }
             ],
+            "identifier": "c4bfc9fa-9248-5500-bcd6-07a471c8e959",
+            "issued": "2024-05-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/5vvw-rrpa",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-05-07",
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
+            "title": "Scorecard MEASURE vCORESET.1.1-test (coreset-local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/Structure/cdtree/cdtree.shtml",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-08",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vkhf-hsp7",
             "description": "CDTree is a stand-alone application for classifying protein sequences and investigating their evolutionary relationships. CDTree can import, analyze and update existing Conserved Domain (CDD) records and hierarchies, and also allows users to create their own.",
-            "title": "CDTree",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18021,84 +18003,87 @@
                     "title": "CDTree Homepage and Application Download"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vkhf-hsp7",
+            "issued": "2021-06-30",
+            "keyword": [
+                "dataset",
+                "protein",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/Structure/cdtree/cdtree.shtml",
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
+            "title": "CDTree"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5wke-dyve",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-03-28",
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
-            "identifier": "79953b14-7831-55e3-826e-e536e797c75c",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard filters v2.11.16 (dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/filters.csv",
-                    "description": "Scorecard filters v2.11.16 (dev)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard filters v2.11.16 (dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard filters v2.11.16 (dev)"
                 }
             ],
+            "identifier": "79953b14-7831-55e3-826e-e536e797c75c",
+            "issued": "2023-03-28",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/5wke-dyve",
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
+            "title": "Scorecard filters v2.11.16 (dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5wmq-82nv",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2018-07-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-16",
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
-            "identifier": "a6d2c261-210d-587c-8fa4-892444b7de42",
             "description": "Number of Managed Care Program Types, by Quality Assurance Requirements, Performance Incentives, and Provider Value-Based Purchasing Status, at any point in 2022",
-            "title": "Managed Care Features by QA and Performance Incentive",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18107,51 +18092,39 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "a6d2c261-210d-587c-8fa4-892444b7de42",
+            "issued": "2018-07-11",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/5wmq-82nv",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-10-16",
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
+            "title": "Managed Care Features by QA and Performance Incentive"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual (R/P1Y)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-07-29",
-            "temporal": "1988/2020",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "female",
-                "health care use",
-                "health us",
-                "hispanic",
-                "male",
-                "mexican",
-                "national health and nutrition examination survey",
-                "non-hispanic asian",
-                "non-hispanic white",
-                "prescription drugs",
-                "prescriptions",
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
-            "identifier": "https://data.cdc.gov/api/views/b666-c5v5",
             "description": "Data on prescription drug use in the past 30 days in the United States, by sex, race and Hispanic origin, and age group. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Health and Nutrition Examination Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Prescription drug use in the past 30 days, by sex, race and Hispanic origin, and age group: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18174,39 +18147,50 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/b666-c5v5",
+            "issued": "2024-07-29",
+            "keyword": [
+                "female",
+                "health care use",
+                "health us",
+                "hispanic",
+                "male",
+                "mexican",
+                "national health and nutrition examination survey",
+                "non-hispanic asian",
+                "non-hispanic white",
+                "prescription drugs",
+                "prescriptions",
+                "sdoh-use-of-health-care"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual (R/P1Y)",
+            "modified": "2024-11-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "1988/2020",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "DQS Prescription drug use in the past 30 days, by sex, race and Hispanic origin, and age group: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/smai-7mz9",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-03-05",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "lyme"
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
-            "identifier": "https://data.cdc.gov/api/views/smai-7mz9",
             "description": "To facilitate the public health and research community's access to NNDSS data on Lyme disease, CDC has developed a public use dataset. Based on reports submitted to CDC, this dataset provides the number of confirmed cases by county for the years 1992\ufffd\ufffd\ufffd2011, in four 5\ufffd\ufffd\ufffdyear intervals. County tabulation is by American National Standard Institute (ANSI) [formerly Federal Information Processing Standard (FIPS)] codes. County codes of \"0\" represent \"unknown\" county of residence within each state. More recent county-level case counts are not publicly available at this time.",
-            "title": "LymeDisease_9211_county",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18229,47 +18213,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/smai-7mz9",
+            "issued": "2015-03-05",
+            "keyword": [
+                "lyme"
+            ],
+            "landingPage": "https://data.cdc.gov/d/smai-7mz9",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2015-08-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "LymeDisease_9211_county"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/physiciansupplier-procedure-summary",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2010-01-01/2023-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-21",
-            "references": [
-                "https://data.cms.gov/resources/physician-supplier-procedure-summary-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "medicare",
-                "original medicare"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CMS EDG Data Questions - OIT",
                 "hasEmail": "mailto:CMSEDG_DataRequests_Intake@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/164fc736-4179-4100-9f79-592b69e41975/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/physician-supplier-procedure-summary-data-dictionary",
             "description": "The Physician/Supplier Procedure Summary (PSPS) data provides a summary of calendar year Medicare Part B carrier and durable medical equipment fee-for-service (FFS) claims. The file is organized by carrier, pricing locality, Healthcare Common Procedure Coding System (HCPCS) code, HCPCS modifier, provider specialty, type of service, and place of service. The summarized fields are total submitted services and charges, total allowed services and charges, total denied services and charges, and total payment amounts.\u00a0 This dataset is produced annually and is typically available in July (i.e., data for CY2015 is usually available in July 2016).\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Physician/Supplier Procedure Summary",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/164fc736-4179-4100-9f79-592b69e41975/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/164fc736-4179-4100-9f79-592b69e41975/data",
+                    "mediaType": "text/html",
                     "title": "Physician/Supplier Procedure Summary : 2023-01-01"
                 },
                 {
@@ -18441,87 +18422,87 @@
                     "title": "Physician/Supplier Procedure Summary : 2010-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/physician-supplier-procedure-summary-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/164fc736-4179-4100-9f79-592b69e41975/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "medicare",
+                "original medicare"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/physiciansupplier-procedure-summary",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-08-21",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/physician-supplier-procedure-summary-methodology"
+            ],
+            "temporal": "2010-01-01/2023-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Physician/Supplier Procedure Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5y7s-i72b",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-05-10",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-09",
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
-            "identifier": "b3520474-b2d6-40ce-a185-5111cda9bdc5",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-01-to-2023-05-07",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-5-01-2023-to-5-07-2023.csv",
-                    "description": " https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-5-01-2023-to-5-07-2023.csv",
                     "@type": "dcat:Distribution",
+                    "description": " https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-5-01-2023-to-5-07-2023.csv",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-5-01-2023-to-5-07-2023.csv",
+                    "mediaType": "text/csv",
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-01-to-2023-05-07"
                 }
             ],
+            "identifier": "b3520474-b2d6-40ce-a185-5111cda9bdc5",
+            "issued": "2023-05-10",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/5y7s-i72b",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-05-09",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-01-to-2023-05-07"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5ymz-5cum",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-05",
-            "keyword": [
-                "behavioral health care",
-                "chip",
-                "integrated care",
-                "medicaid",
-                "substance use disorder physical health condition"
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
-            "identifier": "ac553cd4-63eb-44d4-9946-f29c0ccc1838",
             "description": "This table presents beneficiaries who received a service for a physical health condition among beneficiaries who received a service for a substance use disorder, by physical health condition, 2017-2021.\r\n\r\nSome states have serious data quality issues, making the data unusable for identifying this population. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional, Gender, Age, Zip code, Race and ethnicity, Eligibility group code, Enrollment in CMC Plans. \r\n\r\nData from Maryland, Tennessee, and Utah are omitted for the tables due to data quality concerns. Maryland was excluded in 2017 due to unusable diagnosis codes in the IP file and the OT file. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2020. In addition, states with a high data quality concern on one or more measures are noted in the table in the \"Data Quality\" column. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Beneficiaries receiving a physical health service among beneficiaries receiving a SUD service by physical health cond, 2017-2021",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18530,90 +18511,89 @@
                     "title": "Beneficiaries receiving a physical health service among beneficiaries receiving a SUD service by physical health cond, 2017-2021"
                 }
             ],
+            "identifier": "ac553cd4-63eb-44d4-9946-f29c0ccc1838",
+            "issued": "2023-03-28",
+            "keyword": [
+                "behavioral health care",
+                "chip",
+                "integrated care",
+                "medicaid",
+                "substance use disorder physical health condition"
+            ],
+            "landingPage": "https://healthdata.gov/d/5ymz-5cum",
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
+            "title": "Beneficiaries receiving a physical health service among beneficiaries receiving a SUD service by physical health cond, 2017-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/5yvt-yp32",
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
-            "identifier": "4a9e6829-475e-53e4-9f8e-4070ec39bdf1",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt version v2.10.22 (coreset-impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/version.csv",
-                    "description": "CoreSEt version v2.10.22 (coreset-impl)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt version v2.10.22 (coreset-impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/version.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt version v2.10.22 (coreset-impl)"
                 }
             ],
+            "identifier": "4a9e6829-475e-53e4-9f8e-4070ec39bdf1",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/5yvt-yp32",
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
+            "title": "CoreSEt version v2.10.22 (coreset-impl)"
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
-                "preemption",
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
-            "identifier": "https://data.cdc.gov/api/views/piju-vf3p",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Preemptio/piju-vf3p",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  E-Cigarette Legislation\u2014Preemption. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies.  Data are reported on a quarterly basis. Data include information related to statutory state preemption of more stringent local laws on advertising, smokefree indoor air, youth access and licensure.",
-            "title": "CDC STATE System E-Cigarette Legislation - Preemption",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18636,52 +18616,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Preemptio/piju-vf3p",
+            "identifier": "https://data.cdc.gov/api/views/piju-vf3p",
+            "issued": "2023-07-18",
+            "keyword": [
+                "e-cigarette",
+                "legislation",
+                "osh",
+                "policy",
+                "preemption",
+                "state system"
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
+            "title": "CDC STATE System E-Cigarette Legislation - Preemption"
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
-                "city",
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
-            "identifier": "https://data.cdc.gov/api/views/q8ig-wwk9",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
             "description": "This dataset contains model-based place (incorporated and census designated places) level estimates for the PLACES 2021 release. PLACES is the expansion of the original 500 Cities Project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. The dataset includes estimates for 29 measures: 4 chronic disease-related risk behaviors, 13 health outcomes, 3 health status, and 9 on using preventive services. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2010 population data, and American Community Survey (ACS) 2015\u20132019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS because the relevant questions are only asked every other year in the BRFSS. More information about the methodology can be found at  www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, Place Data 2021 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18704,53 +18676,60 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
+            "identifier": "https://data.cdc.gov/api/views/q8ig-wwk9",
+            "issued": "2022-10-11",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "city",
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
+            "title": "PLACES: Local Data for Better Health, Place Data 2021 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/alternative-payments-medicare-diabetes-prevention-program/medicare-diabetes-prevention-program",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2025-01-01/2025-03-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-10",
-            "references": [
-                "https://data.cms.gov/resources/medicare-diabetes-prevention-program-methodology"
-            ],
-            "keyword": [
-                "medicare",
-                "medicare advantage",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/a15c198e-4cf3-46ab-a30e-15c69bd13edd/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-diabetes-prevention-program-data-dictionary",
             "description": "The Medicare Diabetes Prevention Program dataset contains information about suppliers from which eligible Medicare beneficiaries may be furnished associated services. The information in this dataset can include organization name, location, contact information, National Provider Identifier (NPI) among other data points. Location data populates the \"Map of MDPP Suppliers furnishing MDPP Services\" map.",
-            "title": "Medicare Diabetes Prevention Program",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a15c198e-4cf3-46ab-a30e-15c69bd13edd/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a15c198e-4cf3-46ab-a30e-15c69bd13edd/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Diabetes Prevention Program : 2025-01-10"
                 },
                 {
@@ -18766,44 +18745,50 @@
                     "title": "Medicare Diabetes Prevention Program : 2025-01-10"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-diabetes-prevention-program-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/a15c198e-4cf3-46ab-a30e-15c69bd13edd/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/alternative-payments-medicare-diabetes-prevention-program/medicare-diabetes-prevention-program",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2025-01-10",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-diabetes-prevention-program-methodology"
+            ],
+            "temporal": "2025-01-01/2025-03-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Diabetes Prevention Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/625f-fyt3",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2018-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-24",
-            "keyword": [
-                "medicaid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeff Chamblee",
                 "hasEmail": "mailto:no-reply@data.medicaid.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "c491f14b-6dd5-5e00-9e8d-0c49420e7caa",
             "description": "Federal law requires that state Medicaid programs make Disproportionate Share Hospital (DSH) payments to qualifying hospitals that serve a large number of Medicaid and uninsured individuals. State-specific annual DSH reports are posted as submitted by states based on their availability.\r\n\r\nFor more information, visit https://www.medicaid.gov/medicaid/finance/dsh/index.html.",
-            "title": "Disproportionate Share Hospital (DSH) Payments - Annual Reporting Requirements",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18812,36 +18797,38 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "c491f14b-6dd5-5e00-9e8d-0c49420e7caa",
+            "issued": "2018-01-18",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/625f-fyt3",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2019-01-24",
+            "programCode": [
+                "009:076"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Disproportionate Share Hospital (DSH) Payments - Annual Reporting Requirements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/aeq9-xksa",
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
-            "identifier": "https://data.cdc.gov/api/views/aeq9-xksa",
             "description": "Nanomaterials represent a new class of materials with numerous industrial applications. Considering the projected increase in the production and use of nanomaterials, a corresponding increase in occupational exposure to nanomaterials and their resulting adverse health effects should be anticipated among workers. There is substantial evidence in the literature, based on cell culture and animal studies, supporting the potential toxicity and detrimental health effects associated with exposure to nanomaterials. Intervention and/or prevention of adverse health effects associated with occupational exposure to toxic nanomaterials will be a major concern for health providers and regulatory and non-regulatory government agencies as the use of nanomaterials expand. A key element in the intervention and/or prevention of the adverse health effects associated with occupational exposure to toxic nanomaterials is a clear understanding of the molecular mechanisms underlying the pulmonary toxicity induced by nanomaterials.\n\nDue to its physicochemical and mechanical properties, nanocellulose has found many applications in manufactured goods in the paper and food industry, cosmetics, biomedicine, and pharmaceuticals. There is potential for human exposure to nanocellulose or products that contain nanocellulose both during the production and use of the materials that contain nanocellulose. The objectives of the current study were to determine lung toxicity potential of crystalline nanocellulose (CNC) and the molecular mechanisms underlying the toxicity. A rat inhalation exposure model was employed to determine the lung toxicity potential of CNC. Global gene expression profile in the lung and bioinformatic analysis of the gene expression data were conducted to determine the molecular mechanisms underlying the CNC-induced lung toxicity.",
-            "title": "Lung toxicity and gene expression changes in response to whole-body inhalation exposure to cellulose nanocrystal in rats",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18849,42 +18836,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/aeq9-xksa",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/aeq9-xksa",
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
+            "title": "Lung toxicity and gene expression changes in response to whole-body inhalation exposure to cellulose nanocrystal in rats"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/62ju-7phz",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-14",
-            "keyword": [
-                "individual",
-                "individual market dental",
-                "py2024",
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
-            "identifier": "6b755d82-519a-4b5c-b04d-04013c1a2d9c",
             "description": "The Dental Individual Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to consumers in the individual market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2024 Individual Dental",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18892,47 +18873,39 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "6b755d82-519a-4b5c-b04d-04013c1a2d9c",
+            "issued": "2024-08-06",
+            "keyword": [
+                "individual",
+                "individual market dental",
+                "py2024",
+                "qhp landscape instructions",
+                "sadp"
+            ],
+            "landingPage": "https://healthdata.gov/d/62ju-7phz",
+            "modified": "2024-08-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2024 Individual Dental"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-05-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-12",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
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
-            "identifier": "https://data.cdc.gov/api/views/vsak-wrfu",
             "description": "Effective June 28, 2023, this dataset will no longer be updated. Similar data are accessible from CDC WONDER (https://wonder.cdc.gov/mcd-icd10-provisional.html).\n\nDeaths involving COVID-19 reported to NCHS by sex and age group and week ending date.",
-            "title": "Provisional COVID-19 Deaths by Week, Sex, and Age",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18955,40 +18928,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/vsak-wrfu",
+            "issued": "2020-05-15",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "sex",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-07-12",
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
+            "title": "Provisional COVID-19 Deaths by Week, Sex, and Age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/63tv-jvxk",
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
-            "identifier": "41ec3131-feea-4dc3-917e-57fe26f87d96",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210906 to 20210912",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18996,39 +18981,36 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "41ec3131-feea-4dc3-917e-57fe26f87d96",
+            "issued": "2021-10-14",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/63tv-jvxk",
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
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210906 to 20210912"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/63yi-srh7",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-09-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-24",
-            "keyword": [
-                "exchange puf",
-                "marketplace puf",
-                "plan id crosswalk",
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
-            "identifier": "af1301a6-77fb-4369-a157-09125608161d",
             "description": "The Plan ID Crosswalk PUF (CW-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The purpose of the CW-PUF is to map QHPs and SADPs offered through the Exchanges during the previous plan year to plans that will be offered through the Exchanges in the current plan year.",
-            "title": "Plan ID Crosswalk PUF \u2013 PY2025",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19036,32 +19018,37 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "af1301a6-77fb-4369-a157-09125608161d",
+            "issued": "2024-09-26",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "plan id crosswalk",
+                "py2025"
+            ],
+            "landingPage": "https://healthdata.gov/d/63yi-srh7",
+            "modified": "2024-10-24",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Plan ID Crosswalk PUF \u2013 PY2025"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ya5p-jf7v",
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
-            "identifier": "https://data.cdc.gov/api/views/ya5p-jf7v",
             "description": "Occupational immune diseases are some of the most common illnesses that affect workers in the United States.  The Healthcare and Social Assistance Sector (HCSA) has one of the highest incidence of allergic disease compared to other industrial sectors. Individuals in this sector are frequently exposed to a variety of high-level cleaners and disinfectants along with antiseptics for the purposes of sterilization of surfaces, medical and surgical instruments, and reducing the incidence of nosocomial infections.  The range of specificity and effectiveness of these agents is very diverse based on the type of chemical used.  Commonly used antimicrobials include: alcohol, chlorine, iodine based agents; phenols; hydrogen peroxide; and quaternary ammonium compounds (QAC).   While the importance of these kinds of chemicals is understood, many of these agents are also known to directly contribute to allergic disease.  Antimicrobials including disinfectants and antiseptics are unique in that they have been identified to c",
-            "title": "Antimicrobials and Allergic Disease: Identifying Novel Biomarkers and Mechanisms of Action",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19069,44 +19056,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ya5p-jf7v",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/ya5p-jf7v",
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
+            "title": "Antimicrobials and Allergic Disease: Identifying Novel Biomarkers and Mechanisms of Action"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/i42d-szcv",
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
-                "tetanus",
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
-            "identifier": "https://data.cdc.gov/api/views/i42d-szcv",
             "description": "NNDSS - Table II. Tetanus to Varicella  - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Tetanus to Varicella",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19129,20 +19107,56 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/i42d-szcv",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "nedss",
+                "netss",
+                "nndss",
+                "tetanus",
+                "varicella morbidity",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/i42d-szcv",
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
+            "title": "NNDSS - Table II. Tetanus to Varicella"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/64cs-er3k",
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
+                    "downloadURL": "https://download.medicaid.gov/data/Behavioral-Health-Services-Provided-to-the-MedicaidCHIP-Population.csv",
+                    "mediaType": "text/csv",
+                    "title": "Behavioral Health Services\u00a0Provided to the Medicaid and CHIP Population"
+                }
+            ],
+            "identifier": "f403f019-48f5-48f0-b0ce-c051cfe04a5e",
             "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-05",
             "keyword": [
                 "behavioral health",
                 "chip",
@@ -19153,79 +19167,43 @@
                 "substance use disorder",
                 "t-msis analytic files"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Medicaid.gov",
-                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/d/64cs-er3k",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-01-05",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Medicare & Medicaid Services"
             },
-            "identifier": "f403f019-48f5-48f0-b0ce-c051cfe04a5e",
-            "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of behavioral health services, including emergency department services, inpatient services, intensive outpatient/partial hospitalizations, outpatient services, or services delivered through telehealth, provided to Medicaid and CHIP beneficiaries, by state. Users can filter by either mental health disorder or substance use disorder. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating behavioral health services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Diagnosis Code - IP, Diagnosis Code - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Behavioral Health Services\u00a0Provided to the Medicaid and CHIP Population",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/Behavioral-Health-Services-Provided-to-the-MedicaidCHIP-Population.csv",
-                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of behavioral health services, including emergency department services, inpatient services, intensive outpatient/partial hospitalizations, outpatient services, or services delivered through telehealth, provided to Medicaid and CHIP beneficiaries, by state. Users can filter by either mental health disorder or substance use disorder. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating behavioral health services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Diagnosis Code - IP, Diagnosis Code - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-                    "@type": "dcat:Distribution",
-                    "title": "Behavioral Health Services\u00a0Provided to the Medicaid and CHIP Population"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "Behavioral Health Services\u00a0Provided to the Medicaid and CHIP Population"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospice-enrollments",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-04-20",
-            "temporal": "2023-04-01/2025-03-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2023-03/f193e9ef-9fd7-4de3-9a27-0d5281cf80a9/Hospice_Data_Guidance.pdf"
-            ],
-            "keyword": [
-                "hospice",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/25704213-e833-4b8b-9dbc-58dd17149209/data-viewer",
-            "description": "The Hospice Enrollments dataset provides enrollment information of all hospices currently enrolled in Medicare. This data includes information on the hospice's legal business name, doing business as name, organization type and address.\u00a0",
-            "title": "Hospice Enrollments",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-03/f736ce50-3d6b-4ee2-802f-2e5424ae71ac/Hospice_Enrollments_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Hospice Enrollments dataset provides enrollment information of all hospices currently enrolled in Medicare. This data includes information on the hospice's legal business name, doing business as name, organization type and address.\u00a0",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/25704213-e833-4b8b-9dbc-58dd17149209/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/25704213-e833-4b8b-9dbc-58dd17149209/data",
+                    "mediaType": "text/html",
                     "title": "Hospice Enrollments : 2025-01-01"
                 },
                 {
@@ -19325,50 +19303,50 @@
                     "title": "Hospice Enrollments : 2023-04-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2023-03/f736ce50-3d6b-4ee2-802f-2e5424ae71ac/Hospice_Enrollments_Data_Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/25704213-e833-4b8b-9dbc-58dd17149209/data-viewer",
+            "issued": "2023-04-20",
+            "keyword": [
+                "hospice",
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospice-enrollments",
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
+                "https://data.cms.gov/sites/default/files/2023-03/f193e9ef-9fd7-4de3-9a27-0d5281cf80a9/Hospice_Data_Guidance.pdf"
+            ],
+            "temporal": "2023-04-01/2025-03-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Hospice Enrollments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-07-28",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "flu vaccination",
-                "immunization",
-                "influenza",
-                "influenza coverage",
-                "vaccination",
-                "vaccination coverage",
-                "vaxviews"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCIRD ISD Assessment Branch",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/vh55-3he6",
             "description": "Influenza Vaccination Coverage for All Ages (6+ Months)\n\n\u2022 Data on influenza vaccination coverage from the National Immunization Survey-Flu (NIS-Flu) and the Behavioral Risk Factor Surveillance System (BRFSS) for the general population at the national, regional, and state levels by age group and race/ethnicity.\n \n\u2022 Additional information available at https://www.cdc.gov/flu/fluvaxview/index.htm",
-            "title": "Influenza Vaccination Coverage for All Ages (6+ Months)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19391,24 +19369,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vh55-3he6",
+            "issued": "2021-07-28",
+            "keyword": [
+                "flu vaccination",
+                "immunization",
+                "influenza",
+                "influenza coverage",
+                "vaccination",
+                "vaccination coverage",
+                "vaxviews"
+            ],
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/index.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Flu Vaccinations"
-            ]
+            ],
+            "title": "Influenza Vaccination Coverage for All Ages (6+ Months)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.hrsa.gov/vaccine-compensation/data/index.html",
             "bureauCode": [
                 "009:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Hrsa Press",
+                "hasEmail": "mailto:press@hrsa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.hrsa.gov/vaccine-compensation/data/index.html",
+            "description": "<p>The VICP program publishes a summary PDF report with several data tables:</p>\n<ul>\n<li>\n<p>Number of Petitions Filed by Adjudication Categories by Alleged Vaccine, including # of doses distributed (2006-2014)</p>\n</li>\n<li>\n<p>Number of Petitions Filed, Compensated, and Dismissed by Alleged Vaccine (cumulative 1998 through 2016)</p>\n</li>\n<li>\n<p>Number of Petitions Filed by year (1998-2017)</p>\n</li>\n<li>\n<p>Number of Adjudications compensable, dismissed and total (FY1989 - FY2017)</p>\n</li>\n<li>\n<p>Awards paid including amounts, attorneys fees, and total outlays (FY1989 - FY2016)</p>\n</li>\n</ul>",
+            "identifier": "1c6c0d71-9ef1-42a1-a8b8-7eb13ff95f4b",
             "issued": "2013-12-04",
-            "temporal": "1988-01-01T00:00:00-05:00/1988-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "references": [
-                "https://vaers.hhs.gov/index"
-            ],
             "keyword": [
                 "adjudication",
                 "administrative",
@@ -19420,55 +19422,38 @@
                 "vaccine injury",
                 "vicp"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Hrsa Press",
-                "hasEmail": "mailto:press@hrsa.gov"
-            },
+            "landingPage": "https://www.hrsa.gov/vaccine-compensation/data/index.html",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:011"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Health Resources and Services Administration"
             },
-            "identifier": "1c6c0d71-9ef1-42a1-a8b8-7eb13ff95f4b",
-            "description": "<p>The VICP program publishes a summary PDF report with several data tables:</p>\n<ul>\n<li>\n<p>Number of Petitions Filed by Adjudication Categories by Alleged Vaccine, including # of doses distributed (2006-2014)</p>\n</li>\n<li>\n<p>Number of Petitions Filed, Compensated, and Dismissed by Alleged Vaccine (cumulative 1998 through 2016)</p>\n</li>\n<li>\n<p>Number of Petitions Filed by year (1998-2017)</p>\n</li>\n<li>\n<p>Number of Adjudications compensable, dismissed and total (FY1989 - FY2017)</p>\n</li>\n<li>\n<p>Awards paid including amounts, attorneys fees, and total outlays (FY1989 - FY2016)</p>\n</li>\n</ul>",
-            "title": "National Vaccine Injury Compensation Program (VICP) -Data & Statistics",
-            "programCode": [
-                "009:011"
+            "references": [
+                "https://vaers.hhs.gov/index"
             ],
-            "describedBy": "https://www.hrsa.gov/vaccine-compensation/data/index.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1988-01-01T00:00:00-05:00/1988-01-01T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "National Vaccine Injury Compensation Program (VICP) -Data & Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/65mz-x5ye",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-12-06",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-04",
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
-            "identifier": "094de49c-13c3-437c-8419-af9ad3862666",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-11-27-to-2023-12-03",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19477,68 +19462,65 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-11-27-to-2023-12-03"
                 }
             ],
+            "identifier": "094de49c-13c3-437c-8419-af9ad3862666",
+            "issued": "2023-12-06",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/65mz-x5ye",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-12-04",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-11-27-to-2023-12-03"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.dknet.org/",
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
                 "fn": "Abraham, Kristin",
                 "hasEmail": "mailto:abrahamk@niddk.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "b635b7e8-e003-4b4e-9b2e-94bbccee5c97",
+            "dataQuality": true,
             "description": "<p>The NIDDK Information Network serves the needs of basic and clinical investigators by providing seamless access to large pools of data relevant to the mission of NIDDK. The goal of DKnet is to develop a community-based network for integration across disciplines to include the larger DK universe of diseases, investigators, and potential users.</p>",
-            "title": "dkNET",
+            "identifier": "b635b7e8-e003-4b4e-9b2e-94bbccee5c97",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.dknet.org/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:110"
             ],
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "dataQuality": true
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "title": "dkNET"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#vaccine-confidence",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-07-06",
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
-            "identifier": "https://data.cdc.gov/api/views/qz99-wyhv",
             "description": "National Immunization Survey-Adult COVID Module (NIS-ACM): CDC is providing information on COVID-19 vaccine confidence to supplement vaccine administration data. Trends in behavioral indicators represent the percent of unvaccinated people responding to each of the indicators by intent status and by week for the national-level view, and by month for the jurisdiction-level view.",
-            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): Trends in Behavioral Indicators Among Unvaccinated People",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19561,84 +19543,83 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qz99-wyhv",
+            "issued": "2022-07-06",
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
+            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): Trends in Behavioral Indicators Among Unvaccinated People"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nlm.nih.gov/tsd/serials/lsiou.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dataset",
-                "library services",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/dc87-bt4r",
             "description": "The List of Serials Indexed for Online Users (LSIOU) provides bibliographic information for all journals whose articles were ever indexed over time with the MeSH\u00ae vocabulary and cited in MEDLINE\u00ae, the backbone of the NLM PubMed\u00ae database. It includes titles that ceased publication, changed titles, or are no longer indexed. More detailed bibliographic data and information about indexing coverage for serials cited in MEDLINE/PubMed can be found in LocatorPlus Catalog\u00ae, the NLM online catalog, and the NLM Catalog, an Entrez database.",
-            "title": "List of Serials Indexed for Online Users (LSIOU)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "ftp://ftp.nlm.nih.gov/online/journals/",
-                    "description": "The LSIOU is produced in XML.  The current year's file is in the directory linked below and named lsi2021.xml (for 2021).  Previous year's files are located in the 'archive' folder.",
                     "@type": "dcat:Distribution",
+                    "description": "The LSIOU is produced in XML.  The current year's file is in the directory linked below and named lsi2021.xml (for 2021).  Previous year's files are located in the 'archive' folder.",
+                    "downloadURL": "ftp://ftp.nlm.nih.gov/online/journals/",
+                    "mediaType": "text/html",
                     "title": "Download Data - List of Serials Indexed for Online Users (LSIOU)"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/dc87-bt4r",
+            "issued": "2021-08-26",
+            "keyword": [
+                "dataset",
+                "library services",
+                "literature"
+            ],
+            "landingPage": "https://www.nlm.nih.gov/tsd/serials/lsiou.html",
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
+            "title": "List of Serials Indexed for Online Users (LSIOU)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/books/NBK3831/",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/9kh4-cnc3",
             "description": "Accessed through the NCBI Bookshelf, the Help Manual contains documentation for many NCBI resources, including PubMed, PubMed Central, the Entrez system, Gene, SNP and LinkOut. All chapters can be downloaded in PDF format.",
-            "title": "NCBI Help Manual",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19647,137 +19628,134 @@
                     "title": "NCBI Help Manual"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/9kh4-cnc3",
+            "issued": "2022-03-01",
+            "keyword": [
+                "computational biology",
+                "education",
+                "reference",
+                "training and instruction"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/books/NBK3831/",
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
+            "title": "NCBI Help Manual"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/66fh-dpbp",
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
-            "identifier": "7b094759-dc32-5e07-98a7-40dba23b1605",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet version v2.10.64 (coreset-dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/version.csv",
-                    "description": "CoreSet version v2.10.64 (coreset-dev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet version v2.10.64 (coreset-dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/version.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet version v2.10.64 (coreset-dev)"
                 }
             ],
+            "identifier": "7b094759-dc32-5e07-98a7-40dba23b1605",
+            "issued": "2024-11-06",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/66fh-dpbp",
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
+            "title": "CoreSet version v2.10.64 (coreset-dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/66fk-xr8a",
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
-            "identifier": "0ca65533-a457-57ec-b080-9ab30597929c",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt filters v2.10.14 (coreset-dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.14/20241029/filters.csv",
-                    "description": "CoreSEt filters v2.10.14 (coreset-dev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt filters v2.10.14 (coreset-dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.14/20241029/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt filters v2.10.14 (coreset-dev)"
                 }
             ],
+            "identifier": "0ca65533-a457-57ec-b080-9ab30597929c",
+            "issued": "2024-11-06",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/66fk-xr8a",
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
+            "title": "CoreSEt filters v2.10.14 (coreset-dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
             "bureauCode": [
                 "009:20"
             ],
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
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DDT Public Inquiries",
                 "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/vkwg-yswv",
+            "describedBy": "https://chronicdata.cdc.gov/d/vkwg-yswv",
             "description": "2013-2018. This dataset is a de-identified summary table of vision and eye health data indicators from BRFSS, stratified by all available combinations of age group, race/ethnicity, gender, risk factor and state. BRFSS is a system of telephone surveys conducted by CDC that collect state data about U.S. residents regarding their health-related risk behaviors, chronic health conditions, and use of preventive services. BRFSS completes more than 400,000 adult interviews each year across 50 states, the District of Columbia, and three U.S. territories. BRFSS data for VEHSS includes one question from the core component related to Visual Function. Data were suppressed following NCHS standards. Data will be updated as it becomes available. Detailed information on VEHSS BRFSS analyses can be found on the VEHSS BRFSS webpage (link). General information about BRFSS can be found on the BRFSS website (https://www.cdc.gov/brfss). The VEHSS BRFSS dataset was last updated in November 2019.",
-            "title": "Behavioral Risk Factors \u2013 Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19800,41 +19778,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/d/vkwg-yswv",
+            "identifier": "https://data.cdc.gov/api/views/vkwg-yswv",
+            "issued": "2024-03-20",
+            "keyword": [
+                "brfss",
+                "contact lenses",
+                "glasses",
+                "visual function"
+            ],
+            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2024-03-20",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/brfss",
+                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/behavioral-risk-factors-surveillance-system.html"
+            ],
             "theme": [
                 "Vision & Eye Health"
-            ]
+            ],
+            "title": "Behavioral Risk Factors \u2013 Vision and Eye Health Surveillance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/b8tp-jsmh",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-28",
-            "keyword": [
-                "measles",
-                "modeling",
-                "sequencing"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nina Masters",
                 "hasEmail": "mailto:rhv2@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/b8tp-jsmh",
             "description": "The table contains metadata variables used to execute compartmental and genetic modeling on measles cases investigated as a component of Operation Allies Welcome.",
-            "title": "Measles Case and Genetic Metadata, Operation Allies Welcome",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19857,52 +19839,49 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/b8tp-jsmh",
+            "issued": "2023-07-28",
+            "keyword": [
+                "measles",
+                "modeling",
+                "sequencing"
+            ],
+            "landingPage": "https://data.cdc.gov/d/b8tp-jsmh",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-07-28",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Models"
-            ]
+            ],
+            "title": "Measles Case and Genetic Metadata, Operation Allies Welcome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/medicaid-managed-care",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-12-14",
-            "temporal": "2023-10-01/2023-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-13",
-            "references": [
-                "https://data.cms.gov/resources/medicaid-managed-care-methodology"
-            ],
-            "keyword": [
-                "counties",
-                "health care use & payments",
-                "health equity",
-                "medicaid",
-                "states & territories"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid Managed Care - CPI",
                 "hasEmail": "mailto:CPI_MCO_Dashboard@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/a93f5362-2fe6-4b4d-8260-118be0d618e0/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicaid-managed-care-data-dictionary",
             "description": "The Medicaid Managed Care\u00a0dataset uses CMS' state Transformed Medicaid Statistical Information System (T-MSIS)\u00a0data for Arizona, Michigan, Nevada, and New Mexico to identify various metrics for managed care plans within each state. These metrics are designed to allow users to compare plans in each state across different specialty areas (currently Pediatric Dental, Behavioral Health, and Prenatal OB/GYN).\u00a0This dataset does not include all available data in T-MSIS but utilized a subset to calculate the individual metrics identified.",
-            "title": "Medicaid Managed Care",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a93f5362-2fe6-4b4d-8260-118be0d618e0/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a93f5362-2fe6-4b4d-8260-118be0d618e0/data",
+                    "mediaType": "text/html",
                     "title": "Medicaid Managed Care : 2023-12-01"
                 },
                 {
@@ -19918,48 +19897,50 @@
                     "title": "Medicaid Managed Care : 2023-12-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicaid-managed-care-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/a93f5362-2fe6-4b4d-8260-118be0d618e0/data-viewer",
+            "issued": "2024-12-14",
+            "keyword": [
+                "counties",
+                "health care use & payments",
+                "health equity",
+                "medicaid",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/medicaid-managed-care",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-12-13",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicaid-managed-care-methodology"
+            ],
+            "temporal": "2023-10-01/2023-12-31",
             "theme": [
                 "Medicaid"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicaid Managed Care"
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
-            "temporal": "1900/2018",
-            "modified": "2022-03-30",
-            "keyword": [
-                "age-adjusted death rate",
-                "cause of death",
-                "mortality united states",
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
-            "identifier": "https://data.cdc.gov/api/views/6rkc-nb2q",
             "description": "This dataset of U.S. mortality trends since 1900 highlights trends in age-adjusted death rates for five selected major causes of death.\n\nAge-adjusted death rates (deaths per 100,000) after 1998 are calculated based on the 2000 U.S. standard population. Populations used for computing death rates for 2011\u20132017 are postcensal estimates based on the 2010 census, estimated as of July 1, 2010. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for noncensus years between 2000 and 2010 are revised using updated intercensal population estimates and may differ from rates previously published. Data on age-adjusted death rates prior to 1999 are taken from historical data (see References below).\n\nRevisions to the International Classification of Diseases (ICD) over time may result in discontinuities in cause-of-death trends.\n\nSOURCES\n\nCDC/NCHS, National Vital Statistics System, historical data, 1900-1998 (see https://www.cdc.gov/nchs/nvss/mortality_historical_data.htm); CDC/NCHS, National Vital Statistics System, mortality data (see http://www.cdc.gov/nchs/deaths.htm); and CDC WONDER (see http://wonder.cdc.gov).\n\nREFERENCES\n\n1. National Center for Health Statistics, Data Warehouse. Comparability of cause-of-death between ICD revisions. 2008. Available from: http://www.cdc.gov/nchs/nvss/mortality/comparability_icd.htm.\n\n2. National Center for Health Statistics. Vital statistics data available. Mortality multiple cause files. Hyattsville, MD: National Center for Health Statistics. Available from: https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm.\n\n3. Kochanek KD, Murphy SL, Xu JQ, Arias E. Deaths: Final data for 2017. National Vital Statistics Reports; vol 68 no 9. Hyattsville, MD: National Center for Health Statistics. 2019. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_09-508.pdf.\n\n4. Arias E, Xu JQ. United States life tables, 2017. National Vital Statistics Reports; vol 68 no 7. Hyattsville, MD: National Center for Health Statistics. 2019. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_07-508.pdf.\n\n5. National Center for Health Statistics. Historical Data, 1900-1998. 2009. Available from: https://www.cdc.gov/nchs/nvss/mortality_historical_data.htm.",
-            "title": "NCHS - Age-adjusted Death Rates for Selected Major Causes of Death",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19982,23 +19963,55 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/6rkc-nb2q",
+            "issued": "2015-07-14",
+            "keyword": [
+                "age-adjusted death rate",
+                "cause of death",
+                "mortality united states",
+                "nchs"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/mortality-trends/index.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2022-03-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "1900/2018",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - Age-adjusted Death Rates for Selected Major Causes of Death"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-births",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/natality.html",
+            "description": "<p>The Births (Natality) online databases in CDC WONDER report birth rates, fertility rates and counts of live births  occurring within the United States to U.S. residents and non-residents. Counts can be obtained by state, county, child's gender and weight, mother's race, mother's age, mother's education, gestation period, prenatal care, birth plurality, and mother's medical and tobacco use risk factors. The data are derived from birth certificates.  Data are available since 1995. The data are produced by the National Center for Health Statistics.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/natality.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "2703dd18-34f2-4101-8a43-9499eba7f787",
             "issued": "2012-05-30",
-            "temporal": "1995-01-01T00:00:00-05:00/2006-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "age",
                 "anemia",
@@ -20030,64 +20043,35 @@
                 "tobacco use",
                 "year"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-births",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:015"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "2703dd18-34f2-4101-8a43-9499eba7f787",
-            "description": "<p>The Births (Natality) online databases in CDC WONDER report birth rates, fertility rates and counts of live births  occurring within the United States to U.S. residents and non-residents. Counts can be obtained by state, county, child's gender and weight, mother's race, mother's age, mother's education, gestation period, prenatal care, birth plurality, and mother's medical and tobacco use risk factors. The data are derived from birth certificates.  Data are available since 1995. The data are produced by the National Center for Health Statistics.</p>",
-            "title": "CDC WONDER: Births",
-            "programCode": [
-                "009:015"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://wonder.cdc.gov/natality.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/natality.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1995-01-01T00:00:00-05:00/2006-12-31T00:00:00-05:00",
             "theme": [
                 "Health",
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Births"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/67xx-b5dq",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-09",
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
-            "identifier": "153cd4c8-3ede-4400-be3f-b255a9ba45d4",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 12-02-2024-to-12-08-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20095,40 +20079,36 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "153cd4c8-3ede-4400-be3f-b255a9ba45d4",
+            "issued": "2024-12-11",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/67xx-b5dq",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-09",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 12-02-2024-to-12-08-2024"
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
-            "modified": "2025-01-14",
-            "keyword": [
-                "legislation",
-                "osh",
-                "policy",
-                "state system",
-                "tobacco",
-                "youth access"
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
-            "identifier": "https://data.cdc.gov/api/views/hgv5-3wrn",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Youth-Access/hgv5-3wrn",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation\u2014Youth Access. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies.  Data are reported on a quarterly basis. Data include information related to restrictions, enforcement and penalties associated with the sale of cigarettes to youth through retail sales and vending machines.",
-            "title": "CDC STATE System Tobacco Legislation - Youth Access",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20151,25 +20131,55 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Youth-Access/hgv5-3wrn",
+            "identifier": "https://data.cdc.gov/api/views/hgv5-3wrn",
+            "issued": "2023-07-18",
+            "keyword": [
+                "legislation",
+                "osh",
+                "policy",
+                "state system",
+                "tobacco",
+                "youth access"
+            ],
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2025-01-14",
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
+            "title": "CDC STATE System Tobacco Legislation - Youth Access"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/mortality-public.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-05-15",
-            "temporal": "1979/2019",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-29",
-            "references": [
-                "https://www.cdc.gov/nchs/data/datalinkage/public-use-linked-mortality-files-data-dictionary.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCHS Data Linkage Program",
+                "hasEmail": "mailto:DataLinkage@cdc.gov"
+            },
+            "describedBy": "https://www.cdc.gov/nchs/data/datalinkage/public-use-linked-mortality-file-description.pdf",
+            "describedByType": "application/pdf",
+            "description": "NCHS has linked data from various surveys with death certificate records from the National Death Index (NDI). Linkage of the NCHS survey participant data with the NDI mortality data provides the opportunity to conduct a vast array of outcome studies designed to investigate the association of a wide variety of health factors with mortality. The Linked Mortality Files (LMF) have been updated with mortality follow-up data through December 31, 2019.\n\nPublic-use Linked Mortality Files (LMF) are available for 1986-2018 NHIS, 1999-2018 NHANES, and NHANES III. The files include a limited set of mortality variables for adult participants only. The public-use versions of the NCHS Linked Mortality Files were subjected to data perturbation techniques to reduce the risk of participant re-identification. For select records, synthetic data were substituted for follow-up time or underlying cause of death. Information regarding vital status was not perturbed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/nchs/data-linkage/mortality-public.htm",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/r9nv-zxge",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2023-05-15",
             "keyword": [
                 "linked mortality files",
                 "nchs surveys",
@@ -20196,72 +20206,39 @@
                 "sdoh-use-of-health-care",
                 "sdoh-workplace"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NCHS Data Linkage Program",
-                "hasEmail": "mailto:DataLinkage@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/mortality-public.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-29",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/r9nv-zxge",
-            "description": "NCHS has linked data from various surveys with death certificate records from the National Death Index (NDI). Linkage of the NCHS survey participant data with the NDI mortality data provides the opportunity to conduct a vast array of outcome studies designed to investigate the association of a wide variety of health factors with mortality. The Linked Mortality Files (LMF) have been updated with mortality follow-up data through December 31, 2019.\n\nPublic-use Linked Mortality Files (LMF) are available for 1986-2018 NHIS, 1999-2018 NHANES, and NHANES III. The files include a limited set of mortality variables for adult participants only. The public-use versions of the NCHS Linked Mortality Files were subjected to data perturbation techniques to reduce the risk of participant re-identification. For select records, synthetic data were substituted for follow-up time or underlying cause of death. Information regarding vital status was not perturbed.",
-            "title": "Public-Use Linked Mortality Files",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/nchs/data-linkage/mortality-public.htm",
-                    "mediaType": "text/html"
-                }
+            "references": [
+                "https://www.cdc.gov/nchs/data/datalinkage/public-use-linked-mortality-files-data-dictionary.pdf"
             ],
-            "describedBy": "https://www.cdc.gov/nchs/data/datalinkage/public-use-linked-mortality-file-description.pdf",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "1979/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Public-Use Linked Mortality Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/medicare-restricted.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-06-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2014/2018",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data-linkage/cms/nchs-cms_medicare14_18_linked_data-list_of_variables.pdf"
-            ],
-            "keyword": [
-                "linked medicare files",
-                "nchs surveys",
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
-            "identifier": "https://data.cdc.gov/api/views/mjpe-bnz8",
-            "description": "NCHS has linked data from various surveys with Medicare program enrollment and health care utilization and expenditure data from the Centers for Medicare & Medicaid Services (CMS). Linkage of the NCHS survey participants with the CMS Medicare data provides the opportunity to study changes in health status, health care utilization and costs, and prescription drug use among Medicare enrollees. Medicare is the federal health insurance program for people who are 65 or older, certain younger people with disabilities, and people with End-Stage Renal Disease.",
-            "title": "NCHS Survey Data Linked to Centers for Medicare & Medicaid Services (CMS) Medicare Data Files",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/cms_medicare_linked_data_match_rate_tables_1.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "NCHS has linked data from various surveys with Medicare program enrollment and health care utilization and expenditure data from the Centers for Medicare & Medicaid Services (CMS). Linkage of the NCHS survey participants with the CMS Medicare data provides the opportunity to study changes in health status, health care utilization and costs, and prescription drug use among Medicare enrollees. Medicare is the federal health insurance program for people who are 65 or older, certain younger people with disabilities, and people with End-Stage Renal Disease.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20269,55 +20246,47 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/cms_medicare_linked_data_match_rate_tables_1.pdf",
+            "identifier": "https://data.cdc.gov/api/views/mjpe-bnz8",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-06-16",
+            "keyword": [
+                "linked medicare files",
+                "nchs surveys",
+                "research-data-center"
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
+                "https://www.cdc.gov/nchs/data-linkage/cms/nchs-cms_medicare14_18_linked_data-list_of_variables.pdf"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "United States",
+            "temporal": "2014/2018",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Survey Data Linked to Centers for Medicare & Medicaid Services (CMS) Medicare Data Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/surveillance/nvsn/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-28",
-            "@type": "dcat:Dataset",
-            "temporal": "12 month rolling period",
-            "modified": "2025-01-29",
-            "keyword": [
-                "adenovirus",
-                "covid-19",
-                "enterovirus",
-                "evd-68",
-                "human coronaviruses",
-                "human metapneumovirus",
-                "influenza",
-                "medically attended illness",
-                "parainfluenza virus",
-                "pediatric",
-                "respiratory illness",
-                "rhinovirus",
-                "rsv",
-                "viral detections"
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
-            "identifier": "https://data.cdc.gov/api/views/r229-z6ma",
             "description": "Percent positivity of 9 viral pathogens, and enrollment counts of children with ARI by week for the past 12 months (rolling x-axis).",
-            "title": "Pathogen Detections Among Enrolled Children in the New Vaccine Surveillance Network (NVSN), Acute Respiratory Illnesses (ARI), 12 Month Rolling Period",
-            "isPartOf": "Yes",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20340,54 +20309,64 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/r229-z6ma",
+            "isPartOf": "Yes",
+            "issued": "2024-02-28",
+            "keyword": [
+                "adenovirus",
+                "covid-19",
+                "enterovirus",
+                "evd-68",
+                "human coronaviruses",
+                "human metapneumovirus",
+                "influenza",
+                "medically attended illness",
+                "parainfluenza virus",
+                "pediatric",
+                "respiratory illness",
+                "rhinovirus",
+                "rsv",
+                "viral detections"
+            ],
+            "landingPage": "https://www.cdc.gov/surveillance/nvsn/index.html",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-29",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "12 month rolling period",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Pathogen Detections Among Enrolled Children in the New Vaccine Surveillance Network (NVSN), Acute Respiratory Illnesses (ARI), 12 Month Rolling Period"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-all-owners",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/029c119f-f79c-49be-9100-344d31d10344/data-viewer",
-            "description": "The Hospital All Owners Information dataset provides information on all owners of the hospitals. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
-            "title": "Hospital All Owners",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/Hospital_All_Owners_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Hospital All Owners Information dataset provides information on all owners of the hospitals. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/029c119f-f79c-49be-9100-344d31d10344/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/029c119f-f79c-49be-9100-344d31d10344/data",
+                    "mediaType": "text/html",
                     "title": "Hospital All Owners : 2025-01-01"
                 },
                 {
@@ -20703,27 +20682,52 @@
                     "title": "Hospital All Owners : 2022-11-13"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/Hospital_All_Owners_Data_Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/029c119f-f79c-49be-9100-344d31d10344/data-viewer",
+            "issued": "2022-12-21",
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-all-owners",
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
+            "title": "Hospital All Owners"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.hcup-us.ahrq.gov/db/nation/nis/nisdbdocumentation.jsp",
             "bureauCode": [
                 "009:33"
             ],
-            "rights": "N/A",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HCUP Technical Support",
+                "hasEmail": "mailto:hcup@ahrq.gov"
+            },
+            "describedBy": "https://www.hcup-us.ahrq.gov/db/nation/nis/nisdbdocumentation.jsp",
+            "description": "The Healthcare Cost and Utilization Project (HCUP) National Inpatient Sample (NIS) is the largest publicly available all-payer inpatient care database in the United States. The NIS is designed to produce U.S. regional and national estimates of inpatient utilization, access, cost, quality, and outcomes. Unweighted, it contains data from more than 7 million hospital stays each year. Weighted, it estimates more than 35 million hospitalizations nationally. Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality (AHRQ), HCUP data inform decision making at the national, State, and community levels.\n\nStarting with the 2012 data year, the NIS is a sample of discharges from all hospitals participating in HCUP, covering more than 97 percent of the U.S. population. For prior years, the NIS was a sample of hospitals. The NIS allows for weighted national estimates to identify, track, and analyze national trends in health care utilization, access, charges, quality, and outcomes. The NIS's large sample size enables analyses of rare conditions, such as congenital anomalies; uncommon treatments, such as organ transplantation; and special patient populations, such as the uninsured. NIS data are available since 1988, allowing analysis of trends over time. \n\nThe NIS inpatient data include clinical and resource use information typically available from discharge abstracts with safeguards to protect the privacy of individual patients, physicians, and hospitals (as required by data sources).  Data elements include but are not limited to: diagnoses, procedures, discharge status, patient demographics (e.g., gender, age), total charges, length of stay, and expected payment source, including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge\u2019. The NIS excludes data elements that could directly or indirectly identify individuals. \n\nRestricted access data files are available with a data use agreement and brief online security training.",
+            "identifier": "bae01dec-8c8a-48c0-8d22-e0f85f2edd8e",
             "issued": "2021-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "claims",
                 "diagnoses",
@@ -20737,140 +20741,123 @@
                 "procedures",
                 "utilization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HCUP Technical Support",
-                "hasEmail": "mailto:hcup@ahrq.gov"
-            },
+            "landingPage": "https://www.hcup-us.ahrq.gov/db/nation/nis/nisdbdocumentation.jsp",
+            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
             },
-            "identifier": "bae01dec-8c8a-48c0-8d22-e0f85f2edd8e",
-            "description": "The Healthcare Cost and Utilization Project (HCUP) National Inpatient Sample (NIS) is the largest publicly available all-payer inpatient care database in the United States. The NIS is designed to produce U.S. regional and national estimates of inpatient utilization, access, cost, quality, and outcomes. Unweighted, it contains data from more than 7 million hospital stays each year. Weighted, it estimates more than 35 million hospitalizations nationally. Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality (AHRQ), HCUP data inform decision making at the national, State, and community levels.\n\nStarting with the 2012 data year, the NIS is a sample of discharges from all hospitals participating in HCUP, covering more than 97 percent of the U.S. population. For prior years, the NIS was a sample of hospitals. The NIS allows for weighted national estimates to identify, track, and analyze national trends in health care utilization, access, charges, quality, and outcomes. The NIS's large sample size enables analyses of rare conditions, such as congenital anomalies; uncommon treatments, such as organ transplantation; and special patient populations, such as the uninsured. NIS data are available since 1988, allowing analysis of trends over time. \n\nThe NIS inpatient data include clinical and resource use information typically available from discharge abstracts with safeguards to protect the privacy of individual patients, physicians, and hospitals (as required by data sources).  Data elements include but are not limited to: diagnoses, procedures, discharge status, patient demographics (e.g., gender, age), total charges, length of stay, and expected payment source, including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge\u2019. The NIS excludes data elements that could directly or indirectly identify individuals. \n\nRestricted access data files are available with a data use agreement and brief online security training.",
-            "title": "National Inpatient Sample (NIS) - Restricted Access Files",
-            "programCode": [
-                "009:072"
-            ],
-            "describedBy": "https://www.hcup-us.ahrq.gov/db/nation/nis/nisdbdocumentation.jsp",
-            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx"
+            "rights": "N/A",
+            "title": "National Inpatient Sample (NIS) - Restricted Access Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6apd-9hk3",
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
-            "identifier": "c407d189-9d2e-55a7-b0df-526f29fb96ba",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet pillar v2.10.64 (coreset-prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/pillar.csv",
-                    "description": "CoreSet pillar v2.10.64 (coreset-prod)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet pillar v2.10.64 (coreset-prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet pillar v2.10.64 (coreset-prod)"
                 }
             ],
+            "identifier": "c407d189-9d2e-55a7-b0df-526f29fb96ba",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/6apd-9hk3",
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
+            "title": "CoreSet pillar v2.10.64 (coreset-prod)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6bfs-4664",
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
-            "identifier": "fbf6f052-37cf-5512-914c-f732124a7a99",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet measure v2.10.64 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure.csv",
-                    "description": "CoreSet measure v2.10.64 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet measure v2.10.64 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet measure v2.10.64 (coreset-etl-test)"
                 }
             ],
+            "identifier": "fbf6f052-37cf-5512-914c-f732124a7a99",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/6bfs-4664",
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
+            "title": "CoreSet measure v2.10.64 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/tt3f-rr33",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-06-02",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-05",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:ERIC@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/tt3f-rr33",
             "description": "The U.S. government has taken unprecedented action to address the public health threat posed by this new coronavirus. To accelerate response efforts, CDC received supplemental funds through five congressional acts: the Coronavirus Preparedness and Response Supplemental Appropriations Act, 2020; Coronavirus Aid, Relief, and Economic Security Act; Paycheck Protection Program and Health Care Enhancement Act; Coronavirus Response and Relief Supplemental Appropriations Act, 2021; and American Rescue Plan Act of 2021. CDC is actively funding state, tribal, local, and territorial public health organizations to meet the challenges of this fast-moving public health threat.",
-            "title": "COVID-19 State, Tribal, Local, and Territorial Funding",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20893,45 +20880,35 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/tt3f-rr33",
+            "issued": "2021-06-02",
+            "landingPage": "https://data.cdc.gov/d/tt3f-rr33",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-09-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "COVID-19 State, Tribal, Local, and Territorial Funding"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kx9y-asbg",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
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
-            "identifier": "https://data.cdc.gov/api/views/kx9y-asbg",
             "description": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chancroid - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Reporting jurisdictions were informed CDC could receive data for this condition in August 2019. Please note there will be a delay in reporting of case notifications for this condition to CDC.",
-            "title": "NNDSS - TABLE 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chancroid",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20954,81 +20931,80 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kx9y-asbg",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "carbapenemase-producing carbapenem-resistant enterobacteriaceae",
+                "chancroid",
+                "chlamydia trachomatis infection",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/kx9y-asbg",
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
+            "title": "NNDSS - TABLE 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chancroid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/national-ambulatory-medical-care-survey-namcs",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.cdc.gov/nchs/ahcd/ahcd_questionnaires.htm",
+            "description": "<p>The National Ambulatory Medical Care Survey (NAMCS) is a national survey designed to meet the need for objective, reliable information about the provision and use of ambulatory medical care services in the United States. Findings are based on a sample of visits to non-federal employed office-based physicians who are primarily engaged in direct patient care.</p>",
+            "identifier": "9e365513-8d63-4e61-a577-8598ae3c4a1c",
             "issued": "2013-06-15",
-            "temporal": "1973-01-01T00:00:00-05:00/1973-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "centers-for-disease-control-and-prevention-department-of-health-human-services",
                 "health care providers",
                 "population statistics",
                 "treatments"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-ambulatory-medical-care-survey-namcs",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "9e365513-8d63-4e61-a577-8598ae3c4a1c",
-            "description": "<p>The National Ambulatory Medical Care Survey (NAMCS) is a national survey designed to meet the need for objective, reliable information about the provision and use of ambulatory medical care services in the United States. Findings are based on a sample of visits to non-federal employed office-based physicians who are primarily engaged in direct patient care.</p>",
-            "title": "National Ambulatory Medical Care Survey (NAMCS)",
-            "programCode": [
-                "009:072"
-            ],
-            "describedBy": "http://www.cdc.gov/nchs/ahcd/ahcd_questionnaires.htm",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "temporal": "1973-01-01T00:00:00-05:00/1973-01-01T00:00:00-05:00",
+            "title": "National Ambulatory Medical Care Survey (NAMCS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/n322-ce6f",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "brucellosis",
-                "campylobacteriosis",
-                "candida auris",
-                "clinical",
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
-            "identifier": "https://data.cdc.gov/api/views/n322-ce6f",
             "description": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21051,39 +21027,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/n322-ce6f",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "brucellosis",
+                "campylobacteriosis",
+                "candida auris",
+                "clinical",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/n322-ce6f",
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
+            "title": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/29ew-qk7z",
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
-            "identifier": "https://data.cdc.gov/api/views/29ew-qk7z",
             "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 3 - Philadelphia",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21106,203 +21089,196 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/29ew-qk7z",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/29ew-qk7z",
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
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 3 - Philadelphia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://immport.niaid.nih.gov/",
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
                 "fn": "Lin, Dawei",
                 "hasEmail": "mailto:dawei.lin@nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "615a68a0-7096-434e-b364-9aad242c96e3",
+            "dataQuality": true,
             "description": "<p>The ImmPort system serves as a long-term, sustainable archive of immunology research data generated by investigators mainly funded through the NIAID/DAIT. The core component of the ImmPort system is an extensive data warehouse containing an integration of experimental data and clinical trial data. The ImmPort system also provides data analysis tools and an immunology-focused ontology. The analytical tools created and integrated as part of the ImmPort system are available to any researcher within ImmPort after registration and approval by DAIT. Additionally, the data provided mainly by NIAID/DAIT funded researchers in ImmPort will be available to all registered users after the appropriate embargo time.</p>",
-            "title": "The Immunology Database and Analysis Portal (ImmPort)",
+            "identifier": "615a68a0-7096-434e-b364-9aad242c96e3",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "https://immport.niaid.nih.gov/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
             "programCode": [
                 "009:026"
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
+            "title": "The Immunology Database and Analysis Portal (ImmPort)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:00"
             ],
-            "landingPage": "https://data.cdc.gov/d/tkjk-cwh5",
-            "issued": "2015-03-25",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-18",
-            "keyword": [
-                "cdc",
-                "centers for disease control and prevention"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Susan Wilkin",
                 "hasEmail": "mailto:smw1@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/tkjk-cwh5",
             "description": "The CDC Division for Heart Disease and Stroke Prevention's Data Trends & Maps online tool allows searching for and view of health indicators related to Heart Disease and Stroke Prevention on the basis of a specific location or a health indicator.",
-            "title": "Division for Heart Disease and Stroke Prevention: Data Trends & Maps",
+            "identifier": "https://data.cdc.gov/api/views/tkjk-cwh5",
+            "issued": "2015-03-25",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/tkjk-cwh5",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2015-08-18",
             "programCode": [
                 "009:020"
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "Division for Heart Disease and Stroke Prevention: Data Trends & Maps"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6eve-74uu",
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
-            "identifier": "9eb3008a-70a1-5f32-8f3e-c9aa10b62f1e",
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
+            "identifier": "9eb3008a-70a1-5f32-8f3e-c9aa10b62f1e",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/6eve-74uu",
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
-            "landingPage": "https://healthdata.gov/d/6ewi-6eh5",
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
-            "identifier": "277374e9-ce53-53cd-81d0-d8d27edac2c4",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_brief",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250127_ETL_DEV/brief.csv",
-                    "description": "{\"dataset\": \"brief\", \"stage\": \"featAuto\", \"update_id\": \"20250127_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"brief\", \"stage\": \"featAuto\", \"update_id\": \"20250127_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250127_ETL_DEV/brief.csv",
+                    "mediaType": "text/csv",
                     "title": "brief csv file"
                 }
             ],
+            "identifier": "277374e9-ce53-53cd-81d0-d8d27edac2c4",
+            "issued": "2024-07-25",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/6ewi-6eh5",
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
+            "title": "featAuto_brief"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bkwy-pyv3",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
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
-            "identifier": "https://data.cdc.gov/api/views/bkwy-pyv3",
             "description": "NNDSS - TABLE 1W.  Meningococcal disease,  All serogroups to Meningococcal disease, Serogroup B - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21325,44 +21301,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bkwy-pyv3",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "all serogroups",
+                "meningococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "serogroup b",
+                "serogroups acwy",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bkwy-pyv3",
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
+            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/n83i-w4cq",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/n83i-w4cq",
             "description": "NNDSS - Table 1I.  Cryptosporidiosis to Cyclosporiasis - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21385,48 +21363,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/n83i-w4cq",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "cryptosporidiosis",
+                "cyclosporiasis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/n83i-w4cq",
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
+            "title": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/tzyy-aayg",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2021-09-10",
-            "keyword": [
-                "covid",
-                "covid-19",
-                "executive order",
-                "government order",
-                "legal epidemiology",
-                "mask mandates",
-                "masks",
-                "mitigation",
-                "proclamation",
-                "public health order",
-                "social distancing"
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
-            "identifier": "https://data.cdc.gov/api/views/tzyy-aayg",
             "description": "State and territorial executive orders, administrative orders, resolutions, and proclamations are collected from government websites and cataloged and coded using Microsoft Excel by one coder with one or more additional coders conducting quality assurance.\n\nData were collected to determine when members of the public in states and territories were subject to state and territorial executive orders, administrative orders, resolutions, and proclamations for COVID-19 that require them to wear masks in public. \u201cMembers of the public\u201d are defined as individuals operating in a personal capacity. \u201cIn public\u201d is defined to mean either (1) anywhere outside the home or (2) both in retail businesses and in restaurants/food establishments. Data consists exclusively of state and territorial orders.\n\nThese data are derived from publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly require individuals to wear masks in public found by the CDC, COVID-19 Community Intervention & Critical Populations Task Force, Monitoring & Evaluation Team, Mitigation Policy Analysis Unit, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program, and Max Gakh, Assistant Professor, School of Public Health, University of Nevada, Las Vegas from April 8, 2020 through  August 15, 2021. These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded; news media reports on restrictions were excluded. Recommendations not included in an order are not included in these data. Effective and expiration dates were coded using only the dates provided; no distinction was made based on the specific time of the day the order became effective or expired. These data do not include data on counties that have opted out of their state mask mandate pursuant to state law. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
-            "title": "U.S. State and Territorial Public Mask Mandates From April 8, 2020 through August 15, 2021 by State by Day",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21449,114 +21423,153 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/tzyy-aayg",
+            "issued": "2021-09-10",
+            "keyword": [
+                "covid",
+                "covid-19",
+                "executive order",
+                "government order",
+                "legal epidemiology",
+                "mask mandates",
+                "masks",
+                "mitigation",
+                "proclamation",
+                "public health order",
+                "social distancing"
+            ],
+            "landingPage": "https://data.cdc.gov/d/tzyy-aayg",
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
+            "title": "U.S. State and Territorial Public Mask Mandates From April 8, 2020 through August 15, 2021 by State by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6g28-j6yt",
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
-            "identifier": "156125e3-48b1-5d33-a5e5-9191a9588a66",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_measure_allStates",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_allStates.csv",
-                    "description": "{\"dataset\": \"measure_allStates\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_allStates\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_allStates.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_allStates csv file"
                 }
             ],
+            "identifier": "156125e3-48b1-5d33-a5e5-9191a9588a66",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/6g28-j6yt",
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
+            "title": "featAuto_measure_allStates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6hew-2w3i",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-05-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
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
-            "identifier": "08e4a98e-066a-54b3-b2e7-0fede5c8f5d9",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard FILTERS vCORESET.1.1-test (coreset-local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/CORESET.1.1-test/20240430/FILTERS.csv",
-                    "description": "Scorecard FILTERS vCORESET.1.1-test (coreset-local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard FILTERS vCORESET.1.1-test (coreset-local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/CORESET.1.1-test/20240430/FILTERS.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard FILTERS vCORESET.1.1-test (coreset-local)"
                 }
             ],
+            "identifier": "08e4a98e-066a-54b3-b2e7-0fede5c8f5d9",
+            "issued": "2024-05-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/6hew-2w3i",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-05-07",
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
+            "title": "Scorecard FILTERS vCORESET.1.1-test (coreset-local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2010",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug-related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 22 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Drug Abuse Warning Network (DAWN-2010) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2010-nid13599",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2010-nid13599"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2010-nid13599",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol",
                 "demographic characteristics",
@@ -21569,76 +21582,32 @@
                 "substance abuse",
                 "suicide"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2010",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2010-nid13599",
-            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug-related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 22 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
-            "title": "Drug Abuse Warning Network (DAWN-2010)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2010-nid13599",
-                    "description": "Drug Abuse Warning Network (DAWN-2010) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2010-nid13599"
-                }
-            ]
+            "title": "Drug Abuse Warning Network (DAWN-2010)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nhis/shs.htm",
+            "accrualPeriodicity": "annual",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
-            "issued": "2024-04-08",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-2023",
-            "modified": "2024-12-05",
-            "references": [
-                "https://wwwn.cdc.gov/NHISDataQueryTool/SHS_adult/SHS_Tech_Notes.pdf"
-            ],
-            "keyword": [
-                "nhis",
-                "sdoh-access-to-health-care",
-                "sdoh-employment",
-                "sdoh-food-access",
-                "sdoh-food-insecurity",
-                "sdoh-higher-education",
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
                 "hasEmail": "mailto:CDCINFO@CDC.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/gpsd-ru5i",
-            "description": "List of footnotes, notes, and source information for NHIS Adult Summary Statistics. Each row of this dataset contains the accompanying text for a footnote found in the NHIS Adults Summary Statistics Dataset.",
-            "title": "DQS NHIS Adult Summary Statistics Footnotes",
-            "isPartOf": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+            "describedBy": "https://wwwn.cdc.gov/NHISDataQueryTool/SHS_adult/SHS_Tech_Notes.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "List of footnotes, notes, and source information for NHIS Adult Summary Statistics. Each row of this dataset contains the accompanying text for a footnote found in the NHIS Adults Summary Statistics Dataset.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21661,43 +21630,57 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://wwwn.cdc.gov/NHISDataQueryTool/SHS_adult/SHS_Tech_Notes.pdf",
+            "identifier": "https://data.cdc.gov/api/views/gpsd-ru5i",
+            "isPartOf": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+            "issued": "2024-04-08",
+            "keyword": [
+                "nhis",
+                "sdoh-access-to-health-care",
+                "sdoh-employment",
+                "sdoh-food-access",
+                "sdoh-food-insecurity",
+                "sdoh-higher-education",
+                "sdoh-housing-stability",
+                "sdoh-poverty-income",
+                "sdoh-source-of-health-care",
+                "sdoh-use-of-health-care",
+                "sdoh-workplace",
+                "summary health statistics"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nhis/shs.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "annual",
+            "modified": "2024-12-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://wwwn.cdc.gov/NHISDataQueryTool/SHS_adult/SHS_Tech_Notes.pdf"
+            ],
+            "rights": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+            "spatial": "United States",
+            "temporal": "2019-2023",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS NHIS Adult Summary Statistics Footnotes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6hze-m9us",
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
-            "identifier": "6a91f80f-e2fd-5f43-8e38-afcebebb8387",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2013",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21705,43 +21688,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "6a91f80f-e2fd-5f43-8e38-afcebebb8387",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/6hze-m9us",
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
+            "title": "State Drug Utilization Data 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/k4xj-uge6",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2016-06-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-27",
-            "keyword": [
-                "fact sheet",
-                "housing",
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
-            "identifier": "https://data.cdc.gov/api/views/k4xj-uge6",
             "description": "Explore the Going Smokefree Matters \u2013 In Your Home Infographic which outlines key facts related to the effects of secondhand smoke exposure in the home.",
-            "title": "Going Smokefree Matters - In Your Home Infographic",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21749,46 +21729,43 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/k4xj-uge6",
+            "issued": "2016-06-15",
+            "keyword": [
+                "fact sheet",
+                "housing",
+                "infographic",
+                "secondhand smoke",
+                "smokefree"
+            ],
+            "landingPage": "https://data.cdc.gov/d/k4xj-uge6",
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
+            "title": "Going Smokefree Matters - In Your Home Infographic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/d2tw-32xv",
+            "accrualPeriodicity": "Biweekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-10-21",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-02-01/2022-12-11",
-            "modified": "2025-01-13",
-            "keyword": [
-                "coronavirus",
-                "covid",
-                "covid19",
-                "covid-19",
-                "laboratory",
-                "prevalence",
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
-            "identifier": "https://data.cdc.gov/api/views/d2tw-32xv",
             "description": "CDC is working with commercial laboratories to conduct large-scale geographic seroprevalence surveys to estimate the percentage of people who were previously infected with SARS-CoV-2, the virus that causes COVID-19 disease. The strategy involves working with state, local, territorial, academic, and commercial partners to better understand COVID-19 in the United States using serology (antibody) testing for surveillance (\u201cseroprevalence surveys\u201d or \u201cserosurveys\u201d). For the surveys, de-identified clinical blood samples are tested for antibodies to SARS-CoV-2.\n\nThis dataset contains the data used to by the Nationwide Commercial Laboratory Seroprevalence Survey interactive visualization available at <a href=\"https://covid.cdc.gov/covid-data-tracker/#national-lab\">https://covid.cdc.gov/covid-data-tracker/#national-lab</a>.\n\nAdditional information is available at <a href=\"https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/commercial-lab-surveys.html\">https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/commercial-lab-surveys.html</a>.",
-            "title": "Nationwide Commercial Laboratory Seroprevalence Survey",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21811,40 +21788,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/d2tw-32xv",
+            "issued": "2020-10-21",
+            "keyword": [
+                "coronavirus",
+                "covid",
+                "covid19",
+                "covid-19",
+                "laboratory",
+                "prevalence",
+                "seroprevalence",
+                "serosurveys"
+            ],
+            "landingPage": "https://data.cdc.gov/d/d2tw-32xv",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Biweekly",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
+            "temporal": "2020-02-01/2022-12-11",
             "theme": [
                 "Laboratory Surveillance"
-            ]
+            ],
+            "title": "Nationwide Commercial Laboratory Seroprevalence Survey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6jkc-yr9c",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-27",
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
-            "identifier": "ff6f5073-b92a-4426-953e-a9a58b19e768",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-03-20-to-2023-03-26",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21853,18 +21838,45 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-03-20-to-2023-03-26"
                 }
             ],
+            "identifier": "ff6f5073-b92a-4426-953e-a9a58b19e768",
+            "issued": "2023-03-28",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/6jkc-yr9c",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-03-27",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-03-20-to-2023-03-26"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6k2v-s5xi",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Glenda R. Lewis",
+                "hasEmail": "mailto:retailfoodprotectionteam@fda.hhs.gov"
+            },
+            "description": "The Food Code Reference System (FCRS) is a searchable database that provides access to FDA\ufffds interpretative positions and responses to questions related to the FDA Food Code.  Users of the FCRS can search the database using dropdown menus, keywords and date. This system is a searchable repository of food code interpretations.  There are no exportable data sets.  All reports are in PDF format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This system is a searchable repository of food code interpretations.  There are no exportable data sets.  All reports are in PDF format.  ",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/fcrs/",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "9B9C0AD1-73D2-4280-A1DE-45D15DDB7386",
             "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2015-01-01",
             "keyword": [
                 "fcrs",
                 "fda food code",
@@ -21873,65 +21885,30 @@
                 "food code interpretations",
                 "food code reference system"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Glenda R. Lewis",
-                "hasEmail": "mailto:retailfoodprotectionteam@fda.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/d/6k2v-s5xi",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2015-01-01",
+            "programCode": [
+                "009:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "9B9C0AD1-73D2-4280-A1DE-45D15DDB7386",
-            "description": "The Food Code Reference System (FCRS) is a searchable database that provides access to FDA\ufffds interpretative positions and responses to questions related to the FDA Food Code.  Users of the FCRS can search the database using dropdown menus, keywords and date. This system is a searchable repository of food code interpretations.  There are no exportable data sets.  All reports are in PDF format.",
-            "title": "Food Code Reference System",
-            "programCode": [
-                "009:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/fcrs/",
-                    "mediaType": "text/html",
-                    "description": "This system is a searchable repository of food code interpretations.  There are no exportable data sets.  All reports are in PDF format.  "
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "Food Code Reference System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/paqx-33a8",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "congenital",
-                "nedss",
-                "netss",
-                "nndss",
-                "primary and secondary",
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
-            "identifier": "https://data.cdc.gov/api/views/paqx-33a8",
             "description": "NNDSS - TABLE 1HH. Syphilis, Congenital to Syphilis, Primary and Secondary \u2013 2020.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1HH. Syphilis, Congenital to Syphilis, Primary and Secondary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21954,20 +21931,56 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/paqx-33a8",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "congenital",
+                "nedss",
+                "netss",
+                "nndss",
+                "primary and secondary",
+                "syphilis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/paqx-33a8",
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
+            "title": "NNDSS - TABLE 1HH. Syphilis, Congenital to Syphilis, Primary and Secondary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2009",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), to analyze general treatment services trends, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.  Data are collected on topics including facility operation, services offered (assessment and pretreatment, pharmacotherapies, testing, transitional, ancillary), detoxification, primary focus (substance abuse, mental health, both, general health, and other), hotline operation, Opioid Treatment Programs and medication dispensed/prescribed, counseling and therapeutic approaches, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2009) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2009-nid13529",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2009-nid13529"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2009-nid13529",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -21980,58 +21993,30 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2009",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2009-nid13529",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), to analyze general treatment services trends, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.  Data are collected on topics including facility operation, services offered (assessment and pretreatment, pharmacotherapies, testing, transitional, ancillary), detoxification, primary focus (substance abuse, mental health, both, general health, and other), hotline operation, Opioid Treatment Programs and medication dispensed/prescribed, counseling and therapeutic approaches, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2009)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2009-nid13529",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2009) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2009-nid13529"
-                }
-            ]
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2009)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6kib-a2qc",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2019-09-24",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-29",
-            "keyword": [
-                "medicaid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Vaughn",
                 "hasEmail": "mailto:no-reply@data.medicaid.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "2b18f2f7-d0f3-5efe-afc4-4881fcbdf200",
             "description": "In fall 2014, the Center for Medicaid and CHIP Services (CMCS) conducted a Nationwide Adult Medicaid (NAM) Consumer Assessment of Healthcare Providers and Systems (CAHPS) survey of Medicaid enrollees to attain national and state-by-state measures of access, barriers to care, and experiences with care across delivery systems and major population subgroups. The survey interviewed a representative sample of adults ages 18 and older enrolled in Medicaid during October through December 2013.\r\nAdditional information, including a data dictionary and analysis guidance and downloadable SAS files are available on the <a href=\"https://www.medicaid.gov/medicaid/quality-of-care/performance-measurement/adult-cahps/index.html\">NAM CAHPS</a> webpage. Please note that all analyses must account for the survey\u2019s sample design and use weights and strata. Sample code is available in on the <a href=\"https://www.medicaid.gov/medicaid/quality-of-care/performance-measurement/adult-cahps/index.html\">NAM CAHPS</a> webpage.",
-            "title": "NAM CAHPS 2014 Public Use",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22040,37 +22025,35 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "2b18f2f7-d0f3-5efe-afc4-4881fcbdf200",
+            "issued": "2019-09-24",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/6kib-a2qc",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2019-11-29",
+            "programCode": [
+                "009:076"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "NAM CAHPS 2014 Public Use"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/sfei-pddr",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-10-15",
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
-            "identifier": "https://data.cdc.gov/api/views/sfei-pddr",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "CDC STATE System E-Cigarette Legislation Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22078,38 +22061,40 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/sfei-pddr",
+            "issued": "2015-10-15",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "https://data.cdc.gov/d/sfei-pddr",
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
                 "Legislation"
-            ]
+            ],
+            "title": "CDC STATE System E-Cigarette Legislation Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6kra-73es",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-03-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-11",
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
-            "identifier": "34f57ab6-0675-4185-b12a-e78d5a915fd5",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-04-2024-to-03-10-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22118,64 +22103,92 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-04-2024-to-03-10-2024"
                 }
             ],
+            "identifier": "34f57ab6-0675-4185-b12a-e78d5a915fd5",
+            "issued": "2024-03-13",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/6kra-73es",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6krm-9nmi",
-            "bureauCode": [
-                "009:38"
+            "modified": "2024-03-11",
+            "programCode": [
+                "009:000"
             ],
-            "issued": "2024-11-13",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-04-2024-to-03-10-2024"
+        },
+        {
             "@type": "dcat:Dataset",
-            "modified": "2024-11-12",
-            "references": [
-                "https://www.mathematica.org/"
-            ],
-            "keyword": [
-                "scorecard",
-                "utility"
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "009:38"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "51548560-0fd0-501d-8bbc-e5695b2ebcfa",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt state v2.10.16 (coreset-dev0)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/state.csv",
-                    "description": "CoreSEt state v2.10.16 (coreset-dev0)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt state v2.10.16 (coreset-dev0)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/state.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt state v2.10.16 (coreset-dev0)"
                 }
             ],
+            "identifier": "51548560-0fd0-501d-8bbc-e5695b2ebcfa",
+            "issued": "2024-11-13",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/6krm-9nmi",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-11-12",
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
+            "title": "CoreSEt state v2.10.16 (coreset-dev0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1982",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This series measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, tobacco, and nonmedical use of prescription drugs among members of United States households aged 12 and older. Questions include age at first use, as well as lifetime, annual, and past-month usage for the following drug classes: cannabis, cocaine, hallucinogens, heroin, alcohol, tobacco, and nonmedical use of prescription drugs, including psychotherapeutics. Respondents were also asked about problems resulting from their use of drugs, alcohol, and tobacco, their perceptions of the risks involved, and personal and family income sources and amounts. Half of the respondents were asked questions regarding substance use by close friends. Demographic data include gender, race, age, ethnicity, educational level, job status, income level, veteran status, household composition, and population density. Youth respondents were also asked about time spent on homework and leisure activities.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1982) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1982-nid13573",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1982-nid13573"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1982-nid13573",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol",
                 "alcohol abuse",
@@ -22202,55 +22215,29 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1982",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1982-nid13573",
-            "description": "<p>This series measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, tobacco, and nonmedical use of prescription drugs among members of United States households aged 12 and older. Questions include age at first use, as well as lifetime, annual, and past-month usage for the following drug classes: cannabis, cocaine, hallucinogens, heroin, alcohol, tobacco, and nonmedical use of prescription drugs, including psychotherapeutics. Respondents were also asked about problems resulting from their use of drugs, alcohol, and tobacco, their perceptions of the risks involved, and personal and family income sources and amounts. Half of the respondents were asked questions regarding substance use by close friends. Demographic data include gender, race, age, ethnicity, educational level, job status, income level, veteran status, household composition, and population density. Youth respondents were also asked about time spent on homework and leisure activities.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-1982)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1982-nid13573",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-1982) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1982-nid13573"
-                }
-            ]
+            "title": "National Household Survey on Drug Abuse (NHSDA-1982)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kuas-t2xn",
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
-            "identifier": "https://data.cdc.gov/api/views/kuas-t2xn",
             "description": "Occupational exposure to 4,4\u2019-methylene diphenyl diisocyanate (MDI), the most widely used monomeric diisocyanate (dNCO), is associated with occupational asthma (OA) development. Recruitment of immune cells to the lung microenvironment via secreted chemokines by alveolar macrophages may play a role during asthma pathogenesis. Our prior study identified that alternatively activated (M2) macrophage-associated markers and chemokines were induced by MDI/MDI-Glutathione (GSH)-mediated Kr\u00fcppel-Like Factor 4 (KLF4) upregulation in macrophages and induced chemotaxis abilities to na\u00efve T-cells and eosinophils; however, the underlying molecular mechanism(s) by which MDI upregulated KLF4 expression is unclear. Previously, we identified that two microRNAs (miRs) including hsa-miR-206-3p and hsa-miR-381-3p were significantly downregulated in MDI-GSH-exposed THP-1 macrophages. In silico analysis revealed that one hsa-miR-206-3p and two hsa-miR-381-3p predicted binding sites exist on the 3\u2019 untranslated region (UTR) of KLF4 transcripts. We hypothesize that MDI/MDI-GSH exposure induces M2 macrophage-associated markers and chemokines through hsa-miR-206-3p/hsa-miR-381-3p mediated KLF4 upregulation in macrophages. The first aim of this study was to examine whether hsa-miR-206-3p/hsa-miR-381-3p regulates KLF4 expression in THP-1 macrophages through a posttranscriptional regulation mechanism. Our second aim was to determine whether hsa-miR-206-3p/hsa-miR-381-3p participates in KLF4-regulated M2 macrophage-associated markers and chemokines after MDI-exposure. After identifying the role of endogenous hsa-miR-206-3p/hsa-miR-381-3p in regulation of KLF4 transcription factor after MDI-exposure, we investigated the role of hsa-miR-206-3p/hsa-miR-381-3p in regulation of M2 macrophage-associated markers and chemokines\u2019 expressions in relation to the exposure to MDI.",
-            "title": "MicroRNA-Mediated Kr\u00fcppel-Like Factor 4 upregulation Induces Alternatively Activated Macrophage-Associated Markers and Chemokines Transcription in 4,4\u2019-Methylene Diphenyl Diisocyanate Exposed Macrophages",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22258,41 +22245,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kuas-t2xn",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/kuas-t2xn",
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
+            "title": "MicroRNA-Mediated Kr\u00fcppel-Like Factor 4 upregulation Induces Alternatively Activated Macrophage-Associated Markers and Chemokines Transcription in 4,4\u2019-Methylene Diphenyl Diisocyanate Exposed Macrophages"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/n44h-hy2j",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2016-11-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
-            "keyword": [
-                "500 cities",
-                "boundaries",
-                "city",
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
-            "identifier": "https://data.cdc.gov/api/views/n44h-hy2j",
             "description": "This city boundary shapefile was extracted from Esri Data and Maps for ArcGIS 2014 - U.S. Populated Place Areas. This shapefile can be joined to 500 Cities city-level Data (GIS Friendly Format) in a geographic information system (GIS) to make city-level maps.",
-            "title": "500 Cities: City Boundaries",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22300,46 +22281,41 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/n44h-hy2j",
+            "issued": "2016-11-08",
+            "keyword": [
+                "500 cities",
+                "boundaries",
+                "city",
+                "shapefile"
+            ],
+            "landingPage": "https://data.cdc.gov/d/n44h-hy2j",
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
+            "title": "500 Cities: City Boundaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kkix-nh4v",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "acute",
-                "chronic",
-                "nedss",
-                "netss",
-                "nndss",
-                "q fever",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/kkix-nh4v",
             "description": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22362,56 +22338,55 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kkix-nh4v",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "acute",
+                "chronic",
+                "nedss",
+                "netss",
+                "nndss",
+                "q fever",
+                "total",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/kkix-nh4v",
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
+            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/end-stage-renal-disease-treatment-choices-model/end-stage-renal-disease-facility-aggregation-group-performance",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-12-01",
-            "temporal": "2021-12-01/2023-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-09",
-            "references": [
-                "https://data.cms.gov/resources/esrd-treatment-choices-etc-model-methodology"
-            ],
-            "keyword": [
-                "clinics",
-                "coordinated care",
-                "end stage renal disease facilities",
-                "hospitals & facilities",
-                "medicare",
-                "original medicare",
-                "outpatient facilities",
-                "service delivery models",
-                "value-based care"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ETC Model - CMMI",
                 "hasEmail": "mailto:ETC-CMMI@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/4bae4223-a1dc-4b9c-bd7e-d9622461be35/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/esrd-facility-aggregation-group-performance-data-dictionary",
             "description": "The End-Stage Renal Disease (ESRD) Facility Aggregation Group Performance dataset provides performance information in the End-Stage Renal Disease (ESRD) Treatment Choices (ETC) Model. The dataset includes information on Performance Payment Adjustment (PPA), Modality Performance Score (MPS), home dialysis rate, and transplant rate, as well as the individual components of each rate for each model participant ESRD facility aggregation group.\n\n\u00a0\n\nAll ESRD facilities\u00a0within the same aggregation group share the same performance information. The supplementary aggregation group crosswalk file may be used to map aggregation groups to individual ETC Participant ESRD facilities.",
-            "title": "End-Stage Renal Disease Facility Aggregation Group Performance",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4bae4223-a1dc-4b9c-bd7e-d9622461be35/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4bae4223-a1dc-4b9c-bd7e-d9622461be35/data",
+                    "mediaType": "text/html",
                     "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2023-06-01"
                 },
                 {
@@ -22463,51 +22438,53 @@
                     "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2021-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/esrd-facility-aggregation-group-performance-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/4bae4223-a1dc-4b9c-bd7e-d9622461be35/data-viewer",
+            "issued": "2023-12-01",
+            "keyword": [
+                "clinics",
+                "coordinated care",
+                "end stage renal disease facilities",
+                "hospitals & facilities",
+                "medicare",
+                "original medicare",
+                "outpatient facilities",
+                "service delivery models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/end-stage-renal-disease-treatment-choices-model/end-stage-renal-disease-facility-aggregation-group-performance",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2024-08-09",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/esrd-treatment-choices-etc-model-methodology"
+            ],
+            "temporal": "2021-12-01/2023-06-30",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "End-Stage Renal Disease Facility Aggregation Group Performance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bqse-bujd",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-            "identifier": "https://data.cdc.gov/api/views/bqse-bujd",
             "description": "NNDSS - Table 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22530,20 +22507,56 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bqse-bujd",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/bqse-bujd",
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
+            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1999",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1999) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1999-nid13634",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1999-nid13634"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1999-nid13634",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -22556,42 +22569,42 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1999",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1999-nid13634",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1999)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1999-nid13634",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1999) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1999-nid13634"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1999)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/namcs.htm",
+            "accrualPeriodicity": "This data will no longer be updated.",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "NAMCS is an annual survey of 3,000 physicians working in nonfederally employed, office-based settings in the 50 U.S. states or Washington, D.C., sampled from the American Medical Association and the American Osteopathic Association master files. Physicians working in specialties of anesthesiology, radiology, or pathology are not eligible to be sampled. Sampled physicians who had retired or were aged 85 or over; were a resident, intern, or fellow; were not principally engaged in patient care activities at the time of the interview; could not be contacted; or were not providing care in an office-based setting were not eligible to complete NAMCS.",
+            "description": "The National Ambulatory Medical Care Survey (NAMCS), conducted by the National Center for Health Statistics (NCHS), collects data from physician offices to describe practice characteristics and patterns of ambulatory care delivery in the United States. After the COVID-19 pandemic began, NCHS added questions to the 2020 and 2021 NAMCS Physician Induction Interview to evaluate physicians\u2019 experiences related to the pandemic. Specifically, physicians in office-based settings were asked about: shortages of personal protective equipment (PPE); experiences with COVID-19 testing; providers in their office who tested positive for COVID-19; turning away COVID-19 patients; and telemedicine or telehealth technology use at their office. Measures related to these topic areas are further described and displayed in data dashboards here: https://www.cdc.gov/nchs/covid19/namcs.htm.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Standard application process link attached.",
+                    "downloadURL": "https://www.cdc.gov/rdc/b3prosal/pp300.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/8kjs-i662",
+            "isPartOf": "https://www.cdc.gov/nchs/covid19/namcs.htm",
             "issued": "2021-12-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-2021",
-            "modified": "2024-03-06",
             "keyword": [
                 "covid",
                 "covid-19",
@@ -22604,47 +22617,47 @@
                 "research-data-center",
                 "telemedicine"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/covid19/namcs.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-03-06",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/8kjs-i662",
-            "description": "The National Ambulatory Medical Care Survey (NAMCS), conducted by the National Center for Health Statistics (NCHS), collects data from physician offices to describe practice characteristics and patterns of ambulatory care delivery in the United States. After the COVID-19 pandemic began, NCHS added questions to the 2020 and 2021 NAMCS Physician Induction Interview to evaluate physicians\u2019 experiences related to the pandemic. Specifically, physicians in office-based settings were asked about: shortages of personal protective equipment (PPE); experiences with COVID-19 testing; providers in their office who tested positive for COVID-19; turning away COVID-19 patients; and telemedicine or telehealth technology use at their office. Measures related to these topic areas are further described and displayed in data dashboards here: https://www.cdc.gov/nchs/covid19/namcs.htm.",
-            "title": "National Ambulatory Medical Care Survey, 2020-2021, restricted physician-only data",
-            "isPartOf": "https://www.cdc.gov/nchs/covid19/namcs.htm",
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
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "United States",
-            "describedBy": "NAMCS is an annual survey of 3,000 physicians working in nonfederally employed, office-based settings in the 50 U.S. states or Washington, D.C., sampled from the American Medical Association and the American Osteopathic Association master files. Physicians working in specialties of anesthesiology, radiology, or pathology are not eligible to be sampled. Sampled physicians who had retired or were aged 85 or over; were a resident, intern, or fellow; were not principally engaged in patient care activities at the time of the interview; could not be contacted; or were not providing care in an office-based setting were not eligible to complete NAMCS.",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "This data will no longer be updated.",
+            "temporal": "2020-2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Ambulatory Medical Care Survey, 2020-2021, restricted physician-only data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1990",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, anabolic steroids, and tobacco<br />\namong members of United States households aged 12 and older. Questions<br />\ninclude age at first use, as well as lifetime, annual, and past-month<br />\nusage for the following drug classes: marijuana, inhalants, cocaine,<br />\nhallucinogens, heroin, alcohol, tobacco, and nonmedical use of<br />\npsychotherapeutics. Respondents were also asked about problems<br />\nresulting from their use of drugs, alcohol, and tobacco, their<br />\nperceptions of the risks involved, insurance coverage, and personal<br />\nand family income sources and amounts. Demographic data include<br />\ngender, race, ethnicity, educational level, job status, income level,<br />\nhousehold composition, and population density.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1990) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1990-nid13628",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1990-nid13628"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1990-nid13628",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "alcohol consumption",
@@ -22670,40 +22683,40 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1990",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1990-nid13628",
-            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, anabolic steroids, and tobacco<br />\namong members of United States households aged 12 and older. Questions<br />\ninclude age at first use, as well as lifetime, annual, and past-month<br />\nusage for the following drug classes: marijuana, inhalants, cocaine,<br />\nhallucinogens, heroin, alcohol, tobacco, and nonmedical use of<br />\npsychotherapeutics. Respondents were also asked about problems<br />\nresulting from their use of drugs, alcohol, and tobacco, their<br />\nperceptions of the risks involved, insurance coverage, and personal<br />\nand family income sources and amounts. Demographic data include<br />\ngender, race, ethnicity, educational level, job status, income level,<br />\nhousehold composition, and population density.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-1990)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1990-nid13628",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-1990) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1990-nid13628"
-                }
-            ]
+            "title": "National Household Survey on Drug Abuse (NHSDA-1990)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-8-year-r-das-nsduh-2002-2009",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This file includes data from the 2002 through 2009 National Survey on Drug Use and Health (NSDUH) survey. The only variables included in the 8-year 2002-2009 data file are ones that were collected in a comparable manner across all 8 years.<br />\nThe National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Certain questions are asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Also included are questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Demographic information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.<br />\nIn the income section, which was interviewer-administered, a split-sample study had been embedded within the 2006 and 2007 surveys to compare a shorter version of the income questions with a longer set of questions that had been used in previous surveys. This shorter version was adopted for the 2008 NSDUH and will be used for future NSDUHs.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health: 8-Year R-DAS (NSDUH-2002-2009) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-8-year-r-das-nsduh-2002-2009-nid13530",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-8-year-r-das-nsduh-2002-2009-nid13530"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-8-year-r-das-nsduh-2002-2009-nid13530",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -22744,55 +22757,29 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-8-year-r-das-nsduh-2002-2009",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-8-year-r-das-nsduh-2002-2009-nid13530",
-            "description": "<p>This file includes data from the 2002 through 2009 National Survey on Drug Use and Health (NSDUH) survey. The only variables included in the 8-year 2002-2009 data file are ones that were collected in a comparable manner across all 8 years.<br />\nThe National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Certain questions are asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Also included are questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Demographic information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.<br />\nIn the income section, which was interviewer-administered, a split-sample study had been embedded within the 2006 and 2007 surveys to compare a shorter version of the income questions with a longer set of questions that had been used in previous surveys. This shorter version was adopted for the 2008 NSDUH and will be used for future NSDUHs.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health: 8-Year R-DAS (NSDUH-2002-2009)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-8-year-r-das-nsduh-2002-2009-nid13530",
-                    "description": "National Survey on Drug Use and Health: 8-Year R-DAS (NSDUH-2002-2009) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-8-year-r-das-nsduh-2002-2009-nid13530"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health: 8-Year R-DAS (NSDUH-2002-2009)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/c8as-e7h6",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-03-23",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-25",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mara Howard-Williams",
                 "hasEmail": "mailto:prw0@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/c8as-e7h6",
             "description": "This dataset contains state and territorial vaccine mandates currently in effect as of ____ that require the group listed to be fully vaccinated. State and territorial laws are collected from publicly available government websites and cataloged and coded using HHS Protect by one coder with one or more additional coders conducting quality assurance.\nData were collected to determine when certain groups were subject to vaccine mandates. Data can be used to determine the status of state-issued vaccine requirements for certain groups as of the date of last update. \nThese data are derived from publicly available state and territorial laws and official policy documents found by CDC\u2019s Mitigation Policy Analysis Unit, and CDC\u2019s Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from July 26, 2021 through _____. These data will be updated as new laws are collected. Any orders not available through publicly accessible websites are not included in this dataset. Recommendations not included in a law are not included in these data. Effective and expiration dates were coded using only the date provided in the law. These data do not necessarily represent the official position of the Centers for Disease Control and Prevention.",
-            "title": "State-Level Vaccine Mandates - Currently in Effect",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22815,45 +22802,35 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/c8as-e7h6",
+            "issued": "2022-03-23",
+            "landingPage": "https://data.cdc.gov/d/c8as-e7h6",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-09-25",
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
+            "title": "State-Level Vaccine Mandates - Currently in Effect"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -22876,21 +22853,70 @@
                     "mediaType": "application/xml"
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-01-04",
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
+            "title": "NNDSS - Table II. Hepatitis (viral, acute, by type) C"
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
+            "description": "Data on delay or nonreceipt of needed medical care, nonreceipt of needed prescription drugs, or nonreceipt of needed dental care during the past 12 months due to cost, in the United States, by selected population characteristics. Data from Health, United States. SOURCE: National Center for Health Statistics, National Health Interview Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/p4r5-qsgs/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/p4r5-qsgs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/p4r5-qsgs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/p4r5-qsgs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/p4r5-qsgs",
             "issued": "2024-04-11",
-            "temporal": "1997/2019",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
             "keyword": [
                 "adults",
                 "american indian or alaska native",
@@ -22917,76 +22943,35 @@
                 "urban population",
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
-            "identifier": "https://data.cdc.gov/api/views/p4r5-qsgs",
-            "description": "Data on delay or nonreceipt of needed medical care, nonreceipt of needed prescription drugs, or nonreceipt of needed dental care during the past 12 months due to cost, in the United States, by selected population characteristics. Data from Health, United States. SOURCE: National Center for Health Statistics, National Health Interview Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Delay or nonreceipt of needed medical care, prescription drugs, or dental care during the past 12 months due to cost: United States",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-05",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/p4r5-qsgs/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/p4r5-qsgs/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/p4r5-qsgs/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/p4r5-qsgs/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "temporal": "1997/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS Delay or nonreceipt of needed medical care, prescription drugs, or dental care during the past 12 months due to cost: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6u68-qupw",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-03-12",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-06",
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
-            "identifier": "586ae752-6d4b-4129-a3f6-569fcab9e104",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-27-to-2023-03-05",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22995,47 +22980,38 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-27-to-2023-03-05"
                 }
             ],
+            "identifier": "586ae752-6d4b-4129-a3f6-569fcab9e104",
+            "issued": "2023-03-12",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/6u68-qupw",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-03-06",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-27-to-2023-03-05"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-medicare-deaths",
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
-                "mortality",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/e1339c5d-8f24-46b0-95ac-32eb8d236f87/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
             "description": "The CMS Program Statistics -\u00a0Medicare Deaths summary tables provide data on Medicare deaths.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR ENROLL AB 33. \u00a0Medicare Deaths: \u00a0Total (Original Medicare and Medicare Advantage and Other Health Plan) Beneficiaries, by Month of Death, Yearly Trend\n\tMDCR ENROLL AB 34. \u00a0Medicare Deaths: \u00a0Total, Original Medicare, and Medicare Advantage and Other Health Plan Beneficiaries, by Demographic Characteristics\n\tMDCR ENROLL AB 35. \u00a0Medicare Deaths: \u00a0Total (Original Medicare and Medicare Advantage and Other Health Plan) Beneficiaries, by Area of Residence\n\tMDCR ENROLL AB 36. \u00a0Medicare Deaths: \u00a0Original Medicare Beneficiaries, by Month of Death, Yearly Trend\n\tMDCR ENROLL AB 37. \u00a0Medicare Deaths: \u00a0Original Medicare Beneficiaries, by Area of Residence\n\tMDCR ENROLL AB 38. \u00a0Medicare Deaths: \u00a0Medicare Advantage and Other Health Plan Beneficiaries, by Month of Death, Yearly Trend\n\tMDCR ENROLL AB 39. \u00a0Medicare Deaths: \u00a0Medicare Advantage and Other Health Plan Beneficiaries, by Area of Residence",
-            "title": "CMS Program Statistics - Medicare Deaths",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23092,44 +23068,53 @@
                     "title": "CMS Program Statistics - Medicare Deaths : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/e1339c5d-8f24-46b0-95ac-32eb8d236f87/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "beneficiary enrollment",
+                "health equity",
+                "medicare",
+                "medicare advantage",
+                "mortality",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-medicare-deaths",
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
+            "title": "CMS Program Statistics - Medicare Deaths"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/STATESystem",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "references": [
-                "https://chronicdata.cdc.gov/d/mhj9-4wi2"
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
-            "identifier": "https://data.cdc.gov/api/views/b2jx-uyck",
+            "describedBy": "https://chronicdata.cdc.gov/Tobacco-Use/U-S-Census-Annual-Estimates-of-the-Resident-Popula/b2jx-uyck",
             "description": "2010-2018; 2019. US Census Annual Estimates of the Resident Population for Selected Age Groups by Sex for the United States. The estimates for the 2010-2018 dataset are based on the 2010 Census and reflect changes to the April 1, 2010 population due to the Count Question Resolution program and geographic program revisions. Median age is calculated based on single year of age. The estimates for 2019 are based on a one-year dataset that was published on the US Census website in 2021. For population estimates methodology statements, see http://www.census.gov/popest/methodology/index.html.",
-            "title": "US Census Annual Estimates of the Resident Population for Selected Age Groups by Sex for the United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23152,40 +23137,38 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Tobacco-Use/U-S-Census-Annual-Estimates-of-the-Resident-Popula/b2jx-uyck",
+            "identifier": "https://data.cdc.gov/api/views/b2jx-uyck",
+            "issued": "2025-01-31",
+            "landingPage": "http://www.cdc.gov/STATESystem",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://chronicdata.cdc.gov/d/mhj9-4wi2"
+            ],
             "theme": [
                 "Funding"
-            ]
+            ],
+            "title": "US Census Annual Estimates of the Resident Population for Selected Age Groups by Sex for the United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/genbank/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/gt3p-8c5s",
             "description": "NIH Genetic sequence database; an annotated collection of all publicly available DNA sequences.",
-            "title": "GenBank",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23194,88 +23177,88 @@
                     "title": "GenBank Homepage, Search, and Utilities"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/gt3p-8c5s",
+            "issued": "2021-06-30",
+            "keyword": [
+                "genetics",
+                "genomics"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/genbank/",
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
+            "title": "GenBank"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6vsi-hayn",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-08-31",
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
-            "identifier": "bbd82935-a2ad-54b9-ad95-fbbee436a4e7",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_measureSearchInfo",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measureSearchInfo.csv",
-                    "description": "{\"dataset\": \"measureSearchInfo\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measureSearchInfo\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measureSearchInfo.csv",
+                    "mediaType": "text/csv",
                     "title": "measureSearchInfo csv file"
                 }
             ],
+            "identifier": "bbd82935-a2ad-54b9-ad95-fbbee436a4e7",
+            "issued": "2022-08-31",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/6vsi-hayn",
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
+            "title": "implAuto_measureSearchInfo"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6w5e-rnru",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2020-07-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-10-14",
-            "keyword": [
-                "core sets",
-                "performance rates",
-                "quality measures"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RajB",
                 "hasEmail": "mailto:hanraj.balasubramanian@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "e36d89c0-f62e-56d5-bc7e-b0adf89262b8",
             "description": "Performance rates on frequently reported health care quality measures in the CMS Medicaid/CHIP Child and Adult Core Sets, for FFY 2019 reporting.\r\n\r\nSource: Mathematica analysis of MACPro and Form CMS-416 reports for the FFY 2019 reporting cycle. Dataset revised October 2020. For more information, see the Children's Health Care Quality Measures and Adult Health Care Quality Measures webpages.",
-            "title": "2019 Child and Adult Health Care Quality Measures Quality",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23284,52 +23267,49 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "e36d89c0-f62e-56d5-bc7e-b0adf89262b8",
+            "issued": "2020-07-22",
+            "keyword": [
+                "core sets",
+                "performance rates",
+                "quality measures"
+            ],
+            "landingPage": "https://healthdata.gov/d/6w5e-rnru",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-10-14",
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
+            "title": "2019 Child and Adult Health Care Quality Measures Quality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/innovation-center-model-awardees",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2017-01-01/2017-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-22",
-            "references": [
-                "https://data.cms.gov/resources/model-awardees-methodology"
-            ],
-            "keyword": [
-                "medicare",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/424de599-7a34-4243-af70-95d24dd675dd/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/model-awardees-data-dictionary",
             "description": "The Innovation Center Model Awardees dataset provides information about institutions that have participated in the model process, and have been awarded funding based on their efforts to design, implement, or test innovative healthcare delivery initiatives. The data includes the name of the institution, related keywords, project name, geographic reach, funding amount, real or projected 3-year savings, a summary of the institutions activities in the model, categories related to the type of healthcare initiative, stage of participation, and the URL for the model or initiative page on the CMMI website.",
-            "title": "Innovation Center Model Awardees",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/424de599-7a34-4243-af70-95d24dd675dd/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/424de599-7a34-4243-af70-95d24dd675dd/data",
+                    "mediaType": "text/html",
                     "title": "Innovation Center Model Awardees : 2017-09-15"
                 },
                 {
@@ -23345,57 +23325,49 @@
                     "title": "Innovation Center Model Awardees : 2017-09-15"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/model-awardees-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/424de599-7a34-4243-af70-95d24dd675dd/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/innovation-center-model-awardees",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2021-06-22",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/model-awardees-methodology"
+            ],
+            "temporal": "2017-01-01/2017-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Innovation Center Model Awardees"
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
-            "modified": "2024-08-23",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
-            "keyword": [
-                "behaviors",
-                "brfss",
-                "county",
-                "disability",
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
-            "identifier": "https://data.cdc.gov/api/views/h3ej-a9ec",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
             "description": "This dataset contains model-based county estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. This dataset includes estimates for 36 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2021 or 2020 county population estimate data, and American Community Survey 2017\u20132021, or 2016\u20132020 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. More information about the methodology can be found at  www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, County Data 2023 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23418,22 +23390,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
+            "identifier": "https://data.cdc.gov/api/views/h3ej-a9ec",
+            "issued": "2024-07-15",
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
-            "theme": [
-                "500 Cities & Places"
-            ]
+            "modified": "2024-08-23",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-        {
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "theme": [
+                "500 Cities & Places"
+            ],
+            "title": "PLACES: Local Data for Better Health, County Data 2023 release"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.hcup-us.ahrq.gov/db/state/sedddbdocumentation.jsp",
             "bureauCode": [
                 "009:33"
             ],
-            "rights": "N/A",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HCUP Technical Support",
+                "hasEmail": "mailto:hcup@ahrq.gov"
+            },
+            "describedBy": "https://www.hcup-us.ahrq.gov/db/state/sedddbdocumentation.jsp",
+            "description": "The Healthcare Cost and Utilization Project (HCUP) State Emergency Department Databases (SEDD) contain the universe of emergency department visits in participating States. The data are translated into a uniform format to facilitate multi-State comparisons and analyses. The SEDD consist of data from hospital-based emergency department visits that do not result in an admission.  The SEDD include all patients, regardless of the expected payer including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge\u2019. Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality (AHRQ), HCUP data inform decision making at the national, State, and community levels.\n\nThe SEDD contain clinical and resource use information included in a typical discharge abstract, with safeguards to protect the privacy of individual patients, physicians, and facilities (as required by data sources). Data elements include but are not limited to: diagnoses, procedures, admission and discharge status, patient demographics (e.g., gender, age, race), total charges, length of stay, and expected payment source, including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge\u2019. In addition to the core set of uniform data elements common to all SEDD, some include State-specific data elements. The SEDD exclude data elements that could directly or indirectly identify individuals. For some States, hospital and county identifiers are included that permit linkage to the American Hospital Association Annual Survey File and the Bureau of Health Professions' Area Resource File except in States that do not allow the release of hospital identifiers.\n\nRestricted access data files are available with a data use agreement and brief online security training.",
+            "identifier": "2b348273-0524-432c-92dd-f386f134300e",
             "issued": "2012-11-11",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "claims",
                 "community health",
@@ -23450,57 +23454,35 @@
                 "sexual assault",
                 "utilization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HCUP Technical Support",
-                "hasEmail": "mailto:hcup@ahrq.gov"
-            },
+            "landingPage": "https://www.hcup-us.ahrq.gov/db/state/sedddbdocumentation.jsp",
+            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:074"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
             },
-            "identifier": "2b348273-0524-432c-92dd-f386f134300e",
-            "description": "The Healthcare Cost and Utilization Project (HCUP) State Emergency Department Databases (SEDD) contain the universe of emergency department visits in participating States. The data are translated into a uniform format to facilitate multi-State comparisons and analyses. The SEDD consist of data from hospital-based emergency department visits that do not result in an admission.  The SEDD include all patients, regardless of the expected payer including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge\u2019. Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality (AHRQ), HCUP data inform decision making at the national, State, and community levels.\n\nThe SEDD contain clinical and resource use information included in a typical discharge abstract, with safeguards to protect the privacy of individual patients, physicians, and facilities (as required by data sources). Data elements include but are not limited to: diagnoses, procedures, admission and discharge status, patient demographics (e.g., gender, age, race), total charges, length of stay, and expected payment source, including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge\u2019. In addition to the core set of uniform data elements common to all SEDD, some include State-specific data elements. The SEDD exclude data elements that could directly or indirectly identify individuals. For some States, hospital and county identifiers are included that permit linkage to the American Hospital Association Annual Survey File and the Bureau of Health Professions' Area Resource File except in States that do not allow the release of hospital identifiers.\n\nRestricted access data files are available with a data use agreement and brief online security training.",
-            "title": "HCUP State Emergency Department Databases (SEDD) - Restricted Access File",
-            "programCode": [
-                "009:074"
-            ],
-            "describedBy": "https://www.hcup-us.ahrq.gov/db/state/sedddbdocumentation.jsp",
-            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx",
+            "rights": "N/A",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "HCUP State Emergency Department Databases (SEDD) - Restricted Access File"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -23523,71 +23505,94 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6xn7-gg85",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-06-09",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-07",
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
-            "identifier": "10ebe487-2deb-5e03-88bc-9d847fca5d76",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard TAG v0.3.1-1 (etl_test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.1-1/TAG.csv",
-                    "description": "Scorecard TAG v0.3.1-1 (etl_test)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard TAG v0.3.1-1 (etl_test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.1-1/TAG.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard TAG v0.3.1-1 (etl_test)"
                 }
             ],
+            "identifier": "10ebe487-2deb-5e03-88bc-9d847fca5d76",
+            "issued": "2023-06-09",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/6xn7-gg85",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-06-07",
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
+            "title": "Scorecard TAG v0.3.1-1 (etl_test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/CMS-Statistics/6xwe-dket",
             "bureauCode": [
                 "009:38"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": false,
+            "description": "<p>This reference provides significant summary information about health expenditures and the Centers for Medicare &amp; Medicaid Services' (CMS) programs. The information presented was the most current available at the time of publication. Significant time lags may occur between the end of a data year and aggregation of data for that year.</p>",
+            "identifier": "497f3c85-d7e8-44c4-83c1-c04f966ceccb",
             "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-18",
             "keyword": [
                 "cms",
                 "community health",
@@ -23600,37 +23605,36 @@
                 "statistics",
                 "utilization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/CMS-Statistics/6xwe-dket",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2024-03-18",
+            "programCode": [
+                "009:078"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Medicare & Medicaid Services, Department of Health & Human Services"
             },
-            "identifier": "497f3c85-d7e8-44c4-83c1-c04f966ceccb",
-            "description": "<p>This reference provides significant summary information about health expenditures and the Centers for Medicare &amp; Medicaid Services' (CMS) programs. The information presented was the most current available at the time of publication. Significant time lags may occur between the end of a data year and aggregation of data for that year.</p>",
-            "title": "CMS Statistics",
-            "programCode": [
-                "009:078"
-            ],
-            "dataQuality": false,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "CMS Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.hcup-us.ahrq.gov/db/nation/kid/kiddbdocumentation.jsp",
             "bureauCode": [
                 "009:33"
             ],
-            "rights": "N/A",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HCUP Technical Support",
+                "hasEmail": "mailto:hcup@ahrq.gov"
+            },
+            "describedBy": "https://www.hcup-us.ahrq.gov/db/nation/kid/kiddbdocumentation.jsp",
+            "description": "The Healthcare Cost and Utilization Project (HCUP) Kids' Inpatient Database (KID) is the largest publicly available all-payer pediatric inpatient care database in the United States, containing data from two to three million hospital stays each year. Its large sample size is ideal for developing national and regional estimates and enables analyses of rare conditions, such as congenital anomalies, as well as uncommon treatments, such as organ transplantation. Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality, HCUP data inform decision making at the national, State, and community levels.\n\nThe KID is a sample of pediatric discharges from 4,000 U.S. hospitals in the HCUP State Inpatient Databases yielding approximately two to three million unweighted hospital discharges for newborns, children, and adolescents per year. About 10 percent of normal newborns and 80 percent of other neonatal and pediatric stays are selected from each hospital that is sampled for patients younger than 21 years of age. \n\nThe KID contains clinical and resource use information included in a typical discharge abstract, with safeguards to protect the privacy of individual patients, physicians, and hospitals (as required by data sources). It includes discharge status, diagnoses, procedures, patient demographics (e.g., sex, age), expected source of primary payment (e.g., Medicare, Medicaid, private insurance, self-pay, and other insurance types), and hospital charges and cost.\n\nRestricted access data files are available with a data use agreement and brief online security training.",
+            "identifier": "7f696142-9d9e-452f-af1a-3568c3c4bd11",
             "issued": "2021-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "claims",
                 "diagnoses",
@@ -23647,54 +23651,32 @@
                 "procedures",
                 "utilization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HCUP Technical Support",
-                "hasEmail": "mailto:hcup@ahrq.gov"
-            },
+            "landingPage": "https://www.hcup-us.ahrq.gov/db/nation/kid/kiddbdocumentation.jsp",
+            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:015"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
             },
-            "identifier": "7f696142-9d9e-452f-af1a-3568c3c4bd11",
-            "description": "The Healthcare Cost and Utilization Project (HCUP) Kids' Inpatient Database (KID) is the largest publicly available all-payer pediatric inpatient care database in the United States, containing data from two to three million hospital stays each year. Its large sample size is ideal for developing national and regional estimates and enables analyses of rare conditions, such as congenital anomalies, as well as uncommon treatments, such as organ transplantation. Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality, HCUP data inform decision making at the national, State, and community levels.\n\nThe KID is a sample of pediatric discharges from 4,000 U.S. hospitals in the HCUP State Inpatient Databases yielding approximately two to three million unweighted hospital discharges for newborns, children, and adolescents per year. About 10 percent of normal newborns and 80 percent of other neonatal and pediatric stays are selected from each hospital that is sampled for patients younger than 21 years of age. \n\nThe KID contains clinical and resource use information included in a typical discharge abstract, with safeguards to protect the privacy of individual patients, physicians, and hospitals (as required by data sources). It includes discharge status, diagnoses, procedures, patient demographics (e.g., sex, age), expected source of primary payment (e.g., Medicare, Medicaid, private insurance, self-pay, and other insurance types), and hospital charges and cost.\n\nRestricted access data files are available with a data use agreement and brief online security training.",
-            "title": "HCUP Kids' Inpatient Database (KID) - Restricted Access File",
-            "programCode": [
-                "009:015"
-            ],
-            "describedBy": "https://www.hcup-us.ahrq.gov/db/nation/kid/kiddbdocumentation.jsp",
-            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx"
+            "rights": "N/A",
+            "title": "HCUP Kids' Inpatient Database (KID) - Restricted Access File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6ycm-taqf",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-08-10",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-17",
-            "keyword": [
-                "exchange puf",
-                "marketplace puf",
-                "plan attributes",
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
-            "identifier": "cbfda538-6b7b-476a-a667-19212b853629",
             "description": "The Plan Attributes PUF (Plan-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Plan-PUF contains plan variant-level data on maximum out of pocket payments, deductibles, health savings account (HSA) eligibility, and other plan attributes.",
-            "title": "Plan Attributes PUF - PY2022",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23702,37 +23684,38 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "cbfda538-6b7b-476a-a667-19212b853629",
+            "issued": "2022-08-10",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "plan attributes",
+                "py2022"
+            ],
+            "landingPage": "https://healthdata.gov/d/6ycm-taqf",
+            "modified": "2022-08-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Plan Attributes PUF - PY2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6ygp-x4nf",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2014-11-07",
-            "temporal": "2017-01-01T00:00:00+00:00/2018-01-01T00:00:00+00:00",
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
-            "identifier": "1c5d0fc9-693a-534a-8240-4627d9362b0d",
             "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
-            "title": "NADAC (National Average Drug Acquisition Cost) 2017",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23741,40 +23724,41 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "1c5d0fc9-693a-534a-8240-4627d9362b0d",
+            "issued": "2014-11-07",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "landingPage": "https://healthdata.gov/d/6ygp-x4nf",
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
+            "temporal": "2017-01-01T00:00:00+00:00/2018-01-01T00:00:00+00:00",
             "theme": [
                 "National Average Drug Acquisition Cost",
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "NADAC (National Average Drug Acquisition Cost) 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/6yxg-v436",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-10-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-22",
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
-            "identifier": "50a46484-9a54-42d0-8da6-509a8b5656c0",
             "description": "All states (including the District of Columbia) are required to provide data to The Centers for Medicare &amp; Medicaid Services (CMS) on a range of indicators related to key application, eligibility, and enrollment processes within the state Medicaid and Children\u2019s Health Insurance Programs (CHIP). These data reflect enrollment activity for all populations receiving comprehensive Medicaid and CHIP benefits in all states, as well as state program performance.",
-            "title": "PI dataset",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23782,18 +23766,47 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "50a46484-9a54-42d0-8da6-509a8b5656c0",
+            "issued": "2024-10-23",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/6yxg-v436",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-22",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "PI dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-mortality-underlying-cause-death",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/cmf.html",
+            "description": "<p>The CDC WONDER Mortality - Underlying Cause of Death online database is a county-level national mortality and population database spanning the years since 1979.  Data are updated annually. The number of deaths, crude death rates, age-adjusted death rates, standard errors and confidence intervals for death rates can be obtained by place of residence (total U.S., Census region, Census division, state, and county), age group (including infant age groups), race (years 1979-1998: White, Black, and Other; years 1999-present: American Indian or Alaska Native, Asian or Pacific Islander, Black or African American, and White), Hispanic origin (years 1979-1998: not available; years 1999-present: Hispanic or Latino, not Hispanic or Latino, Not Stated), gender, year of death, and underlying cause ofdeath (years 1979-1998: 4-digit ICD-9 code and 72 cause-of-death recode; years 1999-present: 4-digit ICD-10 codes and 113 cause-of-death recode, as well as the Injury Mortality matrix classification for Intent and Mechanism), and urbanization level of residence (2006 NCHS urban-rural classification scheme for counties).  The data are produced by the National Center for Health Statistics.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/mortSQL.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "1321ae3e-d8d7-4c9a-8f36-f53c10912853",
             "issued": "2012-05-30",
-            "temporal": "1999-01-01T00:00:00-05:00/2007-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "age",
                 "births",
@@ -23813,77 +23826,36 @@
                 "state",
                 "urbanization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-mortality-underlying-cause-death",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "1321ae3e-d8d7-4c9a-8f36-f53c10912853",
-            "description": "<p>The CDC WONDER Mortality - Underlying Cause of Death online database is a county-level national mortality and population database spanning the years since 1979.  Data are updated annually. The number of deaths, crude death rates, age-adjusted death rates, standard errors and confidence intervals for death rates can be obtained by place of residence (total U.S., Census region, Census division, state, and county), age group (including infant age groups), race (years 1979-1998: White, Black, and Other; years 1999-present: American Indian or Alaska Native, Asian or Pacific Islander, Black or African American, and White), Hispanic origin (years 1979-1998: not available; years 1999-present: Hispanic or Latino, not Hispanic or Latino, Not Stated), gender, year of death, and underlying cause ofdeath (years 1979-1998: 4-digit ICD-9 code and 72 cause-of-death recode; years 1999-present: 4-digit ICD-10 codes and 113 cause-of-death recode, as well as the Injury Mortality matrix classification for Intent and Mechanism), and urbanization level of residence (2006 NCHS urban-rural classification scheme for counties).  The data are produced by the National Center for Health Statistics.</p>",
-            "title": "CDC WONDER: Mortality - Underlying Cause of Death",
-            "programCode": [
-                "009:048"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://wonder.cdc.gov/mortSQL.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/cmf.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1999-01-01T00:00:00-05:00/2007-12-31T00:00:00-05:00",
             "theme": [
                 "Health",
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Mortality - Underlying Cause of Death"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-06-15",
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
-            "identifier": "https://data.cdc.gov/api/views/gd4x-jyhw",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-ZCTA-Data-2020/qnzd-25i4",
             "description": "This dataset contains model-based ZIP Code Tabulation Area (ZCTA) level estimates for the PLACES 2022 release. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 29 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2010 population data, and American Community Survey 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, ZCTA Data 2022 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23906,42 +23878,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-ZCTA-Data-2020/qnzd-25i4",
+            "identifier": "https://data.cdc.gov/api/views/gd4x-jyhw",
+            "issued": "2023-06-15",
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
+            "title": "PLACES: Local Data for Better Health, ZCTA Data 2022 release"
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
-                "iis",
-                "immunization information system",
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
-            "identifier": "https://data.cdc.gov/api/views/scrf-8d7w",
             "description": "Monthly Cumulative Number and Percent of Adults 60 Years and Older Who Received at least one RSV Vaccination Doses by Jurisdiction\n\n\u2022 Estimated Respiratory Syncytial Virus (RSV) vaccination coverage for adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems (IIS) data, submitted from jurisdictions to CDC monthly in aggregate by age group.\n\n \u2022 Starting in July 2023, the CDC recommended the RSV vaccine to protect against serious illness from RSV. (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)\n\u2003",
-            "title": "Monthly Cumulative Number and Percent of Adults 60 Years and Older Who Received at least one RSV Vaccination Doses by Jurisdiction, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23964,40 +23946,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Jurisdictions - States, District of Columbia, Islands, and US cities",
+            "identifier": "https://data.cdc.gov/api/views/scrf-8d7w",
+            "issued": "2024-02-09",
+            "keyword": [
+                "iis",
+                "immunization information system",
+                "rsv vaccination"
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
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "Jurisdictions - States, District of Columbia, Islands, and US cities",
+            "temporal": "2023-2024",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Monthly Cumulative Number and Percent of Adults 60 Years and Older Who Received at least one RSV Vaccination Doses by Jurisdiction, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rbj6-gv57",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Pathology and Physiology Research Branch (PPRB), Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rbj6-gv57",
             "description": "Nanotechnology is one of the most rapidly developing areas of the economy and involves the study and control of matter in the nanoscale. The nanoscale is the size range from 1 to 100 nm. Recently, some nanomaterials have demonstrated the ability to enter the brain through the olfactory pathway from the nose to the brain. \u2060This pathway can potentially enable inhaled nanomaterials to enter the brain. Inhalation exposures are technically difficult and expensive. Intranasal instillation is a potential screening tool for evaluating nose to brain transport. However, particles in aqueous media tend to agglomerate and agglomerated particles often act like larger particles in terms of surface area, toxicity, and size thresholds for transport pathways. For neuronal transport within the brain, the upper size limit is estimated to be approximately 100 nm. Therefore, nanomaterials must be adequately dispersed in the vehicle used for instillation in order to evaluate their potential for transport from the nose to the brain.\n\nBecause 100 nm is the upper size limit estimated for transport within the central nervous system, components of dispersion media may need to be different from dispersion media used to evaluate toxicity in other tissues. For example, albumin, a protein which is useful in dispersion media developed for the lung, can interact with nanomaterials and increase their size. In addition, neurons transport sodium out of the cell, suggesting that a dispersion medium to evaluate nose-to-brain transport should avoid high sodium concentrations. To overcome issues with the size of albumin and other proteins as well as the potential effects of sodium and phosphate, we hypothesized that free amino acids, a balanced electrolyte solution, and a mixture of phospholipids could produce a solution that both dispersed nanomaterials and was compatible with neuronal transport. This study describes and characterizes a solution for nasal and olfactory transport (SNOT) that can disperse nanomaterials and dyes with nanoscale dimensions, enabling intranasal instillation so that potential nose-to-brain transport can be evaluated.",
-            "title": "Developing a Solution for Nasal and Olfactory Transport of Nanomaterials",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24005,44 +23992,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rbj6-gv57",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/rbj6-gv57",
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
+            "title": "Developing a Solution for Nasal and Olfactory Transport of Nanomaterials"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/d4v7-r7ct",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/d4v7-r7ct",
             "description": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis\n\nNNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24065,43 +24043,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/d4v7-r7ct",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "cryptosporidiosis",
+                "cyclosporiasis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/d4v7-r7ct",
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
+            "title": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-visualization/mortality-trends/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-07-14",
-            "@type": "dcat:Dataset",
-            "temporal": "1915/2013",
-            "modified": "2022-03-30",
-            "keyword": [
-                "infant",
-                "mortality",
-                "nchs",
-                "neonatal",
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
-            "identifier": "https://data.cdc.gov/api/views/epev-k6ss",
             "description": "Rates are infants (under 1 year) and neonatal (under 28 days) deaths per 1,000 live births.\r\n\r\nhttps://www.cdc.gov/nchs/data-visualization/mortality-trends/",
-            "title": "NCHS - Infant and neonatal mortality rates: United States, 1915-2013",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24124,41 +24103,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/epev-k6ss",
+            "issued": "2015-07-14",
+            "keyword": [
+                "infant",
+                "mortality",
+                "nchs",
+                "neonatal",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/mortality-trends/",
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
+            "temporal": "1915/2013",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - Infant and neonatal mortality rates: United States, 1915-2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/73cb-dczt",
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
-            "identifier": "bb63ad8e-cab1-56e3-b492-da95d7e8cc5f",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2007",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24166,41 +24149,41 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "bb63ad8e-cab1-56e3-b492-da95d7e8cc5f",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/73cb-dczt",
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
+            "title": "State Drug Utilization Data 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/73du-vigx",
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
-            "identifier": "0a2ec693-b322-54fb-a950-dfcdc873e3cf",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2006",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24208,21 +24191,51 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "0a2ec693-b322-54fb-a950-dfcdc873e3cf",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/73du-vigx",
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
+            "title": "State Drug Utilization Data 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2005-0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) primarily<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions included age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovered substance abuse treatment history and perceived need for<br />\ntreatment, and included questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey included questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents were<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2005 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, drug use by friends,<br />\nsocial support, extracurricular activities, exposure to substance<br />\nabuse prevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Several measures<br />\nfocused on prevention-related themes in this section. Also retained<br />\nwere questions on mental health and access to care, perceived risk of<br />\nusing drugs, perceived availability of drugs, driving and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey. Background information<br />\nincludes gender, race, age, ethnicity, marital status, educational<br />\nlevel, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2005) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2005-nid13606",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2005-nid13606"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2005-nid13606",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -24260,40 +24273,40 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2005-0",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2005-nid13606",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) primarily<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions included age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovered substance abuse treatment history and perceived need for<br />\ntreatment, and included questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey included questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents were<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2005 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, drug use by friends,<br />\nsocial support, extracurricular activities, exposure to substance<br />\nabuse prevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Several measures<br />\nfocused on prevention-related themes in this section. Also retained<br />\nwere questions on mental health and access to care, perceived risk of<br />\nusing drugs, perceived availability of drugs, driving and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey. Background information<br />\nincludes gender, race, age, ethnicity, marital status, educational<br />\nlevel, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health (NSDUH-2005)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2005-nid13606",
-                    "description": "National Survey on Drug Use and Health (NSDUH-2005) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2005-nid13606"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health (NSDUH-2005)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1995",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1995) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1995-nid13610",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1995-nid13610"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1995-nid13610",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -24306,73 +24319,38 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1995",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1995-nid13610",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1995)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1995-nid13610",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1995) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1995-nid13610"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1995)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/accountable-care-organizations",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2014-01-01/2025-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://data.cms.gov/resources/acos-aco-participants-and-snf-affiliates-methodology"
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
                 "fn": "Shared Savings Program - CM",
                 "hasEmail": "mailto:SharedSavingsProgram@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/69ec2609-5ce5-4ce1-b14c-1f8809fda2c2/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/accountable-care-organizations-data-dictionary",
             "description": "The\u00a0Accountable Care Organizations data\u00a0provides information on ACOs participating in the Medicare Shared Savings Program (Shared Savings Program), including their name, track status, number of years in the program, and contact information for key personnel.\u00a0\n\n\u00a0\n\nDISCLAIMER: This information is current as of the last update. Changes to ACO information occur periodically. Each ACO has the most up-to-date information about their organization. Consider contacting the ACO for the latest information.",
-            "title": "Accountable Care Organizations",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/69ec2609-5ce5-4ce1-b14c-1f8809fda2c2/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/69ec2609-5ce5-4ce1-b14c-1f8809fda2c2/data",
+                    "mediaType": "text/html",
                     "title": "Accountable Care Organizations : 2025-01-15"
                 },
                 {
@@ -24532,136 +24510,132 @@
                     "title": "Accountable Care Organizations : 2014-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/accountable-care-organizations-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/69ec2609-5ce5-4ce1-b14c-1f8809fda2c2/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/accountable-care-organizations",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/acos-aco-participants-and-snf-affiliates-methodology"
+            ],
+            "temporal": "2014-01-01/2025-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accountable Care Organizations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/74vp-x3pk",
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
-            "identifier": "23254130-7c29-51ff-a442-32f7fd9b9bde",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_map",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/map.csv",
-                    "description": "{\"dataset\": \"map\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"map\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/map.csv",
+                    "mediaType": "text/csv",
                     "title": "map csv file"
                 }
             ],
+            "identifier": "23254130-7c29-51ff-a442-32f7fd9b9bde",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/74vp-x3pk",
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
+            "title": "devAuto_map"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.uniprot.org/",
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
                 "fn": "PILLAI, AJAY",
                 "hasEmail": "mailto:ajaydr@mail.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "6313d629-6ef8-44d3-b766-0d61dd8a90d4",
+            "dataQuality": true,
             "description": "<p>The Universal Protein Resource (UniProt) is a comprehensive resource for protein sequence and annotation data. The UniProt databases are the UniProt Knowledgebase (UniProtKB), the UniProt Reference Clusters (UniRef), and the UniProt Archive (UniParc).</p>",
-            "title": "The Universal Protein Resource (UniProt)",
+            "identifier": "6313d629-6ef8-44d3-b766-0d61dd8a90d4",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.uniprot.org/",
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
+            "title": "The Universal Protein Resource (UniProt)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-03-25",
-            "temporal": "2018/2020",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "deaths",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
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
-            "identifier": "https://data.cdc.gov/api/views/w56u-89fn",
             "description": "Death counts by age, sex, and week for years 2018-2020.  Data for 2018 and 2019 are final.  Data for 2020 are provisional.",
-            "title": "AH Deaths by Week, Sex, and Age for 2018-2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24684,61 +24658,50 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/w56u-89fn",
+            "issued": "2021-03-25",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "sex",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
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
+            "temporal": "2018/2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Deaths by Week, Sex, and Age for 2018-2020"
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
-            "identifier": "https://data.cdc.gov/api/views/u93h-quup",
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2001/u93h-quup",
             "description": "2001. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2001",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24761,77 +24724,90 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2001/u93h-quup",
+            "identifier": "https://data.cdc.gov/api/views/u93h-quup",
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
+            "title": "CDC PRAMStat Data for 2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.wormbase.org/#012-3-6",
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
                 "fn": "GOOD, PETER J.",
                 "hasEmail": "mailto:goodp@mail.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "0d8198dc-ba28-4f8b-87ac-b088ec9338d4",
+            "dataQuality": true,
             "description": "<p>WormBase is an international consortium of biologists and computer scientists dedicated to providing the research community with accurate, current, accessible information concerning the genetics, genomics and biology of C. elegans and related nematodes.</p>",
-            "title": "WormBase",
-            "programCode": [
-                "009:003"
+            "identifier": "0d8198dc-ba28-4f8b-87ac-b088ec9338d4",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
             ],
+            "landingPage": "http://www.wormbase.org/#012-3-6",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "dataQuality": true
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "title": "WormBase"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9kbf-icdi",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "brucellosis",
-                "campylobacteriosis",
-                "candida auris",
-                "clinical",
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
-            "identifier": "https://data.cdc.gov/api/views/9kbf-icdi",
             "description": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Reporting jurisdictions were informed CDC could receive data for this condition in August 2019. Please note there will be a delay in reporting of case notifications for this condition to CDC.",
-            "title": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24854,38 +24830,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9kbf-icdi",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "brucellosis",
+                "campylobacteriosis",
+                "candida auris",
+                "clinical",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9kbf-icdi",
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
+            "title": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.ncbi.nlm.nih.gov/dbvar/",
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
                 "fn": "Phan, Lon",
                 "hasEmail": "mailto:lonphan@ncbi.nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "94317aa7-2d78-469d-99ea-17b353ca9de2",
+            "dataQuality": true,
             "description": "<p>dbVar is a database of genomic structural variation. It accepts data from all species and includes clinical data. It can accept diverse types of events, including inversions, insertions and translocations. Additionally, both germline and somatic variants are accepted.</p>",
-            "title": "dbVar",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24894,43 +24879,39 @@
                     "title": "dbVar"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "94317aa7-2d78-469d-99ea-17b353ca9de2",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.ncbi.nlm.nih.gov/dbvar/",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:041"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "dbVar"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/778a-rfm8",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-08-09",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-16",
-            "keyword": [
-                "py2023",
-                "qhp",
-                "qhp landscape instructions",
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
-            "identifier": "a1e624b6-764b-449f-ae88-05aacd5162cd",
             "description": "The Medical SHOP Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2023 Medical SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24938,45 +24919,39 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "a1e624b6-764b-449f-ae88-05aacd5162cd",
+            "issued": "2023-08-09",
+            "keyword": [
+                "py2023",
+                "qhp",
+                "qhp landscape instructions",
+                "shop",
+                "shop market medical"
+            ],
+            "landingPage": "https://healthdata.gov/d/778a-rfm8",
+            "modified": "2023-08-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2023 Medical SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.cdc.gov/brfss/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://www.cdc.gov/brfss/"
-            ],
-            "keyword": [
-                "...",
-                "behavioral",
-                "brfss",
-                "county",
-                "factor",
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
-            "identifier": "https://data.cdc.gov/api/views/cpem-dkkm",
+            "describedBy": "https://chronicdata.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factors-Selected-Metropolitan-Area/cpem-dkkm",
             "description": "2011 to 2012. BRFSS SMART County Prevalence combined land line and cell phone data.  The Selected Metropolitan Area Risk Trends (SMART) project uses the Behavioral Risk Factor Surveillance System (BRFSS) to analyze the data of selected counties with 500 or more respondents. BRFSS data can be used to identify emerging health problems, establish and track health objectives, and develop and evaluate public health policies and programs. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Data will be updated annually as it becomes available. Detailed information on sampling methodology and quality assurance can be found on the BRFSS website (http://www.cdc.gov/brfss). Methodology: http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf Glossary: https://chronicdata.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct",
-            "title": "Behavioral Risk Factors: Selected Metropolitan Area Risk Trends (SMART) County Prevalence Data (2011 to 2012)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24999,39 +24974,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factors-Selected-Metropolitan-Area/cpem-dkkm",
+            "identifier": "https://data.cdc.gov/api/views/cpem-dkkm",
+            "issued": "2023-07-18",
+            "keyword": [
+                "...",
+                "behavioral",
+                "brfss",
+                "county",
+                "factor",
+                "risk",
+                "smart",
+                "survey"
+            ],
+            "landingPage": "https://www.cdc.gov/brfss/",
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
+                "https://www.cdc.gov/brfss/"
+            ],
             "theme": [
                 "Behavioral Risk Factors"
-            ]
+            ],
+            "title": "Behavioral Risk Factors: Selected Metropolitan Area Risk Trends (SMART) County Prevalence Data (2011 to 2012)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/77xx-8ivd",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-09-27",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-26",
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
-            "identifier": "d906204c-3476-4a75-bd35-342b8dc56687",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-09-18-to-2023-09-24",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25040,42 +25025,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-09-18-to-2023-09-24"
                 }
             ],
+            "identifier": "d906204c-3476-4a75-bd35-342b8dc56687",
+            "issued": "2023-09-27",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/77xx-8ivd",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-09-26",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-09-18-to-2023-09-24"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/nis/",
+            "accrualPeriodicity": "Approximately Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-12-01",
-            "@type": "dcat:Dataset",
-            "temporal": "Monthly",
-            "modified": "2023-04-28",
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
-            "identifier": "https://data.cdc.gov/api/views/b6uq-hdgz",
             "description": "Cumulative Influenza Vaccination Coverage and Comparison, Adults 18 Years and Older, United States, Data Source:  National Immunization Survey-Adult COVID Module.\n\n\u2022 The National Immunization Survey-Adult COVID Module (NIS-ACM) was launched in April 2021 among adults 18 years and older. The survey was used to monitor COVID-19 vaccination uptake and confidence in vaccination among adults and included questions about influenza vaccination.",
-            "title": "Cumulative Influenza Vaccination Coverage and Comparison, Adults 18 Years and Older, US, National Immunization Survey-Adult COVID Module",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25098,48 +25077,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, District of Columbia, US Virgin Islands, and Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/b6uq-hdgz",
+            "issued": "2022-12-01",
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
-            "accrualPeriodicity": "Approximately Monthly",
+            "modified": "2023-04-28",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States, District of Columbia, US Virgin Islands, and Puerto Rico",
+            "temporal": "Monthly",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Cumulative Influenza Vaccination Coverage and Comparison, Adults 18 Years and Older, US, National Immunization Survey-Adult COVID Module"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/vutr-sfkh",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
-            "keyword": [
-                "cardiovascular",
-                "cardiovascular disease",
-                "cerebrovascular disease",
-                "counties",
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
-            "identifier": "https://data.cdc.gov/api/views/vutr-sfkh",
             "description": "2019 to 2021, 3-year average. Rates are age-standardized. County rates are spatially smoothed. The data can be viewed by sex and race/ethnicity. Data source: National Vital Statistics System. Additional data, maps, and methodology can be viewed on the Interactive Atlas of Heart Disease and Stroke http://www.cdc.gov/dhdsp/maps/atlas",
-            "title": "Stroke Mortality Data Among US Adults (35+) by State/Territory and County \u2013 2019-2021",
-            "programCode": [
-                "009:029"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25162,41 +25141,43 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vutr-sfkh",
+            "issued": "2024-02-23",
+            "keyword": [
+                "cardiovascular",
+                "cardiovascular disease",
+                "cerebrovascular disease",
+                "counties",
+                "county",
+                "stroke"
+            ],
+            "landingPage": "https://data.cdc.gov/d/vutr-sfkh",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-30",
+            "programCode": [
+                "009:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Heart Disease & Stroke Prevention"
-            ]
+            ],
+            "title": "Stroke Mortality Data Among US Adults (35+) by State/Territory and County \u2013 2019-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/w47j-r23n",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-09-14",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-27",
-            "keyword": [
-                "glossary",
-                "methodology",
-                "sam",
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
-            "identifier": "https://data.cdc.gov/api/views/w47j-r23n",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "Smoking-Attributable Mortality, Morbidity, and Economic Costs (SAMMEC) - Smoking-Attributable Mortality (SAM) Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25204,48 +25185,43 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/w47j-r23n",
+            "issued": "2015-09-14",
+            "keyword": [
+                "glossary",
+                "methodology",
+                "sam",
+                "sammec"
+            ],
+            "landingPage": "https://data.cdc.gov/d/w47j-r23n",
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
+            "title": "Smoking-Attributable Mortality, Morbidity, and Economic Costs (SAMMEC) - Smoking-Attributable Mortality (SAM) Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/max-linkage.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-06-16",
-            "@type": "dcat:Dataset",
-            "temporal": "1999/2014",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data/datalinkage/nchs-cms-medicaid-linked-data-list-of-variables.pdf"
-            ],
-            "keyword": [
-                "linked medicaid files",
-                "max",
-                "nchs surveys",
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
-            "identifier": "https://data.cdc.gov/api/views/sv3x-rgz2",
-            "description": "NCHS has linked various surveys with the Medicaid Analytic eXtract (MAX) files collected from the Centers for Medicare & Medicaid Services (CMS). Linkage of the NCHS survey participants with the CMS Medicaid MAX data provides the opportunity to study changes in health status, health care utilization and expenditures in low-income families with children and the elderly U.S. populations.",
-            "title": "NCHS Survey Data Linked to Centers for Medicare & Medicaid Services (CMS) MAX Data",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/nchs-cms-medicaid-linked-data-match-rate-tables-508.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "NCHS has linked various surveys with the Medicaid Analytic eXtract (MAX) files collected from the Centers for Medicare & Medicaid Services (CMS). Linkage of the NCHS survey participants with the CMS Medicaid MAX data provides the opportunity to study changes in health status, health care utilization and expenditures in low-income families with children and the elderly U.S. populations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25253,90 +25229,95 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/nchs-cms-medicaid-linked-data-match-rate-tables-508.pdf",
+            "identifier": "https://data.cdc.gov/api/views/sv3x-rgz2",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-06-16",
+            "keyword": [
+                "linked medicaid files",
+                "max",
+                "nchs surveys",
+                "research-data-center"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/max-linkage.htm",
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
+                "https://www.cdc.gov/nchs/data/datalinkage/nchs-cms-medicaid-linked-data-list-of-variables.pdf"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "United States",
+            "temporal": "1999/2014",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Survey Data Linked to Centers for Medicare & Medicaid Services (CMS) MAX Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/796s-yvap",
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
-            "identifier": "d62f5f31-d44c-5818-ad92-6f5058b1153c",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet measure v2.10.64 (coreset-prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure.csv",
-                    "description": "CoreSet measure v2.10.64 (coreset-prod)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet measure v2.10.64 (coreset-prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet measure v2.10.64 (coreset-prod)"
                 }
             ],
+            "identifier": "d62f5f31-d44c-5818-ad92-6f5058b1153c",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/796s-yvap",
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
+            "title": "CoreSet measure v2.10.64 (coreset-prod)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/798x-p6ne",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-01",
-            "references": [
-                "http://www.fda.gov/medicaldevices/productsandmedicalprocedures/deviceapprovalsandclearances/pmaapprovals/default.htm",
-                "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma.cfm"
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
-            "identifier": "475907fb-6a5d-4ad8-90c0-b276edc05227",
+            "describedBy": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Databases/ucm135279.htm",
             "description": "Premarket approval by FDA is the required process of scientific review to ensure the safety and effectiveness of all devices classified as Class III devices. An approved Premarket Approval Application (PMA) is, in effect, a private license granted to the applicant for marketing a particular medical device. This database may be searched by a variety of fields and is updated on a monthly basis.",
-            "title": "Premarket Approvals (PMA)",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25344,43 +25325,39 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Databases/ucm135279.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "475907fb-6a5d-4ad8-90c0-b276edc05227",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "https://healthdata.gov/d/798x-p6ne",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-01",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.fda.gov/medicaldevices/productsandmedicalprocedures/deviceapprovalsandclearances/pmaapprovals/default.htm",
+                "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma.cfm"
+            ],
+            "title": "Premarket Approvals (PMA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "nephtrackingsupport@cdc.gov",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-10-13",
-            "@type": "dcat:Dataset",
-            "temporal": "2001-2019",
-            "modified": "2023-10-13",
-            "keyword": [
-                "air pollution",
-                "air quality",
-                "\u2022\tasthma",
-                "environmental health",
-                "national ambient air quality standards",
-                "national environmental health tracking network",
-                "ozone"
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
-            "identifier": "https://data.cdc.gov/api/views/jcn4-jcv5",
             "description": "This dataset provides modeled predictions of ozone levels from the EPA's Downscaler model. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Data are at the county levels for 2001-2014. The dataset includes the maximum, median, mean, and population-weighted mean concentration. Please refer to the metadata attachment for more information.\n\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\n\nBy using these data, you signify your agreement to comply with the following requirements:\n1. Use the data for statistical reporting and analysis only.\n2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals.\n3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov.\n4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.\n5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC.\n6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily County-Level Ozone Concentrations, 2001-2019",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25403,48 +25380,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S. states",
+            "identifier": "https://data.cdc.gov/api/views/jcn4-jcv5",
+            "issued": "2023-10-13",
+            "keyword": [
+                "air pollution",
+                "air quality",
+                "\u2022\tasthma",
+                "environmental health",
+                "national ambient air quality standards",
+                "national environmental health tracking network",
+                "ozone"
+            ],
+            "landingPage": "nephtrackingsupport@cdc.gov",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-10-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "U.S. states",
+            "temporal": "2001-2019",
             "theme": [
                 "Environmental Health & Toxicology"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Daily County-Level Ozone Concentrations, 2001-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
             "bureauCode": [
                 "009:20"
             ],
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
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vax Views",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9wzx-rwzv",
             "description": "Monthly Cumulative Influenza Vaccination Coverage, by Race/Ethnicity, Pregnant Persons 18 years to 49 years, United States",
-            "title": "Monthly Cumulative Influenza Vaccination Coverage, by Race/Ethnicity, Pregnant Persons 18 years to 49 years, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25467,79 +25445,80 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9wzx-rwzv",
+            "issued": "2021-03-10",
+            "keyword": [
+                "flu",
+                "influenza",
+                "pregnant persons",
+                "vaccine coverage"
+            ],
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-01",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "Vaccine Safety Datalink"
+            ],
             "theme": [
                 "Pregnancy & Vaccination"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Monthly Cumulative Influenza Vaccination Coverage, by Race/Ethnicity, Pregnant Persons 18 years to 49 years, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/q9tu-7yha",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-03-24",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "cdc",
-                "centers for disease control and prevention"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PHM",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/q9tu-7yha",
             "description": "Each day, between 12 to 13 U.S. workers die as a result of a traumatic injury on the job. Investigations conducted through the FACE program allow the identification of factors that contribute to these fatal injuries. This information is used to develop comprehensive recommendations for preventing similar deaths. This web page provides access to NIOSH investigation reports and other safety resources.",
-            "title": "Fatality Assessment and Control Evaluation (FACE) Program",
+            "identifier": "https://data.cdc.gov/api/views/q9tu-7yha",
+            "issued": "2015-03-24",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/q9tu-7yha",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2015-08-27",
             "programCode": [
                 "009:020"
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Injury & Violence"
-            ]
+            ],
+            "title": "Fatality Assessment and Control Evaluation (FACE) Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/dhdsp/maps/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
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
-            "identifier": "https://data.cdc.gov/api/views/55yu-xksw",
             "description": "2019 to 2021, 3-year average. Rates are age-standardized. County rates are spatially smoothed. The data can be viewed by sex and race/ethnicity. Data source: National Vital Statistics System. Additional data, maps, and methodology can be viewed on the Interactive Atlas of Heart Disease and Stroke http://www.cdc.gov/dhdsp/maps/atlas",
-            "title": "Heart Disease Mortality Data Among US Adults (35+) by State/Territory and County \u2013 2019-2021",
-            "programCode": [
-                "009:029"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25562,46 +25541,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/55yu-xksw",
+            "issued": "2024-02-23",
+            "keyword": [
+                "cardiovascular",
+                "cardiovascular disease",
+                "counties",
+                "county",
+                "heart",
+                "heart disease"
+            ],
+            "landingPage": "https://www.cdc.gov/dhdsp/maps/index.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-30",
+            "programCode": [
+                "009:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Heart Disease & Stroke Prevention"
-            ]
+            ],
+            "title": "Heart Disease Mortality Data Among US Adults (35+) by State/Territory and County \u2013 2019-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adults.html",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-01-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-24",
-            "modified": "2024-08-09",
-            "keyword": [
-                "covid-19",
-                "covid-19 vaccination",
-                "immunization",
-                "nis-acm",
-                "vaccination",
-                "vaccination coverage",
-                "vaccine confidence",
-                "vaxviews"
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
-            "identifier": "https://data.cdc.gov/api/views/uc4z-hbsd",
             "description": "\u2022 National Immunization Survey Adult COVID Module (NIS-ACM): CDC is providing information on the Updated 2023-24 COVID-19 vaccine confidence to supplement vaccine administration data. These data represent trends in vaccination status and intent, and other behavioral indicators, by demographics and other characteristics. \n\n\u2022 The data start in October 2023.  \n\n\u2022 The archived data can be found here:",
-            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): COVIDVaxViews| Data | Centers for Disease Control and Prevention (cdc.gov)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25624,51 +25601,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/uc4z-hbsd",
+            "issued": "2024-01-16",
+            "keyword": [
+                "covid-19",
+                "covid-19 vaccination",
+                "immunization",
+                "nis-acm",
+                "vaccination",
+                "vaccination coverage",
+                "vaccine confidence",
+                "vaxviews"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adults.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2024-08-09",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2023-24",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): COVIDVaxViews| Data | Centers for Disease Control and Prevention (cdc.gov)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/a93x-tfzm",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/a93x-tfzm",
             "description": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus \u2013 2020.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers\". NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
-            "title": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25691,52 +25667,55 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/a93x-tfzm",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "crimean-congo hemorrhagic fever virus",
+                "ebola virus",
+                "guanarito virus",
+                "nedss",
+                "netss",
+                "nndss",
+                "viral hemorrhagic fevers",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/a93x-tfzm",
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
+            "title": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/alternative-payments-comprehensive-care-for-joint-replacement-model/comprehensive-care-for-joint-replacement-model-metropolitan-statistical-areas",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2020-01-01/2020-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-04",
-            "references": [
-                "https://data.cms.gov/resources/comprehensive-care-for-joint-replacement-model-msa-methodology"
-            ],
-            "keyword": [
-                "medicare",
-                "original medicare",
-                "payment models",
-                "rural-urban",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/62e490c0-9503-4b5f-9518-8e82fe20ccb6/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/comprehensive-care-for-joint-replacement-model-msa-data-dictionary",
             "description": "The Comprehensive Care for Joint Replacement Model: Metropolitan Statistical Areas (MSAs) dataset presents MSAs that are participating in the CMS Innovation Center Comprehensive Care for Joint Replacement Model, a model to support better and more efficient care for beneficiaries undergoing the most common inpatient surgery for Medicare beneficiaries: hip and knee replacements. Participation in this model is designated by geographic area, specifically MSAs. The information contained in the dataset can include MSA identification number, MSA geographic name and associated county or counties.\u00a0",
-            "title": "Comprehensive Care for Joint Replacement Model: Metropolitan Statistical Areas",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/62e490c0-9503-4b5f-9518-8e82fe20ccb6/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/62e490c0-9503-4b5f-9518-8e82fe20ccb6/data",
+                    "mediaType": "text/html",
                     "title": "Comprehensive Care for Joint Replacement Model: Metropolitan Statistical Areas : 2020-07-01"
                 },
                 {
@@ -25752,26 +25731,58 @@
                     "title": "Comprehensive Care for Joint Replacement Model: Metropolitan Statistical Areas : 2020-07-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/comprehensive-care-for-joint-replacement-model-msa-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/62e490c0-9503-4b5f-9518-8e82fe20ccb6/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "original medicare",
+                "payment models",
+                "rural-urban",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/alternative-payments-comprehensive-care-for-joint-replacement-model/comprehensive-care-for-joint-replacement-model-metropolitan-statistical-areas",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2021-01-04",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/comprehensive-care-for-joint-replacement-model-msa-methodology"
+            ],
+            "temporal": "2020-01-01/2020-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Comprehensive Care for Joint Replacement Model: Metropolitan Statistical Areas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4zc2-9ujh",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "F. Abigail Ferrell",
+                "hasEmail": "mailto:fferrell@cdc.gov"
+            },
+            "description": "Animals at petting zoos and agricultural fairs can be carriers of pathogens, such as Escherichia coli. Disease outbreaks at animal contact exhibits can be prevented by handwashing after contact with animals and keeping food and beverage away from exhibits. This research procedure and code book accompanies the data set, Animal Contact Exhibits_Legal Epidemiology Dataset_2016, which catalogs and analyzes a collection of state hand sanitation laws for the following categories of animal contact exhibits:\na. Petting zoos\nb. Agricultural fairs\nc. County or state fairs\nd. Exotic animal exhibits\ne. Circuses\nf. Zoos",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/4zc2-9ujh/application/pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/4zc2-9ujh",
             "issued": "2017-06-27",
-            "@type": "dcat:Dataset",
-            "modified": "2017-06-27",
             "keyword": [
                 "agricultural fair",
                 "animal contact exhibit",
@@ -25784,107 +25795,77 @@
                 "zoo",
                 "zoonotic disease"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "F. Abigail Ferrell",
-                "hasEmail": "mailto:fferrell@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/4zc2-9ujh",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2017-06-27",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/4zc2-9ujh",
-            "description": "Animals at petting zoos and agricultural fairs can be carriers of pathogens, such as Escherichia coli. Disease outbreaks at animal contact exhibits can be prevented by handwashing after contact with animals and keeping food and beverage away from exhibits. This research procedure and code book accompanies the data set, Animal Contact Exhibits_Legal Epidemiology Dataset_2016, which catalogs and analyzes a collection of state hand sanitation laws for the following categories of animal contact exhibits:\na. Petting zoos\nb. Agricultural fairs\nc. County or state fairs\nd. Exotic animal exhibits\ne. Circuses\nf. Zoos",
-            "title": "Animal Contact Exhibits_Legal Epidemiology Research Procedure and Code Book_2016",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/download/4zc2-9ujh/application/pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "Animal Contact Exhibits_Legal Epidemiology Research Procedure and Code Book_2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7ccn-vsdz",
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
-                "dual enrollment",
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
-            "identifier": "93b36a8e-4dd5-4ff4-9a8b-8c6537684705",
             "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by dual eligibility status for Medicaid and Medicare (full dual eligibility, partial dual eligibility, or not dually eligible). There are three metrics presented: (1) the number of beneficiaries ever dually eligible for Medicaid and Medicare over the year (duplicated count); (2) the number of beneficiaries dually eligible for Medicaid and Medicare as of an individual\u2019s last month of enrollment (unduplicated count); and (3) average monthly eligibility for Medicaid and Medicare. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Dually Enrolled in Medicare. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Dual Status Information for Medicaid and CHIP Beneficiaries by Year",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/DualStatus-anul.csv",
-                    "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by dual eligibility status for Medicaid and Medicare (full dual eligibility, partial dual eligibility, or not dually eligible). There are three metrics presented: (1) the number of beneficiaries ever dually eligible for Medicaid and Medicare over the year (duplicated count); (2) the number of beneficiaries dually eligible for Medicaid and Medicare as of an individual\u2019s last month of enrollment (unduplicated count); and (3) average monthly eligibility for Medicaid and Medicare. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Dually Enrolled in Medicare. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by dual eligibility status for Medicaid and Medicare (full dual eligibility, partial dual eligibility, or not dually eligible). There are three metrics presented: (1) the number of beneficiaries ever dually eligible for Medicaid and Medicare over the year (duplicated count); (2) the number of beneficiaries dually eligible for Medicaid and Medicare as of an individual\u2019s last month of enrollment (unduplicated count); and (3) average monthly eligibility for Medicaid and Medicare. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Dually Enrolled in Medicare. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/DualStatus-anul.csv",
+                    "mediaType": "text/csv",
                     "title": "Dual Status Information for Medicaid and CHIP Beneficiaries by Year"
                 }
             ],
+            "identifier": "93b36a8e-4dd5-4ff4-9a8b-8c6537684705",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "dual enrollment",
+                "medicaid",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/7ccn-vsdz",
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
+            "title": "Dual Status Information for Medicaid and CHIP Beneficiaries by Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7d6b-fh6k",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-08-10",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-17",
-            "keyword": [
-                "py2022",
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
-            "identifier": "b2b221ae-4285-4e05-b70b-13e09e7d65cf",
             "description": "The Dental SHOP Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2022 Dental SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25892,83 +25873,85 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "b2b221ae-4285-4e05-b70b-13e09e7d65cf",
+            "issued": "2022-08-10",
+            "keyword": [
+                "py2022",
+                "qhp landscape",
+                "sadp",
+                "shop",
+                "shop market dental"
+            ],
+            "landingPage": "https://healthdata.gov/d/7d6b-fh6k",
+            "modified": "2022-08-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2022 Dental SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7dag-cf7m",
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
-                "major eligibility group",
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
-            "identifier": "bffd757a-3ae9-42fc-809a-820c2919496b",
             "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by major eligibility group (children, adult expansion group, adult, aged, persons with disabilities, or COVID newly-eligible). There are three metrics presented: (1) the number of beneficiaries ever enrolled in each major eligibility group over the year (duplicated count); (2) the number of beneficiaries enrolled in each major eligibility group as of an individual\u2019s last month of enrollment (unduplicated count); and (3) average monthly enrollment in each major eligibility group. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues, making the data unusable for calculating these measures. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state and year are considered unusable or of high concern based on DQ Atlas thresholds for the topic Eligibility Group Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.  \r\n \r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Major Eligibility Group Information for Medicaid and CHIP Beneficiaries by Year",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/MajorEligibilityGroup-anul.csv",
-                    "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by major eligibility group (children, adult expansion group, adult, aged, persons with disabilities, or COVID newly-eligible). There are three metrics presented: (1) the number of beneficiaries ever enrolled in each major eligibility group over the year (duplicated count); (2) the number of beneficiaries enrolled in each major eligibility group as of an individual\u2019s last month of enrollment (unduplicated count); and (3) average monthly enrollment in each major eligibility group. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues, making the data unusable for calculating these measures. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state and year are considered unusable or of high concern based on DQ Atlas thresholds for the topic Eligibility Group Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.  \n \nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by major eligibility group (children, adult expansion group, adult, aged, persons with disabilities, or COVID newly-eligible). There are three metrics presented: (1) the number of beneficiaries ever enrolled in each major eligibility group over the year (duplicated count); (2) the number of beneficiaries enrolled in each major eligibility group as of an individual\u2019s last month of enrollment (unduplicated count); and (3) average monthly enrollment in each major eligibility group. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues, making the data unusable for calculating these measures. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state and year are considered unusable or of high concern based on DQ Atlas thresholds for the topic Eligibility Group Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.  \n \nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/MajorEligibilityGroup-anul.csv",
+                    "mediaType": "text/csv",
                     "title": "Major Eligibility Group Information for Medicaid and CHIP Beneficiaries by Year"
                 }
             ],
+            "identifier": "bffd757a-3ae9-42fc-809a-820c2919496b",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "major eligibility group",
+                "medicaid",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/7dag-cf7m",
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
+            "title": "Major Eligibility Group Information for Medicaid and CHIP Beneficiaries by Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/health-disparities.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-03-09",
-            "@type": "dcat:Dataset",
-            "temporal": "1997-01-01/2018-12-31",
-            "modified": "2023-08-23",
-            "keyword": [
-                "health disparities",
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
-            "identifier": "https://data.cdc.gov/api/views/fdpm-fddm",
             "description": "The Overview of Health Disparities analysis is a component of the Healthy People 2020 (HP2020) Final Review. The analysis included 611 objectives in HP2020. This file contains summary level information used for the evaluation of changes in disparities during HP2020, including calculations for the disparities measures and the disparities change categories for all objectives and population characteristics in the analysis. See Technical Notes for the Healthy People 2020 Overview of Health Disparities (https://www.cdc.gov/nchs/healthy_people/hp2020/health-disparities-technical-notes.htm) for additional information and criteria for objectives, data years, and population characteristics included in the analysis and statistical formulas and definitions for the disparities measures. \n\nData for additional years during the HP2020 tracking period that are not included in the Overview of Health Disparities are available on the HP2020 website (https://www.healthypeople.gov/2020/). \n\nNote that \u201crate\u201d as used may refer to a statistical rate expressed per unit population or a proportion, depending on how the HP2020 objective was defined.",
-            "title": "Healthy People 2020 Overview of Health Disparities",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25991,167 +25974,197 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
-            "theme": [
-                "NCHS"
-            ],
-            "language": [
-                "en-US"
-            ]
-        },
+            "identifier": "https://data.cdc.gov/api/views/fdpm-fddm",
+            "issued": "2022-03-09",
+            "keyword": [
+                "health disparities",
+                "healthy people 2020"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/health-disparities.htm",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-08-23",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
+            "temporal": "1997-01-01/2018-12-31",
+            "theme": [
+                "NCHS"
+            ],
+            "title": "Healthy People 2020 Overview of Health Disparities"
+        },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7dez-whbx",
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
-            "identifier": "2ed1141f-e940-58f2-b9ff-6a3b15c081db",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard pillar v2.11.9 (prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/pillar.csv",
-                    "description": "Scorecard pillar v2.11.9 (prod)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard pillar v2.11.9 (prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard pillar v2.11.9 (prod)"
                 }
             ],
+            "identifier": "2ed1141f-e940-58f2-b9ff-6a3b15c081db",
+            "issued": "2023-07-22",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/7dez-whbx",
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
+            "title": "Scorecard pillar v2.11.9 (prod)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7dy7-uy2j",
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
-            "identifier": "9923e5b7-1172-557e-8422-727f242f1d83",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_measure_backgroundAndMethods",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_backgroundAndMethods.csv",
-                    "description": "{\"dataset\": \"measure_backgroundAndMethods\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_backgroundAndMethods\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_backgroundAndMethods.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_backgroundAndMethods csv file"
                 }
             ],
+            "identifier": "9923e5b7-1172-557e-8422-727f242f1d83",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/7dy7-uy2j",
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
+            "title": "prodAuto_measure_backgroundAndMethods"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7e2j-4gng",
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
-            "identifier": "113f1a9c-59a6-5b84-a166-0524eeafda2b",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_states_measures_download",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/states_measures_download.csv",
-                    "description": "{\"dataset\": \"states_measures_download\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"states_measures_download\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/states_measures_download.csv",
+                    "mediaType": "text/csv",
                     "title": "states_measures_download csv file"
                 }
             ],
+            "identifier": "113f1a9c-59a6-5b84-a166-0524eeafda2b",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/7e2j-4gng",
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
+            "title": "devAuto_states_measures_download"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2008",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), to analyze general treatment services trends, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.  Data are collected on topics including facility operation, services offered (assessment and pre-treatment, pharmacotherapies, testing, transitional, ancillary), detoxification, primary focus (substance abuse, mental health, both, general health, and other), hotline operation, Opioid Treatment Programs and medication dispensed/prescribed, counseling and therapeutic approaches, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2008) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2008-nid13620",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2008-nid13620"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2008-nid13620",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -26164,65 +26177,30 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2008",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2008-nid13620",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), to analyze general treatment services trends, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.  Data are collected on topics including facility operation, services offered (assessment and pre-treatment, pharmacotherapies, testing, transitional, ancillary), detoxification, primary focus (substance abuse, mental health, both, general health, and other), hotline operation, Opioid Treatment Programs and medication dispensed/prescribed, counseling and therapeutic approaches, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2008)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2008-nid13620",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2008) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2008-nid13620"
-                }
-            ]
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2008)"
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
-            "temporal": "1970/2013",
-            "modified": "2022-03-29",
-            "keyword": [
-                "age group",
-                "birth rates",
-                "nchs",
-                "united states",
-                "women"
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
-            "identifier": "https://data.cdc.gov/api/views/jvf6-ix4w",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "https://www.cdc.gov/nchs/data-visualization/births-to-unmarried-women/index.htm",
-            "title": "NCHS - Nonmarital Birth Rates, by Age Group for All Women Age 15-44: United States, 1970-2013",
-            "isPartOf": "NCHS - Nonmarital Birth Rates, by Age Group for All Women Age 15-44: United States, 1970-2013",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26245,46 +26223,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/jvf6-ix4w",
+            "isPartOf": "NCHS - Nonmarital Birth Rates, by Age Group for All Women Age 15-44: United States, 1970-2013",
+            "issued": "2015-12-02",
+            "keyword": [
+                "age group",
+                "birth rates",
+                "nchs",
+                "united states",
+                "women"
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
+            "temporal": "1970/2013",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - Nonmarital Birth Rates, by Age Group for All Women Age 15-44: United States, 1970-2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/adults-60-coverage-intent.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-11",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-09-11",
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
-            "identifier": "https://data.cdc.gov/api/views/5vw4-awn6",
             "description": "Weekly RSV Vaccination Coverage of Adults 60 Years and Older by Jurisdiction \n\n\u2022 RSV vaccination coverage among adults 60 years and older is assessed through the National Immunization Survey-Adult COVID Module, providing weekly RSV vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n \u2022 The CDC recommended the RSV vaccine for adults 60 years and older in July 2023. (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)",
-            "title": "Differences in Weekly Cumulative Percentage of Adults 60 Years and Older Vaccinated with Respiratory Syncytial Virus (RSV) Vaccine by Selected Demographics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26307,48 +26288,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/5vw4-awn6",
+            "issued": "2023-12-11",
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
+            "modified": "2024-09-11",
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
+            "title": "Differences in Weekly Cumulative Percentage of Adults 60 Years and Older Vaccinated with Respiratory Syncytial Virus (RSV) Vaccine by Selected Demographics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kmxt-xb3i",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-16",
-            "@type": "dcat:Dataset",
-            "temporal": "Most recent month",
-            "modified": "2025-01-21",
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
-            "identifier": "https://data.cdc.gov/api/views/kmxt-xb3i",
             "description": "Count and percent of total COVID-19 deaths since January 1, 2020, by age group, race/ethnicity, and sex",
-            "title": "Total COVID-19 Deaths since January 1, 2020 by Age Group, Race/Ethnicity, and Sex",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26371,41 +26350,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/kmxt-xb3i",
+            "issued": "2023-11-16",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "demographics",
+                "mortality"
+            ],
+            "landingPage": "https://data.cdc.gov/d/kmxt-xb3i",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-21",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "Most recent month",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Total COVID-19 Deaths since January 1, 2020 by Age Group, Race/Ethnicity, and Sex"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-compressed-mortality-underlying-cause-death",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-08-03",
-            "temporal": "1968-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "epidemiology",
-                "mortality deaths births health population cause disease icd urbanization state county infant race hi"
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
-            "identifier": "a9ec849a-2e11-40d6-809a-b6a2adafbabb",
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/cmf.html",
             "description": "<p>The CDC WONDER Mortality - Underlying Cause of Death online database is a county-level national mortality and population database spanning the years since 1979 -2008. The number of deaths, crude death rates, age-adjusted death rates, standard errors and 95% confidence intervals for death rates can be obtained by place of residence (total U.S., Census region, Census division, state, and county), age group (including infant age groups), race (years 1979-1998: White, Black, and Other; years 1999-2008: American Indian or Alaska Native, Asian or Pacific Islander, Black or African American, and White), Hispanic origin (years 1979-1998: not available; years 1999-present: Hispanic or Latino, not Hispanic or Latino, Not Stated), gender, year of death, and underlying cause of death (years 1979-1998: 4-digit ICD-9 code and 72 cause-of-death recode; years 1999-present: 4-digit ICD-10 codes and 113 cause-of-death recode, as well as the Injury Mortality matrix classification for Intent and Mechanism), and urbanization level of residence (2006 NCHS urban-rural classification scheme for counties). The Compressed Mortality data are produced by the National Center for Health Statistics.</p>",
-            "title": "CDC WONDER: Compressed Mortality - Underlying Cause of Death",
-            "programCode": [
-                "009:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26414,57 +26398,42 @@
                     "title": "Text "
                 }
             ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/cmf.html",
-            "dataQuality": true,
+            "identifier": "a9ec849a-2e11-40d6-809a-b6a2adafbabb",
+            "issued": "2012-08-03",
+            "keyword": [
+                "epidemiology",
+                "mortality deaths births health population cause disease icd urbanization state county infant race hi"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-compressed-mortality-underlying-cause-death",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "temporal": "1968-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
             "theme": [
                 "Health",
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Compressed Mortality - Underlying Cause of Death"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/oralhealth/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
-            "references": [
-                "https://www.cdc.gov/oralhealthdata/"
-            ],
-            "keyword": [
-                "access to care",
-                "adult",
-                "adults",
-                "brfss",
-                "dental care",
-                "dental cleaning",
-                "dental visits",
-                "dentist",
-                "division of oral health",
-                "nohss",
-                "oral health",
-                "prevalence",
-                "surveillance",
-                "tooth loss"
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
-            "identifier": "https://data.cdc.gov/api/views/jz6n-v26y",
+            "describedBy": "https://chronicdata.cdc.gov/Oral-Health/NOHSS-Adult-Indicators/jz6n-v26y",
             "description": "2012-2020 (even years). Data from BRFSS for indicators of adult oral health for even years from 2012 through 2020. National estimates are represented by the median prevalence among 50 states and the District of Columbia data. Estimates are prepared from the BRFSS public use data sets. Estimates in this file are not age adjusted, and may differ slightly from estimates available from the BRFSS web site or Chronic Disease Indicators due to small differences in definition, age adjustment or rounding.  For more information, see: https://www.cdc.gov/oralhealthdata/overview/Adult-Indicators.html.",
-            "title": "NOHSS Adult Indicators",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26487,41 +26456,55 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Oral-Health/NOHSS-Adult-Indicators/jz6n-v26y",
+            "identifier": "https://data.cdc.gov/api/views/jz6n-v26y",
+            "issued": "2023-07-18",
+            "keyword": [
+                "access to care",
+                "adult",
+                "adults",
+                "brfss",
+                "dental care",
+                "dental cleaning",
+                "dental visits",
+                "dentist",
+                "division of oral health",
+                "nohss",
+                "oral health",
+                "prevalence",
+                "surveillance",
+                "tooth loss"
+            ],
+            "landingPage": "http://www.cdc.gov/oralhealth/",
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
+                "https://www.cdc.gov/oralhealthdata/"
+            ],
             "theme": [
                 "Oral Health"
-            ]
+            ],
+            "title": "NOHSS Adult Indicators"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7hhb-dd7s",
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
-            "identifier": "737f7186-b4d5-5272-a997-0ee94f4d4c3b",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2009",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26529,44 +26512,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "737f7186-b4d5-5272-a997-0ee94f4d4c3b",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/7hhb-dd7s",
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
+            "title": "State Drug Utilization Data 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hhvg-83jq",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-13",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "antibodies",
-                "covid-19",
-                "immunoassays",
-                "neutralization assay",
-                "sars-cov-2",
-                "serological tests"
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
-            "identifier": "https://data.cdc.gov/api/views/hhvg-83jq",
             "description": "Severe acute respiratory syndrome (SARS) coronavirus 2 (SARS-CoV-2) is a novel human coronavirus that was identified in 2019. SARS-CoV-2 infection results in an acute, severe respiratory disease called coronavirus disease 2019 (COVID-19).  The emergence and rapid spread of SARS-CoV-2 has led to a global public health crisis, which continues to affect populations across the globe. Real time reverse transcription polymerase chain reaction (rRT-PCR) is the reference standard test for COVID-19 diagnosis. Serological tests are valuable tools for serosurveillance programs and establishing correlates of protection from disease. This study evaluated the performance of one in-house enzyme linked immunosorbent assay (ELISA) utilizing the pre-fusion stabilized ectodomain of SARS-CoV-2 spike (S), two commercially available chemiluminescence assays Ortho VITROS Immunodiagnostic Products Anti-SARS-CoV-2 Total Reagent Pack and Abbott SARS-CoV-2 IgG assay and one commercially available Surrogate Virus Neutralization Test (sVNT), GenScript USA Inc., cPass SARS-CoV-2 Neutralization Antibody Detection Kit for the detection of SARS-CoV-2 specific antibodies.  Using a panel of rRT-PCR confirmed COVID-19 patients\u2019 sera and a negative control group as a reference standard, all three immunoassays demonstrated high comparable positivity rates and low discordant rates.  All three immunoassays were highly sensitive with estimated sensitivities ranging from 95.4%-96.6%. ROC curve analysis indicated that all three immunoassays had high diagnostic accuracies with area under the curve (AUC) values ranging from 0.9698-0.9807. High positive correlation was demonstrated among the conventional microneutralization test (MNT) titers and the sVNT inhibition percent values.  Our study indicates that independent evaluations are necessary to optimize the overall utility and the interpretation of the results of serological tests.  Overall, we demonstrate that all serological tests evaluated in this study are suitable for the detection of SARS-CoV-2 antibodies.",
-            "title": "Examination of SARS-CoV-2 serological test results from multiple commercial and laboratory platforms with an in-house serum panel",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26589,45 +26568,43 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hhvg-83jq",
+            "issued": "2023-12-13",
+            "keyword": [
+                "antibodies",
+                "covid-19",
+                "immunoassays",
+                "neutralization assay",
+                "sars-cov-2",
+                "serological tests"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hhvg-83jq",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Coronavirus and Other Respiratory Viruses"
-            ]
+            ],
+            "title": "Examination of SARS-CoV-2 serological test results from multiple commercial and laboratory platforms with an in-house serum panel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/pkas-xr96",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-13",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-13",
-            "keyword": [
-                "2016",
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
-            "identifier": "https://data.cdc.gov/api/views/pkas-xr96",
             "description": "NNDSS - Table IV. Tuberculosis - 2016.This Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States will exclude counts from US territories.  Footnote: C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Min: Minimum.    Max: Maximum. * Case counts for reporting year 2015 and 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf Data for TB are displayed quarterly.",
-            "title": "NNDSS - Table IV. Tuberculosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26650,44 +26627,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/pkas-xr96",
+            "issued": "2017-01-13",
+            "keyword": [
+                "2016",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "tb",
+                "tuberculosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/pkas-xr96",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2017-01-13",
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
-            "landingPage": "https://data.cdc.gov/d/espg-acwi",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/espg-acwi",
             "description": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Novel influenza A virus infections are human infections with influenza A viruses that are different from currently circulating human seasonal influenza viruses. With the exception of one avian lineage influenza A (H7N2) virus, all novel influenza A virus infections reported to CDC since 2012 have been variant influenza viruses.",
-            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26710,41 +26688,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/espg-acwi",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "novel influenza a virus infections",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/espg-acwi",
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
+            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections"
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
-            "identifier": "https://data.cdc.gov/api/views/judz-8etw",
             "description": "\u2022 Weekly Influenza Vaccination Status and Intent for Vaccination, Overall, by Selected Demographics, and Jurisdiction, Children 6 Months-17 Years. \n\n\u2022 Weekly Influenza vaccination coverage and parental intent for vaccination among children is calculated using data from the National Immunization Survey\u2013Flu (NIS\u2013Flu) (https://www.cdc.gov/nis/about/index.html). NIS\u2013Flu is a national random-digit-dialed cellular telephone survey of households with children ages 6 months\u201317 years conducted during October-June. The respondent to a NIS\u2013Flu survey is a parent or guardian who said they were knowledgeable about the child\u2019s vaccination history. All estimates are based upon parental report of receipt of vaccination and month of that vaccination.",
-            "title": "Weekly Influenza Vaccination Status and Intent for Vaccination, Overall, by Selected Demographics, and Jurisdiction, Children 6 Months-17 Years, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26767,139 +26749,140 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/judz-8etw",
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
+            "title": "Weekly Influenza Vaccination Status and Intent for Vaccination, Overall, by Selected Demographics, and Jurisdiction, Children 6 Months-17 Years, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7j8c-zzs8",
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
-            "identifier": "6ecbdafe-abf9-5744-8a5c-b63ee27a5ab2",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt state v2.10.22 (coreset-impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/state.csv",
-                    "description": "CoreSEt state v2.10.22 (coreset-impl)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt state v2.10.22 (coreset-impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/state.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt state v2.10.22 (coreset-impl)"
                 }
             ],
+            "identifier": "6ecbdafe-abf9-5744-8a5c-b63ee27a5ab2",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/7j8c-zzs8",
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
+            "title": "CoreSEt state v2.10.22 (coreset-impl)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7jff-gzx7",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-06-08",
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
-            "identifier": "6175e915-68d0-50b0-820a-0d016087eeb5",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_files_allDownloadsSSBtn",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/files_allDownloadsSSBtn.csv",
-                    "description": "{\"dataset\": \"files_allDownloadsSSBtn\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"files_allDownloadsSSBtn\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/files_allDownloadsSSBtn.csv",
+                    "mediaType": "text/csv",
                     "title": "files_allDownloadsSSBtn csv file"
                 }
             ],
+            "identifier": "6175e915-68d0-50b0-820a-0d016087eeb5",
+            "issued": "2022-06-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/7jff-gzx7",
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
+            "title": "implAuto_files_allDownloadsSSBtn"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7k3i-nv4y",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2014-11-07",
-            "temporal": "2021-01-01T00:00:00+00:00/2022-01-01T00:00:00+00:00",
-            "@type": "dcat:Dataset",
-            "modified": "2021-12-28",
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
-            "identifier": "d5eaf378-dcef-5779-83de-acdd8347d68e",
             "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
-            "title": "NADAC (National Average Drug Acquisition Cost) 2021",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26908,43 +26891,41 @@
                     "title": "NADAC (National Average Drug Acquisition Cost) 2021"
                 }
             ],
+            "identifier": "d5eaf378-dcef-5779-83de-acdd8347d68e",
+            "issued": "2014-11-07",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "landingPage": "https://healthdata.gov/d/7k3i-nv4y",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2021-12-28",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "temporal": "2021-01-01T00:00:00+00:00/2022-01-01T00:00:00+00:00",
             "theme": [
                 "National Average Drug Acquisition Cost",
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "NADAC (National Average Drug Acquisition Cost) 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/dbvar",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "dataset",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/pubs-rzki",
             "description": "Database of Genomic Structural Variation (dbVar) is NCBI's database of human genomic Structural Variation \u2014 large variants >50 bp including insertions, deletions, duplications, inversions, mobile elements, translocations, and complex variants.",
-            "title": "Database of Genomic Structural Variation (dbVar)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26959,38 +26940,42 @@
                     "title": "Download dbVar Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/pubs-rzki",
+            "issued": "2021-06-17",
+            "keyword": [
+                "dataset",
+                "genetics",
+                "genomics",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/dbvar",
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
+            "title": "Database of Genomic Structural Variation (dbVar)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.hhs.gov/programs/social-services/unaccompanied-children/index.html",
+            "accrualPeriodicity": "No longer being updated",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-04-05",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "keyword": [
-                "unaccompanied children"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HHS",
                 "hasEmail": "mailto:media@acf.hhs.gov "
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/w9g9-rj4y",
             "description": "This data is no longer being updated. New data is being tracked at https://healthdata.gov/National/HHS-Unaccompanied-Children-Program/ehpz-xc9n\n\nThis data represents unaccompanied children who are taken into custody by Customs and Border Protection brought to a facility and processed for transfer to the Department of Health and Human Services (HHS) as required by law. HHS holds the child for testing and quarantine, and shelters the child until the child is placed with a sponsor here in the United States.",
-            "title": "HHS Unaccompanied Children Program",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27013,36 +26998,38 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/w9g9-rj4y",
+            "issued": "2021-04-05",
+            "keyword": [
+                "unaccompanied children"
+            ],
+            "landingPage": "https://www.hhs.gov/programs/social-services/unaccompanied-children/index.html",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "No longer being updated",
+            "modified": "2021-05-21",
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
+            "title": "HHS Unaccompanied Children Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/wepx-mhy6",
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
-            "identifier": "https://data.cdc.gov/api/views/wepx-mhy6",
             "description": "Workers across every occupational sector have the potential to be exposed to a wide variety of chemicals, and the skin is a primary route of exposure. Furthermore, exposure to certain chemicals has been linked to inflammatory and allergic diseases. Thus, understanding the immune responses to chemical exposures on the skin and the potential for inflammation and sensitization is needed to improve worker safety and health. Responses in the skin microenvironment impact the potential for sensitization and these responses may include the presence of proinflammatory cytokines, inflammasome activation, barrier integrity, skin microbiota, and the presence of immune cells. Selection of mouse strain to evaluate skin effects, such as haired (BALB/c) or hairless (SKH1) mice, varies dependent on the experimental design and needs of a study. However, dermal chemical exposure may impact reactions in the skin differently depending on the strain of mouse. Additionally, there is a need for established methods to evaluate immune responses in the skin. In this study, exposure to the immunomodulatory chemical triclosan was evaluated in two mouse models using immunophenotyping by flow cytometry and gene expression analysis.  The flow cytometry panel reported in this manuscript in combination with gene expression analysis may be used in future studies to better evaluate the effect of chemical exposures on the skin immune response.  These findings may be important to consider during strain selection, experimental design, and result interpretation of chemical exposures on the skin.",
-            "title": "Exposure to the immunomodulatory chemical triclosan differentially impacts immune cell populations in the skin of haired (BALB/c) and hairless (SKH1) mice",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27050,46 +27037,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wepx-mhy6",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/wepx-mhy6",
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
+            "title": "Exposure to the immunomodulatory chemical triclosan differentially impacts immune cell populations in the skin of haired (BALB/c) and hairless (SKH1) mice"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/u2nj-bus9",
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
-            "identifier": "https://data.cdc.gov/api/views/u2nj-bus9",
             "description": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27112,94 +27088,95 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/u2nj-bus9",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "paralytic",
+                "pertussis",
+                "plague",
+                "poliomyelitis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/u2nj-bus9",
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
+            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7n5y-iuh4",
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
-            "identifier": "5c267647-50e9-4a81-b2f2-8f23cec6631a",
             "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by program type (Medicaid or CHIP). There are three metrics presented: (1) the number of beneficiaries ever enrolled in each program type over the year (duplicated count); (2) the number of beneficiaries enrolled in each program type as of an individual\u2019s last month of enrollment (unduplicated count); and (3) average monthly enrollment in each program type. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues, making the data unusable for calculating these measures. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state and year are considered unusable or of high concern based on DQ Atlas thresholds for the topics Medicaid-only enrollment and M-CHIP and S-CHIP Enrollment. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.\r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Program Information for Medicaid and CHIP Beneficiaries by Year",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/ProgramType-anul.csv",
-                    "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by program type (Medicaid or CHIP). There are three metrics presented: (1) the number of beneficiaries ever enrolled in each program type over the year (duplicated count); (2) the number of beneficiaries enrolled in each program type as of an individual\u2019s last month of enrollment (unduplicated count); and (3) average monthly enrollment in each program type. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues, making the data unusable for calculating these measures. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state and year are considered unusable or of high concern based on DQ Atlas thresholds for the topics Medicaid-only enrollment and M-CHIP and S-CHIP Enrollment. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.\n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by program type (Medicaid or CHIP). There are three metrics presented: (1) the number of beneficiaries ever enrolled in each program type over the year (duplicated count); (2) the number of beneficiaries enrolled in each program type as of an individual\u2019s last month of enrollment (unduplicated count); and (3) average monthly enrollment in each program type. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues, making the data unusable for calculating these measures. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state and year are considered unusable or of high concern based on DQ Atlas thresholds for the topics Medicaid-only enrollment and M-CHIP and S-CHIP Enrollment. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.\n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/ProgramType-anul.csv",
+                    "mediaType": "text/csv",
                     "title": "Program Information for Medicaid and CHIP Beneficiaries by Year"
                 }
             ],
+            "identifier": "5c267647-50e9-4a81-b2f2-8f23cec6631a",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "medicaid",
+                "program enrollment",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/7n5y-iuh4",
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
+            "title": "Program Information for Medicaid and CHIP Beneficiaries by Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-medicare-part-d-enrollment",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/d8c69aca-2497-4a83-a181-706a960c77f0/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
             "description": "The CMS Program Statistics -\u00a0Medicare Part D Enrollment tables provide data on characteristics of the Medicare Part D covered population.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR ENROLL D 1. Medicare Part D Enrollment: Part D Enrollees by Type of Plan, Low Income Subsidy (LIS), and Retiree Drug Subsidy, Yearly Trend\n\tMDCR ENROLL D 2. Medicare Part D Enrollment: Part D Enrollees by Type of Plan, Low Income Subsidy (LIS), and Retiree Drug Subsidy, by Demographic Characteristics\n\tMDCR ENROLL D 3. Medicare Part D Enrollment: Part D Enrollees by Type of Plan, Low Income Subsidy (LIS), and Retiree Drug Subsidy, by Area of Residence",
-            "title": "CMS Program Statistics - Medicare Part D Enrollment",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27256,26 +27233,76 @@
                     "title": "CMS Program Statistics - Medicare Part D Enrollment : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/d8c69aca-2497-4a83-a181-706a960c77f0/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "beneficiary enrollment",
+                "health equity",
+                "medicare",
+                "medicare advantage",
+                "medicare prescription drug",
+                "national",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-medicare-part-d-enrollment",
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
+            "title": "CMS Program Statistics - Medicare Part D Enrollment"
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
+            "description": "This dataset shows health conditions and contributing causes mentioned in conjunction with deaths involving coronavirus disease 2019 (COVID-19), by sex, race and Hispanic origin, and age group, for 2020.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tdmv-axfy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tdmv-axfy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tdmv-axfy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tdmv-axfy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/tdmv-axfy",
             "issued": "2021-04-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
             "keyword": [
                 "age",
                 "age group",
@@ -27304,80 +27331,34 @@
                 "sex",
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
-            "identifier": "https://data.cdc.gov/api/views/tdmv-axfy",
-            "description": "This dataset shows health conditions and contributing causes mentioned in conjunction with deaths involving coronavirus disease 2019 (COVID-19), by sex, race and Hispanic origin, and age group, for 2020.",
-            "title": "AH Provisional COVID-19 Deaths and Contributing Conditions by Sex, Race and Hispanic Origin, and Age, 2020",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-01",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tdmv-axfy/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tdmv-axfy/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tdmv-axfy/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tdmv-axfy/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths and Contributing Conditions by Sex, Race and Hispanic Origin, and Age, 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/v2zw-2d2v",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-08-02",
-            "@type": "dcat:Dataset",
-            "temporal": "January 16, 2022 to May 28, 2022",
-            "modified": "2023-08-02",
-            "keyword": [
-                "covid-19 breakthrough",
-                "covid-19 cases",
-                "covid-19 vaccination"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Maya Sternberg",
                 "hasEmail": "mailto:vbtsurveillance@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/v2zw-2d2v",
             "description": "Reported numbers of SARS-CoV-2 infections by age group (5\u201311, 12\u201317, 18\u201349, 50\u201364, \u226565 years of age) from 22 U.S. jurisdictions (AR, AZ, CA, CO, CT, DC, FL, GA, IN, KS, MI, MA, MN, NC, NE, NJ, NM, NYC, PHL, TN, UT, WI ); ~53% of the U.S. population) with routine linkages between COVID-19 case surveillance and immunization information system (IIS) data reported to CDC during January 16, 2022 \u2013 May 28, 2022. \nVaccine administration (coverage) data reported to CDC were aggregated by U.S. reporting jurisdiction, MMWR week of vaccination (\u226514 days after completing the primary vaccine series), FDA-approved vaccine products, and age group (5\u201311, 12\u201317, 18\u201349, 50\u201364, \u226565 years). \nVaccination status: A person vaccinated with at least a primary series had SARS-CoV-2 RNA or antigen detected on a respiratory specimen collected \u226514 days after verifiably completing BNT162b2 (Pfizer-BioNTech) primary series. An unvaccinated person had SARS-CoV-2 RNA or antigen detected on a respiratory specimen and has not been verified to have received COVID-19 vaccine. Excluded were partially vaccinated people who received at least one FDA-authorized vaccine dose but did not complete a primary series \u226514 days before collection of a specimen where SARS-CoV-2 RNA or antigen was detected. \nTo estimate the number of unvaccinated persons in each MMWR week, the 2019 U.S. Census population estimates by jurisdiction and age group were used (except for California, where State Department of Finance 2021 population projections were determined to be more accurate). The number of unvaccinated persons each MMWR week was estimated by subtracting the cumulative number of vaccinated (all products) and partially vaccinated persons (all products) from the respective population totals for each jurisdiction and age group. \nContinuity correction: A continuity correction has been applied to the denominators by capping the percent population coverage at 95%. To do this, we assumed that at least 5% of each age group would always be unvaccinated in each jurisdiction. Adding this correction ensures that there is always a reasonable denominator for the unvaccinated population that would prevent rates from growing unrealistically large due to potential overestimates of vaccination coverage.",
-            "title": "Weekly COVID-19 cases among persons \u22655 years old among unvaccinated and vaccinated with a BNT162b2 (Pfizer-BioNTech) primary series by age group \u2014 22 U.S. jurisdictions, January 16 to May 28, 2022",
-            "programCode": [
-                "009:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27400,46 +27381,42 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Select US Jurisdictions",
+            "identifier": "https://data.cdc.gov/api/views/v2zw-2d2v",
+            "issued": "2023-08-02",
+            "keyword": [
+                "covid-19 breakthrough",
+                "covid-19 cases",
+                "covid-19 vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/v2zw-2d2v",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-02",
+            "programCode": [
+                "009:031"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "Select US Jurisdictions",
+            "temporal": "January 16, 2022 to May 28, 2022",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Weekly COVID-19 cases among persons \u22655 years old among unvaccinated and vaccinated with a BNT162b2 (Pfizer-BioNTech) primary series by age group \u2014 22 U.S. jurisdictions, January 16 to May 28, 2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7kht-czfj",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
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
-            "identifier": "https://data.cdc.gov/api/views/7kht-czfj",
             "description": "NNDSS - Table 1C. Arboviral diseases, neuroinvasive and non-neuroinvasive,  St. Louis encephalitis virus disease to Western equine encephalitis virus disease - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1C. Arboviral diseases, St. Louis encephalitis virus to Western equine encephalitis virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27462,81 +27439,85 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7kht-czfj",
+            "issued": "2019-04-24",
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
+            "landingPage": "https://data.cdc.gov/d/7kht-czfj",
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
+            "title": "NNDSS - TABLE 1C. Arboviral diseases, St. Louis encephalitis virus to Western equine encephalitis virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7p7w-sp3f",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-06-27",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-26",
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
-            "identifier": "93c14523-3acb-4253-a9e0-98b0bd201541",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-06-19-to-2023-06-25",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-6192023-to-6252023.csv",
-                    "description": " ",
                     "@type": "dcat:Distribution",
+                    "description": " ",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-6192023-to-6252023.csv",
+                    "mediaType": "text/csv",
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-06-19-to-2023-06-25"
                 }
             ],
+            "identifier": "93c14523-3acb-4253-a9e0-98b0bd201541",
+            "issued": "2023-06-27",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/7p7w-sp3f",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-06-26",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-06-19-to-2023-06-25"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/npals.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-07-12",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01/2021-07",
-            "modified": "2022-09-12",
-            "keyword": [
-                "adult day services centers",
-                "covid-19",
-                "long-term care",
-                "residential care communities"
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
-            "identifier": "https://data.cdc.gov/api/views/3j26-kg6d",
             "description": "The NCHS National Post-acute and Long-term Care Study (NPALS) collects data on long-term care every two years for all 50 states and the District of Columbia to monitor the diverse post-acute and long-term care fields. The 2020 survey provided an opportunity to collect COVID-19-related data for residential care communities and adult day services centers, important long-term care settings. These data are not available from other data systems. These data are related to experiences of COVID-19 from January 2020 through mid-July 2021, including the number of COVID-19 cases, hospitalizations, and deaths among users and staff, practices taken to reduce COVID-19 exposure and transmission, and personal protective equipment (PPE) shortages.",
-            "title": "Long-term Care and COVID-19",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27559,44 +27540,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/3j26-kg6d",
+            "issued": "2021-07-12",
+            "keyword": [
+                "adult day services centers",
+                "covid-19",
+                "long-term care",
+                "residential care communities"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/npals.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2022-09-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
+            "temporal": "2020-01/2021-07",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Long-term Care and COVID-19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7q9y-sd6m",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-09",
-            "keyword": [
-                "child enrollment",
-                "eligibility determinations"
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
-            "identifier": "014d2aae-cf0a-4bea-8557-2d76bd0a8643",
             "description": "All states (including the District of Columbia) are required to provide data to The Centers for Medicare &amp; Medicaid Services (CMS) on a range of indicators related to key application, eligibility, and enrollment processes within the state Medicaid and Children\u2019s Health Insurance Programs (CHIP). These data reflect enrollment activity for all populations receiving comprehensive Medicaid and CHIP benefits in all states, as well as state program performance.",
-            "title": "State Medicaid and CHIP Test",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27605,88 +27589,85 @@
                     "title": "State Medicaid and CHIP Test"
                 }
             ],
+            "identifier": "014d2aae-cf0a-4bea-8557-2d76bd0a8643",
+            "issued": "2024-10-31",
+            "keyword": [
+                "child enrollment",
+                "eligibility determinations"
+            ],
+            "landingPage": "https://healthdata.gov/d/7q9y-sd6m",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2025-01-09",
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
+            "title": "State Medicaid and CHIP Test"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/7qnn-bkhb",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-06-05",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
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
-            "identifier": "0e155159-225c-538f-b3c7-641b965c0fb9",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard version v2.11.18 (etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/version.csv",
-                    "description": "Scorecard version v2.11.18 (etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard version v2.11.18 (etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/version.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard version v2.11.18 (etl-test)"
                 }
             ],
+            "identifier": "0e155159-225c-538f-b3c7-641b965c0fb9",
+            "issued": "2024-06-05",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/7qnn-bkhb",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2025-01-13",
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
+            "title": "Scorecard version v2.11.18 (etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/tplc.cfm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-01",
-            "references": [
-                "http://www.fda.gov/AboutFDA/CentersOffices/OfficeofMedicalProductsandTobacco/CDRH/CDRHTransparency/ucm199906.htm"
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
-            "identifier": "db8a6684-bf00-48a8-af05-c493e6dfcb4c",
             "description": "The Total Product Life Cycle (TPLC) database integrates premarket and postmarket data about medical devices. It includes information pulled from CDRH databases including Premarket Approvals (PMA), Premarket Notifications (510[k]), Adverse Events, and Recalls. You can search the TPLC database by device name or procode to receive a full report about a particular product line.",
-            "title": "Total Product Life Cycle (TPLC)",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27694,37 +27675,38 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "db8a6684-bf00-48a8-af05-c493e6dfcb4c",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/tplc.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-01",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.fda.gov/AboutFDA/CentersOffices/OfficeofMedicalProductsandTobacco/CDRH/CDRHTransparency/ucm199906.htm"
+            ],
+            "title": "Total Product Life Cycle (TPLC)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://ncbi.github.io/igblast/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "computational biology",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jhn6-5qv8",
             "description": "IgBLAST was developed at NCBI to facilitate analysis of immunoglobulin as well as T cell receptor (TR) sequences. It uses BLAST search algorithm.",
-            "title": "IgBLAST",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27739,46 +27721,41 @@
                     "title": "Downlod IgBlast Tool"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jhn6-5qv8",
+            "issued": "2021-06-30",
+            "keyword": [
+                "computational biology",
+                "genomics",
+                "tools & utilities"
+            ],
+            "landingPage": "https://ncbi.github.io/igblast/",
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
                 "Molecular biology/Genetics"
-            ]
+            ],
+            "title": "IgBLAST"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-visualization/state-life-expectancy/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-04-05",
-            "@type": "dcat:Dataset",
-            "temporal": "2018-01-01/2018-12-31",
-            "modified": "2022-04-01",
-            "keyword": [
-                "deaths",
-                "life expectancy",
-                "mortality",
-                "nchs",
-                "nvss",
-                "sex",
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
-            "identifier": "https://data.cdc.gov/api/views/a5a8-jsrq",
             "description": "The dataset presents life expectancy at birth estimates based on annual complete period life tables for each of the 50 states and the District of Columbia (D.C.)\nin 2018 for the total, male and female populations.",
-            "title": "U.S. State Life Expectancy by Sex, 2018",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27801,22 +27778,58 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/a5a8-jsrq",
+            "issued": "2021-04-05",
+            "keyword": [
+                "deaths",
+                "life expectancy",
+                "mortality",
+                "nchs",
+                "nvss",
+                "sex",
+                "state",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/state-life-expectancy/",
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
+            "temporal": "2018-01-01/2018-12-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "U.S. State Life Expectancy by Sex, 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2010",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and<br />\nhashish, heroin, nonprescription methadone, other opiates and<br />\nsynthetics, PCP, other hallucinogens, methamphetamine, other amphetamines,<br />\nother stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2010) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2010-nid13541",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2010-nid13541"
+                }
+            ],
```

