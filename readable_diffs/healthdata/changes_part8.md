# Change History for healthdata.json (Part 8)

### Changes from 31606f9 to dd2190f (Part 7/11)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/fc5f-ixvg",
             "description": "NNDSS - Table 1D. Arboviral diseases, neuroinvasive and non-neuroinvasive, West Nile virus disease to Babesiosis - 2019.In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1D. Arboviral diseases, West Nile virus to Babesiosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87952,35 +87929,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fc5f-ixvg",
+            "issued": "2019-04-24",
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
+            "landingPage": "https://data.cdc.gov/d/fc5f-ixvg",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2020-01-07",
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
-            "landingPage": "https://data.cdc.gov/d/nnvr-zdhw",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Respiratory Health Division, Surveillance Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/nnvr-zdhw",
             "description": "The National Study of Coal Workers\u2019 Pneumoconiosis (NSCWP) is a large, continuing epidemiologic study of the respiratory health of U.S. coal miners. By using information from the study, prevalence of coal workers\u2019 pneumoconiosis (CWP) was related to indexes of dust exposure obtained from research and compliance sampling data. Clear relationships between prevalences of both simple CWP and progressive massive fibrosis (PMF) and estimated dust exposure were seen. Additional effects independently associated with coal rank (% carbon) and age were also seen. Logistic model fitting indicated that between 2% and 12% of miners exposed to a 2-mg/m3 dust environment in bituminous coal mines would be expected to have Category 2 or greater CWP after a 40-yr working life; PMF would be expected for between 1.3% and 6.7%. The risks for anthracite miners appeared to be greater. There was a suggestion of a background level of abnormality, not associated with dust exposure, but increasing with age. Although there are certain we",
-            "title": "An Investigation Into the Relationship Between Coal Workers\u2019 Pneumoconiosis and Dust Exposure in U.S. Coal Miners",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87988,39 +87975,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/nnvr-zdhw",
+            "issued": "2024-11-13",
+            "landingPage": "https://data.cdc.gov/d/nnvr-zdhw",
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
+            "title": "An Investigation Into the Relationship Between Coal Workers\u2019 Pneumoconiosis and Dust Exposure in U.S. Coal Miners"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hget-9fst",
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
-            "identifier": "https://data.cdc.gov/api/views/hget-9fst",
             "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2014 national data: National Occupant Protection Use Survey (NOPUS), 2014.  Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 state data: Seat Belt Use in 2014- Use Rates in the States and Territories",
-            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 2 - New York",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88043,45 +88026,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hget-9fst",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hget-9fst",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 2 - New York"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/jf8m-mtc3",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-20",
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
-            "identifier": "https://data.cdc.gov/api/views/jf8m-mtc3",
             "description": "NNDSS - TABLE 1V. Malaria to Measles, Imported - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \n\nNotice:  The total numbers of measles cases in Table 1v for weeks 1-51 in the 2019 data are correct but counts for imported and indigenous categories are incorrect. Measles data for week 52 (in Table 1v) were updated on 02-28-2020 to correct the classification of imported and indigenous. Please see week 52, 2019 data for the correct breakout of imported and indigenous measles cases.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\n\n\u00a7 Measles is considered imported if the disease was acquired outside of the United States and is considered indigenous if the disease was acquired anywhere within the United States or it is not known where the disease was acquired.",
-            "title": "NNDSS - TABLE 1V. Malaria to Measles, Imported",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88104,35 +88081,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/jf8m-mtc3",
+            "issued": "2019-04-24",
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
+            "landingPage": "https://data.cdc.gov/d/jf8m-mtc3",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2020-03-20",
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
-            "landingPage": "https://data.cdc.gov/d/hh8a-ys2f",
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
-            "identifier": "https://data.cdc.gov/api/views/hh8a-ys2f",
             "description": "The association between human respiratory disease transmission by respiratory droplets and aerosols is well established for several known pathogens.1 Given that the average individual spends > 90% of their day indoors, there has been intense focus on factors associated with indoor transmission. To minimize exposure risks, the Centers for Disease Control and Prevention (CDC) recommends behavioral and personal protective equipment mitigation strategies to limit COVID-19 transmission, including wearing masks, maintaining physical distances of  \u2265 1.8 m, and avoiding crowded indoor and outdoor spaces. As such, the current investigation examines the combined effect of physical distancing, universal masking, and ventilation on exposure to airborne particles generated during breathing and coughing within a controlled indoor environment. The results of this investigation quantitatively examine the contribution of the matrix of controls employed and provides guidance on respiratory disease mitigation strategies within the indoor environment.",
-            "title": "Reduction of exposure to simulated respiratory aerosols using ventilation, physical distancing, and universal masking",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88140,40 +88127,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hh8a-ys2f",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/hh8a-ys2f",
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
+            "title": "Reduction of exposure to simulated respiratory aerosols using ventilation, physical distancing, and universal masking"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/jirv-7bvn",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2014-11-07",
-            "temporal": "2015-01-01T00:00:00+00:00/2016-01-01T00:00:00+00:00",
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
-            "identifier": "4d7af295-2132-55a8-b40c-d6630061f3e8",
             "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
-            "title": "NADAC (National Average Drug Acquisition Cost) 2015",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88182,103 +88165,98 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "4d7af295-2132-55a8-b40c-d6630061f3e8",
+            "issued": "2014-11-07",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "landingPage": "https://healthdata.gov/d/jirv-7bvn",
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
+            "temporal": "2015-01-01T00:00:00+00:00/2016-01-01T00:00:00+00:00",
             "theme": [
                 "National Average Drug Acquisition Cost",
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "NADAC (National Average Drug Acquisition Cost) 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/jj4y-qp9m",
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
-            "identifier": "f48c4dc5-80d3-5528-8d79-238c124fe10d",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_states_measures",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states_measures.csv",
-                    "description": "{\"dataset\": \"states_measures\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"states_measures\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states_measures.csv",
+                    "mediaType": "text/csv",
                     "title": "states_measures csv file"
                 }
             ],
+            "identifier": "f48c4dc5-80d3-5528-8d79-238c124fe10d",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/jj4y-qp9m",
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
+            "title": "implAuto_states_measures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-provider",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-05-11",
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
-                "original medicare"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/ee6fb1a5-39b9-46b3-a980-a7284551a732/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-inpatient-hospitals-by-provider-data-dictionary",
             "description": "The Medicare Inpatient Hospitals by Provider dataset provides information on inpatient discharges for Original Medicare Part A beneficiaries by IPPS hospitals. It includes information on the use, payment, and hospital charges for more than 3,000 U.S. hospitals that received IPPS payments. The data are organized by hospital.",
-            "title": "Medicare Inpatient Hospitals - by Provider",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ee6fb1a5-39b9-46b3-a980-a7284551a732/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ee6fb1a5-39b9-46b3-a980-a7284551a732/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Inpatient Hospitals - by Provider : 2022-12-01"
                 },
                 {
@@ -88402,52 +88380,50 @@
                     "title": "Medicare Inpatient Hospitals - by Provider : 2013-12-02"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-inpatient-hospitals-by-provider-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/ee6fb1a5-39b9-46b3-a980-a7284551a732/data-viewer",
+            "issued": "2023-05-11",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "hospitals & facilities",
+                "inpatient",
+                "medicare",
+                "original medicare"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-provider",
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
+            "title": "Medicare Inpatient Hospitals - by Provider"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ig4m-ub43",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-01-08",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "2014",
-                "chickenpox",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "varicella",
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
-            "identifier": "https://data.cdc.gov/api/views/ig4m-ub43",
             "description": "NNDSS - Table II. Varicella to West Nile virus disease - 2014.In this Table, all conditions with a 5-year average annual national total of more than or equals 1,000 cases but less than or equals 10,000 cases will be displayed (\ufffd\ufffd\ufffd 1,000 and \ufffd\ufffd_ 10,000). The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Case counts for reporting years 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd\ufffd Updated weekly from reports to the Division of Vector-Borne Infectious Diseases, National Center for Zoonotic, Vector-Borne, and Enteric Diseases (ArboNet Surveillance). Data for California serogroup, eastern equine, Powassan, St. Louis, and western equine diseases are available in Table I. \ufffd\ufffd Not reportable in all states. Data from states where the condition is not reportable are excluded from this table, except starting in 2007 for the Arboviral diseases and influenza-associated pediatric mortality, and in 2003 for SARS-CoV. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/document/SRCA_FINAL_REPORT_2006-2012_final.xlsx.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
-            "title": "NNDSS - Table II. Varicella to West Nile virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88470,44 +88446,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ig4m-ub43",
+            "issued": "2015-01-08",
+            "keyword": [
+                "2014",
+                "chickenpox",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "varicella",
+                "west nile virus",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ig4m-ub43",
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
+            "title": "NNDSS - Table II. Varicella to West Nile virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-visualization/drug-poisoning-mortality/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2017-12-06",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-30",
-            "keyword": [
-                "deaths",
-                "drug poisoning",
-                "mortality",
-                "national",
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
-            "identifier": "https://data.cdc.gov/api/views/xbxb-epbu",
             "description": "This dataset describes drug poisoning deaths at the U.S. and state level by selected demographic characteristics, and includes age-adjusted death rates for drug poisoning. \r\n\r\nDeaths are classified using the International Classification of Diseases, Tenth Revision (ICD\u201310). Drug-poisoning deaths are defined as having ICD\u201310 underlying cause-of-death codes X40\u2013X44 (unintentional), X60\u2013X64 (suicide), X85 (homicide), or Y10\u2013Y14 (undetermined intent).\r\n\r\nEstimates are based on the National Vital Statistics System multiple cause-of-death mortality files (1). Age-adjusted death rates (deaths per 100,000 U.S. standard population for 2000) are calculated using the direct method. Populations used for computing death rates for 2011\u20132016 are postcensal estimates based on the 2010 U.S. census. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for noncensus years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published.\r\n\r\nDeath rates for some states and years may be low due to a high number of unresolved pending cases or misclassification of ICD\u201310 codes for unintentional poisoning as R99, \u201cOther ill-defined and unspecified causes of mortality\u201d (2). For example, this issue is known to affect New Jersey in 2009 and West Virginia in 2005 and 2009 but also may affect other years and other states. Drug poisoning death rates may be underestimated in those instances.\r\n\r\nREFERENCES\r\n1. National Center for Health Statistics. National Vital Statistics System: Mortality data. Available from: http://www.cdc.gov/nchs/deaths.htm.\r\n\r\n2. CDC. CDC Wonder: Underlying cause of death 1999\u20132016. Available from: http://wonder.cdc.gov/wonder/help/ucd.html.",
-            "title": "NCHS - Drug Poisoning Mortality by State: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88530,43 +88508,46 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://healthdata.gov/d/jki3-r9ys",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "py2025",
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
-            "identifier": "c4b9735c-68d0-4f8e-9563-cba97783618e",
             "description": "The Dental SHOP Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2025 Dental SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88574,36 +88555,38 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "c4b9735c-68d0-4f8e-9563-cba97783618e",
+            "issued": "2024-12-10",
+            "keyword": [
+                "py2025",
+                "qhp landscape instructions",
+                "sadp",
+                "shop",
+                "shop market dental"
+            ],
+            "landingPage": "https://healthdata.gov/d/jki3-r9ys",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2025 Dental SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/an65-3p9b",
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
-            "identifier": "https://data.cdc.gov/api/views/an65-3p9b",
             "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, HHS Region 1 - Boston",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88626,41 +88609,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/an65-3p9b",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/an65-3p9b",
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
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, HHS Region 1 - Boston"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/child-coverage-vaccination.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-29",
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
-            "identifier": "https://data.cdc.gov/api/views/vncy-2ds7",
             "description": "\u2022 Weekly Cumulative Influenza Vaccination Coverage by Flu Season, Selected Demographics, and Race and Ethnicity Among 6 Months-17 Years. \n\n\u2022 Weekly Influenza vaccination coverage and parental intent for vaccination among children is calculated using data from the National Immunization Survey\u2013Flu (NIS\u2013Flu) (https://www.cdc.gov/nis/about/index.html). NIS\u2013Flu is a national random-digit-dialed cellular telephone survey of households with children ages 6 months\u201317 years conducted during October-June. The respondent to a NIS\u2013Flu survey is a parent or guardian who said they were knowledgeable about the child\u2019s vaccination history. All estimates are based upon parental report of receipt of vaccination and month of that vaccination.",
-            "title": "Weekly Cumulative Influenza Vaccination Coverage by Flu Season, Selected Demographics, and Race and Ethnicity Among Children 6 Months-17 Years, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88683,58 +88665,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/vncy-2ds7",
+            "issued": "2025-01-29",
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
+            "title": "Weekly Cumulative Influenza Vaccination Coverage by Flu Season, Selected Demographics, and Race and Ethnicity Among Children 6 Months-17 Years, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2018-10-16",
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
-            "identifier": "https://data.cdc.gov/api/views/djk3-k3zs",
             "description": "2015, 2014. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project census city-level data in GIS-friendly format can be joined with city spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-City-Boundaries/n44h-hy2j) in a geographic information system (GIS) to produce maps of 27 measures at the city-level. Because some questions are only asked every other year in the BRFSS, there are 7 measures in this 2017 release from the 2014 BRFSS that were the same as the 2016 release.",
-            "title": "500 Cities: City-level Data (GIS Friendly Format), 2017 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88757,35 +88726,53 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/djk3-k3zs",
+            "issued": "2018-10-16",
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
+            "title": "500 Cities: City-level Data (GIS Friendly Format), 2017 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/sks5-7yq7",
-            "issued": "2018-06-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-07",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jarvis Sims",
                 "hasEmail": "mailto:xma4@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/sks5-7yq7",
             "description": "A complete listing of subscription databases provided by the Stephen B. Thacker CDC Library.",
-            "title": "CDC Library Subscription Databases",
-            "programCode": [
-                "009:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88808,90 +88795,79 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/sks5-7yq7",
+            "issued": "2018-06-06",
+            "landingPage": "https://data.cdc.gov/d/sks5-7yq7",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-07",
+            "programCode": [
+                "009:031"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "CDC Library Subscription Databases"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/jmxz-6n7j",
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
-                "service use",
-                "t-msis analytic files",
-                "vaccination"
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
-            "identifier": "43d419f9-f863-4f68-b622-311a8800100d",
             "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of vaccinations provided to Medicaid and CHIP beneficiaries under age 19 (as of the first day of the month), by state. The following vaccinations are included: Chickenpox, DTaP, HPV, Hepatitis A, Hepatitis B, Influenza, MMR, Meningococcal, Meningococcal B, Pneumococcal conjugate, Pneumococcal polysaccharide, Polio, Rotavirus, Tdap, and all vaccinations. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating vaccination measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Vaccinations Provided to the Medicaid and CHIP Population under age 19",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/Vaccinations-Provided-to-the-MedicaidCHIP-Population-under-age-19.csv",
-                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of vaccinations provided to Medicaid and CHIP beneficiaries under age 19 (as of the first day of the month), by state. The following vaccinations are included: Chickenpox, DTaP, HPV, Hepatitis A, Hepatitis B, Influenza, MMR, Meningococcal, Meningococcal B, Pneumococcal conjugate, Pneumococcal polysaccharide, Polio, Rotavirus, Tdap, and all vaccinations. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating vaccination measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of vaccinations provided to Medicaid and CHIP beneficiaries under age 19 (as of the first day of the month), by state. The following vaccinations are included: Chickenpox, DTaP, HPV, Hepatitis A, Hepatitis B, Influenza, MMR, Meningococcal, Meningococcal B, Pneumococcal conjugate, Pneumococcal polysaccharide, Polio, Rotavirus, Tdap, and all vaccinations. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating vaccination measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/Vaccinations-Provided-to-the-MedicaidCHIP-Population-under-age-19.csv",
+                    "mediaType": "text/csv",
                     "title": "Vaccinations Provided to the Medicaid and CHIP Population under age 19"
                 }
             ],
+            "identifier": "43d419f9-f863-4f68-b622-311a8800100d",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "medicaid",
+                "service use",
+                "t-msis analytic files",
+                "vaccination"
+            ],
+            "landingPage": "https://healthdata.gov/d/jmxz-6n7j",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
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
+            "title": "Vaccinations Provided to the Medicaid and CHIP Population under age 19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/afja-b25e",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "keyword": [
-                "2016",
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
-            "identifier": "https://data.cdc.gov/api/views/afja-b25e",
             "description": "NNDSS - Table II. Giardiasis to Haemophilus influenza - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.  NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\u00a7 Data for H. influenzae (age <5 years for serotype b, nonserotype b, and unknown serotype) are available in Table I.",
-            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88914,20 +88890,57 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/afja-b25e",
+            "issued": "2017-01-05",
+            "keyword": [
+                "2016",
+                "giardiasis",
+                "gonorrhea",
+                "haemophilus influenzae",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/afja-b25e",
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
+            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1992",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, anabolic steroids, and tobacco<br />\namong members of United States households aged 12 and older. Data are<br />\nalso provided on treatment for drug use and on illegal activities<br />\nrelated to drug use. Questions include age at first use, as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, inhalants, cocaine, hallucinogens, heroin, alcohol, tobacco,<br />\nand nonmedical use of psychotherapeutics. Respondents were also asked<br />\nabout problems resulting from their use of drugs, alcohol, and<br />\ntobacco, their perceptions of the risks involved, insurance coverage,<br />\nand personal and family income sources and amounts. Demographic data<br />\ninclude gender, race, ethnicity, educational level, job status, income<br />\nlevel, household composition, and population density.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1992) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1992-nid13560",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1992-nid13560"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1992-nid13560",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "alcohol consumption",
@@ -88955,89 +88968,89 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1992",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1992-nid13560",
-            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, anabolic steroids, and tobacco<br />\namong members of United States households aged 12 and older. Data are<br />\nalso provided on treatment for drug use and on illegal activities<br />\nrelated to drug use. Questions include age at first use, as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, inhalants, cocaine, hallucinogens, heroin, alcohol, tobacco,<br />\nand nonmedical use of psychotherapeutics. Respondents were also asked<br />\nabout problems resulting from their use of drugs, alcohol, and<br />\ntobacco, their perceptions of the risks involved, insurance coverage,<br />\nand personal and family income sources and amounts. Demographic data<br />\ninclude gender, race, ethnicity, educational level, job status, income<br />\nlevel, household composition, and population density.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-1992)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1992-nid13560",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-1992) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1992-nid13560"
-                }
-            ]
+            "title": "National Household Survey on Drug Abuse (NHSDA-1992)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/jn5c-ypvd",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-07-25",
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
-            "identifier": "cb573493-01ed-531e-9a99-c1197f4db8e0",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_briefType",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/briefType.csv",
-                    "description": "{\"dataset\": \"briefType\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"briefType\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/briefType.csv",
+                    "mediaType": "text/csv",
                     "title": "briefType csv file"
                 }
             ],
+            "identifier": "cb573493-01ed-531e-9a99-c1197f4db8e0",
+            "issued": "2024-07-25",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/jn5c-ypvd",
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
+            "title": "implAuto_briefType"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-online-tuberculosis-information-system-otis",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/tb.html",
+            "description": "<p>The Online Tuberculosis Information System (OTIS) on CDC WONDER contains information on verified tuberculosis (TB) cases reported to the Centers for Disease Control and Prevention (CDC) by state health departments, the District of Columbia and Puerto Rico since 1993. These data were extracted from the CDC national TB surveillance system. OTIS reports case counts, incidence rates, population counts, percentage of cases that completed therapy within 1 year of diagnosis, and percentage of cases tested for drug susceptibility. Data for 22 variables are included in the data set, including: age groups, race / ethnicity, sex, vital status, year reported, state, metropolitan area, several patient risk factors, directly observed therapy, disease verification criteria and multi-drug resistant TB. Each year these data are updated with an additional year of cases plus revisions to cases reported in previous years. OTIS is produced by the U.S. Department of Health and Human Services, Public Health Service, Centers for Disease Control and Prevention (CDC), National Center for HIV/AIDS, viral Hepatitis, STD and TB Prevention (NCHHSTP).</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/tb.html",
+                    "mediaType": "text/html",
+                    "title": "Text"
+                }
+            ],
+            "identifier": "9041abdb-0c6b-4398-bb69-8d7d88df4e5f",
             "issued": "2012-08-03",
-            "temporal": "1993-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "age",
                 "alcohol use",
@@ -89069,65 +89082,35 @@
                 "vital status",
                 "year"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-online-tuberculosis-information-system-otis",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "9041abdb-0c6b-4398-bb69-8d7d88df4e5f",
-            "description": "<p>The Online Tuberculosis Information System (OTIS) on CDC WONDER contains information on verified tuberculosis (TB) cases reported to the Centers for Disease Control and Prevention (CDC) by state health departments, the District of Columbia and Puerto Rico since 1993. These data were extracted from the CDC national TB surveillance system. OTIS reports case counts, incidence rates, population counts, percentage of cases that completed therapy within 1 year of diagnosis, and percentage of cases tested for drug susceptibility. Data for 22 variables are included in the data set, including: age groups, race / ethnicity, sex, vital status, year reported, state, metropolitan area, several patient risk factors, directly observed therapy, disease verification criteria and multi-drug resistant TB. Each year these data are updated with an additional year of cases plus revisions to cases reported in previous years. OTIS is produced by the U.S. Department of Health and Human Services, Public Health Service, Centers for Disease Control and Prevention (CDC), National Center for HIV/AIDS, viral Hepatitis, STD and TB Prevention (NCHHSTP).</p>",
-            "title": "CDC WONDER: Online Tuberculosis Information System (OTIS)",
-            "programCode": [
-                "009:027"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://wonder.cdc.gov/tb.html",
-                    "mediaType": "text/html",
-                    "title": "Text"
-                }
-            ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/tb.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1993-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Online Tuberculosis Information System (OTIS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/telemedicine-use.htm",
+            "accrualPeriodicity": "R/P2W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-04-27",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-08-19/2022-07-11",
-            "modified": "2023-04-14",
-            "keyword": [
-                "covid-19",
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
-            "identifier": "https://data.cdc.gov/api/views/h7xa-837u",
             "description": "To rapidly monitor recent changes in the use of telemedicine, the National Center for Health Statistics (NCHS) and the Health Resources and Services Administration\u2019s Maternal and Child Health Bureau (HRSA MCHB) partnered with the Census Bureau on an experimental data system called the Household Pulse Survey. This 20-minute online survey was designed to complement the ability of the federal statistical system to rapidly respond and provide relevant information about the impact of the coronavirus pandemic in the U.S.\n\nThe U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of the COVID-19 pandemic on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, sex, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
-            "title": "Telemedicine Use in the Last 4 Weeks",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89150,46 +89133,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/h7xa-837u",
+            "issued": "2021-04-27",
+            "keyword": [
+                "covid-19",
+                "telemedicine"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/telemedicine-use.htm",
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
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
+            "temporal": "2020-08-19/2022-07-11",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Telemedicine Use in the Last 4 Weeks"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adult-coverage-vaccination.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-07",
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
-            "identifier": "https://data.cdc.gov/api/views/hm35-qkiu",
             "description": "Weekly COVID-19 Vaccination Coverage of Adults 18 Years and Older by Demographic Characteristics \n\n\u2022 COVID-19 vaccination coverage among adults 18 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly COVID-19 vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n \n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine for adults ages 18 years and older.",
-            "title": "Cumulative Percentage of Adults 18 Years and Older Vaccinated with the Updated 2023-24 COVID-19 Vaccine",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89212,48 +89194,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/hm35-qkiu",
+            "issued": "2023-11-07",
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
+            "title": "Cumulative Percentage of Adults 18 Years and Older Vaccinated with the Updated 2023-24 COVID-19 Vaccine"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/nis/",
+            "accrualPeriodicity": "Approximately Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-03-28",
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
-            "identifier": "https://data.cdc.gov/api/views/3myw-4j4q",
             "description": "Cumulative Influenza Vaccination Coverage Age Group, Race/Ethnicity, and Jurisdiction, Adults 18 Years and Older, United States, National Immunization Survey Adult COVID Module.\n\nArchived data are available including for Figures 4B and 4C:  https://data.cdc.gov/resource/8dyx-9z99 \n\n\u2022  The National Immunization Survey-Adult COVID Module (NIS-ACM) was launched in April 2021 among adults 18 years and older. The survey was used to monitor COVID-19 vaccination uptake and confidence in vaccination among adults and included questions about influenza vaccination.",
-            "title": "Cumulative Influenza Vaccination Coverage by Race/Ethnicity and Age Group, NIS-ACM",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89276,47 +89256,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/3myw-4j4q",
+            "issued": "2023-03-28",
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
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-03-28",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "spatial": "United States, District of Columbia, US Virgin Islands, and Puerto Rico",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Approximately Monthly",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Cumulative Influenza Vaccination Coverage by Race/Ethnicity and Age Group, NIS-ACM"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/jpaz-yhdx",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-14",
-            "keyword": [
-                "py2024",
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
-            "identifier": "77bae5d1-43da-4348-9679-82b7d1ce3eb8",
             "description": "The Medical SHOP Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2024 Medical SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89324,48 +89305,39 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "77bae5d1-43da-4348-9679-82b7d1ce3eb8",
+            "issued": "2024-08-06",
+            "keyword": [
+                "py2024",
+                "qhp",
+                "qhp landscape instructions",
+                "shop",
+                "shop market medical"
+            ],
+            "landingPage": "https://healthdata.gov/d/jpaz-yhdx",
+            "modified": "2024-08-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2024 Medical SHOP"
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
-                "census tract",
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
-            "identifier": "https://data.cdc.gov/api/views/cwsq-ngmh",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh",
             "description": "This dataset contains model-based census tract estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 40 measures: 12 for health outcomes, 7 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, 3 for health status, and 7 for health-related social needs. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2022 or 2021 data, Census Bureau 2020 population data, and American Community Survey 2018\u20132022 estimates. The 2024 release uses 2022 BRFSS data for 36 measures and 2021 BRFSS data for 4 measures (high blood pressure, high cholesterol, cholesterol screening, and taking medicine for high blood pressure control among those with high blood pressure) that the survey collects data on every other year. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, Census Tract Data 2024 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89388,46 +89360,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh",
+            "identifier": "https://data.cdc.gov/api/views/cwsq-ngmh",
+            "issued": "2024-08-23",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "census tract",
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
+            "title": "PLACES: Local Data for Better Health, Census Tract Data 2024 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/qvzb-qs6p",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-22",
-            "keyword": [
-                "abcs",
-                "active bacterial core surveillance",
-                "bactfacts",
-                "invasive pneumococcal disease serotypes",
-                "ipd serotype frequencies",
-                "ipd serotypes",
-                "spn serotypes",
-                "streptococcus pneumoniae serotypes"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Active Bacterial Core Surveillance",
                 "hasEmail": "mailto:abcs@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/qvzb-qs6p",
             "description": "CDC monitors invasive bacterial infections that cause bloodstream infections, sepsis, and meningitis in persons living in the community through Active Bacterial Core surveillance (ABCs). ABCs conducts laboratory- and population-based surveillance for invasive pneumococcal disease (IPD). ABCs serotype data are used to measure the impact of vaccine use in the United States on vaccine-type IPD. \n\nThis table reports IPD case counts in the ABCs catchment area by serotype for years 1998 through 2022. Cases are grouped into the following mutually exclusive age groups: age <2 years old, age 2\u20134 years old, age 5\u201317 years old, age 18\u201349 years old, age 50\u201364 years old, and age \u226565 years old.\n\nABCs methods and surveillance areas reporting IPD cases has changed over time. Given these changes, trends in serotype distribution by year and age group should be interpreted with caution. Additional information on ABCs methods and surveillance population is available at <a href=\"https://www.cdc.gov/abcs/methodology/index.html\">https://www.cdc.gov/abcs/methodology/index.html</a>.\n\nAnalyze and visualize data using the ABCs Bact Facts Interactive Data Dashboard at <a href=\"https://www.cdc.gov/abcs/bact-facts/data-dashboard.html?CDC_AAref_Val=https://www.cdc.gov/abcs/bact-facts-interactive-dashboard.html\">https://www.cdc.gov/abcs/bact-facts-interactive-dashboard</a>.",
-            "title": "1998-2022 Serotype Data for Invasive Pneumococcal Disease Cases by Age Group from Active Bacterial Core surveillance",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89450,39 +89427,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qvzb-qs6p",
+            "issued": "2023-05-30",
+            "keyword": [
+                "abcs",
+                "active bacterial core surveillance",
+                "bactfacts",
+                "invasive pneumococcal disease serotypes",
+                "ipd serotype frequencies",
+                "ipd serotypes",
+                "spn serotypes",
+                "streptococcus pneumoniae serotypes"
+            ],
+            "landingPage": "https://data.cdc.gov/d/qvzb-qs6p",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-07-22",
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
+            "title": "1998-2022 Serotype Data for Invasive Pneumococcal Disease Cases by Age Group from Active Bacterial Core surveillance"
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
@@ -89490,24 +89473,50 @@
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Cessation Coverage"
-            ]
+            ],
+            "title": "Medicaid Coverage Of Cessation Treatments And Barriers To Treatments Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/non-federal-acute-care-hospital-health-it-adoption-and-use",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2021-12-01",
-            "references": [
-                "https://www.healthit.gov/data/apps/non-federal-acute-care-hospital-health-it-adoption-and-use",
-                "https://www.healthit.gov/data/quickstats/non-federal-acute-care-hospital-electronic-health-record-adoption"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/non-federal-acute-care-hospital-health-it-adoption-and-use",
+            "description": "The adoption and use of electronic health records is a key ONC priority. This page provides data access and documentation for the non-federal acute care hospital EHR adoption and use open data. These data include measures for electronic health record (EHR) adoption, patient health information exchange, including measures of interoperable exchange, and patient engagement capabilities.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/aha.csv",
+                    "mediaType": "text/csv",
+                    "title": "aha.csv"
+                }
             ],
+            "identifier": "4ace2vzk-eulv-7lnl-xxcj-kg2k8iivmu6m",
+            "issued": "2023-10-03",
             "keyword": [
                 "adoption",
                 "health care facilities",
@@ -89517,58 +89526,34 @@
                 "patient engagement",
                 "patient information"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/non-federal-acute-care-hospital-health-it-adoption-and-use",
+            "modified": "2021-12-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "4ace2vzk-eulv-7lnl-xxcj-kg2k8iivmu6m",
-            "description": "The adoption and use of electronic health records is a key ONC priority. This page provides data access and documentation for the non-federal acute care hospital EHR adoption and use open data. These data include measures for electronic health record (EHR) adoption, patient health information exchange, including measures of interoperable exchange, and patient engagement capabilities.",
-            "title": "Non-federal Acute Care Hospital Health IT Adoption and Use",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/aha.csv",
-                    "mediaType": "text/csv",
-                    "title": "aha.csv"
-                }
+            "references": [
+                "https://www.healthit.gov/data/apps/non-federal-acute-care-hospital-health-it-adoption-and-use",
+                "https://www.healthit.gov/data/quickstats/non-federal-acute-care-hospital-electronic-health-record-adoption"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/non-federal-acute-care-hospital-health-it-adoption-and-use"
+            "title": "Non-federal Acute Care Hospital Health IT Adoption and Use"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/jrc9-essi",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-07-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-03",
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
-            "identifier": "325529aa-89b0-4892-913f-4515e4db1355",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-06-26-to-2023-07-02",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89577,45 +89562,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-06-26-to-2023-07-02"
                 }
             ],
+            "identifier": "325529aa-89b0-4892-913f-4515e4db1355",
+            "issued": "2023-07-05",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/jrc9-essi",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-07-03",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-06-26-to-2023-07-02"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kp49-9dp8",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-03-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-30",
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
-            "identifier": "https://data.cdc.gov/api/views/kp49-9dp8",
             "description": "State and territorial executive orders, administrative orders, resolutions, and proclamations are collected from government websites and cataloged and coded using Microsoft Excel by one coder with one or more additional coders conducting quality assurance.\n\nData were collected to determine when bars in states and territories were subject to closing and reopening requirements through executive orders, administrative orders, resolutions, and proclamations for COVID-19. Data can be used to determine when bars in states and territories were subject to closing and reopening requirements through executive orders, administrative orders, resolutions, and proclamations for COVID-19. Data consists exclusively of state and territorial orders, many of which apply to specific counties within their respective state or territory; therefore, data is broken down to the county level.\n\nThese data are derived from publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly close or reopen bars found by the CDC, COVID-19 Community Intervention & Critical Populations Task Force, Monitoring & Evaluation Team, Mitigation Policy Analysis Unit, and the CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 11, 2020 through May 31, 2021.  These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded; news media reports on restrictions were excluded. Recommendations not included in an order are not included in these data. Effective and expiration dates were coded using only the date provided; no distinction was made based on the specific time of the day the order became effective or expired. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
-            "title": "U.S. State and Territorial Orders Closing and Reopening Bars Issued from March 11, 2020 through May 31, 2021 by County by Day",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89638,72 +89613,80 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kp49-9dp8",
+            "issued": "2022-03-30",
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
+            "landingPage": "https://data.cdc.gov/d/kp49-9dp8",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-01-30",
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
+            "title": "U.S. State and Territorial Orders Closing and Reopening Bars Issued from March 11, 2020 through May 31, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.beiresources.org/",
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
                 "fn": "Yao, Alison",
                 "hasEmail": "mailto:yaoal@niaid.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "1f97b8dc-27ee-4ef1-b54c-d160a7d053b6",
+            "dataQuality": true,
             "description": "<p>BEI Resources provides reagents, tools and information for studying Category A, B, and C priority pathogens, emerging infectious disease agents, non-pathogenic microbes and other microbiological materials of relevance to the research community.</p>",
-            "title": "BEI Resource Repository",
+            "identifier": "1f97b8dc-27ee-4ef1-b54c-d160a7d053b6",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.beiresources.org/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:028"
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
+            "title": "BEI Resource Repository"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hauf-e9a4",
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
-            "identifier": "https://data.cdc.gov/api/views/hauf-e9a4",
             "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2014 national data: National Occupant Protection Use Survey (NOPUS), 2014.  Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 state data: Seat Belt Use in 2014- Use Rates in the States and Territories",
-            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 3 - Philadelphia",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89726,38 +89709,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hauf-e9a4",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hauf-e9a4",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 3 - Philadelphia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/jsqz-id25",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-03-02",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-28",
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
-            "identifier": "139ad317-b64b-4db4-b76b-3eff03fc7abd",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-02-21 to 2022-02-27",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89765,43 +89750,35 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "139ad317-b64b-4db4-b76b-3eff03fc7abd",
+            "issued": "2022-03-02",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/jsqz-id25",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2022-02-28",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-02-21 to 2022-02-27"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -89824,46 +89801,45 @@
                     "mediaType": "application/xml"
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-02-22",
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
+            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/a9xa-yrhn",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "hansen's disease",
-                "hantavirus infection",
-                "hantavirus pulmonary syndrome",
-                "nedss",
-                "netss",
-                "nndss",
-                "non-hantavirus pulmonary syndrome",
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
-            "identifier": "https://data.cdc.gov/api/views/a9xa-yrhn",
             "description": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Includes data for old world hantavirus infections, such as Seoul virus infections. Prior to 2015, this condition was not nationally notifiable and data for this condition was not submitted to CDC's National Notifiable Diseases Surveillance System (NNDSS).\n\u00b6 Includes data for Andes virus infections.",
-            "title": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89886,40 +89862,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/a9xa-yrhn",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "hansen's disease",
+                "hantavirus infection",
+                "hantavirus pulmonary syndrome",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-hantavirus pulmonary syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/a9xa-yrhn",
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
+            "title": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://fdanj.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2019-08-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "api",
-                "fda",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/cpdk-v8cd",
             "description": "A digital archive of the published federal notices of judgment (a summary of the final outcome of a court case) for manufacturers and products prosecuted under authority of the 1906 Pure Food and Drug Act (https://fdanj.nlm.nih.gov/)",
-            "title": "FDA Notices of Judgment Collection, 1908-1966",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89942,23 +89924,65 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/cpdk-v8cd",
+            "issued": "2019-08-22",
+            "keyword": [
+                "api",
+                "fda",
+                "history of medicine"
+            ],
+            "landingPage": "https://fdanj.nlm.nih.gov/",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-04",
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
+            "title": "FDA Notices of Judgment Collection, 1908-1966"
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
+            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/Behavioral-Risk-Factor-Data-Tobacco-Use-2010-And-P/fpp2-pp25",
+            "description": "1996-2010. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  BRFSS Survey Data.  The BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. The data for the STATE System were extracted from the annual BRFSS surveys from participating states.  Tobacco topics included are cigarette smoking status, cigarette smoking prevalence by demographics, cigarette smoking frequency, and quit attempts.  NOTE:  these data are not to be compared with BRFSS data collected 2011 and forward, as the methodologies were changed.  Please refer to the FAQs / Methodology sections for more details.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fpp2-pp25",
+            "issued": "2025-01-31",
             "keyword": [
                 "adult",
                 "age",
@@ -89992,98 +90016,46 @@
                 "tobacco",
                 "tobacco use"
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
-            "identifier": "https://data.cdc.gov/api/views/fpp2-pp25",
-            "description": "1996-2010. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  BRFSS Survey Data.  The BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. The data for the STATE System were extracted from the annual BRFSS surveys from participating states.  Tobacco topics included are cigarette smoking status, cigarette smoking prevalence by demographics, cigarette smoking frequency, and quit attempts.  NOTE:  these data are not to be compared with BRFSS data collected 2011 and forward, as the methodologies were changed.  Please refer to the FAQs / Methodology sections for more details.",
-            "title": "Behavioral Risk Factor Data: Tobacco Use (2010 And Prior)",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
+            "references": [
+                "https://chronicdata.cdc.gov/d/5amh-5sx3"
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/Behavioral-Risk-Factor-Data-Tobacco-Use-2010-And-P/fpp2-pp25",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
             "theme": [
                 "Survey Data"
-            ]
+            ],
+            "title": "Behavioral Risk Factor Data: Tobacco Use (2010 And Prior)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-post-acute-care-hospice/medicare-post-acute-care-and-hospice-by-geography-provider",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-11-03",
-            "temporal": "2022-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-14",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-05/MUP_PAC_RY24_Methodology_2024_508.pdf"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
-                "home health",
-                "hospice",
-                "hospitals & facilities",
-                "inpatient",
-                "long term care",
-                "medicare",
-                "national",
-                "original medicare",
-                "rehabilitation",
-                "states & territories"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PDAG Data Products - OEDA",
                 "hasEmail": "mailto:PDAG_Data_Products@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/fa8caa65-d5c3-492e-be49-835fe42c9190/data-viewer",
-            "description": "The Medicare Post-Acute Care and Hospice Provider Utilization and Payment Public Use Files (PAC PUF) contains information on demographic and clinical characteristics of beneficiaries served, professional and paraprofessional service utilization, and payment information at the provider, state, and national levels for each PAC setting (i.e. HHA, hospices, SNF, IRF, and LTCH). There are additional datasets which can be found as a downloadable report under \u2018Resources', which include information specific to the unique variables (e.g., case-mix groups) for HHAs, SNFs and IRFs.\n\nPlease note the data included may not be representative of a physician\u2019s entire practice. The data are also not intended to indicate the quality of care provided and are not risk-adjusted to account for differences in underlying severity of disease of patient populations.\u00a0\n\nMore information can be found below in the resources section.",
-            "title": "Medicare Post-Acute Care and Hospice - by Geography & Provider",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-05/MUP_PAC_RY24_Data_Dictionary_2024_FINAL.xlsx",
             "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Medicare Post-Acute Care and Hospice Provider Utilization and Payment Public Use Files (PAC PUF) contains information on demographic and clinical characteristics of beneficiaries served, professional and paraprofessional service utilization, and payment information at the provider, state, and national levels for each PAC setting (i.e. HHA, hospices, SNF, IRF, and LTCH). There are additional datasets which can be found as a downloadable report under \u2018Resources', which include information specific to the unique variables (e.g., case-mix groups) for HHAs, SNFs and IRFs.\n\nPlease note the data included may not be representative of a physician\u2019s entire practice. The data are also not intended to indicate the quality of care provided and are not risk-adjusted to account for differences in underlying severity of disease of patient populations.\u00a0\n\nMore information can be found below in the resources section.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fa8caa65-d5c3-492e-be49-835fe42c9190/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fa8caa65-d5c3-492e-be49-835fe42c9190/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Post-Acute Care and Hospice - by Geography & Provider : 2022-01-02"
                 },
                 {
@@ -90099,28 +90071,67 @@
                     "title": "Medicare Post-Acute Care and Hospice - by Geography & Provider : 2022-01-02"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-05/MUP_PAC_RY24_Data_Dictionary_2024_FINAL.xlsx",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/fa8caa65-d5c3-492e-be49-835fe42c9190/data-viewer",
+            "issued": "2022-11-03",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "home health",
+                "hospice",
+                "hospitals & facilities",
+                "inpatient",
+                "long term care",
+                "medicare",
+                "national",
+                "original medicare",
+                "rehabilitation",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-post-acute-care-hospice/medicare-post-acute-care-and-hospice-by-geography-provider",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-05/MUP_PAC_RY24_Methodology_2024_508.pdf"
+            ],
+            "temporal": "2022-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Post-Acute Care and Hospice - by Geography & Provider"
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
@@ -90133,45 +90144,47 @@
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
                 "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://www.healthit.gov/data/datasets/onc-health-information-technology-economic-and-clinical-health-hitech-grantee",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/onc-health-information-technology-economic-and-clinical-health-hitech-grantee",
+            "description": "The Health Information Technology for Economic and Clinical Health (HITECH) Act was passed as part of the American Recovery and Reinvestment Act (ARRA) to invest in the U.S. health IT infrastructure. The Office of the National Coordinator for Health IT (ONC) received over $2 billion of these HITECH funds, which was granted to health and community organizations across the U.S. This crosswalk provides geographic data for the service areas of two of these HITECH programs: the Health IT Regional Extension Centers (REC) Program and the Beacon Communities Program. This data can be linked to program financial and performance data to map and visualize program data. You can access the data in multiple formats below.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/HealthIT_Dashboard_AreaType_Crosswalk.csv",
+                    "mediaType": "text/csv",
+                    "title": "HealthIT_Dashboard_AreaType_Crosswalk.csv"
+                }
+            ],
+            "identifier": "5k0pnwr0-zzo9-pvru-dy7y-29vcs3fudqax",
             "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2014-12-01",
             "keyword": [
                 "american reconstruction and recovery act",
                 "arra",
@@ -90182,61 +90195,30 @@
                 "rec",
                 "regional extension centers"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/onc-health-information-technology-economic-and-clinical-health-hitech-grantee",
+            "modified": "2014-12-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "5k0pnwr0-zzo9-pvru-dy7y-29vcs3fudqax",
-            "description": "The Health Information Technology for Economic and Clinical Health (HITECH) Act was passed as part of the American Recovery and Reinvestment Act (ARRA) to invest in the U.S. health IT infrastructure. The Office of the National Coordinator for Health IT (ONC) received over $2 billion of these HITECH funds, which was granted to health and community organizations across the U.S. This crosswalk provides geographic data for the service areas of two of these HITECH programs: the Health IT Regional Extension Centers (REC) Program and the Beacon Communities Program. This data can be linked to program financial and performance data to map and visualize program data. You can access the data in multiple formats below.",
-            "title": "ONC Health Information Technology for Economic and Clinical Health (HITECH) Grantee Crosswalk",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/HealthIT_Dashboard_AreaType_Crosswalk.csv",
-                    "mediaType": "text/csv",
-                    "title": "HealthIT_Dashboard_AreaType_Crosswalk.csv"
-                }
-            ],
-            "describedBy": "https://www.healthit.gov/data/datasets/onc-health-information-technology-economic-and-clinical-health-hitech-grantee"
+            "title": "ONC Health Information Technology for Economic and Clinical Health (HITECH) Grantee Crosswalk"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adult-coverage-vaccination.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-03",
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
-            "identifier": "https://data.cdc.gov/api/views/pakc-hru3",
             "description": "\u2022 COVID-19 vaccination coverage and intent among adults 18 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly COVID-19 vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine for adults ages 18 years and older.",
-            "title": "Weekly Intent for Vaccination and Cumulative Percentage of Adults 18 Years and Older Vaccinated with Updated 2023-24 COVID-19 Vaccine",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90259,65 +90241,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/pakc-hru3",
+            "issued": "2023-11-03",
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
+            "title": "Weekly Intent for Vaccination and Cumulative Percentage of Adults 18 Years and Older Vaccinated with Updated 2023-24 COVID-19 Vaccine"
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
-            "identifier": "https://data.cdc.gov/api/views/akmt-4qtj",
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2006/akmt-4qtj",
             "description": "2006. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2006",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90340,36 +90303,60 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2006/akmt-4qtj",
+            "identifier": "https://data.cdc.gov/api/views/akmt-4qtj",
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
+            "title": "CDC PRAMStat Data for 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/b6fe-yq88",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division, Chemical and Biological Monitoring Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/b6fe-yq88",
             "description": "A method for measuring PAA vapors in air using impinger sampling and field-portable colorimetric analysis is presented. The capture efficiency of aqueous media in glass and plastic impingers was evaluated when used for PAA vapor sampling. Measurement of PAA was done using a N,N-diethyl-p-phenylenediamine (DPD) colorimetric method with a field portable spectrometer. The linearity of the DPD method was determined for PAA both in-solution and captured from vapor phase using glass or plastic impingers. The Limit of Detection (LOD) for the glass and plastic impinger (0.24 mg/m3 (0.077 mg/L) and 0.28 mg/m3 (0.091 mg/L)), respectively, and Limit of Quantitation (LOQ) (0.79 mg/m3 (0.25 mg/L) and 0.92 mg/m3 (0.30 mg/L) for the glass and plastic impingers, respectively, are below the threshold limit value (TLV) short term exposure limit (STEL) of 1.24 mg/m3 (0.4 ppm) over a 15 minute period. This impinger method allows for a low cost, easy to use, and rapid in-field measurement for occupational exposure to PAA.",
-            "title": "A Field-Portable Colorimetric Method for the Measurement of Peracetic Acid Vapors: A Comparison of Glass and Plastic Impingers",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90377,98 +90364,90 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/b6fe-yq88",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/b6fe-yq88",
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
+            "title": "A Field-Portable Colorimetric Method for the Measurement of Peracetic Acid Vapors: A Comparison of Glass and Plastic Impingers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/jxgy-4c9s",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-12",
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
-            "identifier": "a8647354-7dcb-5949-9582-b40e7a985bef",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt measure_value v2.10.16 (coreset-dev0)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/measure_value.csv",
-                    "description": "CoreSEt measure_value v2.10.16 (coreset-dev0)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt measure_value v2.10.16 (coreset-dev0)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt measure_value v2.10.16 (coreset-dev0)"
                 }
             ],
+            "identifier": "a8647354-7dcb-5949-9582-b40e7a985bef",
+            "issued": "2024-11-13",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/jxgy-4c9s",
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
+            "title": "CoreSEt measure_value v2.10.16 (coreset-dev0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/hospital-service-area",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2015-01-01/2023-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-26",
-            "references": [
-                "https://data.cms.gov/resources/hospital-service-area-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "hospitals & facilities",
-                "inpatient",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/8708ca8b-8636-44ed-8303-724cbfaf78ad/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/hospital-service-area-data-dictionary",
             "description": "The Hospital Service Area data\u00a0is a summary of calendar year Medicare inpatient hospital fee-for-service and Medicare Advantage claims data. It contains number of discharges, total days of care, and total charges summarized by hospital provider number and the ZIP code of the Medicare beneficiary.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Hospital Service Area",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8708ca8b-8636-44ed-8303-724cbfaf78ad/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8708ca8b-8636-44ed-8303-724cbfaf78ad/data",
+                    "mediaType": "text/html",
                     "title": "Hospital Service Area : 2023-01-01"
                 },
                 {
@@ -90580,91 +90559,95 @@
                     "title": "Hospital Service Area : 2015-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/hospital-service-area-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/8708ca8b-8636-44ed-8303-724cbfaf78ad/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "hospitals & facilities",
+                "inpatient",
+                "medicare",
+                "original medicare"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/hospital-service-area",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-07-26",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/hospital-service-area-methodology"
+            ],
+            "temporal": "2015-01-01/2023-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Hospital Service Area"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/jxyn-z54e",
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
-            "identifier": "4804ca61-bb86-564d-83ab-51fcb94f0981",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet measure_value v2.10.64 (coreset-cmsdev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure_value.csv",
-                    "description": "CoreSet measure_value v2.10.64 (coreset-cmsdev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet measure_value v2.10.64 (coreset-cmsdev)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet measure_value v2.10.64 (coreset-cmsdev)"
                 }
             ],
+            "identifier": "4804ca61-bb86-564d-83ab-51fcb94f0981",
+            "issued": "2024-11-13",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/jxyn-z54e",
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
+            "title": "CoreSet measure_value v2.10.64 (coreset-cmsdev)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -90672,38 +90655,40 @@
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2020-02-13",
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
+            "title": "CDC Social Vulnerability Index (SVI) Mapping Dashboard"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/jys3-jbpy",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-18",
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
-            "identifier": "a5c46841-e9c1-4293-bfd3-6e4948a367f2",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-11-2024-to-03-17-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90712,44 +90697,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-11-2024-to-03-17-2024"
                 }
             ],
+            "identifier": "a5c46841-e9c1-4293-bfd3-6e4948a367f2",
+            "issued": "2024-03-27",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/jys3-jbpy",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-03-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-11-2024-to-03-17-2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-visualization/life-expectancy/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2019-06-21",
-            "@type": "dcat:Dataset",
-            "temporal": "2010/2015",
-            "modified": "2022-04-01",
-            "keyword": [
-                "birth",
-                "census tract",
-                "county",
-                "life expectancy",
-                "nchs",
-                "nvss",
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
-            "identifier": "https://data.cdc.gov/api/views/5h56-n989",
             "description": "This dataset includes estimates of U.S. life expectancy at birth by state and census tract for the period 2010-2015 (1). Estimates were produced for 65,662 census tracts, covering the District of Columbia (D.C.) and all states, excluding Maine and Wisconsin, representing 88.7% of all U.S. census tracts (see notes).  These estimates are the result of the collaborative project, \u201cU.S. Small-area Life Expectancy Estimates Project (USALEEP),\u201d between the National Center for Health Statistics (NCHS), the National Association for Public Health Statistics and Information Systems (NAPHSIS), and the Robert Wood Johnson Foundation (RWJF) (2).",
-            "title": "U.S. Life Expectancy at Birth by State and Census Tract - 2010-2015",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90772,42 +90749,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/5h56-n989",
+            "issued": "2019-06-21",
+            "keyword": [
+                "birth",
+                "census tract",
+                "county",
+                "life expectancy",
+                "nchs",
+                "nvss",
+                "state",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/life-expectancy/",
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
+            "temporal": "2010/2015",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "U.S. Life Expectancy at Birth by State and Census Tract - 2010-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "computational biology",
-                "dataset",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jz6b-hbzb",
             "description": "Conserved Domain Database (CDD) is a protein annotation resource that consists of a collection of well-annotated multiple sequence alignment models for ancient domains and full-length proteins.",
-            "title": "Conserved Domain Database (CDD)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90828,39 +90810,41 @@
                     "title": "Access Conserved Domain Database (CCD) via E-utilities API"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jz6b-hbzb",
+            "issued": "2016-08-08",
+            "keyword": [
+                "computational biology",
+                "dataset",
+                "protein"
+            ],
+            "landingPage": "http://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml",
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
+            "title": "Conserved Domain Database (CDD)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm191015.htm",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "cvm",
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
-            "identifier": "e3b58aa4-eb31-406f-a766-1a4f2da87565",
             "description": "The Electronic Animal Drug Product Listing Directory is a directory of all animal drug products that have been listed electronically since June 1, 2009, to comply with changes enacted as part of the FDA Amendments Act of 2007.",
-            "title": "Electronic Animal Drug Product Listing Directory",
-            "programCode": [
-                "009:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90868,39 +90852,36 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "e3b58aa4-eb31-406f-a766-1a4f2da87565",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cvm",
+                "labeling"
+            ],
+            "landingPage": "http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm191015.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1D"
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:004"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Electronic Animal Drug Product Listing Directory"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.ncbi.nlm.nih.gov/bioproject/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-08",
-            "keyword": [
-                "api",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/25yr-g2pr",
             "description": "The BioProject database links to data that have been or will be deposited into archival databases maintained at members of the International Nucleotide Sequence Database Consortium (INSDC, which comprises the DNA DataBank of Japan (DDBJ), the European Nucleotide Archive at European Molecular Biology Laboratory (ENA), and GenBank at the National Center for Biotechnology Information (NCBI)).",
-            "title": "BioProject",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90915,48 +90896,42 @@
                     "title": "Download BioProject Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/25yr-g2pr",
+            "issued": "2016-08-08",
+            "keyword": [
+                "api",
+                "computational biology",
+                "dataset",
+                "genomics"
+            ],
+            "landingPage": "http://www.ncbi.nlm.nih.gov/bioproject/",
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
+            "title": "BioProject"
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
-                "census tract",
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
-            "identifier": "https://data.cdc.gov/api/views/ib3w-k9rq",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
             "description": "This dataset contains model-based census tract level estimates for the PLACES project 2020 release in GIS-friendly format. The PLACES project is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code tabulation Areas (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2018 or 2017 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2014-2018 or 2013-2017 estimates. The 2020 release uses 2018 BRFSS data for 23 measures and 2017 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening). Four measures are based on the 2017 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the census tract 2015 boundary file in a GIS system to produce maps for 27 measures at the census tract level. An ArcGIS Online feature service is also available at https://www.arcgis.com/home/item.html?id=8eca985039464f4d83467b8f6aeb1320 for users to make maps online or to add data to desktop GIS software.",
-            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2020 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90979,43 +90954,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
+            "identifier": "https://data.cdc.gov/api/views/ib3w-k9rq",
+            "issued": "2021-09-29",
+            "keyword": [
+                "behaviors",
+                "census tract",
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
+            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2020 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.hcup-us.ahrq.gov",
             "bureauCode": [
                 "009:33"
             ],
-            "issued": "2022-06-07",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "references": [
-                "https://www.hcup-us.ahrq.gov/datavisualizations/HCUP_Visualization_DataTable_March2021.xlsx"
-            ],
-            "keyword": [
-                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
-                "inpatient trends"
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
-            "identifier": "https://healthdata.gov/api/views/k2dr-3fsc",
+            "describedBy": "https://www.hcup-us.ahrq.gov/datavisualizations/covid-19-inpatient-trends.jsp",
             "description": "The HCUP Visualization of Inpatient Trends in COVID-19 and Other Conditions displays State-specific monthly trends in inpatient stays related to COVID-19 and other conditions, and facilitates comparisons of the number of hospital discharges, the average length of stays, and in-hospital mortality rates across patient/stay characteristics and States. This information is based on the HCUP State Inpatient Databases (SID), starting with 2018 data, plus newer annual and quarterly inpatient data, if and when available.",
-            "title": "HCUP Visualization of Inpatient Trends in COVID-19 and Other Conditions",
-            "programCode": [
-                "009:074"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91024,38 +91005,38 @@
                     "title": "HCUP Visualization of Inpatient Trends in COVID-19 and Other Conditions"
                 }
             ],
-            "describedBy": "https://www.hcup-us.ahrq.gov/datavisualizations/covid-19-inpatient-trends.jsp"
+            "identifier": "https://healthdata.gov/api/views/k2dr-3fsc",
+            "issued": "2022-06-07",
+            "keyword": [
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "inpatient trends"
+            ],
+            "landingPage": "https://www.hcup-us.ahrq.gov",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:074"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
+            },
+            "references": [
+                "https://www.hcup-us.ahrq.gov/datavisualizations/HCUP_Visualization_DataTable_March2021.xlsx"
+            ],
+            "title": "HCUP Visualization of Inpatient Trends in COVID-19 and Other Conditions"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -91078,49 +91059,42 @@
                     "mediaType": "application/xml"
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
                 "Smoking & Tobacco Use"
-            ]
+            ],
+            "title": "BRFSS Prevalence and Trends Data: Tobacco Use - Four Level Smoking Data for 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-03-24",
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
-                "united states",
-                "urbanicity",
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
-            "identifier": "https://data.cdc.gov/api/views/hkhc-f7hg",
             "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nProvisional COVID-19 deaths by urbanicity and week. Deaths are based on the county of occurrence in the United States. Urbanicity is defined as metropolitan and non-metropolitan, based on the 2013 National Center for Health Statistics (NCHS) Urban-Rural Classification Scheme for Counties. Counties are classified as \u201cmetropolitan\u201d if they are large central metro, large fringe metro, medium metro or small metro; and \u201cnon-metropolitan\u201d if micropolitan or non-core.",
-            "title": "Provisional COVID-19 Deaths by Week and Urbanicity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91143,23 +91117,75 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/hkhc-f7hg",
+            "issued": "2021-03-24",
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
+                "urbanicity",
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
+            "title": "Provisional COVID-19 Deaths by Week and Urbanicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/dhcs/drug-use/index.htm",
+            "accrualPeriodicity": "R/P2M",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "The National Hospital Care Survey (NHCS) collects data on patient care in hospital-based settings to describe patterns of health care delivery and utilization in the United States. Settings currently include inpatient and emergency departments (ED). From this collection, the NHCS contributes data that may inform emerging national health threats such as the current opioid public health emergency. The 2022 - 2024 NHCS are not yet fully operational so it is important to note that the data presented here are preliminary and not nationally representative.\n\nThe data are from 24 hospitals submitting inpatient and 24 hospitals submitting ED Uniform Bill (UB)-04 administrative claims from August 1, 2022\u2013July 31, 2024. Even though the data are not nationally representative, they can provide insight into the use of opioids and other overdose drugs. The NHCS data is submitted from various types of hospitals (e.g., general/acute, children\u2019s, etc.) and can show results from a variety of indicators related to drug use, such as overall drug use, comorbidities, and drug and polydrug overdose. NHCS data can also be used to report on patient conditions within the hospital over time.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/gypc-kpgn",
             "issued": "2022-09-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-08-01/2024-07-31",
-            "modified": "2024-11-25",
             "keyword": [
                 "amphetamine",
                 "bed size",
@@ -91190,84 +91216,39 @@
                 "substance use",
                 "tramadol"
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
-            "identifier": "https://data.cdc.gov/api/views/gypc-kpgn",
-            "description": "The National Hospital Care Survey (NHCS) collects data on patient care in hospital-based settings to describe patterns of health care delivery and utilization in the United States. Settings currently include inpatient and emergency departments (ED). From this collection, the NHCS contributes data that may inform emerging national health threats such as the current opioid public health emergency. The 2022 - 2024 NHCS are not yet fully operational so it is important to note that the data presented here are preliminary and not nationally representative.\n\nThe data are from 24 hospitals submitting inpatient and 24 hospitals submitting ED Uniform Bill (UB)-04 administrative claims from August 1, 2022\u2013July 31, 2024. Even though the data are not nationally representative, they can provide insight into the use of opioids and other overdose drugs. The NHCS data is submitted from various types of hospitals (e.g., general/acute, children\u2019s, etc.) and can show results from a variety of indicators related to drug use, such as overall drug use, comorbidities, and drug and polydrug overdose. NHCS data can also be used to report on patient conditions within the hospital over time.",
-            "title": "Drug Use Data from Selected Hospitals",
+            "landingPage": "https://www.cdc.gov/nchs/dhcs/drug-use/index.htm",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-25",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
             "spatial": "US",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2022-08-01/2024-07-31",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Drug Use Data from Selected Hospitals"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/k3v5-ddgt",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "individual",
-                "individual market dental",
-                "py2025",
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
-            "identifier": "c0b5f0c0-87d8-4a3f-b637-b114e482d329",
             "description": "The Dental Individual Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to consumers in the individual market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2025 Individual Dental",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91275,41 +91256,39 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "c0b5f0c0-87d8-4a3f-b637-b114e482d329",
+            "issued": "2024-12-10",
+            "keyword": [
+                "individual",
+                "individual market dental",
+                "py2025",
+                "qhp landscape instructions",
+                "sadp"
+            ],
+            "landingPage": "https://healthdata.gov/d/k3v5-ddgt",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2025 Individual Dental"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual (R/P1Y)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-07-08",
-            "temporal": "1980/2020",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-09",
-            "keyword": [
-                "american hospital association",
-                "community hospital beds",
-                "health us",
-                "hospital",
-                "sdoh-access-to-health-care",
-                "state"
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
-            "identifier": "https://data.cdc.gov/api/views/uiux-mrvg",
             "description": "Data on community hospital beds in the United States, by state. Data are from Health, United States. SOURCE: American Hospital Association (AHA) Annual Survey of Hospitals, Hospital Statistics.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Community hospital beds, by state: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91332,42 +91311,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/uiux-mrvg",
+            "issued": "2024-07-08",
+            "keyword": [
+                "american hospital association",
+                "community hospital beds",
+                "health us",
+                "hospital",
+                "sdoh-access-to-health-care",
+                "state"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual (R/P1Y)",
+            "modified": "2024-09-09",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "1980/2020",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "DQS Community hospital beds, by state: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/AboutFDA/FDAAcronymsAbbreviations/default.htm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2012-04-04",
-            "references": [
-                "http://www.accessdata.fda.gov/scripts/cder/acronyms/index.cfm"
-            ],
-            "keyword": [
-                "definitions"
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
-            "identifier": "4dc9ed1a-1287-40e5-9c14-41011aac1308",
             "description": "The FDA Acronyms and Abbreviations database provides a quick reference to acronyms and abbreviations related to Food and Drug Administration (FDA) activities",
-            "title": "FDA Acronyms and Abbreviations",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91375,89 +91356,84 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "4dc9ed1a-1287-40e5-9c14-41011aac1308",
+            "issued": "2021-02-25",
+            "keyword": [
+                "definitions"
+            ],
+            "landingPage": "http://www.fda.gov/AboutFDA/FDAAcronymsAbbreviations/default.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2012-04-04",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.accessdata.fda.gov/scripts/cder/acronyms/index.cfm"
+            ],
+            "title": "FDA Acronyms and Abbreviations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/k4gi-7y87",
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
-            "identifier": "de0dc5a3-76a0-5531-a07d-282c9404173b",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt pillar v2.10.22 (coreset-impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/pillar.csv",
-                    "description": "CoreSEt pillar v2.10.22 (coreset-impl)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt pillar v2.10.22 (coreset-impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt pillar v2.10.22 (coreset-impl)"
                 }
             ],
+            "identifier": "de0dc5a3-76a0-5531-a07d-282c9404173b",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/k4gi-7y87",
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
+            "title": "CoreSEt pillar v2.10.22 (coreset-impl)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mkns-9vjv",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mkns-9vjv",
             "description": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91480,41 +91456,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mkns-9vjv",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/mkns-9vjv",
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
+            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/d3c4-tq79",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2018-06-15",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-27",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/d3c4-tq79",
             "description": "This dataset provides modeled predictions of ozone levels from the EPA's Downscaler model. Data are at the census tract level for 2001-2005. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\r\n\r\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily Census Tract-Level Ozone Concentrations, 2001-2005",
-            "programCode": [
-                "009:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91537,38 +91518,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/d3c4-tq79",
+            "issued": "2018-06-15",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "ozone"
+            ],
+            "landingPage": "https://data.cdc.gov/d/d3c4-tq79",
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
+            "title": "Daily Census Tract-Level Ozone Concentrations, 2001-2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/k5s7-ii8g",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-07-13",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-18",
-            "keyword": [
-                "enrollment strategies"
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
-            "identifier": "601a8897-1453-5282-81cd-be49d7ec7503",
             "description": "States may rely on eligibility information from \"Express Lane\" agency programs to streamline and simplify enrollment and renewal in Medicaid and CHIP. Express Lane agencies may include Supplemental Nutrition Assistance Program (SNAP), School Lunch programs, Temporary Assistance for Needy Families, Head Start, and the Women, infant, and children's program (WIC) , among others. States can also use state income tax data to determine Medicaid and CHIP eligibility for children.",
-            "title": "Express Lane Eligibility for Medicaid and CHIP Coverage",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91577,50 +91562,39 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "601a8897-1453-5282-81cd-be49d7ec7503",
+            "issued": "2016-07-13",
+            "keyword": [
+                "enrollment strategies"
+            ],
+            "landingPage": "https://healthdata.gov/d/k5s7-ii8g",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2019-01-18",
+            "programCode": [
+                "009:076"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "Eligibility"
-            ]
+            ],
+            "title": "Express Lane Eligibility for Medicaid and CHIP Coverage"
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
-            "@type": "dcat:Dataset",
-            "temporal": "2015/2020",
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
-                "yearly"
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
-            "identifier": "https://data.cdc.gov/api/views/chcz-j2du",
             "description": "Death counts by age and sex for years 2015-2020. Data for 2015-2019 are final. Data for 2020 are provisional.",
-            "title": "AH Deaths by Year, Sex, and Age for 2015-2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91643,47 +91617,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/chcz-j2du",
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
+                "yearly"
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
+            "spatial": "United States",
+            "temporal": "2015/2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Deaths by Year, Sex, and Age for 2015-2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mbsb-z5f8",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "all ages",
-                "invasive pneumococcal diseases",
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
-            "identifier": "https://data.cdc.gov/api/views/mbsb-z5f8",
             "description": "NNDSS - Table II. Invasive Pneumococcal Diseases, All Ages - 2017. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease. This condition was previously named Streptococcus pneumoniae invasive disease and cases were reported to CDC using different event codes to specify whether the cases were drug resistant or in a defined age group, such as <5 years.",
-            "title": "NNDSS - Table II. Invasive Pneumococcal Diseases, All Ages",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91706,40 +91683,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mbsb-z5f8",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "all ages",
+                "invasive pneumococcal diseases",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mbsb-z5f8",
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
+            "title": "NNDSS - Table II. Invasive Pneumococcal Diseases, All Ages"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/k65v-ain7",
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
-            "identifier": "ae4d5347-5137-5f6c-b66c-3420fa0316d8",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 1991",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91747,36 +91730,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "ae4d5347-5137-5f6c-b66c-3420fa0316d8",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/k65v-ain7",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
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
+            "title": "State Drug Utilization Data 1991"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ujph-mgrh",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Spokane Mining Research Division\u2014Miner Health Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ujph-mgrh",
             "description": "The National Health Interview Survey (NHIS) is an annual cross-sectional survey that collects information on a broad range of health topics; it was developed by the National Center for Health Statistics (NCHS) and is currently administered by the U.S. Census Bureau. NHIS datasets for the years 2007\u20132018 were combined to ensure an adequate sample size to study currently working male miners. During 2007\u20132018, the NHIS included four core modules. The Family and Sample Adult core modules were used in the study. The Family core module collected health and sociodemographic information on each member of each family within the household. The Sample Adult core module collected health and industry and occupation information for the randomly chosen sample adult from each household interviewed.",
-            "title": "Health conditions among male workers in mining and other industries reliant on manual labor occupations: National Health Interview Survey, 2007\u20132018",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91784,52 +91771,44 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ujph-mgrh",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/ujph-mgrh",
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
+            "title": "Health conditions among male workers in mining and other industries reliant on manual labor occupations: National Health Interview Survey, 2007\u20132018"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/quality-of-care/payroll-based-journal-daily-non-nurse-staffing",
-            "bureauCode": [
-                "009:38"
-            ],
-            "issued": "2021-12-22",
-            "temporal": "2017-01-01/2024-06-30",
             "@type": "dcat:Dataset",
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
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "009:38"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nursing Home Staffing - CCSQ (PBJ Reports)",
                 "hasEmail": "mailto:nhstaffing@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/b497431a-5b57-42c0-9016-90105b51841e/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/payroll-based-journal-daily-non-nurse-staffing-data-dictionary",
             "description": "The Payroll Based Journal (PBJ) Nurse Staffing and Non-Nurse Staffing datasets provide information submitted by nursing homes including rehabilitation services on a quarterly basis. The data include the hours staff are paid to work each day, for each facility. Examples of reporting categories include Director of Nursing, Administrative Registered Nurses, Registered Nursing, Administrative Licensed Practice Nurses, Licensed Practice Nurses, Certified Nurse Aides, Certified Medication Aides, and Nurse Aides in Training. There are also other non-nurse staff categories provided in the data such as Respiratory Therapist, Occupational Therapist, and Social Worker. The datasets also include a facility\u2019s daily census calculated using the Minimum Data Set (MDS) submission.\n\nThe Payroll Based Journal (PBJ) Employee Detail Nursing Home Staffing datasets and technical information have been moved to a new location.\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Payroll Based Journal Daily Non-Nurse Staffing",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b497431a-5b57-42c0-9016-90105b51841e/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b497431a-5b57-42c0-9016-90105b51841e/data",
+                    "mediaType": "text/html",
                     "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2024-04-01"
                 },
                 {
@@ -92193,52 +92172,50 @@
                     "title": "Payroll Based Journal Daily Non-Nurse Staffing : 2017-03-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/payroll-based-journal-daily-non-nurse-staffing-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/b497431a-5b57-42c0-9016-90105b51841e/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "hospitals & facilities",
+                "medicare",
+                "original medicare",
+                "skilled nursing"
+            ],
+            "landingPage": "https://data.cms.gov/quality-of-care/payroll-based-journal-daily-non-nurse-staffing",
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
+            "title": "Payroll Based Journal Daily Non-Nurse Staffing"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive.html",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-01-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-01-24",
-            "keyword": [
-                "covid-19",
-                "covid-19 vaccination",
-                "immunization",
-                "nis-ccm",
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
-            "identifier": "https://data.cdc.gov/api/views/s5a6-fn5p",
             "description": "National Immunization Survey Child COVID Module (NIS-CCM): CDC is providing information on COVID-19 vaccine uptake and confidence. These data represent trends in vaccination status and intent, and other behavioral indicators, by demographics and other characteristics.",
-            "title": "National Immunization Survey Child COVID Module (NIS-CCM): COVIDVaxViews| Data | Centers for Disease Control and Prevention (cdc.gov)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92261,44 +92238,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "National",
+            "identifier": "https://data.cdc.gov/api/views/s5a6-fn5p",
+            "issued": "2024-01-16",
+            "keyword": [
+                "covid-19",
+                "covid-19 vaccination",
+                "immunization",
+                "nis-ccm",
+                "vaccination",
+                "vaccination coverage",
+                "vaccine confidence",
+                "vaxviews"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2024-01-24",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "National",
+            "temporal": "2023-2024",
             "theme": [
                 "Child Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "National Immunization Survey Child COVID Module (NIS-CCM): COVIDVaxViews| Data | Centers for Disease Control and Prevention (cdc.gov)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4tmr-eik2",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-01-28",
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
-            "identifier": "https://data.cdc.gov/api/views/4tmr-eik2",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "CDC Best Practices for Comprehensive Tobacco Control Programs - 2014 Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92306,40 +92289,39 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4tmr-eik2",
+            "issued": "2015-01-28",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "https://data.cdc.gov/d/4tmr-eik2",
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
+            "title": "CDC Best Practices for Comprehensive Tobacco Control Programs - 2014 Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://learn.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-06-29",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "keyword": [
-                "education",
-                "training and instruction",
-                "videos"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/khy6-95gu",
             "description": "The Learning Resources Database is a catalog of interactive tutorials, videos, online classes, finding aids, and other instructional resources on National Library of Medicine (NLM) products and services. Resources may be available for immediate use via a browser or downloadable for use in course management systems.",
-            "title": "Learning Resources Database",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92362,35 +92344,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/khy6-95gu",
+            "issued": "2022-06-29",
+            "keyword": [
+                "education",
+                "training and instruction",
+                "videos"
+            ],
+            "landingPage": "https://learn.nlm.nih.gov/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-31",
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
+            "title": "Learning Resources Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/8vj7-uiam",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -92398,59 +92385,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8vj7-uiam",
+            "issued": "2024-12-05",
+            "landingPage": "https://data.cdc.gov/d/8vj7-uiam",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-05",
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
+            "title": "Characterizing dynamic atmosphere generation system performance for analytical method development"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -92473,51 +92437,63 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://ephtracking.cdc.gov/DataExplorer/#/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-03-08",
-            "@type": "dcat:Dataset",
-            "temporal": "2016-2020",
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -92540,24 +92516,61 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S. states",
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-03-08",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "U.S. states",
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
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2006",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2006) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-nid13581",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-nid13581"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-nid13581",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -92570,66 +92583,29 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2006",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-nid13581",
-            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2006)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-nid13581",
-                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2006) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-nid13581"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2006)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://ephtracking.cdc.gov/DataExplorer/#/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-09-19",
-            "@type": "dcat:Dataset",
-            "temporal": "2001-2019",
-            "modified": "2023-09-19",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/dqwm-pbi7",
             "description": "This dataset provides modeled predictions of PM2.5 levels from the EPA's Downscaler model. Data are at the county level for 2001-2019. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\n\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\n\nBy using these data, you signify your agreement to comply with the following requirements:\n1. Use the data for statistical reporting and analysis only.\n2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals.\n3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov.\n4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.\n5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC.\n6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily County-Level PM2.5 Concentrations, 2001-2019",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92652,42 +92628,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S. states",
+            "identifier": "https://data.cdc.gov/api/views/dqwm-pbi7",
+            "issued": "2023-09-19",
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-09-19",
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
-            ]
+            ],
+            "title": "Daily County-Level PM2.5 Concentrations, 2001-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kbtb-47jc",
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
-                "py2022",
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
-            "identifier": "0a973ff8-9926-49c5-91e1-ee6c9c1288e1",
             "description": "The Service Area PUF (SA-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The SA-PUF contains issuer-level data on geographic service areas including state, county, and zip code.",
-            "title": "Service Area PUF \u2013 PY2022",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92695,49 +92677,38 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "0a973ff8-9926-49c5-91e1-ee6c9c1288e1",
+            "issued": "2022-08-10",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2022",
+                "service area"
+            ],
+            "landingPage": "https://healthdata.gov/d/kbtb-47jc",
+            "modified": "2022-08-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Service Area PUF \u2013 PY2022"
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
-                "city",
-                "disability",
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
-            "identifier": "https://data.cdc.gov/api/views/krqc-563j",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
             "description": "This dataset contains model-based place (incorporated and census-designated places) estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 36 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population data, and American Community Survey 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. More information about the methodology can be found at  www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, Place Data 2023 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92760,42 +92731,53 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
+            "identifier": "https://data.cdc.gov/api/views/krqc-563j",
+            "issued": "2024-07-15",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "city",
+                "disability",
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
+            "title": "PLACES: Local Data for Better Health, Place Data 2023 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kdeq-n7js",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-12-16",
-            "@type": "dcat:Dataset",
-            "modified": "2021-12-22",
-            "keyword": [
-                "exchange puf",
-                "machine readable",
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
-            "identifier": "6044cb77-5350-4ffc-908e-5c9283da5056",
             "description": "The Machine Readable PUF (MR-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The MR-PUF contains issuer-level URL locations for machine-readable network provider and formulary information.",
-            "title": "Machine Readable PUF - PY2022",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92803,37 +92785,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "6044cb77-5350-4ffc-908e-5c9283da5056",
+            "issued": "2021-12-16",
+            "keyword": [
+                "exchange puf",
+                "machine readable",
+                "marketplace puf",
+                "py2022"
+            ],
+            "landingPage": "https://healthdata.gov/d/kdeq-n7js",
+            "modified": "2021-12-22",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Machine Readable PUF - PY2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kduu-h3ai",
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
                 "hasEmail": "mailto:no-reply@data.medicaid.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "5b10a5b4-dabe-5419-99d8-043df47b8e4b",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2005",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92841,43 +92824,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "5b10a5b4-dabe-5419-99d8-043df47b8e4b",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/kduu-h3ai",
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
+            "title": "State Drug Utilization Data 2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pss.cfm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-01",
-            "references": [
-                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/PostmarketRequirements/PostmarketSurveillance/ucm134497.htm",
-                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/GuidanceDocuments/ucm268064.htm"
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
-            "identifier": "3d55fceb-5248-4475-b675-503312202d0d",
             "description": "The 522 Postmarket Surveillance Studies Program encompasses design, tracking, oversight, and review responsibilities for studies mandated under section 522 of the Federal Food, Drug and Cosmetic Act. The program helps ensure that well-designed 522 postmarket surveillance (PS) studies are conducted effectively and efficiently and in the least burdensome manner.",
-            "title": "522 Postmarket Surveillance Studies",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92885,43 +92865,39 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "3d55fceb-5248-4475-b675-503312202d0d",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pss.cfm",
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
+                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/PostmarketRequirements/PostmarketSurveillance/ucm134497.htm",
+                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/GuidanceDocuments/ucm268064.htm"
+            ],
+            "title": "522 Postmarket Surveillance Studies"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -92944,40 +92920,47 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis"
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
-                "mental health"
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
-            "identifier": "https://data.cdc.gov/api/views/yni7-er2q",
             "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, gender, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
-            "title": "Mental Health Care in the Last 4 Weeks",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93000,25 +92983,55 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/yni7-er2q",
+            "issued": "2020-09-23",
+            "keyword": [
+                "covid-19",
+                "mental health"
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
+                "name": "Centers for Disease Control and Prevention"
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
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-2000",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Household Survey on Drug Abuse (NHSDA) series<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions include age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovers substance abuse treatment history and perceived need for<br />\ntreatment, and includes questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. Respondents are also asked about personal and family income<br />\nsources and amounts, health care access and coverage, illegal<br />\nactivities and arrest record, problems resulting from the use of<br />\ndrugs, and needle-sharing. Questions introduced in previous NHSDA<br />\nadministrations were retained in the 2000 survey, including questions<br />\nasked only of respondents aged 12 to 17. These \"youth experiences\"<br />\nitems covered a variety of topics, such as neighborhood environment,<br />\nillegal activities, gang involvement, drug use by friends, social<br />\nsupport, extracurricular activities, exposure to substance abuse<br />\nprevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Also retained were<br />\nquestions on mental health and access to care, perceived risk of using<br />\ndrugs, perceived availability of drugs, driving behavior and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey and retained in the 2000<br />\nsurvey. Demographic data include gender, race, age, ethnicity, marital<br />\nstatus, educational level, job status, veteran status, and current<br />\nhousehold composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-2000) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2000-nid13562",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2000-nid13562"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2000-nid13562",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -93050,66 +93063,29 @@
                 "substance abuse treatment",
                 "tranquilizers"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-2000",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2000-nid13562",
-            "description": "<p>The National Household Survey on Drug Abuse (NHSDA) series<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions include age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovers substance abuse treatment history and perceived need for<br />\ntreatment, and includes questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. Respondents are also asked about personal and family income<br />\nsources and amounts, health care access and coverage, illegal<br />\nactivities and arrest record, problems resulting from the use of<br />\ndrugs, and needle-sharing. Questions introduced in previous NHSDA<br />\nadministrations were retained in the 2000 survey, including questions<br />\nasked only of respondents aged 12 to 17. These \"youth experiences\"<br />\nitems covered a variety of topics, such as neighborhood environment,<br />\nillegal activities, gang involvement, drug use by friends, social<br />\nsupport, extracurricular activities, exposure to substance abuse<br />\nprevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Also retained were<br />\nquestions on mental health and access to care, perceived risk of using<br />\ndrugs, perceived availability of drugs, driving behavior and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey and retained in the 2000<br />\nsurvey. Demographic data include gender, race, age, ethnicity, marital<br />\nstatus, educational level, job status, veteran status, and current<br />\nhousehold composition.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-2000)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2000-nid13562",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-2000) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2000-nid13562"
-                }
-            ]
+            "title": "National Household Survey on Drug Abuse (NHSDA-2000)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -93132,42 +93108,46 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/uarv-cqnu",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-03-17",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "associate",
-                "host site",
-                "location",
-                "phap",
-                "program"
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
-            "identifier": "https://data.cdc.gov/api/views/uarv-cqnu",
             "description": "The map illustrates the total number of 2013 and 2014 PHAP associates in each state and U.S. territory.",
-            "title": "2013-2014 PHAP Associates by State",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93190,33 +93170,40 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/uarv-cqnu",
+            "issued": "2015-03-17",
+            "keyword": [
+                "associate",
+                "host site",
+                "location",
+                "phap",
+                "program"
+            ],
+            "landingPage": "https://data.cdc.gov/d/uarv-cqnu",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2015-08-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "2013-2014 PHAP Associates by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/f3zz-zga5",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-08",
-            "temporal": "9/1/2023 - Present",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Syndromic Surveillance Program",
                 "hasEmail": "mailto:nssp@cdc.gov "
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/f3zz-zga5",
             "description": "Respiratory illness activity is monitored using the acute respiratory illness (ARI) metric. ARI captures a broad range of diagnoses from emergency department visits for respiratory illnesses, from the common cold to severe infections like influenza, RSV and COVID-19. It captures illnesses that may not present with fever, offering a more complete picture than the previous influenza-like illness (ILI) metric.  \n\n Updated once per week on Fridays.",
-            "title": "Level of Acute Respiratory Illness (ARI) Activity by State",
-            "programCode": [
-                "009:038"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93239,43 +93226,38 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/f3zz-zga5",
+            "issued": "2024-11-08",
+            "landingPage": "https://data.cdc.gov/d/f3zz-zga5",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-24",
+            "programCode": [
+                "009:038"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "U.S.",
+            "temporal": "9/1/2023 - Present",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Level of Acute Respiratory Illness (ARI) Activity by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/khre-5qyk",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "exchange puf",
-                "marketplace puf",
-                "network",
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
-            "identifier": "1cec574b-9353-41cf-9c81-b7c49c482bb2",
             "description": "The Network PUF (Ntwrk-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Ntwrk-PUF contains issuer-level data identifying provider network URLs.",
-            "title": "Network PUF - PY2025",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93283,44 +93265,37 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "1cec574b-9353-41cf-9c81-b7c49c482bb2",
+            "issued": "2024-12-10",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "network",
+                "py2025"
+            ],
+            "landingPage": "https://healthdata.gov/d/khre-5qyk",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Network PUF - PY2025"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/3nij-2pw6",
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
-                "non-congenital",
-                "sabia virus",
-                "viral hemorrhagic fevers",
-                "wonder",
-                "yellow fever",
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
-            "identifier": "https://data.cdc.gov/api/views/3nij-2pw6",
             "description": "NNDSS - TABLE 1PP. Viral hemorrhagic fevers, Sabia virus to Zika virus disease, non-congenital \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1PP. Viral hemorrhagic fevers, Sabia virus to Zika virus disease, non-congenital",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93343,38 +93318,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/3nij-2pw6",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-congenital",
+                "sabia virus",
+                "viral hemorrhagic fevers",
+                "wonder",
+                "yellow fever",
+                "zika virus disease"
+            ],
+            "landingPage": "https://data.cdc.gov/d/3nij-2pw6",
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
+            "title": "NNDSS - TABLE 1PP. Viral hemorrhagic fevers, Sabia virus to Zika virus disease, non-congenital"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kia2-kqun",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-20",
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
-            "identifier": "0f06578a-8f49-46f9-8e42-80edf20ea395",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-12-2024-to-02-18-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93383,88 +93368,83 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-12-2024-to-02-18-2024"
                 }
             ],
+            "identifier": "0f06578a-8f49-46f9-8e42-80edf20ea395",
+            "issued": "2024-02-23",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/kia2-kqun",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-02-20",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-12-2024-to-02-18-2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kizf-jt27",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "references": [
-                "https://www.medicaid.gov/dq-atlas/welcome",
-                "https://www.mathematica.org/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_allStates_download\", \"stage\": \"featAuto\", \"update_id\": \"20220302_ETL_DEV_OT_SPLIT\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220302_ETL_DEV_OT_SPLIT/measure_allStates_download.csv",
+                    "mediaType": "text/csv",
+                    "title": "measure_allStates_download csv file"
+                }
             ],
+            "identifier": "63e60221-3cef-552a-8d1e-39baf4c2bd4b",
+            "issued": "2021-10-08",
             "keyword": [
                 "dqatlas",
                 "dqatlas_featauto",
                 "utility"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DataConnect Support Team",
-                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/d/kizf-jt27",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-03-02",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Medicare & Medicaid Services"
             },
-            "identifier": "63e60221-3cef-552a-8d1e-39baf4c2bd4b",
-            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_measure_allStates_download",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220302_ETL_DEV_OT_SPLIT/measure_allStates_download.csv",
-                    "description": "{\"dataset\": \"measure_allStates_download\", \"stage\": \"featAuto\", \"update_id\": \"20220302_ETL_DEV_OT_SPLIT\"}",
-                    "@type": "dcat:Distribution",
-                    "title": "measure_allStates_download csv file"
-                }
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "featAuto_measure_allStates_download"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/s5vm-cztk",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2018-07-10",
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
-            "identifier": "https://data.cdc.gov/api/views/s5vm-cztk",
             "description": "This dataset provides modeled predictions of PM2.5 levels from the EPA's Downscaler model. Data are at the census tract level for 2001-2005. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\r\n\r\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2001-2005",
-            "programCode": [
-                "009:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93487,46 +93467,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/s5vm-cztk",
+            "issued": "2018-07-10",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "particulate matter",
+                "pm2.5"
+            ],
+            "landingPage": "https://data.cdc.gov/d/s5vm-cztk",
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
+            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2001-2005"
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
-                "zcta"
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
-            "identifier": "https://data.cdc.gov/api/views/bumh-rgsq",
             "description": "This dataset contains ZCTA-level social determinants of health (SDOH) measures from the American Community Survey 5-year data for the entire United States\u201450 states and the District of Columbia. Data were downloaded from data.census.gov using Census API and processed by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. These measures complement existing PLACES measures, including PLACES SDOH measures (e.g., health insurance, routine check-up). These data can be used together with PLACES data to identify which health and SDOH issues overlap in a community to help inform public health planning.  \n\nTo access spatial data, please use the ArcGIS Online service:  https://cdcarcgis.maps.arcgis.com/home/item.html?id=d51009ea78b54635be95c6ec9955ec17.",
-            "title": "SDOH Measures for ZCTA, ACS 2017-2021",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93549,38 +93525,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bumh-rgsq",
+            "issued": "2023-10-26",
+            "keyword": [
+                "acs",
+                "estimates",
+                "places",
+                "sdoh",
+                "zcta"
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
+            "title": "SDOH Measures for ZCTA, ACS 2017-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xml",
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
-            "identifier": "5d4b366c-07ca-4358-a783-01aa2fe59684",
             "description": "This list includes human and pet food subject to recall in the United States since January 2009 related to peanut products distributed by Peanut Corporation of America.",
-            "title": "Peanut Product Recalls",
-            "programCode": [
-                "009:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93588,33 +93573,35 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "5d4b366c-07ca-4358-a783-01aa2fe59684",
+            "issued": "2021-02-25",
+            "keyword": [
+                "recalls"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xml",
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
+            "title": "Peanut Product Recalls"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4wzk-pwz3",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HELD Toxicology and Molecular Biology Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4wzk-pwz3",
             "description": "Traumatic brain injury (TBI) is as a major cause of death and disability experienced by nearly 3 million people annually resulting from falls, vehicular accidents, or from being struck by or against an object. While TBIs can range in severity, the majority of injuries are considered to be mild. However, TBI of any severity has the potential to have long-lasting neurological effects including headaches, cognitive/memory impairments, mood dysfunction, and fatigue as a result of neuronal damage and neuroinflammation. The goal of the study was to evaluate the neuroinflammatory and neuronal damage outcomes associated with mild or moderate-severe TBI via the modification of an established closed-head injury model of TBI by varying the material of the projectile.  Rats that received TBI using a stainless steel projectile exhibited outcomes strongly correlated to moderate-severe TBI, such as prolonged unconsciousness, impaired neurobehavior, increased risk for hematoma and death, as well as significant neuronal degeneration and neuroinflammation throughout the cortex, hippocampus, thalamus, and cerebellum.  In contrast, rats that received TBI with an aluminum projectile exhibited characteristics more congruous with mild TBI, such as a trend for longer periods of unconscious in the absence of neurobehavioral deficits, a lack of neurodegeneration and mild neuroinflammation.  Our results indicate that different levels of behavioral, neuroinflammatory, and damage outcomes are associated with differing levels of TBI severity.",
-            "title": "A Projectile Concussive Impact Model Produces Neuroinflammation in Both Mild and Moderate-Severe Traumatic Brain Injury",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93622,44 +93609,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4wzk-pwz3",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/4wzk-pwz3",
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
+            "title": "A Projectile Concussive Impact Model Produces Neuroinflammation in Both Mild and Moderate-Severe Traumatic Brain Injury"
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
-            "identifier": "https://data.cdc.gov/api/views/wrev-kwxu",
+            "describedBy": "https://data.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Pa/wrev-kwxu",
             "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Patient and Cycle Characteristics dataset summarizes the types of ART services performed and the kinds of patients who received ART procedures in a specific clinic. Please note patient characteristics are presented per cycle rather than per patient. As a result, patients who had more than one ART cycle within the reporting year are represented more than once.",
-            "title": "2022 Final Assisted Reproductive Technology (ART) Patient and Cycle Characteristics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93682,88 +93661,91 @@
                     "mediaType": "application/xml"
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
+            "title": "2022 Final Assisted Reproductive Technology (ART) Patient and Cycle Characteristics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/km4k-2uzc",
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
-            "identifier": "10012a8e-f16e-5acd-bc7e-209cb7aa94e2",
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
+            "identifier": "10012a8e-f16e-5acd-bc7e-209cb7aa94e2",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/km4k-2uzc",
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
-            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-08-28",
-            "keyword": [
-                "adults",
-                "covid-19 vaccination",
-                "iqvia"
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
-            "identifier": "https://data.cdc.gov/api/views/w76m-r924",
             "description": "Weekly Cumulative Estimated Number of Updated 2023-24 COVID-19 Vaccinations Administered in Pharmacies and Physical Medical Offices, Adults 18 Years and Older, United States \n\n\u2022 Estimated number of updated COVID-19 vaccinations among adults 18 years and older is assessed through IQVIA (https://www.iqvia.com/) as a source of information on vaccinations administered in retail pharmacies (include chain, mass merchandise, food stores, and independent pharmacies) and physician medical offices. \n\n\u2022 Starting in September 2023, the CDC recommended the updated 2023-2024 COVID-19 vaccine for adults ages 18 years and older.",
-            "title": "Weekly Cumulative Estimated Number of Updated 2023-24 COVID-19 Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, United States, Data Source(s): IQVIA Pharmacy and Physician Medical Office Claims",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93786,30 +93768,57 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States - National",
+            "identifier": "https://data.cdc.gov/api/views/w76m-r924",
+            "issued": "2023-12-16",
+            "keyword": [
+                "adults",
+                "covid-19 vaccination",
+                "iqvia"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
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
+            "spatial": "United States - National",
+            "temporal": "2023-2024",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Estimated Number of Updated 2023-24 COVID-19 Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, United States, Data Source(s): IQVIA Pharmacy and Physician Medical Office Claims"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nhanes/biospecimens/dnaspecimens.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
-            "issued": "2015-03-01",
-            "@type": "dcat:Dataset",
-            "temporal": "1991/2012",
-            "modified": "2023-03-27",
-            "references": [
-                "https://www.cdc.gov/nchs/nhanes/index.htm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:NHANESGenetics@cdc.gov"
+            },
+            "describedBy": "The NHANES samples were selected using a complex, stratified, multistage probability cluster sampling design.",
+            "description": "DNA samples were collected in the <b>Third National Health and Nutrition Examination Survey</b> (NHANES III; 1988-1994) and in subsequent NHANES cycles (1999-2002, 2007-2008, 2009-2010, and 2011-2012). The program is a nationally representative collection of stored DNA samples and genetic data and will serve to add to the extensive amount of health, nutritional, and environmental information collected from NHANES. Resulting genetic variants are deposited into the NHANES Genetic Data Repository. These datasets are categorized as restricted data since they contain identifiable information.\n\nFor more information on the NHANES Genetic Data please visit: <a href=\"https://www.cdc.gov/nchs/nhanes/biospecimens/dnaspecimens.htm\">NHANES DNA Specimens and Genetic Data Program at: https://www.cdc.gov/nchs/nhanes/biospecimens/dnaspecimens.htm.</a>\nFor more information on NHANES, visit the <a href=\"https://www.cdc.gov/nchs/nhanes/index.htm\">NHANES - National Health and Nutrition Examination Survey Homepage at: https://www.cdc.gov/nchs/nhanes/index.htm.</a>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "National Health and Nutrition Examination Survey (NHANES) Genetic Restricted Data"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hdx4-e4uu",
+            "isPartOf": "https://wwwn.cdc.gov/nchs/nhanes/default.aspx",
+            "issued": "2015-03-01",
             "keyword": [
                 "genetics",
                 "health statistics",
@@ -93820,74 +93829,42 @@
                 "surveillance",
                 "survey"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:NHANESGenetics@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/biospecimens/dnaspecimens.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-03-27",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/hdx4-e4uu",
-            "description": "DNA samples were collected in the <b>Third National Health and Nutrition Examination Survey</b> (NHANES III; 1988-1994) and in subsequent NHANES cycles (1999-2002, 2007-2008, 2009-2010, and 2011-2012). The program is a nationally representative collection of stored DNA samples and genetic data and will serve to add to the extensive amount of health, nutritional, and environmental information collected from NHANES. Resulting genetic variants are deposited into the NHANES Genetic Data Repository. These datasets are categorized as restricted data since they contain identifiable information.\n\nFor more information on the NHANES Genetic Data please visit: <a href=\"https://www.cdc.gov/nchs/nhanes/biospecimens/dnaspecimens.htm\">NHANES DNA Specimens and Genetic Data Program at: https://www.cdc.gov/nchs/nhanes/biospecimens/dnaspecimens.htm.</a>\nFor more information on NHANES, visit the <a href=\"https://www.cdc.gov/nchs/nhanes/index.htm\">NHANES - National Health and Nutrition Examination Survey Homepage at: https://www.cdc.gov/nchs/nhanes/index.htm.</a>",
-            "title": "National Health and Nutrition Examination Survey (NHANES) Genetic Restricted Data",
-            "isPartOf": "https://wwwn.cdc.gov/nchs/nhanes/default.aspx",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "mediaType": "text/html",
-                    "title": "National Health and Nutrition Examination Survey (NHANES) Genetic Restricted Data"
-                }
+            "references": [
+                "https://www.cdc.gov/nchs/nhanes/index.htm"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "United States",
-            "describedBy": "The NHANES samples were selected using a complex, stratified, multistage probability cluster sampling design.",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "1991/2012",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Health and Nutrition Examination Survey (NHANES) Genetic Restricted Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/vbim-akqf",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-05-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2024-21-06",
-            "modified": "2025-01-13",
-            "references": [
-                "https://github.com/CDCgov/covid_case_privacy_review/blob/master/analysis/public%2012%20utility%20summary.pdf"
-            ],
-            "keyword": [
-                "cases",
-                "coronavirus",
-                "covid",
-                "covid19",
-                "covid-19",
-                "surveillance"
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
-            "identifier": "https://data.cdc.gov/api/views/vbim-akqf",
-            "description": "<b>Note:</b>\nReporting of new COVID-19 Case Surveillance data will be discontinued July 1, 2024, to align with the process of removing SARS-CoV-2 infections (COVID-19 cases) from the list of nationally notifiable diseases. Although these data will continue to be publicly available, the dataset will no longer be updated.  \n\nAuthorizations to collect certain public health data expired at the end of the U.S. public health emergency declaration on May 11, 2023. The following jurisdictions discontinued COVID-19 case notifications to CDC: Iowa (11/8/21), Kansas (5/12/23), Kentucky (1/1/24), Louisiana (10/31/23), New Hampshire (5/23/23), and Oklahoma (5/2/23). Please note that these jurisdictions will not routinely send new case data after the dates indicated. As of 7/13/23, case notifications from Oregon will only include pediatric cases resulting in death.\n\n\nThis case surveillance public use dataset has 12 elements for all COVID-19 cases shared with CDC and includes demographics, any exposure history, disease severity indicators and outcomes, presence of any underlying medical conditions and risk behaviors, and no geographic data.\n\n<h4><b>CDC has three COVID-19 case surveillance datasets:</b></h4><ul><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4\">COVID-19 Case Surveillance Public Use Data with Geography</a>: Public use, patient-level dataset with clinical data (including symptoms), demographics, and county and state of residence. (19 data elements)</li><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf\">COVID-19 Case Surveillance Public Use Data</a>: Public use, patient-level dataset with clinical and symptom data and demographics, with no geographic data. (12 data elements)</li><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Restricted-Access-Detai/mbd7-r32t\">COVID-19 Case Surveillance Restricted Access Detailed Data</a>: Restricted access, patient-level dataset with clinical and symptom data, demographics, and state and county of residence. Access requires a registration process and a data use agreement. (33 data elements)</li></ul>\n\nThe following apply to all three datasets:\n<ul><li>Data elements can be found on the COVID-19 case report form located at <a href=\"https://www.cdc.gov/coronavirus/2019-ncov/downloads/pui-form.pdf\">www.cdc.gov/coronavirus/2019-ncov/downloads/pui-form.pdf</a>.</li><li>Data are considered provisional by CDC and are subject to change until the data are reconciled and verified with the state and territorial data providers.</li><li>Some data cells are suppressed to protect individual privacy.</li><li>The datasets will include all cases with the earliest date available in each record (date received by CDC or date related to illness/specimen collection) at least 14 days prior to the creation of the current datasets. This 14-day lag allows case reporting to be stabilized and ensures that time-dependent outcome data are accurately captured.</li><li>Datasets are updated monthly.</li><li>Datasets are created using CDC\u2019s <a href=\"https://www.cdc.gov/grants/additional-requirements/ar-25.html\">Policy on Public Health Research and Nonresearch Data Management and Access</a> and include protections designed to protect individual privacy.</li><li>For more information about data collection and reporting, please see\u202f<a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/about-us-cases-deaths.html\">https://www.cdc.gov/coronavirus/2019-ncov/covid-data/about-us-cases-deaths.html.</a></li><li>For more information about the COVID-19 case surveillance data, please see <a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html\"> https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html</a><br></li></ul>\n\n<h4><b>Overview</b></h4>\n\nThe COVID-19 case surveillance database includes individual-level data reported to U.S. states and aut",
-            "title": "COVID-19 Case Surveillance Public Use Data",
+            "describedBy": "https://data.cdc.gov/api/views/vbim-akqf/files/0eb0e326-d1bd-42a3-a748-acc6d6663326?download=true&filename=data_dictionary_covid_cases_public.xlsx",
             "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "<b>Note:</b>\nReporting of new COVID-19 Case Surveillance data will be discontinued July 1, 2024, to align with the process of removing SARS-CoV-2 infections (COVID-19 cases) from the list of nationally notifiable diseases. Although these data will continue to be publicly available, the dataset will no longer be updated.  \n\nAuthorizations to collect certain public health data expired at the end of the U.S. public health emergency declaration on May 11, 2023. The following jurisdictions discontinued COVID-19 case notifications to CDC: Iowa (11/8/21), Kansas (5/12/23), Kentucky (1/1/24), Louisiana (10/31/23), New Hampshire (5/23/23), and Oklahoma (5/2/23). Please note that these jurisdictions will not routinely send new case data after the dates indicated. As of 7/13/23, case notifications from Oregon will only include pediatric cases resulting in death.\n\n\nThis case surveillance public use dataset has 12 elements for all COVID-19 cases shared with CDC and includes demographics, any exposure history, disease severity indicators and outcomes, presence of any underlying medical conditions and risk behaviors, and no geographic data.\n\n<h4><b>CDC has three COVID-19 case surveillance datasets:</b></h4><ul><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4\">COVID-19 Case Surveillance Public Use Data with Geography</a>: Public use, patient-level dataset with clinical data (including symptoms), demographics, and county and state of residence. (19 data elements)</li><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf\">COVID-19 Case Surveillance Public Use Data</a>: Public use, patient-level dataset with clinical and symptom data and demographics, with no geographic data. (12 data elements)</li><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Restricted-Access-Detai/mbd7-r32t\">COVID-19 Case Surveillance Restricted Access Detailed Data</a>: Restricted access, patient-level dataset with clinical and symptom data, demographics, and state and county of residence. Access requires a registration process and a data use agreement. (33 data elements)</li></ul>\n\nThe following apply to all three datasets:\n<ul><li>Data elements can be found on the COVID-19 case report form located at <a href=\"https://www.cdc.gov/coronavirus/2019-ncov/downloads/pui-form.pdf\">www.cdc.gov/coronavirus/2019-ncov/downloads/pui-form.pdf</a>.</li><li>Data are considered provisional by CDC and are subject to change until the data are reconciled and verified with the state and territorial data providers.</li><li>Some data cells are suppressed to protect individual privacy.</li><li>The datasets will include all cases with the earliest date available in each record (date received by CDC or date related to illness/specimen collection) at least 14 days prior to the creation of the current datasets. This 14-day lag allows case reporting to be stabilized and ensures that time-dependent outcome data are accurately captured.</li><li>Datasets are updated monthly.</li><li>Datasets are created using CDC\u2019s <a href=\"https://www.cdc.gov/grants/additional-requirements/ar-25.html\">Policy on Public Health Research and Nonresearch Data Management and Access</a> and include protections designed to protect individual privacy.</li><li>For more information about data collection and reporting, please see\u202f<a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/about-us-cases-deaths.html\">https://www.cdc.gov/coronavirus/2019-ncov/covid-data/about-us-cases-deaths.html.</a></li><li>For more information about the COVID-19 case surveillance data, please see <a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html\"> https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html</a><br></li></ul>\n\n<h4><b>Overview</b></h4>\n\nThe COVID-19 case surveillance database includes individual-level data reported to U.S. states and aut",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93910,116 +93887,151 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
-            "describedBy": "https://data.cdc.gov/api/views/vbim-akqf/files/0eb0e326-d1bd-42a3-a748-acc6d6663326?download=true&filename=data_dictionary_covid_cases_public.xlsx",
+            "identifier": "https://data.cdc.gov/api/views/vbim-akqf",
+            "issued": "2020-05-15",
+            "keyword": [
+                "cases",
+                "coronavirus",
+                "covid",
+                "covid19",
+                "covid-19",
+                "surveillance"
+            ],
+            "landingPage": "https://data.cdc.gov/d/vbim-akqf",
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
+            "references": [
+                "https://github.com/CDCgov/covid_case_privacy_review/blob/master/analysis/public%2012%20utility%20summary.pdf"
+            ],
+            "spatial": "US",
+            "temporal": "2020-01-01/2024-21-06",
             "theme": [
                 "Case Surveillance"
-            ]
+            ],
+            "title": "COVID-19 Case Surveillance Public Use Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kp27-ns4b",
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
-            "identifier": "281a686a-e457-5570-a102-157023507ab8",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet filters v2.10.64 (coreset-prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/filters.csv",
-                    "description": "CoreSet filters v2.10.64 (coreset-prod)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet filters v2.10.64 (coreset-prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet filters v2.10.64 (coreset-prod)"
                 }
             ],
+            "identifier": "281a686a-e457-5570-a102-157023507ab8",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/kp27-ns4b",
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
+            "title": "CoreSet filters v2.10.64 (coreset-prod)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kp7p-697u",
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
-            "identifier": "f768cec0-26a6-5a21-ba76-94e1d3387f34",
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
+            "identifier": "f768cec0-26a6-5a21-ba76-94e1d3387f34",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/kp7p-697u",
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
-            "landingPage": "https://healthdata.gov/dataset/cdc-biosense-tarrant-county-texas",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Tarrant County Public Health (TCPH) and Biosense collaboration is an effort to visualize TCPH health data collected by Biosense using Google Fusion Table technology and make that visualization publicly available. The data consists of patient visits to hospital emergency departments associated with Tarrant County Public Health (TCPH)  that had the illness Gastro Intestinal, Heat Related, or Upper Respiratory divided by all emergency department visits that occurred for the same time period and in the geographic granularity for which the calculation was made.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/nssp/biosense/onboarding.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "2e3a0a06-5e2d-4cbc-8c63-0d54e10978d9",
             "issued": "2012-05-30",
-            "temporal": "2007-01-01T00:00:00-05:00/2007-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "chronic disease",
                 "community health",
@@ -94037,65 +94049,36 @@
                 "upper respiratory",
                 "visualization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-biosense-tarrant-county-texas",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "2e3a0a06-5e2d-4cbc-8c63-0d54e10978d9",
-            "description": "<p>The Tarrant County Public Health (TCPH) and Biosense collaboration is an effort to visualize TCPH health data collected by Biosense using Google Fusion Table technology and make that visualization publicly available. The data consists of patient visits to hospital emergency departments associated with Tarrant County Public Health (TCPH)  that had the illness Gastro Intestinal, Heat Related, or Upper Respiratory divided by all emergency department visits that occurred for the same time period and in the geographic granularity for which the calculation was made.</p>",
-            "title": "CDC BioSense On-Boarding",
-            "programCode": [
-                "009:048"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/nssp/biosense/onboarding.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "2007-01-01T00:00:00-05:00/2007-01-01T00:00:00-05:00",
             "theme": [
                 "Community",
                 "Health"
-            ]
+            ],
+            "title": "CDC BioSense On-Boarding"
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
-            "identifier": "https://data.cdc.gov/api/views/yctb-fv7w",
             "description": "\u2022 COVID-19 vaccination coverage among children 6 months to 17 years is assessed through the National Immunization Survey providing weekly COVID-19 vaccination coverage estimates (https://www.cdc.gov/vaccines/imz-managers/nis/about.html). \n\n\u2022 Weekly estimates of COVID-19 vaccination coverage and parental intent for vaccination among children through December 31, 2023, were calculated using data from the National Immunization Survey-Child COVID Module (NIS-CCM) (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-ccm). Beginning January 2, 2024, the NIS-CCM was discontinued, and questions regarding receipt of COVID-19 vaccination among children were added to the NIS-Flu (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-cim). \n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19 (https://www.cdc.gov/coronavirus/2019-ncov/vaccines/stay-up-to-date.html).",
-            "title": "Cumulative Percentage of Children Ages 6 Months -17 Years Who Are Up to Date with the Updated 2023-24 COVID-19 Vaccine",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94118,40 +94101,41 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/yctb-fv7w",
+            "issued": "2023-11-07",
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
+            "title": "Cumulative Percentage of Children Ages 6 Months -17 Years Who Are Up to Date with the Updated 2023-24 COVID-19 Vaccine"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kqrh-gg42",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2025-01-15",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-14",
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
-            "identifier": "b4cfe208-05cd-46a0-baef-fe0e67d2abb1",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 01-06-2025-to-01-12-2025",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94160,105 +94144,84 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 01-06-2025-to-01-12-2025"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "b4cfe208-05cd-46a0-baef-fe0e67d2abb1",
+            "issued": "2025-01-15",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/kqrh-gg42",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 01-06-2025-to-01-12-2025"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kqx9-wkhb",
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
-            "identifier": "46ea08d0-c3cc-5ecd-b665-18e50c2854fe",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_map",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/map.csv",
-                    "description": "{\"dataset\": \"map\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"map\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/map.csv",
+                    "mediaType": "text/csv",
                     "title": "map csv file"
                 }
             ],
+            "identifier": "46ea08d0-c3cc-5ecd-b665-18e50c2854fe",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/kqx9-wkhb",
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
+            "title": "prodAuto_map"
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
-            "identifier": "https://data.cdc.gov/api/views/dnxe-zgxs",
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2002/dnxe-zgxs",
             "description": "2002.  Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2002",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94281,116 +94244,127 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2002/dnxe-zgxs",
+            "identifier": "https://data.cdc.gov/api/views/dnxe-zgxs",
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
+            "title": "CDC PRAMStat Data for 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nlm.nih.gov/research/visible/visible_human.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-08-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "anatomy",
-                "data distribution",
-                "dataset",
-                "images",
-                "medical imaging"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ux2j-9i9a",
             "description": "The NLM Visible Human Project\u00ae has created publicly-available complete, anatomically detailed, three-dimensional representations of a human male body and a human female body. Specifically, the VHP provides a public-domain library of cross-sectional cryosection, CT, and MRI images obtained from one male cadaver and one female cadaver. The Visible Man data set was publicly released in 1994 and the Visible Woman in 1995.\n\nhttps://www.nlm.nih.gov/research/visible/visible_human.html",
-            "title": "Visible Human Project",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Visible-Human/Sample-Data/index.html",
-                    "description": "The Visible Human Project Sample Data contains the following sample images:\nCT scans after freezing, CT scans prior to freezing, Five slices from the Visible Female, Six slices from the Visible Male, MRI-MaleHead, MRI-MaleThorax, MRI-MaleAbdomen, MRI-MalePelvis, MRI-MaleThigh, MRI-MaleFeet.",
                     "@type": "dcat:Distribution",
+                    "description": "The Visible Human Project Sample Data contains the following sample images:\nCT scans after freezing, CT scans prior to freezing, Five slices from the Visible Female, Six slices from the Visible Male, MRI-MaleHead, MRI-MaleThorax, MRI-MaleAbdomen, MRI-MalePelvis, MRI-MaleThigh, MRI-MaleFeet.",
+                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Visible-Human/Sample-Data/index.html",
+                    "mediaType": "text/html",
                     "title": "Download - Visible Human Project - Sample Data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Visible-Human/Male-Images/index.html",
-                    "description": "The Visible Human Male data set consists of MRI, CT, and anatomical images. Axial MRI images of the head and neck, and longitudinal sections of the rest of the body were obtained at 4mm intervals. The MRI images are 256 by 256 pixel resolution with each pixel made up of 12 bits of gray tone. The CT data consist of axial CT scans of the entire body taken at 1mm intervals at a pixel resolution of 512 by 512 with each pixel made up of 12 bits of gray tone. The approximately 7.5 megabyte axial anatomical images are 2048 pixels by 1216 pixels, with each pixel being .33mm in size, and defined by 24 bits of color. The anatomical cross-sections are at 1mm intervals to coincide with the CT images. There are 1,871 cross-sections for both CT and anatomical images. The complete male data set is approximately 15 gigabytes.",
                     "@type": "dcat:Distribution",
+                    "description": "The Visible Human Male data set consists of MRI, CT, and anatomical images. Axial MRI images of the head and neck, and longitudinal sections of the rest of the body were obtained at 4mm intervals. The MRI images are 256 by 256 pixel resolution with each pixel made up of 12 bits of gray tone. The CT data consist of axial CT scans of the entire body taken at 1mm intervals at a pixel resolution of 512 by 512 with each pixel made up of 12 bits of gray tone. The approximately 7.5 megabyte axial anatomical images are 2048 pixels by 1216 pixels, with each pixel being .33mm in size, and defined by 24 bits of color. The anatomical cross-sections are at 1mm intervals to coincide with the CT images. There are 1,871 cross-sections for both CT and anatomical images. The complete male data set is approximately 15 gigabytes.",
+                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Visible-Human/Male-Images/index.html",
+                    "mediaType": "text/html",
                     "title": "Download - Visible Human Project - Male Data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Visible-Human/Female-Images/index.html",
-                    "description": "The Visible Human Female data set has the same characteristics as the Visible Human Male. However, the axial anatomical images were obtained at 0.33 mm intervals. Spacing in the \u201cZ\u201d dimension was reduced to 0.33mm in order to match the 0.33mm pixel sizing in the \u201cX-Y\u201d plane. As a result, developers interested in three-dimensional reconstructions are able to work with cubic voxels. There are 5,189 anatomical images in the Visible Human Female data set. The data set size is approximately 40 gigabytes.",
                     "@type": "dcat:Distribution",
+                    "description": "The Visible Human Female data set has the same characteristics as the Visible Human Male. However, the axial anatomical images were obtained at 0.33 mm intervals. Spacing in the \u201cZ\u201d dimension was reduced to 0.33mm in order to match the 0.33mm pixel sizing in the \u201cX-Y\u201d plane. As a result, developers interested in three-dimensional reconstructions are able to work with cubic voxels. There are 5,189 anatomical images in the Visible Human Female data set. The data set size is approximately 40 gigabytes.",
+                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Visible-Human/Female-Images/index.html",
+                    "mediaType": "text/html",
                     "title": "Download - Visible Human Project - Female Data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Visible-Human/Additional-Head-Images/index.html",
-                    "description": "Data is the head of a 72 year old male donor. The donor was preserved in formalin and the blood vessels were filled with araldite-F.  Before freezing, MRI and CAT imaging was preformed. After freezing the specimen was cryo sectioned at 0.147mm intervals and digital photographs were taken with a resolution of 1056 x 1528 pixels.",
                     "@type": "dcat:Distribution",
+                    "description": "Data is the head of a 72 year old male donor. The donor was preserved in formalin and the blood vessels were filled with araldite-F.  Before freezing, MRI and CAT imaging was preformed. After freezing the specimen was cryo sectioned at 0.147mm intervals and digital photographs were taken with a resolution of 1056 x 1528 pixels.",
+                    "downloadURL": "https://data.lhncbc.nlm.nih.gov/public/Visible-Human/Additional-Head-Images/index.html",
+                    "mediaType": "text/html",
                     "title": "Download - Visible Human Project - Additional Head Images"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ux2j-9i9a",
+            "issued": "2020-08-10",
+            "keyword": [
+                "anatomy",
+                "data distribution",
+                "dataset",
+                "images",
+                "medical imaging"
+            ],
+            "landingPage": "https://www.nlm.nih.gov/research/visible/visible_human.html",
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
+            "title": "Visible Human Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/aemt-mg7g",
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
-            "identifier": "https://data.cdc.gov/api/views/aemt-mg7g",
             "description": "<b>Note:</b> \nAfter November 1, 2024, this dataset will no longer be updated due to a transition in NHSN Hospital Respiratory Data reporting that occurred on Friday, November 1, 2024. For more information on NHSN Hospital Respiratory Data reporting, please visit https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html.\n\nDue to a recent update in voluntary NHSN Hospital Respiratory Data reporting that occurred on Wednesday, October 9, 2024, reporting levels and other data displayed on this page may fluctuate week-over-week beginning Friday, October 18, 2024. For more information on NHSN Hospital Respiratory Data reporting, please visit https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html.  Find more information about the updated CMS requirements: https://www.federalregister.gov/documents/2024/08/28/2024-17021/medicare-and-medicaid-programs-and-the-childrens-health-insurance-program-hospital-inpatient.\u202f  \n\nThis dataset represents weekly respiratory virus-related hospitalization data and metrics aggregated to national and state/territory levels reported during two periods: 1) data for collection dates from August 1, 2020 to April 30, 2024, represent data reported by hospitals during a mandated reporting period as specified by the HHS Secretary; and 2) data for collection dates beginning May 1, 2024, represent data reported voluntarily by hospitals to CDC\u2019s National Healthcare Safety Network (NHSN). NHSN monitors national and local trends in healthcare system stress and capacity for up to approximately 6,000 hospitals in the United States. Data reported represent aggregated counts and include metrics capturing information specific to COVID-19- and influenza-related hospitalizations, hospital occupancy, and hospital capacity. Find more information about reporting to NHSN at:\u202fhttps://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html.\n\n<b>Source: COVID-19 hospitalization data reported to CDC\u2019s National Healthcare Safety Network (NHSN).</b>\n<ul><li><b>Data source description (updated October 18, 2024):</b> As of October 9, 2024, Hospital Respiratory Data (HRD; formerly Respiratory Pathogen, Hospital Capacity, and Supply data or \u2018COVID-19 hospital data\u2019) are reported to HHS through CDC\u2019s National Healthcare Safety Network based on updated requirements from the Centers for Medicare and Medicaid Services (CMS). These data are voluntarily reported to NHSN as of May 1, 2024 until November 1, 2024, at which time CMS will require acute care and critical access hospitals to electronically report information via NHSN about COVID-19, Influenza, and RSV, hospital bed census and capacity, and limited patient demographic information, including age. Data for collection dates prior to May 1, 2024, represent data reported during a previously mandated reporting period as specified by the HHS Secretary. Data for collection dates May 1, 2024, and onwards represent data reported voluntarily to NHSN; as such, data included represents reporting hospitals only for a given week and might not be complete or representative of all hospitals. NHSN monitors national and local trends in healthcare system stress and capacity for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Find more information about reporting to NHSN: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html. Find more information about the updated CMS requirements: https://www.federalregister.gov/documents/2024/08/28/2024-17021/medicare-and-medicaid-programs-and-the-childrens-health-insurance-program-hospital-inpatient.\u202f </li><li><b>Data quality:</b> While CDC reviews reported data for completeness and errors and corrects those found, some reporting errors might still exist within the data. CDC and partners work with reporters to correct these errors and update the data in subse",
-            "title": "Weekly United States Hospitalization Metrics by Jurisdiction, During Mandatory Reporting Period from August 1, 2020 to April 30, 2024, and for Data Reported Voluntarily Beginning May 1, 2024, National Healthcare Safety Network (NHSN) - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94413,45 +94387,53 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/aemt-mg7g",
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
+            "landingPage": "https://data.cdc.gov/d/aemt-mg7g",
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
             "theme": [
                 "Public Health Surveillance"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly United States Hospitalization Metrics by Jurisdiction, During Mandatory Reporting Period from August 1, 2020 to April 30, 2024, and for Data Reported Voluntarily Beginning May 1, 2024, National Healthcare Safety Network (NHSN) - ARCHIVED"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -94474,28 +94456,56 @@
                     "mediaType": "application/xml"
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
+            "title": "Monthly Nirsevimab Receipt and Intent Among Females Aged 18-49 Years Who Have a Baby <8 Months, Are Currently Pregnant, or Are Trying to Get Pregnant, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://smokefree.gov/",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "references": [
-                "https://smokefree.gov/about-us/smokefree"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HealthData.Gov Team",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "description": "<p>Overview: The QuitNowTXT text messaging program is designed as a resource that can be adapted to specific contexts including those outside the United States and in languages other than English. Based on evidence-based practices, this program is a smoking cessation intervention for smokers who are ready to quit smoking. Although evidence supports the use of text messaging as a platform to deliver cessation interventions, it is expected that the maximum effect of the program will be demonstrated when it is integrated into other elements of a national tobacco control strategy.  The QuitNowTXT program is designed to deliver tips, motivation, encouragement and fact-based information via unidirectional and interactive bidirectional message formats. The core of the program consists of messages sent to the user based on a scheduled quit day identified by the user. Messages are sent for up to four weeks pre-quit date and up to six weeks post quit date. Messages assessing mood, craving, and smoking status are also sent at various intervals, and the user receives messages back based on the response they have submitted. In addition, users can request assistance in dealing with craving, stress/mood, and responding to slips/relapses by texting specific key words to the QuitNow. Rotating automated messages are then returned to the user based on the keyword. Details of the program are provided below. Texting STOP to the service discontinues further texts being sent.  This option is provided every few messages as required by the United States cell phone providers.  It is not an option to remove this feature if the program is used within the US.  If a web-based registration is used, it is suggested that users provide demographic information such as age, gender, and smoking frequency (daily or almost every day, most days, only a few days a week, only on weekends, a few times a month or less) in addition to their mobile phone number and quit date. This information will be useful for assessing the reach of the program, as well as identifying possible need to develop libraries to specific groups. The use of only a mobile phone-based registration system reduces barriers for participant entry into the program but limits the collection of additional data. At bare minimum, quit date must be collected.  At sign up, participants will have the option to choose a quit date up to one month out. Text messages will start up to 14 days before their specified quit date. Users also have the option of changing their quit date at any time if desired. The program can also be modified to provide texts to users who have already quit within the last month.  One possible adaptation of the program is to include a QuitNowTXT \"light\" version. This adaptation would allow individuals who do not have unlimited text messaging capabilities but would still like to receive support to participate by controlling the number of messages they receive. In the light program, users can text any of the programmed keywords without fully opting in to the program. Program Design: The program is designed as a 14-day countdown to quit date, with subsequent six weeks of daily messages. Each day within the program is identified as either a pre-quit date (Q- # days) or a post-quit date (Q+#). If a user opts into the program fewer than 14 days before their quit date, the system will begin sending messages on that day. For example, if they opt in four days prior to their quit date, the system will send a welcome message and recognize that they are at Q-4 (or four days before their quit date), and they will receive the message that everyone else receives four days before their quit date. As the user progresses throughout the program, they will receive messages outlined in the text message library. Throughout the program, users will receive texts that cover a variety of content areas including tips, informational content, motivational messaging, and keyword responses. The frequency of messages in",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Who is this program for?\nAdults in the United States who are ready to quit smoking. This program is offered by the National Cancer Institute\u2019s Smokefree.gov.\n\n\nHow does it work?\nSign up with the form below or text QUIT to 47848.\n\nAfter you confirm your enrollment, you will receive daily text messages to support you in quitting smoking from the short code 47848 (message and data rates may apply). The program lasts for 6-8 weeks.\n\nYou can opt out at any time by texting STOP. Text HELP at any time for information on the program. ",
+                    "downloadURL": "https://smokefree.gov/tools-tips/text-programs/quit-for-good/smokefreetxt",
+                    "mediaType": "text/html",
+                    "title": "SmokefreeTXT"
+                }
             ],
+            "identifier": "c90f280f-7c5c-4d12-a648-a521301708c0",
+            "issued": "2021-02-13",
             "keyword": [
                 "cancer",
                 "cessation",
@@ -94509,62 +94519,36 @@
                 "tobacco control",
                 "treatments"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HealthData.Gov Team",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://smokefree.gov/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:047"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Cancer Institute (NCI), National Institutes of Health (NIH)"
             },
-            "identifier": "c90f280f-7c5c-4d12-a648-a521301708c0",
-            "description": "<p>Overview: The QuitNowTXT text messaging program is designed as a resource that can be adapted to specific contexts including those outside the United States and in languages other than English. Based on evidence-based practices, this program is a smoking cessation intervention for smokers who are ready to quit smoking. Although evidence supports the use of text messaging as a platform to deliver cessation interventions, it is expected that the maximum effect of the program will be demonstrated when it is integrated into other elements of a national tobacco control strategy.  The QuitNowTXT program is designed to deliver tips, motivation, encouragement and fact-based information via unidirectional and interactive bidirectional message formats. The core of the program consists of messages sent to the user based on a scheduled quit day identified by the user. Messages are sent for up to four weeks pre-quit date and up to six weeks post quit date. Messages assessing mood, craving, and smoking status are also sent at various intervals, and the user receives messages back based on the response they have submitted. In addition, users can request assistance in dealing with craving, stress/mood, and responding to slips/relapses by texting specific key words to the QuitNow. Rotating automated messages are then returned to the user based on the keyword. Details of the program are provided below. Texting STOP to the service discontinues further texts being sent.  This option is provided every few messages as required by the United States cell phone providers.  It is not an option to remove this feature if the program is used within the US.  If a web-based registration is used, it is suggested that users provide demographic information such as age, gender, and smoking frequency (daily or almost every day, most days, only a few days a week, only on weekends, a few times a month or less) in addition to their mobile phone number and quit date. This information will be useful for assessing the reach of the program, as well as identifying possible need to develop libraries to specific groups. The use of only a mobile phone-based registration system reduces barriers for participant entry into the program but limits the collection of additional data. At bare minimum, quit date must be collected.  At sign up, participants will have the option to choose a quit date up to one month out. Text messages will start up to 14 days before their specified quit date. Users also have the option of changing their quit date at any time if desired. The program can also be modified to provide texts to users who have already quit within the last month.  One possible adaptation of the program is to include a QuitNowTXT \"light\" version. This adaptation would allow individuals who do not have unlimited text messaging capabilities but would still like to receive support to participate by controlling the number of messages they receive. In the light program, users can text any of the programmed keywords without fully opting in to the program. Program Design: The program is designed as a 14-day countdown to quit date, with subsequent six weeks of daily messages. Each day within the program is identified as either a pre-quit date (Q- # days) or a post-quit date (Q+#). If a user opts into the program fewer than 14 days before their quit date, the system will begin sending messages on that day. For example, if they opt in four days prior to their quit date, the system will send a welcome message and recognize that they are at Q-4 (or four days before their quit date), and they will receive the message that everyone else receives four days before their quit date. As the user progresses throughout the program, they will receive messages outlined in the text message library. Throughout the program, users will receive texts that cover a variety of content areas including tips, informational content, motivational messaging, and keyword responses. The frequency of messages in",
-            "title": "QuitNowTXT Text Messaging Library",
-            "programCode": [
-                "009:047"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://smokefree.gov/tools-tips/text-programs/quit-for-good/smokefreetxt",
-                    "description": "Who is this program for?\nAdults in the United States who are ready to quit smoking. This program is offered by the National Cancer Institute\u2019s Smokefree.gov.\n\n\nHow does it work?\nSign up with the form below or text QUIT to 47848.\n\nAfter you confirm your enrollment, you will receive daily text messages to support you in quitting smoking from the short code 47848 (message and data rates may apply). The program lasts for 6-8 weeks.\n\nYou can opt out at any time by texting STOP. Text HELP at any time for information on the program. ",
-                    "@type": "dcat:Distribution",
-                    "title": "SmokefreeTXT"
-                }
+            "references": [
+                "https://smokefree.gov/about-us/smokefree"
             ],
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "QuitNowTXT Text Messaging Library"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kspi-2sgr",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-01-19",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-26",
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
-            "identifier": "4a00010a-132b-4e4d-a611-543c9521280f",
             "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
-            "title": "NADAC (National Average Drug Acquisition Cost) 2023",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94573,22 +94557,51 @@
                     "title": "NADAC (National Average Drug Acquisition Cost) 2023"
                 }
             ],
+            "identifier": "4a00010a-132b-4e4d-a611-543c9521280f",
+            "issued": "2023-01-19",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "landingPage": "https://healthdata.gov/d/kspi-2sgr",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2023-12-26",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "theme": [
                 "National Average Drug Acquisition Cost",
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "NADAC (National Average Drug Acquisition Cost) 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-4-year-r-das-nsduh-2002-2005",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This file includes data from the 2002 through 2013 National Survey on Drug Use and Health (NSDUH) survey. The only variables included in the data file are ones that were collected in a comparable manner across all four years from 2002-2005, from 2006-2009, or from 2010-2013.<br />\nThe National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Certain questions are asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Also included are questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Demographic information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.<br />\nIn the income section, which was interviewer-administered, a split-sample study had been embedded within the 2006 and 2007 surveys to compare a shorter version of the income questions with a longer set of questions that had been used in previous surveys. This shorter version was adopted for the 2008 NSDUH and will be used for future NSDUHs.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health: 4-Year R-DAS (NSDUH-2002-2005) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-4-year-r-das-nsduh-2002-2005-nid13611",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-4-year-r-das-nsduh-2002-2005-nid13611"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-4-year-r-das-nsduh-2002-2005-nid13611",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -94629,66 +94642,29 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-4-year-r-das-nsduh-2002-2005",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-4-year-r-das-nsduh-2002-2005-nid13611",
-            "description": "<p>This file includes data from the 2002 through 2013 National Survey on Drug Use and Health (NSDUH) survey. The only variables included in the data file are ones that were collected in a comparable manner across all four years from 2002-2005, from 2006-2009, or from 2010-2013.<br />\nThe National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Certain questions are asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Also included are questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Demographic information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.<br />\nIn the income section, which was interviewer-administered, a split-sample study had been embedded within the 2006 and 2007 surveys to compare a shorter version of the income questions with a longer set of questions that had been used in previous surveys. This shorter version was adopted for the 2008 NSDUH and will be used for future NSDUHs.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health: 4-Year R-DAS (NSDUH-2002-2005)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-4-year-r-das-nsduh-2002-2005-nid13611",
-                    "description": "National Survey on Drug Use and Health: 4-Year R-DAS (NSDUH-2002-2005) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-4-year-r-das-nsduh-2002-2005-nid13611"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health: 4-Year R-DAS (NSDUH-2002-2005)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/cah8-bpvk",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "lujo virus",
-                "machupo virus",
-                "marburg virus",
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
-            "identifier": "https://data.cdc.gov/api/views/cah8-bpvk",
             "description": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Lujo virus to Viral hemorrhagic fevers, Marburg virus \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents..\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Lujo virus to Viral hemorrhagic fevers, Marburg virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94711,45 +94687,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cah8-bpvk",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "lujo virus",
+                "machupo virus",
+                "marburg virus",
+                "nedss",
+                "netss",
+                "nndss",
+                "viral hemorrhagic fevers",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/cah8-bpvk",
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
+            "title": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Lujo virus to Viral hemorrhagic fevers, Marburg virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4day-mt2f",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-13",
-            "temporal": "2022-01-01/Present",
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
-            "identifier": "https://data.cdc.gov/api/views/4day-mt2f",
             "description": "This file contains death counts and death rates for drug overdose, suicide, homicide and firearm injuries by census tract of residence (additional datasets exist for other levels of geography). The data is grouped by 2 different time periods including yearly and trailing twelve months. Please see data dictionary for intents and mechanisms included in each measure. \n\n \n\nWhen there are 1-9 deaths in an area, CDC uses a Bayesian model to calculate rates. A Bayesian model is a type of statistical model often used in geographic analysis. This model can improve stability of the rates in lower population areas and protects privacy by taking into account information from neighboring areas.",
-            "title": "Mapping Injury, Overdose, and Violence - Census Tract",
-            "programCode": [
-                "009:033"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94772,49 +94750,51 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4day-mt2f",
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
+            "landingPage": "https://data.cdc.gov/d/4day-mt2f",
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
+            "temporal": "2022-01-01/Present",
             "theme": [
                 "Injury & Violence"
-            ]
+            ],
+            "title": "Mapping Injury, Overdose, and Violence - Census Tract"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://medpix.nlm.nih.gov/home",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "education",
-                "images",
-                "medical imaging",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vp23-ayt5",
             "description": "MedPix is a database of patient cases integrating images and textual information. The content material is organized by disease location (organ system), pathology category, patient profiles, and by image classification and caption.  Additional information at https://medpix.nlm.nih.gov/home",
-            "title": "MedPix",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://openi.nlm.nih.gov/services#searchAPIUsingGET",
-                    "description": "MedPix can be accessed programmatically via the Open-i API.",
                     "@type": "dcat:Distribution",
+                    "description": "MedPix can be accessed programmatically via the Open-i API.",
+                    "downloadURL": "https://openi.nlm.nih.gov/services#searchAPIUsingGET",
+                    "mediaType": "text/html",
                     "title": "API"
                 },
                 {
@@ -94824,94 +94804,98 @@
                     "title": "Query Interface"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cup.nlm.nih.gov/login",
-                    "description": "If you have images and interesting clinical observations you'd like to showcase in MedPix\u00ae, Open-i\u2120 or both, we would like to publish them. Please register and submit good-quality de-identified images with a brief description of the clinical course. To submit a MedPix case, please provide differential diagnoses and treatment plan based on evidence supported by references.",
                     "@type": "dcat:Distribution",
+                    "description": "If you have images and interesting clinical observations you'd like to showcase in MedPix\u00ae, Open-i\u2120 or both, we would like to publish them. Please register and submit good-quality de-identified images with a brief description of the clinical course. To submit a MedPix case, please provide differential diagnoses and treatment plan based on evidence supported by references.",
+                    "downloadURL": "https://cup.nlm.nih.gov/login",
+                    "mediaType": "text/html",
                     "title": "Submit Your Case Report"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vp23-ayt5",
+            "issued": "2021-06-30",
+            "keyword": [
+                "api",
+                "education",
+                "images",
+                "medical imaging",
+                "training and instruction"
+            ],
+            "landingPage": "https://medpix.nlm.nih.gov/home",
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
+            "title": "MedPix"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kv2y-hu7s",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2021-10-25",
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
-            "identifier": "99a60727-dc56-5dc2-a72c-5b2e71078ad6",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_measure_allStates_download",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20211018_v2_ETL_DEV_OT_SPLIT/measure_allStates_download.csv",
-                    "description": "{\"dataset\": \"measure_allStates_download\", \"stage\": \"prodAuto\", \"update_id\": \"20211018_v2_ETL_DEV_OT_SPLIT\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_allStates_download\", \"stage\": \"prodAuto\", \"update_id\": \"20211018_v2_ETL_DEV_OT_SPLIT\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20211018_v2_ETL_DEV_OT_SPLIT/measure_allStates_download.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_allStates_download csv file"
                 }
             ],
+            "identifier": "99a60727-dc56-5dc2-a72c-5b2e71078ad6",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/kv2y-hu7s",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2021-10-25",
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
+            "title": "prodAuto_measure_allStates_download"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Safety/Recalls/EnforcementReports/default.htm",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "ora",
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
-            "identifier": "99f89749-f77f-4d0f-a415-8c7b633bac1f",
             "description": "Whereas not all recalls are announced in the media or on our Recalls press release page, all recalls montiored by FDA are included in FDA's weekly Enforcement Report once they are classified according to the level of hazard involved.",
-            "title": "Enforcement Reports",
-            "programCode": [
-                "009:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94919,50 +94903,37 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "99f89749-f77f-4d0f-a415-8c7b633bac1f",
+            "issued": "2021-02-25",
+            "keyword": [
+                "ora",
+                "regulations"
+            ],
+            "landingPage": "http://www.fda.gov/Safety/Recalls/EnforcementReports/default.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1W"
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:008"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Enforcement Reports"
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
-                "city",
-                "disability",
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
-            "identifier": "https://data.cdc.gov/api/views/eav7-hnsx",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
             "description": "This dataset contains model-based place (incorporated and census-designated places) estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 40 measures: 12 for health outcomes, 7 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, 3 for health status, and 7 for health-related social needs. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2022 or 2021 data, Census Bureau 2020 population data, and American Community Survey 2018\u20132022 estimates. The 2024 release uses 2022 BRFSS data for 36 measures and 2021 BRFSS data for 4 measures (high blood pressure, high cholesterol, cholesterol screening, and taking medicine for high blood pressure control among those with high blood pressure) that the survey collects data on every other year. More information about the methodology can be found at  www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, Place Data 2024 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94985,39 +94956,53 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
+            "identifier": "https://data.cdc.gov/api/views/eav7-hnsx",
+            "issued": "2024-08-23",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "city",
+                "disability",
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
+            "title": "PLACES: Local Data for Better Health, Place Data 2024 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kwct-eszz",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-11-29",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
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
-            "identifier": "67483256-e996-4342-9867-fc0b6a67230f",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-11-20-to-2023-11-26",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95026,83 +95011,82 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-11-20-to-2023-11-26"
                 }
             ],
+            "identifier": "67483256-e996-4342-9867-fc0b6a67230f",
+            "issued": "2023-11-29",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/kwct-eszz",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-11-27",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-11-20-to-2023-11-26"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kwun-rzng",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-04-08",
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
-            "identifier": "7a2f3f40-7955-5018-be8a-9bc3347fd05c",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard state v2.11.18 (etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/state.csv",
-                    "description": "Scorecard state v2.11.18 (etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard state v2.11.18 (etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/state.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard state v2.11.18 (etl-test)"
                 }
             ],
+            "identifier": "7a2f3f40-7955-5018-be8a-9bc3347fd05c",
+            "issued": "2023-04-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/kwun-rzng",
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
+            "title": "Scorecard state v2.11.18 (etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/foundation-health-measures.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "temporal": "2010-01-01/2018-12-31",
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
-            "identifier": "https://data.cdc.gov/api/views/f3a8-hmpp",
             "description": "The Foundation Health Measures component of the Healthy People 2020 (HP2020) Final Review includes data on 14 global summary measures used to monitor improvement in population health. See Technical Notes of the Foundation Health Measures in the HP2020 Final Review for additional information on the definition and construction of these measures included.",
-            "title": "Healthy People 2020 Foundation Health Measures",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95125,49 +95109,43 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/f3a8-hmpp",
+            "issued": "2022-01-14",
+            "keyword": [
+                "healthy people 2020"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/foundation-health-measures.htm",
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
+            "temporal": "2010-01-01/2018-12-31",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Healthy People 2020 Foundation Health Measures"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -95190,44 +95168,46 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://www.cdc.gov/respiratory-viruses/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-10-02",
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
-            "identifier": "https://data.cdc.gov/api/views/uqxy-gepz",
             "description": "\u2022\tWeekly RSV Vaccination Coverage, Pregnant Women 18-49 Years Old by Race and Ethnicity \n \n\u2022       Weekly RSV vaccination coverage estimates for pregnant women ages 18\u201349 years are based on electronic health record (EHR) data from the Vaccine Safety Datalink (VSD) (https://www.cdc.gov/vaccine-safety-systems/vsd/), a collaboration between CDC\u2019s Immunization Safety Office and multiple integrated health care organizations.",
-            "title": "Weekly Respiratory Syncytial Virus (RSV) Vaccination Coverage among Pregnant or Recently Pregnant Women 18-49 Years, by Race and Ethnicity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95250,45 +95230,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/uqxy-gepz",
+            "issued": "2024-10-02",
+            "keyword": [
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "rsv vaccination",
+                "vsd"
+            ],
+            "landingPage": "https://www.cdc.gov/respiratory-viruses/index.html",
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
+            "spatial": "United States",
+            "temporal": "2024-2025",
             "theme": [
                 "Pregnancy & Vaccination"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Respiratory Syncytial Virus (RSV) Vaccination Coverage among Pregnant or Recently Pregnant Women 18-49 Years, by Race and Ethnicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kycx-quy6",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-09-28",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-25",
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
-            "identifier": "fc3c7c14-4b08-59c2-97db-0726e478dfdf",
             "description": "Performance rates on frequently reported health care quality measures in the CMS Medicaid/CHIP Child and Adult Core Sets, for FFY 2016 reporting.\r\n\r\nSource: Mathematica analysis of MACPro and Form CMS-416 reports for the FFY 2016 reporting cycle. For more information, see the <a href=\"https://www.medicaid.gov/medicaid/quality-of-care/performance-measurement/child-core-set/index.html\">Children's Health Care Quality Measures</a> and <a href=\"https://www.medicaid.gov/medicaid/quality-of-care/performance-measurement/adult-core-set/index.html\">Adult Health Care Quality Measures</a> webpages.",
-            "title": "2016 Child and Adult Health Care Quality Measures",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95297,49 +95280,41 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "fc3c7c14-4b08-59c2-97db-0726e478dfdf",
+            "issued": "2017-09-28",
+            "keyword": [
+                "core sets",
+                "performance rates",
+                "quality measures"
+            ],
+            "landingPage": "https://healthdata.gov/d/kycx-quy6",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2018-10-25",
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
+            "title": "2016 Child and Adult Health Care Quality Measures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/53g5-jf7x",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-08",
-            "temporal": "2020-12-06/2024-02-04",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "influenza",
-                "mortality",
-                "nchs",
-                "respiratory-virus-response",
-                "rsv",
-                "united-states",
-                "weekly"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov "
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/53g5-jf7x",
             "description": "This file contains the provisional percent of total deaths by week for COVID-19, Influenza, and Respiratory Syncytial Virus for deaths occurring among residents in the United States, by sex, age group, and race and Hispanic origin. Provisional data are based on non-final counts of deaths based on the flow of mortality data in National Vital Statistics System.",
-            "title": "Provisional Percent of Deaths for COVID-19, Influenza, and RSV by Select Characteristics",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95362,86 +95337,94 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/53g5-jf7x",
+            "issued": "2024-11-08",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "influenza",
+                "mortality",
+                "nchs",
+                "respiratory-virus-response",
+                "rsv",
+                "united-states",
+                "weekly"
+            ],
+            "landingPage": "https://data.cdc.gov/d/53g5-jf7x",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-24",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2020-12-06/2024-02-04",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional Percent of Deaths for COVID-19, Influenza, and RSV by Select Characteristics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/kzpu-ckqv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-12",
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
-            "identifier": "7081da9c-0c0a-5099-a546-a57e2896fd5f",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt filters v2.10.16 (coreset-dev0)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/version.csv",
-                    "description": "CoreSEt filters v2.10.16 (coreset-dev0)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt filters v2.10.16 (coreset-dev0)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/version.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt filters v2.10.16 (coreset-dev0)"
                 }
             ],
+            "identifier": "7081da9c-0c0a-5099-a546-a57e2896fd5f",
+            "issued": "2024-11-13",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/kzpu-ckqv",
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
+            "title": "CoreSEt filters v2.10.16 (coreset-dev0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/u5yv-9uts",
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
-            "identifier": "https://data.cdc.gov/api/views/u5yv-9uts",
             "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 7 - Kansas City",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95464,35 +95447,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/u5yv-9uts",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/u5yv-9uts",
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
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 7 - Kansas City"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fveu-vvk9",
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
-            "identifier": "https://data.cdc.gov/api/views/fveu-vvk9",
             "description": "E-cigarettes utilize a wide range of flavoring chemicals whose respiratory health effects are not well understood. In this study, we used pulmonary-associated cell lines to assess the in vitro cytotoxic effects of thirty flavoring chemicals. Human bronchial epithelial cells (BEAS-2B) and both na\u00efve and activated macrophages (THP-1) were treated with 10, 100, and 1000 \u00b5M of flavoring chemicals and analyzed for changes in viability, cell membrane damage, reactive oxygen species (ROS) production, and inflammatory cytokine release. Viability was most greatly affected by decanal, hexanal, nonanal, cinnamaldehyde, eugenol, vanillin, alpha-pinene, eugenol, and limonene. High amounts of ROS were elicited by vanillin, ethyl maltol, and the diketones (2,3-pentanedione, 2,3-heptanedione, and 2,3-hexanedione) from both cell lines. Na\u00efve THP-1 cells produced significant levels of IL-1\u03b2, IL-8, and TNF-\u03b1 when exposed to ethyl maltol and hexanal. Activated THP-1 cells released increased IL-1\u03b2 and TNF-\u03b1 when exposed to ethyl maltol, but many flavoring chemicals had an apparent suppressive effect on inflammatory cytokines released by activated macrophages, with varying degrees of accompanying cytotoxicity. The diketones, L-carvone, and linalool, suppressed cytokine release in the absence of cytotoxicity. These findings provide insight into patterns of cytotoxicity and inflammatory cytokine release potentially relevant to the development of pathological changes in the lungs of e-cigarette users.",
-            "title": "Effects of E-Cigarette Flavoring Chemicals on Human Macrophages and Bronchial Epithelial Cells",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95500,40 +95487,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fveu-vvk9",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/fveu-vvk9",
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
+            "title": "Effects of E-Cigarette Flavoring Chemicals on Human Macrophages and Bronchial Epithelial Cells"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mr8w-325u",
             "bureauCode": [
                 "009:000"
             ],
-            "issued": "2016-10-06",
-            "@type": "dcat:Dataset",
-            "modified": "2016-10-06",
-            "keyword": [
-                "122 cities",
-                "mmwr table iii",
-                "mortality"
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
-            "identifier": "https://data.cdc.gov/api/views/mr8w-325u",
             "description": "This file contains the complete set of data reported to 122 Cities Mortality Reposting System.  The system was retired as of 10/6/2016.  While the system was running each week, the vital statistics offices of 122 cities across the United States reported the total number of death certificates processed and the number of those for which pneumonia or influenza was listed as the underlying or contributing cause of death by age group (Under 28 days, 28 days - 1 year, 1-14 years, 15-24 years, 25-44 years, 45-64 years, 65-74 years, 75-84 years, and - 85 years).  U:Unavailable. - : No reported cases.* Mortality data in this table were voluntarily reported from 122 cities in the United States, most of which have populations of >100,000. A death is reported by the place of its occurrence and by the week that the death certificate was filed. Fetal deaths are not included.  Total includes unknown ages. \nMore information on Flu Activity & Surveillance is available at http://www.cdc.gov/flu/weekly/fluactivitysurv.htm.",
-            "title": "Deaths in 122 U.S. cities - 1962-2016. 122 Cities Mortality Reporting System",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95556,35 +95538,37 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/mr8w-325u",
+            "issued": "2016-10-06",
+            "keyword": [
+                "122 cities",
+                "mmwr table iii",
+                "mortality"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mr8w-325u",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-10-06",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "Deaths in 122 U.S. cities - 1962-2016. 122 Cities Mortality Reporting System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/xjqa-xcwb",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2018-09-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "disaster information"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/xjqa-xcwb",
             "description": "This resource was retired on June 1, 2021 and is no longer updated. These data remain available to support research and development efforts.\n\nDisaster Lit\u00ae: Database for Disaster Medicine and Public Health is a dataset of links to disaster medicine and public health documents available on the Internet at no cost. Documents include expert guidelines, research reports, conference proceedings, training classes, factsheets, websites, databases, and similar materials selected from over 700 organizations for a professional audience. Materials were selected from non-commercial publishing sources and supplement disaster-related resources from PubMed (biomedical journal literature) and MedlinePlus (health information for the public).",
-            "title": "Disaster Lit",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95607,20 +95591,62 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/xjqa-xcwb",
+            "issued": "2018-09-17",
+            "keyword": [
+                "disaster information"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/xjqa-xcwb",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-04",
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
+            "title": "Disaster Lit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/dwqk-w36f",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "NNDSS - Table I. infrequently reported notifiable diseases - 2016.  In this Table, provisional* cases of selected\u2020 infrequently reported notifiable diseases (<1,000 cases reported during the preceding year) are displayed.  \r\nNote:\r\n\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in these tables are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\n\u201cSymbols and footnotes changed in week #4, please refer to the MMWR publication for the symbols/footnotes for weeks 1, 2, and 3\u201d.\r\n\r\nFootnote:\r\n-: No reported cases    N: Not reportable    NA: Not available NN: Not Nationally Notifiable.  NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.\r\n* Case counts for reporting year 2016 are provisional and subject to change.  Data for years 2011 through 2015 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. \r\n\u2020 This table does not include cases from the U.S. territories. Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions.  \r\n\u00a7 Calculated by summing the incidence counts for the current week, the 2 weeks preceding the current week, and the 2 weeks following the current week, for a total of 5 preceding years.  Additional information is available at http://wwwn.cdc.gov/nndss/document/5yearweeklyaverage.pdf. \r\n\u00b6 Includes both neuroinvasive and nonneuroinvasive. Updated weekly reports from the Division of Vector-Borne Diseases, National Center for Emerging and Zoonotic Infectious Diseases (ArboNET Surveillance). Data for West Nile virus are available in Table II. \r\n** Not reportable in all reporting jurisdictions. Data from states where the condition is not reportable are excluded from this table, except for the arboviral diseases and influenza-associated pediatric mortality. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.\r\n\u2020\u2020 Office of Management and Budget approval of the NNDSS Revision #0920-0728 on January 21, 2016, authorized CDC to receive data for these conditions. CDC is in the process\r\nof soliciting data for these conditions (except Zika virus, congenital infection). CDC and the U.S. states are still modifying the technical infrastructure needed to collect and transmit data for Zika virus congenital infections.\r\n\u00a7\u00a7 Jamestown Canyon virus and Lacrosse virus have replaced California serogroup diseases.\r\n\u00b6\u00b6 Data for Haemophilus influenzae (all ages, all serotypes) are available in Table II.\r\n***  Please refer to the MMWR publication for weekly updates to the footnote for this condition.  \r\n\u2020\u2020\u2020 Please refer to the MMWR publication for weekly updates to the footnote for this condition. \r\n\u00a7\u00a7\u00a7 Data for meningococcal disease (all serogroups) are available in Table II. \r\n\u00b6\u00b6\u00b6 Please refer to the MMWR publication for weekly updates to the footnote for this condition. \r\n**** Updated weekly from reports to the Division of STD Prevention, National Center for HIV/AIDS, Viral Hepatitis, STD, and TB Prevention. \r\n\u2020\u2020\u2020\u2020 Please refer to the MMWR publication for weekly updates to the footnote for this condition. \r\n\u00a7\u00a7\u00a7\u00a7 All cases reported have occurred in travelers returning from affected areas, with their sexual contacts, or infants infected in ute",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dwqk-w36f/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dwqk-w36f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dwqk-w36f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dwqk-w36f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/dwqk-w36f",
             "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
             "keyword": [
                 "2016",
                 "anthrax",
@@ -95683,58 +95709,58 @@
                 "wonder",
                 "yellow fever"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CDC INFO",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/dwqk-w36f",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2017-01-05",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/dwqk-w36f",
-            "description": "NNDSS - Table I. infrequently reported notifiable diseases - 2016.  In this Table, provisional* cases of selected\u2020 infrequently reported notifiable diseases (<1,000 cases reported during the preceding year) are displayed.  \r\nNote:\r\n\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in these tables are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\n\u201cSymbols and footnotes changed in week #4, please refer to the MMWR publication for the symbols/footnotes for weeks 1, 2, and 3\u201d.\r\n\r\nFootnote:\r\n-: No reported cases    N: Not reportable    NA: Not available NN: Not Nationally Notifiable.  NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.\r\n* Case counts for reporting year 2016 are provisional and subject to change.  Data for years 2011 through 2015 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. \r\n\u2020 This table does not include cases from the U.S. territories. Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions.  \r\n\u00a7 Calculated by summing the incidence counts for the current week, the 2 weeks preceding the current week, and the 2 weeks following the current week, for a total of 5 preceding years.  Additional information is available at http://wwwn.cdc.gov/nndss/document/5yearweeklyaverage.pdf. \r\n\u00b6 Includes both neuroinvasive and nonneuroinvasive. Updated weekly reports from the Division of Vector-Borne Diseases, National Center for Emerging and Zoonotic Infectious Diseases (ArboNET Surveillance). Data for West Nile virus are available in Table II. \r\n** Not reportable in all reporting jurisdictions. Data from states where the condition is not reportable are excluded from this table, except for the arboviral diseases and influenza-associated pediatric mortality. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.\r\n\u2020\u2020 Office of Management and Budget approval of the NNDSS Revision #0920-0728 on January 21, 2016, authorized CDC to receive data for these conditions. CDC is in the process\r\nof soliciting data for these conditions (except Zika virus, congenital infection). CDC and the U.S. states are still modifying the technical infrastructure needed to collect and transmit data for Zika virus congenital infections.\r\n\u00a7\u00a7 Jamestown Canyon virus and Lacrosse virus have replaced California serogroup diseases.\r\n\u00b6\u00b6 Data for Haemophilus influenzae (all ages, all serotypes) are available in Table II.\r\n***  Please refer to the MMWR publication for weekly updates to the footnote for this condition.  \r\n\u2020\u2020\u2020 Please refer to the MMWR publication for weekly updates to the footnote for this condition. \r\n\u00a7\u00a7\u00a7 Data for meningococcal disease (all serogroups) are available in Table II. \r\n\u00b6\u00b6\u00b6 Please refer to the MMWR publication for weekly updates to the footnote for this condition. \r\n**** Updated weekly from reports to the Division of STD Prevention, National Center for HIV/AIDS, Viral Hepatitis, STD, and TB Prevention. \r\n\u2020\u2020\u2020\u2020 Please refer to the MMWR publication for weekly updates to the footnote for this condition. \r\n\u00a7\u00a7\u00a7\u00a7 All cases reported have occurred in travelers returning from affected areas, with their sexual contacts, or infants infected in ute",
-            "title": "NNDSS - Table I. infrequently reported notifiable diseases",
-            "programCode": [
-                "009:020"
+            "theme": [
+                "NNDSS"
+            ],
+            "title": "NNDSS - Table I. infrequently reported notifiable diseases"
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
+            "description": "Provisional deaths involving coronavirus disease 2019 (COVID-19) reported to NCHS by age group among United States residents, from MMWR Week 40 2020 through MMWR Week 39 2021.\n\nAge groups: 0-4, 5-11, 12-15, 16-17, 18-24, 25-39, 40-49, 50-64, 65-74, and 75+ years",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/dwqk-w36f/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/mawz-airi/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/dwqk-w36f/rows.rdf?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/mawz-airi/rows.rdf?accessType=DOWNLOAD",
                     "mediaType": "application/rdf+xml"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/dwqk-w36f/rows.json?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/mawz-airi/rows.json?accessType=DOWNLOAD",
                     "mediaType": "application/json"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/dwqk-w36f/rows.xml?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/mawz-airi/rows.xml?accessType=DOWNLOAD",
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "theme": [
-                "NNDSS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/mawz-airi",
             "issued": "2021-10-06",
-            "@type": "dcat:Dataset",
-            "temporal": "2020/2021",
-            "modified": "2022-03-28",
             "keyword": [
                 "age",
                 "age group",
@@ -95748,82 +95774,36 @@
                 "provisional",
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
-            "identifier": "https://data.cdc.gov/api/views/mawz-airi",
-            "description": "Provisional deaths involving coronavirus disease 2019 (COVID-19) reported to NCHS by age group among United States residents, from MMWR Week 40 2020 through MMWR Week 39 2021.\n\nAge groups: 0-4, 5-11, 12-15, 16-17, 18-24, 25-39, 40-49, 50-64, 65-74, and 75+ years",
-            "title": "AH Provisional COVID-19 Deaths by Age, United States, Week 40 2020 through Week 39 2021",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-03-28",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/mawz-airi/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/mawz-airi/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/mawz-airi/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/mawz-airi/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2020/2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by Age, United States, Week 40 2020 through Week 39 2021"
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
-                "legislation",
-                "licensure",
-                "osh",
-                "policy",
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
-            "identifier": "https://data.cdc.gov/api/views/eb4y-d4ic",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Licensure/eb4y-d4ic",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation\u2014Licensure. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies.  Data are reported on a quarterly basis. Data include information related to requirements, restrictions and penalties associated with holding a retail license to sell tobacco products over-the-counter and through vending machines.",
-            "title": "CDC STATE System Tobacco Legislation - Licensure",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95846,39 +95826,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Licensure/eb4y-d4ic",
+            "identifier": "https://data.cdc.gov/api/views/eb4y-d4ic",
+            "issued": "2023-07-18",
+            "keyword": [
+                "legislation",
+                "licensure",
+                "osh",
+                "policy",
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
             "theme": [
                 "Legislation"
-            ]
+            ],
+            "title": "CDC STATE System Tobacco Legislation - Licensure"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/shelleggsrecall/ShellEggsRecallList2010.xml",
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
-            "identifier": "2e20dcb3-74a1-46e1-a7bd-900b78dd0355",
             "description": "Epidemiologic investigations conducted by health officials in California, Colorado, and Minnesota revealed several restaurants or events where more than one person who fell ill with Salmonella Enteriditis had eaten. Information from these investigations suggested that shell eggs were the likely source of infections in many of these restaurants or events. And on August 13, 2010, Wright County Egg of Galt, Iowa, conducted a nationwide voluntary recalls of shell eggs that it had shipped since May 19, 2010.",
-            "title": "Shell Egg Recalls",
-            "programCode": [
-                "009:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95886,42 +95871,36 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "2e20dcb3-74a1-46e1-a7bd-900b78dd0355",
+            "issued": "2021-02-25",
+            "keyword": [
+                "recalls"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/shelleggsrecall/ShellEggsRecallList2010.xml",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "irregular"
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/nis/",
-            "bureauCode": [
-                "009:20"
+            "modified": "1900-01-01",
+            "programCode": [
+                "009:001"
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
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Shell Egg Recalls"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "Approximately Monthly",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCIRD",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ty79-wym3",
             "description": "Cumulative Influenza Vaccination Coverage by Age Group, Race/Ethnicity, Urbanicity and Jurisdiction, NIS-ACM, Adults 18 Years and Older, United States, National Immunization Survey-Adult COVID Module. Archived data are available at the following locations: \n1. https://data.cdc.gov/resource/8dyx-9z99 \n2. https://data.cdc.gov/resource/3myw-4j4q\n\n\u2022 The National Immunization Survey-Adult COVID Module (NIS-ACM) was launched in April 2021 among adults 18 years and older. The survey was used to monitor COVID-19 vaccination uptake and confidence in vaccination among adults and included questions about influenza vaccination.",
-            "title": "Cumulative Influenza Vaccination Coverage by Age Group, Race/Ethnicity, Urbanicity and Jurisdiction, NIS-ACM, Adults 18 Years and Older - NIS ACM",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95944,27 +95923,59 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, District of Columbia, US Virgin Islands, and Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/ty79-wym3",
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
+            "title": "Cumulative Influenza Vaccination Coverage by Age Group, Race/Ethnicity, Urbanicity and Jurisdiction, NIS-ACM, Adults 18 Years and Older - NIS ACM"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/rch2-p4nb",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS2_technical_documentation.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional \nsurveys from probability-sampled commercial survey panels which began in 2015. \nRANDS 2 was administered by Gallup using the Gallup Panel in the spring of 2016 \nand contains existing questions from the National Health Interview Survey (NHIS) \nas well as embedded probe questions for cognitive evaluations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/rch2-p4nb",
             "issued": "2022-06-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2016",
-            "modified": "2023-04-20",
             "keyword": [
                 "anxiety",
                 "chronic conditions",
@@ -95974,66 +95985,37 @@
                 "physical activity",
                 "research-data-center"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/rch2-p4nb",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-04-20",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/rch2-p4nb",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional \nsurveys from probability-sampled commercial survey panels which began in 2015. \nRANDS 2 was administered by Gallup using the Gallup Panel in the spring of 2016 \nand contains existing questions from the National Health Interview Survey (NHIS) \nas well as embedded probe questions for cognitive evaluations.",
-            "title": "NCHS Research and Development Survey (RANDS) Round 2 Restricted File",
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
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS2_technical_documentation.pdf",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "2016",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 2 Restricted File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/m52a-sqhk",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-10-24",
-            "@type": "dcat:Dataset",
-            "modified": "2021-10-22",
-            "keyword": [
-                "exchange puf",
-                "marketplace puf",
-                "plan id crosswalk",
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
-            "identifier": "db1b95d1-b2e9-4413-8cf5-2f851f80b44f",
             "description": "The Plan ID Crosswalk PUF (CW-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The purpose of the CW-PUF is to map QHPs and SADPs offered through the Exchanges during the previous plan year to plans that will be offered through the Exchanges in the current plan year.",
-            "title": "Plan ID Crosswalk PUF \u2013 PY2022",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -96041,38 +96023,38 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "db1b95d1-b2e9-4413-8cf5-2f851f80b44f",
+            "issued": "2021-10-24",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "plan id crosswalk",
+                "py2022"
+            ],
+            "landingPage": "https://healthdata.gov/d/m52a-sqhk",
+            "modified": "2021-10-22",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Plan ID Crosswalk PUF \u2013 PY2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/m563-snjf",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2017-12-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-16",
-            "keyword": [
-                "comprehensive managed care",
-                "enrollment",
-                "managed care",
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
-            "identifier": "79692ea5-21e1-56bf-8149-97d437120c4b",
             "description": "The Share of Medicaid Enrollees in any Managed Care and in Comprehensive Managed CaAre profiles state-level enrollment statistics (numbers and percentages) of total Medicaid enrollees in any type of managed care as well as those enrolled specifically in comprehensive managed care programs. The report provides managed care enrollment by state with all 50 states, the District of Columbia and the US territories are represented in these data.\r\n\r\n1. Note: \"n/a\" indicates that a state or territory was not able to report data or does not have a managed care program.\r\n\r\n2. The \u201cTotal Medicaid Enrollees\u201d column represents an unduplicated count of all beneficiaries in FFS and any type of managed care, including Medicaid-only and dually eligible individuals receiving full Medicaid benefits or Medicaid cost sharing.\r\n\r\n3. The \u201cTotal Medicaid Enrollment in Any Type of Managed Care\u201d column represents an unduplicated count of beneficiaries enrolled in any Medicaid managed care program, including comprehensive MCOs, limited benefit MCOs, PCCMs, and PCCM entities.\r\n\r\n4. The \u201cMedicaid Enrollment in Comprehensive Managed Care\u201d column represents an unduplicated count of Medicaid beneficiaries enrolled in a managed care plan that provides comprehensive benefits (acute, primary care, specialty, and any other), as well as PACE programs. It excludes beneficiaries who are enrolled in a Financial Alignment Initiative Medicare-Medicaid Plan as their only form of managed care.",
-            "title": "Share of Medicaid Enrollees in Managed Care",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -96081,50 +96063,45 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "79692ea5-21e1-56bf-8149-97d437120c4b",
+            "issued": "2017-12-05",
+            "keyword": [
+                "comprehensive managed care",
+                "enrollment",
+                "managed care",
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/m563-snjf",
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
+            "title": "Share of Medicaid Enrollees in Managed Care"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/provider-of-services-file-hospital-non-hospital-facilities",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2011-10-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "references": [
-                "https://data.cms.gov/resources/provider-of-services-file-methodology"
-            ],
-            "keyword": [
-                "hospitals & facilities",
-                "inpatient",
-                "medicare",
-                "medicare advantage",
-                "original medicare",
-                "outpatient facilities",
-                "provider enrollment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "QIESData - CCSQ",
                 "hasEmail": "mailto:QIESData@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/8ba0f9b4-9493-4aa0-9f82-44ea9468d1b5/data-viewer",
-            "description": "Please be advised that as of Q4 2023 there is a new Provider of Service file (POS) that contains the provider and certification details for Home Health Agencies (HHAs), Hospices, and Ambulatory Surgical Centers (ASCs). Data contained in this file are extracted from the Internet Quality Improvement and Evaluation System (iQIES) environment and will be updated quarterly along with the other two POS files.\n\n\u00a0\n\nThe Provider of Services File - Hospital & Non-Hospital Facilities data\u00a0provide critical resources for other federal regulator requirements as well as supports the ongoing quality & research efforts sponsored by CMS. In this file you will find provider certification, termination, accreditation, ownership, name, location and other characteristics organized by CMS Certification Number.",
-            "title": "Provider of Services File - Hospital & Non-Hospital Facilities",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-07/0ca58d5d-7914-4532-b22d-41741d3e6151/P.QWB.POSQ.OTHER.LAYOUT.MAR23.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "Please be advised that as of Q4 2023 there is a new Provider of Service file (POS) that contains the provider and certification details for Home Health Agencies (HHAs), Hospices, and Ambulatory Surgical Centers (ASCs). Data contained in this file are extracted from the Internet Quality Improvement and Evaluation System (iQIES) environment and will be updated quarterly along with the other two POS files.\n\n\u00a0\n\nThe Provider of Services File - Hospital & Non-Hospital Facilities data\u00a0provide critical resources for other federal regulator requirements as well as supports the ongoing quality & research efforts sponsored by CMS. In this file you will find provider certification, termination, accreditation, ownership, name, location and other characteristics organized by CMS Certification Number.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -96505,45 +96482,51 @@
                     "title": "Provider of Services File - Hospital & Non-Hospital Facilities : 2011-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2023-07/0ca58d5d-7914-4532-b22d-41741d3e6151/P.QWB.POSQ.OTHER.LAYOUT.MAR23.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/8ba0f9b4-9493-4aa0-9f82-44ea9468d1b5/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "hospitals & facilities",
+                "inpatient",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "outpatient facilities",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/provider-of-services-file-hospital-non-hospital-facilities",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/provider-of-services-file-methodology"
+            ],
+            "temporal": "2011-10-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Provider of Services File - Hospital & Non-Hospital Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ea3z-m7eh",
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
-            "identifier": "https://data.cdc.gov/api/views/ea3z-m7eh",
             "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 7 - Kansas City",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -96566,97 +96549,86 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ea3z-m7eh",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ea3z-m7eh",
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
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 7 - Kansas City"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/m64t-cgek",
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
-            "identifier": "8f705c5d-9b20-548a-bb44-849d2839aa91",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet version v2.10.64 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/version.csv",
-                    "description": "CoreSet version v2.10.64 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet version v2.10.64 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/version.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet version v2.10.64 (coreset-etl-test)"
                 }
             ],
+            "identifier": "8f705c5d-9b20-548a-bb44-849d2839aa91",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/m64t-cgek",
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
+            "title": "CoreSet version v2.10.64 (coreset-etl-test)"
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
-                "census tract",
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
-            "identifier": "https://data.cdc.gov/api/views/em5e-5hvn",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh",
             "description": "This dataset contains model-based census tract estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 36 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population data, and American Community Survey 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for seven measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, Census Tract Data 2023 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -96679,46 +96651,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh",
+            "identifier": "https://data.cdc.gov/api/views/em5e-5hvn",
+            "issued": "2024-07-15",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "census tract",
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
+            "title": "PLACES: Local Data for Better Health, Census Tract Data 2023 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "nephtrackingsupport@cdc.gov",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-09-19",
-            "@type": "dcat:Dataset",
-            "temporal": "2016,2017,2018,2019,2020",
-            "modified": "2024-03-08",
-            "keyword": [
-                "air pollution",
-                "air quality",
-                "asthma",
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
-            "identifier": "https://data.cdc.gov/api/views/hf2a-3ebq",
             "description": "This dataset provides modeled predictions of ozone levels from the EPA's Downscaler model. Data are at the census tract level for 2016-2020. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information. Learn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action. By using these data, you signify your agreement to comply with the following requirements: 1. Use the data for statistical reporting and analysis only. 2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. 3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. 4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. 5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC. 6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network.Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily Census Tract-Level Ozone Concentrations, 2016 - 2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -96741,57 +96718,59 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "National",
+            "identifier": "https://data.cdc.gov/api/views/hf2a-3ebq",
+            "issued": "2023-09-19",
+            "keyword": [
+                "air pollution",
+                "air quality",
+                "asthma",
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
+            "modified": "2024-03-08",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "National",
+            "temporal": "2016,2017,2018,2019,2020",
             "theme": [
                 "Environmental Health & Toxicology"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Daily Census Tract-Level Ozone Concentrations, 2016 - 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/federally-qualified-health-center-all-owners",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/ed289c89-0bb8-4221-a20a-85776066381b/data-viewer",
-            "description": "The\u00a0Federally Qualified Health Center (FQHC) All Owners dataset provides ownership information on all\u00a0FQHCs currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
-            "title": "Federally Qualified Health Center All Owners",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/FQHC_All_Owners_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The\u00a0Federally Qualified Health Center (FQHC) All Owners dataset provides ownership information on all\u00a0FQHCs currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ed289c89-0bb8-4221-a20a-85776066381b/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ed289c89-0bb8-4221-a20a-85776066381b/data",
+                    "mediaType": "text/html",
                     "title": "Federally Qualified Health Center All Owners : 2025-01-01"
                 },
                 {
@@ -96867,57 +96846,50 @@
                     "title": "Federally Qualified Health Center All Owners : 2023-10-28"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/FQHC_All_Owners_Data_Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/ed289c89-0bb8-4221-a20a-85776066381b/data-viewer",
+            "issued": "2023-12-08",
+            "keyword": [
+                "federally qualified health centers",
+                "hospitals & facilities",
+                "medicare",
+                "outpatient facilities",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/federally-qualified-health-center-all-owners",
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
+            "title": "Federally Qualified Health Center All Owners"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-08-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-12",
-            "keyword": [
-                "age",
-                "age group",
-                "children",
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
-            "identifier": "https://data.cdc.gov/api/views/nr4s-juj3",
             "description": "Effective June 28, 2023, this dataset will no longer be updated. Similar data are accessible from CDC WONDER (https://wonder.cdc.gov/mcd-icd10-provisional.html).\n\nDeaths involving coronavirus disease 2019 (COVID-19) with a focus on ages 0-18 years in the United States.",
-            "title": "Provisional COVID-19 Deaths: Focus on Ages 0-18 Years",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -96940,56 +96912,61 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/nr4s-juj3",
+            "issued": "2020-08-05",
+            "keyword": [
+                "age",
+                "age group",
+                "children",
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
+            "title": "Provisional COVID-19 Deaths: Focus on Ages 0-18 Years"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/innovation-center-webinars-and-forums",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2024-06-01/2024-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-21",
-            "references": [
-                "https://data.cms.gov/resources/webinars-and-forums-methodology"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/cc3bd6db-2ae9-4d86-95be-20267f159f73/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/webinars-and-forums-data-dictionary",
             "description": "The Innovation Center Webinars and Forums dataset contains listings of a variety of events from CMS Innovation Center models, demonstrations, initiatives and programs. The types of events include webinars, open door forums, office hours and conference calls among others. These events provide opportunities to learn about current activity, upcoming proceedings and to ask questions and offer feedback.",
-            "title": "Innovation Center Webinars and Forums",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cc3bd6db-2ae9-4d86-95be-20267f159f73/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cc3bd6db-2ae9-4d86-95be-20267f159f73/data",
+                    "mediaType": "text/html",
                     "title": "Innovation Center Webinars and Forums : 2024-06-21"
                 },
                 {
@@ -97005,63 +96982,61 @@
                     "title": "Innovation Center Webinars and Forums : 2024-06-21"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/webinars-and-forums-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/cc3bd6db-2ae9-4d86-95be-20267f159f73/data-viewer",
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
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/innovation-center-webinars-and-forums",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2024-06-21",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/webinars-and-forums-methodology"
+            ],
+            "temporal": "2024-06-01/2024-06-30",
             "theme": [
                 "Medicare",
                 "Children's Health Insurance Program"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Innovation Center Webinars and Forums"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/end-stage-renal-disease-treatment-choices-model/managing-clinician-aggregation-group-performance",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/6a0dbf98-e4b0-4037-ac63-1439b08f4a71/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/managing-clinician-aggregation-group-performance-data-dictionary",
             "description": "The\u00a0Managing Clinician Aggregation Group Performance dataset provides performance information in the End-Stage Renal Disease (ESRD) Treatment Choices (ETC) Model. The dataset includes information on Performance Payment Adjustment (PPA), Modality Performance Score (MPS), home dialysis rate, and transplant rate, as well as the individual components of each rate for each model participant Managing Clinician\u00a0aggregation group.\n\n\u00a0\n\nAll Managing Clinicians within the same aggregation group share the same performance information. The supplementary aggregation group crosswalk file may be used to map aggregation groups to individual ETC Participant Managing Clinicians.",
-            "title": "Managing Clinician Aggregation Group Performance",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6a0dbf98-e4b0-4037-ac63-1439b08f4a71/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6a0dbf98-e4b0-4037-ac63-1439b08f4a71/data",
+                    "mediaType": "text/html",
                     "title": "Managing Clinician Aggregation Group Performance : 2023-06-01"
                 },
                 {
@@ -97113,53 +97088,54 @@
                     "title": "Managing Clinician Aggregation Group Performance : 2021-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/managing-clinician-aggregation-group-performance-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/6a0dbf98-e4b0-4037-ac63-1439b08f4a71/data-viewer",
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
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/end-stage-renal-disease-treatment-choices-model/managing-clinician-aggregation-group-performance",
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
+            "title": "Managing Clinician Aggregation Group Performance"
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
-            "modified": "2024-09-19",
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
-            "identifier": "https://data.cdc.gov/api/views/d2rk-yvas",
+            "describedBy": "https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-A/d2rk-yvas",
             "description": "2011 to present. BRFSS combined land line and cell phone age-adjusted prevalence data. The BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. \nData will be updated annually as it becomes available.\n\nDetailed information on sampling methodology and quality assurance can be found on the BRFSS website (http://www.cdc.gov/brfss). \nMethodology: http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf \nGlossary: https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct",
-            "title": "Behavioral Risk Factor Surveillance System (BRFSS) Age-Adjusted Prevalence Data (2011 to present)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97182,40 +97158,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-A/d2rk-yvas",
+            "identifier": "https://data.cdc.gov/api/views/d2rk-yvas",
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
+            "modified": "2024-09-19",
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
+            "title": "Behavioral Risk Factor Surveillance System (BRFSS) Age-Adjusted Prevalence Data (2011 to present)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/pvr7-gpk4",
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
-            "identifier": "https://data.cdc.gov/api/views/pvr7-gpk4",
             "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012, 2014.",
-            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days),  2012 & 2014, Region 7 - Kansas City",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97238,53 +97221,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/pvr7-gpk4",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/pvr7-gpk4",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days),  2012 & 2014, Region 7 - Kansas City"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/aco-realizing-equity-access-and-community-health/aco-realizing-equity-access-and-community-health-financial-and-quality-results",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-06-27",
-            "temporal": "2021-01-01/2021-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-12",
-            "references": [
-                "https://data.cms.gov/resources/aco-realizing-equity-access-and-community-health-aco-reach-model-methodology"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/6c3532b3-8325-48fd-a939-12b41d2b126a/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/aco-reach-financial-and-quality-results-data-dictionary",
             "description": "The Accountable Care Organization Realizing Equity, Access and Community Health (ACO REACH) Model Financial and Quality Results Public Use File (PUF) details performance for the ACO REACH Model, formerly Global and Professional Direct Contracting (GPDC) Model, prior to settlement. This data includes information such as the ACOs risk arrangement, stop loss, capitation, savings rate, and quality results.\u00a0\n\n\u00a0\n\nThe expanded quality performance results are expected to be released in the fall.",
-            "title": "ACO Realizing Equity, Access and Community Health Financial and Quality Results",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6c3532b3-8325-48fd-a939-12b41d2b126a/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6c3532b3-8325-48fd-a939-12b41d2b126a/data",
+                    "mediaType": "text/html",
                     "title": "ACO Realizing Equity, Access and Community Health Financial and Quality Results : 2021-12-31"
                 },
                 {
@@ -97300,45 +97278,50 @@
                     "title": "ACO Realizing Equity, Access and Community Health Financial and Quality Results : 2021-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/aco-reach-financial-and-quality-results-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/6c3532b3-8325-48fd-a939-12b41d2b126a/data-viewer",
+            "issued": "2023-06-27",
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/aco-realizing-equity-access-and-community-health/aco-realizing-equity-access-and-community-health-financial-and-quality-results",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-01-12",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/aco-realizing-equity-access-and-community-health-aco-reach-model-methodology"
+            ],
+            "temporal": "2021-01-01/2021-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACO Realizing Equity, Access and Community Health Financial and Quality Results"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/Structure/CN3D/cn3d.shtml",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "molecular biology",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/y4ra-85if",
             "description": "A stand-alone application for viewing 3-dimensional structures from NCBI Entrez retrieval service. Runs on Windows, Macintosh, and UNIX and can be configured to receive data from most popular Web browsers.",
-            "title": "Cn3D",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97347,45 +97330,39 @@
                     "title": "Cn3D Application Homepage"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/y4ra-85if",
+            "issued": "2021-06-30",
+            "keyword": [
+                "molecular biology",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/Structure/CN3D/cn3d.shtml",
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
+            "title": "Cn3D"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9d9z-vf8f",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-            "identifier": "https://data.cdc.gov/api/views/9d9z-vf8f",
             "description": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97408,40 +97385,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9d9z-vf8f",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "anaplasma phagocytophilum infection",
+                "ehrlichia chaffeensis infection",
+                "ehrlichiosis and anaplasmosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9d9z-vf8f",
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
+            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mann-88zm",
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
-            "identifier": "c39d3302-2d39-5209-9310-388ab1c8cbb8",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 1999",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97449,41 +97432,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "c39d3302-2d39-5209-9310-388ab1c8cbb8",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/mann-88zm",
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
+            "title": "State Drug Utilization Data 1999"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://ucum.nlm.nih.gov/ucum-service.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ecgi-98tx",
             "description": "A web API service for validating and converting unit expressions from the Unified Code for Units of Measure (UCUM). http://unitsofmeasure.org/trac",
-            "title": "UCUM Web API Service",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97504,96 +97486,87 @@
                     "title": "UCUM unit to base units conversion"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ecgi-98tx",
+            "issued": "2021-06-30",
+            "keyword": [
+                "api",
+                "health data standards",
+                "terminologies"
+            ],
+            "landingPage": "https://ucum.nlm.nih.gov/ucum-service.html",
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
+            "title": "UCUM Web API Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mbgv-9wrx",
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
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "CoreSet pillar v2.10.64 (coreset-impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/pillar.csv",
+                    "mediaType": "text/csv",
+                    "title": "CoreSet pillar v2.10.64 (coreset-impl)"
+                }
+            ],
+            "identifier": "b4e5caf6-bdb0-5700-9c29-eff99f1298cf",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/mbgv-9wrx",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-10",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Medicare & Medicaid Services"
             },
-            "identifier": "b4e5caf6-bdb0-5700-9c29-eff99f1298cf",
-            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet pillar v2.10.64 (coreset-impl)",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/pillar.csv",
-                    "description": "CoreSet pillar v2.10.64 (coreset-impl)",
-                    "@type": "dcat:Distribution",
-                    "title": "CoreSet pillar v2.10.64 (coreset-impl)"
-                }
+            "references": [
+                "https://www.mathematica.org/"
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Uncategorized"
-            ]
+            ],
+            "title": "CoreSet pillar v2.10.64 (coreset-impl)"
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
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DDT Public Inquiries",
                 "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/tdbk-8ubw",
+            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/National-Health-and-Nutrition-Examination-Survey-N/tdbk-8ubw",
             "description": "1999-2008; 2005-2008. This dataset is a de-identified summary table of vision and eye health data indicators from NHANES, stratified by all available combinations of age group, race/ethnicity, gender, and risk factor. NHANES is a program of studies conducted by the National Center for Health Statistics at CDC designed to assess the health and nutritional status of adults and children in the U.S, and combines interviews and physical examinations. NHANES stopped collecting vision and eye health data in 2008. Approximate sample size is 5,000 persons per year. NHANES data for VEHSS includes questions and examinations related to Visual Function, Vision Exam Measures, Eye Health Conditions, Service Utilization, and Examination Measures. Data were suppressed for cell sizes less than 30 persons, or where the relative standard error more than 30% of the mean. Detailed information on VEHSS NHANES analyses can be found on the VEHSS NHANES webpage (https://www.cdc.gov/visionhealth/vehss/data/national-surveys/national-health-and-nutrition-examination-survey.html). Additional information about NHANES can be found on the NHANES website (https://www.cdc.gov/nchs/nhanes/index.htm). The VEHSS NHANES dataset was last updated in June 2018.",
-            "title": "National Health and Nutrition Examination Survey (NHANES) \u2013 Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97616,40 +97589,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/National-Health-and-Nutrition-Examination-Survey-N/tdbk-8ubw",
+            "identifier": "https://data.cdc.gov/api/views/tdbk-8ubw",
+            "issued": "2023-09-21",
+            "keyword": [
+                "blind",
+                "cataract",
+                "diabetes",
+                "glaucoma",
+                "nhanes",
+                "service utilization",
+                "vision exam measures",
+                "visual acuity",
+                "visual function"
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
+                "https://www.cdc.gov/nchs/nhanes/index.htm",
+                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/national-health-and-nutrition-examination-survey.html"
+            ],
             "theme": [
                 "Vision & Eye Health"
-            ]
+            ],
+            "title": "National Health and Nutrition Examination Survey (NHANES) \u2013 Vision and Eye Health Surveillance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mbsy-7qjz",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-07-13",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-24",
-            "keyword": [
-                "enrollment strategies",
-                "presumptive eligibility"
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
-            "identifier": "47329369-e935-5de3-880f-d6a85a5fe9d1",
             "description": "Health care providers and Head Start programs can play a major role in finding and enrolling uninsured children through presumptive eligibility. States can authorize \u201cqualified entities\u201d -- health care providers, community-based organizations, and schools, among others -- to screen for Medicaid and CHIP eligibility and immediately enroll children who appear to be eligible.\r\n\r\nPresumptive eligibility allows children to get access to Medicaid or CHIP services without having to wait for their application to be fully processed. Qualified entities can also help families gather the documents needed to complete the full application process, thereby reducing the administrative burden on States to obtain missing information.",
-            "title": "Presumptive Eligibility for Medicaid and CHIP Coverage",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97658,82 +97642,85 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "47329369-e935-5de3-880f-d6a85a5fe9d1",
+            "issued": "2016-07-13",
+            "keyword": [
+                "enrollment strategies",
+                "presumptive eligibility"
+            ],
+            "landingPage": "https://healthdata.gov/d/mbsy-7qjz",
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
                 "Eligibility"
-            ]
+            ],
+            "title": "Presumptive Eligibility for Medicaid and CHIP Coverage"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mbu2-m9qy",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-04-08",
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
-            "identifier": "a7c8e38d-baa6-5f37-b1ce-5ce1a55a36e7",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard pillar v2.11.18 (etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/pillar.csv",
-                    "description": "Scorecard pillar v2.11.18 (etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard pillar v2.11.18 (etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard pillar v2.11.18 (etl-test)"
                 }
             ],
+            "identifier": "a7c8e38d-baa6-5f37-b1ce-5ce1a55a36e7",
+            "issued": "2023-04-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/mbu2-m9qy",
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
+            "title": "Scorecard pillar v2.11.18 (etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fsf9-trph",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-12-12",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-12",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Pathology and Physiology Research Branch, Health Effects Laboratory Division",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/fsf9-trph",
             "description": "Introduction: Thermal spray, in general, is a process that involves forcing a melted substance, such as metal or ceramic in the form of wire or powder, onto the surface of a targeted object to enhance its desired surface properties. In this paper, the melted substance is metal wire generated by an electric arc and forcibly coated on a rotary iron substrate using compressed air. This thermal process is referred to as double-wire arc thermal spray. The particles generated through these methods fall within the nanometer to micrometer agglomerate size range. There is concern regarding potential human health outcomes as these particles exhibit a similarity in particle morphology to welding fumes. Thermal spray wires with Zn (PMET540), Fe and Cr (PMET731), and Ni (PMET885) as primary metal compositions were used to generate particulate via an electric arc wire thermal spray generator for exposure to human bronchial cells (BEAS-2B) to examine comparative toxicity ranging from 0-200 \u00b5g/mL. Resulting cellular viability was assessed through live cell counts, and percent cytotoxicity was measured as a function of LDH release. Oxidative stress, genotoxicity, and alteration in Total Antioxidant Capacity were evaluated through DNA damage (COMET analysis) and antioxidant concentration at 0, 3.125, 25, and 100 \u00b5g/mL. Protein markers for Endothelin-1 (ET-1), Interleukin-6 (IL-6), and Interleukin-8 (IL-8) were also assessed to determine inflammation and endothelial alteration.",
-            "title": "Comparative in vitro toxicity of different thermal spray particulates in human bronchial cells",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97741,53 +97728,44 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fsf9-trph",
+            "issued": "2024-12-12",
+            "landingPage": "https://data.cdc.gov/d/fsf9-trph",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-12",
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
+            "title": "Comparative in vitro toxicity of different thermal spray particulates in human bronchial cells"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/quality-of-care/agency-for-healthcare-research-and-quality-ahrq-patient-safety-indicator-11-psi-11-measure-rates",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2015-01-01/2016-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-08",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2020-09/Agency%20for%20Healthcare%20Research%20and%20Quality%20%28AHRQ%29%20Patient%20Safety%20Indicator%2011%20%28PSI-11%29%20Measure%20Rates%20Methodology_0.pdf"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "hospitals & facilities",
-                "inpatient",
-                "medicare",
-                "original medicare",
-                "safety of care"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Deficit Reduction Act Hospital Acquired Conditions - CCSQ",
                 "hasEmail": "mailto:drahac@mathematica-mpr.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/7cf9662e-7c5c-4fe0-a8c6-828edf81a23c/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/agency-for-healthcare-research-and-quality-ahrq-patient-safety-indicator-11-psi-11-measure-rates-data-dictionary",
             "description": "The Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates dataset provides information on provider-level measure\u00a0rates regarding one preventable complication (postoperative respiratory failure) for Medicare fee-for-service discharges. The PSI-11 measure data is solely reported for providers\u2019 information and quality improvement purposes and are not a part of the Deficit Reduction Act (DRA) Hospital-Acquired Condition (HAC) Payment Provision or HAC Reduction Program.",
-            "title": "Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7cf9662e-7c5c-4fe0-a8c6-828edf81a23c/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7cf9662e-7c5c-4fe0-a8c6-828edf81a23c/data",
+                    "mediaType": "text/html",
                     "title": "Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates : 2016-07-29"
                 },
                 {
@@ -97815,48 +97793,51 @@
                     "title": "Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates : 2015-08-19"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/agency-for-healthcare-research-and-quality-ahrq-patient-safety-indicator-11-psi-11-measure-rates-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/7cf9662e-7c5c-4fe0-a8c6-828edf81a23c/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "hospitals & facilities",
+                "inpatient",
+                "medicare",
+                "original medicare",
+                "safety of care"
+            ],
+            "landingPage": "https://data.cms.gov/quality-of-care/agency-for-healthcare-research-and-quality-ahrq-patient-safety-indicator-11-psi-11-measure-rates",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-12-08",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2020-09/Agency%20for%20Healthcare%20Research%20and%20Quality%20%28AHRQ%29%20Patient%20Safety%20Indicator%2011%20%28PSI-11%29%20Measure%20Rates%20Methodology_0.pdf"
+            ],
+            "temporal": "2015-01-01/2016-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mcj4-a5xe",
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
-            "identifier": "731b5a4b-02ce-4e87-91fc-18854d3f3301",
             "description": "The Medical Individual Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to consumers in the individual market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2023 Individual Medical",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97864,35 +97845,39 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "731b5a4b-02ce-4e87-91fc-18854d3f3301",
+            "issued": "2023-08-23",
+            "keyword": [
+                "individual",
+                "individual market medical",
+                "py2023",
+                "qhp",
+                "qhp landscape instructions"
+            ],
+            "landingPage": "https://healthdata.gov/d/mcj4-a5xe",
+            "modified": "2023-08-28",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2023 Individual Medical"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mcpi-563a",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-02-09",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-08",
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
-            "identifier": "818846a8-6cf4-48ef-b941-11de8b1de51a",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-01-31 to 2022-02-06",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97900,92 +97885,84 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "818846a8-6cf4-48ef-b941-11de8b1de51a",
+            "issued": "2022-02-09",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/mcpi-563a",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2022-02-08",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-01-31 to 2022-02-06"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/md44-9yt2",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-06-03",
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
-            "identifier": "ed77b0e4-49a3-5f10-a2e2-b3878abb7c76",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_footnotes",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/footnotes.csv",
-                    "description": "{\"dataset\": \"footnotes\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"footnotes\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/footnotes.csv",
+                    "mediaType": "text/csv",
                     "title": "footnotes csv file"
                 }
             ],
+            "identifier": "ed77b0e4-49a3-5f10-a2e2-b3878abb7c76",
+            "issued": "2023-06-03",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/md44-9yt2",
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
+            "title": "implAuto_footnotes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-visualization/state-life-expectancy/index_2019.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-02-03",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-01-01/2019-12-31",
-            "modified": "2022-03-29",
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
-            "identifier": "https://data.cdc.gov/api/views/ncvk-7amm",
             "description": "The dataset presents life expectancy at birth estimates based on annual complete period life tables for each of the 50 states and the District of Columbia (D.C.)\nin 2019 for the total, male and female populations.",
-            "title": "U.S. State Life Expectancy by Sex, 2019",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98008,48 +97985,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/ncvk-7amm",
+            "issued": "2022-02-03",
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
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/state-life-expectancy/index_2019.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2022-03-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2019-01-01/2019-12-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "U.S. State Life Expectancy by Sex, 2019"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -98072,39 +98048,46 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Mumps to Rabies, animal"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rq85-buyi",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-10-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-01",
-            "keyword": [
-                "cdc.gov",
-                "web metrics"
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
-            "identifier": "https://data.cdc.gov/api/views/rq85-buyi",
             "description": "For more information on CDC.gov metrics please see http://www.cdc.gov/metrics/",
-            "title": "Monthly Page Views to CDC.gov",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98127,52 +98110,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rq85-buyi",
+            "issued": "2018-10-02",
+            "keyword": [
+                "cdc.gov",
+                "web metrics"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rq85-buyi",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-01",
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
+            "title": "Monthly Page Views to CDC.gov"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/quality-of-care/long-term-care-facility-characteristics",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-08-01",
-            "temporal": "2023-10-01/2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-31",
-            "references": [
-                "https://data.cms.gov/resources/long-term-care-facility-characteristics-methodology"
-            ],
-            "keyword": [
-                "hospitals & facilities",
-                "inpatient",
-                "long term care",
-                "medicare",
-                "skilled nursing"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NH Facility - CCSQ",
                 "hasEmail": "mailto:NursingHomeData@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/129a6503-c0f1-4132-b186-4c0232c2d894/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/long-term-care-facility-characteristics-data-dictionary",
             "description": "The Long-Term Care Facility Characteristics, CMS Form 671, dataset provides information submitted by nursing homes on the CMS Form 671 collected during annual surveys. The data include information about resident census, ownership, dedicated special care units, facility characteristics, and staffing.\n\n\u00a0\n\nNote: Annual surveys are conducted every 9 to 15 months. Additionally, some states are experiencing delays in conducting annual surveys, resulting in longer periods of time since the last annual survey. As such, some of the data included in these files may not be up to date.",
-            "title": "Long-Term Care Facility Characteristics",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/129a6503-c0f1-4132-b186-4c0232c2d894/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/129a6503-c0f1-4132-b186-4c0232c2d894/data",
+                    "mediaType": "text/html",
                     "title": "Long-Term Care Facility Characteristics : 2024-07-01"
                 },
                 {
@@ -98224,46 +98203,50 @@
                     "title": "Long-Term Care Facility Characteristics : 2023-10-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/long-term-care-facility-characteristics-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/129a6503-c0f1-4132-b186-4c0232c2d894/data-viewer",
+            "issued": "2024-08-01",
+            "keyword": [
+                "hospitals & facilities",
+                "inpatient",
+                "long term care",
+                "medicare",
+                "skilled nursing"
+            ],
+            "landingPage": "https://data.cms.gov/quality-of-care/long-term-care-facility-characteristics",
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
+                "https://data.cms.gov/resources/long-term-care-facility-characteristics-methodology"
+            ],
+            "temporal": "2023-10-01/2024-09-30",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Long-Term Care Facility Characteristics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/meg6-u3zg",
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
-            "identifier": "b28a22a2-2c7b-5745-a3f9-d64621f51388",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 1997",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98271,51 +98254,41 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "b28a22a2-2c7b-5745-a3f9-d64621f51388",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/meg6-u3zg",
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
+            "title": "State Drug Utilization Data 1997"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/national-epidemiologic-survey-alcohol-and-related-conditions-nesarc-iii",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2014-04-08",
-            "temporal": "2012-02-01T00:00:00-05:00/2013-01-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "adult",
-                "alcohol",
-                "anxiety",
-                "disability",
-                "disparities",
-                "epidemiology",
-                "mental health",
-                "mood disorder",
-                "other",
-                "population statistics",
-                "sexual assault",
-                "substance use"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NIAAA Information",
                 "hasEmail": "mailto:niaaaweb-r@exchange.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
-            },
-            "identifier": "39fcee10-a135-40eb-a0e2-b0dea72be504",
+            "dataQuality": true,
             "description": "<p>The National Epidemiologic Survey on Alcohol and Related Conditions - III (NESARC-III) is a nationally representative survey of 46,500 adult Americans that collected data on alcohol use disorders and their associated disabilities in addition to collecting saliva samples for the purpose of understanding the prevalence, risk factors, health disparities, economic costs and gene-environment interactions related to alcohol use disorders and their associated disabilities.</p>\n<p>Results from the study are not yet available. The data collection is also associated with clinical trial number: NCT01273220.</p>",
-            "title": "National Epidemiologic Survey on Alcohol and Related Conditions (NESARC) - III",
-            "programCode": [
-                "009:062"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98342,42 +98315,52 @@
                     "title": "Text "
                 }
             ],
-            "dataQuality": true,
+            "identifier": "39fcee10-a135-40eb-a0e2-b0dea72be504",
+            "issued": "2014-04-08",
+            "keyword": [
+                "adult",
+                "alcohol",
+                "anxiety",
+                "disability",
+                "disparities",
+                "epidemiology",
+                "mental health",
+                "mood disorder",
+                "other",
+                "population statistics",
+                "sexual assault",
+                "substance use"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-epidemiologic-survey-alcohol-and-related-conditions-nesarc-iii",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:062"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
+            },
+            "temporal": "2012-02-01T00:00:00-05:00/2013-01-31T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "National Epidemiologic Survey on Alcohol and Related Conditions (NESARC) - III"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/health-information-national-trends-survey-hints",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-08-01",
-            "temporal": "2003-10-02T00:00:00-04:00/2003-10-02T00:00:00-04:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "health communication  cancer information seeking information  cancer perception   cancer knowledge",
-                "internet use  numeracy  nutrition  physical activity  patient-provider communication  risk perceptio",
-                "population statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCI HINTS",
                 "hasEmail": "mailto:NCIHints@mail.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
-            },
-            "identifier": "e070c4c9-e4cf-4494-9e0a-40eb5761809e",
+            "dataQuality": true,
+            "describedBy": "http://hints.cancer.gov/instrument.aspx",
             "description": "<p>The Health Information National Trends Survey (HINTS) is a biennial, cross-sectional survey of a nationally-representative sample of American adults that is used to assess the impact of the health information environment. The survey provides updates on changing patterns, needs, and information opportunities in health; Identifies changing communications trends and practices; Assesses cancer information access and usage; Provides information about how cancer risks are perceived; and Offers a testbed to researchers to test new theories in health communication.&#13;&#13;&#13;</p>",
-            "title": "Health Information National Trends Survey (HINTS)",
-            "programCode": [
-                "009:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98386,23 +98369,53 @@
                     "title": " "
                 }
             ],
-            "describedBy": "http://hints.cancer.gov/instrument.aspx",
-            "dataQuality": true,
+            "identifier": "e070c4c9-e4cf-4494-9e0a-40eb5761809e",
+            "issued": "2012-08-01",
+            "keyword": [
+                "health communication  cancer information seeking information  cancer perception   cancer knowledge",
+                "internet use  numeracy  nutrition  physical activity  patient-provider communication  risk perceptio",
+                "population statistics"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/health-information-national-trends-survey-hints",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:031"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
+            },
+            "temporal": "2003-10-02T00:00:00-04:00/2003-10-02T00:00:00-04:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "Health Information National Trends Survey (HINTS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/civil-remedies-division-administrative-law-judge-decisions",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.hhs.gov/dab/decisions/civildecisions/index.html",
+            "description": "<p>Decisions issued by Administrative Law Judges of the Departmental Appeals Board's Civil Remedies Division concerning fraud and abuse determinations by the Office of the Inspector General (OIG) or the Centers for Medicare &amp; Medicaid Services (CMS); provider/supplier enforcement and certification determinations by CMS; terminations of or refusal to grant or continue federal funding for alleged civil rights violations; Program Fraud Civil Remedies Act determinations; civil money penalty determinations by Social Security Administration (SSA); and Equal Access to Justice Act determinations relating to OIG proceedings.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.hhs.gov/dab/decisions/index.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "10d259c7-dd50-4786-a98e-6a51ed6312d2",
             "issued": "2012-05-30",
-            "temporal": "1985-03-08T00:00:00-05:00/1985-03-08T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "abuse",
                 "administrative",
@@ -98501,75 +98514,38 @@
                 "transaction",
                 "violation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/civil-remedies-division-administrative-law-judge-decisions",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:077"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "10d259c7-dd50-4786-a98e-6a51ed6312d2",
-            "description": "<p>Decisions issued by Administrative Law Judges of the Departmental Appeals Board's Civil Remedies Division concerning fraud and abuse determinations by the Office of the Inspector General (OIG) or the Centers for Medicare &amp; Medicaid Services (CMS); provider/supplier enforcement and certification determinations by CMS; terminations of or refusal to grant or continue federal funding for alleged civil rights violations; Program Fraud Civil Remedies Act determinations; civil money penalty determinations by Social Security Administration (SSA); and Equal Access to Justice Act determinations relating to OIG proceedings.</p>",
-            "title": "Civil Remedies Division Administrative Law Judge Decisions",
-            "programCode": [
-                "009:077"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.hhs.gov/dab/decisions/index.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://www.hhs.gov/dab/decisions/civildecisions/index.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1985-03-08T00:00:00-05:00/1985-03-08T00:00:00-05:00",
             "theme": [
                 "Community",
                 "Health",
                 "Medicare",
                 "Hospital"
-            ]
+            ],
+            "title": "Civil Remedies Division Administrative Law Judge Decisions"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -98592,46 +98568,51 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://clinicaltrials.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-11",
-            "keyword": [
-                "api",
-                "biomedical research",
-                "clinical trials",
-                "united states"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/k4z8-wtxk",
             "description": "Provides patients, family members, health care professionals, and members of the public easy access to information on clinical trials for a wide range of diseases and conditions.",
-            "title": "ClinicalTrials.gov",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98652,20 +98633,52 @@
                     "title": "ClinicalTrials.gov API"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/k4z8-wtxk",
+            "issued": "2012-05-30",
+            "keyword": [
+                "api",
+                "biomedical research",
+                "clinical trials",
+                "united states"
+            ],
+            "landingPage": "https://clinicaltrials.gov/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-11",
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
+            "title": "ClinicalTrials.gov"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1994",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1994) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1994-nid13568",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1994-nid13568"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1994-nid13568",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -98678,110 +98691,81 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1994",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1994-nid13568",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1994)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1994-nid13568",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1994) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1994-nid13568"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1994)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mg4k-w883",
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
-            "identifier": "be80f45d-6dd9-56b9-b01e-1506bc875327",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet state v2.10.64 (coreset-impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/state.csv",
-                    "description": "CoreSet state v2.10.64 (coreset-impl)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet state v2.10.64 (coreset-impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/state.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet state v2.10.64 (coreset-impl)"
                 }
             ],
+            "identifier": "be80f45d-6dd9-56b9-b01e-1506bc875327",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/mg4k-w883",
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
+            "title": "CoreSet state v2.10.64 (coreset-impl)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/mbui-hx3y",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "data distribution"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/mbui-hx3y",
             "description": "GENE-TOX provided genetic toxicology (mutagenicity) test data from expert peer review of open scientific literature for more than 3,000 chemicals from the United States Environmental Protection Agency (EPA) covering the years 1991 - 1998.  GENE-TOX is no longer updated.",
-            "title": "GENE-TOX (Genetic Toxicology Data Bank)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/genetoxlease/",
-                    "description": "Download over 3214 GENE-TOX records.",
                     "@type": "dcat:Distribution",
+                    "description": "Download over 3214 GENE-TOX records.",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/genetoxlease/",
+                    "mediaType": "text/html",
                     "title": "Download GENE-TOX Data"
                 },
                 {
@@ -98797,40 +98781,39 @@
                     "title": "GENE-TOX Data Element Guide"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/mbui-hx3y",
+            "issued": "2020-09-22",
+            "keyword": [
+                "data distribution"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/mbui-hx3y",
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
+            "title": "GENE-TOX (Genetic Toxicology Data Bank)"
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
-            "identifier": "https://data.cdc.gov/api/views/8jp2-ecz7",
             "description": "\u2022 Weekly COVID-19 vaccination coverage estimates among children 6 months to 17 years is assessed through the National Immunization Survey (https://www.cdc.gov/vaccines/imz-managers/nis/about.html). \n\n\u2022 Weekly estimates of COVID-19 vaccination coverage among children through December 31, 2023, were calculated using data from the National Immunization Survey-Child COVID Module (NIS-CCM) (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-ccm). Beginning January 2, 2024, the NIS-CCM was discontinued, and questions regarding receipt of COVID-19 vaccination among children were added to the NIS-Flu (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-cim). \n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19.",
-            "title": "Weekly Cumulative Percentage of Children Ages 6 Months -17 Years who are up to date with the updated 2023-24 COVID-19 Vaccine, by Jurisdiction",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98853,42 +98836,42 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/8jp2-ecz7",
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
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mgs9-bipk",
-            "bureauCode": [
-                "009:00"
             ],
-            "issued": "2015-09-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-11",
-            "keyword": [
-                "drug utilization",
-                "medicaid reimbursements",
-                "pharmacy"
+            "title": "Weekly Cumulative Percentage of Children Ages 6 Months -17 Years who are up to date with the updated 2023-24 COVID-19 Vaccine, by Jurisdiction"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P10Y",
+            "bureauCode": [
+                "009:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Medicaid.gov",
                 "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "2fed5758-5fd6-5dbb-8f92-34b3a0c3c8dd",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2015",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98896,43 +98879,41 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "2fed5758-5fd6-5dbb-8f92-34b3a0c3c8dd",
+            "issued": "2015-09-04",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/mgs9-bipk",
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
+            "title": "State Drug Utilization Data 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/health-insurance-coverage.htm",
+            "accrualPeriodicity": "R/P2W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-05-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-08-19/2024-09-16",
-            "modified": "2024-10-04",
-            "keyword": [
-                "covid-19",
-                "private coverage",
-                "public coverage",
-                "uninsured"
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
-            "identifier": "https://data.cdc.gov/api/views/jb9g-gnvr",
             "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, gender, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
-            "title": "Indicators of Health Insurance Coverage at the Time of Interview",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98955,44 +98936,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/jb9g-gnvr",
+            "issued": "2020-05-20",
+            "keyword": [
+                "covid-19",
+                "private coverage",
+                "public coverage",
+                "uninsured"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/health-insurance-coverage.htm",
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
+            "title": "Indicators of Health Insurance Coverage at the Time of Interview"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/nuccore",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-03-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "biochemistry",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/58zq-hzhw",
             "description": "The Nucleotide database is a collection of sequences from several sources, including GenBank, RefSeq, TPA and PDB. Genome, gene and transcript sequence data provide the foundation for biomedical research and discovery.",
-            "title": "Nucleotide",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99001,38 +98984,40 @@
                     "title": "Nucleotide"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/58zq-hzhw",
+            "issued": "2022-03-01",
+            "keyword": [
+                "biochemistry",
+                "dataset"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/nuccore",
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
+            "title": "Nucleotide"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/HVPCP/HydrolyzedVegetableProteinProductsList2010.xml",
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
-            "identifier": "0a235bac-418f-4fa9-81b7-1af3259a54b1",
             "description": "This list includes products subject to recall in the United States since February 2010 related to hydrolyzed vegetable protein (HVP) paste and powder distributed by Basic Food Flavors, Inc. HVP is a flavor enhancer used in a wide variety of processed food products such as soups, sauces, chilis, stews, hot dogs, gravies, seasoned snack foods, dips, and dressings.",
-            "title": "Hydrolyzed Vegetable Protein Containing Products Recalls",
-            "programCode": [
-                "009:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99040,49 +99025,35 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "0a235bac-418f-4fa9-81b7-1af3259a54b1",
+            "issued": "2021-02-25",
+            "keyword": [
+                "recalls"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/HVPCP/HydrolyzedVegetableProteinProductsList2010.xml",
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
+            "title": "Hydrolyzed Vegetable Protein Containing Products Recalls"
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
-            "identifier": "https://data.cdc.gov/api/views/uuui-fh3m",
             "description": "This dataset contains model-based place (incorporated and census designated places) level estimates for the PLACES 2022 release in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. These data can be joined with the 2019 Census TIGER/Line place boundary file in a GIS system to produce maps for 29 measures at the place level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software. https://cdcarcgis.maps.arcgis.com/home/item.html?id=3b7221d4e47740cab9235b839fa55cd7",
-            "title": "PLACES: Place Data (GIS Friendly Format), 2022 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99105,35 +99076,51 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/uuui-fh3m",
+            "issued": "2023-06-15",
+            "keyword": [
+                "behaviors",
+                "city",
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
+            "title": "PLACES: Place Data (GIS Friendly Format), 2022 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xqmi-ykpp",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -99141,43 +99128,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xqmi-ykpp",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/xqmi-ykpp",
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
+            "title": "Effects of Crystalline Silica Inhalation in a High-Fat Western Diet"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mic4-3ve7",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2025-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "keyword": [
-                "chip",
-                "epsdt",
-                "medicaid",
-                "service use",
-                "t-msis analytic files",
-                "well-child visits"
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
-            "identifier": "289182e5-44c8-4fcc-96c4-4af69be9863f",
             "description": "This data set includes annual counts and percentages of Medicaid and Children\u2019s Health Insurance Program (CHIP) enrollees who received a well-child visit paid for by Medicaid or CHIP, overall and by five subpopulation topics: age group, race and ethnicity, urban or rural residence, program type, and primary language.\r\nThese results were generated using Transformed Medicaid Statistical Information System (T-MSIS) Analytic Files (TAF) Release 1 data and the Race/Ethnicity Imputation Companion File. This data set includes Medicaid and CHIP enrollees in all 50 states, the District of Columbia, Puerto Rico, and the U.S. Virgin Islands, except where otherwise noted. Enrollees in Guam, American Samoa, and the Northern Mariana Islands are not included. Results include enrollees with comprehensive Medicaid or CHIP benefits for all 12 months of the year and who were younger than age 19 at the end of the calendar year. Results shown for the race and ethnicity subpopulation topic exclude enrollees in the U.S. Virgin Islands. Results shown for the primary language subpopulation topic exclude select states with data quality issues with the primary language variable in TAF. Some rows in the data set have a value of \"DS,\" which indicates that data were suppressed according to the Centers for Medicare & Medicaid Services\u2019 Cell Suppression Policy for values between 1 and 10.\r\nThis data set is based on the brief: \"Medicaid and CHIP enrollees who received a well-child visit in 2020.\" Enrollees are identified as receiving a well-child visit in the year according to the Line 6 criteria in the Form CMS-416 reporting instructions. Enrollees are assigned to an age group subpopulation using age as of December 31st of the calendar year. Enrollees are assigned to a race and ethnicity subpopulation using the state-reported race and ethnicity information in TAF when it is available and of good quality; if it is missing or unreliable, race and ethnicity is indirectly estimated using an enhanced version of Bayesian Improved Surname Geocoding (BISG) (Race and ethnicity of the national Medicaid and CHIP population in 2020). Enrollees are assigned to an urban or rural subpopulation based on the 2010 Rural-Urban Commuting Area (RUCA) code associated with their home or mailing address ZIP code in TAF (Rural Medicaid and CHIP enrollees in 2020). Enrollees are assigned to a program type subpopulation based on the CHIP code and eligibility group code that applies to the majority of their enrolled-months during the year (Medicaid-Only Enrollment; M-CHIP and S-CHIP Enrollment). Enrollees are assigned to a primary language subpopulation based on their reported ISO language code in TAF (English/missing, Spanish, and all other language codes) (Primary Language). Please refer to the full brief for additional context about the methodology and detailed findings. Future updates to this data set will include more recent data years as the TAF data become available.",
-            "title": "Medicaid and CHIP enrollees who received a well-child visit",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99185,43 +99164,41 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "289182e5-44c8-4fcc-96c4-4af69be9863f",
+            "issued": "2025-01-18",
+            "keyword": [
+                "chip",
+                "epsdt",
+                "medicaid",
+                "service use",
+                "t-msis analytic files",
+                "well-child visits"
+            ],
+            "landingPage": "https://healthdata.gov/d/mic4-3ve7",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Medicaid and CHIP enrollees who received a well-child visit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-visualization/state-life-expectancy/index_2021.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-09-11",
-            "@type": "dcat:Dataset",
-            "temporal": "2021-01-01/2021-12-31",
-            "modified": "2024-09-11",
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
-            "identifier": "https://data.cdc.gov/api/views/it4f-frdc",
             "description": "The dataset presents life expectancy at birth estimates based on annual complete period life tables for each of the 50 states and the District of Columbia (D.C.)\nin 2021 for the total, male and female populations.",
-            "title": "U.S. State Life Expectancy by Sex, 2021",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99244,43 +99221,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/it4f-frdc",
+            "issued": "2024-09-11",
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
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/state-life-expectancy/index_2021.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2024-09-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2021-01-01/2021-12-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "U.S. State Life Expectancy by Sex, 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mj9r-3n8y",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "exchange puf",
-                "marketplace puf",
-                "plan attributes",
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
-            "identifier": "ad5c073e-8451-4378-b3d8-4ba189f29cfe",
             "description": "The Plan Attributes PUF (Plan-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Plan-PUF contains plan variant-level data on maximum out of pocket payments, deductibles, health savings account (HSA) eligibility, and other plan attributes.",
-            "title": "Plan Attributes PUF - PY2025",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99288,36 +99270,37 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "ad5c073e-8451-4378-b3d8-4ba189f29cfe",
+            "issued": "2024-12-10",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "plan attributes",
+                "py2025"
+            ],
+            "landingPage": "https://healthdata.gov/d/mj9r-3n8y",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Plan Attributes PUF - PY2025"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/homologene",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-30",
-            "keyword": [
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/n3nx-dytj",
             "description": "System for automated detection of homologs among the annotated genes of several completely sequenced eukaryotic genomes.",
-            "title": "HomoloGene",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99332,91 +99315,85 @@
                     "title": "Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/n3nx-dytj",
+            "issued": "2021-06-30",
+            "keyword": [
+                "dataset",
+                "genomics"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/homologene",
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
                 "Molecular biology/Genetics"
-            ]
+            ],
+            "title": "HomoloGene"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mkaa-fjd6",
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
-            "identifier": "bdab949c-913c-53b1-935a-991453fd4f65",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet measure v2.10.64 (coreset-cmsdev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure.csv",
-                    "description": "CoreSet measure v2.10.64 (coreset-cmsdev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet measure v2.10.64 (coreset-cmsdev)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet measure v2.10.64 (coreset-cmsdev)"
                 }
             ],
+            "identifier": "bdab949c-913c-53b1-935a-991453fd4f65",
+            "issued": "2024-11-13",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/mkaa-fjd6",
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
+            "title": "CoreSet measure v2.10.64 (coreset-cmsdev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/52kh-2h7i",
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
-            "identifier": "https://data.cdc.gov/api/views/52kh-2h7i",
             "description": "NNDSS - TABLE 1AA. Poliovirus infection, nonparalytic to Psittacosis - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1AA. Poliovirus infection, nonparalytic to Psittacosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99439,50 +99416,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/52kh-2h7i",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "nedss",
+                "netss",
+                "nndss",
+                "nonparalytic",
+                "poliovirus infection",
+                "psittacosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/52kh-2h7i",
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
+            "title": "NNDSS - TABLE 1AA. Poliovirus infection, nonparalytic to Psittacosis"
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
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DNPAO Public Inquiries",
                 "hasEmail": "mailto:dnpaoinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/nxst-x9p4",
+            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/CDC-Nutrition-Physical-Activity-and-Obesity-Legisl/nxst-x9p4",
             "description": "This dataset contains policy data for 50 US states and DC from 2001 to 2017. Data include information related to state legislation and regulations on nutrition, physical activity, and obesity in settings such as early care and education centers, restaurants, schools, work places, and others. To identify individual bills, use the identifier ProvisionID.  A bill or citation may appear more than once because it could apply to multiple health or policy topics, settings, or states. As of Q 2 2016, data include only enacted legislation.",
-            "title": "CDC Nutrition, Physical Activity, and Obesity - Legislation",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99505,38 +99478,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/CDC-Nutrition-Physical-Activity-and-Obesity-Legisl/nxst-x9p4",
+            "identifier": "https://data.cdc.gov/api/views/nxst-x9p4",
+            "issued": "2023-07-18",
+            "keyword": [
+                "body mass index (bmi)",
+                "built environment",
+                "farm",
+                "fruits and vegetables",
+                "nutrition",
+                "obesity",
+                "physical activity",
+                "physical activity education",
+                "transportation",
+                "zoning"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
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
+                "http://www.cdc.gov/nccdphp/DNPAO"
+            ],
             "theme": [
                 "Nutrition",
                 "Physical Activity",
                 "and Obesity"
-            ]
+            ],
+            "title": "CDC Nutrition, Physical Activity, and Obesity - Legislation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xmn2-yrqr",
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
-            "identifier": "https://data.cdc.gov/api/views/xmn2-yrqr",
             "description": "The development of vibration-induced finger disorders is likely associated with combined static and dynamic responses of the fingers to vibration exposure. To study the mechanisms of these disorders, a new rat-tail model has been established to mimic the finger pressure and vibration exposures. However, the mechanical behavior of the tail during compression needs to be better understood to improve the model and its applications. The purpose of the current study was to investigate the static and time-dependent force responses of the rat tail during compression. Compression tests were conducted on male Sprague-Dawley cadaver rat tails using a micromechanical testing system at three deformation velocities and three deformation magnitudes. Contact-width, and the time-histories of force and deformation were measured. Additionally, force-relaxation tests were conducted and a Prony series was used to model the force-relaxation behavior of the tail.",
-            "title": "Quantification of mechanical behavior of rat tail under compression",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99544,46 +99531,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xmn2-yrqr",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/xmn2-yrqr",
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
+            "title": "Quantification of mechanical behavior of rat tail under compression"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -99606,39 +99582,46 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Lyme disease to Meningococcal"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/k9ai-xgx2",
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
-            "identifier": "https://data.cdc.gov/api/views/k9ai-xgx2",
             "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 6 - Dallas",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99661,40 +99644,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/k9ai-xgx2",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/k9ai-xgx2",
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
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 6 - Dallas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mpjr-7iz7",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2014-11-07",
-            "temporal": "2014-01-01T00:00:00+00:00/2015-01-01T00:00:00+00:00",
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
-            "identifier": "ba0c3734-8012-549a-8f50-2ff389d0e0ef",
             "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
-            "title": "NADAC (National Average Drug Acquisition Cost) 2014",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99703,40 +99686,42 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "ba0c3734-8012-549a-8f50-2ff389d0e0ef",
+            "issued": "2014-11-07",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "landingPage": "https://healthdata.gov/d/mpjr-7iz7",
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
+            "temporal": "2014-01-01T00:00:00+00:00/2015-01-01T00:00:00+00:00",
             "theme": [
                 "National Average Drug Acquisition Cost",
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "NADAC (National Average Drug Acquisition Cost) 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mq9a-nckf",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-04-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-01",
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
-            "identifier": "49d67dfc-9432-4f63-bb99-a3eacf8bf93e",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-25-2024-to-03-31-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99745,39 +99730,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-25-2024-to-03-31-2024"
                 }
             ],
+            "identifier": "49d67dfc-9432-4f63-bb99-a3eacf8bf93e",
+            "issued": "2024-04-02",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/mq9a-nckf",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-04-01",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 03-25-2024-to-03-31-2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/2sxq-n8zu",
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
-            "identifier": "https://data.cdc.gov/api/views/2sxq-n8zu",
             "description": "Interactive visualization: http://www.cdc.gov/chikungunya/modeling/index.html. This dataset contains monthly predictions for the spread of chikungunya virus transmission. A full description of the methods is available at: http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0104915.",
-            "title": "Nowcast Predictions for Chikungunya Virus-Infected Travelers",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99800,93 +99781,85 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/2sxq-n8zu",
+            "issued": "2015-08-10",
+            "keyword": [
+                "americas",
+                "chikungunya",
+                "predictions",
+                "travelers"
+            ],
+            "landingPage": "https://data.cdc.gov/d/2sxq-n8zu",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-02-21",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "Nowcast Predictions for Chikungunya Virus-Infected Travelers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mr2u-r2n5",
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
-            "identifier": "19233349-77b4-5f99-8e60-beb0aa1165de",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet state v2.10.64 (coreset-dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/state.csv",
-                    "description": "CoreSet state v2.10.64 (coreset-dev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet state v2.10.64 (coreset-dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/state.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet state v2.10.64 (coreset-dev)"
                 }
             ],
+            "identifier": "19233349-77b4-5f99-8e60-beb0aa1165de",
+            "issued": "2024-11-06",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/mr2u-r2n5",
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
+            "title": "CoreSet state v2.10.64 (coreset-dev)"
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
-            "modified": "2023-08-25",
-            "references": [
-                "https://www.cdc.gov/oralhealthdata/"
-            ],
-            "keyword": [
-                "cleft lip/cleft palate recording",
-                "cleft lip/cleft palate referral to care",
-                "infrastructure",
-                "oral health",
-                "policy",
-                "programs",
-                "school based sealant programs",
-                "state dental directors",
-                "state oral health program characteristics",
-                "workforce"
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
-            "identifier": "https://data.cdc.gov/api/views/vwmz-4ja3",
+            "describedBy": "https://chronicdata.cdc.gov/Oral-Health/ASTDD-Synopses-of-State-Oral-Health-Programs-Selec/vwmz-4ja3",
             "description": "2011-2022. The ASTDD Synopses of State Oral Health Programs contain information useful in tracking states\u2019 efforts to improve oral health and contributions to progress toward the national targets for Healthy People objectives for oral health. A subset of the information collected from the most recent five years is provided on the Oral Health Data website. For more information, see http://www.cdc.gov/oralhealthdata/overview/synopses/index.html",
-            "title": "ASTDD Synopses of State Oral Health Programs - Selected indicators",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99909,39 +99882,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Oral-Health/ASTDD-Synopses-of-State-Oral-Health-Programs-Selec/vwmz-4ja3",
+            "identifier": "https://data.cdc.gov/api/views/vwmz-4ja3",
+            "issued": "2023-07-18",
+            "keyword": [
+                "cleft lip/cleft palate recording",
+                "cleft lip/cleft palate referral to care",
+                "infrastructure",
+                "oral health",
+                "policy",
+                "programs",
+                "school based sealant programs",
+                "state dental directors",
+                "state oral health program characteristics",
+                "workforce"
+            ],
+            "landingPage": "http://www.cdc.gov/oralhealth/",
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
+                "https://www.cdc.gov/oralhealthdata/"
+            ],
             "theme": [
                 "Oral Health"
-            ]
+            ],
+            "title": "ASTDD Synopses of State Oral Health Programs - Selected indicators"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mr95-wjj2",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-11",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-10",
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
-            "identifier": "b960ee5c-42f9-4d97-927b-5c244bef40cf",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-02-to-2023-10-08",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99950,18 +99935,46 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-02-to-2023-10-08"
                 }
             ],
+            "identifier": "b960ee5c-42f9-4d97-927b-5c244bef40cf",
+            "issued": "2023-10-11",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/mr95-wjj2",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-10-10",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-02-to-2023-10-08"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-10-year-substate-r-das-nsduh-2002-2011",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This file includes data from the 2002 through 2011 National Survey on Drug Use and Health (NSDUH) survey. The only variables included in the data file are ones that were collected in a comparable manner across all ten years of data.<br />\nThe National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Certain questions are asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Also included are questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Demographic information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.<br />\nIn the income section, which was interviewer-administered, a split-sample study had been embedded within the 2006 and 2007 surveys to compare a shorter version of the income questions with a longer set of questions that had been used in previous surveys. This shorter version was adopted for the 2008 NSDUH and will be used for future NSDUHs.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health: 10-Year Substate R-DAS (NSDUH-2002-2011) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-10-year-substate-r-das-nsduh-2002-2011-nid13609",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-10-year-substate-r-das-nsduh-2002-2011-nid13609"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-10-year-substate-r-das-nsduh-2002-2011-nid13609",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -100002,41 +100015,54 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-10-year-substate-r-das-nsduh-2002-2011",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-10-year-substate-r-das-nsduh-2002-2011-nid13609",
-            "description": "<p>This file includes data from the 2002 through 2011 National Survey on Drug Use and Health (NSDUH) survey. The only variables included in the data file are ones that were collected in a comparable manner across all ten years of data.<br />\nThe National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Certain questions are asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Also included are questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Demographic information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.<br />\nIn the income section, which was interviewer-administered, a split-sample study had been embedded within the 2006 and 2007 surveys to compare a shorter version of the income questions with a longer set of questions that had been used in previous surveys. This shorter version was adopted for the 2008 NSDUH and will be used for future NSDUHs.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health: 10-Year Substate R-DAS (NSDUH-2002-2011)",
-            "programCode": [
-                "009:030"
+            "title": "National Survey on Drug Use and Health: 10-Year Substate R-DAS (NSDUH-2002-2011)"
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
+            "description": "Cumulative provisional counts of deaths sex, race/Hispanic origin, age group, and by select underlying causes of death.  The dataset also includes provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.  Includes deaths that occurred between January 1, 2020 to July 28, 2020.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-10-year-substate-r-das-nsduh-2002-2011-nid13609",
-                    "description": "National Survey on Drug Use and Health: 10-Year Substate R-DAS (NSDUH-2002-2011) \n",
                     "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-10-year-substate-r-das-nsduh-2002-2011-nid13609"
-                }
-            ]
+                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
                 },
                 {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
-            "bureauCode": [
-                "009:20"
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mwk9-wnfr",
             "issued": "2020-07-22",
-            "temporal": "2020-01-01/2020-07-28",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
             "keyword": [
                 "age",
                 "age group",
@@ -100066,79 +100092,34 @@
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
-            "identifier": "https://data.cdc.gov/api/views/mwk9-wnfr",
-            "description": "Cumulative provisional counts of deaths sex, race/Hispanic origin, age group, and by select underlying causes of death.  The dataset also includes provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.  Includes deaths that occurred between January 1, 2020 to July 28, 2020.",
-            "title": "AH Cumulative Provisional COVID-19 Deaths by Sex, Race, and Age from 1/1/2020 to 7/28/2020",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-01",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2020-01-01/2020-07-28",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Cumulative Provisional COVID-19 Deaths by Sex, Race, and Age from 1/1/2020 to 7/28/2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/h28b-t43q",
             "bureauCode": [
                 "009:032"
             ],
-            "issued": "2018-08-01",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-27",
-            "keyword": [
-                "environmental health",
-                "skin cancer",
-                "solar radiation",
-                "ultraviolet"
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
-            "identifier": "https://data.cdc.gov/api/views/h28b-t43q",
             "description": "This dataset provides data at the county level for the contiguous United States. It includes daily Ozone Monitoring Instrument (OMI) Population-Weighted Ultraviolet (UV) irradiance data from October 2004-2015 provided by the Environmental Remote Sensing group at the Rollins School of Public Health at Emory University. Please refer to the metadata attachment for more information.\r\n\r\nThese data are used by the CDC's National Environmental Public Health Tracking Network to generate sunlight and UV measures. Learn more about sunlight and UV on the Tracking Network's website: https://ephtracking.cdc.gov/showUVLanding.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking. \r\n\r\nProblems or Questions? \r\nEmail trackingsupport@cdc.gov.",
-            "title": "Population-Weighted Ultraviolet Irradiance, 2004-2015",
-            "programCode": [
-                "009:20"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -100161,53 +100142,51 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/h28b-t43q",
+            "issued": "2018-08-01",
+            "keyword": [
+                "environmental health",
+                "skin cancer",
+                "solar radiation",
+                "ultraviolet"
+            ],
+            "landingPage": "https://data.cdc.gov/d/h28b-t43q",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-11-27",
+            "programCode": [
+                "009:20"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Environmental Health & Toxicology"
-            ]
+            ],
+            "title": "Population-Weighted Ultraviolet Irradiance, 2004-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/provider-of-services-file-clinical-laboratories",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2011-10-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-16",
-            "references": [
-                "https://data.cms.gov/resources/provider-of-services-file-methodology"
-            ],
-            "keyword": [
-                "all other provider care types",
-                "health care use & payments",
-                "medicare",
-                "medicare advantage",
-                "original medicare"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "QIESData - CCSQ",
                 "hasEmail": "mailto:QIESData@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/d3eb38ac-d8e9-40d3-b7b7-6205d3d1dc16/data-viewer",
-            "description": "The Provider of Services (POS) Clinical Laboratories (CLIA) data provides information on CLIA demographics and types of testing services the facility provides. In this file you will find provider number, name, address and characteristics of the participating institution providers.",
-            "title": "Provider of Services File - Clinical Laboratories",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-07/50eacc07-7930-4e62-97e3-e04a2dc1e2a3/P.QWB.POSQ.CLIA.LAYOUT.MAR23.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Provider of Services (POS) Clinical Laboratories (CLIA) data provides information on CLIA demographics and types of testing services the facility provides. In this file you will find provider number, name, address and characteristics of the participating institution providers.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d3eb38ac-d8e9-40d3-b7b7-6205d3d1dc16/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d3eb38ac-d8e9-40d3-b7b7-6205d3d1dc16/data",
+                    "mediaType": "text/html",
                     "title": "Provider of Services File - Clinical Laboratories : 2024-12-01"
                 },
                 {
@@ -100595,28 +100574,60 @@
                     "title": "Provider of Services File - Clinical Laboratories : 2011-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2023-07/50eacc07-7930-4e62-97e3-e04a2dc1e2a3/P.QWB.POSQ.CLIA.LAYOUT.MAR23.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/d3eb38ac-d8e9-40d3-b7b7-6205d3d1dc16/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "all other provider care types",
+                "health care use & payments",
+                "medicare",
+                "medicare advantage",
+                "original medicare"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/provider-of-services-file-clinical-laboratories",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2025-01-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/provider-of-services-file-methodology"
+            ],
+            "temporal": "2011-10-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Provider of Services File - Clinical Laboratories"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/vt72-wepb",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS6-technical-documentation.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The sixth round of RANDS (RANDS 6) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from August 10, 2022 to August 29, 2022. RANDS 6 contained the embedded probe questions and experiments as in previous rounds of RANDS. It also explored different administrations of questions asked on the National Survey of Family Growth (NSFG) through split-sample experiments. RANDS 6 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/vt72-wepb",
             "issued": "2023-02-22",
-            "@type": "dcat:Dataset",
-            "temporal": "2022",
-            "modified": "2023-04-20",
             "keyword": [
                 "birth control",
                 "cervical cancer screening",
@@ -100628,60 +100639,36 @@
                 "sex education",
                 "sexual identity"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/vt72-wepb",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-04-20",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/vt72-wepb",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The sixth round of RANDS (RANDS 6) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from August 10, 2022 to August 29, 2022. RANDS 6 contained the embedded probe questions and experiments as in previous rounds of RANDS. It also explored different administrations of questions asked on the National Survey of Family Growth (NSFG) through split-sample experiments. RANDS 6 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
-            "title": "NCHS Research and Development Survey (RANDS) Round 6 Restricted File",
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
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS6-technical-documentation.pdf",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "2022",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 6 Restricted File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/jgkt-w9bh",
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
-            "identifier": "https://data.cdc.gov/api/views/jgkt-w9bh",
             "description": "Air pollution serves as a major risk factor for the development of asthma, respiratory disease and heart disease. Diesel particulate and fumes are a major contributor to air pollution. Workers in a number of different occupations, including mining, oil and gas exploration and refining, and drivers of heavy equipment who are regularly exposed to diesel exhaust while on the job, and persons living in areas with high levels of air pollution, are at an increased risk for developing asthma, cardiovascular disease and certain cancers.\n\nUnderstanding the physiological and cellular effects of diesel exhaust inhalation on Various organs in the body is critical for identifying exposure-induced biological and physiological markers of disease or dysfunction. The experiments in this manuscript, focus on the effects of diesel exhaust (DE) inhalation on peripheral and cardiovascular function. In the current studies, we hypothesized that the development of cardiovascular disease in workers regularly exposed to DE is the result of the inhalation of volatile gases and particulate within the vapor that affect the cardiovascular system by altering physiological and cellular processes that affect peripheral vascular responsiveness to agents that cause blood vessels to constrict and vessels that cause blood vessels to dilate, blood pressure, cardiac output and kidney function (kidney function as it may contribute to changes in blood pressure). We also predicted that these changes in physiology would be associated with changes in the expression of proteins and the production of genes that play a role in regulating oxidative stress, responses to decreases in oxygen, and markers of kidney function that are associated with blood pressure.",
-            "title": "The effects of diesel exhaust inhalation on cardiovascular function",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -100689,47 +100676,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/jgkt-w9bh",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/jgkt-w9bh",
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
+            "title": "The effects of diesel exhaust inhalation on cardiovascular function"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ar8q-3jhn",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-11-04",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-01-01/2022-03-31",
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
-            "identifier": "https://data.cdc.gov/api/views/ar8q-3jhn",
             "description": "CDC is collaborating with Vitalant Research Institute, American Red Cross, and Westat Inc. to conduct a nationwide COVID-19 seroprevalence survey of blood donors. De-identified blood samples are tested for antibodies to SARS-CoV-2 to better understand the percentage of people in the United States who have antibodies against SARS-CoV-2 (the virus that causes COVID-19) and to track how this percentage changes over time. Both SARS-CoV-2 infection and COVID-19 vaccines currently used in the United States result in production of anti-spike (anti-S) antibodies but only infection results in production of anti-nucleocapsid (anti-N) antibodies.\nInfection-induced seroprevalence estimates the proportion of the population with antibody evidence of previous SARS-CoV-2 infection and refers to the percent of the population with anti-nucleocapsid antibodies.\nCombined infection-Induced and Vaccination-Induced seroprevalence estimates the proportion of the population with antibody evidence of previous SARS-CoV-2 infection, COVID-19 vaccination, or both, and refers to the percent of the population that has anti-spike antibodies, anti-nucleocapsid antibodies, or both.\n\nThis link connects to a webpage that displays the data from the Nationwide Blood Donor Seroprevalence Survey. It offers an interactive visualization available at https://covid.cdc.gov/covid-data-tracker/#nationwide-blood-donor-seroprevalence-2022",
-            "title": "2022\u20132023 Nationwide Blood Donor Seroprevalence Survey Combined Infection- and Vaccination-Induced Seroprevalence Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -100752,37 +100728,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/ar8q-3jhn",
+            "issued": "2022-11-04",
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
+            "landingPage": "https://data.cdc.gov/d/ar8q-3jhn",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
+            "temporal": "2022-01-01/2022-03-31",
             "theme": [
                 "Laboratory Surveillance"
-            ]
+            ],
+            "title": "2022\u20132023 Nationwide Blood Donor Seroprevalence Survey Combined Infection- and Vaccination-Induced Seroprevalence Estimates"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -100805,64 +100792,90 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/7vg3-e5u2",
+            "issued": "2023-01-25",
+            "landingPage": "https://data.cdc.gov/d/7vg3-e5u2",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-01-25",
+            "programCode": [
+                "009:030"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "county-level ASD prevalence estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/muvx-39qu",
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
-            "identifier": "c25ba6cf-541c-5090-9a4f-88f686bab55e",
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
+            "identifier": "c25ba6cf-541c-5090-9a4f-88f686bab55e",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/muvx-39qu",
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
-            "landingPage": "https://healthdata.gov/dataset/medicare-appeals-council-decisions-0",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.hhs.gov/dab/divisions/medicareoperations/macdecisions/mac_decisions.html#overpayment_claims",
+            "description": "<p>Decisions of the Departmental Appeals Board's Medicare Appeals Council involving claims for entitlement to Medicare and individual claims for Medicare coverage and payment filed by beneficiaries or health care providers/suppliers.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.hhs.gov/dab/divisions/medicareoperations/macdecisions/mac_decisions.html#overpayment_claims",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "92cece16-e224-4a1d-92ae-d48f2b18bfb3",
             "issued": "2012-05-30",
-            "temporal": "2003-06-11T00:00:00-04:00/2003-06-11T00:00:00-04:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "administrative",
                 "adopt",
@@ -100942,48 +100955,48 @@
                 "supplier",
                 "surgery"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/medicare-appeals-council-decisions-0",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:111"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "92cece16-e224-4a1d-92ae-d48f2b18bfb3",
-            "description": "<p>Decisions of the Departmental Appeals Board's Medicare Appeals Council involving claims for entitlement to Medicare and individual claims for Medicare coverage and payment filed by beneficiaries or health care providers/suppliers.</p>",
-            "title": "Medicare Appeals Council Decisions",
-            "programCode": [
-                "009:111"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.hhs.gov/dab/divisions/medicareoperations/macdecisions/mac_decisions.html#overpayment_claims",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://www.hhs.gov/dab/divisions/medicareoperations/macdecisions/mac_decisions.html#overpayment_claims",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "2003-06-11T00:00:00-04:00/2003-06-11T00:00:00-04:00",
             "theme": [
                 "Health",
                 "Medicare",
                 "Hospital"
-            ]
+            ],
+            "title": "Medicare Appeals Council Decisions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-cancer-statistics",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/cancer.html",
+            "description": "<p>The United States Cancer Statistics (USCS) online databases in WONDER provide cancer incidence and mortality data for the United States for the years since 1999, by year, state and metropolitan areas (MSA), age group, race, ethnicity,  gender, childhood cancer classifications and cancer site. Report case counts, deaths, crude and age-adjusted incidence and death rates,  and 95% confidence intervals  for rates.  The USCS  data are the official federal statistics on cancer incidence from registries having high-quality data and cancer mortality statistics for 50 states and the District of Columbia. USCS are produced by the Centers for Disease Control and Prevention (CDC) and the National Cancer Institute (NCI), in collaboration with the North American Association of Central Cancer Registries (NAACCR). Mortality data are provided by the Centers for Disease Control and Prevention (CDC), National Center for Health Statistics (NCHS), National Vital Statistics System  (NVSS).</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/cancer.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "c935e71d-c2b5-4736-876a-e0abaddc1684",
             "issued": "2012-05-30",
-            "temporal": "1999-01-01T00:00:00-05:00/2006-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "age",
                 "cancer",
@@ -101000,70 +101013,34 @@
                 "state",
                 "year"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-cancer-statistics",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:047"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "c935e71d-c2b5-4736-876a-e0abaddc1684",
-            "description": "<p>The United States Cancer Statistics (USCS) online databases in WONDER provide cancer incidence and mortality data for the United States for the years since 1999, by year, state and metropolitan areas (MSA), age group, race, ethnicity,  gender, childhood cancer classifications and cancer site. Report case counts, deaths, crude and age-adjusted incidence and death rates,  and 95% confidence intervals  for rates.  The USCS  data are the official federal statistics on cancer incidence from registries having high-quality data and cancer mortality statistics for 50 states and the District of Columbia. USCS are produced by the Centers for Disease Control and Prevention (CDC) and the National Cancer Institute (NCI), in collaboration with the North American Association of Central Cancer Registries (NAACCR). Mortality data are provided by the Centers for Disease Control and Prevention (CDC), National Center for Health Statistics (NCHS), National Vital Statistics System  (NVSS).</p>",
-            "title": "CDC WONDER: Cancer Statistics",
-            "programCode": [
-                "009:047"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://wonder.cdc.gov/cancer.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://wonder.cdc.gov/cancer.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1999-01-01T00:00:00-05:00/2006-12-31T00:00:00-05:00",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Cancer Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/g3c9-wbme",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/g3c9-wbme",
             "description": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101086,68 +101063,103 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/g3c9-wbme",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "confirmed",
+                "nedss",
+                "netss",
+                "nndss",
+                "probable",
+                "vibriosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/g3c9-wbme",
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
+            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mw6v-khw2",
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
-            "identifier": "3b56f633-6976-505f-89e4-31d04b742b50",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard MEASURE_VALUE v0.3.58-test (local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.58-test/20230728/MEASURE_VALUE.csv",
-                    "description": "Scorecard MEASURE_VALUE v0.3.58-test (local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard MEASURE_VALUE v0.3.58-test (local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.58-test/20230728/MEASURE_VALUE.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard MEASURE_VALUE v0.3.58-test (local)"
                 }
             ],
+            "identifier": "3b56f633-6976-505f-89e4-31d04b742b50",
+            "issued": "2023-08-10",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/mw6v-khw2",
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
+            "title": "Scorecard MEASURE_VALUE v0.3.58-test (local)"
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
@@ -101158,68 +101170,36 @@
                 "restricted",
                 "visit characteristics"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:ambcare@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/ahcd/ahcd_questionnaires.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-11-21",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
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
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
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
-            "landingPage": "https://www.ncbi.nlm.nih.gov/snp/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "api",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/x4yw-gnzq",
             "description": "Database of Short Genetic Variations (dbSNP) contains human single nucleotide variations, microsatellites, and small-scale insertions and deletions along with publication, population frequency, molecular consequence, and genomic and RefSeq mapping information for both common variations and clinical mutations.",
-            "title": "Database of Short Genetic Variations (dbSNP)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101240,45 +101220,42 @@
                     "title": "Access dbSNP via E-Utilities API"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/x4yw-gnzq",
+            "issued": "2021-06-17",
+            "keyword": [
+                "api",
+                "dataset",
+                "genetics",
+                "genomics",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/snp/",
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
+            "title": "Database of Short Genetic Variations (dbSNP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4y34-2pku",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "keyword": [
-                "2016",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4y34-2pku",
             "description": "NNDSS - Table II. Babesiosis to Campylobacteriosis - 2016. In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.   NP:  Nationally notifiable but not published.   Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n* Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions.",
-            "title": "NNDSS - Table II. Babesiosis to Campylobacteriosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101301,41 +101278,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4y34-2pku",
+            "issued": "2017-01-05",
+            "keyword": [
+                "2016",
+                "babesiosis",
+                "campylobacteriosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/4y34-2pku",
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
+            "title": "NNDSS - Table II. Babesiosis to Campylobacteriosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mxg9-r7sq",
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
-            "identifier": "bb4936ea-8adf-41a5-882b-786a0b3a8822",
             "description": "This table presents beneficiaries who received at least one behavioral health service, by behavioral health condition, 2017-2021.\r\n\r\nSome states have serious data quality issues, making the data unusable for identifying this population. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional, Gender, Age, Zip code, Race and ethnicity, Eligibility group code, Enrollment in CMC Plans. \r\n\r\nData from Maryland, Tennessee, and Utah are omitted for the tables due to data quality concerns. Maryland was excluded in 2017 due to unusable diagnosis codes in the IP file and the OT file. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2020. In addition, states with a high data quality concern on one or more measures are noted in the table in the \"Data Quality\" column. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Beneficiaries receiving a behavioral health service by behavioral health condition, 2017-2021",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101344,22 +101326,66 @@
                     "title": "Beneficiaries receiving a behavioral health service by behavioral health condition, 2017-2021"
                 }
             ],
+            "identifier": "bb4936ea-8adf-41a5-882b-786a0b3a8822",
+            "issued": "2023-03-28",
+            "keyword": [
+                "behavioral health care",
+                "chip",
+                "integrated care",
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/mxg9-r7sq",
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
+            "title": "Beneficiaries receiving a behavioral health service by behavioral health condition, 2017-2021"
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
+            "description": "Final counts of deaths by the week the deaths occurred, by state of occurrence, and by select causes of death for 2014-2019.  Death counts in this dataset were derived from the National Vital Statistics System database that provides the most timely access to the data.  Therefore, counts may differ slightly from final data due to differences in processing, recoding, and imputation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3yf8-kanr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3yf8-kanr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3yf8-kanr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3yf8-kanr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/3yf8-kanr",
             "issued": "2020-04-21",
-            "@type": "dcat:Dataset",
-            "temporal": "2014-01-01/2019-12-31",
-            "modified": "2022-04-01",
             "keyword": [
                 "all causes",
                 "alzheimer disease",
@@ -101384,125 +101410,84 @@
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/3yf8-kanr",
-            "description": "Final counts of deaths by the week the deaths occurred, by state of occurrence, and by select causes of death for 2014-2019.  Death counts in this dataset were derived from the National Vital Statistics System database that provides the most timely access to the data.  Therefore, counts may differ slightly from final data due to differences in processing, recoding, and imputation.",
-            "title": "Weekly Counts of Deaths by State and Select Causes, 2014-2019",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-01",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/3yf8-kanr/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/3yf8-kanr/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/3yf8-kanr/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/3yf8-kanr/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2014-01-01/2019-12-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Weekly Counts of Deaths by State and Select Causes, 2014-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mxsq-ivys",
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
-            "identifier": "f1c9d3a8-f9e8-556d-a9ea-fe31a38037ff",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_fileType_measureDisplayGroups",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/fileType_measureDisplayGroups.csv",
-                    "description": "{\"dataset\": \"fileType_measureDisplayGroups\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"fileType_measureDisplayGroups\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/fileType_measureDisplayGroups.csv",
+                    "mediaType": "text/csv",
                     "title": "fileType_measureDisplayGroups csv file"
                 }
             ],
+            "identifier": "f1c9d3a8-f9e8-556d-a9ea-fe31a38037ff",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/mxsq-ivys",
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
+            "title": "featAuto_fileType_measureDisplayGroups"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/mxu9-jhjc",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-24",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-23",
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
-            "identifier": "789babe6-36f6-4023-bf8d-b4fcc6313b11",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-16-to-2023-10-22",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101511,52 +101496,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-16-to-2023-10-22"
                 }
             ],
+            "identifier": "789babe6-36f6-4023-bf8d-b4fcc6313b11",
+            "issued": "2023-10-24",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/mxu9-jhjc",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-10-23",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-16-to-2023-10-22"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/index.htm",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-05-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-12-29/2025-01-16",
-            "modified": "2025-01-30",
-            "keyword": [
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "influenza",
-                "monthly",
-                "mortality",
-                "nchs",
-                "nvss",
-                "pneumonia",
-                "provisional",
-                "puerto rico",
-                "state",
-                "united states",
-                "weekly",
-                "yearly"
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
-            "identifier": "https://data.cdc.gov/api/views/r8kw-7aab",
             "description": "Effective September 27, 2023, this dataset will be updated weekly on Thursdays.\n\nDeaths involving COVID-19, pneumonia, and influenza reported to NCHS by week ending date and by state",
-            "title": "Provisional COVID-19 Death Counts by Week Ending Date and State",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101579,41 +101548,55 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/r8kw-7aab",
+            "issued": "2020-05-01",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "influenza",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "pneumonia",
+                "provisional",
+                "puerto rico",
+                "state",
+                "united states",
+                "weekly",
+                "yearly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/index.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States, Puerto Rico",
+            "temporal": "2019-12-29/2025-01-16",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional COVID-19 Death Counts by Week Ending Date and State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://submit.ncbi.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-03-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "biotechnology",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/iwfp-ktt7",
             "description": "A single entry point for users to link to and find information about data submission processes at NCBI.",
-            "title": "NCBI Submission Portal",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101622,42 +101605,39 @@
                     "title": "NCBI Submission Portal"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/iwfp-ktt7",
+            "issued": "2022-03-02",
+            "keyword": [
+                "biotechnology",
+                "tools & utilities"
+            ],
+            "landingPage": "https://submit.ncbi.nlm.nih.gov/",
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
                 "Research"
-            ]
+            ],
+            "title": "NCBI Submission Portal"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/jxu8-x79m",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-16",
-            "keyword": [
-                "brfss",
-                "cigarette smoking",
-                "dashboard",
-                "disparities",
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
-            "identifier": "https://data.cdc.gov/api/views/jxu8-x79m",
             "description": "2011\u20132023. The tobacco disparities dashboard data utilized the Behavioral Risk Factor Surveillance System (BRFSS) data to measure cigarette smoking disparities by age, disability, education, employment, income, mental health status, race and ethnicity, sex, and urban-rural status. The disparity value is the relative difference in the cigarette smoking prevalence among adults 18 and older in a focus group divided by the cigarette smoking prevalence among adults 18 and older in a reference group. A disparity value above 1 indicates that adults in the focus group smoke cigarettes at a higher rate, as reflected by the disparity value, compared with the rate among adults in the reference group who smoke cigarettes. A disparity value below 1 indicates that adults in the focus group smoke cigarettes at a lower rate, as reflected by the disparity value, compared with the rate among adults in the reference group who smoke cigarettes. A disparity value of 1 means there is no relative difference in the rate of adults who smoke cigarettes for the two groups compared.",
-            "title": "State Tobacco Related Disparities Dashboard Data",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101680,43 +101660,43 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/jxu8-x79m",
+            "issued": "2024-04-24",
+            "keyword": [
+                "brfss",
+                "cigarette smoking",
+                "dashboard",
+                "disparities",
+                "tobacco"
+            ],
+            "landingPage": "https://data.cdc.gov/d/jxu8-x79m",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2025-01-16",
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
+            "title": "State Tobacco Related Disparities Dashboard Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-10",
-            "keyword": [
-                "e-cigarette",
-                "legislation",
-                "osh",
-                "policy",
-                "smokefree campus",
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
-            "identifier": "https://data.cdc.gov/api/views/itia-u6fu",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Smokefree/itia-u6fu",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  E-Cigarette Legislation\u2014Smokefree Campus. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include state smokefree indoor air laws for smokefree campuses in private and public colleges and schools (K-12).",
-            "title": "CDC STATE System E-Cigarette Legislation - Smokefree Campus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101739,36 +101719,43 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Smokefree/itia-u6fu",
+            "identifier": "https://data.cdc.gov/api/views/itia-u6fu",
+            "issued": "2023-07-19",
+            "keyword": [
+                "e-cigarette",
+                "legislation",
+                "osh",
+                "policy",
+                "smokefree campus",
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
+            "title": "CDC STATE System E-Cigarette Legislation - Smokefree Campus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/iudi-d4pc",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "TMBB/HELD",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/iudi-d4pc",
             "description": "Fibrogenic carbon nanotubes (CNTs) induce the polarization of M1 and M2 macrophages in mouse lungs. Polarization of the macrophages regulates the production of proinflammatory and pro-resolving lipid mediators (LMs) to mediate acute inflammation and its resolution in a time-dependent manner. Here we examined the molecular mechanism by which multi-walled CNTs (MWCNTs, Mitsui-7) induce M1 polarization in vitro. Treatment of murine macrophages (J774A.1) with Mitsui-7 MWCNTs increased the expression of Alox5 mRNA and protein in a concentration- and time-dependent manner. The MWCNTs induced the expression of CD68, and that induction persisted for up to 3 days post-exposure. The expression and activity of inducible nitric oxide synthase, an intracellular marker of M1, were increased by MWCNTs. Consistent with M1 polarization, the MWCNTs induced the production and secretion of proinflammatory cytokines tumor necrosis factor-\u03b1 and interleukin-1\u03b2, and proinflammatory LMs leukotriene B4 (LTB4) and prostaglandin E2 (PGE2). The cell-free media from MWCNT-polarized macrophages induced the migration of neutrophilic cells (differentiated from HL-60), which was blocked by Acebilustat, a specific leukotriene A4 hydrolase inhibitor, or LY239111, an LTB4 receptor antagonist, but not NS-398, a cyclooxygenase 2 inhibitor, revealing LTB4 as a major mediator of neutrophil chemotaxis from MWCNT-polarized macrophages. Knockdown of Alox5 using specific small hairpin-RNA suppressed MWCNT-induced M1 polarization, LTB4 secretion, and migration of neutrophils. Taken together, these findings demonstrate the polarization of M1 macrophages by Mitsui-7 MWCNTs in vitro and that induction of Alox5 is an important mechanism by which the MWCNTs promote proinflammatory responses by boosting M1 polarization and production of proinflammatory LMs.",
-            "title": "Multi-Walled Carbon Nanotubes Induce Arachidonate 5-Lipoxygenase Expression and Enhance the Polarization and Function of M1 Macrophages in vitro",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101776,49 +101763,38 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/iudi-d4pc",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/iudi-d4pc",
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
+            "title": "Multi-Walled Carbon Nanotubes Induce Arachidonate 5-Lipoxygenase Expression and Enhance the Polarization and Function of M1 Macrophages in vitro"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-advantage-skilled-nursing-facility",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-06-13",
-            "temporal": "2016-01-01/2021-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-16",
-            "references": [
-                "https://data.cms.gov/resources/medicare-service-type-reports-methodology"
-            ],
-            "keyword": [
-                "beneficiary enrollment",
-                "health equity",
-                "hospitals & facilities",
-                "medicare",
-                "medicare advantage",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/81d7cb4c-9e7e-43ab-8858-0a2250291935/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics - Medicare Advantage, Skilled Nursing Facility tables provide utilization data for skilled nursing facilities, by Medicare Advantage beneficiaries.\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. \u00a0Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\n\n\tMDCR SNF MA 1. \u00a0Medicare Skilled Nursing Facilities: Utilization for Medicare Advantage Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR SNF MA 2. \u00a0Medicare Skilled Nursing Facilities: Utilization for Medicare Advantage Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR SNF MA 3. \u00a0Medicare Skilled Nursing Facilities: Utilization for Medicare Advantage Beneficiaries, by Area of Residence",
-            "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101857,55 +101833,53 @@
                     "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility : 2016-12-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/81d7cb4c-9e7e-43ab-8858-0a2250291935/data-viewer",
+            "issued": "2023-06-13",
+            "keyword": [
+                "beneficiary enrollment",
+                "health equity",
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-advantage-skilled-nursing-facility",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-05-16",
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
+            "temporal": "2016-01-01/2021-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/provisional-tables.htm",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2017-07-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-01-01/2024-06-30",
-            "modified": "2024-12-11",
-            "keyword": [
-                "birth",
-                "deaths",
-                "monthly",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "puerto rico",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hmz2-vwda",
             "description": "NOTES: Figures include all revisions received from the states and, therefore, may differ from those previously published. Data are provisional and are subject to monthly reporting variation. National data are calculated by summing the number of events reported by state of residence; counts are rounded to the nearest thousand (births and deaths) or hundred (infant deaths). Provisional counts may differ by approximately 2% from final counts, due to rounding and reporting variation. Additionally, the accuracy of the provisional counts may change over time. Data are estimates by state of residence. For discussion of the nature, source, and limitations of the data, see \"Technical Notes\" of the report, Births, Marriages, Divorces, and Deaths: Provisional Data for 2009. Available from URL: http://www.cdc.gov/nchs/data/nvsr/nvsr58/nvsr58_25.htm. Final counts of births, deaths, and infant deaths for previous years can be obtained from http://wonder.cdc.gov.\r\n\r\nSOURCE: Provisional data from the National Vital Statistics System, National Center for Health Statistics, CDC.",
-            "title": "VSRR - State and National Provisional Counts for Live Births, Deaths, and Infant Deaths",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101928,47 +101902,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/hmz2-vwda",
+            "issued": "2017-07-20",
+            "keyword": [
+                "birth",
+                "deaths",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "puerto rico",
+                "state",
+                "united states",
+                "vsrr"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/provisional-tables.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-12-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2023-01-01/2024-06-30",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "VSRR - State and National Provisional Counts for Live Births, Deaths, and Infant Deaths"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/qbrk-85z2",
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
-            "identifier": "https://data.cdc.gov/api/views/qbrk-85z2",
             "description": "NNDSS - TABLE 1II. Tetanus to Trichinellosis \u2013 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101991,42 +101968,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qbrk-85z2",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "nedss",
+                "netss",
+                "nndss",
+                "tetanus",
+                "toxic shock syndrome (other than streptococcal)",
+                "trichinellosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/qbrk-85z2",
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
+            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/v5qq-ktfc",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-05-22",
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
-            "identifier": "https://data.cdc.gov/api/views/v5qq-ktfc",
             "description": "This dataset provides modeled predictions of PM2.5 levels from the EPA's Downscaler model. Data are at the census tract level for 2001-2005. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\n\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\n\nBy using these data, you signify your agreement to comply with the following requirements:\n1. Use the data for statistical reporting and analysis only.\n2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals.\n3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov.\n4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.\n5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC.\n6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2001-2005",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -102049,50 +102029,43 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/v5qq-ktfc",
+            "issued": "2020-05-22",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "particulate matter",
+                "pm2.5"
+            ],
+            "landingPage": "https://data.cdc.gov/d/v5qq-ktfc",
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
+            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2001-2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/39z2-9zu6",
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
-            "identifier": "https://data.cdc.gov/api/views/39z2-9zu6",
             "description": "<b>Note:</b> After May 3, 2024, this dataset will no longer be updated because hospitals are no longer required to report data on COVID-19 hospital admissions, and hospital capacity and occupancy data, to HHS through CDC\u2019s National Healthcare Safety Network. The related CDC COVID Data Tracker site was revised or retired on May 10, 2023.\n\nThis dataset represents daily COVID-19 hospitalization data and metrics aggregated to national, state/territory, and regional levels. COVID-19 hospitalization data are reported to CDC\u2019s National Healthcare Safety Network, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN and included in this dataset represent aggregated counts and include metrics capturing information specific to COVID-19 hospital admissions, and inpatient and ICU bed capacity occupancy.\n\n<b>Reporting information:</b><ul><li>As of December 15, 2022, COVID-19 hospital data are required to be reported to NHSN, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Prior to December 15, 2022, hospitals reported data directly to the U.S. Department of Health and Human Services (HHS) or via a state submission for collection in the HHS Unified Hospital Data Surveillance System (UHDSS).</li><li>While CDC reviews these data for errors and corrects those found, some reporting errors might still exist within the data. To minimize errors and inconsistencies in data reported, CDC removes outliers before calculating the metrics. CDC and partners work with reporters to correct these errors and update the data in subsequent weeks.</li><li>Many hospital subtypes, including acute care and critical access hospitals, as well as Veterans Administration, Defense Health Agency, and Indian Health Service hospitals, are included in the metric calculations provided in this report. Psychiatric, rehabilitation, and religious non-medical hospital types are excluded from calculations.</li><li>Data are aggregated and displayed for hospitals with the same Centers for Medicare and Medicaid Services (CMS) Certification Number (CCN), which are assigned by CMS to counties based on the CMS Provider of Services files.</li><li>Full details on COVID-19 hospital data reporting guidance can be found here: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf</li></ul>\n\n<b>Metric details:</b><ul><li><b>Time Period:</b> timeseries data will update weekly on Mondays as soon as they are reviewed and verified, usually before 8 pm ET. Updates will occur the following day when reporting coincides with a federal holiday. Note: Weekly updates might be delayed due to delays in reporting. All data are provisional. Because these provisional counts are subject to change, including updates to data reported previously, adjustments can occur. Data may be updated since original publication due to delays in reporting (to account for data received after a given Thursday publication) or data quality corrections.</li><li><b>New COVID-19 Hospital Admissions (count):</b> Number of new admissions of patients with laboratory-confirmed COVID-19 in the previous week (including both adult and pediatric admissions) in the entire jurisdiction.</li><li><b>New COVID-19 Hospital Admissions (7-Day Average):</b> 7-day average of new admissions of patients with laboratory-confirmed COVID-19 in the previous week (including both adult and pediatric admissions) in the entire jurisdiction.</li><li><b>Cumulative COVID-19 Hospital Admissions:</b> Cumulative total number of admissions of patients with laborat",
-            "title": "United States COVID-19 Hospitalization Metrics by Jurisdiction, Timeseries \u2013 ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -102115,52 +102088,60 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/39z2-9zu6",
+            "issued": "2023-07-06",
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
+            "landingPage": "https://data.cdc.gov/d/39z2-9zu6",
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
+                "CDT aggregate hospital data displays: https://covid.cdc.gov/covid-data-tracker/#cases_new-admissions-rate-state CDT Hospitalizations Landing Page: https://covid.cdc.gov/covid-data-tracker/#hospitalizations-landing NHSN Hospital Data Reporting: https://www.cdc.gov/nhsn/covid19/hospital-reporting.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fnhsn%2Fcovid19%2Ftransition.html  Full reporting guidance: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf"
+            ],
+            "rights": "N/A",
+            "spatial": "US",
+            "temporal": "8/1/2020 - 5/3/2024",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "United States COVID-19 Hospitalization Metrics by Jurisdiction, Timeseries \u2013 ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/order-and-referring",
+            "accrualPeriodicity": "R/P3.5D",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2023-05-21/2025-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
-            "references": [
-                "https://data.cms.gov/resources/order-and-referring-methodology"
-            ],
-            "keyword": [
-                "medicare",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/c99b5865-1119-4436-bb80-c5af2773ea1f/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/order-and-referring-data-dictionary",
             "description": "The Order and Referring dataset provides information on all physicians and non-physician practitioners, by their National Provider Identifier (NPI), who are of a type/specialty that is legally eligible to order and refer in the Medicare program and who have current enrollment records in Medicare.\u00a0\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Order and Referring",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c99b5865-1119-4436-bb80-c5af2773ea1f/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c99b5865-1119-4436-bb80-c5af2773ea1f/data",
+                    "mediaType": "text/html",
                     "title": "Order and Referring : 2025-01-21"
                 },
                 {
@@ -104216,60 +104197,49 @@
                     "title": "Order and Referring : 2023-06-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/order-and-referring-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/c99b5865-1119-4436-bb80-c5af2773ea1f/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/order-and-referring",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3.5D",
+            "modified": "2025-01-21",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/order-and-referring-methodology"
+            ],
+            "temporal": "2023-05-21/2025-01-18",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Order and Referring"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ua7e-t2fy",
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
-            "identifier": "https://data.cdc.gov/api/views/ua7e-t2fy",
+            "describedBy": "N/A",
             "description": "This dataset represents weekly hospital respiratory data and metrics aggregated to national and state/territory levels reported to CDC\u2019s National Health Safety Network (NHSN) beginning August 2020. Data for reporting dates through April 30, 2024 represent data reported during a previous mandated reporting period as specified by the HHS Secretary. Data for reporting dates May 1, 2024 \u2013 October 31, 2024 represent voluntarily reported data in the absence of a mandate. Data for reporting dates beginning November 1, 2024 represent data reported during a current mandated reporting period. All data and metrics capturing information on respiratory syncytial virus (RSV) were voluntarily reported until November 1, 2024. All data included in this dataset represent aggregated counts, and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and new hospital admissions with corresponding metrics indicating reporting coverage for a given reporting week. NHSN monitors national and local trends in healthcare system stress and capacity for all acute care and critical access hospitals in the United States.\n\nFor more information on the reporting mandate per the Centers for Medicare and Medicaid Services (CMS) requirements, visit: <a href=\"https://www.cms.gov/medicare/health-safety-standards/quality-safety-oversight-general-information/policy-memos-states/updates-condition-participation-cop-requirements-hospitals-and-critical-access-hospitals-cahs-report\">Updates to the Condition of Participation (CoP) Requirements for Hospitals and Critical Access Hospitals (CAHs) To Report Acute Respiratory Illnesses</a>.\n\nFor more information regarding NHSN\u2019s collection of these data, including full reporting guidance, visit: <a href=\"https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html\">NHSN Hospital Respiratory Data.</a>\n\n<b>Source: CDC National Healthcare Safety Network (NHSN).</b>\n<ul><li><b>Data source description</b> (updated November 15, 2024): As of October 9, 2024, Hospital Respiratory Data (HRD; formerly Respiratory Pathogen, Hospital Capacity, and Supply data or 'COVID-19 hospital data') are reported to HHS through CDC's National Healthcare Safety Network (NHSN) based on updated requirements from the Centers for Medicare and Medicaid Services (CMS). These data were voluntarily reported to NHSN May 1, 2024 until November 1, 2024, at which time CMS began requiring acute care and critical access hospitals to electronically report information via NHSN about COVID-19, influenza, and RSV, hospital bed census and capacity. Hospital bed capacity and occupancy data for all patients and for patients with COVID-19 or influenza for collection dates prior to May 1, 2024, represent data reported during a previously mandated reporting period as specified by the HHS Secretary, and data for collection dates May 1, 2024 \u2013 October 31, 2024 represent data reported voluntarily to NHSN. All RSV data through October 31, 2024 represent voluntarily reported data; as such, all voluntarily reported data included in this dataset represent reporting hospitals only for a given week and might not be complete or representative of all hospitals during the specified reporting periods.</li><li>NHSN monitors national and local trends in healthcare system stress and capacity for all acute care and critical access hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Find more information about reporting to NHSN: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html.</li><li><b>Data quality:</b> While CDC reviews reported data for completeness and errors and corrects those found, some reporting errors might still exist within the data. CDC and partners work with reporters to correct these errors and update the data in subsequent weeks. Data reported as of December",
-            "title": "Weekly Hospital Respiratory Data (HRD) Metrics by Jurisdiction, National Healthcare Safety Network (NHSN)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -104292,56 +104262,59 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
-            "describedBy": "N/A",
+            "identifier": "https://data.cdc.gov/api/views/ua7e-t2fy",
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
+            "landingPage": "https://data.cdc.gov/d/ua7e-t2fy",
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
+            "title": "Weekly Hospital Respiratory Data (HRD) Metrics by Jurisdiction, National Healthcare Safety Network (NHSN)"
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
-            "identifier": "https://data.cdc.gov/api/views/82ci-krud",
             "description": "<b>Note:</b> After May 3, 2024, this dataset will no longer be updated because hospitals are no longer required to report data on COVID-19 hospital admissions, hospital capacity, or occupancy data to HHS through CDC\u2019s National Healthcare Safety Network (NHSN). The related CDC COVID Data Tracker site was revised or retired on May 10, 2023.\n\n<b>Note:</b>\n<b>May 3,2024:</b> Due to incomplete or missing hospital data received for the April 21,2024 through April 27, 2024 reporting period, the COVID-19 Hospital Admissions Level could not be calculated for CNMI and will be reported as \u201cNA\u201d or \u201cNot Available\u201d in the COVID-19 Hospital Admissions Level data released on May 3, 2024.\n\n\nThis dataset represents COVID-19 hospitalization data and metrics aggregated to county or county-equivalent, for all counties or county-equivalents (including territories) in the United States as of the initial date of reporting for each weekly metric. COVID-19 hospitalization data are reported to CDC\u2019s National Healthcare Safety Network, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN and included in this dataset represent aggregated counts and include metrics capturing information specific to COVID-19 hospital admissions, and inpatient and ICU bed capacity occupancy.\n\n<b>Reporting information:</b><ul><li>As of December 15, 2022, COVID-19 hospital data are required to be reported to  NHSN, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Prior to December 15, 2022, hospitals reported data directly to the U.S. Department of Health and Human Services (HHS) or via a state submission for collection in the HHS Unified Hospital Data Surveillance System (UHDSS). </li><li>While CDC reviews these data for errors and corrects those found, some reporting errors might still exist within the data. To minimize errors and inconsistencies in data reported, CDC removes outliers before calculating the metrics. CDC and partners work with reporters to correct these errors and update the data in subsequent weeks.</li><li>Many hospital subtypes, including acute care and critical access hospitals, as well as Veterans Administration, Defense Health Agency, and Indian Health Service hospitals, are included in the metric calculations provided in this report. Psychiatric, rehabilitation, and religious non-medical hospital types are excluded from calculations.  </li><li>Data are aggregated and displayed for hospitals with the same Centers for Medicare and Medicaid Services (CMS) Certification Number (CCN), which are assigned by CMS to counties based on the CMS Provider of Services files. </li> <li>Full details on COVID-19 hospital data reporting guidance can be found here: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf</li></ul>\n<b>Calculation of county-level hospital metrics:</b><ul><li>County-level hospital data are derived using calculations performed at the Health Service Area (HSA) level. An HSA is defined by CDC\u2019s National Center for Health Statistics as a geographic area containing at least one county which is self-contained with respect to the population\u2019s provision of routine hospital care. Every county in the United States is assigned to an HSA, and each HSA must contain at least one hospital. Therefore, use of HSAs in the calculation of local hospital metrics allows for more accurate characterization of the relationship between health care utilization and health status at the local level. </li><li>Data presented at the county-level represent admissions, hosp",
-            "title": "Weekly United States COVID-19 Hospitalization Metrics by County (Historical) \u2013 ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -104364,43 +104337,51 @@
                     "mediaType": "application/xml"
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
+                "inpatient beds"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://data.cdc.gov/d/r3zz-ivb8",
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
-            "identifier": "https://data.cdc.gov/api/views/r3zz-ivb8",
             "description": "This dataset contains deidentified data from the National Malaria Surveillance System on the number of malaria cases reported in the United States in 2016, by county. Only counties reporting five or more cases are included in this dataset.",
-            "title": "Number of Reported Malaria Cases by County\u2014 United States, 2016",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -104423,20 +104404,52 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/r3zz-ivb8",
+            "issued": "2020-07-27",
+            "keyword": [
+                "county",
+                "division of parasitic diseases and malaria",
+                "malaria",
+                "united states"
+            ],
+            "landingPage": "https://data.cdc.gov/d/r3zz-ivb8",
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
+            "title": "Number of Reported Malaria Cases by County\u2014 United States, 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2004-0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) measures the<br />\nprevalence and correlates of drug use in the United States. The<br />\nsurveys are designed to provide quarterly, as well as annual,<br />\nestimates. Information is provided on the use of illicit drugs,<br />\nalcohol, and tobacco among members of United States households aged 12<br />\nand older. Questions included age at first use as well as lifetime,<br />\nannual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovered substance abuse treatment history and perceived need for<br />\ntreatment, and included questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey included questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents were<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2004 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, drug use by friends,<br />\nsocial support, extracurricular activities, exposure to substance<br />\nabuse prevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Several measures<br />\nfocused on prevention-related themes in this section. Also retained<br />\nwere questions on mental health and access to care, perceived risk of<br />\nusing drugs, perceived availability of drugs, driving and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey and retained through the<br />\n2003 survey. Background information includes gender, race, age,<br />\nethnicity, marital status, educational level, job status, veteran<br />\nstatus, and current household composition. In addition, in 2004 Adult and Adolescent Mental Health modules were added.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2004) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2004-nid13548",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2004-nid13548"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2004-nid13548",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -104474,117 +104487,84 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2004-0",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2004-nid13548",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) measures the<br />\nprevalence and correlates of drug use in the United States. The<br />\nsurveys are designed to provide quarterly, as well as annual,<br />\nestimates. Information is provided on the use of illicit drugs,<br />\nalcohol, and tobacco among members of United States households aged 12<br />\nand older. Questions included age at first use as well as lifetime,<br />\nannual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovered substance abuse treatment history and perceived need for<br />\ntreatment, and included questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey included questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents were<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2004 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, drug use by friends,<br />\nsocial support, extracurricular activities, exposure to substance<br />\nabuse prevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Several measures<br />\nfocused on prevention-related themes in this section. Also retained<br />\nwere questions on mental health and access to care, perceived risk of<br />\nusing drugs, perceived availability of drugs, driving and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey and retained through the<br />\n2003 survey. Background information includes gender, race, age,<br />\nethnicity, marital status, educational level, job status, veteran<br />\nstatus, and current household composition. In addition, in 2004 Adult and Adolescent Mental Health modules were added.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health (NSDUH-2004)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2004-nid13548",
-                    "description": "National Survey on Drug Use and Health (NSDUH-2004) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2004-nid13548"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health (NSDUH-2004)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://healthdata.gov/d/n67c-9yeu",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-05-04",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-03",
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
-            "identifier": "8099abf0-ddac-552c-b539-fd623bd17ec2",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard Example",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/pillar.csv",
-                    "description": "Scorecard Example CSV updated at Wed, 03 May 2023 16:00:33 by WN7D",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard Example CSV updated at Wed, 03 May 2023 16:00:33 by WN7D",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard Example CSV"
                 }
             ],
+            "identifier": "8099abf0-ddac-552c-b539-fd623bd17ec2",
+            "issued": "2023-05-04",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/n67c-9yeu",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2023-05-03",
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
+            "title": "Scorecard Example"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/pending-initial-logging-and-tracking-non-physicians",
+            "accrualPeriodicity": "R/P3.5D",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2023-05-21/2025-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
-            "references": [
-                "https://data.cms.gov/resources/pending-initial-logging-and-tracking-physician-and-non-physicians-methodology"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/261b83b6-b89f-43ad-ae7b-0d419a3bc24b/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/pending-initial-logging-and-tracking-physician-and-non-physicians-data-dictionary",
             "description": "The Pending Initial Logging and Tracking\u00a0(L & T) Non Physicians dataset provides a list of pending applications that have not been processed by CMS contractors for Non Physicians.",
-            "title": "Pending Initial Logging and Tracking Non Physicians",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/261b83b6-b89f-43ad-ae7b-0d419a3bc24b/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/261b83b6-b89f-43ad-ae7b-0d419a3bc24b/data",
+                    "mediaType": "text/html",
                     "title": "Pending Initial Logging and Tracking Non Physicians : 2025-01-21"
                 },
                 {
@@ -106652,47 +106632,49 @@
                     "title": "Pending Initial Logging and Tracking Non Physicians : 2023-06-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/pending-initial-logging-and-tracking-physician-and-non-physicians-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/261b83b6-b89f-43ad-ae7b-0d419a3bc24b/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/pending-initial-logging-and-tracking-non-physicians",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3.5D",
+            "modified": "2025-01-21",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/pending-initial-logging-and-tracking-physician-and-non-physicians-methodology"
+            ],
+            "temporal": "2023-05-21/2025-01-18",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Pending Initial Logging and Tracking Non Physicians"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://wwwn.cdc.gov/NHISDataQueryTool/ER_Quarterly/index_quarterly.html",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-06-03",
-            "temporal": "2019-2022",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-09",
-            "keyword": [
-                "early release",
-                "key health indicators",
-                "nhis"
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
-            "identifier": "https://data.cdc.gov/api/views/wpti-gvdi",
             "description": "Interactive Quarterly Early Release Estimates provide health statistics based on data from the 2019-2022 National Health Interview Survey (NHIS) for selected health topics for adults aged 18 years and over. All estimates are unadjusted percentages based on preliminary data files and are released prior to final data editing and final weighting to provide access to the most recent information from the NHIS. Estimates presented here are based on quarterly data. Estimates based on half-year data, with groupings by demographic characteristics, are available in the Interactive Biannual Early Release Estimates. Estimates based on the 1997\u20132018 NHIS can be found in Previous Early Release Reports on Key Health Indicators.",
-            "title": "NHIS Interactive Quarterly Early Release Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106715,42 +106697,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wpti-gvdi",
+            "issued": "2021-06-03",
+            "keyword": [
+                "early release",
+                "key health indicators",
+                "nhis"
+            ],
+            "landingPage": "https://wwwn.cdc.gov/NHISDataQueryTool/ER_Quarterly/index_quarterly.html",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-12-09",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2019-2022",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NHIS Interactive Quarterly Early Release Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/n6ia-x2vv",
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
-            "identifier": "a7cc2aff-8d01-4f68-9ef9-313693f90ce5",
             "description": "This table presents the number of beneficiaries with a delivery, the number of beneficiaries with any SMM condition, and the rate of SMM conditions per 10,000 deliveries, 2017 - 2021.\r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues, making the data unusable for identifying this population. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nData from Maryland, Tennessee, and Utah are omitted from the tables due to data quality concerns. Maryland was excluded in 2017 due to unusable diagnosis codes in the IP file and the OT file. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2020. In addition, states with a high data quality concern on one or more measures are noted in the table in the \"Data Quality\" column. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Number and rate of SMM among Medicaid- and CHIP-covered deliveries, 2017 - 2021",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106759,48 +106741,42 @@
                     "title": "Number and rate of SMM among Medicaid- and CHIP-covered deliveries, 2017 - 2021"
                 }
             ],
+            "identifier": "a7cc2aff-8d01-4f68-9ef9-313693f90ce5",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "maternal health",
+                "medicaid",
+                "pregnancy"
+            ],
```

