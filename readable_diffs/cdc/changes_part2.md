# Change History for cdc.json (Part 2)

### Changes from 9cd27cf to 452e48f (Part 2/8)
**Author:** Automated

**Date:** 2025-02-03 20:01:08+00:00

**Message:** Updated data: Mon Feb  3 20:01:08 UTC 2025

```diff
                     "@type": "dcat:Distribution",
@@ -10663,66 +10569,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/62d6-pm5i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/62d6-pm5i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/62d6-pm5i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/62d6-pm5i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/62d6-pm5i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/62d6-pm5i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/62d6-pm5i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/62d6-pm5i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/62d6-pm5i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/62d6-pm5i",
+            "issued": "2021-09-10",
+            "keyword": [
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
+            "landingPage": "https://data.cdc.gov/d/62d6-pm5i",
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
+            "title": "U.S. State and Territorial Public Mask Mandates From April 10, 2020 through August 15, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/62yv-gyiz",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "age<5",
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
-            "identifier": "https://data.cdc.gov/api/views/62yv-gyiz",
             "description": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 , Confirmed to Invasive pneumococcal disease, age <5, Probable  - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease.",
-            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 , Confirmed to Invasive pneumococcal disease, age <5, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10730,67 +10637,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/62yv-gyiz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/62yv-gyiz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/62yv-gyiz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/62yv-gyiz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/62yv-gyiz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/62yv-gyiz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/62yv-gyiz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/62yv-gyiz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/62yv-gyiz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/62yv-gyiz",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "age<5",
+                "confirmed",
+                "invasive pneumococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/62yv-gyiz",
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
+            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 , Confirmed to Invasive pneumococcal disease, age <5, Probable"
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
-                "name": "Environmental Public Health Tracking"
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
@@ -10798,55 +10704,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/647a-wjd2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/647a-wjd2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/647a-wjd2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/647a-wjd2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/647a-wjd2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/647a-wjd2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/647a-wjd2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/647a-wjd2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/647a-wjd2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2022-09-20",
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
+            "title": "U.S. State and Territorial Orders Closing and Reopening Restaurants Issued from March 11, 2020 through May 31, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/64br-p84f",
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
-            "identifier": "https://data.cdc.gov/api/views/64br-p84f",
             "description": "Triclosan is an antimicrobial chemical used in healthcare settings that can be absorbed through the skin. Exposure to triclosan has been positively associated with food and aeroallergy and asthma exacerbation in humans and, although not directly sensitizing, has been demonstrated to augment the allergic response in a mouse model of asthma. The skin barrier and microbiome are thought to play important roles in mediating inflammation and allergy and disruptions may contribute to development of allergic disease. To investigate potential connections of the skin barrier and microbiome with immune responses to triclosan, SKH1 mice were dermally exposed to triclosan (0.5-2%) or vehicle for up to 7 consecutive days.",
-            "title": "Dermal exposure to the immunomodulatory antimicrobial chemical triclosan alters the skin barrier integrity and microbiome in mice",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10854,19 +10772,65 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/64br-p84f",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/64br-p84f",
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
+            "title": "Dermal exposure to the immunomodulatory antimicrobial chemical triclosan alters the skin barrier integrity and microbiome in mice"
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
+            "description": "Provisional counts of deaths by the month the deaths occurred, by age group, sex, and race/ethnicity, for select underlying causes of death for 2020-2021. Final data are provided for 2019. The dataset also includes monthly provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/65mz-jvh5/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/65mz-jvh5/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/65mz-jvh5/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/65mz-jvh5",
             "issued": "2020-09-04",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
             "keyword": [
                 "age",
                 "age group",
@@ -10897,65 +10861,64 @@
                 "sex",
                 "united states"
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
-            "identifier": "https://data.cdc.gov/api/views/65mz-jvh5",
-            "description": "Provisional counts of deaths by the month the deaths occurred, by age group, sex, and race/ethnicity, for select underlying causes of death for 2020-2021. Final data are provided for 2019. The dataset also includes monthly provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
-            "title": "AH Monthly Provisional Counts of Deaths for Select Causes of Death by Sex, Age, and Race and Hispanic Origin",
-            "programCode": [
-                "009:020"
+            "spatial": "United States",
+            "theme": [
+                "NCHS"
+            ],
+            "title": "AH Monthly Provisional Counts of Deaths for Select Causes of Death by Sex, Age, and Race and Hispanic Origin"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "NNDSS - Table II. Hepatitis (viral, acute) - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/65xe-6neq/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/65mz-jvh5/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/65xe-6neq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/65xe-6neq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/65mz-jvh5/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/65xe-6neq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/65xe-6neq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/65mz-jvh5/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/65xe-6neq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/65xe-6neq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "landingPage": "https://data.cdc.gov/d/65xe-6neq",
-            "bureauCode": [
-                "009:00"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/65xe-6neq",
             "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
             "keyword": [
                 "2015",
                 "hepatitis",
@@ -10969,65 +10932,63 @@
                 "nndss",
                 "wonder"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CDC INFO",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/65xe-6neq",
+            "modified": "2016-01-07",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/65xe-6neq",
-            "description": "NNDSS - Table II. Hepatitis (viral, acute) - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Hepatitis (viral, acute)",
-            "programCode": [
-                "009:020"
+            "theme": [
+                "NNDSS"
+            ],
+            "title": "NNDSS - Table II. Hepatitis (viral, acute)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Services-Available-Counseling-2010-To-Pre/66cx-b9a4",
+            "description": "2010-2020.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/65xe-6neq/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/65xe-6neq/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/65xe-6neq/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/66cx-b9a4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/65xe-6neq/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/65xe-6neq/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/66cx-b9a4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/65xe-6neq/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/65xe-6neq/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/66cx-b9a4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "NNDSS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/statesystem/index.html",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/66cx-b9a4",
             "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://chronicdata.cdc.gov/d/h6kq-aiu7"
-            ],
             "keyword": [
                 "callers",
                 "cessation",
@@ -11042,83 +11003,37 @@
                 "services",
                 "state system"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "OSHData Support",
-                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/66cx-b9a4",
-            "description": "2010-2020.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
-            "title": "Quitline \u2013 Services Available \u2013 Counseling - 2010 To Present",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-08-25",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/66cx-b9a4/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/66cx-b9a4/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/66cx-b9a4/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
+            "references": [
+                "https://chronicdata.cdc.gov/d/h6kq-aiu7"
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Services-Available-Counseling-2010-To-Pre/66cx-b9a4",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
             "theme": [
                 "Quitline"
-            ]
+            ],
+            "title": "Quitline \u2013 Services Available \u2013 Counseling - 2010 To Present"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/66i6-hisz",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2019-05-23",
-            "temporal": "1899-2017",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-23",
-            "keyword": [
-                "botulism"
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
-            "identifier": "https://data.cdc.gov/api/views/66i6-hisz",
             "description": "The CDC Botulism Consultation Service, the Alaska Division of Public Health, and the California Department of Public Health provide clinical consultations on suspected cases of all types of botulism except infant botulism. These agencies are the only sources of antitoxin for non-infant botulism in the United States. The California Infant Botulism Treatment and Prevention provides clinical consultations on suspected infant botulism cases; it is the only source of antitoxin for infant botulism in the United States. Together, these clinical consultations provide expert guidance to clinicians and support the collection of epidemiologic and medical information for all suspected botulism cases reported in the United States.",
-            "title": "Botulism",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11126,47 +11041,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/66i6-hisz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/66i6-hisz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/66i6-hisz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/66i6-hisz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/66i6-hisz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/66i6-hisz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/66i6-hisz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/66i6-hisz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/66i6-hisz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/66i6-hisz",
+            "issued": "2019-05-23",
+            "keyword": [
+                "botulism"
+            ],
+            "landingPage": "https://data.cdc.gov/d/66i6-hisz",
+            "language": [
+                "English"
+            ],
+            "modified": "2019-05-23",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "spatial": "USA",
-            "accrualPeriodicity": "Annual",
+            "temporal": "1899-2017",
             "theme": [
                 "Foodborne, Waterborne, and Related Diseases"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Botulism"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/66km-38zv",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_3_technical_documentation.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 3 is the third round of a three-round survey. The sampled participants of RANDS during COVID-19 Round 3 were recruited using NORC at the University of Chicago (NORC)\u2019s AmeriSpeak Panel, and the survey was administered by NORC from May 17, 2021 to June 30, 2021. RANDS during COVID-19 Round 3 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/66km-38zv",
             "issued": "2022-06-08",
-            "@type": "dcat:Dataset",
-            "temporal": "2021",
-            "modified": "2023-04-24",
             "keyword": [
                 "anxiety",
                 "covid-19",
@@ -11187,63 +11129,35 @@
                 "telemedicine",
                 "vaccination"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/66km-38zv",
+            "modified": "2023-04-24",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/66km-38zv",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 3 is the third round of a three-round survey. The sampled participants of RANDS during COVID-19 Round 3 were recruited using NORC at the University of Chicago (NORC)\u2019s AmeriSpeak Panel, and the survey was administered by NORC from May 17, 2021 to June 30, 2021. RANDS during COVID-19 Round 3 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
-            "title": "NCHS Research and Development Survey (RANDS) Round 3 during COVID-19 Restricted File",
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
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_3_technical_documentation.pdf",
+            "temporal": "2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 3 during COVID-19 Restricted File"
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
-                "name": "data.cdc.gov"
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
@@ -11251,64 +11165,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/68ej-h5ze/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/68ej-h5ze/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/68ej-h5ze/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/68ej-h5ze/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/68ej-h5ze/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/68ej-h5ze/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/68ej-h5ze/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/68ej-h5ze/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/68ej-h5ze/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "Motor Vehicle"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/68sm-zh95",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
+            "identifier": "https://data.cdc.gov/api/views/68ej-h5ze",
+            "issued": "2016-09-14",
             "keyword": [
-                "2021",
-                "cholera",
-                "coccidioidomycosis",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/68ej-h5ze",
+            "modified": "2016-09-14",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "theme": [
+                "Motor Vehicle"
+            ],
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 5 - Chicago"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
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
@@ -11316,59 +11225,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/68sm-zh95/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/68sm-zh95/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/68sm-zh95/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/68sm-zh95/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/68sm-zh95/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/68sm-zh95/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/68sm-zh95/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/68sm-zh95/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/68sm-zh95/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table 1H. Cholera to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/68zh-tyt3",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-02-04",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-27",
-            "keyword": [
-                "glossary",
-                "methods"
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
-            "identifier": "https://data.cdc.gov/api/views/68zh-tyt3",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "University of Illinois at Chicago Health Policy Center - Funding Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11376,44 +11290,38 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/68zh-tyt3",
+            "issued": "2015-02-04",
+            "keyword": [
+                "glossary",
+                "methods"
+            ],
+            "landingPage": "https://data.cdc.gov/d/68zh-tyt3",
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
+            "title": "University of Illinois at Chicago Health Policy Center - Funding Glossary and Methodology"
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
-                "name": "data.cdc.gov"
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
@@ -11421,59 +11329,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6dep-qtzm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6dep-qtzm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6dep-qtzm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6dep-qtzm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6dep-qtzm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6dep-qtzm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6dep-qtzm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6dep-qtzm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6dep-qtzm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection"
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
-                "name": "data.cdc.gov"
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
@@ -11481,64 +11395,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6i2x-3kw3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6i2x-3kw3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6i2x-3kw3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6i2x-3kw3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6i2x-3kw3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6i2x-3kw3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6i2x-3kw3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6i2x-3kw3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6i2x-3kw3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6i2x-3kw3",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6i2x-3kw3",
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
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 5 - Chicago"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6ie8-bpiy",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6ie8-bpiy",
             "description": "NNDSS - TABLE 1HH. Syphilis, Congenital to Syphilis, Primary and Secondary \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1HH. Syphilis, Congenital to Syphilis, Primary and Secondary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11546,72 +11455,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6ie8-bpiy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6ie8-bpiy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6ie8-bpiy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6ie8-bpiy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6ie8-bpiy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6ie8-bpiy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6ie8-bpiy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6ie8-bpiy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6ie8-bpiy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6ie8-bpiy",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "nedss",
+                "netss",
+                "nndss",
+                "syphilis congenital",
+                "syphilis primary and secondary",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6ie8-bpiy",
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
+            "title": "NNDSS - TABLE 1HH. Syphilis, Congenital to Syphilis, Primary and Secondary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "keyword": [
-                "covid",
-                "covid19",
-                "covid-19",
-                "covidnet",
-                "covid-net",
-                "hospitalization rate",
-                "hospitalizations",
-                "rate",
-                "rates by age group",
-                "rates by race and ethnicity",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6jg4-xsqq",
             "description": "The Coronavirus Disease 2019 (COVID-19) Hospitalization Surveillance Network (COVID-NET) a network that conducts active, population-based surveillance for laboratory-confirmed COVID-19-associated hospitalizations among children and adults. COVID-NET, along with the Respiratory Syncytial Virus Hospitalization Surveillance Network (RSV-NET) and the Influenza Hospitalization Surveillance Network (FluSurv-NET), comprise the Respiratory Virus Hospitalization Surveillance Network (RESP-NET). The RESP-NET platforms have overlapping surveillance areas and use similar methods to collect data. COVID-NET is CDC\u2019s source for important data on rates of hospitalizations associated with COVID-19. Hospitalization rates show how many people in the surveillance area are hospitalized with COVID-19, compared to the total number of people residing in that area. \n\nData are preliminary and subject to change as more data become available. Data will be updated weekly.",
-            "title": "Weekly Rates of Laboratory-Confirmed COVID-19 Hospitalizations from the COVID-NET Surveillance System",
-            "programCode": [
-                "009:038"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11619,69 +11521,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6jg4-xsqq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6jg4-xsqq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6jg4-xsqq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6jg4-xsqq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6jg4-xsqq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6jg4-xsqq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6jg4-xsqq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6jg4-xsqq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6jg4-xsqq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "COVID-NET Sites",
+            "identifier": "https://data.cdc.gov/api/views/6jg4-xsqq",
+            "issued": "2024-06-26",
+            "keyword": [
+                "covid",
+                "covid19",
+                "covid-19",
+                "covidnet",
+                "covid-net",
+                "hospitalization rate",
+                "hospitalizations",
+                "rate",
+                "rates by age group",
+                "rates by race and ethnicity",
+                "respiratory illness",
+                "respiratory virus response",
+                "respnet",
+                "resp-net",
+                "surveillance"
+            ],
+            "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:038"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "spatial": "COVID-NET Sites",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Weekly Rates of Laboratory-Confirmed COVID-19 Hospitalizations from the COVID-NET Surveillance System"
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
-                "name": "data.cdc.gov"
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
@@ -11689,45 +11596,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6jgb-zrsp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6jgb-zrsp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6jgb-zrsp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6jgb-zrsp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6jgb-zrsp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6jgb-zrsp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6jgb-zrsp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6jgb-zrsp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6jgb-zrsp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nsrcf/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
-            "issued": "2023-07-03",
-            "@type": "dcat:Dataset",
-            "temporal": "2010-03/2010-10",
-            "modified": "2023-07-03",
-            "references": [
-                "https://www.cdc.gov/nchs/data/nsrcf/2010NSRCF_SurveyMethodologyandDocumentation.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "The 2010 National Survey of Residential Care Facilities (NSRCF) is a first-ever national probability sample survey that collects data on U.S. residential care providers, their staffs and \nservices, and the people they serve. It is designed to provide national estimates of the number of residential care facilities operating in the United States, the number of residents receiving care, and the characteristics of both the facilities and their residents. NSRCF was conducted between March and November 2010. All residential care facilities that participated in the survey were places that were licensed, registered, listed, certified, or otherwise regulated by the state and that had 4 or more licensed, certified, or registered beds, provided room and board with at least two meals a day, around-the-clock on-site supervision, and help with personal care such as bathing and dressing or health related services such as medication management. These facilities served a predominantly adult population and had at least one current resident. Facilities licensed to serve the mentally ill or the developmentally disabled populations exclusively were excluded from the survey.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The 2010 NSRCF data were collected through in-person interviews with facility directors and their \ndesignated staffs; no interviews were conducted directly with residents. Facility data included\nquestions on facility characteristics such as ownership, size, types of living arrangements and \namenities, policies, staffing, services, and general resident characteristics. Data collected on \nresidents included questions on the sampled residents\u2019 demographics, living arrangements, \nactivities, health conditions, cognitive and physical functioning, and services received. The total \nnumber of facilities that participated in the 2010 NSRCF is 2,302, and data are available on 8,094\nresidents from these facilities.",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "National Survey of Residential Care Facilities - Restricted Facility-Level Dataset"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6k6h-dzju",
+            "isPartOf": "https://www.cdc.gov/nchs/nsrcf/nsrcf_questionnaires.htm",
+            "issued": "2023-07-03",
             "keyword": [
                 "assisted living facilities",
                 "long-term care",
@@ -11740,73 +11680,41 @@
                 "sdoh-transportation",
                 "sdoh-use-of-health-care"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nsrcf/index.htm",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-03",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/6k6h-dzju",
-            "description": "The 2010 National Survey of Residential Care Facilities (NSRCF) is a first-ever national probability sample survey that collects data on U.S. residential care providers, their staffs and \nservices, and the people they serve. It is designed to provide national estimates of the number of residential care facilities operating in the United States, the number of residents receiving care, and the characteristics of both the facilities and their residents. NSRCF was conducted between March and November 2010. All residential care facilities that participated in the survey were places that were licensed, registered, listed, certified, or otherwise regulated by the state and that had 4 or more licensed, certified, or registered beds, provided room and board with at least two meals a day, around-the-clock on-site supervision, and help with personal care such as bathing and dressing or health related services such as medication management. These facilities served a predominantly adult population and had at least one current resident. Facilities licensed to serve the mentally ill or the developmentally disabled populations exclusively were excluded from the survey.",
-            "title": "National Survey of Residential Care Facilities - Restricted Facility-Level Dataset",
-            "isPartOf": "https://www.cdc.gov/nchs/nsrcf/nsrcf_questionnaires.htm",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "description": "The 2010 NSRCF data were collected through in-person interviews with facility directors and their \ndesignated staffs; no interviews were conducted directly with residents. Facility data included\nquestions on facility characteristics such as ownership, size, types of living arrangements and \namenities, policies, staffing, services, and general resident characteristics. Data collected on \nresidents included questions on the sampled residents\u2019 demographics, living arrangements, \nactivities, health conditions, cognitive and physical functioning, and services received. The total \nnumber of facilities that participated in the 2010 NSRCF is 2,302, and data are available on 8,094\nresidents from these facilities.",
-                    "@type": "dcat:Distribution",
-                    "title": "National Survey of Residential Care Facilities - Restricted Facility-Level Dataset"
-                }
+            "references": [
+                "https://www.cdc.gov/nchs/data/nsrcf/2010NSRCF_SurveyMethodologyandDocumentation.pdf"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "United States",
+            "temporal": "2010-03/2010-10",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Survey of Residential Care Facilities - Restricted Facility-Level Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6kf3-4udg",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "animal",
-                "human",
-                "nedss",
-                "netss",
-                "nndss",
-                "rabies",
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
-            "identifier": "https://data.cdc.gov/api/views/6kf3-4udg",
             "description": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11814,68 +11722,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6kf3-4udg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6kf3-4udg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6kf3-4udg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6kf3-4udg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6kf3-4udg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6kf3-4udg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6kf3-4udg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6kf3-4udg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6kf3-4udg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6kf3-4udg",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "animal",
+                "human",
+                "nedss",
+                "netss",
+                "nndss",
+                "rabies",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6kf3-4udg",
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
+            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-08-30",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-30",
-            "keyword": [
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
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
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6mjs-pnrx",
             "description": "Provisional counts of deaths involving coronavirus disease 2019 (COVID-19) by week and age group, in the United States.",
-            "title": "AH Provisional COVID-19 Deaths by Week and Age",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11883,61 +11789,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6mjs-pnrx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6mjs-pnrx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6mjs-pnrx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6mjs-pnrx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6mjs-pnrx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6mjs-pnrx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6mjs-pnrx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6mjs-pnrx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6mjs-pnrx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6mjs-pnrx",
+            "issued": "2022-08-30",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
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
+            "modified": "2022-08-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by Week and Age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6nbv-ifib",
             "bureauCode": [
                 "009:032"
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
-            "identifier": "https://data.cdc.gov/api/views/6nbv-ifib",
             "description": "This dataset provides data at the county level for the contiguous United States. It includes monthly Standardized Precipitation Evapotranspiration Index (SPEI)  data from 1895-2016 provided by the Cooperative Institute for Climate and Satellites - North Carolina. Please refer to the metadata attachment for more information.\r\n\r\nThese data are used by the CDC's National Environmental Public Health Tracking Network to generate drought measures. Learn more about drought on the Tracking Network's website: https://ephtracking.cdc.gov/showDroughtLanding.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking. \r\n\r\nProblems or Questions? \r\nEmail trackingsupport@cdc.gov.",
-            "title": "Standardized Precipitation Evapotranspiration Index, 1895-2016",
-            "programCode": [
-                "009:20"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11945,47 +11859,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6nbv-ifib/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6nbv-ifib/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6nbv-ifib/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6nbv-ifib/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6nbv-ifib/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6nbv-ifib/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6nbv-ifib/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6nbv-ifib/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6nbv-ifib/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6nbv-ifib",
+            "issued": "2018-07-26",
+            "keyword": [
+                "drought",
+                "environmental health"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6nbv-ifib",
+            "modified": "2018-11-27",
+            "programCode": [
+                "009:20"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Environmental Health & Toxicology"
-            ]
+            ],
+            "title": "Standardized Precipitation Evapotranspiration Index, 1895-2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nhds/index.htm",
+            "accrualPeriodicity": "Database will not be updated again.",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2023-09-27",
-            "@type": "dcat:Dataset",
-            "temporal": "1965\u20142010",
-            "modified": "2023-09-27",
-            "references": [
-                "https://www.cdc.gov/nchs/nhds/nhds_collection.htm",
-                "https://www.cdc.gov/nchs/nhds/nhds_sample_design.htm",
-                "https://www.cdc.gov/nchs/data/series/sr_01/sr01_039.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:nhcs@cdc.gov"
+            },
+            "describedBy": "Only hospitals having six or more beds for in-patient use are included in the survey and before 1988 those in which the average length of stay for all patients was less than 30 days. In 1988 the scope was altered slightly to include all general and children\u2019s general hospitals regardless of the length of stay.",
+            "description": "The National Hospital Discharge Survey (NHDS), conducted from 1965 to 2010, was a national probability survey designed to meet the need for information on characteristics of inpatients discharged from non-Federal short-stay hospitals in the United States. From 1988-2007 the NHDS collected data from a sample of approximately 270,000 inpatient records acquired from a national sample of about 500 hospitals. From 2008 to 2010 the sample size was reduced to 239. Only hospitals with an average length of stay of fewer than 30 days for all patients, general hospitals, or children\u2019s general hospitals are included in the survey. Federal, military, and Department of Veterans Affairs hospitals, as well as hospital units of institutions (such as prison hospitals), and hospitals with fewer than six beds staffed for patient use, are excluded.\n\nBeginning in 1988, two data collection procedures have been used in the survey. The medical abstract form and the automated data tapes contain items that relate to the personal characteristics of the patient. These items include age, sex, race, ethnicity, marital status, and expected sources of payment. Administrative items such as admission and discharge dates (which allow calculation of length of stay), as well as discharge status are also included. Medical information about patients includes diagnoses and procedures coded to the International Classification of Diseases, 9th Revision, Clinical Modification (ICD-9-CM).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/userestricdt.htm",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6nqh-vaj5",
+            "isPartOf": "https://www.cdc.gov/nchs/nhds/nhds_questionnaires.htm",
+            "issued": "2023-09-27",
             "keyword": [
                 "discharge",
                 "hospital",
@@ -11996,54 +11934,37 @@
                 "sdoh-use-of-health-care",
                 "short-stay-hospitals"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:nhcs@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nhds/index.htm",
+            "modified": "2023-09-27",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/6nqh-vaj5",
-            "description": "The National Hospital Discharge Survey (NHDS), conducted from 1965 to 2010, was a national probability survey designed to meet the need for information on characteristics of inpatients discharged from non-Federal short-stay hospitals in the United States. From 1988-2007 the NHDS collected data from a sample of approximately 270,000 inpatient records acquired from a national sample of about 500 hospitals. From 2008 to 2010 the sample size was reduced to 239. Only hospitals with an average length of stay of fewer than 30 days for all patients, general hospitals, or children\u2019s general hospitals are included in the survey. Federal, military, and Department of Veterans Affairs hospitals, as well as hospital units of institutions (such as prison hospitals), and hospitals with fewer than six beds staffed for patient use, are excluded.\n\nBeginning in 1988, two data collection procedures have been used in the survey. The medical abstract form and the automated data tapes contain items that relate to the personal characteristics of the patient. These items include age, sex, race, ethnicity, marital status, and expected sources of payment. Administrative items such as admission and discharge dates (which allow calculation of length of stay), as well as discharge status are also included. Medical information about patients includes diagnoses and procedures coded to the International Classification of Diseases, 9th Revision, Clinical Modification (ICD-9-CM).",
-            "title": "National Hospital Discharge Survey (NHDS) Restricted Data, 1965-2010",
-            "isPartOf": "https://www.cdc.gov/nchs/nhds/nhds_questionnaires.htm",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/userestricdt.htm",
-                    "mediaType": "text/html"
-                }
+            "references": [
+                "https://www.cdc.gov/nchs/nhds/nhds_collection.htm",
+                "https://www.cdc.gov/nchs/nhds/nhds_sample_design.htm",
+                "https://www.cdc.gov/nchs/data/series/sr_01/sr01_039.pdf"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "United States",
-            "describedBy": "Only hospitals having six or more beds for in-patient use are included in the survey and before 1988 those in which the average length of stay for all patients was less than 30 days. In 1988 the scope was altered slightly to include all general and children\u2019s general hospitals regardless of the length of stay.",
-            "accrualPeriodicity": "Database will not be updated again.",
+            "temporal": "1965\u20142010",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Hospital Discharge Survey (NHDS) Restricted Data, 1965-2010"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6nue-dx9c",
-            "issued": "2024-02-12",
             "@type": "dcat:Dataset",
-            "modified": "2024-02-14",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CGW0@cdc.gov",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/6nue-dx9c",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dataset_for_databricks_demo",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12051,66 +11972,50 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6nue-dx9c/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6nue-dx9c/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6nue-dx9c/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6nue-dx9c/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6nue-dx9c/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6nue-dx9c/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6nue-dx9c/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6nue-dx9c/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6nue-dx9c/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/6nue-dx9c",
+            "issued": "2024-02-12",
+            "landingPage": "https://data.cdc.gov/d/6nue-dx9c",
+            "modified": "2024-02-14",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "dataset_for_databricks_demo"
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -12118,74 +12023,90 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6p3a-6xr9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6p3a-6xr9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6p3a-6xr9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6p3a-6xr9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6p3a-6xr9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6p3a-6xr9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6p3a-6xr9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6p3a-6xr9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6p3a-6xr9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6pnq-x3ea",
-            "issued": "2020-03-30",
             "@type": "dcat:Dataset",
-            "modified": "2020-03-30",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "aso7@cdc.gov",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
+            "description": "",
             "identifier": "https://data.cdc.gov/api/views/6pnq-x3ea",
+            "issued": "2020-03-30",
+            "landingPage": "https://data.cdc.gov/d/6pnq-x3ea",
+            "modified": "2020-03-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.cdc.gov"
             },
-            "description": "",
             "title": "NNDSS - TABLE 1FF. Severe acute respiratory\u200b\u200b\u200b\u200b\u200b\u200b\u200b syndrome-associated coronavirus disease to Shigellosis"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6qm2-fbrx",
-            "issued": "2024-07-24",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-24",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/6qm2-fbrx",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12193,59 +12114,50 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6qm2-fbrx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6qm2-fbrx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6qm2-fbrx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6qm2-fbrx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6qm2-fbrx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6qm2-fbrx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6qm2-fbrx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6qm2-fbrx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6qm2-fbrx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/6qm2-fbrx",
+            "issued": "2024-07-24",
+            "landingPage": "https://data.cdc.gov/d/6qm2-fbrx",
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
-                "name": "National Center for Health Statistics"
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
@@ -12253,68 +12165,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6rkc-nb2q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6rkc-nb2q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6rkc-nb2q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6rkc-nb2q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6rkc-nb2q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6rkc-nb2q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6rkc-nb2q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6rkc-nb2q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6rkc-nb2q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-                "name": "data.cdc.gov"
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
@@ -12322,64 +12230,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6rpz-c2y5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6rpz-c2y5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6rpz-c2y5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6rpz-c2y5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6rpz-c2y5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6rpz-c2y5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6rpz-c2y5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6rpz-c2y5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6rpz-c2y5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2019-01-03",
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
+            "title": "NNDSS - Table II. Salmonellosis (excluding typhoid fever and paratyphoid fever) to Shigellosis"
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
@@ -12387,60 +12297,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6ryw-hetw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6ryw-hetw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6ryw-hetw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6ryw-hetw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6ryw-hetw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6ryw-hetw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6ryw-hetw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6ryw-hetw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6ryw-hetw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "landingPage": "https://data.cdc.gov/d/6ssd-y5qt",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-03-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-13",
-            "keyword": [
-                "cdc",
-                "centers for disease control and prevention"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Danielle Sharpe",
                 "hasEmail": "mailto:svi_coordinator@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6ssd-y5qt",
             "description": "The interactive maps are visual representations of the Social Vulnerability Index (SVI). Data were extracted from the US Census and the American Community Survey.",
-            "title": "CDC Social Vulnerability Index (SVI) Mapping Dashboard",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12448,41 +12362,38 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6ssd-y5qt",
+            "issued": "2015-03-24",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6ssd-y5qt",
+            "modified": "2020-02-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Health Statistics"
-            ]
+            ],
+            "title": "CDC Social Vulnerability Index (SVI) Mapping Dashboard"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6svj-q4zv",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-09-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-10-08/2024-02-17",
-            "modified": "2024-10-18",
-            "keyword": [
-                "archive",
-                "ncird",
-                "ncird-id",
-                "respiratory-virus-response"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alicia Budd, Krista Kniss, and Arielle Colon",
                 "hasEmail": "mailto:acp4@cdc.gov, krk9@cdc.gov, nnp8@cdc.gov  "
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6svj-q4zv",
             "description": "This dataset has been archived and will no longer be updated as of 10/16/2024. For updated data, please refer to the <a href=\"https://gis.cdc.gov/grasp/fluview/main.html\"><b>ILINet State Activity Indicator Map</b></a>.\n\nInformation on outpatient visits to health care providers for respiratory illness referred to as influenza-like illness (ILI) is collected through the U.S. Outpatient Influenza-like Illness Surveillance Network (ILINet). ILINet consists of outpatient healthcare providers in all 50 states, Puerto Rico, the District of Columbia, and the U.S. Virgin Islands. More than 100 million patient visits were reported during the 2022-23 season. Each week, more than 3,000 outpatient health care providers around the country report to CDC the number of patient visits for ILI by age group (0-4 years, 5-24 years, 25-49 years, 50-64 years, and \u226565 years) and the total number of visits for any reason. A subset of providers also reports total visits by age group. For this system, ILI is defined as fever (temperature of 100\u00b0F [37.8\u00b0C] or greater) and a cough and/or a sore throat. Activity levels are based on the percent of outpatient visits due to ILI in a jurisdiction compared to the average percent of ILI visits that occur during weeks with little or no influenza virus circulation (non-influenza weeks) in that jurisdiction. The number of sites reporting each week is variable; therefore, baselines are adjusted each week based on which sites within each jurisdiction provide data. To perform this adjustment, provider level baseline ILI ratios are calculated for those that have a sufficient reporting history. Providers that do not have the required reporting history to calculate a provider-specific baseline are assigned the baseline ratio for their practice type. The jurisdiction level baseline is then calculated using a weighted sum of the baseline ratios for each contributing provider. \n\nThe activity levels compare the mean reported percent of visits due to ILI during the current week to the mean reported percent of visits due to ILI during non-influenza weeks. The 13 activity levels correspond to the number of standard deviations below, at, or above the mean for the current week compared with the mean during non-influenza weeks. Activity levels are classified as minimal (levels 1-3), low (levels 4-5), moderate (levels 6-7), high (levels 8-10), and very high (levels 11-13). An activity level of 1 corresponds to an ILI percentage below the mean, level 2 corresponds to an ILI percentage less than 1 standard deviation above the mean, level 3 corresponds to an ILI percentage more than 1 but less than 2 standard deviations above the mean, and so on, with an activity level of 10 corresponding to an ILI percentage 8 to 11 standard deviations above the mean. The very high levels correspond to an ILI percentage 12 to 15 standard deviations above the mean for level 11, 16 to 19 standard deviations above the mean for level 12, and 20 or more standard deviations above the mean for level 13. \n\nDisclaimers: \n\nThe ILI Activity Indicator map reflects the intensity of ILI activity, not the extent of geographic spread of ILI, within a jurisdiction. Therefore, outbreaks occurring in a single area could cause the entire jurisdiction to display high or very high activity levels. In addition, data collected in ILINet may disproportionally represent certain populations within a jurisdiction, and therefore, may not accurately depict the full picture of respiratory illness activity for the entire jurisdiction. Differences in the data presented here by CDC and independently by some health departments likely represent differing levels of data completeness with data presented by the health department likely being more complete. \n\nMore information is available on <a href=\"https://gis.cdc.gov/grasp/fluview/main.html\">FluView Interactive</a>.",
-            "title": "Outpatient Respiratory Illness Activity Map",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12490,68 +12401,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6svj-q4zv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6svj-q4zv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6svj-q4zv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6svj-q4zv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6svj-q4zv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6svj-q4zv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6svj-q4zv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6svj-q4zv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6svj-q4zv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/6svj-q4zv",
+            "issued": "2023-09-26",
+            "keyword": [
+                "archive",
+                "ncird",
+                "ncird-id",
+                "respiratory-virus-response"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6svj-q4zv",
             "license": "https://www.usa.gov/government-works",
-            "theme": [
+            "modified": "2024-10-18",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "spatial": "US",
+            "temporal": "2022-10-08/2024-02-17",
+            "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Outpatient Respiratory Illness Activity Map"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6tk5-h85s",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "carbapenemase-producing carbapenem-resistant enterobacteriaceae",
-                "enterobacter spp.",
-                "escherichia coli",
-                "klebsiella spp.",
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
-            "identifier": "https://data.cdc.gov/api/views/6tk5-h85s",
             "description": "NNDSS - Table II. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.  \r\n\r\n\u2020 Data for carbapenemase-producing carbapenem-resistant Enterobacteriaceae (CP-CRE) will be displayed in this table after the CDC obtains Office of Management and Budget Paperwork Reduction Act approval to receive data for this condition.",
-            "title": "NNDSS - Table II. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12559,71 +12466,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6tk5-h85s/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6tk5-h85s/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6tk5-h85s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6tk5-h85s/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6tk5-h85s/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6tk5-h85s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6tk5-h85s/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6tk5-h85s/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6tk5-h85s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6tk5-h85s",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "carbapenemase-producing carbapenem-resistant enterobacteriaceae",
+                "enterobacter spp.",
+                "escherichia coli",
+                "klebsiella spp.",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6tk5-h85s",
+            "modified": "2019-01-03",
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
+            "title": "NNDSS - Table II. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae"
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
-            "temporal": "1970/2015",
-            "modified": "2022-03-29",
-            "references": [
-                "https://www.cdc.gov/nchs/data/databriefs/db162.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf"
-            ],
-            "keyword": [
-                "birth rates",
-                "ethnicity",
-                "hispanic origin",
-                "nchs",
-                "nonmarital",
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
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6tkz-y37d",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "This dataset includes birth rates for unmarried women by age group, race, and Hispanic origin in the United States since 1970. \n\nMethods for collecting information on marital status changed over the reporting period and have been documented in:\n\n\u2022 Ventura SJ, Bachrach CA. Nonmarital childbearing in the United States, 1940\u201399. National vital statistics reports; vol 48 no 16. Hyattsville, Maryland: National Center for Health Statistics. 2000. Available from: http://www.cdc.gov/nchs/data/nvsr/nvsr48/nvs48_16.pdf.\n\u2022 National Center for Health Statistics. User guide to the 2013 natality public use file. Hyattsville, Maryland: National Center for Health Statistics. 2014. Available from: http://www.cdc.gov/nchs/data_access/VitalStatsOnline.htm.\n\nNational data on births by Hispanics origin exclude data for Louisiana, New Hampshire, and Oklahoma in 1989; for New Hampshire and Oklahoma in 1990; for New Hampshire in 1991 and 1992. Information on reporting Hispanic origin is detailed in the Technical Appendix for the 1999 public-use natality data file (see (ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/Nat1999doc.pdf.)\n\nAll birth data by race before 1980 are based on race of the child. Starting in 1980, birth data by race are based on race of the mother.",
-            "title": "NCHS - Birth Rates for Unmarried Women by Age, Race, and Hispanic Origin: United States",
-            "isPartOf": "NCHS - Birth Rates for Unmarried Women by Age, Race, and Hispanic Origin: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12631,65 +12534,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6tkz-y37d/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6tkz-y37d/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6tkz-y37d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6tkz-y37d/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6tkz-y37d/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6tkz-y37d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6tkz-y37d/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6tkz-y37d/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6tkz-y37d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/6tkz-y37d",
+            "isPartOf": "NCHS - Birth Rates for Unmarried Women by Age, Race, and Hispanic Origin: United States",
+            "issued": "2015-12-02",
+            "keyword": [
+                "birth rates",
+                "ethnicity",
+                "hispanic origin",
+                "nchs",
+                "nonmarital",
+                "race",
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
+            "references": [
+                "https://www.cdc.gov/nchs/data/databriefs/db162.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf"
+            ],
+            "rights": "public",
+            "spatial": "50 states and District of Columbia",
+            "temporal": "1970/2015",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - Birth Rates for Unmarried Women by Age, Race, and Hispanic Origin: United States"
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
-                "name": "data.cdc.gov"
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
@@ -12697,65 +12611,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6tmq-h6uy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6tmq-h6uy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6tmq-h6uy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6tmq-h6uy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6tmq-h6uy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6tmq-h6uy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6tmq-h6uy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6tmq-h6uy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6tmq-h6uy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6tmq-h6uy",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6tmq-h6uy",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 1 - Boston"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6uy5-4d9d",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-22",
-            "keyword": [
-                "2022",
-                "animal",
-                "human",
-                "nedss",
-                "netss",
-                "nndss",
-                "rabies",
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
-            "identifier": "https://data.cdc.gov/api/views/6uy5-4d9d",
             "description": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12763,73 +12671,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6uy5-4d9d/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6uy5-4d9d/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6uy5-4d9d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6uy5-4d9d/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6uy5-4d9d/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6uy5-4d9d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6uy5-4d9d/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6uy5-4d9d/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6uy5-4d9d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6uy5-4d9d",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "animal",
+                "human",
+                "nedss",
+                "netss",
+                "nndss",
+                "rabies",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6uy5-4d9d",
+            "modified": "2022-02-22",
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
+            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human"
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
-                "brfss",
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
-            "identifier": "https://data.cdc.gov/api/views/6vp6-wxuq",
+            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-Local-Data-for-Better-Health-2017-relea/6vp6-wxuq",
             "description": "This is the complete dataset for the 500 Cities project 2019 release. This dataset includes 2017, 2016 model-based small area estimates for 27 measures of chronic disease related to unhealthy behaviors (5), health outcomes (13), and use of preventive services (9). Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. It represents a first-of-its kind effort to release information on a large scale for cities and for small areas within those cities. It includes estimates for the 500 largest US cities and approximately 28,000 census tracts within these cities. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these measures include Behavioral Risk Factor Surveillance System (BRFSS) data (2017, 2016), Census Bureau 2010 census population data, and American Community Survey (ACS) 2013-2017, 2012-2016 estimates. Because some questions are only asked every other year in the BRFSS, there are 7 measures (all teeth lost, dental visits, mammograms, pap tests, colorectal cancer screening, core preventive services among older adults, and sleep less than 7 hours) from the 2016 BRFSS that are the same in the 2019 release as the previous 2018 release. More information about the methodology can be found at www.cdc.gov/500cities.",
-            "title": "500 Cities: Local Data for Better Health, 2019 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12837,70 +12738,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6vp6-wxuq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6vp6-wxuq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6vp6-wxuq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6vp6-wxuq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6vp6-wxuq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6vp6-wxuq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6vp6-wxuq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6vp6-wxuq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6vp6-wxuq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-Local-Data-for-Better-Health-2017-relea/6vp6-wxuq",
+            "identifier": "https://data.cdc.gov/api/views/6vp6-wxuq",
+            "issued": "2023-07-18",
+            "keyword": [
+                "500cities",
+                "behaviors",
+                "brfss",
+                "census",
+                "cities",
+                "outcomes",
+                "prevalence",
+                "prevention",
+                "tracts",
+                "unhealthy"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
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
+            "title": "500 Cities: Local Data for Better Health, 2019 release"
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
-            "temporal": "2020-01-01/2020-12-31",
-            "modified": "2022-10-18",
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
-            "identifier": "https://data.cdc.gov/api/views/6vqh-esgs",
             "description": "Provisional count of deaths involving coronavirus disease 2019 (COVID-19) by United States county of occurrence, from January 1, 2020 through December 31, 2020.",
-            "title": "AH County of Occurrence COVID-19 Death Counts, 2020 Provisional",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12908,71 +12813,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6vqh-esgs/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6vqh-esgs/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6vqh-esgs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6vqh-esgs/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6vqh-esgs/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6vqh-esgs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6vqh-esgs/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6vqh-esgs/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6vqh-esgs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/6vqh-esgs",
+            "issued": "2020-09-24",
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
+                "united states",
+                "yearly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2022-10-18",
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
+            "title": "AH County of Occurrence COVID-19 Death Counts, 2020 Provisional"
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
-                "name": "National Center for Health Statistics"
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
@@ -12980,59 +12887,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6vwk-ensg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6vwk-ensg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6vwk-ensg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6vwk-ensg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6vwk-ensg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6vwk-ensg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6vwk-ensg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6vwk-ensg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6vwk-ensg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/6wqg-8ykc",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6wqg-8ykc",
             "description": "In August 2020 there were over 186,000 employees in the oil and gas extraction industry in the United States (United States Department of Labor. Bureau of Labor Statistics, 2020).  Many workers in the upstream oil extraction industry have potential risk of crude oil vapor (COV) inhalation.  There are many current knowledge gaps regarding the health effects from inhalation of complex mixtures found in crude oil vapors.  To aid research in filling these gaps, an automated system that could carefully deliver and control the COV concentration within an animal inhalation exposure chamber was needed.  The objective of this project was to develop an automated computer-controlled system to expose small laboratory animals to precise concentrations of crude oil vapor (COV).",
-            "title": "Automated oil vapor inhalation exposure system",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13040,44 +12958,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6wqg-8ykc",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/6wqg-8ykc",
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
+            "title": "Automated oil vapor inhalation exposure system"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6yz5-ufy2",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/6yz5-ufy2",
             "description": "NNDSS - TABLE 1II. Tetanus to Trichinellosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13085,59 +12993,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6yz5-ufy2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6yz5-ufy2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6yz5-ufy2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6yz5-ufy2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6yz5-ufy2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6yz5-ufy2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6yz5-ufy2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6yz5-ufy2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6yz5-ufy2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "NNDSS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6zuv-bn3z",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2022-10-17",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-27",
-            "keyword": [
-                "food safety",
-                "restaurant grading"
+            "identifier": "https://data.cdc.gov/api/views/6yz5-ufy2",
+            "issued": "2019-04-23",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "tetanus",
+                "toxic shock syndrome (other than streptococcal)",
+                "trichinellosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6yz5-ufy2",
+            "modified": "2020-01-02",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "theme": [
+                "NNDSS"
+            ],
+            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hao Tian",
                 "hasEmail": "mailto:ejq7@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
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
@@ -13145,73 +13059,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6zuv-bn3z/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6zuv-bn3z/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6zuv-bn3z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/6zuv-bn3z/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6zuv-bn3z/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6zuv-bn3z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/6zuv-bn3z/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/6zuv-bn3z/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/6zuv-bn3z/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6zuv-bn3z",
+            "issued": "2022-10-17",
+            "keyword": [
+                "food safety",
+                "restaurant grading"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6zuv-bn3z",
+            "language": [
+                "English"
+            ],
+            "modified": "2022-10-27",
+            "programCode": [
+                "009:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "spatial": "United States",
             "systemOfRecords": "No",
             "theme": [
                 "Environmental Health & Toxicology"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Survey Data - Restaurant Grading"
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
-                "children",
-                "dnpao",
-                "low income",
-                "obese",
-                "obesity",
-                "overweight",
-                "wic",
-                "wic-pc"
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
-            "identifier": "https://data.cdc.gov/api/views/735e-byxc",
+            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Women-Infa/735e-byxc",
             "description": "This dataset includes data on weight status for children aged 3 months to 4 years old from Women, Infant, and Children Participant and Program Characteristics (WIC-PC). This data is used for DNPAO's Data, Trends, and Maps database, which provides national and state specific data on obesity, nutrition, physical activity, and breastfeeding. For more information about WIC-PC visit https://www.fns.usda.gov/wic/national-survey-wic-participants.",
-            "title": "Nutrition, Physical Activity, and Obesity - Women, Infant, and Child",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13219,66 +13125,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/735e-byxc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/735e-byxc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/735e-byxc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/735e-byxc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/735e-byxc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/735e-byxc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/735e-byxc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/735e-byxc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/735e-byxc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Women-Infa/735e-byxc",
+            "identifier": "https://data.cdc.gov/api/views/735e-byxc",
+            "issued": "2025-01-30",
+            "keyword": [
+                "children",
+                "dnpao",
+                "low income",
+                "obese",
+                "obesity",
+                "overweight",
+                "wic",
+                "wic-pc"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
+            "modified": "2025-02-03",
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
                 "Nutrition, Physical Activity, and Obesity"
-            ]
+            ],
+            "title": "Nutrition, Physical Activity, and Obesity - Women, Infant, and Child"
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
-                "name": "data.cdc.gov"
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
@@ -13286,65 +13194,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/759d-qk63/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/759d-qk63/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/759d-qk63/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/759d-qk63/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/759d-qk63/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/759d-qk63/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/759d-qk63/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/759d-qk63/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/759d-qk63/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1KK. Vancomycin-intermediate Staphylococcus aureus to Varicella morbidity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/75b3-73qi",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/75b3-73qi",
             "description": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Illnesses with similar clinical presentation that result from Spotted Fever Group Rickettsia infections are reported as Spotted Fever Rickettsioses. Rocky Mountain Spotted Fever (RMSF), caused by Rickettsia rickettsii, is the most common and well-known Spotted Fever.",
-            "title": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13352,69 +13260,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/75b3-73qi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/75b3-73qi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/75b3-73qi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/75b3-73qi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/75b3-73qi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/75b3-73qi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/75b3-73qi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/75b3-73qi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/75b3-73qi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/75b3-73qi",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "spotted fever rickettsiosis",
+                "syphilis primary and secondary",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/75b3-73qi",
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
+            "title": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis"
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
-            "temporal": "2020-01-01/2020-12-31",
-            "modified": "2022-04-01",
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
-            "identifier": "https://data.cdc.gov/api/views/75vb-d79q",
             "description": "Provisional count of deaths involving coronavirus disease 2019 (COVID-19) by United States county of residence, from January 1, 2020 through December 31, 2020.",
-            "title": "AH County of Residence COVID-19 Deaths Counts, 2020 Provisional",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13422,58 +13327,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/75vb-d79q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/75vb-d79q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/75vb-d79q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/75vb-d79q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/75vb-d79q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/75vb-d79q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/75vb-d79q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/75vb-d79q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/75vb-d79q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/75vb-d79q",
+            "issued": "2021-05-12",
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
+                "united states",
+                "yearly"
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
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "2020-01-01/2020-12-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH County of Residence COVID-19 Deaths Counts, 2020 Provisional"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/76u3-26ik",
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
-                "name": "data.cdc.gov"
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
@@ -13481,44 +13399,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/76u3-26ik",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/76u3-26ik",
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
+            "title": "Video-Based 3D pose estimation for residential roofing-dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/natality.htm",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2016-08-03",
-            "@type": "dcat:Dataset",
-            "temporal": "2021-01-01/2024-09-30",
-            "modified": "2024-12-18",
-            "keyword": [
-                "birth rate",
-                "cesarean delivery",
-                "fertility rate",
-                "nchs",
-                "preterm birth",
-                "vital statistics rapid release",
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
-            "identifier": "https://data.cdc.gov/api/views/76vv-a7x8",
             "description": "Provisional estimates of selected reproductive indicators. Estimates are presented for: general fertility rates, age-specific birth rates, total and low risk cesarean delivery rates, preterm birth rates and other gestational age categories.",
-            "title": "NCHS - VSRR Quarterly provisional estimates for selected birth indicators",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13526,52 +13435,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/76vv-a7x8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/76vv-a7x8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/76vv-a7x8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/76vv-a7x8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/76vv-a7x8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/76vv-a7x8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/76vv-a7x8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/76vv-a7x8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/76vv-a7x8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/76vv-a7x8",
+            "issued": "2016-08-03",
+            "keyword": [
+                "birth rate",
+                "cesarean delivery",
+                "fertility rate",
+                "nchs",
+                "preterm birth",
+                "vital statistics rapid release",
+                "vsrr"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/natality.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "2021-01-01/2024-09-30",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - VSRR Quarterly provisional estimates for selected birth indicators"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/783t-9j9i",
-            "issued": "2024-07-23",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/783t-9j9i",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13579,65 +13500,50 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/783t-9j9i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/783t-9j9i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/783t-9j9i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/783t-9j9i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/783t-9j9i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/783t-9j9i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/783t-9j9i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/783t-9j9i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/783t-9j9i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/783t-9j9i",
+            "issued": "2024-07-23",
+            "landingPage": "https://data.cdc.gov/d/783t-9j9i",
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
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2019-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
-            "keyword": [
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "health service area",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
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
-            "identifier": "https://data.cdc.gov/api/views/7873-6w4v",
             "description": "Provisional count of deaths involving coronavirus disease 2019 (COVID-19) in the United States by health service area. Health service area is determined by the decedent's county of residence.",
-            "title": "AH Provisional COVID-19 Deaths Counts by Health Service Area",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13645,67 +13551,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7873-6w4v/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7873-6w4v/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7873-6w4v/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7873-6w4v/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7873-6w4v/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7873-6w4v/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7873-6w4v/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7873-6w4v/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7873-6w4v/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/7873-6w4v",
+            "issued": "2019-06-26",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "health service area",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "united states",
+                "yearly"
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
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths Counts by Health Service Area"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/dhdsp/maps/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-02-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-24",
-            "keyword": [
-                "cardiovascular",
-                "cardiovascular disease",
-                "counties",
-                "county",
-                "heart",
-                "heart disease",
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
-            "identifier": "https://data.cdc.gov/api/views/7b9s-s8ck",
             "description": "This dataset documents rates and trends in heart disease and stroke mortality. Specifically, this report presents county (or county equivalent) estimates of heart disease and stroke death rates in 2000-2019 and trends during two intervals (2000-2010, 2010-2019) by age group (ages 35\u201364 years, ages 65 years and older), race/ethnicity (non-Hispanic American Indian/Alaska Native, non-Hispanic Asian/Pacific Islander, non-Hispanic Black, Hispanic, non-Hispanic White), and sex (women, men). The rates and trends were estimated using a Bayesian spatiotemporal model and a smoothed over space, time, and demographic group. Rates are age-standardized in 10-year age groups using the 2010 US population. Data source: National Vital Statistics System.",
-            "title": "Rates and Trends in Heart Disease and Stroke Mortality Among US Adults (35+) by County, Age Group, Race/Ethnicity, and Sex \u2013 2000-2019",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13713,72 +13622,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7b9s-s8ck/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7b9s-s8ck/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7b9s-s8ck/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7b9s-s8ck/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7b9s-s8ck/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7b9s-s8ck/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7b9s-s8ck/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7b9s-s8ck/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7b9s-s8ck/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "theme": [
+            "identifier": "https://data.cdc.gov/api/views/7b9s-s8ck",
+            "issued": "2022-02-18",
+            "keyword": [
+                "cardiovascular",
+                "cardiovascular disease",
+                "counties",
+                "county",
+                "heart",
+                "heart disease",
+                "stroke"
+            ],
+            "landingPage": "https://www.cdc.gov/dhdsp/maps/index.htm",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-08-24",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "theme": [
                 "Heart Disease & Stroke Prevention"
-            ]
+            ],
+            "title": "Rates and Trends in Heart Disease and Stroke Mortality Among US Adults (35+) by County, Age Group, Race/Ethnicity, and Sex \u2013 2000-2019"
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
-                "county",
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
-            "identifier": "https://data.cdc.gov/api/views/7cmc-7y5g",
             "description": "This dataset contains model-based county-level estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. Project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2021 or 2020 county population estimates, and American Community Survey (ACS) 2017\u20132021 or 2016\u20132020 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. These data can be joined with the census 2020 county boundary file in a GIS system to produce maps for 36 measures at the county level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=2c3deb0c05a748b391ea8c9cf9903588",
-            "title": "PLACES: County Data (GIS Friendly Format), 2023 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13786,71 +13688,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7cmc-7y5g/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7cmc-7y5g/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7cmc-7y5g/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7cmc-7y5g/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7cmc-7y5g/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7cmc-7y5g/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7cmc-7y5g/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7cmc-7y5g/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7cmc-7y5g/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7cmc-7y5g",
+            "issued": "2024-07-15",
+            "keyword": [
+                "behaviors",
+                "county",
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
+            "title": "PLACES: County Data (GIS Friendly Format), 2023 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7dk4-g6vg",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "N/A",
-            "issued": "2023-07-06",
-            "@type": "dcat:Dataset",
-            "temporal": "8/1/2020 - 5/3/2024",
-            "modified": "2025-01-17",
-            "references": [
-                "CDT aggregate hospital data displays: https://covid.cdc.gov/covid-data-tracker/#cases_new-admissions-rate-state CDT Hospitalizations Landing Page: https://covid.cdc.gov/covid-data-tracker/#hospitalizations-landing NHSN Hospital Data Reporting: https://www.cdc.gov/nhsn/covid19/hospital-reporting.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fnhsn%2Fcovid19%2Ftransition.html  Full reporting guidance: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf"
-            ],
-            "keyword": [
-                "admissions",
-                "coronavirus",
-                "covid-19",
-                "hospital capacity",
-                "hospitalizations",
-                "hospital occupancy",
-                "icu beds",
-                "inpatient beds",
-                "ncird-corvd"
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
-            "identifier": "https://data.cdc.gov/api/views/7dk4-g6vg",
             "description": "<b>Note:</b> After May 3, 2024, this dataset will no longer be updated because hospitals are no longer required to report data on COVID-19 hospital admissions, hospital capacity, or occupancy data to HHS through CDC\u2019s National Healthcare Safety Network (NHSN). The related CDC COVID Data Tracker site was revised or retired on May 10, 2023.\n\nThis dataset represents weekly COVID-19 hospitalization data and metrics aggregated to national, state/territory, and regional levels. COVID-19 hospitalization data are reported to CDC\u2019s National Healthcare Safety Network, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN and included in this dataset represent aggregated counts and include metrics capturing information specific to COVID-19 hospital admissions, and inpatient and ICU bed capacity occupancy.\n\n<b>Reporting information:</b><ul><li>As of December 15, 2022, COVID-19 hospital data are required to be reported to NHSN, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Prior to December 15, 2022, hospitals reported data directly to the U.S. Department of Health and Human Services (HHS) or via a state submission for collection in the HHS Unified Hospital Data Surveillance System (UHDSS).</li><li>While CDC reviews these data for errors and corrects those found, some reporting errors might still exist within the data. To minimize errors and inconsistencies in data reported, CDC removes outliers before calculating the metrics. CDC and partners work with reporters to correct these errors and update the data in subsequent weeks.</li><li>Many hospital subtypes, including acute care and critical access hospitals, as well as Veterans Administration, Defense Health Agency, and Indian Health Service hospitals, are included in the metric calculations provided in this report. Psychiatric, rehabilitation, and religious non-medical hospital types are excluded from calculations.</li><li>Data are aggregated and displayed for hospitals with the same Centers for Medicare and Medicaid Services (CMS) Certification Number (CCN), which are assigned by CMS to counties based on the CMS Provider of Services files.</li><li>Full details on COVID-19 hospital data reporting guidance can be found here: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf</li></ul>\n\n<b>Metric details:</b><ul><li><b>Time Period:</b> timeseries data will update weekly on Mondays as soon as they are reviewed and verified, usually before 8 pm ET. Updates will occur the following day when reporting coincides with a federal holiday. Note: Weekly updates might be delayed due to delays in reporting. All data are provisional. Because these provisional counts are subject to change, including updates to data reported previously, adjustments can occur. Data may be updated since original publication due to delays in reporting (to account for data received after a given Thursday publication) or data quality corrections.</li><li><b>New COVID-19 Hospital Admissions (count):</b> Number of new admissions of patients with laboratory-confirmed COVID-19 in the previous week (including both adult and pediatric admissions) in the entire jurisdiction.</li><li><b>New COVID-19 Hospital Admissions (7-Day Average):</b> 7-day average of new admissions of patients with laboratory-confirmed COVID-19 in the previous week (including both adult and pediatric admissions) in the entire jurisdiction.</li><li><b>Cumulative COVID-19 Hospital Admissions:</b> Cumulative total number of admissions of patients with labo",
-            "title": "Weekly United States COVID-19 Hospitalization Metrics by Jurisdiction \u2013 ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13858,75 +13761,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7dk4-g6vg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7dk4-g6vg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7dk4-g6vg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7dk4-g6vg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7dk4-g6vg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7dk4-g6vg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7dk4-g6vg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7dk4-g6vg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7dk4-g6vg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/7dk4-g6vg",
+            "issued": "2023-07-06",
+            "keyword": [
+                "admissions",
+                "coronavirus",
+                "covid-19",
+                "hospital capacity",
+                "hospitalizations",
+                "hospital occupancy",
+                "icu beds",
+                "inpatient beds",
+                "ncird-corvd"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7dk4-g6vg",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "No longer updated (dataset archived)",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
+            },
+            "references": [
+                "CDT aggregate hospital data displays: https://covid.cdc.gov/covid-data-tracker/#cases_new-admissions-rate-state CDT Hospitalizations Landing Page: https://covid.cdc.gov/covid-data-tracker/#hospitalizations-landing NHSN Hospital Data Reporting: https://www.cdc.gov/nhsn/covid19/hospital-reporting.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fnhsn%2Fcovid19%2Ftransition.html  Full reporting guidance: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf"
+            ],
+            "rights": "N/A",
+            "spatial": "US",
+            "temporal": "8/1/2020 - 5/3/2024",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Weekly United States COVID-19 Hospitalization Metrics by Jurisdiction \u2013 ARCHIVED"
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
-            "identifier": "https://data.cdc.gov/api/views/7dvv-y64a",
+            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-7-Month-Follow-Up-Not-Comparable-Across-S/7dvv-y64a",
             "description": "2010-2011.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
-            "title": "Quitline \u2013 7-Month Follow-Up (Not Comparable Across States) \u2013 2010-2011",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13934,68 +13836,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7dvv-y64a/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7dvv-y64a/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7dvv-y64a/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7dvv-y64a/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7dvv-y64a/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7dvv-y64a/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7dvv-y64a/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7dvv-y64a/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7dvv-y64a/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-7-Month-Follow-Up-Not-Comparable-Across-S/7dvv-y64a",
+            "identifier": "https://data.cdc.gov/api/views/7dvv-y64a",
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
+            "title": "Quitline \u2013 7-Month Follow-Up (Not Comparable Across States) \u2013 2010-2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7ecz-2gu3",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7ecz-2gu3",
             "description": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers'. NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
-            "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14003,55 +13910,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7ecz-2gu3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7ecz-2gu3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7ecz-2gu3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7ecz-2gu3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7ecz-2gu3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7ecz-2gu3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7ecz-2gu3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7ecz-2gu3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7ecz-2gu3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7ecz-2gu3",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/7ecz-2gu3",
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
+            "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/7ehz-refy",
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
-                "name": "data.cdc.gov"
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
@@ -14059,42 +13977,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7ehz-refy",
+            "issued": "2024-12-18",
+            "landingPage": "https://data.cdc.gov/d/7ehz-refy",
+            "modified": "2024-12-18",
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
+            "title": "Nerve agent exposure and physiological stress alter brain microstructure and immune profiles after inflammatory challenge in a long-term animal model of Gulf War Illness"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:00"
             ],
-            "landingPage": "https://data.cdc.gov/d/7esm-uptm",
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-19",
-            "keyword": [
-                "122 cities",
-                "2015",
-                "death",
-                "influenza",
-                "mortality",
-                "pneumonia"
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
-            "identifier": "https://data.cdc.gov/api/views/7esm-uptm",
             "description": "TABLE III. Deaths in 122 U.S. cities - 2015122 Cities Mortality Reporting System \ufffd\ufffd\ufffd Each week, the vital statistics offices of 122 cities across the United States report the total number of death certificates processed and the number of those for which pneumonia or influenza was listed as the underlying or contributing cause of death by age group (Under 28 days, 28 days \ufffd\ufffd\ufffd1 year, 1-14 years, 15-24 years, 25-44 years, 45-64 years, 65-74 years, 75-84 years, and \ufffd\ufffd\ufffd 85 years).FOOTNOTE:U: Unavailable      -: No reported cases * Mortality data in this table are voluntarily reported from 122 cities in the United States, most of which have populations of 100,000 or more. A death is reported by the place of its occurrence and by the week that the death certificate was filed. Fetal deaths are not included. ** Totals include unknown ages. *** Partial counts for this city.",
-            "title": "TABLE III. Deaths in 122 U.S. cities",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14102,63 +14012,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7esm-uptm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7esm-uptm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7esm-uptm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7esm-uptm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7esm-uptm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7esm-uptm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7esm-uptm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7esm-uptm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7esm-uptm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/7esm-uptm",
+            "issued": "2016-01-07",
+            "keyword": [
+                "122 cities",
+                "2015",
+                "death",
+                "influenza",
+                "mortality",
+                "pneumonia"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7esm-uptm",
+            "modified": "2018-01-19",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "TABLE III. Deaths in 122 U.S. cities"
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
-                "name": "data.cdc.gov"
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
@@ -14166,66 +14073,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7gnu-j6js/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7gnu-j6js/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7gnu-j6js/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7gnu-j6js/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7gnu-j6js/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7gnu-j6js/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7gnu-j6js/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7gnu-j6js/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7gnu-j6js/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1U. Leptospirosis to Listeriosis, Probable"
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
-                "name": "data.cdc.gov"
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
@@ -14233,121 +14140,122 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7jik-jwvu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7jik-jwvu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7jik-jwvu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7jik-jwvu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7jik-jwvu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7jik-jwvu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7jik-jwvu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7jik-jwvu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7jik-jwvu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nehrs/about.htm",
+            "accrualPeriodicity": "Future funding patterns past 2024 are uncertain however, we expect yearly or biannually is reasonable R/P1Y or R/P2Y",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "Restricted data files can be requested through the Research Data Center. Restricted files contain sensitive protected health information.",
-            "issued": "2024-02-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2018, 2019, 2021",
-            "modified": "2024-02-20",
-            "references": [
-                "https://www.cdc.gov/nchs/data/nehrs/2018_NEHRS_Questionnaire_08092018-508.pdf",
-                "https://www.cdc.gov/nchs/data/nehrs/NEHRS2019-Questionnaire-508.pdf",
-                "https://www.cdc.gov/nchs/data/nehrs/NEHRS2020-Questionnaire-508.pdf"
-            ],
-            "keyword": [
-                "electronic health records",
-                "nchs",
-                "nehrs",
-                "telemedicine"
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
-            "identifier": "https://data.cdc.gov/api/views/7jqv-mu8u",
-            "description": "The National Electronic Health Records Survey (NEHRS) is an annual survey of non-federally employed, office-based physicians practicing in the United States (excluding those in the specialties of anesthesiology, radiology, and pathology). NEHRS began in 2008 and was originally designed as an annual mail supplement to the National Ambulatory Medical Care Survey (NAMCS). Since 2012, NEHRS has been administered as a survey independent of NAMCS.\nData from NEHRS can be used to produce state and national estimates of EHR adoption and capabilities, burden associated with EHRs, and progress physicians have made towards meeting the policy goals of the HITECH Act. In more recent years, survey questions have also asked about Promoting Interoperability programs, sponsored by the Centers for Medicare and Medicaid Services (CMS).",
-            "title": "National Electronic Health Records Survey, Public-use data: 2018, 2019, 2021",
-            "isPartOf": "https://www.cdc.gov/nchs/nehrs/questionnaires.htm",
+            "describedBy": "https://www.cdc.gov/nchs/data/nehrs/2021-NEHRS-public-use-file-layout-508.pdf, https://www.cdc.gov/nchs/data/nehrs/2019-NEHRS-public-use-layout-508.pdf, https://www.cdc.gov/nchs/data/nehrs/2018-NEHRS-public-restricted-layout-508.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The National Electronic Health Records Survey (NEHRS) is an annual survey of non-federally employed, office-based physicians practicing in the United States (excluding those in the specialties of anesthesiology, radiology, and pathology). NEHRS began in 2008 and was originally designed as an annual mail supplement to the National Ambulatory Medical Care Survey (NAMCS). Since 2012, NEHRS has been administered as a survey independent of NAMCS.\nData from NEHRS can be used to produce state and national estimates of EHR adoption and capabilities, burden associated with EHRs, and progress physicians have made towards meeting the policy goals of the HITECH Act. In more recent years, survey questions have also asked about Promoting Interoperability programs, sponsored by the Centers for Medicare and Medicaid Services (CMS).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NEHRS/",
-                    "description": "SAS and STATA .zip files",
                     "@type": "dcat:Distribution",
+                    "description": "SAS and STATA .zip files",
+                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NEHRS/",
+                    "mediaType": "text/html",
                     "title": "NEHRS 2018, 2019, 2021"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data/nehrs/2021-NEHRS-public-use-file-layout-508.pdf, https://www.cdc.gov/nchs/data/nehrs/2019-NEHRS-public-use-layout-508.pdf, https://www.cdc.gov/nchs/data/nehrs/2018-NEHRS-public-restricted-layout-508.pdf",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Future funding patterns past 2024 are uncertain however, we expect yearly or biannually is reasonable R/P1Y or R/P2Y",
+            "identifier": "https://data.cdc.gov/api/views/7jqv-mu8u",
+            "isPartOf": "https://www.cdc.gov/nchs/nehrs/questionnaires.htm",
+            "issued": "2024-02-20",
+            "keyword": [
+                "electronic health records",
+                "nchs",
+                "nehrs",
+                "telemedicine"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nehrs/about.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-02-20",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/data/nehrs/2018_NEHRS_Questionnaire_08092018-508.pdf",
+                "https://www.cdc.gov/nchs/data/nehrs/NEHRS2019-Questionnaire-508.pdf",
+                "https://www.cdc.gov/nchs/data/nehrs/NEHRS2020-Questionnaire-508.pdf"
+            ],
+            "rights": "Restricted data files can be requested through the Research Data Center. Restricted files contain sensitive protected health information.",
+            "spatial": "United States",
+            "temporal": "2018, 2019, 2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Electronic Health Records Survey, Public-use data: 2018, 2019, 2021"
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
-                "name": "data.cdc.gov"
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
@@ -14355,65 +14263,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7kht-czfj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7kht-czfj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7kht-czfj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7kht-czfj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7kht-czfj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7kht-czfj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7kht-czfj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7kht-czfj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7kht-czfj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1C. Arboviral diseases, St. Louis encephalitis virus to Western equine encephalitis virus"
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
-                "name": "data.cdc.gov"
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
@@ -14421,72 +14329,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7mbm-jety/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7mbm-jety/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7mbm-jety/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7mbm-jety/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7mbm-jety/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7mbm-jety/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7mbm-jety/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7mbm-jety/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7mbm-jety/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Chlamydia to Coccidioidomycosis"
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
-                "name": "data.cdc.gov"
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
@@ -14494,64 +14396,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7mra-9cq9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7mra-9cq9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7mra-9cq9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7mra-9cq9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7mra-9cq9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7mra-9cq9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7mra-9cq9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7mra-9cq9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7mra-9cq9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "data.cdc.gov"
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
                 "009:00"
             ],
-            "landingPage": "https://data.cdc.gov/d/7njk-uncd",
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
-                "name": "data.cdc.gov"
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
@@ -14559,63 +14471,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7njk-uncd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7njk-uncd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7njk-uncd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7njk-uncd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7njk-uncd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7njk-uncd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7njk-uncd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7njk-uncd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7njk-uncd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/7njk-uncd",
+            "issued": "2015-08-10",
+            "keyword": [
+                "americas",
+                "chikungunya",
+                "predictions",
+                "travelers"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7njk-uncd",
+            "modified": "2018-02-21",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "Nowcast Predictions for Local Transmission of Chikungunya Virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-14",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://chronicdata.cdc.gov/d/fip8-rcng"
-            ],
-            "keyword": [
-                "average cost per pack",
-                "cigarette sales",
-                "office on smoking and health",
-                "osh",
-                "tax",
-                "tax burden on tobacco"
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
-            "identifier": "https://data.cdc.gov/api/views/7nwe-3aj9",
+            "describedBy": "https://chronicdata.cdc.gov/Policy/The-Tax-Burden-on-Tobacco-1970-2018/7nwe-3aj9",
             "description": "1970-2019. Orzechowski and Walker. Tax Burden on Tobacco. Tax burden data was obtained from the annual compendium on tobacco revenue and industry statistics, The Tax Burden on Tobacco. Data are reported on an annual basis; Data include federal and state-level information regarding taxes applied to the price of a pack of cigarettes.",
-            "title": "The Tax Burden on Tobacco, 1970-2019",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14623,70 +14531,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7nwe-3aj9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7nwe-3aj9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7nwe-3aj9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7nwe-3aj9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7nwe-3aj9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7nwe-3aj9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7nwe-3aj9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7nwe-3aj9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7nwe-3aj9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Policy/The-Tax-Burden-on-Tobacco-1970-2018/7nwe-3aj9",
+            "identifier": "https://data.cdc.gov/api/views/7nwe-3aj9",
+            "issued": "2023-07-14",
+            "keyword": [
+                "average cost per pack",
+                "cigarette sales",
+                "office on smoking and health",
+                "osh",
+                "tax",
+                "tax burden on tobacco"
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
+                "https://chronicdata.cdc.gov/d/fip8-rcng"
+            ],
             "theme": [
                 "Policy"
-            ]
+            ],
+            "title": "The Tax Burden on Tobacco, 1970-2019"
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
-                "name": "data.cdc.gov"
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
@@ -14694,66 +14599,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7pb7-w9us/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7pb7-w9us/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7pb7-w9us/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7pb7-w9us/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7pb7-w9us/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7pb7-w9us/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7pb7-w9us/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7pb7-w9us/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7pb7-w9us/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Lyme disease to Meningococcal"
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
-                "hispanic origin",
-                "live birth rate",
-                "marital status",
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
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7pcd-2tnr",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "https://www.cdc.gov/nchs/data-visualization/births-to-unmarried-women/index.htm",
-            "title": "NCHS - Pregnancy and Live Birth Rates, by Marital Status and Race and Hispanic Origin: United States, 1990-2010",
-            "isPartOf": "NCHS - Pregnancy and Live Birth Rates, by Marital Status and Race and Hispanic Origin: United States, 1990-2010",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14761,66 +14669,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7pcd-2tnr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7pcd-2tnr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7pcd-2tnr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7pcd-2tnr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7pcd-2tnr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7pcd-2tnr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7pcd-2tnr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7pcd-2tnr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7pcd-2tnr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/7pcd-2tnr",
+            "isPartOf": "NCHS - Pregnancy and Live Birth Rates, by Marital Status and Race and Hispanic Origin: United States, 1990-2010",
+            "issued": "2015-12-02",
+            "keyword": [
+                "hispanic origin",
+                "live birth rate",
+                "marital status",
+                "nchs",
+                "race",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-03-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "rights": "public",
+            "spatial": "United States",
+            "temporal": "1990/2010",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - Pregnancy and Live Birth Rates, by Marital Status and Race and Hispanic Origin: United States, 1990-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7pvw-pdbr",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-05-18",
-            "temporal": "2020-01-22/2023-05-10",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "aggregate county data",
-                "cases",
-                "coronavirus",
-                "covid-19",
-                "ncird-corvd"
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
-            "identifier": "https://data.cdc.gov/api/views/7pvw-pdbr",
             "description": "The Public Health Emergency (PHE) declaration for COVID-19 expired on May 11, 2023. As a result, the Aggregate Case and Death Surveillance System will be discontinued. Although these data will continue to be publicly available, this dataset will no longer be updated.\n\nOn October 20, 2022, CDC began retrieving aggregate case and death data from jurisdictional and state partners weekly instead of daily. \n\nThis dataset includes the URLs that were used by the aggregate county data collection process that compiled aggregate case and death counts by county. Within this file, each of the states (plus select jurisdictions and territories) are listed along with the county web sources which were used for pulling these numbers. Some states had a single statewide source for collecting the county data, while other states and local health jurisdictions may have had standalone sources for individual counties. In the cases where both local and state web sources were listed, a composite approach was taken so that the maximum value reported for a location from either source was used. The initial raw data were sourced from these links and ingested into the CDC aggregate county dataset before being published on the COVID Data Tracker.",
-            "title": "United States COVID-19 County Level Data Sources - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14828,66 +14739,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7pvw-pdbr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7pvw-pdbr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7pvw-pdbr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7pvw-pdbr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7pvw-pdbr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7pvw-pdbr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7pvw-pdbr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7pvw-pdbr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7pvw-pdbr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7pvw-pdbr",
+            "issued": "2022-05-18",
+            "keyword": [
+                "aggregate county data",
+                "cases",
+                "coronavirus",
+                "covid-19",
+                "ncird-corvd"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7pvw-pdbr",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
+            },
             "spatial": "US",
-            "accrualPeriodicity": "No longer updated (dataset archived)",
+            "temporal": "2020-01-22/2023-05-10",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "United States COVID-19 County Level Data Sources - ARCHIVED"
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
-                "name": "data.cdc.gov"
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
@@ -14895,83 +14804,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7rci-qmm9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7rci-qmm9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7rci-qmm9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7rci-qmm9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7rci-qmm9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7rci-qmm9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7rci-qmm9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7rci-qmm9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7rci-qmm9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1GG. Smallpox to Streptococcal toxic shock syndrome"
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
-                "linguistics",
-                "machine learning",
-                "ml",
-                "mmwr",
-                "morphology",
-                "ncstltphiw",
-                "pcd",
-                "phic",
-                "semantics",
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
-                "name": "NCSTLTPHIW(PHIC)/ADIDS"
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
@@ -14979,69 +14871,87 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7rih-tqi5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7rih-tqi5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7rih-tqi5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7rih-tqi5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7rih-tqi5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7rih-tqi5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7rih-tqi5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7rih-tqi5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7rih-tqi5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "linguistics",
+                "machine learning",
+                "ml",
+                "mmwr",
+                "morphology",
+                "ncstltphiw",
+                "pcd",
+                "phic",
+                "semantics",
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
+                "name": "NCSTLTPHIW(PHIC)/ADIDS"
+            },
+            "references": [
+                "\"https://github.com/cmheilig/harvest-cdc-journals?tab=readme-ov-file\"",
+                "\"https://www.cdc.gov/mmwr/\"",
+                "\"https://wwwnc.cdc.gov/eid\"",
+                "\"https://www.cdc.gov/pcd/\""
+            ],
+            "temporal": "1982 - 2023",
             "theme": [
                 "National Center for State, Tribal, Local, and Territorial Public Health Infrastructure and Workforce"
-            ]
+            ],
+            "title": "CDC Text Corpora for Learners: MMWR, EID, and PCD Article Metadata"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nnhs/index.htm",
+            "accrualPeriodicity": "None",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
-            "issued": "2024-01-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2004-08-01/2004-12-31",
-            "modified": "2024-03-25",
-            "keyword": [
-                "long-term care",
-                "national nursing home survey",
-                "nursing home residents",
-                "nursing home staff",
-                "research-data-center"
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
-            "identifier": "https://data.cdc.gov/api/views/7ssk-h5k2",
-            "description": "The 2004 National Nursing Home Survey (NNHS), conducted between August and December of 2004, was reintroduced into the field after a five-year break, during which time the survey was redesigned and expanded to collect many new data items. All nursing homes that participated in the NNHS had at least three beds and were either certified (by Medicare or Medicaid) or had a state license to operate as a nursing home. The redesigned survey was administered using a computer-assisted personal interviewing (CAPI) system and included a supplemental survey of nursing assistants employed by nursing homes, the National Nursing Assistant Survey (NNAS), which was sponsored by the Office of the Assistant Secretary for Planning and Evaluation (APSE). \n\nThe National Nursing Home Survey provides information on nursing homes from two perspectives-that of the provider of services and that of the recipient of care. Data about the facilities include characteristics such as size, ownership, Medicare/Medicaid certification, services provided and specialty programs offered, and charges. For recipients, data were obtained on demographic characteristics, health status and medications taken, services received, and sources of payment.\n\nData for the survey were obtained through personal interviews with facility administrators and designated staff who used administrative records to answer questions about the facilities, staff, services and programs, and medical records to answer questions about the residents.\n\nThe total number of nursing home facilities that participated in NNHS is 1,174 and the total number of nursing assistants that participated in the National Nursing Assistant Survey is 3,017.",
-            "title": "2004 National Nursing Home Survey - Restricted Facility Dataset",
-            "isPartOf": "https://www.cdc.gov/nchs/nnhs/nnhs_questionnaires.htm",
+            "describedBy": "https://www.cdc.gov/nchs/data/nnhsd/2004NNHS_DesignCollectionEstimates_072706tags.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The 2004 National Nursing Home Survey (NNHS), conducted between August and December of 2004, was reintroduced into the field after a five-year break, during which time the survey was redesigned and expanded to collect many new data items. All nursing homes that participated in the NNHS had at least three beds and were either certified (by Medicare or Medicaid) or had a state license to operate as a nursing home. The redesigned survey was administered using a computer-assisted personal interviewing (CAPI) system and included a supplemental survey of nursing assistants employed by nursing homes, the National Nursing Assistant Survey (NNAS), which was sponsored by the Office of the Assistant Secretary for Planning and Evaluation (APSE). \n\nThe National Nursing Home Survey provides information on nursing homes from two perspectives-that of the provider of services and that of the recipient of care. Data about the facilities include characteristics such as size, ownership, Medicare/Medicaid certification, services provided and specialty programs offered, and charges. For recipients, data were obtained on demographic characteristics, health status and medications taken, services received, and sources of payment.\n\nData for the survey were obtained through personal interviews with facility administrators and designated staff who used administrative records to answer questions about the facilities, staff, services and programs, and medical records to answer questions about the residents.\n\nThe total number of nursing home facilities that participated in NNHS is 1,174 and the total number of nursing assistants that participated in the National Nursing Assistant Survey is 3,017.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15050,40 +14960,48 @@
                     "title": "2004 National Nursing Home Survey - Restricted Facility Dataset"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7ssk-h5k2",
+            "isPartOf": "https://www.cdc.gov/nchs/nnhs/nnhs_questionnaires.htm",
+            "issued": "2024-01-16",
+            "keyword": [
+                "long-term care",
+                "national nursing home survey",
+                "nursing home residents",
+                "nursing home staff",
+                "research-data-center"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nnhs/index.htm",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-03-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data/nnhsd/2004NNHS_DesignCollectionEstimates_072706tags.pdf",
-            "accrualPeriodicity": "None",
+            "temporal": "2004-08-01/2004-12-31",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2004 National Nursing Home Survey - Restricted Facility Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/7vg3-e5u2",
-            "issued": "2023-01-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-25",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Shaw",
                 "hasEmail": "mailto:nrb7@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7vg3-e5u2",
             "description": "This table provides county-level prevalence for 2018 for seven US states using linked statewide health and education data. For full methods see:\nShaw KA, Williams S, Hughes MM, Warren Z, Bakian AV, Durkin MS, et al. Statewide county-level autism spectrum disorder prevalence estimates \u2014 seven U.S. states, 2018. Annals of Epidemiology. 2023 Jan 18; Available from: https://www.sciencedirect.com/science/article/pii/S1047279723000182",
-            "title": "county-level ASD prevalence estimates",
-            "programCode": [
-                "009:030"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15091,65 +15009,52 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7vg3-e5u2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7vg3-e5u2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7vg3-e5u2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7vg3-e5u2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7vg3-e5u2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7vg3-e5u2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7vg3-e5u2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7vg3-e5u2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7vg3-e5u2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/7vg3-e5u2",
+            "issued": "2023-01-25",
+            "landingPage": "https://data.cdc.gov/d/7vg3-e5u2",
+            "modified": "2023-01-25",
+            "programCode": [
+                "009:030"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "county-level ASD prevalence estimates"
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
-                "name": "data.cdc.gov"
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
@@ -15157,66 +15062,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7vnz-2mjz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7vnz-2mjz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7vnz-2mjz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7vnz-2mjz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7vnz-2mjz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7vnz-2mjz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7vnz-2mjz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7vnz-2mjz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7vnz-2mjz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Hepatitis (viral, acute)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7xhe-mv2e",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7xhe-mv2e",
             "description": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNotice:  Measles data for weeks 1-4 (in Table 1v) were updated on 02-28-2020 to correct the classification of imported and indigenous. For all weeks, measles is considered imported if the disease was acquired outside of the United States and is considered indigenous if the disease was acquired anywhere within the United States or it is not known where the disease was acquired.\n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\n\u00a7 Measles is considered imported if the disease was acquired outside of the United States and is considered indigenous if the disease was acquired anywhere within the United States or it is not known where the disease was acquired.",
-            "title": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15224,73 +15131,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7xhe-mv2e/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7xhe-mv2e/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7xhe-mv2e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7xhe-mv2e/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7xhe-mv2e/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7xhe-mv2e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7xhe-mv2e/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7xhe-mv2e/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7xhe-mv2e/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7xhe-mv2e",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "imported",
+                "indigenous",
+                "malaria",
+                "measles",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7xhe-mv2e",
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
+            "title": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7xva-uux8",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-09-27",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-11-05/2024-02-17",
-            "modified": "2025-01-31",
-            "keyword": [
-                "coronavirus",
-                "covid19",
-                "ed",
-                "emergency department",
-                "flu",
-                "influenza",
-                "national syndromic surveillance program",
-                "ncird",
-                "nssp",
-                "ophdst",
-                "respiratory syncytial",
-                "respiratory syncytial virus",
-                "rsv",
-                "rvr",
-                "virus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Syndromic Surveillance Program",
                 "hasEmail": "mailto:nssp@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7xva-uux8",
             "description": "NSSP Emergency Department Visits - COVID-19, Flu, RSV, Combined \u2013 by Demographic Category \n\nFor additional information, please see: <a href=\"https://www.cdc.gov/ncird/surveillance/respiratory-illnesses/index.html#companion-guide\"><b>Companion Guide: NSSP Emergency Department Data on Respiratory Illness</b></a>.\n\nUpdated once per week on Fridays.",
-            "title": "NSSP Emergency Department Visits - COVID-19, Flu, RSV, Combined \u2013 by Demographic Category",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15298,69 +15199,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7xva-uux8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7xva-uux8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7xva-uux8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7xva-uux8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7xva-uux8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7xva-uux8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7xva-uux8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7xva-uux8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7xva-uux8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/7xva-uux8",
+            "issued": "2023-09-27",
+            "keyword": [
+                "coronavirus",
+                "covid19",
+                "ed",
+                "emergency department",
+                "flu",
+                "influenza",
+                "national syndromic surveillance program",
+                "ncird",
+                "nssp",
+                "ophdst",
+                "respiratory syncytial",
+                "respiratory syncytial virus",
+                "rsv",
+                "rvr",
+                "virus"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7xva-uux8",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "spatial": "U.S.",
+            "temporal": "2022-11-05/2024-02-17",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "NSSP Emergency Department Visits - COVID-19, Flu, RSV, Combined \u2013 by Demographic Category"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7xvh-y5vh",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2021-09-10",
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
                 "fn": "Craig Kassinger",
                 "hasEmail": "mailto:cak8@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Environmental Public Health Tracking"
-            },
-            "identifier": "https://data.cdc.gov/api/views/7xvh-y5vh",
             "description": "State and territorial executive orders, administrative orders, resolutions, proclamations, and other official publicly available government communications are collected from government websites and cataloged and coded using Microsoft Excel by one or more coders with one or more additional coders conducting quality assurance.\n\nData were collected to determine when individuals in states and territories were subject to executive orders, administrative orders, resolutions, proclamations, and other official publicly available government communications related to  COVID-19 banning gatherings of various sizes either (1) generally, or specified that the gathering limit applied only when social distancing was not possible, or (2) even if participants practiced social distancing.\n\nThese data are derived from on the publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly ban gatherings found by the CDC, COVID-19 Community Intervention and Critical Populations Task Force, Monitoring and Evaluation Team & CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 11, 2020 through August 15, 2021. These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded, as well as official government communications such as announcements that counties have progressed through new phases of reopening pursuant to an executive order, directive, or other executive branch action, and posted to government websites; news media reports on restrictions were excluded. Recommendations and guidance documents not included or adopted by reference in an order are not included in these data. These data do not include mandatory business closures, curfews, or requirements/recommendations for people to stay in their homes. Due to limitations of the National Environmental Public Health Tracking Network Data Explorer, these data do not include tribes or cities, nor was a distinction made between county orders that applied county-wide versus those that were limited to unincorporated areas of the county. Effective and expiration dates were coded using only the date provided; no distinction was made based on the specific time of the day the order became effective or expired. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
-            "title": "U.S. State and Territorial Gathering Bans: March 11, 2020-August 15, 2021 by County by Day",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15368,42 +15275,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7xvh-y5vh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7xvh-y5vh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7xvh-y5vh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7xvh-y5vh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7xvh-y5vh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7xvh-y5vh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7xvh-y5vh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7xvh-y5vh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7xvh-y5vh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7xvh-y5vh",
+            "issued": "2021-09-10",
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
+            "landingPage": "https://data.cdc.gov/d/7xvh-y5vh",
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
+            "title": "U.S. State and Territorial Gathering Bans: March 11, 2020-August 15, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nhis/teen.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "The National Health Interview Survey (NHIS)\u2014Teen was a follow-back survey of Sample Children ages 12-17 years old (herein teen) for whom a parent completed the National Health Interview Survey (NHIS) and also provided permission for the teen to participate. NHIS\u2014Teen is a self-administered survey that teens completed themselves either on the web or paper (mailed). Recruitment for NHIS\u2014Teen occurred July 2021\u2014December 2023 during the NHIS Sample Child interview. Teens with permission received an invitation to go online and complete a questionnaire about their own health. Mailed paper questionnaires were sent to nonrespondents. Questions were included to test concordance with parent-reported responses, address time-sensitive data needs, assess public health attitudes or behaviors, and contribute to developmental work to understand differences between parent and self-reported measures of health. \n\nThe majority of NHIS\u2014Teen survey content focused on the health behaviors, social and emotional wellbeing, and healthcare experiences of teens. Detailed sociodemographic characteristics (e.g. health insurance coverage type, family income) as reported by the parent in the NHIS Sample Child interview can be linked to NHIS\u2014Teen. NHIS\u2014Teen was a pilot survey with data collection concluding in March 2024. There are currently no plans to field additional iterations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The National Health Interview Survey (NHIS)\u2014Teen was a follow-back survey of Sample Children ages 12-17 years old (herein teen) for whom a parent completed the National Health Interview Survey (NHIS) and also provided permission for the teen to participate. NHIS\u2014Teen is a self-administered survey that teens completed themselves either on the web or paper (mailed). Recruitment for NHIS\u2014Teen occurred July 2021\u2014December 2023 during the NHIS Sample Child interview. Teens with permission received an invitation to go online and complete a questionnaire about their own health. Mailed paper questionnaires were sent to nonrespondents. Questions were included to test concordance with parent-reported responses, address time-sensitive data needs, assess public health attitudes or behaviors, and contribute to developmental work to understand differences between parent and self-reported measures of health.",
+                    "downloadURL": "https://www.cdc.gov/nchs/nhis/teen.htm",
+                    "mediaType": "text/html",
+                    "title": "NHIS\u2014Teen Restricted Use File"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/7ym9-zzt7",
             "issued": "2024-10-18",
-            "@type": "dcat:Dataset",
-            "temporal": "2021-2023",
-            "modified": "2024-10-18",
             "keyword": [
                 "dhis",
                 "injury",
@@ -15416,64 +15358,36 @@
                 "sdoh-social-emotional",
                 "sdoh-use-of-health-care"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nhis/teen.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-18",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/7ym9-zzt7",
-            "description": "The National Health Interview Survey (NHIS)\u2014Teen was a follow-back survey of Sample Children ages 12-17 years old (herein teen) for whom a parent completed the National Health Interview Survey (NHIS) and also provided permission for the teen to participate. NHIS\u2014Teen is a self-administered survey that teens completed themselves either on the web or paper (mailed). Recruitment for NHIS\u2014Teen occurred July 2021\u2014December 2023 during the NHIS Sample Child interview. Teens with permission received an invitation to go online and complete a questionnaire about their own health. Mailed paper questionnaires were sent to nonrespondents. Questions were included to test concordance with parent-reported responses, address time-sensitive data needs, assess public health attitudes or behaviors, and contribute to developmental work to understand differences between parent and self-reported measures of health. \n\nThe majority of NHIS\u2014Teen survey content focused on the health behaviors, social and emotional wellbeing, and healthcare experiences of teens. Detailed sociodemographic characteristics (e.g. health insurance coverage type, family income) as reported by the parent in the NHIS Sample Child interview can be linked to NHIS\u2014Teen. NHIS\u2014Teen was a pilot survey with data collection concluding in March 2024. There are currently no plans to field additional iterations.",
-            "title": "NHIS\u2014Teen Restricted Use File",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/nchs/nhis/teen.htm",
-                    "description": "The National Health Interview Survey (NHIS)\u2014Teen was a follow-back survey of Sample Children ages 12-17 years old (herein teen) for whom a parent completed the National Health Interview Survey (NHIS) and also provided permission for the teen to participate. NHIS\u2014Teen is a self-administered survey that teens completed themselves either on the web or paper (mailed). Recruitment for NHIS\u2014Teen occurred July 2021\u2014December 2023 during the NHIS Sample Child interview. Teens with permission received an invitation to go online and complete a questionnaire about their own health. Mailed paper questionnaires were sent to nonrespondents. Questions were included to test concordance with parent-reported responses, address time-sensitive data needs, assess public health attitudes or behaviors, and contribute to developmental work to understand differences between parent and self-reported measures of health.",
-                    "@type": "dcat:Distribution",
-                    "title": "NHIS\u2014Teen Restricted Use File"
-                }
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
+            "temporal": "2021-2023",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NHIS\u2014Teen Restricted Use File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/7zky-in8p",
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
-            "identifier": "https://data.cdc.gov/api/views/7zky-in8p",
             "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012, 2014.",
-            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014,  Region 10 - Seattle",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15481,66 +15395,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7zky-in8p/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7zky-in8p/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7zky-in8p/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/7zky-in8p/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7zky-in8p/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7zky-in8p/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/7zky-in8p/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/7zky-in8p/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/7zky-in8p/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7zky-in8p",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7zky-in8p",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014,  Region 10 - Seattle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/oralhealth/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-14",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://www.cdc.gov/oralhealthdata/"
-            ],
-            "keyword": [
-                "division of oral health",
-                "healthy people",
-                "nohss",
-                "oral health",
-                "water fluoridation",
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
-            "identifier": "https://data.cdc.gov/api/views/8235-5d73",
+            "describedBy": "https://chronicdata.cdc.gov/Oral-Health/Water-Fluoridation-Statistics-Percent-of-PWS-popul/8235-5d73",
             "description": "2000-2018. Water Fluoridation Statistics is a biennial report of the percentage and number of people receiving fluoridated water from 2000 through 2018, originally published at http://www.cdc.gov/fluoridation/statistics/index.htm. For more information, see: http://www.cdc.gov/oralhealthdata/overview/fluoridation_indicators.html",
-            "title": "Water Fluoridation Statistics - Percent of PWS population receiving fluoridated water",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15548,73 +15456,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8235-5d73/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8235-5d73/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8235-5d73/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8235-5d73/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8235-5d73/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8235-5d73/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8235-5d73/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8235-5d73/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8235-5d73/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Oral-Health/Water-Fluoridation-Statistics-Percent-of-PWS-popul/8235-5d73",
+            "identifier": "https://data.cdc.gov/api/views/8235-5d73",
+            "issued": "2023-07-14",
+            "keyword": [
+                "division of oral health",
+                "healthy people",
+                "nohss",
+                "oral health",
+                "water fluoridation",
+                "wfrs"
+            ],
+            "landingPage": "http://www.cdc.gov/oralhealth/",
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
+                "https://www.cdc.gov/oralhealthdata/"
+            ],
             "theme": [
                 "Oral Health"
-            ]
+            ],
+            "title": "Water Fluoridation Statistics - Percent of PWS population receiving fluoridated water"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/82ci-krud",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "N/A",
-            "issued": "2023-06-15",
-            "@type": "dcat:Dataset",
-            "temporal": "5/11/2023 - 5/3/2024",
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
-                "inpatient beds",
-                "ncird-corvd"
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
-            "identifier": "https://data.cdc.gov/api/views/82ci-krud",
             "description": "<b>Note:</b> After May 3, 2024, this dataset will no longer be updated because hospitals are no longer required to report data on COVID-19 hospital admissions, hospital capacity, or occupancy data to HHS through CDC\u2019s National Healthcare Safety Network (NHSN). The related CDC COVID Data Tracker site was revised or retired on May 10, 2023.\n\n<b>Note:</b>\n<b>May 3,2024:</b> Due to incomplete or missing hospital data received for the April 21,2024 through April 27, 2024 reporting period, the COVID-19 Hospital Admissions Level could not be calculated for CNMI and will be reported as \u201cNA\u201d or \u201cNot Available\u201d in the COVID-19 Hospital Admissions Level data released on May 3, 2024.\n\n\nThis dataset represents COVID-19 hospitalization data and metrics aggregated to county or county-equivalent, for all counties or county-equivalents (including territories) in the United States as of the initial date of reporting for each weekly metric. COVID-19 hospitalization data are reported to CDC\u2019s National Healthcare Safety Network, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN and included in this dataset represent aggregated counts and include metrics capturing information specific to COVID-19 hospital admissions, and inpatient and ICU bed capacity occupancy.\n\n<b>Reporting information:</b><ul><li>As of December 15, 2022, COVID-19 hospital data are required to be reported to  NHSN, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Prior to December 15, 2022, hospitals reported data directly to the U.S. Department of Health and Human Services (HHS) or via a state submission for collection in the HHS Unified Hospital Data Surveillance System (UHDSS). </li><li>While CDC reviews these data for errors and corrects those found, some reporting errors might still exist within the data. To minimize errors and inconsistencies in data reported, CDC removes outliers before calculating the metrics. CDC and partners work with reporters to correct these errors and update the data in subsequent weeks.</li><li>Many hospital subtypes, including acute care and critical access hospitals, as well as Veterans Administration, Defense Health Agency, and Indian Health Service hospitals, are included in the metric calculations provided in this report. Psychiatric, rehabilitation, and religious non-medical hospital types are excluded from calculations.  </li><li>Data are aggregated and displayed for hospitals with the same Centers for Medicare and Medicaid Services (CMS) Certification Number (CCN), which are assigned by CMS to counties based on the CMS Provider of Services files. </li> <li>Full details on COVID-19 hospital data reporting guidance can be found here: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf</li></ul>\n<b>Calculation of county-level hospital metrics:</b><ul><li>County-level hospital data are derived using calculations performed at the Health Service Area (HSA) level. An HSA is defined by CDC\u2019s National Center for Health Statistics as a geographic area containing at least one county which is self-contained with respect to the population\u2019s provision of routine hospital care. Every county in the United States is assigned to an HSA, and each HSA must contain at least one hospital. Therefore, use of HSAs in the calculation of local hospital metrics allows for more accurate characterization of the relationship between health care utilization and health status at the local level. </li><li>Data presented at the county-level represent admissions, hosp",
-            "title": "Weekly United States COVID-19 Hospitalization Metrics by County (Historical) \u2013 ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15622,67 +15525,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/82ci-krud/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/82ci-krud/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/82ci-krud/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/82ci-krud/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/82ci-krud/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/82ci-krud/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/82ci-krud/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/82ci-krud/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/82ci-krud/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/82ci-krud",
+            "issued": "2023-06-15",
+            "keyword": [
+                "admissions",
+                "coronavirus",
+                "covid-19",
+                "hospital capacity",
+                "hospitalizations",
+                "hospital occupancy",
+                "icu beds",
+                "inpatient beds",
+                "ncird-corvd"
+            ],
+            "landingPage": "https://data.cdc.gov/d/82ci-krud",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "No longer updated (dataset archived)",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
+            },
+            "references": [
+                "CDT county-level hospital data displays: https://covid.cdc.gov/covid-data-tracker/#cases_new-admissions-rate-county  NHSN Hospital Data Reporting: https://www.cdc.gov/nhsn/covid19/hospital-reporting.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fnhsn%2Fcovid19%2Ftransition.html  Full reporting guidance: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf"
+            ],
+            "rights": "N/A",
+            "spatial": "US",
+            "temporal": "5/11/2023 - 5/3/2024",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Weekly United States COVID-19 Hospitalization Metrics by County (Historical) \u2013 ARCHIVED"
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
-                "name": "data.cdc.gov"
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
@@ -15690,68 +15599,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/82nv-dn3y/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/82nv-dn3y/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/82nv-dn3y/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/82nv-dn3y/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/82nv-dn3y/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/82nv-dn3y/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/82nv-dn3y/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/82nv-dn3y/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/82nv-dn3y/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1HH. Syphilis, Congenital to Syphilis, Primary and Secondary"
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
-                "laboratory",
-                "ncird-corvd"
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
-            "identifier": "https://data.cdc.gov/api/views/8396-v7yb",
             "description": "On October 20, 2022, CDC began retrieving aggregate case and death data from jurisdictional and state partners weekly instead of daily. This dataset contains archived community transmission and related data elements by county as originally displayed on the COVID Data Tracker. Although these data will continue to be publicly available, this dataset has not been updated since October 20, 2022. An archived dataset containing weekly community transmission data by county as originally posted can also be found here: <a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/dt66-w6m6\">Weekly COVID-19 County Level of Community Transmission as Originally Posted | Data | Centers for Disease Control and Prevention (cdc.gov)</a>. \n\n<b>Related data</b>\nCDC has been providing the public with two versions of COVID-19 county-level community transmission level data: this dataset with the daily values as originally posted on the COVID Data Tracker, and an historical dataset with daily data as well as the updates and corrections from state and local health departments. Similar to this dataset, the <a href=\"https://data.cdc.gov/Public-Health-Surveillance/United-States-COVID-19-County-Level-of-Community-T/nra9-vzzn\">original historical dataset</a> is archived on 10/20/2022. It will continue to be publicly available but will no longer be updated. A new dataset containing historical community transmission data by county is now published weekly and can be found at: <a href=\"https://data.cdc.gov/dataset/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn\">Weekly COVID-19 County Level of Community Transmission Historical Changes | Data | Centers for Disease Control and Prevention (cdc.gov)</a>.\n\nThis public use dataset has 7 data elements reflecting community transmission levels for all available counties and jurisdictions. It contains reported daily transmission levels at the county level with the same values used to display transmission maps on the COVID Data Tracker. Each day, the dataset is appended to contain the most recent day's data. Transmission level is set to low, moderate, substantial, or high using the calculation rules below.\n\n<b>Methods for calculating county level of community transmission indicator</b>\nThe County Level of Community Transmission indicator uses two metrics: (1) total new COVID-19 cases per 100,000 persons in the last 7 days and (2) percentage of positive SARS-CoV-2 diagnostic nucleic acid amplification tests (NAAT) in the last 7 days. For each of these metrics, CDC classifies transmission values as low, moderate, substantial, or high (below and <a href=\"https://www.cdc.gov/mmwr/volumes/70/wr/mm7030e2.htm?s_cid=mm7030e2_w#T1_down\">here</a>). If the values for each of these two metrics differ (e.g., one indicates moderate and the other low), then the higher of the two should be used for decision-making.\n\n<b>CDC core metrics of and thresholds for community transmission levels of SARS-CoV-2</b>\n\n<b>Total New Case Rate Metric:</b> \"New cases per 100,000 persons in the past 7 days\" is calculated by adding the number of new cases in the county (or other administrative level) in the last 7 days divided by the population in the county (or other administrative level) and multiplying by 100,000. \"New cases per 100,000 persons in the past 7 days\" is considered to have a transmission level of Low (0-9.99); Moderate (10.00-49.99); Substantial (50.00-99.99); and High (greater than or equal to 100.00).\n\n<b>Test Percent Positivity Metric:</b> \"Percentage of positive NAAT in the past 7 days\" is calculated by dividing the number of positive tests in the county (or other administrative level) during the last 7 days by the total number of tests conducted over the last 7 days. \"Percentage of positive NAAT in the past 7 days\" is considered to have a transmission level of Low (less than 5.00); Moderate (5.00-7.99); Substantial (8.00-9.99); and High (greater than or equal to 10.00).\n\nIf",
-            "title": "United States COVID-19 County Level of Community Transmission as Originally Posted - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15759,70 +15665,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8396-v7yb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8396-v7yb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8396-v7yb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8396-v7yb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8396-v7yb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8396-v7yb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8396-v7yb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8396-v7yb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8396-v7yb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "laboratory",
+                "ncird-corvd"
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
+                "name": "CDC"
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
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-11-03",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
-            "modified": "2024-05-24",
-            "references": [
-                "IQVIA Pharmacy and Physician Medical Office Claims"
-            ],
-            "keyword": [
-                "flu",
-                "influenza",
-                "iqvia",
-                "pharmacy vaccinations",
-                "physician medical office vaccinations",
-                "vaccine coverage"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vax View",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/83ng-twza",
             "description": "Weekly Cumulative Estimated Number of Influenza Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, United States\n\n- Archived data are here:  https://data.cdc.gov/resource/uxgd-cqqc\n\n- CDC is exploring use of data obtained from IQVIA\u00a7 (https://www.iqvia.com/) as a source of information on vaccinations administered in retail pharmacies (include chain, mass merchandise, food stores, and independent pharmacies) and physician medical offices.  \n \n- These projected pharmacy estimates include flu vaccinations that were billed for (i.e. claims) or paid by cash. Medical office projected estimates are claims-based only. \n \n- The sampled pharmacies and physician medical offices and the captured volume of transactions represent approximately 92% and 82% of influenza vaccines administered nationally, respectively. \n \n- Vaccinations administered in other settings such as workplaces and community settings are not included in these data. \n \n\n*National estimates for pharmacies and medical offices include vaccinations administered in 50 states and DC. National estimates for medical office vaccinations do not include doses where geographic information (i.e. which state the dose was administered in) was missing. Pharmacy data are through Friday of each week and medical office data are through Saturday of each week. Week ending dates for prior seasons are aligned with the current season\u2019s week ending dates. \n\n\u00a7 1) King, L. M., Bartoces, M., Fleming-Dutra, K. E., et. al, L. A. (2020). Changes in US outpatient antibiotic prescriptions from 2011\u20132016external icon. Clinical Infectious Diseases, 70(3), 370-377. 2) McLaughlin, J. M., Swerdlow, D. L., Khan, F., et. Al (2019). Disparities in uptake of 13-valent pneumococcal conjugate vaccine among older adults in the United Statesexternal icon. Human vaccines & immunotherapeutics, 15(4), 841-849.",
-            "title": "Weekly Cumulative Estimated Number of Influenza Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15830,67 +15737,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/83ng-twza/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/83ng-twza/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/83ng-twza/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/83ng-twza/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/83ng-twza/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/83ng-twza/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/83ng-twza/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/83ng-twza/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/83ng-twza/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/83ng-twza",
+            "issued": "2021-11-03",
+            "keyword": [
+                "flu",
+                "influenza",
+                "iqvia",
+                "pharmacy vaccinations",
+                "physician medical office vaccinations",
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
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
+            },
+            "references": [
+                "IQVIA Pharmacy and Physician Medical Office Claims"
+            ],
+            "spatial": "United States",
+            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Estimated Number of Influenza Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/847z-pxin",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-06-01",
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
                 "hasEmail": "mailto:nephtrackingsupport@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/847z-pxin",
             "description": "This dataset provides modeled predictions of ozone levels from the EPA's Downscaler model. Data are at the census tract level for 2001-2005. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\n\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\n\nBy using these data, you signify your agreement to comply with the following requirements:\n1. Use the data for statistical reporting and analysis only.\n2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals.\n3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov.\n4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.\n5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC.\n6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily Census Tract-Level Ozone Concentrations, 2011-2015",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15898,55 +15810,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/847z-pxin/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/847z-pxin/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/847z-pxin/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/847z-pxin/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/847z-pxin/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/847z-pxin/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/847z-pxin/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/847z-pxin/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/847z-pxin/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/847z-pxin",
+            "issued": "2020-06-01",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "ozone"
+            ],
+            "landingPage": "https://data.cdc.gov/d/847z-pxin",
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
+            "title": "Daily Census Tract-Level Ozone Concentrations, 2011-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/87ea-ip25",
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
-                "name": "data.cdc.gov"
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
@@ -15954,43 +15872,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/87ea-ip25",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/87ea-ip25",
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
+            "title": "NIOSH Health Hazard Evaluation Program Noise Measurement Database"
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
-                "e-cigarette",
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
-            "identifier": "https://data.cdc.gov/api/views/88eg-qzed",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. E-Cigarette Legislation \u2013 Preemption. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include information related to summary state preemption of more stringent or differing local laws on smokefree indoor air, youth access and licensure that are applicable to e-cigarettes.",
-            "title": "CDC STATE System E-Cigarette Legislation - Preemption Summary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15998,64 +15907,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/88eg-qzed/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/88eg-qzed/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/88eg-qzed/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/88eg-qzed/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/88eg-qzed/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/88eg-qzed/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/88eg-qzed/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/88eg-qzed/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/88eg-qzed/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/88eg-qzed",
+            "issued": "2023-07-18",
+            "keyword": [
+                "e-cigarette",
+                "legislation",
+                "osh",
+                "policy",
+                "preemption",
+                "state system",
+                "tobacco"
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
+            "title": "CDC STATE System E-Cigarette Legislation - Preemption Summary"
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
-                "mortality",
-                "ncird-corvd"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC-INFO",
                 "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDC/NCIRD/CORVD"
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
@@ -16063,78 +15973,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/89qs-mr7i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/89qs-mr7i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/89qs-mr7i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/89qs-mr7i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/89qs-mr7i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/89qs-mr7i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/89qs-mr7i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/89qs-mr7i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/89qs-mr7i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "mortality",
+                "ncird-corvd"
+            ],
+            "landingPage": "https://data.cdc.gov/d/89qs-mr7i",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC/NCIRD/CORVD"
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
-                "name": "National Center for Health Statistics"
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
@@ -16142,67 +16040,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/89yk-m38d/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/89yk-m38d/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/89yk-m38d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/89yk-m38d/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/89yk-m38d/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/89yk-m38d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/89yk-m38d/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/89yk-m38d/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/89yk-m38d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
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
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-03-28",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/data/vsus/vsus_1950_1.pdf",
+                "https://www.cdc.gov/nchs/data/misc/usvss.pdf",
+                "https://www.cdc.gov/nchs/data/vsus/nat67_1.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
+                "https://www.cdc.gov/nvsr/nvsr67/nvsr67_01.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13.pdf"
+            ],
+            "rights": "public",
+            "spatial": "50 states and District of Columbia",
+            "temporal": "1960/2018",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - Natality Measures for Females by Race and Hispanic Origin: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/index.html",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-01-10",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-04-17",
-            "keyword": [
-                "nis-acm",
-                "pregnancy",
-                "rsv vaccination"
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
-            "identifier": "https://data.cdc.gov/api/views/8ame-63pc",
             "description": "Monthly Nirsevimab Receipt and Intent Among Females Aged 18-49 Years Who Have a Baby <8 Months, Are Currently Pregnant, or Are Trying to Get Pregnant. \n\n\u2022 Using data from the National Immunization Survey-Adult COVID Module (NIS-ACM), monthly estimates of receipt and intent for baby\u2019s receipt of nirsevimab reported by females aged 18-49 years with infants under the age of 8 months, females aged 18-49 years who are currently pregnant, and females aged 18-49 years who are currently trying to get pregnant. \n\n\u2022 The NIS-ACM is an ongoing random-digit-dial cellular telephone survey of households with adults 18 years and older.",
-            "title": "Monthly Nirsevimab Receipt and Intent Among Females Aged 18-49 Years Who Have a Baby <8 Months, Are Currently Pregnant, or Are Trying to Get Pregnant, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16210,65 +16123,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8ame-63pc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8ame-63pc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8ame-63pc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8ame-63pc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8ame-63pc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8ame-63pc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8ame-63pc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8ame-63pc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8ame-63pc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/8ame-63pc",
+            "issued": "2024-01-10",
+            "keyword": [
+                "nis-acm",
+                "pregnancy",
+                "rsv vaccination"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/index.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2024-04-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
+            },
+            "spatial": "United States",
+            "temporal": "2023-2024",
             "theme": [
                 "Pregnancy & Vaccination"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Monthly Nirsevimab Receipt and Intent Among Females Aged 18-49 Years Who Have a Baby <8 Months, Are Currently Pregnant, or Are Trying to Get Pregnant, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/8bda-nhxv",
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
                 "fn": "Active Bacterial Core Surveillance",
                 "hasEmail": "mailto:abcs@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/8bda-nhxv",
             "description": "<p>ABCs is an ongoing surveillance program that began in 1997. <a href=\"https://www.cdc.gov/abcs/reports-findings/surv-reports.html\">ABCs reports</a> describe the ABCs case definition and the specific methodology used to calculate rates and estimated numbers in the United States for each bacterium by year.  The methods, <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">surveillance areas</a>, and <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">laboratory isolate collection areas</a> have changed over time.\n                Additionally, the way missing data are taken into account changed in 2010.  It went from distributing unknown values based on known values of cases by site to use of multiple imputation using a sequential regression imputation method.\n                Given these changes over time, trends should be interpreted with caution.\n<ul> <li> <a href=\"http://www.cdc.gov/abcs/methodology/index.html\">Methodology</a>\nFind details about surveillance population, case determination, surveillance evaluation, and more. </li>                    <li> <a href=\"http://www.cdc.gov/abcs/reports-findings/index.html\">Reports and Findings</a>\nGet official interpretations from reports and publications created from ABCs data. </li>\n  </ul>",
-            "title": "Active Bacterial Core surveillance (ABCs) Neisseria meningitidis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16276,66 +16190,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8bda-nhxv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8bda-nhxv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8bda-nhxv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8bda-nhxv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8bda-nhxv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8bda-nhxv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8bda-nhxv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8bda-nhxv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8bda-nhxv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8bda-nhxv",
+            "issued": "2021-06-23",
+            "keyword": [
+                "abcs",
+                "bactfacts"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8bda-nhxv",
+            "modified": "2024-09-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Active Bacterial Core surveillance (ABCs) Neisseria meningitidis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/8cyw-fici",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-            "identifier": "https://data.cdc.gov/api/views/8cyw-fici",
             "description": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16343,63 +16250,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8cyw-fici/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8cyw-fici/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8cyw-fici/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8cyw-fici/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8cyw-fici/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8cyw-fici/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8cyw-fici/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8cyw-fici/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8cyw-fici/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8cyw-fici",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "ehrlichia ewingii infection",
+                "ehrlichiosis and anaplasmosis",
+                "giardiasis",
+                "nedss",
+                "netss",
+                "nndss",
+                "undetermined ehrlichiosis/anaplasmosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8cyw-fici",
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
+            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis"
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -16407,73 +16317,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8dyx-9z99/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8dyx-9z99/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8dyx-9z99/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8dyx-9z99/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8dyx-9z99/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8dyx-9z99/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8dyx-9z99/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8dyx-9z99/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8dyx-9z99/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
-            "landingPage": "https://data.cdc.gov/d/8ezu-y38w",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/8ezu-y38w",
             "description": "NNDSS - TABLE 1Q.  Hepatitis B, perinatal infection to Hepatitis C (viral, acute), Probable - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n * Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 For acute Hepatitis C, only confirmed cases were verified.",
-            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C (viral, acute), Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16481,64 +16386,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8ezu-y38w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8ezu-y38w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8ezu-y38w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8ezu-y38w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8ezu-y38w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8ezu-y38w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8ezu-y38w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8ezu-y38w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8ezu-y38w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8ezu-y38w",
+            "issued": "2019-04-24",
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
+            "landingPage": "https://data.cdc.gov/d/8ezu-y38w",
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
+            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C (viral, acute), Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/respiratory-viruses/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-09-25",
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
-            "identifier": "https://data.cdc.gov/api/views/8fbp-accd",
             "description": "Weekly Influenza Vaccination Coverage, Pregnant Women 18-49 Years Old by Race and Ethnicity\n  \nWeekly influenza vaccination coverage estimates for pregnant women 18\u201349 years are based on electronic health record (EHR) data from the Vaccine Safety Datalink (VSD) (https://www.cdc.gov/vaccine-safety-systems/vsd/), a collaboration between CDC\u2019s Immunization Safety Office and multiple integrated health care organizations.",
-            "title": "Weekly Influenza Vaccination Coverage Among Pregnant Women 18-49 Years, by Race and Ethnicity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16546,61 +16456,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8fbp-accd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8fbp-accd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8fbp-accd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8fbp-accd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8fbp-accd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8fbp-accd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8fbp-accd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8fbp-accd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8fbp-accd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/8fbp-accd",
+            "issued": "2024-09-25",
+            "keyword": [
+                "flu vaccination",
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "nis-flu",
+                "vsd"
+            ],
+            "landingPage": "https://www.cdc.gov/respiratory-viruses/index.html",
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
+            "spatial": "United States",
+            "temporal": "2024-2025",
             "theme": [
                 "Pregnancy & Vaccination"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Influenza Vaccination Coverage Among Pregnant Women 18-49 Years, by Race and Ethnicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/8ggw-jwph",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Allergy and Clinical Immunology Branch, Health Effects Laboratory Division",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/8ggw-jwph",
             "description": "The fundamental goal of this study was to develop an in vivo model of the exposome that could be used to evaluate exposure-induced alterations in local and systemic immune markers as a function of various exposomal factors. Accordingly, the model was designed to mimic an occupationally-relevant scenario in which inhalation of welding fumes (WF) constituted the primary occupational/environmental exposure of interest. Immune endpoints were assessed at three different time points representative of different stages in the exposure/response timeline (before WF exposure, directly after, and following a 12 wk recovery period). Moreover, the potential impact of genetic variation and lifestyle factors on the immune response to WF exposure and subsequent recovery was addressed by incorporating two different rat strains (Sprague-Dawley [SD] and Brown Norway [BN]) and two variations in diet (regular and high fat) into the model.\n\nOne of the primary objectives of this study was to determine whether consumption of a HF diet is associated with increased immunological responsivity following exposure to a common respiratory toxicant. The study was also executed with the goal of identifying which experimental factor (genetics/strain, diet, occupational exposure) is most influential in the modulation of local and systemic markers of immune status following WF exposure, and subsequently, the efficacy of inflammation resolution. The information obtained from these analyses will help elucidate which exposomic determinants may be particularly relevant in the context of immunotoxicity, and accordingly, warrant special attention in future investigations. The results will also contribute to the development of other in vivo exposome models and direct future efforts related to the exposome and its impact on human health.",
-            "title": "Examination of the exposome in an animal model: the impact of high fat diet and rat strain on local and systemic immune markers following occupational welding fume exposure",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16608,39 +16526,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8ggw-jwph",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/8ggw-jwph",
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
+            "title": "Examination of the exposome in an animal model: the impact of high fat diet and rat strain on local and systemic immune markers following occupational welding fume exposure"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-06-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "keyword": [
-                "breastfeeding",
-                "nutrition physical activity and weight status",
-                "policy"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Division of Nutrition, Physical Activity, and Obesity",
                 "hasEmail": "mailto:dnpaoinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/8hus-y5nc",
             "description": "Community-Based Survey of Supports for Healthy Eating and Active Living (CBS HEAL) is a CDC survey of a nationally representative sample of U.S. municipalities to better understand existing community-level policies and practices that support healthy eating and active living. The survey collects information about policies such as nutrition standards, incentives for healthy food retail, bike/pedestrian-friendly design, and Complete Streets. About 2,000 municipalities respond to the survey. Participating municipalities receive a report that allows them to compare their policies and practices with other municipalities of similar geography, population size, and urban status.\n\nThe CBS HEAL survey was first administered in 2014 and was administered again in 2021. Data is provided in multiple formats for download including as a SAS file. A methods report and a SAS program for formatting the data are also provided.",
-            "title": "National Community Based Survey of Supports for Healthy Eating and Active Living  (CBS HEAL)",
-            "programCode": [
-                "009:029"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16648,69 +16561,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8hus-y5nc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8hus-y5nc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8hus-y5nc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8hus-y5nc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8hus-y5nc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8hus-y5nc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8hus-y5nc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8hus-y5nc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8hus-y5nc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8hus-y5nc",
+            "issued": "2023-06-28",
+            "keyword": [
+                "breastfeeding",
+                "nutrition physical activity and weight status",
+                "policy"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-08-25",
+            "programCode": [
+                "009:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Nutrition, Physical Activity, and Obesity"
-            ]
+            ],
+            "title": "National Community Based Survey of Supports for Healthy Eating and Active Living  (CBS HEAL)"
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
-                "https://www.cdc.gov/breastfeeding/data/nis_data/index.htm"
-            ],
-            "keyword": [
-                "breastfed",
-                "breastfeeding",
-                "child",
-                "dnpao",
-                "infants",
-                "national immunization survey",
-                "nis",
-                "nutrition"
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
-            "identifier": "https://data.cdc.gov/api/views/8hxn-cvik",
+            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-National-I/8hxn-cvik",
             "description": "This dataset includes breastfeeding data from the National Immunization Survey (NIS). This data is used for DNPAO's Data, Trends, and Maps database, which provides national and state specific data on obesity, nutrition, physical activity, and breastfeeding. For more information about breastfeeding and NIS visit https://www.cdc.gov/breastfeeding/data/nis_data/index.htm.",
-            "title": "Nutrition, Physical Activity, and Obesity - National Immunization Survey (Breastfeeding)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16718,68 +16624,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8hxn-cvik/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8hxn-cvik/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8hxn-cvik/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8hxn-cvik/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8hxn-cvik/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8hxn-cvik/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8hxn-cvik/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8hxn-cvik/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8hxn-cvik/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-National-I/8hxn-cvik",
+            "identifier": "https://data.cdc.gov/api/views/8hxn-cvik",
+            "issued": "2025-01-30",
+            "keyword": [
+                "breastfed",
+                "breastfeeding",
+                "child",
+                "dnpao",
+                "infants",
+                "national immunization survey",
+                "nis",
+                "nutrition"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
+            "modified": "2025-02-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/breastfeeding/data/nis_data/index.htm"
+            ],
             "theme": [
                 "Nutrition, Physical Activity, and Obesity"
-            ]
+            ],
+            "title": "Nutrition, Physical Activity, and Obesity - National Immunization Survey (Breastfeeding)"
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
-                "name": "National Center for Health Statistics"
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
@@ -16787,62 +16694,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8hzs-zshh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8hzs-zshh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8hzs-zshh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8hzs-zshh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8hzs-zshh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8hzs-zshh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8hzs-zshh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8hzs-zshh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8hzs-zshh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-            "landingPage": "https://data.cdc.gov/d/8i5t-42wz",
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
-            "identifier": "https://data.cdc.gov/api/views/8i5t-42wz",
             "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 8 - Denver",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16850,59 +16764,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8i5t-42wz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8i5t-42wz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8i5t-42wz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8i5t-42wz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8i5t-42wz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8i5t-42wz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8i5t-42wz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8i5t-42wz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8i5t-42wz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8i5t-42wz",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8i5t-42wz",
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
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 8 - Denver"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/8ihh-n7ic",
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
-            "identifier": "https://data.cdc.gov/api/views/8ihh-n7ic",
             "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 6 - Dallas",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16910,60 +16824,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8ihh-n7ic/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8ihh-n7ic/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8ihh-n7ic/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8ihh-n7ic/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8ihh-n7ic/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8ihh-n7ic/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8ihh-n7ic/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8ihh-n7ic/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8ihh-n7ic/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8ihh-n7ic",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8ihh-n7ic",
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
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 6 - Dallas"
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
-            "identifier": "https://data.cdc.gov/api/views/8jp2-ecz7",
             "description": "\u2022 Weekly COVID-19 vaccination coverage estimates among children 6 months to 17 years is assessed through the National Immunization Survey (https://www.cdc.gov/vaccines/imz-managers/nis/about.html). \n\n\u2022 Weekly estimates of COVID-19 vaccination coverage among children through December 31, 2023, were calculated using data from the National Immunization Survey-Child COVID Module (NIS-CCM) (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-ccm). Beginning January 2, 2024, the NIS-CCM was discontinued, and questions regarding receipt of COVID-19 vaccination among children were added to the NIS-Flu (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-cim). \n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19.",
-            "title": "Weekly Cumulative Percentage of Children Ages 6 Months -17 Years who are up to date with the updated 2023-24 COVID-19 Vaccine, by Jurisdiction",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16971,45 +16885,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8jp2-ecz7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8jp2-ecz7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8jp2-ecz7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8jp2-ecz7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8jp2-ecz7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8jp2-ecz7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8jp2-ecz7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8jp2-ecz7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8jp2-ecz7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/8jp2-ecz7",
+            "issued": "2023-12-11",
+            "keyword": [
+                "covid-19 vaccination",
+                "nis"
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
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2023-2024",
             "theme": [
                 "Child Vaccinations"
-            ]
+            ],
+            "title": "Weekly Cumulative Percentage of Children Ages 6 Months -17 Years who are up to date with the updated 2023-24 COVID-19 Vaccine, by Jurisdiction"
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
+            "describedBy": "All registered births occurring to residents of the United States for a given year",
+            "description": "This dataset includes all births for a given year and includes all items released in the public-use file. Additional information in this file includes state and county of residence (cities with a population of 100,000 or greater) and exact date of birth (which includes day of month, month, and year).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This dataset includes all births for a given year and includes all items released in the public-use file. Additional information in this file includes state and county of residence (cities with a population of 100,000 or greater) and exact date of birth (which includes day of month, month, and year).",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "NCHS - All-County Natality File with Exact Date of Birth"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/8kbq-i8ii",
+            "isPartOf": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "issued": "2022-06-06",
-            "@type": "dcat:Dataset",
-            "temporal": "1989/2020",
-            "modified": "2023-04-14",
             "keyword": [
                 "births",
                 "county",
@@ -17023,48 +16967,48 @@
                 "sdoh-use-of-health-care",
                 "united states"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:births@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/rdc/index.htm",
+            "modified": "2023-04-14",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/8kbq-i8ii",
-            "description": "This dataset includes all births for a given year and includes all items released in the public-use file. Additional information in this file includes state and county of residence (cities with a population of 100,000 or greater) and exact date of birth (which includes day of month, month, and year).",
-            "title": "NCHS - All-County Natality File with Exact Date of Birth",
-            "isPartOf": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "description": "This dataset includes all births for a given year and includes all items released in the public-use file. Additional information in this file includes state and county of residence (cities with a population of 100,000 or greater) and exact date of birth (which includes day of month, month, and year).",
-                    "@type": "dcat:Distribution",
-                    "title": "NCHS - All-County Natality File with Exact Date of Birth"
-                }
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information. Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement. If approved, data access would occur at a NCHS or Federal Statistical Research Data Center. For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "50 states and District of Columbia, all counties and cities with a population of 100,000 or greater",
-            "describedBy": "All registered births occurring to residents of the United States for a given year",
+            "temporal": "1989/2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - All-County Natality File with Exact Date of Birth"
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
@@ -17077,73 +17021,36 @@
                 "research-data-center",
                 "telemedicine"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/covid19/namcs.htm",
+            "modified": "2024-03-06",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
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
-            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-15",
-            "references": [
-                "https://www.cdc.gov/nccdphp/dnpao/index.html"
-            ],
-            "keyword": [
-                "acs",
-                "american community survey",
-                "bike",
-                "dnpao",
-                "physical activity",
-                "walk",
-                "work"
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
-            "identifier": "https://data.cdc.gov/api/views/8mrp-rmkw",
+            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-American-C/8mrp-rmkw",
             "description": "This dataset includes select data from the U.S. Census Bureau's American Community Survey (ACS) on the percent of adults who bike or walk to work. This data is used for DNPAO's Data, Trends, and Maps database, which provides national and state specific data on obesity, nutrition, physical activity, and breastfeeding. For more information about ACS visit https://www.census.gov/programs-surveys/acs/.",
-            "title": "Nutrition, Physical Activity, and Obesity - American Community Survey",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17151,65 +17058,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8mrp-rmkw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8mrp-rmkw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8mrp-rmkw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8mrp-rmkw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8mrp-rmkw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8mrp-rmkw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8mrp-rmkw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8mrp-rmkw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8mrp-rmkw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-American-C/8mrp-rmkw",
+            "identifier": "https://data.cdc.gov/api/views/8mrp-rmkw",
+            "issued": "2023-07-18",
+            "keyword": [
+                "acs",
+                "american community survey",
+                "bike",
+                "dnpao",
+                "physical activity",
+                "walk",
+                "work"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
+            "modified": "2025-02-03",
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
                 "Nutrition, Physical Activity, and Obesity"
-            ]
+            ],
+            "title": "Nutrition, Physical Activity, and Obesity - American Community Survey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/8n2k-mkiw",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "babesiosis",
-                "campylobacteriosis",
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
-            "identifier": "https://data.cdc.gov/api/views/8n2k-mkiw",
             "description": "NNDSS - Table II. Babesiosis to Campylobacteriosis - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\n\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Babesiosis to Campylobacteriosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17217,62 +17126,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8n2k-mkiw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8n2k-mkiw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8n2k-mkiw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8n2k-mkiw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8n2k-mkiw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8n2k-mkiw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8n2k-mkiw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8n2k-mkiw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8n2k-mkiw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8n2k-mkiw",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "babesiosis",
+                "campylobacteriosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8n2k-mkiw",
+            "modified": "2019-01-03",
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
-            "landingPage": "https://www.cdc.gov/ncezid/dfwed/beam-dashboard.html",
+            "accrualPeriodicity": "Annually",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
-            "keyword": [
-                "beam",
-                "beam dashboard",
-                "campylobacteriosis",
-                "escherichia",
-                "salmonella"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SIMSO",
                 "hasEmail": "mailto:simso@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDC"
-            },
-            "identifier": "https://data.cdc.gov/api/views/8na9-qgz7",
             "description": "The BEAM (Bacteria, Enterics, Amoeba, and Mycotics) Dashboard is an interactive tool to access and visualize data from the System for Enteric Disease Response, Investigation, and Coordination (SEDRIC). The BEAM Dashboard provides timely data on pathogen trends and serotype details to inform work to prevent illnesses from food and animal contact.",
-            "title": "BEAM Dashboard - Serotypes of concern: Burden and Trajectory",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17280,58 +17192,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8na9-qgz7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8na9-qgz7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8na9-qgz7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8na9-qgz7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8na9-qgz7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8na9-qgz7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8na9-qgz7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8na9-qgz7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8na9-qgz7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/8na9-qgz7",
+            "issued": "2025-01-21",
+            "keyword": [
+                "beam",
+                "beam dashboard",
+                "campylobacteriosis",
+                "escherichia",
+                "salmonella"
+            ],
+            "landingPage": "https://www.cdc.gov/ncezid/dfwed/beam-dashboard.html",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annually",
+            "modified": "2025-01-21",
+            "programCode": [
+                "009:028"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
+            },
+            "spatial": "US",
             "theme": [
                 "Foodborne, Waterborne, and Related Diseases"
-            ]
+            ],
+            "title": "BEAM Dashboard - Serotypes of concern: Burden and Trajectory"
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
-                "name": "NCIRD"
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
@@ -17339,67 +17258,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8nyy-xsq7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8nyy-xsq7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8nyy-xsq7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8nyy-xsq7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8nyy-xsq7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8nyy-xsq7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8nyy-xsq7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8nyy-xsq7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8nyy-xsq7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "NCIRD"
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
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/8pt5-q6wp",
-            "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, gender, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions,",
-            "title": "Indicators of Anxiety or Depression Based on Reported Frequency of Symptoms During Last 7 Days",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, sex, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions,",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17407,72 +17320,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8pt5-q6wp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8pt5-q6wp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8pt5-q6wp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8pt5-q6wp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8pt5-q6wp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8pt5-q6wp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8pt5-q6wp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8pt5-q6wp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8pt5-q6wp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/8pt5-q6wp",
+            "issued": "2020-05-20",
+            "keyword": [
+                "depression",
+                "anxiety",
+                "covid-19"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/mental-health.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P2W",
+            "modified": "2025-02-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
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
-            "landingPage": "https://data.cdc.gov/d/8rkx-vimh",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-01-08",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "2014",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/8rkx-vimh",
             "description": "NNDSS - Table II. Mumps to Rabies, animal - 2014.In this Table, all conditions with a 5-year average annual national total of more than or equals 1,000 cases but less than or equals 10,000 cases will be displayed (\ufffd\ufffd\ufffd 1,000 and \ufffd\ufffd_ 10,000). The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Case counts for reporting years 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
-            "title": "NNDSS - Table II. Mumps to Rabies, animal",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17480,66 +17387,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8rkx-vimh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8rkx-vimh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8rkx-vimh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8rkx-vimh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8rkx-vimh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8rkx-vimh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8rkx-vimh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8rkx-vimh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8rkx-vimh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8rkx-vimh",
+            "issued": "2015-01-08",
+            "keyword": [
+                "2014",
+                "mmwr",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "pertussis",
+                "rabies animal",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8rkx-vimh",
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
+            "title": "NNDSS - Table II. Mumps to Rabies, animal"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/8rsa-pnhx",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/8rsa-pnhx",
             "description": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Reporting jurisdictions were informed CDC could receive data for this condition in August 2019. Please note there will be a delay in reporting of case notifications for this condition to CDC.",
-            "title": "NNDSS - TABLE 1F. Brucellosis to Candida auris, clinical",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17547,42 +17454,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8rsa-pnhx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8rsa-pnhx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8rsa-pnhx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8rsa-pnhx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8rsa-pnhx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8rsa-pnhx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8rsa-pnhx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8rsa-pnhx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8rsa-pnhx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8rsa-pnhx",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "brucellosis",
+                "campylobacteriosis",
+                "candida auris",
+                "clinical",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8rsa-pnhx",
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
+            "title": "NNDSS - TABLE 1F. Brucellosis to Candida auris, clinical"
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
@@ -17596,64 +17539,35 @@
                 "reason for visit",
                 "research-data-center"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/ahcd/about_ahcd.htm",
+            "modified": "2024-02-21",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
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
-            "landingPage": "https://data.cdc.gov/d/8v6a-z6zq",
             "bureauCode": [
                 "009:15"
             ],
-            "issued": "2022-01-19",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-20",
-            "keyword": [
-                "american rescue plan",
-                "covid-19"
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
-            "identifier": "https://data.cdc.gov/api/views/8v6a-z6zq",
             "description": "The U.S. Department of Health and Human Services (HHS) via the Health Resources and Services Administration (HRSA) is releasing American Rescue Plan payments to providers and suppliers who have served rural Medicaid, Children's Health Insurance Program (CHIP), and Medicare beneficiaries from January 1, 2019 through September 30, 2020. The dataset will be updated as additional payments are released. Data does not reflect recipients\u2019 attestation status, returned payments, or unclaimed funds.",
-            "title": "American Rescue Plan (ARP) Rural Payments",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17661,57 +17575,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8v6a-z6zq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8v6a-z6zq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8v6a-z6zq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8v6a-z6zq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8v6a-z6zq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8v6a-z6zq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8v6a-z6zq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8v6a-z6zq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8v6a-z6zq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/8v6a-z6zq",
+            "issued": "2022-01-19",
+            "keyword": [
+                "american rescue plan",
+                "covid-19"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8v6a-z6zq",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-06-20",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "HRSA"
+            },
+            "spatial": "U.S.",
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "American Rescue Plan (ARP) Rural Payments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/8ve6-tiah",
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
-                "name": "data.cdc.gov"
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
@@ -17719,34 +17637,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8ve6-tiah",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/8ve6-tiah",
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
+            "title": "Persistence of SARS-CoV-2 on N95 filtering facepiece respirators: implications for reuse"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/8vj7-uiam",
-            "issued": "2024-12-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-05",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chemical and Biological Monitoring Branch (CBMB), Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/8vj7-uiam",
             "description": "Laboratory-generated environments are substantial parts of the work involved in developing and validating methods for sampling volatile organic compounds (VOCs) in workplace atmospheres. We assessed the variability of samples produced by our dynamic atmosphere generation system designed for VOC generation and sampling. The characterization of bias and variability was conducted across various atmospheres containing pure n-heptane as well as mixtures of VOCs, which were collected using coconut shell charcoal tubes. The analysis of VOCs from these charcoal tubes was evaluated to reveal the variability from multiple sources: the generation of the atmosphere, the sampling process, and the analytical procedures. This research aimed to quantify the extent of variability from these sources and to estimate the sampling variability associated with our dynamic generation system. Our findings indicated that sampling variability ranged from 2% for pure n-heptane to 12% for a component within a ten-VOC mixture. Notably, sample variability increased with lower concentration levels and in mixtures compared to single-component atmospheres. This study provides a foundational reference for future experiments focused on atmosphere sampling performance at lower concentrations and in mixed VOC environments.\n\nThe introduction above was rephrased by ChatGPT-4 (with training data up to April 2023) from the original work of: Doepke et al. (2024) Journal of Occupational and Environmental Hygiene, doi:10.1080/15459624.2024.2423749.",
-            "title": "Characterizing dynamic atmosphere generation system performance for analytical method development",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17754,43 +17672,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8vj7-uiam",
+            "issued": "2024-12-05",
+            "landingPage": "https://data.cdc.gov/d/8vj7-uiam",
+            "modified": "2024-12-05",
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
+            "title": "Characterizing dynamic atmosphere generation system performance for analytical method development"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/adultvaxview/index.html and https://www.cdc.gov/flu/fluvaxview/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-05-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-12",
-            "keyword": [
-                "immunization",
-                "influenza",
-                "nursing home vaccination",
-                "pneumococcal",
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
-            "identifier": "https://data.cdc.gov/api/views/8w4j-reb4",
             "description": "Vaccination Coverage among Nursing Home Residents\n\n\u2022 Data on influenza and pneumococcal vaccination coverage from the Long-Term Care Minimum Data Set (MDS) from the Centers for Medicare & Medicaid Services (CMS) at the national, regional, and state levels by sociodemographic characteristics.\n\n\u2022 Additional information available at https://www.cdc.gov/vaccines/imz-managers/coverage/adultvaxview/index.html and https://www.cdc.gov/flu/fluvaxview/index.htm",
-            "title": "Vaccination Coverage among Nursing Home Residents",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17798,64 +17707,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8w4j-reb4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8w4j-reb4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8w4j-reb4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8w4j-reb4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8w4j-reb4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8w4j-reb4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8w4j-reb4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8w4j-reb4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8w4j-reb4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8w4j-reb4",
+            "issued": "2021-05-13",
+            "keyword": [
+                "immunization",
+                "influenza",
+                "nursing home vaccination",
+                "pneumococcal",
+                "vaccination",
+                "vaccination coverage",
+                "vaxviews"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/adultvaxview/index.html and https://www.cdc.gov/flu/fluvaxview/index.htm",
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
+            "title": "Vaccination Coverage among Nursing Home Residents"
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
-            "modified": "2023-04-18",
-            "keyword": [
-                "health statistics",
-                "nchs",
-                "nhanes",
-                "nutrition",
-                "surveillance",
-                "survey"
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
-            "identifier": "https://data.cdc.gov/api/views/8wmh-yzz9",
             "description": "These data represent mean intake, on a given day, estimates of nutrients from foods and beverages from the National Health and Nutrition Examination Survey (NHANES).",
-            "title": "NHANES Select Mean Dietary Intake Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17863,74 +17773,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8wmh-yzz9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8wmh-yzz9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8wmh-yzz9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8wmh-yzz9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8wmh-yzz9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8wmh-yzz9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8wmh-yzz9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8wmh-yzz9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8wmh-yzz9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/8wmh-yzz9",
+            "issued": "2023-03-02",
+            "keyword": [
+                "nchs",
+                "nhanes",
+                "health statistics",
+                "surveillance",
+                "survey",
+                "nutrition"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2025-02-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "U.S.",
+            "temporal": "1999/2018",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NHANES Select Mean Dietary Intake Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/8xkx-amqh",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-12-09",
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
-                "name": "CDC"
-            },
-            "identifier": "https://data.cdc.gov/api/views/8xkx-amqh",
             "description": "Overall US COVID-19 Vaccine administration and vaccine equity data at county level. Data represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.\u00a0",
-            "title": "COVID-19 Vaccinations in the United States,County",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17938,67 +17844,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8xkx-amqh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8xkx-amqh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8xkx-amqh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8xkx-amqh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8xkx-amqh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8xkx-amqh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8xkx-amqh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8xkx-amqh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8xkx-amqh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1D",
-            "theme": [
-                "Vaccinations"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/rands/telemedicine.htm",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2020-09-14",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-06-09/2021-06-30",
-            "modified": "2023-04-24",
+            "identifier": "https://data.cdc.gov/api/views/8xkx-amqh",
+            "issued": "2022-12-09",
             "keyword": [
+                "administration",
+                "age",
+                "coronavirus",
                 "covid-19",
-                "rands",
-                "sdoh-access-to-health-care",
-                "sdoh-higher-education",
-                "sdoh-high-school",
-                "sdoh-use-of-health-care"
+                "immunization",
+                "izdl",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8xkx-amqh",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-05-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
+            },
+            "references": [
+                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
+            ],
+            "spatial": "US",
+            "temporal": "2020-12-13/2023-05-12",
+            "theme": [
+                "Vaccinations"
+            ],
+            "title": "COVID-19 Vaccinations in the United States,County"
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
-            "identifier": "https://data.cdc.gov/api/views/8xy9-ubqz",
             "description": "The Research and Development Survey (RANDS) is a platform designed for conducting survey question evaluation and statistical research. RANDS is an ongoing series of surveys from probability-sampled commercial survey panels used for methodological research at the National Center for Health Statistics (NCHS). RANDS estimates are generated using an experimental approach that differs from the survey design approaches generally used by NCHS, including possible biases from different response patterns and sampling frames as well as increased variability from lower sample sizes. Use of the RANDS platform allows NCHS to produce more timely data than would be possible using traditional data collection methods. RANDS is not designed to replace NCHS\u2019 higher quality, core data collections. Below are experimental estimates of telemedicine access and use for three rounds of RANDS during COVID-19. Data collection for the three rounds of RANDS during COVID-19 occurred between June 9, 2020 and July 6, 2020, August 3, 2020 and August 20, 2020, and May 17, 2021 and June 30, 2021. Information needed to interpret these estimates can be found in the Technical Notes. RANDS during COVID-19 included questions about whether providers offered telemedicine (including video and telephone appointments) in the last 2 months\u2014both during and before the pandemic\u2014and about the use of telemedicine in the last 2 months during the pandemic. As a result of the coronavirus pandemic, many local and state governments discouraged people from leaving their homes for nonessential reasons. Although health care is considered an essential activity, telemedicine offers an opportunity for care without the potential or perceived risks of leaving the home. The National Health Interview Survey, conducted by NCHS, added telemedicine questions to its sample adult questionnaire in July 2020.  The Household Pulse Survey (https://www.cdc.gov/nchs/covid19/pulse/telemedicine-use.htm), an online survey conducted in response to the COVID-19 pandemic by the Census Bureau in partnership with other federal agencies including NCHS, also reports estimates of telemedicine use during the pandemic (beginning in Phase 3.1, which started on April 14, 2021). The Household Pulse Survey reports telemedicine use in the last 4 weeks among adults and among households with at least one child under age 18 years. The experimental estimates on this page are derived from RANDS during COVID-19 and show the percentage of U.S. adults who have a usual place of care and a provider that offered telemedicine in the past 2 months, who used telemedicine in the past 2 months, or who have a usual place of care and a provider that offered telemedicine prior to the coronavirus pandemic. Technical Notes: https://www.cdc.gov/nchs/covid19/rands/telemedicine.htm#limitations",
-            "title": "Access and Use of Telemedicine During COVID-19",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18006,70 +17916,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8xy9-ubqz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8xy9-ubqz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8xy9-ubqz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8xy9-ubqz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8xy9-ubqz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8xy9-ubqz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8xy9-ubqz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8xy9-ubqz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8xy9-ubqz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/8xy9-ubqz",
+            "issued": "2020-09-14",
+            "keyword": [
+                "covid-19",
+                "rands",
+                "sdoh-access-to-health-care",
+                "sdoh-higher-education",
+                "sdoh-high-school",
+                "sdoh-use-of-health-care"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/rands/telemedicine.htm",
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
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "US",
+            "temporal": "2020-06-09/2021-06-30",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Access and Use of Telemedicine During COVID-19"
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
-            "modified": "2025-01-31",
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -18077,67 +17987,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8yup-c35n/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8yup-c35n/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8yup-c35n/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8yup-c35n/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8yup-c35n/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8yup-c35n/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8yup-c35n/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8yup-c35n/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8yup-c35n/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
-            "landingPage": "https://data.cdc.gov/d/8zak-ewtm",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-08-02",
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
-            "identifier": "https://data.cdc.gov/api/views/8zak-ewtm",
             "description": "Percentages are weighted to population characteristics. Data are not available if it did not meet BRFSS stability requirements.For more information on these requirements, as well as risk factors and calculated variables, see the Technical Documents and Survey Data for a specific year - http://www.cdc.gov/brfss/annual_data/annual_data.htm.Recommended citation: Centers for Disease Control and Prevention (CDC). Behavioral Risk Factor Surveillance System. Atlanta, Georgia: U.S. Department of Health and Human Services, Centers for Disease Control and Prevention, [appropriate year].",
-            "title": "BRFSS Prevalence and Trends Data: Tobacco Use - Four Level Smoking Data for 1995-2010",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18145,49 +18057,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8zak-ewtm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8zak-ewtm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8zak-ewtm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8zak-ewtm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8zak-ewtm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8zak-ewtm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8zak-ewtm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8zak-ewtm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8zak-ewtm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8zak-ewtm",
+            "issued": "2013-08-02",
+            "keyword": [
+                "brfss",
+                "current smokers",
+                "former smoker",
+                "non-smoker"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8zak-ewtm",
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
+            "title": "BRFSS Prevalence and Trends Data: Tobacco Use - Four Level Smoking Data for 1995-2010"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/8zbb-qqwc",
-            "issued": "2024-07-24",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-24",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/8zbb-qqwc",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18195,63 +18116,50 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8zbb-qqwc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8zbb-qqwc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8zbb-qqwc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8zbb-qqwc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8zbb-qqwc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8zbb-qqwc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8zbb-qqwc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8zbb-qqwc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8zbb-qqwc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/8zbb-qqwc",
+            "issued": "2024-07-24",
+            "landingPage": "https://data.cdc.gov/d/8zbb-qqwc",
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
-            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-14",
-            "references": [
-                "https://chronicdata.cdc.gov/d/sfei-pddr"
-            ],
-            "keyword": [
-                "e-cigarette",
-                "legislation",
-                "osh",
-                "policy",
-                "state system",
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
-            "identifier": "https://data.cdc.gov/api/views/8zea-kwnt",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Youth-Acc/8zea-kwnt",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. E-Cigarette Legislation\u2014Youth Access. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies.  Data are reported on a quarterly basis. Data include information related to restrictions, enforcement and penalties associated with the sale of e-cigarettes to youth through retail sales and vending machines.",
-            "title": "CDC STATE System E-Cigarette Legislation - Youth Access",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18259,50 +18167,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8zea-kwnt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8zea-kwnt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8zea-kwnt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/8zea-kwnt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8zea-kwnt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8zea-kwnt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/8zea-kwnt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/8zea-kwnt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/8zea-kwnt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Youth-Acc/8zea-kwnt",
+            "identifier": "https://data.cdc.gov/api/views/8zea-kwnt",
+            "issued": "2023-07-18",
+            "keyword": [
+                "e-cigarette",
+                "legislation",
+                "osh",
+                "policy",
+                "state system",
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
+            "references": [
+                "https://chronicdata.cdc.gov/d/sfei-pddr"
+            ],
             "theme": [
                 "Legislation"
-            ]
+            ],
+            "title": "CDC STATE System E-Cigarette Legislation - Youth Access"
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
@@ -18331,72 +18267,46 @@
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
                 "name": "National Center for Health Statistics"
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
-            "landingPage": "https://www.cdc.gov/art/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
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
-            "identifier": "https://data.cdc.gov/api/views/92ri-yjps",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Se/92ri-yjps",
             "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Services and Profiles dataset provides an overview of clinic services, the clinic\u2019s contact information, location, the medical director\u2019s name, and summary statistics.",
-            "title": "2020 Final Assisted Reproductive Technology (ART) Services and Profiles",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18404,69 +18314,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/92ri-yjps/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/92ri-yjps/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/92ri-yjps/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/92ri-yjps/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/92ri-yjps/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/92ri-yjps/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/92ri-yjps/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/92ri-yjps/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/92ri-yjps/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Se/92ri-yjps",
+            "identifier": "https://data.cdc.gov/api/views/92ri-yjps",
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
+            "title": "2020 Final Assisted Reproductive Technology (ART) Services and Profiles"
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
-                "name": "data.cdc.gov"
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
@@ -18474,61 +18379,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/93k9-hy54/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/93k9-hy54/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/93k9-hy54/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/93k9-hy54/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/93k9-hy54/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/93k9-hy54/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/93k9-hy54/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/93k9-hy54/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/93k9-hy54/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Lyme disease to Meningococcal"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/respvaxview/about/index.html",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2024-2025",
-            "modified": "2025-01-31",
-            "keyword": [
-                "covid-19 vaccination",
-                "flu vaccination",
-                "rsv vaccination"
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
-            "identifier": "https://data.cdc.gov/api/views/94wp-9pid",
             "description": "\u2022 CDC is providing information on COVID-19, flu, and RSV vaccination concerns, issues, and motivators to supplement weekly vaccination data. These monthly data represent trends in vaccination concerns, issues, and motivators, by demographics and other characteristics. \n \n\u2022 The data start in August 2024.",
-            "title": "Vaccination Concerns, Issues, and Motivators | RespVaxView | Data | Centers for Disease Control and Prevention (cdc.gov)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18536,82 +18449,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/94wp-9pid/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/94wp-9pid/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/94wp-9pid/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/94wp-9pid/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/94wp-9pid/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/94wp-9pid/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/94wp-9pid/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/94wp-9pid/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/94wp-9pid/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/94wp-9pid",
+            "issued": "2024-11-01",
+            "keyword": [
+                "covid-19 vaccination",
+                "flu vaccination",
+                "rsv vaccination"
+            ],
+            "landingPage": "https://www.cdc.gov/respvaxview/about/index.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
+            },
+            "spatial": "United States- National",
+            "temporal": "2024-2025",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Vaccination Concerns, Issues, and Motivators | RespVaxView | Data | Centers for Disease Control and Prevention (cdc.gov)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-04-28",
-            "@type": "dcat:Dataset",
-            "temporal": "1999/2019",
-            "modified": "2022-04-28",
-            "keyword": [
-                "african americans",
-                "age",
-                "alaskan natives",
-                "american natives",
-                "analgesics",
-                "asian continental ancestry group",
-                "continental population groups",
-                "death",
-                "drug overdose",
-                "european continental ancestry group",
-                "health us",
-                "heroin",
-                "hispanic americans",
-                "injury",
-                "methadone",
-                "mortality",
-                "opioid",
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
-            "identifier": "https://data.cdc.gov/api/views/95ax-ymtc",
             "description": "Data on drug overdose death rates, by drug type and selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National Vital Statistics System, numerator data from annual public-use Mortality Files; denominator data from U.S. Census Bureau national population estimates; and Murphy SL, Xu JQ, Kochanek KD, Arias E, Tejada-Vera B. Deaths: Final data for 2018. National Vital Statistics Reports; vol 69 no 13. Hyattsville, MD: National Center for Health Statistics.2021. Available from: https://www.cdc.gov/nchs/products/nvsr.htm. For more information on the National Vital Statistics System, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
-            "title": "Drug overdose death rates, by drug type, sex, age, race, and Hispanic origin: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18619,62 +18517,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/95ax-ymtc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/95ax-ymtc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/95ax-ymtc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/95ax-ymtc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/95ax-ymtc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/95ax-ymtc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/95ax-ymtc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/95ax-ymtc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/95ax-ymtc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/95ax-ymtc",
+            "issued": "2022-04-28",
+            "keyword": [
+                "african americans",
+                "age",
+                "alaskan natives",
+                "american natives",
+                "analgesics",
+                "asian continental ancestry group",
+                "continental population groups",
+                "death",
+                "drug overdose",
+                "european continental ancestry group",
+                "health us",
+                "heroin",
+                "hispanic americans",
+                "injury",
+                "methadone",
+                "mortality",
+                "opioid",
+                "sex"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-04-28",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "1999/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Drug overdose death rates, by drug type, sex, age, race, and Hispanic origin: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/95m5-agj4",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/95m5-agj4",
             "description": "ABCs is an ongoing surveillance program that began in 1997. <a href=\"https://www.cdc.gov/abcs/reports-findings/surv-reports.html\">ABCs reports</a> describe the ABCs case definition and the specific methodology used to calculate rates and estimated numbers in the United States for each bacterium by year.  The methods, <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">surveillance areas</a>, and <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">laboratory isolate collection areas</a> have changed over time.\n                Additionally, the way missing data are taken into account changed in 2010.  It went from distributing unknown values based on known values of cases by site to use of multiple imputation using a sequential regression imputation method.\n                Given these changes over time, trends should be interpreted with caution.\n<ul><li> <a href=\"http://www.cdc.gov/abcs/methodology/index.html\">Methodology</a>\nFind details about surveillance population, case determination, surveillance evaluation, and more. </li> <li><a href=\"http://www.cdc.gov/abcs/reports-findings/index.html\">Reports and Findings</a>\nGet official interpretations from reports and publications created from ABCs data.\n </li>                </ul>",
-            "title": "Active Bacterial Core surveillance (ABCs) Group B Streptococcus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18682,66 +18596,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/95m5-agj4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/95m5-agj4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/95m5-agj4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/95m5-agj4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/95m5-agj4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/95m5-agj4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/95m5-agj4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/95m5-agj4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/95m5-agj4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/95m5-agj4",
+            "issued": "2021-06-23",
+            "keyword": [
+                "abcs",
+                "bactfacts"
+            ],
+            "landingPage": "https://data.cdc.gov/d/95m5-agj4",
+            "modified": "2024-09-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Active Bacterial Core surveillance (ABCs) Group B Streptococcus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://ephtracking.cdc.gov/DataExplorer/#/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-03-08",
-            "temporal": "2016-2020",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-08",
-            "keyword": [
-                "air pollution",
-                "air quality",
-                "asthma",
-                "environmental health",
-                "national ambient air quality standards",
-                "national environmental health tracking network",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/96sd-hxdt",
             "description": "This dataset provides modeled predictions of PM2.5 levels from the EPA's Downscaler model. Data are at the census tract level for 2016-2020. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information. Learn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action. By using these data, you signify your agreement to comply with the following requirements: 1. Use the data for statistical reporting and analysis only. 2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. 3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. 4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. 5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC. 6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2016 - 2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18749,71 +18656,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/96sd-hxdt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/96sd-hxdt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/96sd-hxdt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/96sd-hxdt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/96sd-hxdt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/96sd-hxdt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/96sd-hxdt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/96sd-hxdt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/96sd-hxdt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/96sd-hxdt",
+            "issued": "2024-03-08",
+            "keyword": [
+                "air pollution",
+                "air quality",
+                "asthma",
+                "environmental health",
+                "national ambient air quality standards",
+                "national environmental health tracking network",
+                "particulate matter",
+                "pm2.5"
+            ],
+            "landingPage": "https://ephtracking.cdc.gov/DataExplorer/#/",
+            "language": [
+                "English"
+            ],
+            "modified": "2024-03-08",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "spatial": "U.S. states",
+            "temporal": "2016-2020",
             "theme": [
                 "Environmental Health & Toxicology"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2016 - 2020"
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
-                "name": "data.cdc.gov"
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
@@ -18821,65 +18727,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/97bc-2r74/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/97bc-2r74/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/97bc-2r74/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/97bc-2r74/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/97bc-2r74/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/97bc-2r74/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/97bc-2r74/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/97bc-2r74/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/97bc-2r74/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease, Age <5 years, Serotype b"
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
-                "name": "data.cdc.gov"
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
@@ -18887,64 +18795,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/97tt-n3j3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/97tt-n3j3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/97tt-n3j3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/97tt-n3j3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/97tt-n3j3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/97tt-n3j3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/97tt-n3j3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/97tt-n3j3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/97tt-n3j3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Chlamydia to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/986w-8kut",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/986w-8kut",
             "description": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18952,65 +18861,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/986w-8kut/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/986w-8kut/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/986w-8kut/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/986w-8kut/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/986w-8kut/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/986w-8kut/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/986w-8kut/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/986w-8kut/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/986w-8kut/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "NNDSS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9976-4iqj",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/986w-8kut",
             "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
             "keyword": [
                 "2021",
-                "animal",
-                "human",
+                "cryptosporidiosis",
+                "cyclosporiasis",
                 "nedss",
                 "netss",
                 "nndss",
-                "rabies",
                 "wonder"
             ],
+            "landingPage": "https://data.cdc.gov/d/986w-8kut",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "theme": [
+                "NNDSS"
+            ],
+            "title": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9976-4iqj",
             "description": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19018,66 +18926,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9976-4iqj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9976-4iqj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9976-4iqj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9976-4iqj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9976-4iqj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9976-4iqj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9976-4iqj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9976-4iqj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9976-4iqj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "NNDSS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9axm-gjt8",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/9976-4iqj",
             "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
             "keyword": [
                 "2021",
-                "dengue",
-                "dengue-like illness",
-                "dengue virus infections",
+                "animal",
+                "human",
                 "nedss",
                 "netss",
                 "nndss",
-                "severe dengue",
+                "rabies",
                 "wonder"
             ],
+            "landingPage": "https://data.cdc.gov/d/9976-4iqj",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "theme": [
+                "NNDSS"
+            ],
+            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
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
@@ -19085,68 +18992,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9axm-gjt8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9axm-gjt8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9axm-gjt8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9axm-gjt8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9axm-gjt8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9axm-gjt8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9axm-gjt8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9axm-gjt8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9axm-gjt8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9b5z-wnve",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-06-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-12-13/2023-09-14",
-            "modified": "2023-10-13",
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
-                "name": "CDC"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9b5z-wnve",
             "description": "This site provides historical data beginning June 14, 2023, for the visualization presented on <a href=\"https://covid.cdc.gov/covid-data-tracker/#vaccinations\">COVID-19 Data Tracker\u2019s \u201cVaccinations in the United States</a>\u201d site titled \u201cPercent of Total Population Who Are Up to Date with COVID-19 Vaccines\u201d\n\n<b>Definition for Up to Date:\nFor surveillance purposes people are \u2018Upto Date\u2019 with COVID-19 vaccines based on the following criteria:</b>\n\nPeople ages 6 years and older: Are up to date\u202fif they received 1 updated Pfizer-BioNTech or Moderna COVID-19 vaccine. \n\nChildren\u202fages 6 months to 5 years who received the\u202fPfizer-BioNTech\u202fCOVID-19 vaccine: Are up to date if: At ages 6 months to 4 years, they received 3 COVID-19 vaccine doses, including at least 1 updated COVID-19 dose; at age 5 years, they received at least 1 updated COVID-19 vaccine dose. \n\nChildren ages 6 months to 5 years who received the Moderna COVID-19 vaccine:\u202fAre up to date if they received 2 Moderna COVID-19 vaccine doses, including at least 1 updated COVID-19 vaccine dose. \n\nPeople who are unable or choose not to get a recommended mRNA vaccine: Are up to date if they receive the Novavax COVID-19 vaccine doses approved for their age group.\n\nCDC uses US Census estimates for the total populations within each specified demographic group regardless of prior vaccination status as denominators. \n\nData represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.",
-            "title": "COVID-19 Vaccines Up to Date Status",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19154,44 +19060,101 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9b5z-wnve/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9b5z-wnve/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9b5z-wnve/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9b5z-wnve/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9b5z-wnve/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9b5z-wnve/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9b5z-wnve/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9b5z-wnve/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9b5z-wnve/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/9b5z-wnve",
+            "issued": "2023-06-26",
+            "keyword": [
+                "administration",
+                "age",
+                "coronavirus",
+                "covid-19",
+                "immunization",
+                "izdl",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9b5z-wnve",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1D",
+            "modified": "2023-10-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
+            },
+            "references": [
+                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
+            ],
+            "spatial": "US",
+            "temporal": "2020-12-13/2023-09-14",
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "COVID-19 Vaccines Up to Date Status"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-05-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2023-07-29",
-            "modified": "2023-09-27",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nDeaths involving COVID-19, pneumonia, and influenza reported to NCHS by sex, age group, and jurisdiction of occurrence.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9bhg-hcku/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/9bhg-hcku/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/9bhg-hcku/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/9bhg-hcku/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/9bhg-hcku/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/9bhg-hcku/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/9bhg-hcku/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/9bhg-hcku",
+            "issued": "2020-05-01",
             "keyword": [
                 "age",
                 "age group",
@@ -19211,66 +19174,66 @@
                 "united states",
                 "yearly"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-09-27",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/9bhg-hcku",
-            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nDeaths involving COVID-19, pneumonia, and influenza reported to NCHS by sex, age group, and jurisdiction of occurrence.",
-            "title": "Provisional COVID-19 Deaths by Sex and Age",
-            "programCode": [
-                "009:020"
+            "spatial": "United States, Puerto Rico",
+            "temporal": "2020-01-01/2023-07-29",
+            "theme": [
+                "NCHS"
+            ],
+            "title": "Provisional COVID-19 Deaths by Sex and Age"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "This dataset includes the number of deaths from all causes by week in which the death occurred and by jurisdiction, from 2015 to 2019, United States and Puerto Rico.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/9bhg-hcku/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/9cpv-whbv/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9bhg-hcku/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9bhg-hcku/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/9cpv-whbv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9cpv-whbv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9bhg-hcku/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9bhg-hcku/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/9cpv-whbv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9cpv-whbv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9bhg-hcku/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9bhg-hcku/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/9cpv-whbv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9cpv-whbv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
-            "theme": [
-                "NCHS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/cov19_landing_2024.htm",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/9cpv-whbv",
             "issued": "2024-09-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-01-04/2020-01-03",
-            "modified": "2024-09-24",
             "keyword": [
                 "all causes",
                 "deaths",
@@ -19282,65 +19245,65 @@
                 "united states",
                 "weekly"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/cov19_landing_2024.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-24",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/9cpv-whbv",
-            "description": "This dataset includes the number of deaths from all causes by week in which the death occurred and by jurisdiction, from 2015 to 2019, United States and Puerto Rico.",
-            "title": "Weekly counts of deaths from all causes by jurisdiction,  2015-2019",
-            "programCode": [
-                "009:020"
+            "spatial": "United States, Puerto Rico",
+            "temporal": "2015-01-04/2020-01-03",
+            "theme": [
+                "NCHS"
+            ],
+            "title": "Weekly counts of deaths from all causes by jurisdiction,  2015-2019"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/9cpv-whbv/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/9d9z-vf8f/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9cpv-whbv/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9cpv-whbv/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/9d9z-vf8f/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9d9z-vf8f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9cpv-whbv/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9cpv-whbv/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/9d9z-vf8f/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9d9z-vf8f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9cpv-whbv/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9cpv-whbv/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/9d9z-vf8f/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9d9z-vf8f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P4Y",
-            "theme": [
-                "NCHS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9d9z-vf8f",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/9d9z-vf8f",
             "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
             "keyword": [
                 "2021",
                 "anaplasma phagocytophilum infection",
@@ -19351,63 +19314,63 @@
                 "nndss",
                 "wonder"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CDC INFO",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/9d9z-vf8f",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/9d9z-vf8f",
-            "description": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection",
-            "programCode": [
-                "009:020"
+            "theme": [
+                "NNDSS"
+            ],
+            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nProvisional counts of deaths by the month the death occurred and by select causes of death for 2020-2023.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/9d9z-vf8f/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9d9z-vf8f/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9d9z-vf8f/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/9dzk-mvmi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9d9z-vf8f/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9d9z-vf8f/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/9dzk-mvmi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9d9z-vf8f/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9d9z-vf8f/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/9dzk-mvmi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "NNDSS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/9dzk-mvmi",
             "issued": "2021-02-03",
-            "temporal": "2020/2023",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-27",
             "keyword": [
                 "all causes",
                 "alzheimer disease",
@@ -19438,87 +19401,35 @@
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
-                "name": "National Center for Health Statistics"
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
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9dzk-mvmi/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9dzk-mvmi/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/9dzk-mvmi/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
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
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual  (R/P1Y)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-07-05",
-            "temporal": "2001/2021",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-24",
-            "keyword": [
-                "american dental association",
-                "dentists",
-                "health us",
-                "sdoh-access-to-health-care",
-                "united states"
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
-            "identifier": "https://data.cdc.gov/api/views/9epi-jrff",
             "description": "Data on active dentists in the United States by state. Data are from Health, United States. SOURCE: American Dental Association, Health Policy Institute.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Dentists, by state: United States.",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19526,44 +19437,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9epi-jrff/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9epi-jrff/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9epi-jrff/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9epi-jrff/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9epi-jrff/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9epi-jrff/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9epi-jrff/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9epi-jrff/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9epi-jrff/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9epi-jrff",
+            "issued": "2024-07-05",
+            "keyword": [
+                "american dental association",
+                "dentists",
+                "health us",
+                "sdoh-access-to-health-care",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual  (R/P1Y)",
+            "modified": "2024-10-24",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "temporal": "2001/2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS Dentists, by state: United States."
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
@@ -19572,51 +19515,48 @@
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
                 "name": "National Center for Health Statistics"
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
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/medicare-restricted.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2023-12-08",
-            "temporal": "1999/2013",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data-linkage/cms/nchs-cms_medicare_linked_data-list_of_variables.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCHS Data Linkage Program",
+                "hasEmail": "mailto:DataLinkage@cdc.gov"
+            },
+            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/nchs-cms_medicare_linked_data_match_rate_tables.pdf",
+            "describedByType": "application/pdf",
+            "description": "NCHS has linked data from various surveys with 1999-2013 Medicare program enrollment and health care utilization and expenditure data from the Centers for Medicare & Medicaid Services (CMS). Linkage of the NCHS survey participants with the CMS Medicare data provides the opportunity to study changes in health status, health care utilization and costs, and prescription drug use among Medicare enrollees. Medicare is the federal health insurance program for people who are 65 or older, certain younger people with disabilities, and people with End-Stage Renal Disease.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9fpg-7hvw",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2023-12-08",
             "keyword": [
                 "linked medicare data",
                 "nhcs",
@@ -19625,69 +19565,37 @@
                 "sdoh-source-of-health-care",
                 "sdoh-use-of-health-care"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NCHS Data Linkage Program",
-                "hasEmail": "mailto:DataLinkage@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/medicare-restricted.htm",
+            "modified": "2024-10-11",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/9fpg-7hvw",
-            "description": "NCHS has linked data from various surveys with 1999-2013 Medicare program enrollment and health care utilization and expenditure data from the Centers for Medicare & Medicaid Services (CMS). Linkage of the NCHS survey participants with the CMS Medicare data provides the opportunity to study changes in health status, health care utilization and costs, and prescription drug use among Medicare enrollees. Medicare is the federal health insurance program for people who are 65 or older, certain younger people with disabilities, and people with End-Stage Renal Disease.",
-            "title": "NCHS Survey Data Linked to Centers for Medicare & Medicaid Services (CMS) 1999-2013 Medicare Data",
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
+                "https://www.cdc.gov/nchs/data-linkage/cms/nchs-cms_medicare_linked_data-list_of_variables.pdf"
             ],
-            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/nchs-cms_medicare_linked_data_match_rate_tables.pdf",
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
-                "name": "data.cdc.gov"
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
@@ -19695,75 +19603,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9g7x-sfq4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9g7x-sfq4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9g7x-sfq4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9g7x-sfq4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9g7x-sfq4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9g7x-sfq4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9g7x-sfq4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9g7x-sfq4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9g7x-sfq4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2018-01-26",
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
+            "title": "NNDSS - Table III. Tuberculosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-04-28",
-            "@type": "dcat:Dataset",
-            "temporal": "1988/2019",
-            "modified": "2023-08-29",
-            "keyword": [
-                "adolescent",
-                "adult",
-                "african americans",
-                "age",
-                "asian continental ancestry group",
-                "child",
-                "chronic conditions",
-                "continental population groups",
-                "european continental ancestry group",
-                "health risk factors",
-                "health us",
-                "hispanic americans",
-                "obesity",
-                "overweight",
-                "poverty",
-                "sdoh-poverty-income",
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
-            "identifier": "https://data.cdc.gov/api/views/9gay-j69q",
             "description": "Data on obesity among children and adolescents aged 2-19 years by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National Health and Nutrition Examination Survey. For more information on the National Health and Nutrition Examination Survey, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
-            "title": "Obesity among children and adolescents aged 2\u201319 years, by selected characteristics: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19771,69 +19670,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9gay-j69q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9gay-j69q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9gay-j69q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9gay-j69q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9gay-j69q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9gay-j69q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9gay-j69q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9gay-j69q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9gay-j69q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/9gay-j69q",
+            "issued": "2022-04-28",
+            "keyword": [
+                "adolescent",
+                "adult",
+                "african americans",
+                "age",
+                "asian continental ancestry group",
+                "child",
+                "chronic conditions",
+                "continental population groups",
+                "european continental ancestry group",
+                "health risk factors",
+                "health us",
+                "hispanic americans",
+                "obesity",
+                "overweight",
+                "poverty",
+                "sdoh-poverty-income",
+                "sex"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2023-08-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "1988/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Obesity among children and adolescents aged 2\u201319 years, by selected characteristics: United States"
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
-                "name": "data.cdc.gov"
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
@@ -19841,70 +19748,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9gny-cbhc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9gny-cbhc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9gny-cbhc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9gny-cbhc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9gny-cbhc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9gny-cbhc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9gny-cbhc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9gny-cbhc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9gny-cbhc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table 1B. Arboviral diseases, neuroinvasive and non-neuroinvasive, Jamestown Canyon virus disease to Powassan virus disease"
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
-                "sdoh-environmental",
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
-                "name": "National Center for Health Statistics"
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
@@ -19912,58 +19816,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9hdi-ekmb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9hdi-ekmb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9hdi-ekmb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9hdi-ekmb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9hdi-ekmb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9hdi-ekmb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9hdi-ekmb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9hdi-ekmb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9hdi-ekmb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "sdoh-environmental",
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
+                "name": "National Center for Health Statistics"
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
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/9ikp-t8tw",
-            "issued": "2024-11-21",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Emma Baubly",
                 "hasEmail": "mailto:rno8@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9ikp-t8tw",
             "description": "",
-            "title": "CDT_INDIVIDUAL_BY_WEEK_LOCAL",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19971,57 +19889,49 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9ikp-t8tw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9ikp-t8tw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9ikp-t8tw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9ikp-t8tw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9ikp-t8tw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9ikp-t8tw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9ikp-t8tw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9ikp-t8tw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9ikp-t8tw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/9ikp-t8tw",
+            "issued": "2024-11-21",
+            "landingPage": "https://data.cdc.gov/d/9ikp-t8tw",
+            "modified": "2025-01-23",
+            "programCode": [
+                "009:028"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "CDT_INDIVIDUAL_BY_WEEK_LOCAL"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9ix3-ryt6",
-            "issued": "2016-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2016-03-03",
-            "keyword": [
-                "2014",
-                "giardiasis",
-                "gonorrhea",
-                "haemophilus influenzae",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
-            ],
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "wja0@cdc.gov",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9ix3-ryt6",
             "description": "NNDSS - Table II. Giardiasis to Haemophilus influenza - 2014.\r\nIn this Table, all conditions with a 5-year average annual national total of more than or equals 1,000 cases but less than or equals 10,000 cases will be displayed (\u2265 1,000 and \u2264 10,000). The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. \r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. \r\n* Case counts for reporting years 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Data for H. influenzae (age <5 yrs serotype b, nonserotype b, and unknown serotype) are available in Table I.\r\n\r\nMore information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
-            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20029,45 +19939,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9ix3-ryt6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9ix3-ryt6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9ix3-ryt6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9ix3-ryt6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9ix3-ryt6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9ix3-ryt6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9ix3-ryt6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9ix3-ryt6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9ix3-ryt6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9ix3-ryt6",
+            "issued": "2016-03-03",
+            "keyword": [
+                "2014",
+                "giardiasis",
+                "gonorrhea",
+                "haemophilus influenzae",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9ix3-ryt6",
+            "modified": "2016-03-03",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=LimitedAccess",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
-            "issued": "2023-01-01",
-            "@type": "dcat:Dataset",
-            "temporal": "1999/2021",
-            "modified": "2023-04-17",
-            "references": [
-                "https://www.cdc.gov/nchs/nhanes/index.htm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "Since 1999, the NHANES sample design has consisted of multi-year, stratified, clustered four-stage samples, with data release in 2-year cycles.",
+            "description": "The <b>National Health and Nutrition Examination Survey</b> (NHANES) is designed to assess the health and nutritional status of adults and children in the United States. The survey is unique in that it combines interviews with standardized physical examinations and laboratory tests. <br>\nNHANES was conducted on a periodic basis from 1971 to 1994. In 1999 NHANES became continuous. Every year, approximately 5,000 people of all ages are interviewed in their homes and complete the health examination conducted in a mobile examination center. <br>\nThe NHANES interview includes demographic, socioeconomic, dietary, and health-related questions. The examination component consists of medical, dental, and physiological measurements, as well as the collection of biospecimens, such as blood and urine for laboratory testing.\n\nThis set of restricted data contains indirect identifying and/or sensitive information collected in <b>continuous NHANES since 1999</b>. Please refer to the links below for additional data available from NHANES:  \n<ul><li><a href=\"https://wwwn.cdc.gov/nchs/nhanes/Default.aspx\">NHANES Public Use Data at: https://wwwn.cdc.gov/nchs/nhanes/Default.aspx</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/hdx4-e4uu\">NHANES Genetic Restricted Data at: https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/hdx4-e4uu</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/ic32-yq9m\">NHANES Restricted Data: Prior to 1999 at: https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/ic32-yq9m</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/3-NHANES-National-Youth-Fitness-Survey-NNYFS-Restr/5u84-m4rs\">NHANES National Youth Fitness Survey (NNYFS) Restricted Data at: https://data.cdc.gov/dataset/3-NHANES-National-Youth-Fitness-Survey-NNYFS-Restr/5u84-m4rs</a></li> </ul>\nPlease refer to the <a href=\"https://wwwn.cdc.gov/nchs/nhanes/analyticguidelines.aspx\">NHANES Analytic Guidelines at: https://wwwn.cdc.gov/nchs/nhanes/analyticguidelines.aspx</a> and the on-line <a href=\"https://wwwn.cdc.gov/nchs/nhanes/tutorials/default.aspx\">NHANES Tutorial at: https://wwwn.cdc.gov/nchs/nhanes/tutorials/default.aspx</a> for further details on the survey design, implementation, and data analysis.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "National Health and Nutrition Examination Survey (NHANES) Restricted Data: 1999 to Present"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9ixb-fwvy",
+            "isPartOf": "https://wwwn.cdc.gov/nchs/nhanes/default.aspx",
+            "issued": "2023-01-01",
             "keyword": [
                 "health statistics",
                 "nchs",
@@ -20094,79 +20034,39 @@
                 "surveillance",
                 "survey"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=LimitedAccess",
+            "modified": "2023-04-17",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/9ixb-fwvy",
-            "description": "The <b>National Health and Nutrition Examination Survey</b> (NHANES) is designed to assess the health and nutritional status of adults and children in the United States. The survey is unique in that it combines interviews with standardized physical examinations and laboratory tests. <br>\nNHANES was conducted on a periodic basis from 1971 to 1994. In 1999 NHANES became continuous. Every year, approximately 5,000 people of all ages are interviewed in their homes and complete the health examination conducted in a mobile examination center. <br>\nThe NHANES interview includes demographic, socioeconomic, dietary, and health-related questions. The examination component consists of medical, dental, and physiological measurements, as well as the collection of biospecimens, such as blood and urine for laboratory testing.\n\nThis set of restricted data contains indirect identifying and/or sensitive information collected in <b>continuous NHANES since 1999</b>. Please refer to the links below for additional data available from NHANES:  \n<ul><li><a href=\"https://wwwn.cdc.gov/nchs/nhanes/Default.aspx\">NHANES Public Use Data at: https://wwwn.cdc.gov/nchs/nhanes/Default.aspx</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/hdx4-e4uu\">NHANES Genetic Restricted Data at: https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/hdx4-e4uu</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/ic32-yq9m\">NHANES Restricted Data: Prior to 1999 at: https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/ic32-yq9m</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/3-NHANES-National-Youth-Fitness-Survey-NNYFS-Restr/5u84-m4rs\">NHANES National Youth Fitness Survey (NNYFS) Restricted Data at: https://data.cdc.gov/dataset/3-NHANES-National-Youth-Fitness-Survey-NNYFS-Restr/5u84-m4rs</a></li> </ul>\nPlease refer to the <a href=\"https://wwwn.cdc.gov/nchs/nhanes/analyticguidelines.aspx\">NHANES Analytic Guidelines at: https://wwwn.cdc.gov/nchs/nhanes/analyticguidelines.aspx</a> and the on-line <a href=\"https://wwwn.cdc.gov/nchs/nhanes/tutorials/default.aspx\">NHANES Tutorial at: https://wwwn.cdc.gov/nchs/nhanes/tutorials/default.aspx</a> for further details on the survey design, implementation, and data analysis.",
-            "title": "National Health and Nutrition Examination Survey (NHANES) Restricted Data: 1999 to Present",
-            "isPartOf": "https://wwwn.cdc.gov/nchs/nhanes/default.aspx",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "mediaType": "text/html",
-                    "title": "National Health and Nutrition Examination Survey (NHANES) Restricted Data: 1999 to Present"
-                }
+            "references": [
+                "https://www.cdc.gov/nchs/nhanes/index.htm"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "United States",
-            "describedBy": "Since 1999, the NHANES sample design has consisted of multi-year, stratified, clustered four-stage samples, with data release in 2-year cycles.",
+            "temporal": "1999/2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Health and Nutrition Examination Survey (NHANES) Restricted Data: 1999 to Present"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-05-14",
-            "@type": "dcat:Dataset",
-            "temporal": "1950/2019",
-            "modified": "2022-04-27",
-            "keyword": [
-                "african americans",
-                "age",
-                "alaskan natives",
-                "american natives",
-                "asian continental ancestry group",
-                "continental population groups",
-                "death",
-                "deaths",
-                "european continental ancestry group",
-                "health us",
-                "hispanic americans",
-                "injury",
-                "mental health",
-                "mortality",
-                "sex",
-                "suicide"
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
-            "identifier": "https://data.cdc.gov/api/views/9j2v-jamp",
             "description": "Data on death rates for suicide, by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National  Vital Statistics System (NVSS); Grove RD, Hetzel AM. Vital statistics rates in the United States, 1940\u20131960. National Center for Health Statistics. 1968; numerator data from NVSS annual public-use Mortality Files; denominator data from U.S. Census Bureau national population estimates; and Murphy SL, Xu JQ, Kochanek KD, Arias E, Tejada-Vera B. Deaths: Final data for 2018. National Vital Statistics Reports; vol 69 no 13. Hyattsville, MD: National Center for Health Statistics. 2021. Available from: https://www.cdc.gov/nchs/products/nvsr.htm. For more information on the National Vital Statistics System, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
-            "title": "Death rates for suicide, by sex, race, Hispanic origin, and age: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20174,69 +20074,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9j2v-jamp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9j2v-jamp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9j2v-jamp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9j2v-jamp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9j2v-jamp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9j2v-jamp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9j2v-jamp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9j2v-jamp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9j2v-jamp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/9j2v-jamp",
+            "issued": "2021-05-14",
+            "keyword": [
+                "african americans",
+                "age",
+                "alaskan natives",
+                "american natives",
+                "asian continental ancestry group",
+                "continental population groups",
+                "death",
+                "deaths",
+                "european continental ancestry group",
+                "health us",
+                "hispanic americans",
+                "injury",
+                "mental health",
+                "mortality",
+                "sex",
+                "suicide"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-04-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "1950/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Death rates for suicide, by sex, race, Hispanic origin, and age: United States"
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
-                "name": "data.cdc.gov"
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
@@ -20244,66 +20151,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9k8a-cbgx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9k8a-cbgx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9k8a-cbgx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9k8a-cbgx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9k8a-cbgx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9k8a-cbgx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9k8a-cbgx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9k8a-cbgx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9k8a-cbgx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "NNDSS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9kbf-icdi",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/9k8a-cbgx",
             "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
             "keyword": [
                 "2021",
-                "brucellosis",
-                "campylobacteriosis",
-                "candida auris",
-                "clinical",
+                "imported",
+                "indigenous",
+                "malaria",
+                "measles",
                 "nedss",
                 "netss",
                 "nndss",
                 "wonder"
             ],
+            "landingPage": "https://data.cdc.gov/d/9k8a-cbgx",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "theme": [
+                "NNDSS"
+            ],
+            "title": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
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
@@ -20311,67 +20218,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9kbf-icdi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9kbf-icdi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9kbf-icdi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9kbf-icdi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9kbf-icdi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9kbf-icdi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9kbf-icdi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9kbf-icdi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9kbf-icdi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical"
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
-                "name": "Environmental Public Health Tracking"
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
@@ -20379,55 +20285,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9kjw-3miq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9kjw-3miq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9kjw-3miq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9kjw-3miq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9kjw-3miq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9kjw-3miq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9kjw-3miq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9kjw-3miq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9kjw-3miq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "U.S. State and Territorial Orders Closing and Reopening Bars Issued from March 11, 2020 through August 15, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/9kpc-xntn",
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
-                "name": "data.cdc.gov"
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
@@ -20435,41 +20353,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9kpc-xntn",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/9kpc-xntn",
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
+            "title": "Controlled Generation of Peracetic Acid Atmospheres for the Evaluation of Chemical Samplers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9mw4-6adp",
+            "accrualPeriodicity": "Annually",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-09-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-02",
-            "keyword": [
-                "asd",
-                "autism",
-                "autism prevalence",
-                "autism spectrum disorder",
-                "prevalence studies"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC Info",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9mw4-6adp",
             "description": "This data table provides a collection of information from peer-reviewed autism prevalence studies. Information reported from each study includes the autism prevalence estimate and additional study characteristics (e.g., case ascertainment and criteria). A PubMed search was conducted to identify studies published at any time through September 2020 using the search terms: autism (title/abstract) OR autistic (title/abstract) AND prevalence (title/abstract). Data were abstracted and included if the study fulfilled the following criteria: \n\u2022\tThe study was published in English; \n\u2022\tThe study produced at least one autism prevalence estimate; and\n\u2022\tThe study was population-based (any age range) within a defined geographic area.",
-            "title": "autism prevalence studies",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20477,68 +20389,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9mw4-6adp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9mw4-6adp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9mw4-6adp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9mw4-6adp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9mw4-6adp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9mw4-6adp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9mw4-6adp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9mw4-6adp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9mw4-6adp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "Annually",
+            "identifier": "https://data.cdc.gov/api/views/9mw4-6adp",
+            "issued": "2020-09-17",
+            "keyword": [
+                "asd",
+                "autism",
+                "autism prevalence",
+                "autism spectrum disorder",
+                "prevalence studies"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9mw4-6adp",
+            "modified": "2023-05-02",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "autism prevalence studies"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9n3x-apcd",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
-            "keyword": [
-                "2015",
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
-            "identifier": "https://data.cdc.gov/api/views/9n3x-apcd",
             "description": "NNDSS - Table II. Cryptosporidiosis to Dengue - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Data for dengue-like illness will be included in this table after the CDC obtains Office of Management and Budget (OMB) Paperwork Reduction Act (PRA) to receive data for this condition.",
-            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20546,66 +20452,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9n3x-apcd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9n3x-apcd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9n3x-apcd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9n3x-apcd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9n3x-apcd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9n3x-apcd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9n3x-apcd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9n3x-apcd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9n3x-apcd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9n3x-apcd",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
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
+            "landingPage": "https://data.cdc.gov/d/9n3x-apcd",
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
+            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue"
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
-                "name": "data.cdc.gov"
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
@@ -20613,67 +20520,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9qys-crt2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9qys-crt2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9qys-crt2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9qys-crt2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9qys-crt2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9qys-crt2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9qys-crt2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9qys-crt2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9qys-crt2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2019-01-03",
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
+            "title": "NNDSS - Table II. Meningococcal disease to Pertussis"
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
-                "name": "data.cdc.gov"
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
@@ -20681,67 +20588,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9t9r-e5a3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9t9r-e5a3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9t9r-e5a3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9t9r-e5a3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9t9r-e5a3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9t9r-e5a3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9t9r-e5a3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9t9r-e5a3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9t9r-e5a3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "data.cdc.gov"
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
@@ -20749,73 +20659,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9tjt-seye/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9tjt-seye/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9tjt-seye/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9tjt-seye/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9tjt-seye/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9tjt-seye/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9tjt-seye/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9tjt-seye/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9tjt-seye/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-07-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-15",
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
-            "identifier": "https://data.cdc.gov/api/views/9umn-c3jf",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-ZCTA-Data-2020/qnzd-25i4",
             "description": "This dataset contains model-based ZIP Code Tabulation Area (ZCTA) level estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 36 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population data, and American Community Survey 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, ZCTA Data 2023 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20823,50 +20725,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9umn-c3jf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9umn-c3jf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9umn-c3jf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9umn-c3jf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9umn-c3jf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9umn-c3jf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9umn-c3jf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9umn-c3jf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9umn-c3jf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-ZCTA-Data-2020/qnzd-25i4",
+            "identifier": "https://data.cdc.gov/api/views/9umn-c3jf",
+            "issued": "2024-07-15",
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
+            "modified": "2024-07-15",
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
+            "title": "PLACES: Local Data for Better Health, ZCTA Data 2023 release"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9vgf-r2z6",
-            "issued": "2024-07-23",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/9vgf-r2z6",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20874,56 +20795,49 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9vgf-r2z6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9vgf-r2z6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9vgf-r2z6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9vgf-r2z6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9vgf-r2z6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9vgf-r2z6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9vgf-r2z6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9vgf-r2z6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9vgf-r2z6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/9vgf-r2z6",
+            "issued": "2024-07-23",
+            "landingPage": "https://data.cdc.gov/d/9vgf-r2z6",
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
-            "landingPage": "https://data.cdc.gov/d/9w38-t35p",
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
-            "identifier": "https://data.cdc.gov/api/views/9w38-t35p",
             "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012, 2014.",
-            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 6 - Dallas",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20931,65 +20845,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9w38-t35p/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9w38-t35p/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9w38-t35p/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9w38-t35p/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9w38-t35p/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9w38-t35p/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9w38-t35p/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9w38-t35p/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9w38-t35p/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9w38-t35p",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9w38-t35p",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 6 - Dallas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9x7v-wy9u",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9x7v-wy9u",
             "description": "NNDSS - TABLE 1II. Tetanus to Trichinellosis \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20997,71 +20905,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9x7v-wy9u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9x7v-wy9u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9x7v-wy9u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9x7v-wy9u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9x7v-wy9u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9x7v-wy9u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9x7v-wy9u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9x7v-wy9u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9x7v-wy9u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9x7v-wy9u",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "nedss",
+                "netss",
+                "nndss",
+                "tetanus",
+                "toxic shock syndrome (other than streptococcal)",
+                "trichinellosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9x7v-wy9u",
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
+            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis"
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
-                "gis",
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
-            "identifier": "https://data.cdc.gov/api/views/9xb7-9z99",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
```

